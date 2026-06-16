# Natural England Special Areas of Conservation (SAC) for England, October 2024

<p class="layer-short">Special Areas Conservation</p>

`env_naturalengland_special_areas_conservation_oct2024`

<img src="../../maps/env_naturalengland_special_areas_conservation_oct2024.png" alt="Styling preview of env_naturalengland_special_areas_conservation_oct2024" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Natural England, via the NE Open Data Hub (ArcGIS Online platform). Special Areas of Conservation (England) dataset. Designation authority: Joint Nature Conservation Committee (JNCC).

**DOCUMENTATION**

- NE Open Data Hub  : https://naturalengland-defra.opendata.arcgis.com/
- JNCC SAC overview : https://jncc.gov.uk/our-work/special-areas-of-conservation-overview/

**DEFINITIONS**

- "Special Areas of Conservation (SACs) are protected areas in the UK designated under" the Habitats Directive - the UK is "required to establish a network of important high-quality conservation sites that will make a significant contribution to conserving the habitats and species identified in Annexes I and II, respectively, of European Council Directive 92/43/EEC on the conservation of natural habitats and of wild fauna and flora, known as the Habitats Directive." (JNCC, Special Areas of Conservation overview)

**SCOPE**

- England. 48,238 rows representing 252 distinct SAC sites; geometry is exploded to one polygon part per row.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Polygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `objectid` | `bigint` | Source field "OBJECTID"; ArcGIS surrogate key preserved from upstream. |
| `sac_name` | `character varying` | Source field "sac_name"; SAC name. |
| `sac_code` | `character varying` | Source field "sac_code"; SAC code. |
| `sac_area` | `double precision` | Source field "sac_area"; SAC area as published by Natural England. |
| `grid_ref` | `character varying` | Source field "grid_ref"; Ordnance Survey grid reference. |
| `easting` | `double precision` | Source field "easting"; site easting. Unit: "metres" (EPSG:27700). |
| `northing` | `double precision` | Source field "northing"; site northing. Unit: "metres" (EPSG:27700). |
| `latitude` | `character varying` | Source field "latitude"; site latitude (WGS84 degrees). |
| `longitude` | `character varying` | Source field "longitude"; site longitude (WGS84 degrees). |
| `name` | `character varying` | Source field "name"; secondary name field carried through from the Natural England ArcGIS Online export (blank in this dataset). |
| `status` | `character varying` | Source field "status"; designation status. Observed value: "Designated". |
| `id` | `bigint` | Source field "id"; carried through from the Natural England ArcGIS Online export. |
| `file_` | `character varying` | Source field "file_"; carried through from the Natural England ArcGIS Online export. |
| `area` | `double precision` | Source field "area"; secondary area value carried through from the Natural England ArcGIS Online export. |
| `easting0` | `double precision` | Source field "easting0"; secondary easting value carried through from the Natural England ArcGIS Online export. |
| `northing0` | `double precision` | Source field "northing0"; secondary northing value carried through from the Natural England ArcGIS Online export. |
| `gis_date` | `character varying` | Source field "gis_date"; date field carried through from the Natural England ArcGIS Online export. |
| `version` | `bigint` | Source field "version"; source version number. |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `fid_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `fid` | `bigint` |  |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `geom` | `geometry(Polygon,27700)` | Polygon in EPSG:27700. SAC boundary geometry. |
| `gid` | `bigint` |  |
