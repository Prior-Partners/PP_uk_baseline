# National Records of Scotland (NRS) Census 2022 Output Areas (OA), Scotland extent, clipped to Mean High Water, May 2024

<p class="layer-short">Output Area Boundary 2022 (Scotland)</p>

`adm_nrs_oa_boundary_2022`

**SOURCE**

- National Records of Scotland (NRS), 2022 Census geography products. File OutputArea2022_MHW.shp from output-area-2022-mhw.zip, published 21 May 2024. All source fields copied as published; nothing derived, renamed or filtered.

**DOCUMENTATION**

- 2022 Census geography products : https://www.nrscotland.gov.uk/publications/2022-census-geography-products
- Metadata record (spatialdata.gov.scot) : https://spatialdata.gov.scot/geonetwork/srv/api/records/a0a643ba-c0ed-4860-93a9-5fee11ac492a
- File specification : Census2022_SpatialDatasetsFileSpecification.pdf, shipped inside the download.

**DEFINITIONS**

- "Output Areas (OAs) are the key geography for dissemination of small area statistics from the Census. OAs are large enough for Census statistics to be released without infringing confidentiality. They are designed to have relatively small numbers of households (in the range of 25 to 89) and population (>=60), while nesting within Council areas. They also act as the basic 'building-blocks' for the creation of other geographies such as Data Zones. There are 46,363 Census 2022 OAs in Scotland." (NRS metadata record)
- "Output Areas created by aggregating frozen postcodes." (NRS file specification)
- "The boundaries are available at Extent of the Realm and clipped to the Mean High Water (MHW) Mark with inland water removed." (NRS file specification)

**SCOPE**

- Scotland. 46,363 Output Areas, the clipped to Mean High Water edition with inland water removed.
- Companion to uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland); together the three give small-area geometry for the whole United Kingdom at the Census 2021/2022 level.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid), as shipped.

**LICENCE**

- Open Government Licence v3.0. Attribution: "Copyright National Records of Scotland, contains Ordnance Survey data (c) Crown copyright and database right (insert year)."

**DATA QUALITY CAVEATS**

- 9 of 46,363 polygons were published with a ring touching itself at a single vertex (S00136407, S00136544, S00138851, S00142130, S00148144, S00162192, S00176070, S00177785, S00181661). Repaired on 2 September 2026 with the data manager's approval; each remains a single polygon with no change in area (0.00 sq m).
- hhcount and popcount carry cell key perturbation: "Cell Key Perturbation has been applied to Scotland's Census 2022 outputs. This means that small adjustments are made automatically to cells in tables, including the Postcode to Output Area lookup." (NRS file specification)
- sqkm and hect are the publisher's areas for the whole Output Area including parts removed from this shapefile, so they will not always agree with an area measured from the geometry.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `code` | `character varying` | Source field `code`; "A code that identifies a Census 2022 Output Area (OA)." (NRS file specification). Matches the S-prefixed keys of the GeoDS Unified UK Census 2021/22 tables. |
| `hhcount` | `bigint` | Source field `HHcount`; Unit: "2022 Census occupied household count at OA level." Cell key perturbation applied by the publisher. |
| `popcount` | `bigint` | Source field `Popcount`; Unit: "2022 Census household population count at OA level." Cell key perturbation applied by the publisher. |
| `council` | `character varying` | Source field `council`; "A code that identifies a 2019 Council Area." |
| `sqkm` | `double precision` | Source field `sqkm`; Unit: "Area of Output Area in square kilometres." Publisher figure for the whole Output Area including parts removed from the shapefile. |
| `hect` | `double precision` | Source field `hect`; Unit: "Area of Output Area in hectares." Publisher figure for the whole Output Area including parts removed from the shapefile. |
| `masterpc` | `character varying` | Source field `masterpc`; "Postcode assigned as the Master Postcode for Output Area." |
| `easting` | `character varying` | Source field `easting`; "Easting of Master Postcode grid reference measured to 1 meter on the British National Grid." Stored as text, as shipped. |
| `northing` | `character varying` | Source field `northing`; "Northing of Master Postcode grid reference measured to 1 meter on the British National Grid." Stored as text, as shipped. |
| `shape_leng` | `double precision` | Source field `Shape_Leng`; [UNDOCUMENTED] ArcGIS perimeter length carried as shipped. |
| `shape_area` | `double precision` | Source field `Shape_Area`; "Area of feature in internal units squared." (NRS shapefile metadata). |
| `geom` | `geometry(MultiPolygon,27700)` | Source shapefile geometry; MultiPolygon in EPSG:27700, clipped to Mean High Water with inland water removed, as shipped. |
