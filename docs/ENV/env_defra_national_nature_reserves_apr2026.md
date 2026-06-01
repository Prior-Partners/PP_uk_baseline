# Defra - Department for Environment, Food and Rural Affairs — Environment Agency National Nature Reserves (NNRs) in England, April 2026

`env_defra_national_nature_reserves_apr2026`

**SOURCE**

- Natural England (designating body), distributed under the Department for Environment, Food and Rural Affairs (Defra) family. Source dataset on the Natural England Open Data Hub.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/
- NE NNR landing   : https://www.gov.uk/government/publications/national-nature-reserves-in-england
- About NNRs       : https://www.gov.uk/government/publications/national-nature-reserves-in-england/national-nature-reserves-in-england

**DEFINITIONS**

- "National Nature Reserves (NNRs) are places where wildlife comes first. They were established to protect the most significant areas of habitat and of geological formations and to provide outdoor laboratories for research." (gov.uk NNR landing page)

**SCOPE**

- England. 299 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | Original feature id preserved at load. |
| `hyperlink` | `character varying` | Source field "hyperlink"; URL to the NNR record on the Natural England website. |
| `ref_code` | `character varying` | Source field "ref_code"; NNR reference code (7-digit numeric). NOT unique across rows — a single NNR may span multiple polygon rows. |
| `name` | `character varying` | Source field "name"; NNR site name (upper case). |
| `measure` | `double precision` | Source field "measure"; numeric measurement as published. |
| `label` | `character varying` | Source field "label"; NNR display label (e.g. "Wealden Heaths (NNR)"). |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. NNR boundary geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
