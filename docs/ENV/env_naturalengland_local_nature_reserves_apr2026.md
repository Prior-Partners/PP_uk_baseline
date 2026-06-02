# Natural England Local Nature Reserves (LNR) for England, April 2026

`env_naturalengland_local_nature_reserves_apr2026`

<a href="http://localhost:7800/?layer=uk_baseline.env_naturalengland_local_nature_reserves_apr2026" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Natural England, via the NE Open Data Hub. Local Nature Reserves (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/

**DEFINITIONS**

- "Local Nature Reserves (LNRs) are a statutory designation made under Section 21 of the National Parks and Access to the Countryside Act 1949 by principal local authorities." (data.gov.uk, Local Nature Reserves (England), Natural England)

**SCOPE**

- England. 1,925 rows.

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
| `ref_code` | `character varying` | Source field "ref_code"; LNR reference code (7-digit). |
| `name` | `character varying` | Source field "name"; LNR name (upper case). |
| `measure` | `double precision` | Source field "measure"; LNR area as published by Natural England. |
| `label` | `character varying` | Source field "label"; display label (e.g. "Clarksons Wood (LNR)"). |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. LNR boundary geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
