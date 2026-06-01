# Defra - Department for Environment, Food and Rural Affairs — Environment Agency Flood Map for Planning, Flood Zones 2 and 3 (river and sea), April 2026

`env_defra_flood_zones_2_3_river_sea_april2026`

<iframe src="../maps/env_defra_flood_zones_2_3_river_sea_april2026.html" title="Interactive preview map of env_defra_flood_zones_2_3_river_sea_april2026" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/env_defra_flood_zones_2_3_river_sea_april2026.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Environment Agency (EA), part of the Department for Environment, Food and Rural Affairs (Defra). Flood Map for Planning product.

**DOCUMENTATION**

- EA Flood Map for Planning : https://environment.data.gov.uk/dataset/bed63fc1-dd26-4685-b143-2941088923b3
- EA Flood Map guidance     : https://www.gov.uk/guidance/flood-map-for-planning

**DEFINITIONS**

- "The Flood Map for Planning shows river and sea flooding data for England. It does not include other sources of flooding." (gov.uk Flood Map guidance)
- Flood Zone 2: "Land assessed as having between a 1 in 100 and 1 in 1,000 annual probability of river flooding (1% – 0.1%), or between a 1 in 200 and 1 in 1,000 annual probability of sea flooding (0.5% – 0.1%) in any year." (EA Flood Map guidance)
- Flood Zone 3: "Land assessed as having a 1 in 100 or greater annual probability of river flooding (>1%), or a 1 in 200 or greater annual probability of sea flooding (>0.5%) in any year." (EA Flood Map guidance)

**SCOPE**

- England. 3,559,142 rows.

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
| `origin` | `character varying(64)` | Source field "origin"; derivation method of the polygon. Observed values: "modelled", "direct rainfall model", "modelled and recorded", "modelled and direct rainfall model", "recorded", "local evidence", and combinations. |
| `flood_zone` | `character varying(3)` | Source field "flood_zone"; Flood Zone classification. Observed values: "FZ2", "FZ3" (see table DEFINITIONS). |
| `flood_source` | `character varying(32)` | Source field "flood_source"; flood source. Observed values: "river", "sea", "river and sea", "river / undefined", "undefined", "unknown". |
| `shape_length` | `double precision` | Source field "Shape_Length"; legacy ArcGIS shape perimeter. |
| `shape_area` | `double precision` | Source field "Shape_Area"; legacy ArcGIS shape area. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Flood-zone polygon geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
