# Geographic Data Service (GeoDS) Unified UK Census 2021/2022, National Statistics Socio-economic Classification (NS-SEC), United Kingdom small-area extent, March 2026

<p class="layer-short">Census 2021/22 National Statistics Socio-economic Classification (NS-SEC) (UK)</p>

`dem_geods_oa_ns_sec_2021_22`

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK. Unified UK Census Data (2021/2), topic table uk062 from variable_tables_csv.zip (published 19 February 2026, last modified 3 March 2026). Harmonised by GeoDS from Office for National Statistics (ONS), National Records of Scotland (NRS) and Northern Ireland Statistics and Research Agency (NISRA) census outputs. All 10 source columns copied as published under their source variable identifiers; nothing derived, renamed or filtered.

**DOCUMENTATION**

- Dataset page : https://data.geods.ac.uk/dataset/unified-uk-census-data
- Method paper (Goodwin and Singleton) : https://doi.org/10.1177/23998083261429563
- Source code : https://github.com/GeographicDataService/unified-uk-census-2021-22
- Variable Metadata and Table Notes files : shipped with the download; local copy on the P: source folder 260902_GeoDS_Unified UK Census 2021-22.

**DEFINITIONS**

- "The Unified UK Census Dataset (2021/2022) is a harmonised, small-area dataset that brings together census data from the three UK census agencies -- ONS (England & Wales), NRS (Scotland), and NISRA (Northern Ireland) -- into a single, comparable release." (GeoDS dataset page)
- "The dataset available for download contains the counts for all 190 variables plus 25 table totals (215 variables in total) across each of the 239,023 small-area geographies. Data Zones are relabelled as "OA" in the dataset for consistency." (GeoDS dataset page)
- Table unit: "Person". Population scope: "Persons Aged 16 or over.". (GeoDS Table Notes)
- Census Day: "21 March 2021 for England, Wales, and Northern Ireland, and 20 March 2022 for Scotland." (GeoDS dataset page)

**SCOPE**

- United Kingdom. 239,023 rows, one per small area: England 178,605; Wales 10,275; Scotland 46,363; Northern Ireland 3,780. Codes are Output Area 2021 (E00, W00), Output Area 2022 (S00) and Data Zone 2021 (N20).
- Counts only; uk062001 is the table total. No percentages are supplied by the publisher and none were computed.
- Sibling of the other 24 GeoDS Unified UK Census tables named dem_geods_oa_*_2021_22.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code.

**LICENCE**

- Open Government Licence v3.0. Attribution: "The data for this research have been provided by the Geographic Data Service (geods.ac.uk), a Smart Data Research UK Investment: ES/Z504464/1. These were created as part of an ESRC Census data opportunity grant - ES/Z50273X/1. Contains data from: ONS, NRS, NISRA"

**DATA QUALITY CAVEATS**

- "The Scottish census was conducted one year later than the rest of the UK (2022 vs 2021), which may introduce temporal differences in some variables." (GeoDS dataset page)
- "The data are compiled from the official census releases of the three UK statistical agencies, each of which applies its own disclosure control and data quality procedures." (GeoDS dataset page)
- Harmonisation notes for this table (GeoDS Table Notes, verbatim): "1. The England table aggregates the categories (L1-L3, L3-6, L8-9, L10-11, L14.1-L14.2), this aggregation is used in the unified tables."
- Northern Ireland geometry was reprojected from Irish Grid with about 3 m accuracy; see uk_baseline.adm_nisra_dz_boundary_2021.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `oa` | `character varying(9)` | Source field `OA`; small-area code: "OA21CD (England/Wales), OA22CD (Scotland), DZ21CD (Northern Ireland)" (GeoDS). Northern Ireland Data Zones are labelled OA by the publisher. |
| `uk062001` | `integer` | Source field `uk062001`; "National Statistics Socio-economic Classification (NS-SEC): Total: All usual residents aged 16 years and over". Unit: "Person". |
| `uk062002` | `integer` | Source field `uk062002`; "National Statistics Socio-economic Classification (NS-SEC): L1, L2 and L3 Higher managerial, administrative and professional occupations". Unit: "Person". |
| `uk062003` | `integer` | Source field `uk062003`; "National Statistics Socio-economic Classification (NS-SEC): L4, L5 and L6 Lower managerial, administrative and professional occupations". Unit: "Person". |
| `uk062004` | `integer` | Source field `uk062004`; "National Statistics Socio-economic Classification (NS-SEC): L7 Intermediate occupations". Unit: "Person". |
| `uk062005` | `integer` | Source field `uk062005`; "National Statistics Socio-economic Classification (NS-SEC): L8 and L9 Small employers and own account workers". Unit: "Person". |
| `uk062006` | `integer` | Source field `uk062006`; "National Statistics Socio-economic Classification (NS-SEC): L10 and L11 Lower supervisory and technical occupations". Unit: "Person". |
| `uk062007` | `integer` | Source field `uk062007`; "National Statistics Socio-economic Classification (NS-SEC): L12 Semi-routine occupations". Unit: "Person". |
| `uk062008` | `integer` | Source field `uk062008`; "National Statistics Socio-economic Classification (NS-SEC): L13 Routine occupations". Unit: "Person". |
| `uk062009` | `integer` | Source field `uk062009`; "National Statistics Socio-economic Classification (NS-SEC): L14.1 and L14.2 Never worked and long-term unemployed". Unit: "Person". |
| `uk062010` | `integer` | Source field `uk062010`; "National Statistics Socio-economic Classification (NS-SEC): L15 Full-time students". Unit: "Person". |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code. |
