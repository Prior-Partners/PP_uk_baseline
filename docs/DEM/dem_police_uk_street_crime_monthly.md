# `dem_police_uk_street_crime_monthly`

data.police.uk street-level crime events, monthly archives.

**SOURCE**

- Data published by data.police.uk (Home Office). 43 territorial police forces in England and Wales, plus British Transport Police, contribute CSV files.

**DOCUMENTATION**

- Archive index : https://data.police.uk/data/archive/
- Data definitions : https://data.police.uk/about/

**DEFINITIONS**

- Crime types: 14 standardised categories assigned by the police force at time of recording (e.g. "Anti-social behaviour", "Burglary", "Violence and sexual offences"). Full list at https://data.police.uk/about/.
- Last outcome category: a snapshot, as of the archive publication month, of the case progression status. Mutates over time as cases progress; the loader's rolling window picks up corrections to the trailing 35 months automatically.

**SCOPE**

- Police forces in England and Wales, plus British Transport Police.
- Rolling 36-month window - months that fall out of the window freeze at their last-published state.

**CRS**

- EPSG:27700 (British National Grid / BNG). Reprojected at load from EPSG:4326 lat/lon supplied in the source CSV.

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- crime_id is nullable - blank for Anti-Social Behaviour (ASB) rows in the source CSV.
- last_outcome is a SNAPSHOT, not a live status. Cases in published months outside the rolling 36-month window are frozen and may not reflect current case state.
- Some rows have NULL geom where the source CSV had blank lat/lon (anonymised or unrecorded location).
- ~17-67% of "Last outcome category" values mutate across releases for the same row - verified by internal archive-comparison checks. Treat the column as a historical-snapshot, not a current-state indicator.

**NOT IN THIS DATASET**

- *-outcomes.csv (case-progression log) is deliberately NOT loaded. last_outcome on this table is sufficient for planning/baseline work.
- Northern Ireland (PSNI) and Scotland (Police Scotland) do not publish via data.police.uk archives.

**LOADED INTO uk_baseline**

- Loaded by PNC, Monthly. Idempotent on source_file (DELETE-then-COPY per CSV per archive).


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `gid` | `bigint` |  |
| `crime_id` | `text` | Source field "Crime ID"; upstream identifier. NULLABLE - blank for Anti-Social Behaviour (ASB) rows. |
| `record_month` | `text` | YYYY-MM string from source "Month" column. |
| `reported_by` | `text` | Source field "Reported by"; police force that recorded the crime. |
| `falls_within` | `text` | Source field "Falls within"; jurisdictional force (often identical to reported_by). |
| `longitude` | `double precision` | Source field "Longitude"; raw lat/lon from CSV. Unit: "degrees" (EPSG:4326). |
| `latitude` | `double precision` | Source field "Latitude"; raw lat/lon from CSV. Unit: "degrees" (EPSG:4326). |
| `location_text` | `text` | Source field "Location"; anonymised free-text location, e.g. "On or near High Street". |
| `lsoa_code` | `text` | Source field "LSOA code"; LSOA 2011 GSS code (source uses 2011). |
| `lsoa_name` | `text` | Source field "LSOA name"; human-readable 2011 LSOA name. |
| `crime_type` | `text` | Source field "Crime type"; one of ~14 standardised Home Office categories. |
| `last_outcome` | `text` | Outcome snapshot as of the archive that published this row. Stale by design. |
| `context` | `text` | Source field "Context"; rarely populated free-text supplementary detail. |
| `geom` | `geometry(Point,27700)` | Reprojected from EPSG:4326 (longitude, latitude) at load time. |
| `source_file` | `text` | CSV filename this row came from. Used as the idempotency key by the loader. |
| `load_ts` | `date` | Date this row was loaded into PostGIS (CURRENT_DATE default). |
