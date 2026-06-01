# Ordnance Survey OS Open Greenspace for Great Britain, April 2025

`env_os_green_space_apr2025`

<iframe src="../../maps/env_os_green_space_apr2025.html" title="Interactive preview map of env_os_green_space_apr2025" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/env_os_green_space_apr2025.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Ordnance Survey (OS), OS Open Greenspace product.

**DOCUMENTATION**

- OS Open Greenspace : https://www.ordnancesurvey.co.uk/products/os-open-greenspace

**DEFINITIONS**

- "Information about publicly accessible urban green spaces across Great Britain. It includes parks, sports facilities and other recreational areas." (OS Open Greenspace product page)

**SCOPE**

- Great Britain. 196,619 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data © Crown copyright and database right" required).

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `character varying` | Source field "id"; OS source feature identifier. |
| `function` | `character varying` | Source field "function"; greenspace function. Observed values include "Play Space", "Public Park Or Garden", "Playing Field", "Religious Grounds", "Allotments Or Community Growing Spaces", "Cemetery", "Golf Course", "Bowling Green", "Tennis Court". |
| `distname1` | `character varying` | Source field "distname1"; distinctive name of the greenspace (where present). |
| `distname2` | `character varying` | Source field "distname2"; additional distinctive name (where present). |
| `distname3` | `character varying` | Source field "distname3"; additional distinctive name (where present). |
| `distname4` | `character varying` | Source field "distname4"; additional distinctive name (where present). |
| `fid_original` | `bigint` | Original feature id preserved at load. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `rgn22cd` | `character varying` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `character varying` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `character varying` | Internal categorisation: Spatial Development Strategy (SDS) area where the feature falls. Blank or NULL where outside any SDS area. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Greenspace site polygon geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
