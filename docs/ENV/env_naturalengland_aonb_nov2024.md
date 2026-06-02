# Natural England Areas of Outstanding Natural Beauty (AONB) for England, November 2024

`env_naturalengland_aonb_nov2024`

<a href="http://localhost:7800/?layer=uk_baseline.env_naturalengland_aonb_nov2024" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

AONBs are now known as National Landscapes (non-statutory rebrand, 2023).

**SOURCE**

- Natural England, via the NE Open Data Hub. Areas of Outstanding Natural Beauty (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/
- AONB designation : https://www.gov.uk/guidance/areas-of-outstanding-natural-beauty-aonbs-designation-and-management

**DEFINITIONS**

- "An area of outstanding natural beauty (AONB) is land protected by the Countryside and Rights of Way Act 2000 (CROW Act). It protects the land to conserve and enhance its natural beauty." (gov.uk, AONB designation and management)
- "'National Landscapes' is the rebranded name for areas of outstanding natural beauty (AONBs). This name change is not statutory." (gov.uk, Protected Landscapes Duty guidance)

**SCOPE**

- England. 140 rows (multiple polygon rows per AONB; 33 named AONBs).

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
| `code` | `character varying` | Source field "code"; AONB code. |
| `name` | `character varying` | Source field "name"; AONB name. |
| `desig_date` | `character varying` | Source field "desig_date"; designation date. Stored as text (e.g. "Dec-72"). |
| `hotlink` | `character varying` | Source field "hotlink"; URL to the Natural England record. |
| `stat_area` | `double precision` | Source field "stat_area"; statutory area as published by Natural England. |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. AONB / National Landscape boundary geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
| `layer` | `character(100)` | Source field "layer"; fixed-string source-layer annotation. Single observed value: "Areas of Outstanding Natural Beauty". |
