# National Trust Land — Limited Access (England & Wales), October 2025

`her_nationaltrust_limited_access_oct2025`

<iframe src="../../maps/her_nationaltrust_limited_access_oct2025.html" title="Interactive preview map of her_nationaltrust_limited_access_oct2025" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/her_nationaltrust_limited_access_oct2025.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- The National Trust. National Trust Open Data — Land, Limited Access.

**DOCUMENTATION**

- National Trust Limited Access (data.gov.uk) : https://www.data.gov.uk/dataset/ded1ab59-afa7-4632-8ff4-24d07cba1e42/national-trust-open-data-land-limited-access

**DEFINITIONS**

- "The National Trust Limited Access data shows areas where access is restricted for at least one of the following reasons: The land is enclosed as part of a National Trust Estate. Access is restricted to a dense path network. There are specific reasons the land is not Always Open e.g. Safety concerns." (National Trust Open Data, Land Limited Access)

**SCOPE**

- 596 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0 (confirm with the National Trust before re-publication).

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | ArcGIS source identifier preserved at load. |
| `id` | `double precision` | Source field "id"; source feature identifier. |
| `name` | `character varying` | Source field "name"; property name. |
| `lastupdated` | `timestamp with time zone` | Source field "lastupdated"; date the source record was last updated. |
| `wd25cd` | `character varying` | Joined at load from ONS Ward 2025 lookup; 2025 Ward GSS code. |
| `wd25nm` | `character varying` | Joined at load from ONS Ward 2025 lookup; 2025 Ward name. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. National Trust land parcel. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the geometry falls. Blank or NULL where outside any SDS area. |
