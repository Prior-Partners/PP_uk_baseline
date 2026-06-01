# Natural England Ancient Woodland Inventory (England), March 2026

`env_naturalengland_ancient_woodland_mar2026`

**SOURCE**

- Natural England, via the NE Open Data Hub. Ancient Woodland (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub          : https://naturalengland-defra.opendata.arcgis.com/
- Ancient woodland guidance : https://www.gov.uk/guidance/ancient-woodland-and-veteran-trees-protection-surveys-licences

**DEFINITIONS**

- "Ancient woodland is an area that has been wooded continuously since at least 1600AD." (data.gov.uk, Ancient Woodland (England), Natural England)

**SCOPE**

- England. 55,647 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**DATA QUALITY CAVEATS**

- Some areas overlap with env_naturalengland_ancient_woodland_revised_apr2026 (the revised inventory); the two datasets are not mutually exclusive.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | Original feature id preserved at load. |
| `name` | `character varying` | Source field "name"; woodland site name. |
| `theme` | `character varying` | Source field "theme"; theme classification. Observed value: "ancient woodland". |
| `themname` | `character varying` | Source field "themname"; theme name. Observed themname/status pairs: "Ancient & Semi-Natural Woodland"/ASNW, "Ancient Replanted Woodland"/PAWS, "Ancient Wood Pasture"/AWP. |
| `themid` | `double precision` | Source field "themid"; theme identifier. |
| `status` | `character varying` | Source field "status"; status code. Observed values: "ASNW", "PAWS", "AWP". |
| `perimeter` | `double precision` | Source field "perimeter"; legacy shape perimeter carried from the source. |
| `area` | `double precision` | Source field "area"; legacy shape area carried from the source. |
| `x_coord` | `integer` | Source field "x_coord"; representative point easting. Unit: "metres" (EPSG:27700). |
| `y_coord` | `integer` | Source field "y_coord"; representative point northing. Unit: "metres" (EPSG:27700). |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Ancient woodland polygon geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
| `layer` | `character(100)` | Source field "layer"; fixed-string source-layer annotation. Single observed value: "Ancient Woodland". |
