# Defra - Department for Environment, Food and Rural Affairs — Environment Agency Flood Map for Planning, Flood Zones with climate-change allowance, July 2025

`env_defra_flood_zones_plus_climate_change_july2025`

**SOURCE**

- Environment Agency (EA), part of the Department for Environment, Food and Rural Affairs (Defra). Flood Map for Planning — climate-change extent dataset.

**DOCUMENTATION**

- EA Flood Map for Planning  : https://environment.data.gov.uk/dataset/bed63fc1-dd26-4685-b143-2941088923b3
- EA climate-change guidance : https://www.gov.uk/guidance/flood-risk-assessments-climate-change-allowances

**DEFINITIONS**

- "Climate change allowances are predictions of anticipated change for: peak river flow, peak rainfall intensity, sea level rise, offshore wind speed and extreme wave height." (gov.uk "What climate change allowances are")

**SCOPE**

- England. 672,790 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0. © Environment Agency.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `integer` | Source identifier preserved at load. |
| `fid_original` | `bigint` | Original feature id preserved at load. |
| `flood_source` | `character varying(32)` | Source field "flood_source"; flood source. Observed values: "river", "sea", "river and sea", "unknown". |
| `name` | `character varying(32)` | Source field "name"; scenario tag. Observed values: "Flood Zones plus climate change", "Unavailable". |
| `shape_length` | `double precision` | Source field "Shape_Length"; legacy ArcGIS shape perimeter. |
| `shape_area` | `double precision` | Source field "Shape_Area"; legacy ArcGIS shape area. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Climate-change flood-extent polygon geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
