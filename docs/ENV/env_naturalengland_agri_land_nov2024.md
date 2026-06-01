# `env_naturalengland_agri_land_nov2024`

Natural England Agricultural Land Classification (ALC) survey for England, November 2024.

**SOURCE**

- Natural England, via the NE Open Data Hub. Agricultural Land Classification (post-war survey) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/
- ALC guidance     : https://www.gov.uk/government/publications/agricultural-land-assess-proposals-for-development/guide-to-assessing-development-proposals-on-agricultural-land

**DEFINITIONS**

- "ALC uses a grading system to enable you to assess and compare the quality of agricultural land in England and Wales." (gov.uk, Guide to assessing development proposals on agricultural land)
- "A combination of climate, topography and soil characteristics and their unique interaction determines the limitation and grade of the land." (gov.uk, Guide to assessing development proposals on agricultural land)

**SCOPE**

- England. 5,926 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | Original feature id preserved at load. |
| `geogext` | `character varying` | Source field "geogext"; survey geographic-extent code. Observed values include "6EW7", "6U", "8". |
| `area` | `double precision` | Source field "area"; legacy shape area carried from the source. |
| `alc_grade` | `character varying` | Source field "alc_grade"; Agricultural Land Classification grade. Observed values: "Grade 1" to "Grade 5", "Urban", "Non Agricultural", "Exclusion". |
| `perimeter` | `double precision` | Source field "perimeter"; legacy shape perimeter carried from the source. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Agricultural Land Classification polygon geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
