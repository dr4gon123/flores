# FLORES — Developers Guide

This guide documents the internal design, data flow, and key implementation decisions for FLORES. It is intended for maintainers adding new FortiOS versions, extending output formats, or debugging scraper failures.

---

## Architecture Overview

FLORES is a two-script pipeline. The scraper fetches raw HTML and emits CSVs; `generate_changelog.py` consumes those CSVs and produces all downstream outputs.

```
fortigate_scraper_config.yaml
          │
          ▼
fortigate_scraper.py  ──►  <major>/<minor>/LOGID/<LOGID>.csv  (raw, one CSV per log ID)
                                    │
                                    ▼
                          generate_changelog.py
                          ├── --changelog   → <major>/<minor>/CHANGELOG.md
                          ├── --matrices    → <major>/<minor>/*_matrix.csv
                          ├── --fields      → <major>/fields/traffic_fields.csv
                          │                   <major>/fields/event_fields.csv
                          │                   <major>/fields/utm_fields.csv
                          │                   <major>/fields/action_descriptions.csv
                          └── --index       → INDEX.md
                                    │
                                    ▼
                          generate_ecs_mappings.py
                          └──────────────────────→ <major>/ECS/traffic_ecs.csv
                                                    <major>/ECS/event_ecs.csv
                                                    <major>/ECS/utm_ecs.csv
```

**Files and their roles:**

| File | Role |
|------|------|
| `fortigate_scraper.py` | HTTP scraper — fetches Fortinet docs, extracts log tables, saves raw CSVs |
| `fortigate_scraper_config.yaml` | Configuration: versions list, rate limiting, output directory, flags |
| `generate_changelog.py` | All downstream analysis: changelogs, field matrices, and consolidated field CSVs |

---

## Pipeline Flow

```
fortigate_scraper_config.yaml
        │
        ▼
FortiGateLogScraper.__init__()
  ├─ _load_config()          — YAML → dict
  ├─ requests.Session()      — shared HTTP session with browser User-Agent
  └─ sets: versions, output_dir, base_delay, max_retries, retry_backoff, force_rescrape, dry_run
        │
        ▼
run()
  ├─ [dry_run=true]  → print plan and exit
  └─ [specific_versions provided] → use them directly
     [otherwise]                  → use self.versions (all configured versions)
              │
              ▼
        for each version:
          scrape_version(version)
            ├─ get_version_dirs()      → (major_dir, minor_dir)
            ├─ get_version_url()       → docs.fortinet.com URL
            ├─ get_page_content(url)   → BeautifulSoup (with rate limit sleep)
            ├─ extract_logid_links()   → {description: full_url}
            │     regex: r'/(\d{1,6})-(logid|log-id|mesgid)-[^/]*$'
            └─ for each LOGID link:
                 [force_rescrape=false] → skip if <minor_dir>/LOGID/<safe_logid>.csv exists
                 get_page_content(logid_url)
                 ├─ extract_log_metadata() → Message_ID, Type, Category, Severity, ...
                 └─ extract_log_table()    → DataFrame (fields + metadata columns)
                       │
                       ▼
                   df['Version'] = version
                   df.to_csv(minor_dir/LOGID/<safe_logid>.csv)

─── After scraping ─────────────────────────────────────────────────────────────

generate_changelog.py
        │
        ▼
discover_versions(root)
  └─ for each major: sorted minor_dirs
          │
          ▼
  load_version(minor_dir)  → dict[stem, DataFrame]  (one DataFrame per LOGID CSV)
          │
          ├─ [--changelog / --matrices]
          │    snapshot_version()  → VersionSnapshot  (intra-version conflicts)
          │    diff_versions(prev, curr)  → VersionDiff  (inter-version changes)
          │    _write_minor_analysis()
          │        ├── CHANGELOG.md
          │        ├── traffic_matrix.csv
          │        ├── event_matrix.csv
          │        └── utm_matrix.csv
          │
          └─ [--fields]  (accumulates all_stems across all minor versions first)
               _write_major_fields()
                   ├── _consolidate_fields(all_stems, 'Traffic', 'Category')
                   │       → fields/traffic_fields.csv
                   ├── _consolidate_fields(all_stems, 'Event', 'Category')
                   │       → fields/event_fields.csv
                   ├── _consolidate_fields(all_stems, None, 'Type')  [UTM]
                   │       → fields/utm_fields.csv
                   └── _consolidate_action_descriptions(all_stems)
                           → fields/action_descriptions.csv
```

---

## Script 1: fortigate_scraper.py

### Purpose

Fetches the Fortinet Log Message Reference for each configured FortiOS version, extracts all log ID pages, and writes one CSV file per log ID into a versioned directory structure.

### Configuration (fortigate_scraper_config.yaml)

| Key | Default | Description |
|-----|---------|-------------|
| `versions` | (required) | List of FortiOS versions to scrape, e.g. `"7.6.4"` |
| `settings.base_delay` | `1.0` | Seconds to sleep between HTTP requests |
| `settings.max_retries` | `3` | Number of additional attempts per URL after an error (0 = no retries) |
| `settings.retry_backoff` | `2.0` | Exponential backoff multiplier: wait = `base_delay × (retry_backoff ^ attempt)` + jitter |
| `settings.force_rescrape` | `false` | If true, re-scrape versions that already have CSV files |
| `settings.dry_run` | `false` | If true, print the plan without making any HTTP requests |
| `settings.output_dir` | `"."` | Root output directory for scraped data |

The config file is located relative to the script file, not the working directory. `_load_config()` uses `Path(__file__).parent` to find it.

### Class: FortiGateLogScraper

Single-class design — all scraping logic lives here. A `requests.Session` is reused across all requests for HTTP connection pooling and shared headers. Rate limiting is enforced inside `get_page_content()` via `time.sleep(self.base_delay)` after every successful fetch.

### Rate Limiting and Retry Behavior

`get_page_content()` retries transient failures with exponential backoff and jitter:

- **Retry loop**: `max_retries + 1` total attempts per URL. Set `max_retries: 0` to disable retries entirely.
- **429 Rate Limited**: If the server responds with HTTP 429, the scraper reads the `Retry-After` response header (if present) or falls back to `base_delay × (retry_backoff ^ attempt)`. It then retries without counting this as an error.
- **Other HTTP / network errors**: On each failure before the last attempt, the scraper waits `base_delay × (retry_backoff ^ attempt) + random.uniform(0, 1)` seconds (jitter prevents thundering-herd on parallel runs). On the final attempt, the error is logged and `None` is returned.
- **Successful fetch**: `time.sleep(base_delay)` is applied before returning to pace requests regardless of retry history.

### LOGID-Level Resume

Every run always fetches the index page for each configured version to get the full LOGID list. Before fetching each LOGID page, the scraper checks whether its output CSV already exists on disk:

```
<minor_version_dir>/LOGID/<safe_logid>.csv
```

If the file exists and `force_rescrape` is false, the LOGID is skipped (counted as successful in the summary). Only missing files are fetched. This means an interrupted run can be resumed safely — the scraper picks up exactly where it left off at LOGID granularity.

Setting `force_rescrape: true` bypasses all skip checks and re-fetches every LOGID.

### Directory Structure Created

```
output_dir/
└── <major>/          e.g., 7.6/
    └── <minor>/      e.g., 7.6.4/
        ├── LOGID/
        │   └── <LOGID_description>.csv
        ├── CHANGELOG.md
        ├── traffic_matrix.csv
        ├── event_matrix.csv
        └── utm_matrix.csv
```

The filename is derived from the link text on the documentation index page. Non-word characters are replaced with underscores via `re.sub(r'[^\w\-_\.]', '_', logid_description)`.

### LOGID URL Pattern

The scraper identifies log ID pages by matching anchor `href` attributes against:

```python
r'/(\d{1,6})-(logid|log-id|mesgid)-[^/]*$'
```

This covers three URL keyword variants Fortinet uses across different FortiOS versions (`logid`, `log-id`, `mesgid`). The numeric portion is 1–6 digits.

### ScrapeResult

`scrape_version()` returns a `ScrapeResult` dataclass rather than a raw dict:

```python
@dataclass
class ScrapeResult:
    successful: int = 0
    failed: list[tuple[str, str, str]] = field(default_factory=list)
```

Each entry in `failed` is `(version, logid_description, reason)`.

### Methods Reference

| Method | What it does |
|--------|-------------|
| `__init__()` | Loads config, creates `requests.Session`, sets all instance state |
| `_load_config()` | Reads YAML from `Path(__file__).parent`; raises on missing file or parse error |
| `get_version_directories()` | Splits `"7.6.4"` into `(Path(".../7.6"), Path(".../7.6/7.6.4"))` |
| `get_version_url()` | Returns the Fortinet docs URL for a given FortiOS version |
| `get_page_content()` | Fetches URL → BeautifulSoup with retry/backoff (up to `max_retries`); handles 429; returns `None` after all attempts fail |
| `extract_logid_links()` | Finds all `<a href>` matching the LOGID URL pattern; returns `dict[str, str]` |
| `extract_log_metadata()` | Regexes page text for Message ID, Type, Category, Severity, etc. |
| `extract_log_table()` | Finds `<table>` with log-field headers; returns DataFrame with metadata columns appended |
| `scrape_version()` | Orchestrates one version: get index, iterate LOGIDs, save CSVs; returns `ScrapeResult` |
| `_log_summary()` | Logs the final scraping summary (totals, success rate, failed LOGID list) |
| `run()` | Top-level entry point; handles dry-run, version filtering, per-version loop |

### HTML Table Detection

`extract_log_table()` checks each `<table>` for headers containing any of: `field`, `description`, `type`, `length`, `data type`, `field name`. The first matching table wins. If no table is found but metadata was extracted, a stub DataFrame with `Field: 'No field table found'` is returned rather than None — this ensures metadata is preserved even for log IDs with unusual page layouts.

---

## Script 2: generate_changelog.py

### Purpose

Reads the raw LOGID CSVs produced by `fortigate_scraper.py` and produces three categories of output, controlled by CLI flags:

| Flag | Output |
|------|--------|
| `--changelog` | `<major>/<minor>/CHANGELOG.md` — intra-version inconsistencies and inter-version field changes |
| `--matrices` | `<major>/<minor>/{traffic,event,utm}_matrix.csv` — field × subtype occurrence counts |
| `--fields` | `<major>/fields/{traffic,event,utm}_fields.csv` + `action_descriptions.csv` — consolidated field definitions across all minor versions |
| `--index` | `INDEX.md` at repo root — links to all changelogs, consolidated field CSVs, and ECS CSVs across every version |

Running without flags generates all four outputs. Flags can be combined.

### Dataset Buckets

All LOGID data is partitioned into three buckets:

| Bucket | Criteria | Subtype column |
|--------|----------|---------------|
| `Traffic` | `Type == 'Traffic'` | `Category` (e.g., `forward`, `local`, `sniffer`) |
| `Event` | `Type == 'Event'` | `Category` (e.g., `system`, `user`, `vpn`) |
| `UTM` | everything else | `Type` itself (e.g., `Webfilter`, `IPS`, `APP-CTRL`) |

GTP LOGIDs are included in all outputs. They flow through the changelog/matrix path via `classify_dataset()` returning their label string, and are included in the UTM field consolidation (`_consolidate_fields`, `_consolidate_action_descriptions`). GTP has no `action` field in practice, so it never appears in `action_descriptions.csv`.

### Key Data Structures

**`LogidDiff`** — field-level diff between two versions of a single LOGID:

```python
@dataclass
class LogidDiff:
    added_fields:    list[tuple[str, str, str, str]]  # (name, type, length, desc)
    removed_fields:  list[tuple[str, str, str, str]]
    type_changes:    dict[str, tuple[str, str]]        # field → (old, new)
    desc_changes:    dict[str, tuple[str, str]]
    length_changes:  dict[str, tuple[str, str]]
    severity_change:      tuple[str, str] | None       # LOGID-level metadata
    message_desc_change:  tuple[str, str] | None
    category_change:      tuple[str, str] | None
```

**`VersionDiff`** — all changes between two minor versions:

```python
@dataclass
class VersionDiff:
    added_logids:   dict[str, tuple[str, str]]            # stem → (label, extra_val)
    removed_logids: dict[str, tuple[str, str]]
    logid_diffs:    dict[str, tuple[str, str, LogidDiff]]  # stem → (label, extra_val, diff)
    utmtype_added:   set[str]
    utmtype_removed: set[str]
```

**`VersionSnapshot`** — intra-version field conflicts for one minor version:

```python
@dataclass
class VersionSnapshot:
    desc_conflicts:   dict[str, dict[str, _ConflictRows]]  # bucket → field → rows
    type_conflicts:   dict[str, dict[str, _ConflictRows]]
    length_conflicts: dict[str, dict[str, _ConflictRows]]
```

`extra_val` is the subtype string: Category for Traffic/Event, UTM-type for UTM.

### Field Consolidation (--fields)

`_consolidate_fields(all_stems, type_filter, group_col)` builds a `(Log Field Name, Data Type, Length, Description)` DataFrame across all minor versions for one log type:

- `type_filter=None` selects UTM (everything not Traffic/Event/GTP); a string value filters to that exact Type.
- `group_col` is `'Category'` for Traffic/Event, `'Type'` for UTM.
- Data Type and Length list all distinct raw values (comma-separated).
- Description uses `_label_descriptions()`: if a field means the same thing across all subtypes, the plain description is used; if meanings differ, each variant is prefixed with its subtype(s) separated by `\n\n`.

`_consolidate_action_descriptions(all_stems)` handles the UTM `action` field separately. Because `action` has a distinct set of valid values per UTM subtype (Webfilter blocks vs. IPS drops vs. APP-CTRL monitors), combining them into one description would be misleading. It produces a single-row DataFrame where each column is a UTM subtype and the value is that subtype's unique action descriptions (deduplicated by normalized form, joined with `\n\n`). GTP is **not** excluded here — it simply has no `action` field in practice, so it never appears in the output.

### Field-Oriented Aggregation (--changelog)

Inter-version changes are presented per field name, not per LOGID. `_aggregate_bucket()` accumulates all LOGIDs in a bucket into five `defaultdict` structures keyed by field name:

```
adds[field_name][(desc, dtype, length, extra)] → [stem, stem, ...]
rems[field_name][(desc, dtype, length, extra)] → [stem, stem, ...]
type_chgs[field_name][(old_type, new_type, extra)] → [stem, stem, ...]
len_chgs[field_name][(old_len, new_len, extra)] → [stem, stem, ...]
desc_chgs[field_name][(old_desc, new_desc, extra)] → [stem, stem, ...]
```

For Traffic, `extra` is always `''` (Category is suppressed), so all Traffic LOGIDs for the same field always merge into one row.

### CRLF Handling in Descriptions

Fortinet CSV files use Windows-style `\r\n` line endings. The helper `_cell_desc()` converts all line-ending variants to HTML `<br>` tags so descriptions render correctly in GFM pipe tables without breaking table structure.

### Metadata Changes

LOGID-level metadata changes (Severity, Message_Description, Category) are captured in `LogidDiff` but are currently **not rendered**. The rendering block is commented out pending a redesign into a field-oriented table format consistent with the rest of the output.

### Methods Reference

| Function | What it does |
|----------|-------------|
| `discover_versions(root)` | Returns `[(major_label, [minor_dirs])]` sorted by version number |
| `load_version(minor_dir)` | Loads all CSVs in a minor version dir; returns `dict[stem, DataFrame]` |
| `classify_dataset(df)` | Returns dataset label: `'Traffic'`, `'Event'`, `'Unknown'`, or UTM subtype name |
| `_dataset_bucket(label)` | Maps label → `'Traffic'`, `'Event'`, or `'UTM'` |
| `_extra_val(df, label)` | Returns Category (Traffic/Event) or label itself (UTM) as the subtype dimension |
| `diff_logid(prev_df, curr_df)` | Field-level diff between two DataFrames for the same LOGID; returns `LogidDiff` |
| `diff_versions(prev, curr)` | Compares two full minor version dicts; returns `VersionDiff` |
| `snapshot_version(version_dict)` | Finds intra-version field conflicts across all LOGIDs; returns `VersionSnapshot` |
| `_aggregate_bucket(bucket, diffs)` | Aggregates per-LOGID diffs into per-field-name maps for one bucket |
| `_consolidate_fields(all_stems, type_filter, group_col)` | Consolidates field definitions (name, type, length, description) across all minor versions for one log type |
| `_consolidate_action_descriptions(all_stems)` | Builds a single-row DataFrame of action field descriptions keyed by UTM subtype |
| `_label_descriptions(subtype_descs)` | Returns plain description if one meaning; subtype-labeled text if meanings differ |
| `_normalize_desc(text)` | Lowercases and strips a description string for semantic comparison |
| `_canonical_desc(descriptions)` | Returns the most frequently occurring original-casing string from a list |
| `_write_minor_analysis(minor_dir, ...)` | Writes CHANGELOG.md and/or matrix CSVs for one minor version |
| `_write_major_fields(major_dir, all_stems)` | Writes consolidated field CSVs and action descriptions for one major version |
| `_cell_desc(text)` | Renders description for a Markdown table cell; converts line endings to `<br>` |
| `_field_table_header(cols)` | Returns `[header_row, separator_row]` for a GFM pipe table |
| `_format_stems(stems)` | Formats a list of LOGID stems, truncating with `*(+N more)*` if long |
| `_render_conflict_rows(field, rows, bucket)` | Renders field heading + table for one conflicting field |
| `_render_version_snapshot(version, snap)` | Renders the intra-version inconsistency `###` section |
| `_render_version_pair(v_prev, v_curr, diff)` | Renders the inter-version changes `###` section |
| `main()` | Entry point: parses flags, discovers versions, drives all output generation |

---

## Running the Pipeline

```bash
# From the flores repo directory

# Step 1: Scrape documentation (reads fortigate_scraper_config.yaml)
python3 fortigate_scraper.py

# Preview what would be scraped without making HTTP requests:
# Set dry_run: true in fortigate_scraper_config.yaml, then run

# Step 2: Generate all outputs
python3 generate_changelog.py

# Or selectively:
python3 generate_changelog.py --changelog   # per-minor CHANGELOG.md only
python3 generate_changelog.py --matrices    # per-minor field matrix CSVs only
python3 generate_changelog.py --fields      # per-major consolidated field CSVs only
python3 generate_changelog.py --index       # root-level INDEX.md only

# Step 3: Regenerate ECS mapping CSVs
python3 generate_ecs_mappings.py
```

To add a new FortiOS version:

1. Add the version string to `versions:` in `fortigate_scraper_config.yaml`
2. Run `fortigate_scraper.py` — existing versions are skipped automatically
3. Re-run `generate_changelog.py` — it reprocesses all versions, so the new version's data is incorporated into all outputs

---

## Code Conventions

`generate_changelog.py` follows these conventions consistently — new code should do the same:

**Type hints on all functions.** Return types and parameter types are declared explicitly. Dataclasses are used for structured intermediate results (`LogidDiff`, `VersionDiff`, `VersionSnapshot`) rather than raw dicts or tuples.

**`pathlib.Path` for all file operations.** `Path.glob()`, `Path.mkdir(exist_ok=True)`, and `/` path joining replace `os.path`, `glob.glob`, and manual `os.makedirs` with existence checks.

**Vectorized pandas.** Avoid `iterrows()` — use `groupby`, `apply`, boolean indexing, and `map` with scalar functions instead. Combine boolean filters into a single expression rather than creating intermediate DataFrames.

**Small, single-responsibility functions.** Each function does one thing. I/O (reading CSVs, writing files) is separated from data transformation. Rendering functions only build strings; write functions only write files.

**No defensive `.copy()` unless a mutation follows.** A `.copy()` is only needed when you intend to modify the DataFrame in place (e.g., `subset[col] = ...`). Filtering alone doesn't require it.

**No intermediate variables for one-use values.** `sorted(result)` inline is cleaner than `sorted_keys = sorted(result); use(sorted_keys)` when the variable adds no semantic clarity.
