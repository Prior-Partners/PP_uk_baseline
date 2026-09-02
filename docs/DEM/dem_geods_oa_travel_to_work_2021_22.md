# Geographic Data Service (GeoDS) Unified UK Census 2021/2022, Method of travel to workplace, United Kingdom small-area extent, March 2026

<p class="layer-short">Census 2021/22 Method of travel to workplace (UK)</p>

`dem_geods_oa_travel_to_work_2021_22`

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK. Unified UK Census Data (2021/2), topic table uk061 from variable_tables_csv.zip (published 19 February 2026, last modified 3 March 2026). Harmonised by GeoDS from Office for National Statistics (ONS), National Records of Scotland (NRS) and Northern Ireland Statistics and Research Agency (NISRA) census outputs. All 11 source columns copied as published; nothing derived or filtered. Columns carry readable names from the GeoDS labels (see SCOPE); the GeoDS identifier is recorded in every column comment.

**DOCUMENTATION**

- Dataset page : https://data.geods.ac.uk/dataset/unified-uk-census-data
- Method paper (Goodwin and Singleton) : https://doi.org/10.1177/23998083261429563
- Source code : https://github.com/GeographicDataService/unified-uk-census-2021-22
- Variable Metadata and Table Notes files : shipped with the download; local copy on the P: source folder 260902_GeoDS_Unified UK Census 2021-22.

**DEFINITIONS**

- "The Unified UK Census Dataset (2021/2022) is a harmonised, small-area dataset that brings together census data from the three UK census agencies -- ONS (England & Wales), NRS (Scotland), and NISRA (Northern Ireland) -- into a single, comparable release." (GeoDS dataset page)
- "The dataset available for download contains the counts for all 190 variables plus 25 table totals (215 variables in total) across each of the 239,023 small-area geographies. Data Zones are relabelled as "OA" in the dataset for consistency." (GeoDS dataset page)
- Table unit: "Person". Population scope: "Persons Aged 16 or over and in full time employment the week before the census. Scotland: Persons Aged 16 or over and in full time employment the week before the census (including full-time students if they gave a work address as the address they primarily travel to for work or study)". (GeoDS Table Notes)
- Census Day: "21 March 2021 for England, Wales, and Northern Ireland, and 20 March 2022 for Scotland." (GeoDS dataset page)

**SCOPE**

- United Kingdom. 239,023 rows, one per small area: England 178,605; Wales 10,275; Scotland 46,363; Northern Ireland 3,780. Codes are Output Area 2021 (E00, W00), Output Area 2022 (S00) and Data Zone 2021 (N20).
- Counts only; `total` (GeoDS uk061001) is the table total. No percentages are supplied by the publisher and none were computed.
- Column names are readable forms of the GeoDS labels, signed off by the data manager on 2 September 2026; each column comment names the GeoDS source identifier. Mapping: scripts/unified_census/column_names.py.
- Sibling of the other 24 GeoDS Unified UK Census tables named dem_geods_oa_*_2021_22.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code.

**LICENCE**

- Open Government Licence v3.0. Attribution: "The data for this research have been provided by the Geographic Data Service (geods.ac.uk), a Smart Data Research UK Investment: ES/Z504464/1. These were created as part of an ESRC Census data opportunity grant - ES/Z50273X/1. Contains data from: ONS, NRS, NISRA"

**DATA QUALITY CAVEATS**

- "The Scottish census was conducted one year later than the rest of the UK (2022 vs 2021), which may introduce temporal differences in some variables." (GeoDS dataset page)
- "The data are compiled from the official census releases of the three UK statistical agencies, each of which applies its own disclosure control and data quality procedures." (GeoDS dataset page)
- Harmonisation notes for this table (GeoDS Table Notes, verbatim): "1. Changes in working patterns due to the COVID-19 pandemic severely impact this variable 2. The Northern Ireland table does not contain the variable "Method of travel to workplace: Underground, metro, light rail, tram", as this form of transport is not available in Northern Ireland. The counts for this variable in the unified table are therefore set to zero for all Northern Ireland Data Zones. 3. An aggregated "Car or Van" variable is created for the unified tables, as the subdivisions of this variable differ for Northern Ireland to the rest of the censuses. 4. The variables for Scotland include those who travel for study as well as work."
- "The COVID-19 pandemic severely impacted method of travel to workplace data across all nations." (GeoDS dataset page)
- Northern Ireland geometry was reprojected from Irish Grid with about 3 m accuracy; see uk_baseline.adm_nisra_dz_boundary_2021.
- 9 Scottish polygons (S00136407, S00136544, S00138851, S00142130, S00148144, S00162192, S00176070, S00177785, S00181661) were published with a ring touching itself at one vertex and were repaired on 2 September 2026 with the data manager's approval; no change in area.
- Geography columns are NULL on 50,143 of 239,023 rows: every Scotland and Northern Ireland row. sds_name and sds_group are also NULL on all 10,275 Wales rows and on 9 England rows (Isles of Scilly pattern), as on the backbone.

**ENRICHMENT**

- Route attr_join on `oa`, applied 2 September 2026 through the uk_new staging schema. England and Wales rows carry Output Area 2021 codes, which nest wholly within LSOA 2021 and MSOA 2021, so the join is exact rather than best-fit; all eleven geography columns were copied from uk_baseline.adm_ons_oa_boundaries_dec2021 (itself enriched 5 August 2026: MSOA 2021 via the ONS 2021 output-area hierarchy, Local Authority District 2022 and 2025, county or unitary authority 2025 and Spatial Development Strategy via uk.ref_lad25_ctyua25_sds_lu_jul2026). Row count unchanged at 239,023. No numeric value was changed, recomputed or apportioned.
- Scotland (Output Area 2022) and Northern Ireland (Data Zone 2021) rows, 50,143 in all, have no MSOA, Local Authority District 2025, county or Spatial Development Strategy in this scheme and are NULL in all eleven columns. Wales carries a county but no SDS.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `oa` | `character varying(9)` | Source field `OA`; small-area code: "OA21CD (England/Wales), OA22CD (Scotland), DZ21CD (Northern Ireland)" (GeoDS). Northern Ireland Data Zones are labelled OA by the publisher. |
| `total` | `integer` | Source field `uk061001`; "Method of travel to workplace: Total: All usual residents aged 16 years and over in employment the week before the census". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `work_from_home` | `integer` | Source field `uk061002`; "Method of travel to workplace: Work mainly at or from home". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `underground_metro_light_rail_tram` | `integer` | Source field `uk061003`; "Method of travel to workplace: Underground, metro, light rail, tram". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `train` | `integer` | Source field `uk061004`; "Method of travel to workplace: Train". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `bus_minibus_or_coach` | `integer` | Source field `uk061005`; "Method of travel to workplace: Bus, minibus or coach". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `taxi` | `integer` | Source field `uk061006`; "Method of travel to workplace: Taxi". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `motorcycle_scooter_or_moped` | `integer` | Source field `uk061007`; "Method of travel to workplace: Motorcycle, scooter or moped". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `car_or_van` | `integer` | Source field `uk061008`; "Method of travel to workplace: Car or van". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `bicycle` | `integer` | Source field `uk061009`; "Method of travel to workplace: Bicycle". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `on_foot` | `integer` | Source field `uk061010`; "Method of travel to workplace: On foot". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `other_method` | `integer` | Source field `uk061011`; "Method of travel to workplace: Other method of travel to work". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code. |
| `msoa21cd` | `character varying(9)` | Middle Layer Super Output Area (MSOA) 2021 code of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `msoa21nm` | `text` | Official Office for National Statistics MSOA 2021 name of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021, which carries the House of Commons Library name. Open Parliament Licence. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `lad22cd` | `character varying(9)` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit assigned from the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit assigned from the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `lad25cd` | `character varying(9)` | Local Authority District 2025 code (current administering authority), best-fit assigned from the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit assigned from the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `ctyua25cd` | `character varying(9)` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. Copied at load from uk_baseline.adm_ons_oa_boundaries_dec2021 on `oa` (Output Area 2021 code); NULL for every Scotland and Northern Ireland row. |
