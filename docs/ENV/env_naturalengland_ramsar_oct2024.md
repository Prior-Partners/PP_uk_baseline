# Natural England Ramsar sites for England, October 2024

`env_naturalengland_ramsar_oct2024`

<img src="../../maps/env_naturalengland_ramsar_oct2024.png" alt="Styling preview of env_naturalengland_ramsar_oct2024" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

<a href="http://localhost:7800/?layer=uk_baseline.env_naturalengland_ramsar_oct2024" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Natural England, via the NE Open Data Hub (ArcGIS Online platform). Ramsar (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub  : https://naturalengland-defra.opendata.arcgis.com/
- NE Ramsar dataset : https://naturalengland-defra.opendata.arcgis.com/datasets/13b5f06edc88471db479b49b4ac04a43_0/about

**DEFINITIONS**

- "A Ramsar site is the land listed as a Wetland of International Importance under the Convention on Wetlands of International Importance Especially as Waterfowl Habitat (the Ramsar Convention) 1973." (Natural England, Ramsar (England) dataset page)

**SCOPE**

- England. 1,107 rows representing 73 distinct Ramsar sites; geometry is exploded to one polygon part per row.

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
| `name` | `character varying` | Source field "name"; Ramsar site name. |
| `code` | `character varying` | Source field "code"; Ramsar site code. |
| `area` | `double precision` | Source field "area"; site area as published by Natural England. |
| `grid_ref` | `character varying` | Source field "grid_ref"; Ordnance Survey grid reference. |
| `easting` | `double precision` | Source field "easting"; site easting. Unit: "metres" (EPSG:27700). |
| `northing` | `double precision` | Source field "northing"; site northing. Unit: "metres" (EPSG:27700). |
| `latitude` | `character varying` | Source field "latitude"; site latitude (WGS84 degrees). |
| `longitude` | `character varying` | Source field "longitude"; site longitude (WGS84 degrees). |
| `name0` | `character varying` | Source field "name0"; secondary name field carried through from the Natural England ArcGIS Online export (blank in this dataset). |
| `status` | `character varying` | Source field "status"; designation status. Observed value: "Listed". |
| `id` | `double precision` | Source field "id"; carried through from the Natural England ArcGIS Online export. |
| `file_` | `character varying` | Source field "file_"; carried through from the Natural England ArcGIS Online export. |
| `area0` | `double precision` | Source field "area0"; secondary area value carried through from the Natural England ArcGIS Online export. |
| `easting0` | `double precision` | Source field "easting0"; secondary easting value carried through from the Natural England ArcGIS Online export. |
| `northing0` | `double precision` | Source field "northing0"; secondary northing value carried through from the Natural England ArcGIS Online export. |
| `gis_date` | `character varying` | Source field "gis_date"; date field carried through from the Natural England ArcGIS Online export. |
| `version` | `integer` | Source field "version"; source version number. |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Ramsar site boundary geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
| `layer` | `character(100)` | Source field "layer"; fixed-string source-layer annotation. Single observed value: "Ramsar". |
