"""
Generates per-major-version CHANGELOG.md files by comparing raw LOGID CSVs
between adjacent minor FortiOS versions.
Run from repo root: python3 generate_changelog.py
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from itertools import groupby
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
    for csv_file in sorted((minor_dir / 'LOGID').glob('*.csv')):
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

    def _logid_table(label: str, entries: dict[str, str], use_extra: bool, extra_col: str | None) -> list[str]:
        if use_extra:
            rows = ['**' + label + '**', ''] + _field_table_header(['LOGID', extra_col])
            rows += [f'| `{s}` | {e or "—"} |' for s, e in sorted(entries.items())]
        else:
            rows = ['**' + label + '**', ''] + _field_table_header(['LOGID'])
            rows += [f'| `{s}` |' for s in sorted(entries)]
        return rows + ['']

    def _field_cols(fixed: list[str], use_extra: bool, extra_col: str | None) -> list[str]:
        return fixed + ([extra_col] if use_extra else []) + ['LOGIDs']

    def _make_field_row(cells: list[str], extra: str, stems: list[str], use_extra: bool) -> str:
        parts = cells + ([extra or '—'] if use_extra else []) + [_format_stems(stems)]
        return '| ' + ' | '.join(parts) + ' |'

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

        if bucket_added:
            lines += _logid_table('LOGIDs added', bucket_added, use_extra, extra_col)
        if bucket_removed:
            lines += _logid_table('LOGIDs removed', bucket_removed, use_extra, extra_col)

        if adds:
            cols = _field_cols(['Log Field Name', 'Description', 'Data Type', 'Length'], use_extra, extra_col)
            lines += ['**Fields added**', ''] + _field_table_header(cols)
            for fname in sorted(adds):
                for (desc, dtype, length, extra), stems in sorted(adds[fname].items()):
                    lines.append(_make_field_row(
                        [f'`{fname}`', _cell_desc(desc), f'`{dtype or "*(empty)*"}`', length or '—'],
                        extra, stems, use_extra,
                    ))
            lines.append('')

        if rems:
            cols = _field_cols(['Log Field Name', 'Description', 'Data Type', 'Length'], use_extra, extra_col)
            lines += ['**Fields removed**', ''] + _field_table_header(cols)
            for fname in sorted(rems):
                for (desc, dtype, length, extra), stems in sorted(rems[fname].items()):
                    lines.append(_make_field_row(
                        [f'`{fname}`', _cell_desc(desc), f'`{dtype or "*(empty)*"}`', length or '—'],
                        extra, stems, use_extra,
                    ))
            lines.append('')

        if type_chgs:
            cols = _field_cols(['Log Field Name', 'Old Type', 'New Type'], use_extra, extra_col)
            lines += ['**Type changes**', ''] + _field_table_header(cols)
            for fname in sorted(type_chgs):
                for (old_t, new_t, extra), stems in sorted(type_chgs[fname].items()):
                    lines.append(_make_field_row([f'`{fname}`', f'`{old_t}`', f'`{new_t}`'], extra, stems, use_extra))
            lines.append('')

        if len_chgs:
            cols = _field_cols(['Log Field Name', 'Old Length', 'New Length'], use_extra, extra_col)
            lines += ['**Length changes**', ''] + _field_table_header(cols)
            for fname in sorted(len_chgs):
                for (old_l, new_l, extra), stems in sorted(len_chgs[fname].items()):
                    lines.append(_make_field_row([f'`{fname}`', old_l, new_l], extra, stems, use_extra))
            lines.append('')

        if desc_chgs:
            cols = _field_cols(['Log Field Name', 'Old Description', 'New Description'], use_extra, extra_col)
            lines += ['**Description changes**', ''] + _field_table_header(cols)
            for fname in sorted(desc_chgs):
                for (old_d, new_d, extra), stems in sorted(desc_chgs[fname].items()):
                    lines.append(_make_field_row(
                        [f'`{fname}`', _cell_desc(old_d), _cell_desc(new_d)], extra, stems, use_extra,
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


def _render_conflict_rows(
    field: str,
    rows: _ConflictRows,
    bucket: str,
    conflict_labels: list[str] | None = None,
) -> list[str]:
    """Render the field heading, optional conflict-type labels, and table for one field.

    Rows sharing the same (desc, dtype, length) are collapsed into a single
    table row with <br>-separated categories and LOGID lists.
    """
    lines = [f'`{field}`', '']
    if conflict_labels:
        lines += conflict_labels + ['']
    utm = bucket == 'UTM'
    extra_col = 'Type' if utm else 'Category'
    lines += _field_table_header(['Log Field Name', 'Description', 'Data Type', 'Length', extra_col, 'LOGIDs'])
    for (desc, dtype, length), group in groupby(rows, key=lambda r: (r[0], r[1], r[2])):
        entries = list(group)
        desc_cell = _cell_desc(desc)
        dtype_cell = dtype or '*(empty)*'
        length_cell = length or '—'
        extra_cell = '<br>'.join((type_val if utm else category) or '—'
                                 for _, _, _, type_val, category, _ in entries)
        stems_cell = '<br>'.join(_format_stems(stems, max_show=3)
                                 for *_, stems in entries)
        lines.append(
            f'| `{field}` | {desc_cell} | `{dtype_cell}` | {length_cell}'
            f' | {extra_cell} | {stems_cell} |'
        )
    lines.append('')
    return lines


def _render_traffic_event_coverage(all_df: pd.DataFrame) -> list[str]:
    """Render per-Category field/LOGID counts for Traffic and Event rows."""
    lines: list[str] = []
    for label in ('Traffic', 'Event'):
        subset = all_df[all_df['Type'] == label]
        if subset.empty:
            continue
        grp = subset.groupby('Category')
        field_counts = grp['Log Field Name'].nunique().sort_index()
        logid_counts = grp['_stem'].nunique().sort_index()
        lines += [f'**{label}**', ''] + _field_table_header(['Category', 'Fields', 'LOGIDs'])
        for cat, n in field_counts.items():
            lines.append(f'| {cat} | {n} | {logid_counts[cat]} |')
        lines.append('')
    return lines


def _render_utm_coverage(all_df: pd.DataFrame) -> list[str]:
    """Render per-Type field/LOGID/category counts for UTM (including GTP) rows."""
    utm = all_df[~all_df['Type'].isin(['Traffic', 'Event'])]
    if utm.empty:
        return []
    grp = utm.groupby('Type')
    field_counts = grp['Log Field Name'].nunique()
    logid_counts = grp['_stem'].nunique()
    cat_counts = grp['Category'].nunique()
    cat_lists = grp['Category'].apply(lambda s: ', '.join(sorted(s.unique())))
    lines: list[str] = ['**UTM** *(including GTP)*', ''] + _field_table_header(['Type', 'Fields', 'LOGIDs', 'Categories', 'Category List'])
    for t in sorted(utm['Type'].unique()):
        lines.append(f'| {t} | {field_counts[t]} | {logid_counts[t]} | {cat_counts[t]} | {cat_lists[t]} |')
    lines.append('')
    return lines


def _render_version_coverage(version_dict: dict[str, pd.DataFrame]) -> str:
    """Render Traffic/Event/UTM field-count summary tables for one minor version."""
    if not version_dict:
        return ''

    pieces = [
        df.assign(_stem=stem)
        for stem, df in version_dict.items()
        if not df.empty and 'Log Field Name' in df.columns
    ]
    if not pieces:
        return ''
    all_df = pd.concat(pieces, ignore_index=True)

    lines = _render_traffic_event_coverage(all_df) + _render_utm_coverage(all_df)
    return '\n'.join(lines)


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

        all_conflict_fields = sorted(set(dc) | set(tc) | set(lc))
        lines += _field_table_header(['Log Field Name', 'Description', 'Data Type', 'Length'])
        for f in all_conflict_fields:
            lines.append(
                f'| `{f}` | {"X" if f in dc else ""} | {"X" if f in tc else ""} | {"X" if f in lc else ""} |'
            )
        lines.append('')

        for field in all_conflict_fields:
            labels = []
            if field in dc:
                labels.append('**Description conflicts** — same field, different `Description` across LOGIDs')
            if field in tc:
                labels.append('**Data Type conflicts** — same field, different `Data Type` across LOGIDs')
            if field in lc:
                labels.append('**Length conflicts** — same field, different `Length` across LOGIDs')
            rows = dc.get(field) or tc.get(field) or lc.get(field)
            lines += _render_conflict_rows(field, rows, bucket, conflict_labels=labels)

    lines += ['---', '']
    return '\n'.join(lines)


def _build_field_matrix(
    version_dict: dict[str, pd.DataFrame],
    type_filter: str | None,
    group_col: str,
) -> pd.DataFrame:
    """Build a field × category/type occurrence matrix for one minor version.

    Rows are field names, columns are categories (Traffic/Event) or types (UTM).
    The first row (index '_total') holds the total LOGID count per column.
    Cell values are the number of distinct LOGIDs containing that field.
    Returns an empty DataFrame if no rows match the filter.
    """
    pieces = [
        df.assign(_stem=stem)
        for stem, df in version_dict.items()
        if not df.empty and 'Log Field Name' in df.columns
    ]
    if not pieces:
        return pd.DataFrame()
    all_df = pd.concat(pieces, ignore_index=True)

    if type_filter is not None:
        subset = all_df[all_df['Type'] == type_filter]
    else:
        subset = all_df[~all_df['Type'].isin(['Traffic', 'Event'])]

    if subset.empty:
        return pd.DataFrame()

    matrix = (
        subset
        .groupby(['Log Field Name', group_col])['_stem']
        .nunique()
        .unstack(fill_value=0)
    )
    matrix = matrix[sorted(matrix.columns)].sort_index()

    totals = subset.groupby(group_col)['_stem'].nunique().reindex(matrix.columns, fill_value=0)
    total_row = totals.to_frame().T
    total_row.index = pd.Index(['_total'], name=matrix.index.name)
    return pd.concat([total_row, matrix])


def _write_minor_analysis(
    minor_dir: Path,
    version_dict: dict[str, pd.DataFrame],
    snap: VersionSnapshot,
    diff: VersionDiff | None = None,
    prev_label: str | None = None,
    do_changelog: bool = True,
    do_matrices: bool = True,
) -> None:
    """Write CHANGELOG.md and/or the three field matrix CSVs for one minor version."""
    if do_changelog:
        content_parts = [
            f'# FortiGate {minor_dir.name} — Analysis', '',
            _render_version_coverage(version_dict),
            _render_version_snapshot(minor_dir.name, snap),
        ]
        if diff is not None and prev_label is not None:
            content_parts.append(_render_version_pair(prev_label, minor_dir.name, diff))
        changelog_path = minor_dir / 'CHANGELOG.md'
        changelog_path.write_text('\n'.join(content_parts) + '\n', encoding='utf-8')
        print(f'Written: {changelog_path} ({changelog_path.stat().st_size:,} bytes)')

    if do_matrices:
        specs = [
            ('traffic_matrix.csv', 'Traffic', 'Category'),
            ('event_matrix.csv',   'Event',   'Category'),
            ('utm_matrix.csv',     None,      'Type'),
        ]
        for filename, type_filter, group_col in specs:
            matrix = _build_field_matrix(version_dict, type_filter, group_col)
            if matrix.empty:
                continue
            path = minor_dir / filename
            matrix.to_csv(path)
            n_fields = len(matrix) - 1  # exclude _total row
            print(f'Written: {path} ({n_fields} fields × {len(matrix.columns)} columns)')


def _normalize_desc(text: str) -> str:
    return text.strip().lower() if text else ''


def _canonical_desc(descriptions: list[str]) -> str:
    return Counter(descriptions).most_common(1)[0][0] if descriptions else ''


def _label_descriptions(subtype_descs: dict[str, list[str]]) -> str:
    """Build subtype-labeled description string. Returns plain text if single meaning."""
    norm_groups: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for subtype, descs in subtype_descs.items():
        for desc in descs:
            norm = _normalize_desc(desc)
            if norm:
                norm_groups[norm].append((desc, subtype))
    if not norm_groups:
        return ''
    meanings = sorted(
        [(_canonical_desc([d for d, _ in pairs]), sorted({s for _, s in pairs}))
         for pairs in norm_groups.values()],
        key=lambda x: x[1][0],
    )
    if len(meanings) == 1:
        return meanings[0][0]
    return '\n\n'.join(f"{'/'.join(subtypes)}: {desc}" for desc, subtypes in meanings)


def _consolidate_fields(
    all_stems: dict[str, pd.DataFrame],
    type_filter: str | None,
    group_col: str,
) -> pd.DataFrame:
    """Consolidate field definitions across all minor versions for one log type.

    Returns a DataFrame with columns: Log Field Name, Data Type, Length, Description.
    Data Type and Length list all distinct raw values (comma-separated).
    Description uses subtype-labeled format when meanings differ across subtypes.
    """
    pieces = [
        df.assign(_stem=stem)
        for stem, df in all_stems.items()
        if not df.empty and 'Log Field Name' in df.columns
    ]
    if not pieces:
        return pd.DataFrame()
    all_df = pd.concat(pieces, ignore_index=True)

    if type_filter is not None:
        subset = all_df[all_df['Type'] == type_filter].copy()
    else:
        subset = all_df[~all_df['Type'].isin(['Traffic', 'Event'])].copy()

    if subset.empty:
        return pd.DataFrame()

    for col in ('Data Type', 'Length', 'Description'):
        if col not in subset.columns:
            subset[col] = ''
    if group_col not in subset.columns:
        subset[group_col] = ''

    type_agg = (
        subset.groupby('Log Field Name')['Data Type']
        .apply(lambda s: ','.join(sorted({t for t in s.map(_safe_str).unique() if t})))
    )
    length_agg = (
        subset.groupby('Log Field Name')['Length']
        .apply(lambda s: ','.join(sorted(
            {lv for lv in s.map(_safe_str).unique() if lv},
            key=lambda x: int(x) if x.isdigit() else x,
        )))
    )
    desc_agg = {
        field: _label_descriptions(
            grp.groupby(group_col)['Description']
            .apply(lambda s: s.map(_safe_str).tolist())
            .to_dict()
        )
        for field, grp in subset.groupby('Log Field Name')
    }

    fields = type_agg.index.tolist()
    return pd.DataFrame({
        'Log Field Name': fields,
        'Data Type': type_agg.values,
        'Length': length_agg.reindex(fields, fill_value='').values,
        'Description': [desc_agg.get(f, '') for f in fields],
    })


def _consolidate_action_descriptions(all_stems: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Build a single-row DataFrame of action field descriptions keyed by UTM subtype."""
    pieces = [
        df
        for df in all_stems.values()
        if not df.empty and 'Log Field Name' in df.columns
    ]
    if not pieces:
        return pd.DataFrame()
    all_df = pd.concat(pieces, ignore_index=True)

    action_rows = all_df[
        ~all_df['Type'].isin(['Traffic', 'Event'])
        & (all_df['Log Field Name'].fillna('') == 'action')
    ]
    if action_rows.empty:
        return pd.DataFrame()

    result: dict[str, str] = {}
    for subtype, grp in action_rows.groupby('Type'):
        seen: set[str] = set()
        unique_descs: list[str] = []
        for desc in grp['Description']:
            safe = _safe_str(desc)
            norm = _normalize_desc(safe)
            if norm and norm not in seen:
                seen.add(norm)
                unique_descs.append(safe)
        result[str(subtype)] = '\n\n'.join(unique_descs)

    return pd.DataFrame([{s: result[s] for s in sorted(result)}])


def _write_major_fields(major_dir: Path, all_stems: dict[str, pd.DataFrame]) -> None:
    """Write consolidated field CSVs for all log types under {major}/fields/."""
    fields_dir = major_dir / 'fields'
    fields_dir.mkdir(exist_ok=True)
    specs = [
        ('traffic_fields.csv', 'Traffic', 'Category'),
        ('event_fields.csv',   'Event',   'Category'),
        ('utm_fields.csv',     None,      'Type'),
    ]
    for filename, type_filter, group_col in specs:
        df = _consolidate_fields(all_stems, type_filter, group_col)
        if df.empty:
            continue
        path = fields_dir / filename
        df.to_csv(path, index=False)
        print(f'Written: {path} ({len(df)} fields)')

    action_df = _consolidate_action_descriptions(all_stems)
    if not action_df.empty:
        path = fields_dir / 'action_descriptions.csv'
        action_df.to_csv(path, index=False)
        print(f'Written: {path} ({len(action_df.columns)} subtypes)')


def _write_changelog_index(root: Path, version_groups: list[tuple[str, list[Path]]]) -> None:
    """Write root INDEX.md and per-major INDEX.md files."""
    def _link(path: Path, label: str, rel: str) -> str:
        return f"[{label}]({rel})" if path.exists() else label

    def _major_section(major_label: str, minor_dirs: list[Path], prefix: str, include_matrices: bool = False) -> list[str]:
        """Build the lines for one major-version section. prefix is prepended to all paths."""
        sec: list[str] = []
        sec.append(f"## FortiOS {major_label}")
        sec.append("")

        sec.append("### Changelog")
        sec.append("")
        for minor_dir in reversed(minor_dirs):
            version = minor_dir.name
            rel = f"{prefix}{version}/CHANGELOG.md"
            sec.append(f"- {_link(root / f'{major_label}/{version}/CHANGELOG.md', version, rel)}")
        sec.append("")

        sec.append("### Consolidated Fields")
        sec.append("")
        field_specs = [
            ("traffic_fields",      f"{prefix}fields/traffic_fields.csv"),
            ("event_fields",        f"{prefix}fields/event_fields.csv"),
            ("utm_fields",          f"{prefix}fields/utm_fields.csv"),
            ("action_descriptions", f"{prefix}fields/action_descriptions.csv"),
        ]
        field_specs = [(label, rel) for label, rel in field_specs if (root / f"{major_label}/fields/{label}.csv").exists()]
        for label, rel in field_specs:
            sec.append(f"- {_link(root / f'{major_label}/fields/{label}.csv', label, rel)}")
        sec.append("")

        sec.append("### ECS")
        sec.append("")
        ecs_names = ["traffic_ecs", "event_ecs", "utm_ecs"]
        ecs_specs = [
            (name, f"{prefix}ECS/{name}.csv")
            for name in ecs_names
            if (root / f"{major_label}/ECS/{name}.csv").exists()
        ]
        for label, rel in ecs_specs:
            sec.append(f"- {_link(root / f'{major_label}/ECS/{label}.csv', label, rel)}")
        sec.append("")

        if include_matrices:
            sec.append("### Field Occurrence Matrix")
            sec.append("")
            matrix_names = ["traffic", "event", "utm"]
            for minor_dir in reversed(minor_dirs):
                version = minor_dir.name
                parts = [
                    _link(root / f"{major_label}/{version}/{name}_matrix.csv", name, f"{prefix}{version}/{name}_matrix.csv")
                    for name in matrix_names
                    if (root / f"{major_label}/{version}/{name}_matrix.csv").exists()
                ]
                if parts:
                    sec.append(f"- **{version}** — {' · '.join(parts)}")
            sec.append("")

        return sec

    root_lines: list[str] = [
        "# FLORES — Index",
        "",
        "> Auto-generated by `generate_changelog.py --index`. Do not edit manually.",
        "",
    ]

    for major_label, minor_dirs in reversed(version_groups):
        # Root INDEX.md: links are relative to repo root (prefix includes major_label/)
        root_lines.extend(_major_section(major_label, minor_dirs, prefix=f"{major_label}/", include_matrices=True))
        root_lines.append("---")
        root_lines.append("")

        # Per-major INDEX.md: links are relative to the major folder (no prefix)
        major_lines = [
            "> Auto-generated by `generate_changelog.py --index`. Do not edit manually.",
            "",
        ]
        major_lines.extend(_major_section(major_label, minor_dirs, prefix="", include_matrices=True))
        major_out = root / major_label / "INDEX.md"
        major_out.write_text("\n".join(major_lines))
        print(f"Written: {major_out}")

    out = root / "INDEX.md"
    out.write_text("\n".join(root_lines))
    print(f"Written: {out}")


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description='Generate FortiGate log field changelogs and field matrices.')
    parser.add_argument('--changelog', action='store_true', help='Generate only per-minor-version CHANGELOG.md files')
    parser.add_argument('--matrices', action='store_true', help='Generate only per-minor-version field matrix CSVs')
    parser.add_argument('--fields', action='store_true', help='Generate consolidated field CSVs per major version')
    parser.add_argument('--index', action='store_true', help='Generate root-level INDEX.md')
    args = parser.parse_args()
    any_flag = args.changelog or args.matrices or args.fields or args.index
    do_changelog = args.changelog or not any_flag
    do_matrices = args.matrices or not any_flag
    do_fields = args.fields or not any_flag
    do_index = args.index or not any_flag

    root = Path(__file__).parent
    version_groups = discover_versions(root)

    if not version_groups:
        print('No version directories found. Run fortigate_scraper.py first.')
        return

    for major_label, minor_dirs in version_groups:
        if not minor_dirs:
            continue

        all_stems: dict[str, pd.DataFrame] = {}

        prev_data = load_version(minor_dirs[0])
        all_stems.update(prev_data)
        if do_changelog or do_matrices:
            prev_snap = snapshot_version(prev_data)
            _write_minor_analysis(minor_dirs[0], prev_data, prev_snap,
                                  do_changelog=do_changelog, do_matrices=do_matrices)

        for prev_dir, curr_dir in zip(minor_dirs, minor_dirs[1:]):
            curr_data = load_version(curr_dir)
            all_stems.update(curr_data)
            if do_changelog or do_matrices:
                diff = diff_versions(prev_data, curr_data) if do_changelog else None
                curr_snap = snapshot_version(curr_data)
                _write_minor_analysis(curr_dir, curr_data, curr_snap,
                                      diff=diff, prev_label=prev_dir.name,
                                      do_changelog=do_changelog, do_matrices=do_matrices)
            prev_data = curr_data

        if do_fields:
            _write_major_fields(root / major_label, all_stems)

    if do_index:
        _write_changelog_index(root, version_groups)


if __name__ == '__main__':
    main()
