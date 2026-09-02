# Scottish Government Data Zones 2022, Scotland extent, December 2024

<p class="layer-short">Data Zone Boundary 2022</p>

`adm_sg_dz_boundary_2022`

**SOURCE**

- Scottish Government, Geographic Information Science and Analysis Team. File SG_DataZone_Bdry_2022.shp from SG_DataZoneBdry_2022.zip, published 16 December 2024. All source fields copied as published; nothing derived, renamed or filtered.

**DOCUMENTATION**

- Dataset record (data.gov.uk) : https://www.data.gov.uk/dataset/afe1aca6-bea2-4283-8847-eecf98ab41a4/data-zone-boundaries-2022
- Small area statistics collection : https://www.gov.scot/collections/small-area-statistics/

**DEFINITIONS**

- "Data Zones are the key geography for the dissemination of small area statistics in Scotland and are widely used across the public sector. Composed of groups of Census Output Areas, Data Zones are large enough that statistics can be presented accurately without fear of disclosure and yet small enough that they can be used to represent communities. They are designed to have roughly standard populations of 500 to 1,000 household residents, nest within local authorities (at the time of the Census), and have compact shapes that respect physical boundaries where possible." (Scottish Government metadata record)
- "Following the update to Data Zones using 2022 Census data, there are now 7,392 Data Zones covering the whole of Scotland." (Scottish Government metadata record)

**SCOPE**

- Scotland. 7,392 Data Zones. The Scottish counterpart of the Lower layer Super Output Area (LSOA); built from the Census 2022 Output Areas in uk_baseline.adm_nrs_oa_boundary_2022.
- The publisher ships one file; its extent coincides with the clipped to Mean High Water Output Area edition.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid), as shipped.

**LICENCE**

- Open Government Licence. Attribution: "Copyright Scottish Government, contains Ordnance Survey data (c) Crown copyright and database right (insert year)."

**DATA QUALITY CAVEATS**

- 1 of 7,392 polygons (S01019073) was published with a ring touching itself at a single vertex. Repaired on 2 September 2026 with the data manager's approval; it remains a single polygon with no change in area (0.00 sq m).
- The publisher gives no field-level definitions for the population, household and area columns; they are carried under their source names. "Note that the standard area measurements will differ from the automated Shape_Area attributes. This will be due to the different coastlines/inland water, and also can be due to the Output Areas policy to remove non-contiguous parts, which was applied after the standard areas were calculated." (Scottish Government metadata record)
- Key column is named `dzcode`, as published. It holds the Data Zone 2022 code, the Scottish equivalent of `lsoa21cd`; deliberately not renamed (data manager decision, 2 September 2026). Join on `dzcode`.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `dzcode` | `character varying` | Source field `DZCode`; Data Zone 2022 code (S01 prefix), the Scottish equivalent of `lsoa21cd`. Kept under the publisher name by data manager decision, 2 September 2026. |
| `dzname` | `character varying` | Source field `DZName`; Data Zone 2022 name. |
| `totpop2022` | `double precision` | Source field `TotPop2022`; [UNDOCUMENTED] carried as shipped. |
| `hhres2022` | `double precision` | Source field `HHRes2022`; [UNDOCUMENTED] carried as shipped. |
| `hhcnt2022` | `double precision` | Source field `HHCnt2022`; [UNDOCUMENTED] carried as shipped. |
| `stdareaha` | `double precision` | Source field `StdAreaHa`; [UNDOCUMENTED] publisher standard area, carried as shipped. |
| `stdareakm2` | `double precision` | Source field `StdAreaKM2`; [UNDOCUMENTED] publisher standard area, carried as shipped. |
| `st_area_sh` | `double precision` | Source field `st_area_sh`; [UNDOCUMENTED] ArcGIS shape area carried as shipped. |
| `st_length_` | `double precision` | Source field `st_length_`; [UNDOCUMENTED] ArcGIS shape length carried as shipped. |
| `geom` | `geometry(MultiPolygon,27700)` | Source shapefile geometry; MultiPolygon in EPSG:27700, as shipped. |
