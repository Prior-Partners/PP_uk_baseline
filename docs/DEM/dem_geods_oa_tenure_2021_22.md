# Geographic Data Service (GeoDS) Unified UK Census 2021/2022, Tenure of household, United Kingdom small-area extent, March 2026

<p class="layer-short">Census 2021/22 Tenure of household (UK)</p>

`dem_geods_oa_tenure_2021_22`

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK. Unified UK Census Data (2021/2), topic table uk054 from variable_tables_csv.zip (published 19 February 2026, last modified 3 March 2026). Harmonised by GeoDS from Office for National Statistics (ONS), National Records of Scotland (NRS) and Northern Ireland Statistics and Research Agency (NISRA) census outputs. All 9 source columns copied as published under their source variable identifiers; nothing derived, renamed or filtered.

**DOCUMENTATION**

- Dataset page : https://data.geods.ac.uk/dataset/unified-uk-census-data
- Method paper (Goodwin and Singleton) : https://doi.org/10.1177/23998083261429563
- Source code : https://github.com/GeographicDataService/unified-uk-census-2021-22
- Variable Metadata and Table Notes files : shipped with the download; local copy on the P: source folder 260902_GeoDS_Unified UK Census 2021-22.

**DEFINITIONS**

- "The Unified UK Census Dataset (2021/2022) is a harmonised, small-area dataset that brings together census data from the three UK census agencies -- ONS (England & Wales), NRS (Scotland), and NISRA (Northern Ireland) -- into a single, comparable release." (GeoDS dataset page)
- "The dataset available for download contains the counts for all 190 variables plus 25 table totals (215 variables in total) across each of the 239,023 small-area geographies. Data Zones are relabelled as "OA" in the dataset for consistency." (GeoDS dataset page)
- Table unit: "Household". Population scope: "All Households". (GeoDS Table Notes)
- Census Day: "21 March 2021 for England, Wales, and Northern Ireland, and 20 March 2022 for Scotland." (GeoDS dataset page)

**SCOPE**

- United Kingdom. 239,023 rows, one per small area: England 178,605; Wales 10,275; Scotland 46,363; Northern Ireland 3,780. Codes are Output Area 2021 (E00, W00), Output Area 2022 (S00) and Data Zone 2021 (N20).
- Counts only; uk054001 is the table total. No percentages are supplied by the publisher and none were computed.
- Sibling of the other 24 GeoDS Unified UK Census tables named dem_geods_oa_*_2021_22.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code.

**LICENCE**

- Open Government Licence v3.0. Attribution: "The data for this research have been provided by the Geographic Data Service (geods.ac.uk), a Smart Data Research UK Investment: ES/Z504464/1. These were created as part of an ESRC Census data opportunity grant - ES/Z50273X/1. Contains data from: ONS, NRS, NISRA"

**DATA QUALITY CAVEATS**

- "The Scottish census was conducted one year later than the rest of the UK (2022 vs 2021), which may introduce temporal differences in some variables." (GeoDS dataset page)
- "The data are compiled from the official census releases of the three UK statistical agencies, each of which applies its own disclosure control and data quality procedures." (GeoDS dataset page)
- Harmonisation notes for this table (GeoDS Table Notes, verbatim): "1. The full table is not available for Northern Ireland due to disclosure controls, in particular, separate variables for  "Owned: Owns with a mortgage or loan" and "Shared ownership" are not available. To create a unified table these variables are aggregated together for England and Scotland into a single variable  "Owned: Owns with a mortgage, loan or shared ownership"."
- Northern Ireland geometry was reprojected from Irish Grid with about 3 m accuracy; see uk_baseline.adm_nisra_dz_boundary_2021.
- 9 Scottish polygons (S00136407, S00136544, S00138851, S00142130, S00148144, S00162192, S00176070, S00177785, S00181661) were published with a ring touching itself at one vertex and were repaired on 2 September 2026 with the data manager's approval; no change in area.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `oa` | `character varying(9)` | Source field `OA`; small-area code: "OA21CD (England/Wales), OA22CD (Scotland), DZ21CD (Northern Ireland)" (GeoDS). Northern Ireland Data Zones are labelled OA by the publisher. |
| `uk054001` | `integer` | Source field `uk054001`; "Tenure of household: Total: All households". Unit: "Household". |
| `uk054002` | `integer` | Source field `uk054002`; "Tenure of household: Owned (Including Shared Ownership)". Unit: "Household". |
| `uk054003` | `integer` | Source field `uk054003`; "Tenure of household: Owned: Owns outright". Unit: "Household". |
| `uk054004` | `integer` | Source field `uk054004`; "Tenure of household: Owned: Owns with a mortgage, loan or shared ownership". Unit: "Household". |
| `uk054005` | `integer` | Source field `uk054005`; "Tenure of household: Social rented". Unit: "Household". |
| `uk054006` | `integer` | Source field `uk054006`; "Tenure of household: Private rented". Unit: "Household". |
| `uk054007` | `integer` | Source field `uk054007`; "Tenure of household: Private rented: Private landlord or letting agency". Unit: "Household". |
| `uk054008` | `integer` | Source field `uk054008`; "Tenure of household: Private rented: Other private rented". Unit: "Household". |
| `uk054009` | `integer` | Source field `uk054009`; "Tenure of household: Lives rent free". Unit: "Household". |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code. |
