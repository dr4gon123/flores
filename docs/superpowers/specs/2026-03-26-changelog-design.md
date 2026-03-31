# Design: FortiGate Log Field Changelog Generator

**Date:** 2026-03-26
**Status:** Approved

## Context

The FLORES pipeline scrapes FortiGate log field documentation across multiple FortiOS minor versions (7.2.0 through 7.2.13, 7.4.0 through 7.4.11, 7.6.0 through 7.6.6, etc.). The existing scripts (`unique_fields.py`, `fortigate_fields.py`) detect intra-version inconsistencies (type conflicts, description variations) but produce no cross-version diff. Admins and SIEM engineers need to know what actually changed between patch releases — which log IDs were added or removed, which fields changed type, which descriptions were updated — without manually comparing CSVs.

This design specifies a new standalone script `generate_changelog.py` that reads the existing raw LOGID CSVs and writes a human-readable `CHANGELOG.md` at the repo root.

---

## Scope

- **Comparison granularity:** Minor-to-minor within each major version only (e.g., 7.2.0 → 7.2.1 → … → 7.2.13). No cross-major transitions.
- **Data source:** Raw LOGID CSVs in `<major>/<minor>/` directories. Not the consolidated `unique_fields/` or `field_descriptions/` outputs (those are per-major, not per-minor).
- **Output:** `CHANGELOG.md` at repo root, fully regenerated on each run.

---

## Change Types Tracked

| Change | Source column | Granularity |
|---|---|---|
| LOGID added / removed | filename | per dataset (Traffic / Event / UTM) |
| Field added / removed | `Log Field Name` | per LOGID |
| Data type changed | `Data Type` | per field per LOGID |
| Description changed | `Description` | per field per LOGID |
| Field length changed | `Length` | per field per LOGID |
| UTM subtype added / removed | `Type` column | per major version section |
| Summary counts | derived | top of each version-pair section |

**Explicitly excluded:** severity changes, LOGID `Message_Meaning` changes, category/subtype reassignment per LOGID.

---

## Architecture

### Functions

```
generate_changelog.py
│
├── discover_versions(root) → list[(major_label, [minor_dir, ...])]
│     Walks root for dirs matching \d+\.\d+ (major) containing \d+\.\d+\.\d+ (minor)
│     Returns majors sorted ascending; minors within each major sorted ascending
│
├── load_version(minor_dir) → dict[logid_stem → pd.DataFrame]
│     Reads all *.csv from one minor version directory
│     Key = filename stem (e.g., "10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY")
│     Skips non-LOGID files (e.g., anything not matching the LOGID pattern)
│
├── classify_dataset(df) → "Traffic" | "Event" | str
│     Returns the dataset bucket for a LOGID DataFrame
│     Mirrors the Type/Category logic in fortigate_fields.py:
│       - Type == "Traffic" → "Traffic"
│       - Type == "Event"   → "Event"
│       - GTP              → excluded (EXCLUDED_TYPES constant)
│       - Everything else  → UTM (value = the Type column, e.g. "Webfilter", "IPS")
│
├── diff_logid(prev_df, curr_df) → LogidDiff
│     Field-level comparison between two versions of the same LOGID:
│       - added_fields:    fields in curr not in prev
│       - removed_fields:  fields in prev not in curr
│       - type_changes:    {field: (old_type, new_type)} for shared fields
│       - desc_changes:    {field: (old_desc, new_desc)} for shared fields
│       - length_changes:  {field: (old_len, new_len)} for shared fields
│
├── diff_versions(prev_dict, curr_dict) → VersionDiff
│     - added_logids:   logids in curr not in prev (with their dataset label)
│     - removed_logids: logids in prev not in curr (with their dataset label)
│     - logid_diffs:    {logid_stem: LogidDiff} for shared logids with changes
│     - utmtype_added / utmtype_removed: UTM subtype labels appearing/disappearing
│
├── render_markdown(major_label, version_pairs, diffs) → str
│     Renders one ## <major> section with ### <v_prev> → <v_curr> subsections
│     Structure per version-pair:
│       **Summary:** N LOGIDs added, M removed | K fields added, L removed |
│                   P types changed | Q descriptions changed | R lengths changed
│       #### Traffic
│         ##### <logid_stem>
│           - LOGID added  (or) Field added/removed/changed lines
│       #### Event
│       #### UTM — new subtypes: X | removed: Y
│         ##### <logid_stem>
│           ...
│     If no changes in a version pair: emit "*(no changes)*" under the header.
│
└── main()
      root = repo root (script location)
      version_groups = discover_versions(root)
      sections = []
      for major_label, minor_dirs in version_groups:
          pairs = zip(minor_dirs, minor_dirs[1:])
          diffs = [diff_versions(load_version(a), load_version(b)) for a, b in pairs]
          sections.append(render_markdown(major_label, pairs, diffs))
      write CHANGELOG.md = header + "\n\n".join(sections)
```

### Data structures

```python
@dataclass
class LogidDiff:
    added_fields:   list[tuple[str, str, str, str]]  # (name, type, length, desc)
    removed_fields: list[tuple[str, str, str, str]]
    type_changes:   dict[str, tuple[str, str]]        # field → (old, new)
    desc_changes:   dict[str, tuple[str, str]]        # field → (old, new)
    length_changes: dict[str, tuple[str, str]]        # field → (old, new)

@dataclass
class VersionDiff:
    added_logids:    dict[str, str]   # logid_stem → dataset_label
    removed_logids:  dict[str, str]
    logid_diffs:     dict[str, LogidDiff]
    utmtype_added:   set[str]
    utmtype_removed: set[str]
```

---

## Output Format

```markdown
# FortiGate Log Field Changelog

## 7.2

### 7.2.0 → 7.2.1

**Summary:** 1 LOGID added, 0 removed | 3 fields added, 0 removed | 1 type changed | 2 descriptions changed | 0 lengths changed

#### Traffic

##### 10 - LOG_ID_TRAFFIC_EXPLICIT_PROXY *(new)*

##### 20 - LOG_ID_TRAFFIC_FORWARD
- Field added: `newfield` (string, len: 32) — "Newly documented field"
- Type changed: `action` `string` → `ip`
- Description changed: `dstcountry`
  - Before: "Destination country"
  - After:  "Destination country code"

#### Event

*(no changes)*

#### UTM — new subtypes: FILE-FILTER | removed subtypes: *(none)*

##### 1600 - LOG_ID_UTM_VIRUS_DETECTED
- Field removed: `legacyfield` (string)
- Length changed: `filename` 255 → 512

---

### 7.2.1 → 7.2.2

*(no changes)*
```

**Description diffs** are shown inline, truncated to 120 characters if longer (with `…` suffix).

---

## Key Design Decisions

- **Reuse GTP exclusion constant:** Import or replicate `EXCLUDED_TYPES = {'GTP'}` to stay consistent with the other scripts.
- **Dataset classification:** Mirrors `fortigate_fields.py` logic exactly (Traffic/Event/UTM by `Type` column; UTM subtype = `Type` value).
- **No-change versions:** Always emit the `### X → Y` header with `*(no changes)*` so every transition is explicitly accounted for in the changelog.
- **Overwrite on each run:** `CHANGELOG.md` is fully regenerated. It is a derived artifact, not hand-maintained.
- **Filename-stem as LOGID key:** Use the CSV filename stem as the identity key for a LOGID. This is stable across versions and human-readable.

---

## Files Modified

| File | Action |
|---|---|
| `generate_changelog.py` | Create (new script) |
| `CHANGELOG.md` | Create (generated output) |

No existing scripts are modified.

---

## Verification

1. Run `python3 generate_changelog.py` from repo root — should produce `CHANGELOG.md` with no errors.
2. Spot-check: open `7.2/7.2.0/` and `7.2/7.2.1/` manually; confirm that a LOGID present in one but not the other appears in the diff.
3. Spot-check: pick a field in a shared LOGID, manually edit its type in a test copy, rerun, confirm the type change appears.
4. Confirm GTP LOGIDs do not appear in the output.
5. Confirm `CHANGELOG.md` is valid Markdown (renders correctly in a viewer).
