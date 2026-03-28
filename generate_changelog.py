"""
Generates per-major-version CHANGELOG.md files by comparing raw LOGID CSVs
between adjacent minor FortiOS versions.
Run from repo root: python3 generate_changelog.py
"""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

MAJOR_RE = re.compile(r'^\d+\.\d+$')
MINOR_RE = re.compile(r'^\d+\.\d+\.\d+$')
@dataclass
class LogidDiff:
    added_fields: list[tuple[str, str, str, str]]    # (name, type, length, desc)
    removed_fields: list[tuple[str, str, str, str]]  # (name, type, length, desc)
    type_changes: dict[str, tuple[str, str]]          # field → (old, new)
    desc_changes: dict[str, tuple[str, str]]          # field → (old, new)
    length_changes: dict[str, tuple[str, str]]        # field → (old, new)
    severity_change: tuple[str, str] | None           # (old, new) or None
    message_desc_change: tuple[str, str] | None       # (old, new) or None
    category_change: tuple[str, str] | None           # (old, new) or None

    def has_changes(self) -> bool:
        return bool(
            self.added_fields or self.removed_fields
            or self.type_changes or self.desc_changes or self.length_changes
            or self.severity_change or self.message_desc_change or self.category_change
        )


@dataclass
class VersionDiff:
    added_logids: dict[str, tuple[str, str]]                    # stem → (dataset_label, extra_val)
    removed_logids: dict[str, tuple[str, str]]                  # stem → (dataset_label, extra_val)
    logid_diffs: dict[str, tuple[str, str, LogidDiff]]          # stem → (dataset_label, extra_val, LogidDiff)
    utmtype_added: set[str]
    utmtype_removed: set[str]

    def has_changes(self) -> bool:
        return bool(
            self.added_logids or self.removed_logids or self.logid_diffs
            or self.utmtype_added or self.utmtype_removed
        )


# Rows for a conflicting field: list of (desc, dtype, length, type_val, category, stems)
_ConflictRows = list[tuple[str, str, str, str, str, list[str]]]


@dataclass
class VersionSnapshot:
    # bucket → field → rows — one row per unique (desc, dtype, length) combo
    # A field is included only if that dimension has >1 distinct value across LOGIDs
    desc_conflicts: dict[str, dict[str, _ConflictRows]]
    type_conflicts: dict[str, dict[str, _ConflictRows]]
    length_conflicts: dict[str, dict[str, _ConflictRows]]


def discover_versions(root: Path) -> list[tuple[str, list[Path]]]:
    """Return sorted list of (major_label, [minor_dirs]) for all versions found under root."""
    result = []
    for entry in sorted(root.iterdir()):
        if not entry.is_dir() or not MAJOR_RE.match(entry.name):
            continue
        minor_dirs = sorted(
            [d for d in entry.iterdir() if d.is_dir() and MINOR_RE.match(d.name)],
            key=lambda d: tuple(int(x) for x in d.name.split('.')),
        )
        result.append((entry.name, minor_dirs))
    return result


def load_version(minor_dir: Path) -> dict[str, pd.DataFrame]:
    """Load all CSV files from a minor version directory, keyed by filename stem."""
    result = {}
    for csv_file in sorted(minor_dir.glob('*.csv')):
        try:
            df = pd.read_csv(csv_file)
            result[csv_file.stem] = df
        except Exception:
            pass
    return result


def classify_dataset(df: pd.DataFrame) -> str:
    """Return dataset label: 'Traffic', 'Event', 'Unknown', or UTM subtype name (including 'GTP')."""
    if df.empty or 'Type' not in df.columns:
        return 'Unknown'
    return str(df['Type'].iloc[0])


def _safe_str(val) -> str:
    """Convert to string, turning NaN/None into empty string."""
    if val is None:
        return ''
    try:
        if pd.isna(val):
            return ''
    except (TypeError, ValueError):
        pass
    return str(val)


def _first_row_val(df: pd.DataFrame, col: str) -> str:
    """Return _safe_str of the first row's value for a column, or '' if missing."""
    if col not in df.columns or df.empty:
        return ''
    return _safe_str(df[col].iloc[0])


def _field_row(idx: pd.DataFrame, field_name: str) -> tuple[str, str, str, str]:
    """Extract (name, type, length, desc) for a field from a set_index'd DataFrame."""
    row = idx.loc[field_name]
    return (
        field_name,
        _safe_str(row.get('Data Type', '')),
        _safe_str(row.get('Length', '')),
        _safe_str(row.get('Description', '')),
    )


def diff_logid(prev_df: pd.DataFrame, curr_df: pd.DataFrame) -> LogidDiff:
    """Compare two versions of the same LOGID's field table."""
    prev_df = prev_df.drop_duplicates(subset='Log Field Name', keep='last')
    curr_df = curr_df.drop_duplicates(subset='Log Field Name', keep='last')

    prev_idx = prev_df.set_index('Log Field Name')
    curr_idx = curr_df.set_index('Log Field Name')

    prev_fields = set(prev_idx.index)
    curr_fields = set(curr_idx.index)

    added_fields = [_field_row(curr_idx, f) for f in sorted(curr_fields - prev_fields)]
    removed_fields = [_field_row(prev_idx, f) for f in sorted(prev_fields - curr_fields)]

    type_changes: dict[str, tuple[str, str]] = {}
    desc_changes: dict[str, tuple[str, str]] = {}
    length_changes: dict[str, tuple[str, str]] = {}

    for f in sorted(prev_fields & curr_fields):
        prev_row = prev_idx.loc[f]
        curr_row = curr_idx.loc[f]

        old_type = _safe_str(prev_row.get('Data Type', ''))
        new_type = _safe_str(curr_row.get('Data Type', ''))
        if old_type != new_type:
            type_changes[f] = (old_type, new_type)

        old_desc = _safe_str(prev_row.get('Description', ''))
        new_desc = _safe_str(curr_row.get('Description', ''))
        if old_desc != new_desc:
            desc_changes[f] = (old_desc, new_desc)

        old_len = _safe_str(prev_row.get('Length', ''))
        new_len = _safe_str(curr_row.get('Length', ''))
        if old_len != new_len:
            length_changes[f] = (old_len, new_len)

    def _meta_change(col: str) -> tuple[str, str] | None:
        old = _first_row_val(prev_df, col)
        new = _first_row_val(curr_df, col)
        return (old, new) if old != new else None

    return LogidDiff(
        added_fields=added_fields,
        removed_fields=removed_fields,
        type_changes=type_changes,
        desc_changes=desc_changes,
        length_changes=length_changes,
        severity_change=_meta_change('Severity'),
        message_desc_change=_meta_change('Message_Description'),
        category_change=_meta_change('Category'),
    )


def _utm_types(version_dict: dict[str, pd.DataFrame]) -> set[str]:
    """Return the set of UTM subtype labels (everything except Traffic, Event, Unknown) in a version."""
    return {
        label
        for df in version_dict.values()
        if (label := classify_dataset(df)) not in ('Traffic', 'Event', 'Unknown')
    }


def _cell_desc(text: str) -> str:
    """Render a description for a Markdown table cell.

    Preserves the full text — replaces all line-ending variants with HTML <br>
    so the cell displays as multi-line without breaking the table structure.
    """
    if not text:
        return '*(empty)*'
    lines = text.splitlines()
    return '<br>'.join(line.rstrip() for line in lines)


def _dataset_bucket(label: str) -> str:
    """Map a dataset label to one of three top-level buckets."""
    if label in ('Traffic', 'Event'):
        return label
    return 'UTM'


def _extra_val(df: pd.DataFrame, label: str) -> str:
    """Return Category for Traffic/Event LOGIDs, or the label itself for UTM subtypes."""
    if _dataset_bucket(label) == 'UTM':
        return label
    return _first_row_val(df, 'Category')


def _field_table_header(cols: list[str]) -> list[str]:
    """Return the two header rows (column names + separator) for a Markdown table."""
    header_row = '| ' + ' | '.join(cols) + ' |'
    sep_row = '|' + '|'.join('-' * (len(c) + 2) for c in cols) + '|'
    return [header_row, sep_row]


def _aggregate_bucket(
    bucket: str,
    bucket_diffs: dict[str, tuple[str, 'LogidDiff']],
) -> tuple[dict, dict, dict, dict, dict]:
    """Aggregate field-level changes across all LOGIDs in a bucket.

    Traffic: category is excluded from the key — all Traffic LOGIDs for the same
    field are merged into one row regardless of subcategory.
    Event/UTM: extra value (Category / UTM-subtype) is included so per-subtype rows
    remain distinct.
    """
    use_extra = bucket != 'Traffic'

    adds: dict[str, dict[tuple, list[str]]] = defaultdict(lambda: defaultdict(list))
    rems: dict[str, dict[tuple, list[str]]] = defaultdict(lambda: defaultdict(list))
    type_chgs: dict[str, dict[tuple, list[str]]] = defaultdict(lambda: defaultdict(list))
    len_chgs: dict[str, dict[tuple, list[str]]] = defaultdict(lambda: defaultdict(list))
    desc_chgs: dict[str, dict[tuple, list[str]]] = defaultdict(lambda: defaultdict(list))

    for stem, (extra, d) in bucket_diffs.items():
        e = extra if use_extra else ''
        for name, dtype, length, desc in d.added_fields:
            adds[name][(desc, dtype, length, e)].append(stem)
        for name, dtype, length, desc in d.removed_fields:
            rems[name][(desc, dtype, length, e)].append(stem)
        for name, (old_t, new_t) in d.type_changes.items():
            type_chgs[name][(old_t, new_t, e)].append(stem)
        for name, (old_l, new_l) in d.length_changes.items():
            len_chgs[name][(old_l, new_l, e)].append(stem)
        for name, (old_d, new_d) in d.desc_changes.items():
            desc_chgs[name][(old_d, new_d, e)].append(stem)

    return adds, rems, type_chgs, len_chgs, desc_chgs


def _render_version_pair(v_prev: str, v_curr: str, diff: VersionDiff) -> str:
    """Render the ### section for one version-pair diff (field-oriented tables)."""
    lines = [f'### {v_prev} → {v_curr} — Inter-version Changes', '']

    if not diff.has_changes():
        lines += ['*(no changes)*', '', '---', '']
        return '\n'.join(lines)

    # Pre-aggregate all bucket data so summary counts are derived from the same
    # aggregated data that the tables display (unique field names, not raw per-LOGID pairs).
    all_bd: dict[str, dict] = {}
    for bucket in ['Traffic', 'Event', 'UTM']:
        bucket_added = {s: e for s, (l, e) in diff.added_logids.items() if _dataset_bucket(l) == bucket}
        bucket_removed = {s: e for s, (l, e) in diff.removed_logids.items() if _dataset_bucket(l) == bucket}
        bucket_diffs = {s: (e, d) for s, (l, e, d) in diff.logid_diffs.items() if _dataset_bucket(l) == bucket}
        adds, rems, type_chgs, len_chgs, desc_chgs = _aggregate_bucket(bucket, bucket_diffs)
        all_bd[bucket] = dict(
            bucket_added=bucket_added, bucket_removed=bucket_removed,
            adds=adds, rems=rems, type_chgs=type_chgs, len_chgs=len_chgs, desc_chgs=desc_chgs,
        )

    n_la = len(diff.added_logids)
    n_lr = len(diff.removed_logids)
    n_fa = sum(len(bd['adds'])      for bd in all_bd.values())
    n_fr = sum(len(bd['rems'])      for bd in all_bd.values())
    n_tc = sum(len(bd['type_chgs']) for bd in all_bd.values())
    n_dc = sum(len(bd['desc_chgs']) for bd in all_bd.values())
    n_lc = sum(len(bd['len_chgs'])  for bd in all_bd.values())

    lines += [
        '| Metric | Count |',
        '|--------|-------|',
        f'| LOGIDs added | {n_la} |',
        f'| LOGIDs removed | {n_lr} |',
        f'| Fields added | {n_fa} |',
        f'| Fields removed | {n_fr} |',
        f'| Type changes | {n_tc} |',
        f'| Description changes | {n_dc} |',
        f'| Length changes | {n_lc} |',
        '',
    ]

    for bucket in ['Traffic', 'Event', 'UTM']:
        utm = bucket == 'UTM'
        use_extra = bucket != 'Traffic'
        extra_col: str | None = ('Type' if utm else 'Category') if use_extra else None

        bd = all_bd[bucket]
        bucket_added = bd['bucket_added']
        bucket_removed = bd['bucket_removed']
        adds = bd['adds']
        rems = bd['rems']
        type_chgs = bd['type_chgs']
        len_chgs = bd['len_chgs']
        desc_chgs = bd['desc_chgs']

        header = f'#### {bucket}'
        if bucket == 'UTM' and (diff.utmtype_added or diff.utmtype_removed):
            added_str = ', '.join(sorted(diff.utmtype_added)) or '*(none)*'
            removed_str = ', '.join(sorted(diff.utmtype_removed)) or '*(none)*'
            header += f' — new subtypes: {added_str} | removed subtypes: {removed_str}'

        if not bucket_added and not bucket_removed and not adds and not rems \
                and not type_chgs and not len_chgs and not desc_chgs:
            continue

        lines += [header, '']

        # LOGIDs added/removed: Traffic shows only the LOGID name; Event/UTM include subtype
        def _logid_table(label: str, entries: dict[str, str]) -> list[str]:
            if use_extra:
                rows = ['**' + label + '**', ''] + _field_table_header(['LOGID', extra_col])
                rows += [f'| `{s}` | {e or "—"} |' for s, e in sorted(entries.items())]
            else:
                rows = ['**' + label + '**', ''] + _field_table_header(['LOGID'])
                rows += [f'| `{s}` |' for s in sorted(entries)]
            return rows + ['']

        if bucket_added:
            lines += _logid_table('LOGIDs added', bucket_added)
        if bucket_removed:
            lines += _logid_table('LOGIDs removed', bucket_removed)

        # Helpers to build table columns and rows with/without the extra column
        def _field_cols(fixed: list[str]) -> list[str]:
            return fixed + ([extra_col] if use_extra else []) + ['LOGIDs']

        def _make_field_row(cells: list[str], extra: str, stems: list[str]) -> str:
            parts = cells + ([extra or '—'] if use_extra else []) + [_format_stems(stems)]
            return '| ' + ' | '.join(parts) + ' |'

        if adds:
            cols = _field_cols(['Log Field Name', 'Description', 'Data Type', 'Length'])
            lines += ['**Fields added**', ''] + _field_table_header(cols)
            for fname in sorted(adds):
                for (desc, dtype, length, extra), stems in sorted(adds[fname].items()):
                    lines.append(_make_field_row(
                        [f'`{fname}`', _cell_desc(desc), f'`{dtype or "*(empty)*"}`', length or '—'],
                        extra, stems,
                    ))
            lines.append('')

        if rems:
            cols = _field_cols(['Log Field Name', 'Description', 'Data Type', 'Length'])
            lines += ['**Fields removed**', ''] + _field_table_header(cols)
            for fname in sorted(rems):
                for (desc, dtype, length, extra), stems in sorted(rems[fname].items()):
                    lines.append(_make_field_row(
                        [f'`{fname}`', _cell_desc(desc), f'`{dtype or "*(empty)*"}`', length or '—'],
                        extra, stems,
                    ))
            lines.append('')

        if type_chgs:
            cols = _field_cols(['Log Field Name', 'Old Type', 'New Type'])
            lines += ['**Type changes**', ''] + _field_table_header(cols)
            for fname in sorted(type_chgs):
                for (old_t, new_t, extra), stems in sorted(type_chgs[fname].items()):
                    lines.append(_make_field_row([f'`{fname}`', f'`{old_t}`', f'`{new_t}`'], extra, stems))
            lines.append('')

        if len_chgs:
            cols = _field_cols(['Log Field Name', 'Old Length', 'New Length'])
            lines += ['**Length changes**', ''] + _field_table_header(cols)
            for fname in sorted(len_chgs):
                for (old_l, new_l, extra), stems in sorted(len_chgs[fname].items()):
                    lines.append(_make_field_row([f'`{fname}`', old_l, new_l], extra, stems))
            lines.append('')

        if desc_chgs:
            cols = _field_cols(['Log Field Name', 'Old Description', 'New Description'])
            lines += ['**Description changes**', ''] + _field_table_header(cols)
            for fname in sorted(desc_chgs):
                for (old_d, new_d, extra), stems in sorted(desc_chgs[fname].items()):
                    lines.append(_make_field_row(
                        [f'`{fname}`', _cell_desc(old_d), _cell_desc(new_d)], extra, stems,
                    ))
            lines.append('')

        # TODO: Metadata changes (severity, message description, category) need to be
        # reformulated into a proper field-oriented table format before being re-enabled.

    lines += ['---', '']
    return '\n'.join(lines)


def diff_versions(
    prev: dict[str, pd.DataFrame],
    curr: dict[str, pd.DataFrame],
) -> VersionDiff:
    """Compare two loaded minor versions, returning all changes."""
    prev_stems = set(prev.keys())
    curr_stems = set(curr.keys())

    added_logids = {
        s: (label := classify_dataset(curr[s]), _extra_val(curr[s], label))
        for s in sorted(curr_stems - prev_stems)
    }
    removed_logids = {
        s: (label := classify_dataset(prev[s]), _extra_val(prev[s], label))
        for s in sorted(prev_stems - curr_stems)
    }

    logid_diffs: dict[str, tuple[str, str, LogidDiff]] = {}
    for s in sorted(prev_stems & curr_stems):
        d = diff_logid(prev[s], curr[s])
        if d.has_changes():
            label = classify_dataset(curr[s])
            extra = _extra_val(curr[s], label)
            logid_diffs[s] = (label, extra, d)

    return VersionDiff(
        added_logids=added_logids,
        removed_logids=removed_logids,
        logid_diffs=logid_diffs,
        utmtype_added=_utm_types(curr) - _utm_types(prev),
        utmtype_removed=_utm_types(prev) - _utm_types(curr),
    )


def snapshot_version(version_dict: dict[str, pd.DataFrame]) -> VersionSnapshot:
    """Find fields with conflicting Description, Data Type, or Length across LOGIDs within each bucket."""
    # bucket → field → (desc, dtype, length) → list[stem]
    seen: dict[str, dict[str, dict[tuple[str, str, str], list[str]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )

    for stem, df in version_dict.items():
        if df.empty or 'Log Field Name' not in df.columns:
            continue
        bucket = _dataset_bucket(classify_dataset(df))
        deduped = df.drop_duplicates(subset='Log Field Name', keep='last')

        fields = deduped['Log Field Name'].map(_safe_str)
        dtypes = (
            deduped['Data Type'].map(_safe_str)
            if 'Data Type' in deduped.columns
            else pd.Series([''] * len(deduped), dtype=str)
        )
        descs = (
            deduped['Description'].map(_safe_str)
            if 'Description' in deduped.columns
            else pd.Series([''] * len(deduped), dtype=str)
        )
        lengths = (
            deduped['Length'].map(_safe_str)
            if 'Length' in deduped.columns
            else pd.Series([''] * len(deduped), dtype=str)
        )
        type_vals = (
            deduped['Type'].map(_safe_str)
            if 'Type' in deduped.columns
            else pd.Series([''] * len(deduped), dtype=str)
        )
        categories = (
            deduped['Category'].map(_safe_str)
            if 'Category' in deduped.columns
            else pd.Series([''] * len(deduped), dtype=str)
        )

        for field, dtype, desc, length, type_val, category in zip(
            fields, dtypes, descs, lengths, type_vals, categories
        ):
            if not field:
                continue
            # For UTM, group by Type (subtype) only — Category is a sub-subcategory that
            # would otherwise cause the same field+description to appear as many separate rows.
            # For Traffic/Event, Type is constant within the bucket, so Category is used.
            if bucket == 'UTM':
                key = (desc, dtype, length, type_val, '')
            else:
                key = (desc, dtype, length, type_val, category)
            seen[bucket][field][key].append(stem)

    desc_conflicts: dict[str, dict[str, _ConflictRows]] = defaultdict(dict)
    type_conflicts: dict[str, dict[str, _ConflictRows]] = defaultdict(dict)
    length_conflicts: dict[str, dict[str, _ConflictRows]] = defaultdict(dict)

    for bucket, fields in seen.items():
        for field, combo_stems in fields.items():
            rows: _ConflictRows = sorted(
                (desc, dtype, length, type_val, category, stems)
                for (desc, dtype, length, type_val, category), stems in combo_stems.items()
            )
            if len({r[0] for r in rows}) > 1:
                desc_conflicts[bucket][field] = rows
            if len({r[1] for r in rows}) > 1:
                type_conflicts[bucket][field] = rows
            if len({r[2] for r in rows}) > 1:
                length_conflicts[bucket][field] = rows

    return VersionSnapshot(
        desc_conflicts=dict(desc_conflicts),
        type_conflicts=dict(type_conflicts),
        length_conflicts=dict(length_conflicts),
    )


def _format_stems(stems: list[str], max_show: int = 5) -> str:
    """Format a list of LOGID stems, truncating if too many."""
    shown = stems[:max_show]
    rest = len(stems) - max_show
    result = ', '.join(shown)
    if rest > 0:
        result += f' *(+{rest} more)*'
    return result


def _render_conflict_rows(field: str, rows: _ConflictRows, bucket: str) -> list[str]:
    """Render the field heading and table for one conflicting field."""
    lines = [f'`{field}`', '']
    utm = bucket == 'UTM'
    extra_col = 'Type' if utm else 'Category'
    lines += _field_table_header(['Log Field Name', 'Description', 'Data Type', 'Length', extra_col, 'LOGIDs'])
    for desc, dtype, length, type_val, category, stems in rows:
        desc_cell = _cell_desc(desc)
        dtype_cell = dtype or '*(empty)*'
        length_cell = length or '—'
        extra_cell = (type_val or '—') if utm else (category or '—')
        lines.append(
            f'| `{field}` | {desc_cell} | `{dtype_cell}` | {length_cell}'
            f' | {extra_cell} | {_format_stems(stems)} |'
        )
    lines.append('')
    return lines


def _render_version_snapshot(version: str, snap: VersionSnapshot) -> str:
    """Render the intra-version inconsistency section for a single minor version."""
    lines = [f'### {version} — Intra-version Inconsistencies', '']

    n_desc = sum(len(f) for f in snap.desc_conflicts.values())
    n_type = sum(len(f) for f in snap.type_conflicts.values())
    n_len = sum(len(f) for f in snap.length_conflicts.values())

    if n_desc + n_type + n_len == 0:
        lines += ['*(no inconsistencies)*', '', '---', '']
        return '\n'.join(lines)

    lines += [
        '**Summary**',
        '',
        '| Conflict Type | Fields |',
        '|--------------|--------|',
        f'| Description conflicts | {n_desc} |',
        f'| Data Type conflicts | {n_type} |',
        f'| Length conflicts | {n_len} |',
        '',
    ]

    for bucket in ['Traffic', 'Event', 'UTM']:
        dc = snap.desc_conflicts.get(bucket, {})
        tc = snap.type_conflicts.get(bucket, {})
        lc = snap.length_conflicts.get(bucket, {})
        if not dc and not tc and not lc:
            continue

        lines += [f'#### {bucket}', '']

        if dc:
            lines += ['**Description conflicts** — same field, different `Description` across LOGIDs', '']
            for field, rows in sorted(dc.items()):
                lines += _render_conflict_rows(field, rows, bucket)

        if tc:
            lines += ['**Data Type conflicts** — same field, different `Data Type` across LOGIDs', '']
            for field, rows in sorted(tc.items()):
                lines += _render_conflict_rows(field, rows, bucket)

        if lc:
            lines += ['**Length conflicts** — same field, different `Length` across LOGIDs', '']
            for field, rows in sorted(lc.items()):
                lines += _render_conflict_rows(field, rows, bucket)

    lines += ['---', '']
    return '\n'.join(lines)


def main() -> None:
    root = Path(__file__).parent
    version_groups = discover_versions(root)

    if not version_groups:
        print('No version directories found. Run fortigate_scraper.py first.')
        return

    for major_label, minor_dirs in version_groups:
        if not minor_dirs:
            continue

        lines: list[str] = [f'# FortiGate {major_label} Log Field Changelog', '']

        prev_data = load_version(minor_dirs[0])
        lines += [f'## {minor_dirs[0].name}', '']
        lines.append(_render_version_snapshot(minor_dirs[0].name, snapshot_version(prev_data)))

        for prev_dir, curr_dir in zip(minor_dirs, minor_dirs[1:]):
            curr_data = load_version(curr_dir)
            diff = diff_versions(prev_data, curr_data)
            lines += [f'## {curr_dir.name}', '']
            lines.append(_render_version_snapshot(curr_dir.name, snapshot_version(curr_data)))
            lines.append(_render_version_pair(prev_dir.name, curr_dir.name, diff))
            prev_data = curr_data

        output = '\n'.join(lines) + '\n'
        output_path = root / major_label / 'CHANGELOG.md'
        output_path.write_text(output, encoding='utf-8')
        print(f'Written: {output_path} ({output_path.stat().st_size:,} bytes)')


if __name__ == '__main__':
    main()
