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


def diff_versions(
    prev: dict[str, pd.DataFrame],
    curr: dict[str, pd.DataFrame],
) -> VersionDiff:
    """Compare two loaded minor versions, returning all changes."""
    prev_stems = set(prev.keys())
    curr_stems = set(curr.keys())

    added_logids = {s: classify_dataset(curr[s]) for s in sorted(curr_stems - prev_stems)}
    removed_logids = {s: classify_dataset(prev[s]) for s in sorted(prev_stems - curr_stems)}

    logid_diffs: dict[str, tuple[str, LogidDiff]] = {}
    for s in sorted(prev_stems & curr_stems):
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
