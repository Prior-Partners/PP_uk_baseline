# Natural England Country Parks for England, June 2023

`env_naturalengland_country_parks_jun2023`

<a href="http://localhost:7800/?layer=uk_baseline.env_naturalengland_country_parks_jun2023" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Natural England, via the NE Open Data Hub. Country Parks (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/

**DEFINITIONS**

- Country parks are "public green spaces often at the edge of urban areas which provide places to enjoy the outdoors and experience nature in an informal semi-rural park setting." (data.gov.uk, Country Parks (England), Natural England)

**SCOPE**

- England. 527 rows.

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
| `ref_code` | `double precision` | Source field "ref_code"; Natural England reference code. |
| `theme` | `character varying` | Source field "theme"; theme classification. Observed value: "country parks". |
| `name` | `character varying` | Source field "name"; country park name. |
| `status` | `character varying` | Source field "status"; status. Observed values: "Known as a Country Park", "Accredited". |
| `measure` | `double precision` | Source field "measure"; site area as published by Natural England. |
| `gridref` | `character varying` | Source field "gridref"; Ordnance Survey grid reference. |
| `label` | `character varying` | Source field "label"; display label. |
| `hyperlink` | `character varying` | Source field "hyperlink"; URL to the Natural England record. |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Country park boundary geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
