# Natural England Sites of Special Scientific Interest (SSSI) for England, April 2026

`env_naturalengland_sssi_apr2026`

<iframe src="../../maps/env_naturalengland_sssi_apr2026.html" title="Interactive preview map of env_naturalengland_sssi_apr2026" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/env_naturalengland_sssi_apr2026.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Natural England, via the NE Open Data Hub. Sites of Special Scientific Interest (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub     : https://naturalengland-defra.opendata.arcgis.com/
- gov.uk SSSI guidance : https://www.gov.uk/guidance/protected-areas-sites-of-special-scientific-interest

**DEFINITIONS**

- "Natural England will 'notify' (or designate) the land as a site of special scientific interest (SSSI)" when "it believes the site has features of special interest, such as its: wildlife, geology, landform." (gov.uk, Protected areas: sites of special scientific interest)

**SCOPE**

- England. 4,777 rows across 4,128 distinct reference codes.

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
| `ref_code` | `character varying` | Source field "ref_code"; SSSI reference code (7-digit). |
| `name` | `character varying` | Source field "name"; SSSI name (includes " SSSI" suffix). |
| `measure` | `double precision` | Source field "measure"; SSSI area as published by Natural England. |
| `label` | `character varying` | Source field "label"; display label. |
| `hyperlink` | `character varying` | Source field "hyperlink"; URL to the Natural England record. |
| `contact_no` | `character varying` | Source field "contact_no"; Natural England contact phone number. |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. SSSI boundary geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
| `layer` | `character(100)` | Source field "layer"; fixed-string source-layer annotation. Single observed value: "Sites of Special Scientific Interest". |
