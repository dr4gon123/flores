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
