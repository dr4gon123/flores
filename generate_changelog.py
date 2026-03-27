"""
Generates CHANGELOG.md by comparing raw LOGID CSVs between adjacent minor FortiOS versions.
Run from repo root: python3 generate_changelog.py
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

EXCLUDED_TYPES = {'GTP'}
MAJOR_RE = re.compile(r'^\d+\.\d+$')
MINOR_RE = re.compile(r'^\d+\.\d+\.\d+$')
DESC_TRUNCATE = 120


@dataclass
class LogidDiff:
    added_fields: list[tuple[str, str, str, str]]    # (name, type, length, desc)
    removed_fields: list[tuple[str, str, str, str]]  # (name, type, length, desc)
    type_changes: dict[str, tuple[str, str]]          # field → (old, new)
    desc_changes: dict[str, tuple[str, str]]          # field → (old, new)
    length_changes: dict[str, tuple[str, str]]        # field → (old, new)

    def has_changes(self) -> bool:
        return bool(
            self.added_fields or self.removed_fields
            or self.type_changes or self.desc_changes or self.length_changes
        )


@dataclass
class VersionDiff:
    added_logids: dict[str, str]                   # stem → dataset_label
    removed_logids: dict[str, str]                 # stem → dataset_label
    logid_diffs: dict[str, tuple[str, LogidDiff]]  # stem → (dataset_label, LogidDiff)
    utmtype_added: set[str]
    utmtype_removed: set[str]

    def has_changes(self) -> bool:
        return bool(
            self.added_logids or self.removed_logids or self.logid_diffs
            or self.utmtype_added or self.utmtype_removed
        )


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
    """Return dataset bucket: 'Traffic', 'Event', 'GTP', 'Unknown', or UTM subtype name."""
    if df.empty or 'Type' not in df.columns:
        return 'Unknown'
    type_val = str(df['Type'].iloc[0])
    if type_val in ('Traffic', 'Event'):
        return type_val
    if type_val in EXCLUDED_TYPES:
        return 'GTP'
    return type_val  # UTM subtype (Webfilter, IPS, APP-CTRL, etc.)


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

    return LogidDiff(
        added_fields=added_fields,
        removed_fields=removed_fields,
        type_changes=type_changes,
        desc_changes=desc_changes,
        length_changes=length_changes,
    )


def _utm_types(version_dict: dict[str, pd.DataFrame]) -> set[str]:
    """Return the set of UTM subtype labels present in a version."""
    return {
        classify_dataset(df)
        for df in version_dict.values()
        if classify_dataset(df) not in ('Traffic', 'Event', 'GTP', 'Unknown')
    }


def _truncate(text: str, max_len: int = DESC_TRUNCATE) -> str:
    """Flatten newlines and truncate to max_len chars, appending '…' if cut."""
    text = str(text).replace('\n', ' ').strip()
    return text if len(text) <= max_len else text[:max_len] + '…'


def _render_logid_diff(d: LogidDiff) -> list[str]:
    """Return bullet lines describing all changes in a single LOGID diff."""
    lines = []
    for name, typ, length, desc in d.added_fields:
        lines.append(f'- Field added: `{name}` ({typ}, len: {length}) — "{_truncate(desc)}"')
    for name, typ, _length, _desc in d.removed_fields:
        lines.append(f'- Field removed: `{name}` ({typ})')
    for f, (old, new) in sorted(d.type_changes.items()):
        lines.append(f'- Type changed: `{f}` `{old}` → `{new}`')
    for f, (old, new) in sorted(d.desc_changes.items()):
        lines.append(f'- Description changed: `{f}`')
        lines.append(f'  - Before: "{_truncate(old)}"')
        lines.append(f'  - After:  "{_truncate(new)}"')
    for f, (old, new) in sorted(d.length_changes.items()):
        lines.append(f'- Length changed: `{f}` {old} → {new}')
    return lines


def _dataset_bucket(label: str) -> str:
    """Map a dataset label to one of three top-level buckets."""
    if label in ('Traffic', 'Event'):
        return label
    return 'UTM'


def _render_version_pair(v_prev: str, v_curr: str, diff: VersionDiff) -> str:
    """Render the ### section for one version-pair diff."""
    lines = [f'### {v_prev} → {v_curr}', '']

    if not diff.has_changes():
        lines += ['*(no changes)*', '', '---', '']
        return '\n'.join(lines)

    # Summary counts (fields from changed LOGIDs only)
    n_la = len(diff.added_logids)
    n_lr = len(diff.removed_logids)
    n_fa = sum(len(d.added_fields) for _, d in diff.logid_diffs.values())
    n_fr = sum(len(d.removed_fields) for _, d in diff.logid_diffs.values())
    n_tc = sum(len(d.type_changes) for _, d in diff.logid_diffs.values())
    n_dc = sum(len(d.desc_changes) for _, d in diff.logid_diffs.values())
    n_lc = sum(len(d.length_changes) for _, d in diff.logid_diffs.values())

    lines.append(
        f'**Summary:** {n_la} LOGID added, {n_lr} removed | '
        f'{n_fa} fields added, {n_fr} removed | '
        f'{n_tc} type changed | {n_dc} descriptions changed | {n_lc} lengths changed'
    )
    lines.append('')

    # Bucket all changes by dataset
    by_bucket: dict[str, list] = {'Traffic': [], 'Event': [], 'UTM': []}

    for stem, label in sorted(diff.added_logids.items()):
        by_bucket[_dataset_bucket(label)].append(('added', stem, label, None))
    for stem, label in sorted(diff.removed_logids.items()):
        by_bucket[_dataset_bucket(label)].append(('removed', stem, label, None))
    for stem, (label, d) in sorted(diff.logid_diffs.items()):
        by_bucket[_dataset_bucket(label)].append(('changed', stem, label, d))

    for bucket in ['Traffic', 'Event', 'UTM']:
        entries = by_bucket[bucket]
        header = f'#### {bucket}'
        if bucket == 'UTM' and (diff.utmtype_added or diff.utmtype_removed):
            added_str = ', '.join(sorted(diff.utmtype_added)) or '*(none)*'
            removed_str = ', '.join(sorted(diff.utmtype_removed)) or '*(none)*'
            header += f' — new subtypes: {added_str} | removed subtypes: {removed_str}'
        lines += [header, '']

        if not entries:
            lines += ['*(no changes)*', '']
            continue

        for kind, stem, _label, d in entries:
            if kind == 'added':
                lines += [f'##### {stem} *(new)*', '']
            elif kind == 'removed':
                lines += [f'##### {stem} *(removed)*', '']
            else:
                lines.append(f'##### {stem}')
                lines += _render_logid_diff(d)
                lines.append('')

    lines += ['---', '']
    return '\n'.join(lines)


def diff_versions(
    prev: dict[str, pd.DataFrame],
    curr: dict[str, pd.DataFrame],
) -> VersionDiff:
    """Compare two loaded minor versions, returning all changes."""
    prev_stems = set(prev.keys())
    curr_stems = set(curr.keys())

    # Filter out excluded types (e.g. GTP) from all collections
    def is_excluded(df: pd.DataFrame) -> bool:
        return classify_dataset(df) in EXCLUDED_TYPES

    added_logids = {
        s: classify_dataset(curr[s])
        for s in sorted(curr_stems - prev_stems)
        if not is_excluded(curr[s])
    }
    removed_logids = {
        s: classify_dataset(prev[s])
        for s in sorted(prev_stems - curr_stems)
        if not is_excluded(prev[s])
    }

    logid_diffs: dict[str, tuple[str, LogidDiff]] = {}
    for s in sorted(prev_stems & curr_stems):
        if is_excluded(curr[s]):
            continue
        d = diff_logid(prev[s], curr[s])
        if d.has_changes():
            logid_diffs[s] = (classify_dataset(curr[s]), d)

    return VersionDiff(
        added_logids=added_logids,
        removed_logids=removed_logids,
        logid_diffs=logid_diffs,
        utmtype_added=_utm_types(curr) - _utm_types(prev),
        utmtype_removed=_utm_types(prev) - _utm_types(curr),
    )


def main() -> None:
    root = Path(__file__).parent
    version_groups = discover_versions(root)

    if not version_groups:
        print('No version directories found. Run fortigate_scraper.py first.')
        return

    major_sections: list[str] = []

    for major_label, minor_dirs in version_groups:
        pairs = list(zip(minor_dirs, minor_dirs[1:]))
        if not pairs:
            continue

        section_lines = [f'## {major_label}', '']
        for prev_dir, curr_dir in pairs:
            prev = load_version(prev_dir)
            curr = load_version(curr_dir)
            diff = diff_versions(prev, curr)
            section_lines.append(_render_version_pair(prev_dir.name, curr_dir.name, diff))

        major_sections.append('\n'.join(section_lines))

    changelog = '# FortiGate Log Field Changelog\n\n' + '\n\n'.join(major_sections) + '\n'
    output_path = root / 'CHANGELOG.md'
    output_path.write_text(changelog, encoding='utf-8')
    print(f'Written: {output_path} ({output_path.stat().st_size:,} bytes)')


if __name__ == '__main__':
    main()
