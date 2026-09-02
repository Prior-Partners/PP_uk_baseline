# Northern Ireland Statistics and Research Agency (NISRA) Census 2021 Super Data Zones, Northern Ireland extent, February 2023

<p class="layer-short">Super Data Zone Boundary 2021 (Northern Ireland)</p>

`adm_nisra_sdz_boundary_2021`

**SOURCE**

- Northern Ireland Statistics and Research Agency (NISRA). File SDZ2021.shp from geography-sdz2021-esri-shapefile.zip, published 21 February 2023. All source fields copied as published; nothing derived, renamed or filtered. Geometry reprojected at load (see CRS).

**DOCUMENTATION**

- Super Data Zone boundaries in GIS format : https://www.nisra.gov.uk/publications/super-data-zone-boundaries-gis-format
- Super Data Zones Census 2021 : https://www.nisra.gov.uk/support/geography/super-data-zones-census-2021
- Information paper : https://www.nisra.gov.uk/files/nisra/publications/geography-new-statistical-output-geographies-for-northern-ireland-derived-from-census-2021.PDF

**DEFINITIONS**

- "Super Data Zones (SDZ2021) are a new statistical output geography, introduced in Northern Ireland after the 2021 Census." (NISRA Super Data Zones Census 2021 page)
- "There are 3,780 Data Zones (DZ2021) across Northern Ireland, which nest within the 850 Super Data Zones (SDZ2021). These in turn nest within the 80 District Electoral Areas (DEA2014) and 11 Local Government Districts (LGD2014)." (NISRA Data Zones Census 2021 page)
- "The average size of the Data Zone areas in population terms is approximately 500 persons and 200 households, while the corresponding figures for Super Data Zones are 2,240 persons and 900 households." (NISRA information paper)

**SCOPE**

- Northern Ireland. 850 Super Data Zones, built from the Data Zones in uk_baseline.adm_nisra_dz_boundary_2021. The Northern Ireland counterpart of the Middle layer Super Output Area (MSOA).

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Reprojected at load from TM65 / Irish Grid (EPSG:29902), the CRS as shipped, by GDAL 3.12.3 through the best available Helmert pipeline (TM65 to WGS 84 (2), then OSGB36 to WGS 84 (6)); stated accuracy 3 m. The OSTN15 grid was not available.

**LICENCE**

- Open Government Licence v3.0. "Contains Ordnance Survey of Northern Ireland information licensed under the Open Government Licence v3.0." (NISRA)

**DATA QUALITY CAVEATS**

- Positions are accurate to about 3 m because of the datum shift from Irish Grid; do not use for survey-level work. Eastings in British National Grid are small or negative for the west of Northern Ireland; this is correct for that grid.
- The publisher gives no field-level definitions; columns are carried under their source names. area_ha and perim_km were attached by the publisher from a rounded areas file.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `sdz2021_cd` | `character varying` | Source field `SDZ2021_cd`; Super Data Zone 2021 code (N21 prefix). |
| `sdz2021_nm` | `character varying` | Source field `SDZ2021_nm`; Super Data Zone 2021 name. |
| `dea2014_cd` | `character varying` | Source field `DEA2014_cd`; parent District Electoral Area 2014 code. |
| `dea2014_nm` | `character varying` | Source field `DEA2014_nm`; parent District Electoral Area 2014 name. |
| `lgd2014_cd` | `character varying` | Source field `LGD2014_cd`; parent Local Government District 2014 code. |
| `lgd2014_nm` | `character varying` | Source field `LGD2014_nm`; parent Local Government District 2014 name. |
| `area_ha` | `double precision` | Source field `Area_ha`; [UNDOCUMENTED] publisher area figure, carried as shipped; the field name states hectares. |
| `perim_km` | `double precision` | Source field `Perim_km`; [UNDOCUMENTED] publisher perimeter figure, carried as shipped; the field name states kilometres. |
| `geom` | `geometry(MultiPolygon,27700)` | Source shapefile geometry; MultiPolygon reprojected at load from TM65 / Irish Grid (EPSG:29902) to EPSG:27700, accuracy about 3 m. |
