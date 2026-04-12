# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

FLORES (FortiGate Log Reference Scraper) extracts FortiGate log field documentation from Fortinet's official docs site and produces Elasticsearch-ready field definitions.

## Pipeline

Two scripts, run from the repo root:

```bash
# Step 1: Scrape Fortinet docs for configured versions
python3 fortigate_scraper.py

# Step 2: Generate changelogs, field matrices, and consolidated field CSVs
python3 generate_changelog.py              # all outputs
python3 generate_changelog.py --changelog  # per-minor CHANGELOG.md only
python3 generate_changelog.py --matrices   # per-minor field matrix CSVs only
python3 generate_changelog.py --fields     # per-major consolidated field CSVs only
python3 generate_changelog.py --index      # root INDEX.md + per-major {major}/INDEX.md

# Step 3: Generate Elasticsearch component templates (lives in fortinet-2-elasticsearch)
# python3 ../fortinet-2-elasticsearch/datasets/Fortinet/elasticsearch_mappings.py
```

## Configuration

`fortigate_scraper_config.yaml` controls the scraper:

- `versions` — list of FortiOS versions to scrape (format: `"X.Y.Z"`)
- `settings.base_delay` — seconds between HTTP requests (default: `1.0`)
- `settings.max_retries` — additional attempts per URL after an error (default: `3`; `0` = no retries)
- `settings.retry_backoff` — exponential backoff multiplier: `base_delay × (backoff ^ attempt)` (default: `2.0`)
- `settings.force_rescrape` — re-scrape versions that already have output (default: `false`)
- `settings.dry_run` — preview which versions would be scraped without fetching (default: `false`)
- `settings.output_dir` — root output directory (default: `"."`, i.e. repo root)

## Output Structure

```
<major>/                              # e.g., 7.6/
├── <minor>/                          # e.g., 7.6.4/
│   ├── LOGID/                        # one CSV per LOGID
│   │   └── <LOGID_description>.csv
│   ├── CHANGELOG.md                  # intra-version conflicts + inter-version diffs
│   ├── traffic_matrix.csv            # field × category occurrence counts
│   ├── event_matrix.csv
│   └── utm_matrix.csv
└── fields/
    ├── traffic_fields.csv            # consolidated across all minor versions
    ├── event_fields.csv
    ├── utm_fields.csv
    └── action_descriptions.csv       # UTM action field variants (one column per subtype)
```

## Key Design Decisions

**Log type classification:**

- `Traffic` — `Type == 'Traffic'`, subtype from `Category` column
- `Event` — `Type == 'Event'`, subtype from `Category` column
- `UTM` — everything else (including GTP), subtype from `Type` column; `action` field written to a separate `action_descriptions.csv` because its values differ significantly per subtype

**Description consolidation:** When a field has the same meaning across subtypes, a single plain description is used. When meanings differ, each variant is labeled `subtype: description` and joined with `\n\n`.

**Scraper resumes at LOGID granularity** — skips individual CSVs that already exist unless `force_rescrape: true`.

## Code Conventions

All new code must follow the conventions established in `generate_changelog.py`:

- **`from __future__ import annotations`** at the top of every script
- **Type hints on all functions** — use built-in generics (`list[str]`, `dict[str, str]`, `X | None`); no `typing` module imports
- **`pathlib.Path` for all file operations** — no `os.path`, `os.makedirs`, or `glob.glob`
- **Dataclasses for structured results** — use `@dataclass` instead of raw dicts or untyped tuples
- **Vectorized pandas** — no `iterrows()`; use `groupby`, boolean indexing, and `map` with scalar functions
- **No defensive `.copy()`** unless an in-place mutation follows
- **One-line docstrings** — `Args:`/`Returns:` blocks that restate the signature are noise; delete them
- **Small, single-responsibility functions** — separate I/O from data transformation

## Reference

For internal design, data flow diagrams, and full method documentation, see `DEVELOPERS_GUIDE.md`.

## Dependencies

```bash
pip install requests beautifulsoup4 pandas lxml pyyaml
```
