# National Trust Land (England & Wales), August 2024

`her_historicengland_national_trust_land_aug2024`

<iframe src="../maps/her_historicengland_national_trust_land_aug2024.html" title="Interactive preview map of her_historicengland_national_trust_land_aug2024" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/her_historicengland_national_trust_land_aug2024.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

One row per National Trust land parcel.

**SOURCE**

- The National Trust. National Trust open data — land.

**DOCUMENTATION**

- National Trust : https://www.nationaltrust.org.uk/

**SCOPE**

- 2,785 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0 (confirm with the National Trust before re-publication).

**LOADED INTO uk_baseline**

- Loaded August 2024.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `objectid` | `bigint` | Source field "OBJECTID"; ArcGIS surrogate key preserved from upstream. |
| `id` | `double precision` | Source field "id"; source feature identifier. |
| `name` | `character varying` | Source field "name"; property name. |
| `lastupdated` | `character varying` | Source field "lastupdated"; date the source record was last updated. |
| `fid_original` | `integer` | ArcGIS source identifier preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(Polygon,27700)` | MultiPolygon in EPSG:27700. National Trust land parcel. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
