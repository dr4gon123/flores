# FLORES — FortiGate Log Message Reference Scraper

FLORES extracts FortiGate log field documentation from Fortinet's official Log Message Reference documentation and transforms it into clean, structured CSV datasets. It is designed for security engineers and data teams who need machine-readable syslog schemas for parser development, log normalization, or field reference.

Schema normalization makes firewall logs queryable, correlatable, and actionable across a modern security stack. Normalizing FortiGate log fields against ECS, OCSF, or a custom schema requires exact field names, data types, and descriptions across hundreds of LOGIDs spread across Traffic, Event, and UTM log types — information that Fortinet distributes across per-minor-version documentation pages.

FLORES provides the full pipeline: collecting, consolidating, and tracking how the schema changes between minor versions, then translating them into ECS and OCSF field mappings ready for your normalization workflow.

For a full index of changelogs, consolidated fields, and ECS mappings across all versions, see [INDEX.md](INDEX.md).

## Quick Start

All scraped data and generated outputs are already committed to this repository — you can use the CSV and Markdown files directly without running anything.

To add a new FortiOS version or regenerate outputs:

```bash
pip install requests beautifulsoup4 pandas lxml pyyaml
python3 fortigate_scraper.py       # scrape Fortinet docs
python3 generate_changelog.py      # changelogs, field matrices, consolidated CSVs, INDEX.md
python3 generate_ecs_mappings.py   # ECS mapping CSVs
```

Output lands in major-version subdirectories (e.g. `7.6/`) in the current working directory.

## Output

```
{major}/                              # e.g. 7.6/
  {minor}/                            # e.g. 7.6.4/ — one CSV per LOGID
    {LOGID_description}.csv
    analysis/
      CHANGELOG.md                    # intra-version conflicts + inter-version diffs
      traffic_matrix.csv              # field × subtype occurrence counts
      event_matrix.csv
      utm_matrix.csv
  fields/
    traffic_fields.csv                # consolidated across all minor versions
    event_fields.csv
    utm_fields.csv
    action_descriptions.csv           # UTM action field variants (one column per subtype)
  ECS/
    traffic_ecs.csv                   # FortiGate fields mapped to ECS targets
    event_ecs.csv
    utm_ecs.csv
```

**`{LOGID_description}.csv`** — raw log field table for one LOGID as scraped from Fortinet
docs. Columns: `Type`, `Log Field Name`, `Description`, `Data Type`.

**`fields/{log_type}_fields.csv`** — consolidated field reference for a log type, aggregated
across all minor versions of the major. When a field has different descriptions per subtype,
each variant is labeled `subtype: description`.

**`analysis/CHANGELOG.md`** — per-minor changelog recording intra-version description
conflicts (same field name, different descriptions across LOGIDs) and inter-version diffs
(fields and LOGIDs added or removed since the previous minor version).

**`analysis/{log_type}_matrix.csv`** — field × subtype matrix showing which fields appear
in which subtypes, with occurrence counts. Column headers are the definitive per-version subtype list.

## Elastic Common Schema (ECS) Mapping

FortiGate fields are cross-referenced to Elastic Common Schema (ECS) for SIEM ingestion and normalization.

| Log type | Status | Output |
|----------|--------|--------|
| Traffic | 45/295 fields mapped | `{major}/ECS/traffic_ecs.csv` |
| Event | 22/404 fields mapped | `{major}/ECS/event_ecs.csv` |
| UTM | 51/567 fields mapped | `{major}/ECS/utm_ecs.csv` |

Run `python3 generate_ecs_mappings.py` to regenerate the ECS CSVs after scraping new versions.

For mapping notation, coverage details, intentionally unmapped fields, and guidance on extending the mapping, see [FIELD_NAMING_NORMALIZATION.md](FIELD_NAMING_NORMALIZATION.md).

## Configuration

Edit `fortigate_scraper_config.yaml` to customize behaviour:

| Setting | Default | Effect |
|---------|---------|--------|
| `base_delay` | `1.0` | Seconds between HTTP requests (rate limiting) |
| `max_retries` | `3` | Additional attempts per URL after an error (`0` = no retries) |
| `retry_backoff` | `2.0` | Exponential backoff multiplier: `base_delay × (backoff ^ attempt)` |
| `force_rescrape` | `false` | Re-scrape versions that already exist locally |
| `dry_run` | `false` | Print scrape plan without fetching any pages |
| `output_dir` | `"."` | Root directory for all output |

## Adding a New FortiOS Version

Add a new entry under `versions` in `fortigate_scraper_config.yaml`:

```yaml
versions:
  - "7.6.7"
```

FLORES will skip versions that already exist locally unless `force_rescrape: true`.


## FortiGate Documentation Notes

FortiGate's log schema is structurally heterogeneous in ways that complicate normalization
pipelines. UTM subtypes are developed independently: the `action` field alone carries
different values and lengths across 16 subtypes, and six of those subtypes have no
description for it at all. GTP logs are structurally incompatible with the rest of UTM
(field type conflicts, ~150 undocumented fields). The schema is not a ratchet — fields and
LOGIDs are both added and removed between minor versions, with no version field embedded in
the log stream itself. The LOGID taxonomy has no consistent rule: some subtypes encode the
outcome in separate LOGIDs (VideoFilter, DNS, CASB), others encode it in the `action` field
(Anomaly, Virus), and a SIEM must know which pattern a subtype follows to correctly classify
an event.

Every structural finding, field conflict, and schema evolution detail is catalogued in
[ANALYSIS.md](ANALYSIS.md), organized by log type, with tables for LOGID distribution, field
counts, cross-type conflicts, and per-minor-version change counts.

## For Developers & Maintainers

See [DEVELOPERS_GUIDE.md](DEVELOPERS_GUIDE.md) for:

- Architecture overview and pipeline walkthrough
- Data flow diagrams (scraper → changelog → fields → ECS)
- Key methods reference

---

*Not interested in FortiGate? Check out [PALOS - PAN-OS Log Scraper](https://github.com/dr4gon123/palos)*
