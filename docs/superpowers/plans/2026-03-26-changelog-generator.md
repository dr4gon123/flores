# Changelog Generator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `generate_changelog.py` — a standalone script that reads the existing raw LOGID CSVs and writes `CHANGELOG.md` comparing each minor FortiOS version to its predecessor within each major version.

**Architecture:** The script discovers all `<major>/<minor>/` directories, loads each minor version's LOGID CSVs into pandas DataFrames, diffs adjacent version pairs field-by-field, and renders the results into Markdown. All logic is broken into pure functions tested in `tests/test_generate_changelog.py`.

**Tech Stack:** Python 3, pandas (already required by the project), pytest (for tests), pathlib, dataclasses, re.

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `generate_changelog.py` | Create | All data structures, pure functions, and `main()` |
| `tests/test_generate_changelog.py` | Create | Unit + integration tests for every function |
| `CHANGELOG.md` | Generate | Output artifact, produced by running the script |

---

## Task 1: Scaffold files and data structures

**Files:**
- Create: `generate_changelog.py`
- Create: `tests/__init__.py`
- Create: `tests/test_generate_changelog.py`

- [ ] **Step 1: Create the test file with imports**

```python
# tests/test_generate_changelog.py
import pandas as pd
import pytest
from pathlib import Path

# helpers shared across tests
def make_logid_df(fields, type_val='Traffic', category='forward'):
    """Build a minimal LOGID DataFrame for testing.
    fields: list of dicts with keys: name, type, length, desc
    """
    rows = []
    for f in fields:
        rows.append({
            'Log Field Name': f['name'],
            'Data Type': f.get('type', 'string'),
            'Length': f.get('length', '32'),
            'Description': f.get('desc', ''),
            'Type': type_val,
            'Category': category,
            'LOGID': '10',
            'Message_ID': '10',
            'Message_Description': 'TEST',
            'Message_Meaning': 'Test log',
            'Severity': 'Notice',
            'Version': '7.2.0',
        })
    return pd.DataFrame(rows)
```

- [ ] **Step 2: Create `generate_changelog.py` scaffold with imports and data structures**

```python
# generate_changelog.py
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
```

- [ ] **Step 3: Verify files exist (no tests yet)**

```bash
python3 -c "import generate_changelog; print('scaffold ok')"
```

Expected: `scaffold ok`

- [ ] **Step 4: Commit scaffold**

```bash
git add generate_changelog.py tests/__init__.py tests/test_generate_changelog.py
git commit -m "chore: scaffold generate_changelog.py with data structures and test file"
```

---

## Task 2: `discover_versions`

**Files:**
- Modify: `generate_changelog.py` — add `discover_versions`
- Modify: `tests/test_generate_changelog.py` — add tests

- [ ] **Step 1: Write the failing test**

Add to `tests/test_generate_changelog.py`:

```python
from generate_changelog import discover_versions

class TestDiscoverVersions:
    def test_finds_sorted_major_and_minor_dirs(self, tmp_path):
        (tmp_path / '7.2' / '7.2.0').mkdir(parents=True)
        (tmp_path / '7.2' / '7.2.1').mkdir(parents=True)
        (tmp_path / '7.2' / '7.2.10').mkdir(parents=True)
        (tmp_path / '7.4' / '7.4.0').mkdir(parents=True)
        (tmp_path / '7.4' / '7.4.1').mkdir(parents=True)
        (tmp_path / 'not_a_version').mkdir(parents=True)
        (tmp_path / '__pycache__').mkdir(parents=True)

        result = discover_versions(tmp_path)

        assert len(result) == 2
        assert result[0][0] == '7.2'
        assert [d.name for d in result[0][1]] == ['7.2.0', '7.2.1', '7.2.10']
        assert result[1][0] == '7.4'

    def test_version_sort_is_numeric_not_lexicographic(self, tmp_path):
        for v in ['7.2.9', '7.2.10', '7.2.2']:
            (tmp_path / '7.2' / v).mkdir(parents=True)

        result = discover_versions(tmp_path)
        names = [d.name for d in result[0][1]]
        assert names == ['7.2.2', '7.2.9', '7.2.10']

    def test_ignores_non_version_dirs(self, tmp_path):
        (tmp_path / 'README.md').touch()
        (tmp_path / '__pycache__').mkdir()
        result = discover_versions(tmp_path)
        assert result == []

    def test_returns_empty_when_no_minors(self, tmp_path):
        (tmp_path / '7.2').mkdir()
        result = discover_versions(tmp_path)
        assert result[0][1] == []
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_generate_changelog.py::TestDiscoverVersions -v
```

Expected: `FAILED` — `ImportError: cannot import name 'discover_versions'`

- [ ] **Step 3: Implement `discover_versions`**

Add to `generate_changelog.py` after the dataclasses:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_generate_changelog.py::TestDiscoverVersions -v
```

Expected: 4 tests PASSED

- [ ] **Step 5: Commit**

```bash
git add generate_changelog.py tests/test_generate_changelog.py
git commit -m "feat: add discover_versions with numeric minor version sorting"
```

---

## Task 3: `load_version`

**Files:**
- Modify: `generate_changelog.py` — add `load_version`
- Modify: `tests/test_generate_changelog.py` — add tests

- [ ] **Step 1: Write the failing test**

Add to `tests/test_generate_changelog.py`:

```python
from generate_changelog import load_version

class TestLoadVersion:
    def test_returns_dict_keyed_by_stem(self, tmp_path):
        df = make_logid_df([{'name': 'action', 'type': 'string', 'length': '32', 'desc': 'Act'}])
        df.to_csv(tmp_path / '10_-_LOG_ID_TRAFFIC_FORWARD.csv', index=False)

        result = load_version(tmp_path)

        assert '10_-_LOG_ID_TRAFFIC_FORWARD' in result
        assert len(result) == 1
        assert list(result['10_-_LOG_ID_TRAFFIC_FORWARD']['Log Field Name']) == ['action']

    def test_loads_multiple_csvs(self, tmp_path):
        for stem in ['10_TRAFFIC', '20_EVENT']:
            df = make_logid_df([{'name': 'x', 'type': 'string', 'length': '8', 'desc': 'd'}])
            df.to_csv(tmp_path / f'{stem}.csv', index=False)

        result = load_version(tmp_path)
        assert set(result.keys()) == {'10_TRAFFIC', '20_EVENT'}

    def test_empty_dir_returns_empty_dict(self, tmp_path):
        assert load_version(tmp_path) == {}

    def test_skips_unreadable_csv(self, tmp_path):
        (tmp_path / 'bad.csv').write_text('not,valid\ncsv,data\n,,broken')
        # Should not raise, just skip or load partially
        result = load_version(tmp_path)
        # bad.csv has no expected LOGID columns; we just verify no exception is raised
        assert isinstance(result, dict)
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_generate_changelog.py::TestLoadVersion -v
```

Expected: `FAILED` — `ImportError: cannot import name 'load_version'`

- [ ] **Step 3: Implement `load_version`**

Add to `generate_changelog.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_generate_changelog.py::TestLoadVersion -v
```

Expected: 4 tests PASSED

- [ ] **Step 5: Commit**

```bash
git add generate_changelog.py tests/test_generate_changelog.py
git commit -m "feat: add load_version to read LOGID CSVs from a minor version directory"
```

---

## Task 4: `classify_dataset`

**Files:**
- Modify: `generate_changelog.py` — add `classify_dataset`
- Modify: `tests/test_generate_changelog.py` — add tests

- [ ] **Step 1: Write the failing test**

Add to `tests/test_generate_changelog.py`:

```python
from generate_changelog import classify_dataset

class TestClassifyDataset:
    def test_traffic(self):
        assert classify_dataset(make_logid_df([{'name': 'x'}], type_val='Traffic')) == 'Traffic'

    def test_event(self):
        assert classify_dataset(make_logid_df([{'name': 'x'}], type_val='Event')) == 'Event'

    def test_gtp_excluded(self):
        assert classify_dataset(make_logid_df([{'name': 'x'}], type_val='GTP')) == 'GTP'

    def test_utm_webfilter(self):
        assert classify_dataset(make_logid_df([{'name': 'x'}], type_val='Webfilter')) == 'Webfilter'

    def test_utm_ips(self):
        assert classify_dataset(make_logid_df([{'name': 'x'}], type_val='IPS')) == 'IPS'

    def test_empty_dataframe(self):
        assert classify_dataset(pd.DataFrame()) == 'Unknown'
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_generate_changelog.py::TestClassifyDataset -v
```

Expected: `FAILED` — `ImportError: cannot import name 'classify_dataset'`

- [ ] **Step 3: Implement `classify_dataset`**

Add to `generate_changelog.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_generate_changelog.py::TestClassifyDataset -v
```

Expected: 6 tests PASSED

- [ ] **Step 5: Commit**

```bash
git add generate_changelog.py tests/test_generate_changelog.py
git commit -m "feat: add classify_dataset mirroring fortigate_fields.py log type logic"
```

---

## Task 5: `diff_logid`

**Files:**
- Modify: `generate_changelog.py` — add `_safe_str`, `_field_row`, `diff_logid`
- Modify: `tests/test_generate_changelog.py` — add tests

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_generate_changelog.py`:

```python
from generate_changelog import diff_logid

class TestDiffLogid:
    def _df(self, fields, **kw):
        return make_logid_df(fields, **kw)

    def test_added_field(self):
        prev = self._df([{'name': 'action', 'type': 'string', 'length': '32', 'desc': 'Act'}])
        curr = self._df([
            {'name': 'action', 'type': 'string', 'length': '32', 'desc': 'Act'},
            {'name': 'newfield', 'type': 'ip', 'length': '64', 'desc': 'New'},
        ])
        result = diff_logid(prev, curr)
        assert len(result.added_fields) == 1
        assert result.added_fields[0] == ('newfield', 'ip', '64', 'New')
        assert result.removed_fields == []

    def test_removed_field(self):
        prev = self._df([
            {'name': 'action', 'type': 'string', 'length': '32', 'desc': 'Act'},
            {'name': 'old', 'type': 'string', 'length': '16', 'desc': 'Old'},
        ])
        curr = self._df([{'name': 'action', 'type': 'string', 'length': '32', 'desc': 'Act'}])
        result = diff_logid(prev, curr)
        assert len(result.removed_fields) == 1
        assert result.removed_fields[0][0] == 'old'

    def test_type_changed(self):
        prev = self._df([{'name': 'srcip', 'type': 'string', 'length': '32', 'desc': 'IP'}])
        curr = self._df([{'name': 'srcip', 'type': 'ip', 'length': '32', 'desc': 'IP'}])
        result = diff_logid(prev, curr)
        assert result.type_changes == {'srcip': ('string', 'ip')}
        assert not result.added_fields
        assert not result.removed_fields

    def test_desc_changed(self):
        prev = self._df([{'name': 'action', 'type': 'string', 'length': '32', 'desc': 'Old desc'}])
        curr = self._df([{'name': 'action', 'type': 'string', 'length': '32', 'desc': 'New desc'}])
        result = diff_logid(prev, curr)
        assert result.desc_changes == {'action': ('Old desc', 'New desc')}

    def test_length_changed(self):
        prev = self._df([{'name': 'filename', 'type': 'string', 'length': '255', 'desc': 'File'}])
        curr = self._df([{'name': 'filename', 'type': 'string', 'length': '512', 'desc': 'File'}])
        result = diff_logid(prev, curr)
        assert result.length_changes == {'filename': ('255', '512')}

    def test_no_changes(self):
        df = self._df([{'name': 'action', 'type': 'string', 'length': '32', 'desc': 'Act'}])
        result = diff_logid(df, df.copy())
        assert not result.has_changes()

    def test_deduplicates_field_names(self):
        """If a field appears twice in a CSV, take last occurrence."""
        rows = [
            {'Log Field Name': 'action', 'Data Type': 'string', 'Length': '32',
             'Description': 'first', 'Type': 'Traffic', 'Category': 'forward',
             'LOGID': '10', 'Message_ID': '10', 'Message_Description': 'T',
             'Message_Meaning': 'T', 'Severity': 'Notice', 'Version': '7.2.0'},
            {'Log Field Name': 'action', 'Data Type': 'string', 'Length': '32',
             'Description': 'second', 'Type': 'Traffic', 'Category': 'forward',
             'LOGID': '10', 'Message_ID': '10', 'Message_Description': 'T',
             'Message_Meaning': 'T', 'Severity': 'Notice', 'Version': '7.2.0'},
        ]
        df = pd.DataFrame(rows)
        result = diff_logid(df, df.copy())
        assert not result.has_changes()
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_generate_changelog.py::TestDiffLogid -v
```

Expected: `FAILED` — `ImportError: cannot import name 'diff_logid'`

- [ ] **Step 3: Implement helpers and `diff_logid`**

Add to `generate_changelog.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_generate_changelog.py::TestDiffLogid -v
```

Expected: 7 tests PASSED

- [ ] **Step 5: Commit**

```bash
git add generate_changelog.py tests/test_generate_changelog.py
git commit -m "feat: add diff_logid for field-level comparison between LOGID versions"
```

---

## Task 6: `diff_versions`

**Files:**
- Modify: `generate_changelog.py` — add `diff_versions`
- Modify: `tests/test_generate_changelog.py` — add tests

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_generate_changelog.py`:

```python
from generate_changelog import diff_versions

def _make_vdict(specs):
    """specs: dict of {stem: (list_of_fields, type_val)}"""
    result = {}
    for stem, (fields, type_val) in specs.items():
        result[stem] = make_logid_df(fields, type_val=type_val)
    return result

class TestDiffVersions:
    def test_added_logid(self):
        prev = _make_vdict({'10_T': ([{'name': 'a', 'type': 'string', 'length': '32', 'desc': 'd'}], 'Traffic')})
        curr = _make_vdict({
            '10_T': ([{'name': 'a', 'type': 'string', 'length': '32', 'desc': 'd'}], 'Traffic'),
            '20_N': ([{'name': 'b', 'type': 'ip', 'length': '64', 'desc': 'n'}], 'Traffic'),
        })
        result = diff_versions(prev, curr)
        assert '20_N' in result.added_logids
        assert result.added_logids['20_N'] == 'Traffic'
        assert not result.removed_logids

    def test_removed_logid(self):
        prev = _make_vdict({
            '10_T': ([{'name': 'a', 'type': 'string', 'length': '32', 'desc': 'd'}], 'Traffic'),
            '20_O': ([{'name': 'b', 'type': 'ip', 'length': '64', 'desc': 'o'}], 'Event'),
        })
        curr = _make_vdict({'10_T': ([{'name': 'a', 'type': 'string', 'length': '32', 'desc': 'd'}], 'Traffic')})
        result = diff_versions(prev, curr)
        assert '20_O' in result.removed_logids
        assert result.removed_logids['20_O'] == 'Event'

    def test_field_change_captured_with_dataset_label(self):
        prev = _make_vdict({'10_T': ([{'name': 'srcip', 'type': 'string', 'length': '32', 'desc': 'IP'}], 'Traffic')})
        curr = _make_vdict({'10_T': ([{'name': 'srcip', 'type': 'ip', 'length': '32', 'desc': 'IP'}], 'Traffic')})
        result = diff_versions(prev, curr)
        assert '10_T' in result.logid_diffs
        label, d = result.logid_diffs['10_T']
        assert label == 'Traffic'
        assert 'srcip' in d.type_changes

    def test_unchanged_logid_not_in_diffs(self):
        spec = {'10_T': ([{'name': 'a', 'type': 'string', 'length': '32', 'desc': 'd'}], 'Traffic')}
        result = diff_versions(_make_vdict(spec), _make_vdict(spec))
        assert not result.has_changes()

    def test_utm_subtype_added(self):
        prev = _make_vdict({'10_W': ([{'name': 'x', 'type': 'string', 'length': '8', 'desc': 'd'}], 'Webfilter')})
        curr = _make_vdict({
            '10_W': ([{'name': 'x', 'type': 'string', 'length': '8', 'desc': 'd'}], 'Webfilter'),
            '20_I': ([{'name': 'y', 'type': 'string', 'length': '8', 'desc': 'd'}], 'IPS'),
        })
        result = diff_versions(prev, curr)
        assert 'IPS' in result.utmtype_added
        assert 'Webfilter' not in result.utmtype_added

    def test_utm_subtype_removed(self):
        prev = _make_vdict({
            '10_W': ([{'name': 'x', 'type': 'string', 'length': '8', 'desc': 'd'}], 'Webfilter'),
            '20_I': ([{'name': 'y', 'type': 'string', 'length': '8', 'desc': 'd'}], 'IPS'),
        })
        curr = _make_vdict({'10_W': ([{'name': 'x', 'type': 'string', 'length': '8', 'desc': 'd'}], 'Webfilter')})
        result = diff_versions(prev, curr)
        assert 'IPS' in result.utmtype_removed
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_generate_changelog.py::TestDiffVersions -v
```

Expected: `FAILED` — `ImportError: cannot import name 'diff_versions'`

- [ ] **Step 3: Implement `diff_versions`**

Add to `generate_changelog.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_generate_changelog.py::TestDiffVersions -v
```

Expected: 7 tests PASSED

- [ ] **Step 5: Commit**

```bash
git add generate_changelog.py tests/test_generate_changelog.py
git commit -m "feat: add diff_versions to compare two loaded minor version dicts"
```

---

## Task 7: Render helpers

**Files:**
- Modify: `generate_changelog.py` — add `_truncate`, `_render_logid_diff`, `_render_version_pair`
- Modify: `tests/test_generate_changelog.py` — add tests

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_generate_changelog.py`:

```python
from generate_changelog import _truncate, _render_version_pair, LogidDiff, VersionDiff

class TestTruncate:
    def test_short_string_unchanged(self):
        assert _truncate('hello') == 'hello'

    def test_long_string_truncated(self):
        result = _truncate('x' * 200)
        assert len(result) == 121  # 120 chars + ellipsis
        assert result.endswith('…')

    def test_newlines_replaced_with_spaces(self):
        assert '\n' not in _truncate('line1\nline2')

class TestRenderVersionPair:
    def _no_change_diff(self):
        return VersionDiff({}, {}, {}, set(), set())

    def _logid_diff(self, **kw):
        defaults = dict(added_fields=[], removed_fields=[], type_changes={},
                        desc_changes={}, length_changes={})
        defaults.update(kw)
        return LogidDiff(**defaults)

    def test_no_changes_emits_no_changes_note(self):
        output = _render_version_pair('7.2.0', '7.2.1', self._no_change_diff())
        assert '### 7.2.0 → 7.2.1' in output
        assert '*(no changes)*' in output

    def test_summary_counts_added_logid(self):
        diff = VersionDiff(
            added_logids={'10_T': 'Traffic'}, removed_logids={},
            logid_diffs={}, utmtype_added=set(), utmtype_removed=set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '1 LOGID added, 0 removed' in output
        assert '10_T *(new)*' in output

    def test_summary_counts_removed_logid(self):
        diff = VersionDiff(
            added_logids={}, removed_logids={'20_E': 'Event'},
            logid_diffs={}, utmtype_added=set(), utmtype_removed=set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '0 LOGID added, 1 removed' in output
        assert '20_E *(removed)*' in output

    def test_field_added_rendered(self):
        d = self._logid_diff(added_fields=[('newf', 'ip', '64', 'New field desc')])
        diff = VersionDiff({}, {}, {'10_T': ('Traffic', d)}, set(), set())
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert 'Field added: `newf` (ip, len: 64)' in output
        assert 'New field desc' in output

    def test_type_change_rendered(self):
        d = self._logid_diff(type_changes={'action': ('string', 'ip')})
        diff = VersionDiff({}, {}, {'10_T': ('Traffic', d)}, set(), set())
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert 'Type changed: `action` `string` → `ip`' in output

    def test_desc_change_rendered(self):
        d = self._logid_diff(desc_changes={'action': ('Old', 'New')})
        diff = VersionDiff({}, {}, {'10_T': ('Traffic', d)}, set(), set())
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert 'Description changed: `action`' in output
        assert 'Before: "Old"' in output
        assert 'After:  "New"' in output

    def test_length_change_rendered(self):
        d = self._logid_diff(length_changes={'filename': ('255', '512')})
        diff = VersionDiff({}, {}, {'10_T': ('Traffic', d)}, set(), set())
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert 'Length changed: `filename` 255 → 512' in output

    def test_utm_subtypes_shown(self):
        diff = VersionDiff(
            added_logids={'10_I': 'IPS'}, removed_logids={},
            logid_diffs={}, utmtype_added={'IPS'}, utmtype_removed=set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert 'new subtypes: IPS' in output

    def test_dataset_grouping(self):
        d_t = self._logid_diff(added_fields=[('x', 'string', '8', 'desc')])
        d_e = self._logid_diff(added_fields=[('y', 'string', '8', 'desc')])
        diff = VersionDiff(
            {}, {},
            {'10_T': ('Traffic', d_t), '20_E': ('Event', d_e)},
            set(), set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert output.index('#### Traffic') < output.index('10_T')
        assert output.index('#### Event') < output.index('20_E')
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_generate_changelog.py::TestTruncate tests/test_generate_changelog.py::TestRenderVersionPair -v
```

Expected: `FAILED` — `ImportError`

- [ ] **Step 3: Implement render helpers**

Add to `generate_changelog.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_generate_changelog.py::TestTruncate tests/test_generate_changelog.py::TestRenderVersionPair -v
```

Expected: 11 tests PASSED

- [ ] **Step 5: Commit**

```bash
git add generate_changelog.py tests/test_generate_changelog.py
git commit -m "feat: add render helpers _truncate, _render_logid_diff, _render_version_pair"
```

---

## Task 8: `main` and integration test

**Files:**
- Modify: `generate_changelog.py` — add `main()`
- Modify: `tests/test_generate_changelog.py` — add integration test

- [ ] **Step 1: Write the integration test**

Add to `tests/test_generate_changelog.py`:

```python
from generate_changelog import discover_versions, load_version, diff_versions, _render_version_pair

class TestIntegration:
    def test_end_to_end_diff_pipeline(self, tmp_path):
        # Set up two minor versions under a fake major
        v1_dir = tmp_path / '7.2' / '7.2.0'
        v2_dir = tmp_path / '7.2' / '7.2.1'
        v1_dir.mkdir(parents=True)
        v2_dir.mkdir(parents=True)

        # v1: LOGID 10, field 'action' typed string
        df1 = make_logid_df([{'name': 'action', 'type': 'string', 'length': '32', 'desc': 'Act'}])
        df1.to_csv(v1_dir / '10_-_LOG_ID_TRAFFIC_FORWARD.csv', index=False)

        # v2: LOGID 10 with type changed; new LOGID 20 added
        df2 = make_logid_df([{'name': 'action', 'type': 'ip', 'length': '32', 'desc': 'Act'}])
        df2.to_csv(v2_dir / '10_-_LOG_ID_TRAFFIC_FORWARD.csv', index=False)
        df_new = make_logid_df([{'name': 'srcip', 'type': 'ip', 'length': '64', 'desc': 'Src'}])
        df_new.to_csv(v2_dir / '20_-_LOG_ID_TRAFFIC_NEW.csv', index=False)

        # Run pipeline
        groups = discover_versions(tmp_path)
        assert len(groups) == 1
        major, minors = groups[0]
        assert major == '7.2'
        assert len(minors) == 2

        prev = load_version(minors[0])
        curr = load_version(minors[1])
        diff = diff_versions(prev, curr)

        assert '20_-_LOG_ID_TRAFFIC_NEW' in diff.added_logids
        assert '10_-_LOG_ID_TRAFFIC_FORWARD' in diff.logid_diffs
        _, d = diff.logid_diffs['10_-_LOG_ID_TRAFFIC_FORWARD']
        assert d.type_changes == {'action': ('string', 'ip')}

        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '20_-_LOG_ID_TRAFFIC_NEW *(new)*' in output
        assert 'Type changed: `action` `string` → `ip`' in output
        assert '**Summary:** 1 LOGID added, 0 removed' in output
```

- [ ] **Step 2: Run test to verify it passes with current code (it should — it only tests pure functions)**

```bash
pytest tests/test_generate_changelog.py::TestIntegration -v
```

Expected: PASSED (pipeline functions already implemented)

- [ ] **Step 3: Implement `main()`**

Add to `generate_changelog.py`:

```python
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
```

- [ ] **Step 4: Run all tests to confirm nothing broke**

```bash
pytest tests/test_generate_changelog.py -v
```

Expected: all tests PASSED

- [ ] **Step 5: Run against real data and inspect output**

```bash
python3 generate_changelog.py
```

Expected: `Written: /home/dragon/flores/CHANGELOG.md (N bytes)` — no errors or tracebacks.

```bash
head -80 CHANGELOG.md
```

Verify: opens with `# FortiGate Log Field Changelog`, has `## 7.2`, `### 7.2.0 → 7.2.1`, Summary line, dataset sections.

- [ ] **Step 6: Spot-check a known diff manually**

Pick a LOGID that exists in both `7.2/7.2.0/` and `7.2/7.2.1/`. Compare the two CSV files:

```bash
ls 7.2/7.2.0/ | head -5
```

Pick any stem, e.g. `10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY`, and verify:

```bash
python3 -c "
import pandas as pd
from pathlib import Path
stem = '10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY'
p = pd.read_csv(f'7.2/7.2.0/{stem}.csv')[['Log Field Name','Data Type','Length']].set_index('Log Field Name')
c = pd.read_csv(f'7.2/7.2.1/{stem}.csv')[['Log Field Name','Data Type','Length']].set_index('Log Field Name')
print('In 7.2.1 not 7.2.0:', set(c.index) - set(p.index))
print('In 7.2.0 not 7.2.1:', set(p.index) - set(c.index))
"
```

Confirm the CHANGELOG.md reflects what the raw diff shows.

- [ ] **Step 7: Commit final script and generated changelog**

```bash
git add generate_changelog.py tests/test_generate_changelog.py CHANGELOG.md
git commit -m "feat: add generate_changelog.py and initial CHANGELOG.md"
```

---

## Verification Checklist

Run this after Task 8 is complete:

- [ ] `pytest tests/test_generate_changelog.py -v` — all tests PASS
- [ ] `python3 generate_changelog.py` — exits cleanly, prints byte count
- [ ] `CHANGELOG.md` renders correctly in a Markdown viewer
- [ ] GTP LOGIDs do not appear anywhere in `CHANGELOG.md` (`grep -i gtp CHANGELOG.md` returns nothing)
- [ ] Every `### X.Y.Z → X.Y.(Z+1)` section is present even if it has `*(no changes)*`
- [ ] At least one type change, description change, or length change appears in the output (real data validation)
