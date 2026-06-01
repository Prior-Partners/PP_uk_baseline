# Natural England Environmentally Sensitive Areas (ESA) for England, June 2024

`env_naturalengland_environmentally_sensitive_areas_jun2024`

**SOURCE**

- Natural England, via the NE Open Data Hub. Environmentally Sensitive Areas (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/

**DEFINITIONS**

- "The Environmentally Sensitive Areas were introduced in 1987 to offer incentives to encourage farmers to adopt agricultural practices which would safeguard and enhance parts of the country of particularly high landscape, wildlife or historic value." (data.gov.uk, Environmentally Sensitive Areas (England), Natural England)
- "The scheme has now closed to new applicants." (data.gov.uk, Environmentally Sensitive Areas (England), Natural England)

**SCOPE**

- England. 7,331 rows (multiple polygon rows per ESA).

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Polygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `objectid` | `bigint` | Source field "OBJECTID"; ArcGIS surrogate key preserved from upstream. |
| `ref_code` | `character varying` | Source field "ref_code"; ESA code (e.g. "LD"). |
| `name` | `character varying` | Source field "name"; ESA name (e.g. "LAKE DISTRICT"). |
| `measure` | `double precision` | Source field "measure"; ESA area as published by Natural England. |
| `desig_date` | `character varying` | Source field "desig_date"; designation year. Stored as text (e.g. "1993"). |
| `hotlink` | `character varying` | Source field "hotlink"; URL to the Natural England record. |
| `fid_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `fid` | `bigint` |  |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `geom` | `geometry(Polygon,27700)` | Polygon in EPSG:27700. ESA boundary geometry. |
| `gid` | `bigint` |  |
