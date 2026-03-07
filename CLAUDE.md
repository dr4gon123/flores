# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

FLORES (FortiGate Log Reference Scraper) extracts FortiGate log field documentation from Fortinet's official docs site and produces Elasticsearch-ready field definitions. It is a standalone companion to the [fortinet-2-elasticsearch](https://github.com/enotspe/fortinet-2-elasticsearch) project.

## Pipeline

Scripts run in sequence from the repo root:

```bash
# Step 1: Scrape Fortinet docs for configured versions
python3 fortigate_scraper.py

# Step 2a: Consolidate unique field/type combinations (no descriptions)
python3 unique_fields.py

# Step 2b: Consolidate fields with descriptions per subtype
python3 fortigate_fields.py

# Step 3: Generate Elasticsearch component templates (lives in fortinet-2-elasticsearch)
# python3 ../fortinet-2-elasticsearch/datasets/Fortinet/elasticsearch_mappings.py
```

All scripts expect to run from the repo root (they resolve paths relative to `os.getcwd()` or the script location).

## Configuration

`fortigate_scraper_config.yaml` controls the scraper:

- `versions` — list of FortiOS versions to scrape (format: `"X.Y.Z"`)
- `settings.base_delay` — seconds between HTTP requests (default: `1.0`)
- `settings.force_rescrape` — re-scrape versions that already have output (default: `false`)
- `settings.dry_run` — preview which versions would be scraped without fetching (default: `false`)
- `settings.output_dir` — root output directory (default: `"."`, i.e. repo root)

## Output Structure

```
<major>/                          # e.g., 7.6/
├── <minor>/                      # e.g., 7.6.4/ — one CSV per LOGID
│   └── <LOGID_description>.csv
├── unique_fields/
│   ├── unique_log_fields_data_types_traffic_<ver>.csv   # unique_fields.py output
│   ├── unique_log_fields_data_types_event_<ver>.csv
│   └── unique_log_fields_data_types_utm_<ver>.csv
└── field_descriptions/
    ├── traffic_fields_<ver>.csv                          # fortigate_fields.py output
    ├── event_fields_<ver>.csv
    ├── utm_fields_<ver>.csv
    └── action_descriptions_<ver>.csv                    # UTM action field variants
```

## Key Design Decisions

**Two consolidation scripts serve different purposes:**
- `unique_fields.py` — produces simple `(Log Field Name, Data Type)` pairs; feeds `elasticsearch_mappings.py`
- `fortigate_fields.py` — produces `(Log Field Name, Data Type, Description)` with subtype-labeled descriptions; richer but not yet wired to template generation

**Type normalization:** All integer variants (`uint8/16/32/64`, `int8/32/64`) are normalized to `number`. Fields with conflicting types across log IDs are demoted to `string`.

**GTP exclusion:** GTP logs are excluded throughout (`EXCLUDED_TYPES = {'GTP'}`). FortiGate Carrier GTP events cause field type conflicts and are not relevant to standard deployments.

**Log type classification:**
- `Traffic` — filtered by `Type == 'Traffic'`, subtype from `Category` column
- `Event` — filtered by `Type == 'Event'`, subtype from `Category` column
- `UTM` — everything else except Traffic/Event/GTP, subtype from `Type` column; `action` field handled separately because its description varies significantly per UTM subtype

**Scraper skips existing versions** unless `force_rescrape: true`. A version is considered existing if its minor version directory contains at least one CSV file.

## Reference

For internal design, data flow diagrams, and full method documentation, see `DEVELOPERS_GUIDE.md`.

## Dependencies

```bash
pip install requests beautifulsoup4 pandas lxml pyyaml
```
