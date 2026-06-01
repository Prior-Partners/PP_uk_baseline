# Natural England Special Protection Areas (SPA) for England, April 2026

`env_naturalengland_special_protection_areas_apr2026`

<iframe src="../maps/env_naturalengland_special_protection_areas_apr2026.html" title="Interactive preview map of env_naturalengland_special_protection_areas_apr2026" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/env_naturalengland_special_protection_areas_apr2026.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Natural England, via the NE Open Data Hub (ArcGIS Online platform). Special Protection Areas (England) dataset. Designation authority: Joint Nature Conservation Committee (JNCC).

**DOCUMENTATION**

- NE Open Data Hub  : https://naturalengland-defra.opendata.arcgis.com/
- JNCC SPA overview : https://jncc.gov.uk/our-work/special-protection-areas-overview/

**DEFINITIONS**

- "Special Protection Areas (SPAs) are protected areas for birds in the UK classified under" the relevant regulations, for species "listed in Annex I of the Birds Directive (79/409/EEC as amended)." (JNCC, Special Protection Areas overview)

**SCOPE**

- England. 1,194 rows representing 88 distinct SPA sites; geometry is exploded to one polygon part per row.

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
| `spa_name` | `character varying` | Source field "spa_name"; SPA name. |
| `spa_code` | `character varying` | Source field "spa_code"; SPA code. |
| `spa_area` | `double precision` | Source field "spa_area"; SPA area as published by Natural England. |
| `grid_ref` | `character varying` | Source field "grid_ref"; Ordnance Survey grid reference. |
| `easting` | `double precision` | Source field "easting"; site easting. Unit: "metres" (EPSG:27700). |
| `northing` | `double precision` | Source field "northing"; site northing. Unit: "metres" (EPSG:27700). |
| `latitude` | `character varying` | Source field "latitude"; site latitude (WGS84 degrees). |
| `longitude` | `character varying` | Source field "longitude"; site longitude (WGS84 degrees). |
| `name` | `character varying` | Source field "name"; secondary name field carried through from the Natural England ArcGIS Online export (blank in this dataset). |
| `status` | `character varying` | Source field "status"; designation status. |
| `id` | `double precision` | Source field "id"; carried through from the Natural England ArcGIS Online export. |
| `file_` | `character varying` | Source field "file_"; carried through from the Natural England ArcGIS Online export. |
| `area` | `double precision` | Source field "area"; secondary area value carried through from the Natural England ArcGIS Online export. |
| `easting0` | `double precision` | Source field "easting0"; secondary easting value carried through from the Natural England ArcGIS Online export. |
| `northing0` | `double precision` | Source field "northing0"; secondary northing value carried through from the Natural England ArcGIS Online export. |
| `gis_date` | `character varying` | Source field "gis_date"; date field carried through from the Natural England ArcGIS Online export. |
| `version` | `integer` | Source field "version"; source version number. |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. SPA boundary geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
