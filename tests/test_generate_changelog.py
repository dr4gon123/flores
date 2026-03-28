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
        assert result.added_logids['20_N'][0] == 'Traffic'
        assert not result.removed_logids

    def test_removed_logid(self):
        prev = _make_vdict({
            '10_T': ([{'name': 'a', 'type': 'string', 'length': '32', 'desc': 'd'}], 'Traffic'),
            '20_O': ([{'name': 'b', 'type': 'ip', 'length': '64', 'desc': 'o'}], 'Event'),
        })
        curr = _make_vdict({'10_T': ([{'name': 'a', 'type': 'string', 'length': '32', 'desc': 'd'}], 'Traffic')})
        result = diff_versions(prev, curr)
        assert '20_O' in result.removed_logids
        assert result.removed_logids['20_O'][0] == 'Event'

    def test_field_change_captured_with_dataset_label(self):
        prev = _make_vdict({'10_T': ([{'name': 'srcip', 'type': 'string', 'length': '32', 'desc': 'IP'}], 'Traffic')})
        curr = _make_vdict({'10_T': ([{'name': 'srcip', 'type': 'ip', 'length': '32', 'desc': 'IP'}], 'Traffic')})
        result = diff_versions(prev, curr)
        assert '10_T' in result.logid_diffs
        label, extra, d = result.logid_diffs['10_T']
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

    def test_gtp_logid_included(self):
        prev = _make_vdict({'10_G': ([{'name': 'x', 'type': 'string', 'length': '8', 'desc': 'd'}], 'GTP')})
        curr = _make_vdict({
            '10_G': ([{'name': 'x', 'type': 'string', 'length': '8', 'desc': 'd'}], 'GTP'),
            '20_G': ([{'name': 'y', 'type': 'string', 'length': '8', 'desc': 'n'}], 'GTP'),
        })
        result = diff_versions(prev, curr)
        assert '10_G' not in result.logid_diffs       # unchanged, so not in diffs
        assert '20_G' in result.added_logids           # new GTP LOGID is tracked
        assert result.added_logids['20_G'][0] == 'GTP'
        # GTP was already in prev so utmtype_added is empty; only new subtypes appear there
        assert 'GTP' not in result.utmtype_added


from generate_changelog import _cell_desc, _render_version_pair, LogidDiff, VersionDiff


class TestCellDesc:
    def test_empty_string_returns_empty_marker(self):
        assert _cell_desc('') == '*(empty)*'

    def test_single_line_unchanged(self):
        assert _cell_desc('hello') == 'hello'

    def test_lf_converted_to_br(self):
        result = _cell_desc('line1\nline2')
        assert result == 'line1<br>line2'

    def test_crlf_converted_to_br(self):
        result = _cell_desc('line1\r\nline2')
        assert result == 'line1<br>line2'

    def test_cr_converted_to_br(self):
        result = _cell_desc('line1\rline2')
        assert result == 'line1<br>line2'

    def test_trailing_whitespace_stripped_per_line(self):
        result = _cell_desc('line1   \nline2  ')
        assert result == 'line1<br>line2'

    def test_multiline_preserved_in_full(self):
        desc = 'Security action:\n  detected - not blocked\n  blocked - blocked'
        result = _cell_desc(desc)
        assert '<br>' in result
        assert 'detected - not blocked' in result
        assert 'blocked - blocked' in result

class TestRenderVersionPair:
    def _no_change_diff(self):
        return VersionDiff({}, {}, {}, set(), set())

    def _logid_diff(self, **kw):
        defaults = dict(added_fields=[], removed_fields=[], type_changes={},
                        desc_changes={}, length_changes={},
                        severity_change=None, message_desc_change=None, category_change=None)
        defaults.update(kw)
        return LogidDiff(**defaults)

    def test_no_changes_emits_no_changes_note(self):
        output = _render_version_pair('7.2.0', '7.2.1', self._no_change_diff())
        assert '### 7.2.0 → 7.2.1' in output
        assert '*(no changes)*' in output

    def test_summary_counts_added_logid(self):
        diff = VersionDiff(
            added_logids={'10_T': ('Traffic', 'forward')}, removed_logids={},
            logid_diffs={}, utmtype_added=set(), utmtype_removed=set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '| LOGIDs added | 1 |' in output
        assert '| LOGIDs removed | 0 |' in output
        assert '`10_T`' in output

    def test_summary_counts_removed_logid(self):
        diff = VersionDiff(
            added_logids={}, removed_logids={'20_E': ('Event', 'system')},
            logid_diffs={}, utmtype_added=set(), utmtype_removed=set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '| LOGIDs added | 0 |' in output
        assert '| LOGIDs removed | 1 |' in output
        assert '`20_E`' in output

    def test_field_added_rendered(self):
        d = self._logid_diff(added_fields=[('newf', 'ip', '64', 'New field desc')])
        diff = VersionDiff({}, {}, {'10_T': ('Traffic', 'forward', d)}, set(), set())
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '`newf`' in output
        assert 'New field desc' in output
        assert '`ip`' in output

    def test_type_change_rendered(self):
        d = self._logid_diff(type_changes={'action': ('string', 'ip')})
        diff = VersionDiff({}, {}, {'10_T': ('Traffic', 'forward', d)}, set(), set())
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '`action`' in output
        assert '`string`' in output
        assert '`ip`' in output
        assert 'Type changes' in output

    def test_desc_change_rendered(self):
        d = self._logid_diff(desc_changes={'action': ('Old', 'New')})
        diff = VersionDiff({}, {}, {'10_T': ('Traffic', 'forward', d)}, set(), set())
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '`action`' in output
        assert 'Old' in output
        assert 'New' in output
        assert 'Description changes' in output

    def test_length_change_rendered(self):
        d = self._logid_diff(length_changes={'filename': ('255', '512')})
        diff = VersionDiff({}, {}, {'10_T': ('Traffic', 'forward', d)}, set(), set())
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '`filename`' in output
        assert '255' in output
        assert '512' in output
        assert 'Length changes' in output

    def test_utm_subtypes_shown(self):
        diff = VersionDiff(
            added_logids={'10_I': ('IPS', 'IPS')}, removed_logids={},
            logid_diffs={}, utmtype_added={'IPS'}, utmtype_removed=set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert 'new subtypes: IPS' in output

    def test_dataset_grouping(self):
        d_t = self._logid_diff(added_fields=[('x', 'string', '8', 'desc')])
        d_e = self._logid_diff(added_fields=[('y', 'string', '8', 'desc')])
        diff = VersionDiff(
            {}, {},
            {'10_T': ('Traffic', 'forward', d_t), '20_E': ('Event', 'system', d_e)},
            set(), set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        # Field 'x' appears in Traffic section, 'y' in Event section
        assert output.index('#### Traffic') < output.index('`x`')
        assert output.index('#### Event') < output.index('`y`')

    def test_traffic_no_category_column(self):
        """Traffic field tables must not have a Category column."""
        d = self._logid_diff(added_fields=[('saasname', 'string', '80', '')])
        # Two Traffic LOGIDs in different categories — should merge into one row
        diff = VersionDiff(
            {}, {},
            {
                '10_FWD': ('Traffic', 'forward', d),
                '14_LCL': ('Traffic', 'local',   d),
            },
            set(), set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert 'Category' not in output
        # saasname appears exactly once (merged)
        assert output.count('`saasname`') == 1
        # Summary counts 1 unique field name, not 2 raw additions
        assert '| Fields added | 1 |' in output

    def test_summary_counts_unique_field_names(self):
        """Fields added/removed counts reflect unique field names, not raw per-LOGID pairs."""
        # Same field added across 3 LOGIDs
        d = self._logid_diff(added_fields=[('f', 'string', '8', 'desc')])
        diff = VersionDiff(
            {}, {},
            {
                'A': ('Traffic', 'forward', d),
                'B': ('Traffic', 'local',   d),
                'C': ('Traffic', 'multicast', d),
            },
            set(), set(),
        )
        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '| Fields added | 1 |' in output  # 1 unique field, not 3


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
        _, _, d = diff.logid_diffs['10_-_LOG_ID_TRAFFIC_FORWARD']
        assert d.type_changes == {'action': ('string', 'ip')}

        output = _render_version_pair('7.2.0', '7.2.1', diff)
        assert '20_-_LOG_ID_TRAFFIC_NEW' in output  # appears in LOGIDs added table
        assert '`action`' in output                  # appears in Type changes table
        assert '`string`' in output
        assert '`ip`' in output
        assert '| LOGIDs added | 1 |' in output
