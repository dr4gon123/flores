import pandas as pd
import pytest
from pathlib import Path
from generate_changelog import discover_versions, load_version

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
