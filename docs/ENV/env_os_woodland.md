# Ordnance Survey OS OpenMap Local — Woodland for Great Britain

`env_os_woodland`

<iframe src="../maps/env_os_woodland.html" title="Interactive preview map of env_os_woodland" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/env_os_woodland.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Ordnance Survey (OS), OS OpenMap Local product.

**DOCUMENTATION**

- OS OpenMap Local      : https://www.ordnancesurvey.co.uk/products/os-open-map-local
- Woodland feature spec : https://docs.os.uk/os-downloads/products/maps-and-imagery-portfolio/os-openmap-local/os-openmap-local-technical-specification/feature-types/woodland

**DEFINITIONS**

- "Areas of trees (coniferous, non-coniferous and mixed) are represented as polygons." (OS OpenMap Local Technical Specification, Woodland)

**SCOPE**

- Great Britain. 1,543,618 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Polygon.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data © Crown copyright and database right" required).

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `character varying` | Source field "id"; OS source feature identifier. |
| `feature_code` | `bigint` | Source field "feature_code"; OS feature code. Single observed value: 15999. |
| `fid_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `geom` | `geometry(Polygon,27700)` | Polygon in EPSG:27700. Woodland polygon geometry. |
| `gid` | `bigint` |  |
