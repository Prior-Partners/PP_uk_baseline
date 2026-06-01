# Historic England Conservation Areas (England), July 2025

`her_historicengland_conservation_areas_jul2025`

<iframe src="../maps/her_historicengland_conservation_areas_jul2025.html" title="Interactive preview map of her_historicengland_conservation_areas_jul2025" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/her_historicengland_conservation_areas_jul2025.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Historic England (compiler). Conservation areas are designated by Local Planning Authorities (LPAs) under the Planning (Listed Buildings and Conservation Areas) Act 1990.

**DOCUMENTATION**

- HE data downloads  : https://historicengland.org.uk/listing/the-list/data-downloads/
- Conservation Areas : https://historicengland.org.uk/advice/your-home/owning-historic-property/conservation-area/

**DEFINITIONS**

- Conservation areas protect the special architectural and historic interest of a place — the features that make it unique and distinctive. (Historic England, Conservation Areas)

**SCOPE**

- England. 14,017 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Historic England.

**DATA QUALITY CAVEATS**

- Compiled from Local Planning Authority sources; completeness and boundary precision vary by LPA.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | ArcGIS source identifier preserved at load. |
| `uid` | `double precision` | Source field "uid"; source unique identifier. |
| `name` | `character varying` | Source field "name"; conservation area name. |
| `date_of_de` | `character varying` | Source field "date_of_de…"; date of designation. |
| `date_updat` | `character varying` | Source field "date_updat…"; date the record was last updated. |
| `lpa` | `character varying` | Source field "lpa"; Local Planning Authority that designated the area (e.g. "Hastings", "St. Albans"). |
| `capture_sc` | `character varying` | Source field "capture_sc…"; cartographic scale at which the geometry was captured. |
| `x` | `integer` | Source field "x"; representative point easting. Unit: metres (EPSG:27700). |
| `y` | `integer` | Source field "y"; representative point northing. Unit: metres (EPSG:27700). |
| `wd25cd` | `character varying` | Joined at load from ONS Ward 2025 lookup; 2025 Ward GSS code. |
| `wd25nm` | `character varying` | Joined at load from ONS Ward 2025 lookup; 2025 Ward name. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Conservation area boundary. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the geometry falls. Blank or NULL where outside any SDS area. |
