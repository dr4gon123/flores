import pandas as pd
import pytest
from pathlib import Path
from generate_changelog import discover_versions, load_version, classify_dataset

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
