# `env_defra_flood_zone_jan2025`

Defra - Department for Environment, Food and Rural Affairs — Environment Agency Flood Map for Planning, Flood Zones 2 and 3, January 2025.

**SOURCE**

- Environment Agency (EA), part of the Department for Environment, Food and Rural Affairs (Defra). Flood Map for Planning product. Distributed via data.gov.uk.

**DOCUMENTATION**

- EA Flood Map for Planning landing : https://environment.data.gov.uk/dataset/bed63fc1-dd26-4685-b143-2941088923b3
- EA Flood Map guidance             : https://www.gov.uk/guidance/flood-map-for-planning
- gov.uk Flood Map for Planning     : https://flood-map-for-planning.service.gov.uk/

**DEFINITIONS**

- "The Flood Map for Planning shows river and sea flooding data for England. It does not include other sources of flooding." (gov.uk Flood Map guidance)
- Flood Zone 2: "Land assessed as having between a 1 in 100 and 1 in 1,000 annual probability of river flooding (1% – 0.1%), or between a 1 in 200 and 1 in 1,000 annual probability of sea flooding (0.5% – 0.1%) in any year." (EA Flood Map guidance)
- Flood Zone 3: "Land assessed as having a 1 in 100 or greater annual probability of river flooding (>1%), or a 1 in 200 or greater annual probability of sea flooding (>0.5%) in any year." (EA Flood Map guidance)

**SCOPE**

- England. 12,247,889 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0. © Environment Agency copyright and database right.

**LOADED INTO uk_baseline**

- Loaded January 2025.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `objectid` | `numeric` | Source field "OBJECTID"; ArcGIS surrogate key preserved from upstream. |
| `origin` | `character varying(64)` | Source field "origin"; derivation method of the polygon. Observed values: "modelled", "direct rainfall model", "local evidence", "recorded" (and combinations). |
| `flood_zone` | `character varying(3)` | Source field "flood_zone"; Flood Zone classification. Observed values: "FZ2", "FZ3" (see table DEFINITIONS for the zone definitions). |
| `flood_sour` | `character varying(32)` | Source field "flood_sour" (truncated from upstream); flood source. Observed values: "river", "sea", "river and sea". |
| `shape_leng` | `numeric` | Source field "Shape_Length"; legacy ArcGIS shape perimeter. |
| `shape_area` | `numeric` | Source field "Shape_Area"; legacy ArcGIS shape area. |
| `id_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `geom` | `geometry(Polygon,27700)` | Polygon in EPSG:27700. Flood-zone polygon geometry. |
