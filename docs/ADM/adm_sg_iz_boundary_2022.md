# Scottish Government Intermediate Zones 2022, Scotland extent, clipped to Mean High Water, December 2024

<p class="layer-short">Intermediate Zone Boundary 2022</p>

`adm_sg_iz_boundary_2022`

**SOURCE**

- Scottish Government, Geographic Information Science and Analysis Team. File SG_IntermediateZoneBdry_2022_MHW.shp from SG_IntermediateZoneBdry_2022.zip, published 16 December 2024; the Extent of the Realm file in the same download was not loaded. All source fields copied as published; nothing derived, renamed or filtered.

**DOCUMENTATION**

- Metadata record (spatialdata.gov.scot) : https://spatialdata.gov.scot/geonetwork/srv/api/records/2978ed67-dade-42ec-b8e1-644e0b1f8cd8
- Small area statistics collection : https://www.gov.scot/collections/small-area-statistics/

**DEFINITIONS**

- "Intermediate Zones are a statistical geography that sit between Data Zones and local authorities, originally created for use with the Scottish Neighbourhood Statistics (SNS) programme (now known as statistics.gov.scot) and the wider public sector. Intermediate Zones are used for the dissemination of statistics that are not suitable for release at the Data Zone level because of the sensitive nature of the statistic, or for reasons of reliability. Intermediate Zones were designed to meet constraints on population thresholds (2,500 - 6,000 household residents), to nest within local authorities (at the time of the Census), and to be built up from aggregations of Data Zones." (Scottish Government metadata record)
- "Following the update to Intermediate Zones using 2022 Census data, there are now 1,334 Intermediate Zones covering the whole of Scotland." (Scottish Government metadata record)

**SCOPE**

- Scotland. 1,334 Intermediate Zones, clipped to Mean High Water edition. The Scottish counterpart of the Middle layer Super Output Area (MSOA); built from the Data Zones in uk_baseline.adm_sg_dz_boundary_2022.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid), as shipped.

**LICENCE**

- Open Government Licence. Attribution: "Copyright Scottish Government, contains Ordnance Survey data (c) Crown copyright and database right (insert year)."

**DATA QUALITY CAVEATS**

- The publisher gives no field-level definitions for the population, household and area columns; they are carried under their source names. "Note that the standard area measurements will differ from the automated Shape_Area attributes. This will be due to the different coastlines/inland water, and also can be due to the Output Areas policy to remove non-contiguous parts, which was applied after the standard areas were calculated." (Scottish Government metadata record)
- Key column is named `izcode`, as published. It holds the Intermediate Zone 2022 code, the Scottish equivalent of `msoa21cd`; deliberately not renamed (data manager decision, 2 September 2026). Join on `izcode`.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `izcode` | `character varying` | Source field `IZCode`; Intermediate Zone 2022 code (S02 prefix), the Scottish equivalent of `msoa21cd`. Kept under the publisher name by data manager decision, 2 September 2026. |
| `izname` | `character varying` | Source field `IZName`; Intermediate Zone 2022 name. |
| `totpop2022` | `double precision` | Source field `TotPop2022`; [UNDOCUMENTED] carried as shipped. |
| `hhres2022` | `double precision` | Source field `HHRes2022`; [UNDOCUMENTED] carried as shipped. |
| `hhcnt2022` | `double precision` | Source field `HHCnt2022`; [UNDOCUMENTED] carried as shipped. |
| `stdareaha` | `double precision` | Source field `StdAreaHa`; [UNDOCUMENTED] publisher standard area, carried as shipped. |
| `stdareakm2` | `double precision` | Source field `StdAreaKM2`; [UNDOCUMENTED] publisher standard area, carried as shipped. |
| `shape_leng` | `double precision` | Source field `Shape_Leng`; [UNDOCUMENTED] ArcGIS perimeter length carried as shipped. |
| `shape_area` | `double precision` | Source field `Shape_Area`; "Area of feature in internal units squared." (Scottish Government shapefile metadata). |
| `geom` | `geometry(MultiPolygon,27700)` | Source shapefile geometry; MultiPolygon in EPSG:27700, clipped to Mean High Water, as shipped. |
