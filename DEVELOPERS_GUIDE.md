# FLORES — Developers Guide

This guide documents the internal design, data flow, and key implementation decisions for the three scripts that make up FLORES. It is intended for maintainers adding new FortiOS versions, extending output formats, or debugging scraper failures.

---

## Architecture Overview

FLORES is a three-script pipeline. The scraper fetches raw HTML and emits CSVs; the two downstream scripts consume those CSVs independently and produce different views of the same data.

```
fortigate_scraper_config.yaml
          │
          ▼
fortigate_scraper.py  ──►  <major>/<minor>/<LOGID>.csv  (raw, one CSV per log ID)
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
           unique_fields.py               fortigate_fields.py
           (type consolidation)           (description consolidation)
                    │                               │
                    ▼                               ▼
        <major>/unique_fields/         <major>/field_descriptions/
          unique_log_fields_           traffic_fields_*.csv
          data_types_*.csv             event_fields_*.csv
                                       utm_fields_*.csv
                                       action_descriptions_*.csv
```

**Files and their roles:**

| File | Role |
|------|------|
| `fortigate_scraper.py` | HTTP scraper — fetches Fortinet docs, extracts log tables, saves raw CSVs |
| `fortigate_scraper_config.yaml` | Configuration: versions list, rate limiting, output directory, flags |
| `unique_fields.py` | Consolidates field/type pairs; resolves type conflicts across log IDs |
| `fortigate_fields.py` | Consolidates field/type/description; preserves per-subtype meaning differences |

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
  └─ _get_versions_to_scrape()
       ├─ [force_rescrape=true]  → all versions
       └─ [force_rescrape=false] → filter with _version_exists()
              │                    (checks minor_version_dir has *.csv files)
              ▼
        for each version:
          scrape_version(version)
            ├─ get_version_dirs()      → (major_dir, minor_dir)
            ├─ get_version_url()       → docs.fortinet.com URL
            ├─ get_page_content(url)   → BeautifulSoup (with rate limit sleep)
            ├─ extract_logid_links()   → {description: full_url}
            │     regex: r'/(\d{1,6})-(logid|log-id|mesgid)-[^/]*$'
            └─ for each LOGID link:
                 get_page_content(logid_url)
                 ├─ extract_log_metadata() → Message_ID, Type, Category, Severity, ...
                 └─ extract_log_table()    → DataFrame (fields + metadata columns)
                       │
                       ▼
                   df['Version'] = version
                   df.to_csv(minor_dir/<safe_logid>.csv)

─── After scraping ─────────────────────────────────────────────────────────────

unique_fields.py                        fortigate_fields.py
(run from the data directory)           (run from the data directory)
        │                                           │
        ▼                                           ▼
scan cwd for dirs matching              scan cwd for dirs matching
  MAJOR_VERSION_DIR_RE (^\d+\.\d+$)      MAJOR_VERSION_DIR_RE (^\d+\.\d+$)
        │                                           │
for each major version:                 for each major version:
  scan for VERSION_DIR_RE dirs            scan for VERSION_DIR_RE dirs
  (^\d+\.\d+\.\d+$)                       (^\d+\.\d+\.\d+$)
        │                                           │
  glob all *.csv → concat → dedup         glob all *.csv
        │                                           │
  replace INTEGER_TYPES → 'number'        for each log type in LOG_TYPE_CONFIG:
        │                                   process_log_type(files, log_type, config)
  split by Type:                               ├─ filter rows by Type column
    Traffic: Type == 'Traffic'                 ├─ collect field_descriptions[field][subtype]
    Event:   Type == 'Event'                   ├─ collect field_data_types[field]
    UTM:     Type not in {Traffic,Event,GTP}   └─ (UTM) separate action_descriptions[subtype]
        │                                           │
  find fields where Data Type count > 1    resolve_data_type() per field
  → set all to 'string'                    process_field_descriptions() per field
        │                                           │
  drop Type column                          save field_descriptions/
  save unique_fields/                         {traffic|event|utm}_fields_*.csv
    unique_log_fields_data_types_*.csv        action_descriptions_*.csv  (UTM only)
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

The config file is located relative to the script file, not the working directory. `_load_config()` computes `os.path.dirname(os.path.abspath(__file__))` to find it.

### Class: FortiGateLogScraper

Single-class design — all scraping logic lives here. A `requests.Session` is reused across all requests for HTTP connection pooling and shared headers. Rate limiting is enforced inside `get_page_content()` via `time.sleep(self.base_delay)` after every successful fetch.

### Rate Limiting and Retry Behavior

`get_page_content()` retries transient failures with exponential backoff and jitter:

- **Retry loop**: `max_retries + 1` total attempts per URL. Set `max_retries: 0` to disable retries entirely.
- **429 Rate Limited**: If the server responds with HTTP 429, the scraper reads the `Retry-After` response header (if present) or falls back to `base_delay × (retry_backoff ^ attempt)`. It then retries without counting this as an error.
- **Other HTTP / network errors**: On each failure before the last attempt, the scraper waits `base_delay × (retry_backoff ^ attempt) + random.uniform(0, 1)` seconds (jitter prevents thundering-herd on parallel runs). On the final attempt, the error is logged and `None` is returned.
- **Successful fetch**: `time.sleep(base_delay)` is applied before returning to pace requests regardless of retry history.

### Version Skip Logic

Before scraping, `_get_versions_to_scrape()` checks each version with `_version_exists()`. A version is considered "done" if its minor version directory exists **and** contains at least one `.csv` file. This prevents re-scraping on interrupted runs. Setting `force_rescrape: true` bypasses this check entirely.

### Directory Structure Created

```
output_dir/
└── <major>/          e.g., 7.6/
    └── <minor>/      e.g., 7.6.4/
        └── <LOGID_description>.csv
```

The filename is derived from the link text on the documentation index page. Non-word characters are replaced with underscores via `re.sub(r'[^\w\-_\.]', '_', logid_description)`.

### LOGID URL Pattern

The scraper identifies log ID pages by matching anchor `href` attributes against:

```python
r'/(\d{1,6})-(logid|log-id|mesgid)-[^/]*$'
```

This covers three URL keyword variants Fortinet uses across different FortiOS versions (`logid`, `log-id`, `mesgid`). The numeric portion is 1–6 digits.

### Methods Reference

| Method | What it does |
|--------|-------------|
| `__init__()` | Loads config, creates `requests.Session`, sets all instance state |
| `_load_config()` | Reads YAML from script directory; raises on missing file or parse error |
| `_version_exists()` | Returns True if minor version dir has ≥1 CSV file |
| `_get_versions_to_scrape()` | Filters version list based on `force_rescrape` flag |
| `get_version_directories()` | Splits `"7.6.4"` into `("output/7.6", "output/7.6/7.6.4")` |
| `get_version_url()` | Generates `docs.fortinet.com` URL for a given version string |
| `get_page_content()` | Fetches URL → BeautifulSoup with retry/backoff (up to `max_retries`); handles 429; returns None after all attempts fail |
| `extract_logid_links()` | Finds all `<a href>` matching the LOGID URL pattern; returns `{text: full_url}` |
| `extract_log_metadata()` | Regexes page text for Message ID, Type, Category, Severity, etc. |
| `extract_log_table()` | Finds `<table>` with log-field headers; returns DataFrame with metadata columns appended |
| `scrape_version()` | Orchestrates one version: get index, iterate LOGIDs, save CSVs |
| `run()` | Top-level entry point; handles dry-run, version filtering, per-version loop, summary |

### HTML Table Detection

`extract_log_table()` checks each `<table>` for headers containing any of: `field`, `description`, `type`, `length`, `data type`, `field name`. The first matching table wins. If no table is found but metadata was extracted, a stub DataFrame with `Field: 'No field table found'` is returned rather than None — this ensures metadata is preserved even for log IDs with unusual page layouts.

---

## Script 2: unique_fields.py

### Purpose

Reads all raw CSVs for a major version, consolidates unique `(Log Field Name, Data Type)` combinations per log category, and resolves any type inconsistencies.

### Data Flow

1. Discover major version dirs matching `MAJOR_VERSION_DIR_RE`
2. Within each, discover minor version dirs matching `VERSION_DIR_RE`
3. `glob` all `*.csv` files across all minor versions
4. `pd.concat` all DataFrames, `drop_duplicates()` on `['Type', 'Log Field Name', 'Data Type']`
5. Normalize integer types (see below)
6. Split into three category DataFrames: Traffic, Event, UTM
7. Per category: find fields appearing with >1 distinct Data Type → set all occurrences to `'string'`
8. Drop the `Type` column; save `(Log Field Name, Data Type)` pairs

### Type Normalization

All integer variants are collapsed to `'number'` before conflict detection:

```python
INTEGER_TYPES = ['uint64', 'uint32', 'uint16', 'uint8', 'int8', 'int32', 'int64']
consolidated_df['Data Type'] = consolidated_df['Data Type'].replace(INTEGER_TYPES, 'number')
```

This is done with pandas `.replace()` on the entire column before the split, so normalization applies uniformly.

### Inconsistency Resolution

After normalization, fields that still appear with >1 distinct Data Type (e.g., `string` in one log ID, `ip` in another) are demoted to `'string'`. This is the conservative choice: a field that sometimes looks like an IP but sometimes carries non-IP values cannot be mapped as an IP type.

```python
inconsistent_data_types = df.groupby('Log Field Name')['Data Type'].nunique()
inconsistent_fields = inconsistent_data_types[inconsistent_data_types > 1]
# → set all rows for those fields to 'string'
```

### UTM Category

UTM is everything that is not Traffic, Event, or GTP:

```python
utm_types = consolidated_df[~consolidated_df['Type'].isin(['Traffic', 'Event', 'GTP'])]['Type'].unique()
df_utm = consolidated_df[consolidated_df['Type'].isin(utm_types)].copy()
```

### Output Files

Written to `<major>/unique_fields/`:

| File | Contents |
|------|----------|
| `unique_log_fields_data_types_traffic_<ver>.csv` | `(Log Field Name, Data Type)` for Traffic |
| `unique_log_fields_data_types_event_<ver>.csv` | `(Log Field Name, Data Type)` for Event |
| `unique_log_fields_data_types_utm_<ver>.csv` | `(Log Field Name, Data Type)` for all UTM subtypes combined |

---

## Script 3: fortigate_fields.py

### Purpose

Reads all raw CSVs for a major version, consolidates field descriptions per log subtype, and resolves multi-subtype description conflicts. Unlike `unique_fields.py`, it preserves description text — and when a field means something different in different subtypes, it labels both meanings in the output.

### Key Design: Subtype-Aware Descriptions

The central insight is that a field name like `action` means different things in Webfilter vs. IPS vs. APP-CTRL. Rather than arbitrarily picking one description or concatenating all of them, `process_field_descriptions()` groups descriptions by semantic meaning (case-insensitive) and only introduces subtype labels when the meanings genuinely differ.

### LOG_TYPE_CONFIG

All log-type-specific behavior is centralized in one dict, eliminating per-type conditionals in the processing loop:

```python
LOG_TYPE_CONFIG = {
    'Traffic': {
        'filter_column': 'Type',
        'filter_value': 'Traffic',
        'subtype_column': 'Category',  # subtype comes from Category column
        'output_prefix': 'traffic',
        'special_action': False,
    },
    'Event': {
        'filter_column': 'Type',
        'filter_value': 'Event',
        'subtype_column': 'Category',  # subtype comes from Category column
        'output_prefix': 'event',
        'special_action': False,
    },
    'UTM': {
        'filter_column': 'Type',
        'filter_values_exclude': {'Traffic', 'Event', 'GTP'},
        'subtype_column': 'Type',      # subtype IS the Type (APP-CTRL, IPS, etc.)
        'output_prefix': 'utm',
        'special_action': True,        # action field gets separate treatment
    },
}
```

For Traffic and Event, the subtype comes from the `Category` column (e.g., `forward`, `local`, `sniffer` for Traffic). For UTM, the `Type` column itself IS the subtype (e.g., `Webfilter`, `IPS`, `APP-CTRL`).

### UTM `action` Field Special Handling

The `action` field in UTM logs has a distinct set of valid values per subtype (Webfilter blocks vs. IPS drops vs. APP-CTRL monitors). Mixing all these into one description would be misleading. When `special_action: True`:

- During row processing, if `field_name == 'action'`, the description goes to `action_descriptions[subtype]` instead of `field_descriptions`
- The field still appears in the main output CSV with an empty description
- A separate `action_descriptions_<ver>.csv` is written with one column per UTM subtype, containing that subtype's action values

### process_field_descriptions()

The core description consolidation function:

```
Input:  field_data = {subtype: [description, description, ...], ...}

1. Normalize all descriptions: lowercase + strip
2. Group by normalized form → collect (original_desc, subtype) pairs
3. For each unique normalized form:
   a. Pick canonical text = most frequent original casing
   b. Collect all subtypes that use this meaning
4. If only one unique meaning → return canonical text (no labels)
5. If multiple meanings → format as:
      "subtype_a/subtype_b: description one\n\nsubtype_c: description two"
```

The normalization step handles the common case where Fortinet's docs use slightly different casing for the same sentence across FortiOS versions — these collapse to a single meaning.

### resolve_data_type()

A helper used in `process_log_type()` to normalize a collection of raw types:

```python
def resolve_data_type(raw_types):
    normalized = {'number' if dt in INTEGER_TYPES else dt for dt in raw_types}
    return 'string' if len(normalized) > 1 else (next(iter(normalized)) if normalized else 'string')
```

Steps: normalize integers → if one unique type remains, use it; if multiple, use `'string'`; if empty, default to `'string'`.

This is functionally equivalent to what `unique_fields.py` does in pandas, but operates per-field rather than per-column.

### Output Files

Written to `<major>/field_descriptions/`:

| File | Contents |
|------|----------|
| `traffic_fields_<ver>.csv` | `(Log Field Name, Description, Data Type)` for Traffic |
| `event_fields_<ver>.csv` | `(Log Field Name, Description, Data Type)` for Event |
| `utm_fields_<ver>.csv` | `(Log Field Name, Description, Data Type)` for UTM (action has empty description) |
| `action_descriptions_<ver>.csv` | One column per UTM subtype; one row of action value descriptions |

---

## Shared Constants and Patterns

### Version Directory Regexes

Both `unique_fields.py` and `fortigate_fields.py` use the same compiled patterns to distinguish directory types:

```python
MAJOR_VERSION_DIR_RE = re.compile(r'^\d+\.\d+$')    # matches: 7.2, 7.4, 7.6
VERSION_DIR_RE       = re.compile(r'^\d+\.\d+\.\d+$') # matches: 7.2.4, 7.6.0
```

These patterns are anchored (`^...$`) to prevent partial matches against other directory names like `unique_fields` or `field_descriptions`.

### INTEGER_TYPES

Both scripts normalize these type names to `'number'`:

```
uint8, uint16, uint32, uint64, int8, int32, int64
```

The rationale: Fortinet documents integer fields with varying widths (`uint8`, `uint32`, `uint64`, etc.), but this granularity is a FortiOS implementation detail with no practical meaning for consumers of the data. Collapsing all variants to `'number'` produces a cleaner, storage-agnostic type vocabulary — downstream tools can map `'number'` to whatever numeric type suits their target system.

Note: `unique_fields.py` stores INTEGER_TYPES as a list (for pandas `.replace()`), while `fortigate_fields.py` stores it as a set (for O(1) membership tests in `resolve_data_type()`).

### GTP Exclusion

GTP logs are excluded everywhere in the pipeline:

- `unique_fields.py`: `utm_types = ... ~isin(['Traffic', 'Event', 'GTP'])`
- `fortigate_fields.py`: `LOG_TYPE_CONFIG['UTM']['filter_values_exclude'] = {'Traffic', 'Event', 'GTP'}`

GTP is only present in FortiGate Carrier (a specialized variant), and its log fields cause type conflicts with regular FortiGate fields (e.g., `checksum`, `from`, `to`, `version` can be either `string` or `uint32` depending on context). Excluding GTP keeps the output clean for standard FortiGate deployments.

---

## Running the Pipeline

```bash
# From the flores repo directory

# Step 1: Scrape documentation (reads fortigate_scraper_config.yaml)
python3 fortigate_scraper.py

# Preview what would be scraped without making HTTP requests:
# Set dry_run: true in fortigate_scraper_config.yaml, then run

# Step 2a: Consolidate data types (no arguments — scans current directory)
python3 unique_fields.py

# Step 2b: Consolidate field descriptions (no arguments — scans current directory)
python3 fortigate_fields.py
```

Steps 2a and 2b are independent and can be run in either order. Both scan for `^\d+\.\d+$` directories in the current working directory, so they must be run from the same root where the version directories live.

To add a new FortiOS version:

1. Add the version string to `versions:` in `fortigate_scraper_config.yaml`
2. Run `fortigate_scraper.py` — existing versions are skipped automatically
3. Re-run `unique_fields.py` and `fortigate_fields.py` — they reprocess all versions, so the new version's data is merged into the output

---

## Key Methods Reference

| Method | Script | What it does |
|--------|--------|-------------|
| `FortiGateLogScraper.__init__()` | scraper | Loads config, creates HTTP session, sets base_delay, max_retries, retry_backoff, force_rescrape, dry_run |
| `_load_config()` | scraper | Reads YAML from script's own directory; raises on missing file or parse error |
| `_version_exists()` | scraper | Returns True if minor version dir exists and contains ≥1 CSV file |
| `_get_versions_to_scrape()` | scraper | Filters version list: all if force_rescrape, else only missing versions |
| `get_version_directories()` | scraper | Splits `"7.6.4"` into `(output/7.6, output/7.6/7.6.4)` paths |
| `get_version_url()` | scraper | Constructs `docs.fortinet.com` URL for a FortiOS version |
| `get_page_content()` | scraper | Fetches URL → BeautifulSoup with retry/backoff; handles 429; returns None after all attempts fail |
| `extract_logid_links()` | scraper | Regex-scans all `<a href>` for LOGID URL pattern; returns `{text: url}` dict |
| `extract_log_metadata()` | scraper | Regex-extracts Message ID, Type, Category, Severity from page text |
| `extract_log_table()` | scraper | Finds first `<table>` with log-field headers; returns DataFrame with metadata columns |
| `scrape_version()` | scraper | Orchestrates full version scrape: index page → LOGID loop → CSV save per LOGID |
| `run()` | scraper | Entry point: dry-run check, version filtering, per-version dispatch, final summary |
| `process_log_type()` | fields | Reads all CSVs for one log type; collects field_descriptions and field_data_types dicts |
| `process_field_descriptions()` | fields | Resolves multi-subtype descriptions: single meaning → plain text, multiple → labeled |
| `get_canonical_description()` | fields | Given a list of equivalent descriptions, returns the most frequent original casing |
| `resolve_data_type()` | fields | Normalizes a collection of raw type strings to one resolved type |
| `normalize_description()` | fields | Lowercases and strips a description string for comparison |
| `process_major_version()` | both | Discovers minor version dirs, globs CSVs, drives per-type processing and output |
