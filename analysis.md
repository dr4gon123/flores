# FortiGate Log Field Analysis: Findings

This document summarizes structural and data quality findings derived from the FLORES pipeline outputs. For each minor version, the `<major>/<minor>/analysis/` directory contains:

- `CHANGELOG.md` — intra-version field conflicts (description, data type, length) and inter-version diffs
- `traffic_matrix.csv`, `event_matrix.csv`, `utm_matrix.csv` — field × subtype occurrence counts, showing which fields appear in which log subtypes

The consolidated `<major>/fields/` CSVs aggregate across all minor versions of that major:

- `traffic_fields.csv` — all Traffic log fields
- `event_fields.csv` — all Event log fields
- `utm_fields.csv` — all UTM log fields
- `action_descriptions.csv` — UTM `action` field values per subtype (one column per subtype, since values diverge too much to consolidate)

---

## UTM: A Tower of Babel

UTM is structurally the most heterogeneous log type. Its subtypes (antivirus, IPS, web filter, application control, DNS, DLP, email filter, SSL, ICAP, WAF, SSH, VoIP, GTP, anomaly, casb, virtual-patch, file-filter) are developed independently, and it shows.

### The `action` field

`action` is present in every UTM subtype but means something different in each one. The table below maps each subtype to its length and the values it actually carries (sourced from `7.6.6/analysis/CHANGELOG.md`):

| Subtype | Length | Description / values |
|---------|--------|----------------------|
| APP-CTRL | 16 | pass / block / reject / reset |
| IPS | 16 | detected / dropped / reset / reset_client / reset_server / drop_session / pass_session / clear_session |
| Virus | 18 | blocked / passthrough / monitored / analytics (Sandbox submission); *some Virus LOGIDs have no description* |
| DLP | 20 | log-only / block / exempt / ban / ban-sender / quarantine-ip / quarantine-interface *(several marked "Not in use since FortiOS 5.0")* |
| Webfilter | 11 | blocked / passthrough |
| WAF | 17 | Deny / Start / (all others = allowed by firewall policy) |
| SSH | 17 | passthrough / blocked |
| VoIP | 15 | "Action. Eg. block, allow" |
| DNS | 16 | "Security action performed by DNS filter" |
| Anomaly | 16 | "Action" *(no further detail)* |
| EmailFilter | 8 | *(no description)* |
| FILE-FILTER | 20 | *(no description)* |
| ICAP | 17 | *(no description)* |
| SSL | 20 | *(no description)* |
| casb | 11 | *(no description)* |
| virtual-patch | 16 | *(no description)* |

Six of sixteen subtypes have no description for `action` at all. The length ranges from 8 (EmailFilter) to 20 (DLP, FILE-FILTER, SSL) with no consistent logic. Compared to traffic (length 16) and event (length 65), this single field illustrates why a unified schema mapping cannot cover all log types.

`action_descriptions.csv` exists precisely to capture this divergence — one column per UTM subtype — but the six undocumented subtypes above have empty columns.

### GTP: a different data model

GTP logs (18 LOGIDs, LOGID range 41216–41228+) are structurally incompatible with the rest of UTM:

- Fields `from` and `to` are typed `ip` in GTP but `string` in every other UTM subtype (DLP, Virus, EmailFilter, Webfilter, VoIP all use `string`, length 128).
- GTP-specific fields (`cgsn6`, `endusraddress6`, `msgtypename`, `timeoutdelete`, `ulimcc`, `ulimnc`, `upteid`, `ugsn6`, `from6`, `to6`) have **no descriptions** across all 18 LOGIDs — approximately 150+ undocumented fields.
- GTP logs mobile core network traffic (GPRS Tunneling Protocol), a completely different domain from web/endpoint security. It shares the UTM log type classification but has no semantic overlap with other UTM subtypes.

Any unified schema template for UTM will break on GTP's `ip`-typed fields or require a separate mapping.

### Type and length conflicts within UTM

UTM has **21 fields with multiple type or length combinations** within its own subtypes. Traffic and Event have zero such fields. Selected examples:

| Field | Variants |
|-------|---------|
| `msg` | lengths 512, 518, 4096 |
| `virusid` | types `string`/`uint32`, lengths 10/64 |
| `service` | 3 distinct lengths (5, 36, 80) |
| `direction` | lengths 8 and 4096 |
| `reason` | lengths 128 (VoIP) and 4096 (ICAP) — 32× difference |

### Missing field descriptions

Beyond GTP, undocumented fields are widespread:

| Category | Missing descriptions |
|----------|---------------------|
| GTP (18 LOGIDs) | ~150+ fields |
| Virus (73 LOGIDs) | ~80 fields (~42 per LOGID in some cases) |
| ICAP (LOGID 60000) | ~30 fields |
| APP-CTRL | 9 fields |
| DNS | 6 fields |

The `CHANGELOG.md` in each minor version's `analysis/` folder records **133 description conflicts** for 7.6.0 alone — cases where the same field name has different or empty descriptions across LOGIDs within the same version.

---

## Field Fragmentation

Across all three log types (Traffic, Event, UTM) in 7.6.0:

| Scope | Field count |
|-------|------------|
| UTM unique fields | 262 |
| Traffic unique fields | 198 |
| Event unique fields | 390 |
| **Total union** | **712** |
| Shared across all three | **37 (5.2%)** |

Breakdown of overlap:

| Group | Fields |
|-------|--------|
| Event only | 319 |
| Traffic only | 121 |
| UTM only | 171 |
| Traffic + UTM | 30 |
| Event + UTM | 24 |
| Event + Traffic | 10 |

**95% of fields are absent from at least one log type.** A unified schema would be overwhelmingly sparse, increasing storage overhead and complicating query patterns. Separate indices or tables per log type (or per subtype) are the practical outcome.

Even within a single log type, subtypes diverge:

- Traffic: HTTP-Transaction has 60 fields; Forward/Local/Multicast have 172 — a 2.9× spread within one log type
- Event: System has 165 fields; REST API has 17 — a 9.7× spread
- UTM: Virus has 99 fields; FORTI-SWITCH has 18 — a 5.5× spread

The 4 cross-type data type conflicts that force incompatible mappings:

| Field | Traffic | Event | UTM |
|-------|---------|-------|-----|
| `channel` | `uint32` | `uint8` | — |
| `filesize` | — | `uint32` | `uint64` |
| `rcvdbyte` | `uint64` | `uint64` | `uint32` and `uint64` |
| `xid` | — | `uint32` | `uint16` |

---

## LOGID Distribution

LOGIDs are not evenly distributed across categories. Some categories have hundreds; others have one.

### Event

| Category | LOGIDs | Unique fields |
|----------|--------|--------------|
| System | 594 | 165 |
| Wireless | 189 | 83 |
| VPN | 75 | 61 |
| Switch-Controller | 64 | 39 |
| User | 53 | 40 |
| HA | 37 | 30 |
| Endpoint | — | 36 |
| REST API | — | 17 |

System and Wireless together account for the overwhelming majority of Event LOGIDs. Wireless in particular has nearly 200 LOGIDs covering fine-grained association, roaming, interference, and rogue AP events — most of which are rarely seen in production deployments.

### UTM

| Subtype | LOGIDs | Unique fields |
|---------|--------|--------------|
| Virus | 73 | 99 |
| Webfilter | 63 | 90 |
| GTP | 18 | 86 |
| APP-CTRL | — | 89 |
| DNS | 12 | 54 |
| EmailFilter | 5 | 60 |
| Anomaly | — | 46 |
| FORTI-SWITCH | 1 | 18 |

### Traffic

Traffic is the most uniform: Forward, Local, Multicast, Sniffer, and ZTNA subtypes all share 156–172 fields. The exception is HTTP-Transaction, which has a single LOGID and only 60 fields — it captures HTTP-level metadata not present in the others.

### Implication

High-LOGID categories dominate schema design decisions and testing coverage. Rare categories (FORTI-SWITCH, REST API, HTTP-Transaction) may appear correct in schema definitions while having subtle mapping gaps that only surface at ingestion time.

---

## Schema Evolution Across Minor Versions

The schema is not a ratchet — fields and LOGIDs are both added and removed between minor versions. The inter-version diff section of each `analysis/CHANGELOG.md` is the authoritative record of these changes.

### Changes per minor version (7.6.0 baseline)

| Version | LOGIDs added | LOGIDs removed | Fields added | Fields removed |
|---------|-------------|----------------|--------------|----------------|
| 7.6.1 | 22 | 1 | 30 | 2 |
| 7.6.2 | 0 | 0 | 2 | 0 |
| 7.6.3 | 25 | 0 | 17 | 15 |
| 7.6.4 | 17 | 2 | 25 | 3 |
| 7.6.5 | 14 | 0 | 11 | 2 |

Additions consistently outnumber removals, so the net trend is growth — but removals are real. 7.6.3 is the most disruptive: 15 fields removed in the same release that added 25.

Schema churn between minor versions creates several concrete problems:

**Field removals break parsing rules.** A SIEM ingestion pipeline built against 7.6.2 that extracts or normalizes one of the 15 fields removed in 7.6.3 will silently produce nulls or parsing errors after a FortiGate upgrade — with no indication from the device itself that the field disappeared. Detection rules or dashboards referencing those fields stop working without any alert.

**Field additions go unnoticed without version tracking.** When 22 new LOGIDs and 30 fields appear in 7.6.1, a SIEM that doesn't track schema versions will either drop the new fields (if using a strict mapping) or ingest them untyped (if using dynamic mapping), both of which degrade data quality. New fields often carry security-relevant context — ignoring them means incomplete detections.

**No version field in the log itself.** FortiGate logs do not embed the FortiOS version that generated them. A SIEM receiving logs from a mixed fleet (some devices on 7.6.2, some on 7.6.4) cannot distinguish which schema applies to a given log line. Fields that were removed in 7.6.3 may still arrive from older devices, while new fields from 7.6.4 devices will be absent from older ones — in the same index, at the same time.

### Field values marked deprecated but still documented

The only explicit deprecation markers in the 7.6 documentation appear as values within the `action` field for the DLP subtype (`utm_fields.csv`, `action_descriptions.csv`):

| Value | Status | Replacement |
|-------|--------|-------------|
| `ban` | Not in use since FortiOS 5.0 | `blocked` |
| `ban-sender` | Not in use since FortiOS 5.0 | `quarantine` |
| `quarantine-ip` | Not in use since FortiOS 5.0 | *(none stated)* |
| `quarantine-interface` | Not in use since FortiOS 5.0 | *(none stated)* |

These are values, not fields — the `action` field itself is still present and active. However, a device that predates FortiOS 5.0 (or has legacy config) could still emit these values. A SIEM normalizing `action` to a controlled vocabulary would need to decide whether to map them to their replacements or treat them as unknown. There is no equivalent marker for any other field or value across the rest of the schema.

### New categories appearing mid-major

- `telemetry` — new Event subtype, +12 fields
- `web-svc` — new Event subtype, +27 fields

New subtypes arrive without announcement in the docs; the `analysis/CHANGELOG.md` inter-version diff is the only structured record of these additions.
