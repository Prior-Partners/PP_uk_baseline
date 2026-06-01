# ONS Wards (electoral wards), England & Wales extent, May 2025

`adm_ons_ward_boundary_may2025`

**SOURCE**

- Office for National Statistics (ONS), Open Geography Portal.

**DOCUMENTATION**

- Dataset page : https://geoportal.statistics.gov.uk/datasets/6ba7cf950a504d82809131c945fe70f1_0/about
- Digital boundaries methods : https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries

**DEFINITIONS**

- "Generalised (20m) - clipped to the coastline (Mean High Water mark)." (ONS digitalboundaries page, definition of BGC)

**SCOPE**

- England & Wales.
- 8,405 wards.

**CRS**

- EPSG:27700 (British National Grid / BNG).

**LICENCE**

- Open Government Licence v3.0.

**ENRICHMENT**

- lad25cd, lad25nm, lad25nmw : joined from ONS Ward -> LAD lookup (2025 LAD).
- rgn22cd, rgn22nm : joined from ONS Ward -> Region lookup (2022 region).
- sds_boundary : Spatial Development Strategy area name (e.g. "Greater London").

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `gid` | `integer` |  |
| `wd25cd` | `character varying` | Source field "WD25CD"; ONS GSS 9-character Ward code. |
| `wd25nm` | `character varying` | Source field "WD25NM"; human-readable Ward name (English). |
| `wd25nmw` | `character varying` | Source field "WD25NMW"; human-readable Ward name (Welsh, populated where applicable). |
| `lad25cd` | `character varying` | Joined at load from ONS Ward->LAD lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load; 2025 LAD name (English). |
| `lad25nmw` | `character varying` | Joined at load; 2025 LAD name (Welsh, populated where applicable). |
| `bng_e` | `integer` | Source field "BNG_E"; Ward centroid easting. Unit: "metres". |
| `bng_n` | `integer` | Source field "BNG_N"; Ward centroid northing. Unit: "metres". |
| `long` | `double precision` | Source field "LONG"; Ward centroid longitude. Unit: "degrees". |
| `lat` | `double precision` | Source field "LAT"; Ward centroid latitude. Unit: "degrees". |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GUID-format unique identifier. |
| `geom` | `geometry(MultiPolygon,27700)` | Source field "geometry"; MultiPolygon in EPSG:27700. BGC = 20m generalised, clipped to Mean High Water — see table comment. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Unit: hectares. Stale if geometry is later edited. |
| `rgn22cd` | `text` | Joined at load from ONS Ward->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the geometry falls (e.g. "Greater London", "West Midlands", "Greater Manchester"). Blank or NULL where the geometry is outside any SDS area. |
