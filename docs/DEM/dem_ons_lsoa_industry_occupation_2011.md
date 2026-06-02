# ONS Census 2011 industry of employment at Lower-layer Super Output Area (LSOA) 2011

`dem_ons_lsoa_industry_occupation_2011`

<a href="http://localhost:7800/?layer=uk_baseline.dem_ons_lsoa_industry_occupation_2011" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Office for National Statistics (ONS), Census 2011, England and Wales. Source: table QS605EW "Industry by sex" (or KS605EW summary). Reference date 27 March 2011. Loaded via an earlier Prior + Partners pass.

**DOCUMENTATION**

- NOMIS Census 2011 QS605EW : https://www.nomisweb.co.uk/census/2011/qs605ew
- ONS Census 2011 landing page : https://www.ons.gov.uk/census/2011census
- SIC 2007 classification : https://onsdigital.github.io/dp-classification-tools/standard-industrial-classification/ONS_SIC_hierarchy_view.html

**DEFINITIONS**

- "This information is used to assign a code to the industry an individual works in using the UK Standard Industrial Classification of Economic Activities (UKSIC)." (NOMIS Census 2011 QS605EW)
- Base population: usual residents aged 16-74 in employment in the week before Census Day (27 March 2011).

**SCOPE**

- England and Wales. LSOA 2011 boundary; 34,753 distinct lsoa11cd.
- Base population: usual residents aged 16-74 in employment.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- This is Census 2011 data — superseded by Census 2021 (`dem_ons_lsoa_industry_occupation_2021`). Use the 2021 layer for current analysis; this layer for historic comparison only.
- LSOA 2011 boundary; NOT directly comparable cell-by-cell to LSOA 2021 (boundaries changed in ~10% of areas). Use ONS LSOA11->LSOA21 best-fit lookup for cross-year comparison.

**LOADED INTO uk_baseline**

- Data: Census Day 27 March 2011.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `lsoa11cd` | `character varying` | Source field "LSOA11CD"; ONS GSS 9-character LSOA 2011 code. |
| `population` | `integer` | Source field; total population in the LSOA at Census 2011. |
| `total_households` | `integer` | Source field; total households in the LSOA at Census 2011. |
| `total_hhold_size_pop` | `integer` | Source field; population base used for household-size calculations. |
| `msoa21cd` | `character varying` | Joined at load from ONS LSOA->MSOA lookup; 2021 MSOA GSS code. |
| `msoa21nm` | `character varying` | Joined at load from ONS LSOA->MSOA lookup; 2021 MSOA name. |
| `male_pop` | `double precision` | Source field; male population in the LSOA at Census 2011. |
| `female_pop` | `double precision` | Source field; female population in the LSOA at Census 2011. |
| `wd21cd` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2021 Ward GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2021 Ward name. |
| `lsoa21cd` | `character varying` | Source field "LSOA21CD"; ONS GSS 9-character LSOA 2021 code. |
| `lsoa21nm` | `character varying` | Source field "LSOA21NM"; human-readable LSOA 2021 name. |
| `lad22cd` | `character varying` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD GSS code. |
| `lad22nm` | `character varying` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD name. |
| `lsoa11nm` | `character varying` | Source field "LSOA11NM"; human-readable LSOA 2011 name. |
| `agriculture_forestry_fishing_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Agriculture, forestry and fishing" (SIC 2007). Stored as text in this table. |
| `mining_quarrying_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Mining and quarrying" (SIC 2007). Stored as text in this table. |
| `manufacturing_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Manufacturing" (SIC 2007). Stored as text in this table. |
| `electricity_gas_steam_aircon_supply_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Electricity, gas, steam and air conditioning supply" (SIC 2007). Stored as text in this table. |
| `water_waste_sewerage_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Water supply, sewerage and waste management" (SIC 2007). Stored as text in this table. |
| `construction_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Construction" (SIC 2007). Stored as text in this table. |
| `wholesale_retail_motor_repair_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Wholesale and retail trade, repair of motor vehicles and motorcycles" (SIC 2007). Stored as text in this table. |
| `transport_storage_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Transport and storage" (SIC 2007). Stored as text in this table. |
| `accommodation_food_service_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Accommodation and food service activities" (SIC 2007). Stored as text in this table. |
| `information_communication_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Information and communication" (SIC 2007). Stored as text in this table. |
| `financial_insurance_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Financial and insurance activities" (SIC 2007). Stored as text in this table. |
| `real_estate_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Real estate activities" (SIC 2007). Stored as text in this table. |
| `professional_scientific_technical_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Professional, scientific and technical activities" (SIC 2007). Stored as text in this table. |
| `admin_support_service_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Administrative and support service activities" (SIC 2007). Stored as text in this table. |
| `public_admin_defence_social_security_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Public administration and defence, compulsory social security" (SIC 2007). Stored as text in this table. |
| `education_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Education" (SIC 2007). Stored as text in this table. |
| `health_social_work_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Human health and social work activities" (SIC 2007). Stored as text in this table. |
| `arts_entertainment_recreation_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Arts, entertainment and recreation" (SIC 2007). Stored as text in this table. |
| `other_service_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Other service activities" (SIC 2007). Stored as text in this table. |
| `activities_of_household_employers_goods_services_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use" (SIC 2007). Stored as text in this table. |
| `extraterritorial_orgs_count` | `character varying` | Source field; count of usual residents aged 16-74 in employment classified as "Activities of extraterritorial organisations and bodies" (SIC 2007). Stored as text in this table. |
| `total_employment` | `character varying` | Source field; total persons in employment in the LSOA at Census 2011 (denominator for the _perc columns). |
| `agriculture_forestry_fishing_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Agriculture, forestry and fishing". Unit: "percent (0 to 100)". Stored as text in this table. |
| `mining_quarrying_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Mining and quarrying". Unit: "percent (0 to 100)". Stored as text in this table. |
| `manufacturing_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Manufacturing". Unit: "percent (0 to 100)". Stored as text in this table. |
| `electricity_gas_steam_aircon_supply_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Electricity, gas, steam and air conditioning supply". Unit: "percent (0 to 100)". Stored as text in this table. |
| `water_waste_sewerage_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Water supply, sewerage and waste management". Unit: "percent (0 to 100)". Stored as text in this table. |
| `construction_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Construction". Unit: "percent (0 to 100)". Stored as text in this table. |
| `wholesale_retail_motor_repair_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Wholesale and retail trade, repair of motor vehicles and motorcycles". Unit: "percent (0 to 100)". Stored as text in this table. |
| `transport_storage_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Transport and storage". Unit: "percent (0 to 100)". Stored as text in this table. |
| `accommodation_food_service_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Accommodation and food service activities". Unit: "percent (0 to 100)". Stored as text in this table. |
| `information_communication_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Information and communication". Unit: "percent (0 to 100)". Stored as text in this table. |
| `financial_insurance_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Financial and insurance activities". Unit: "percent (0 to 100)". Stored as text in this table. |
| `real_estate_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Real estate activities". Unit: "percent (0 to 100)". Stored as text in this table. |
| `professional_scientific_technical_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Professional, scientific and technical activities". Unit: "percent (0 to 100)". Stored as text in this table. |
| `admin_support_service_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Administrative and support service activities". Unit: "percent (0 to 100)". Stored as text in this table. |
| `public_admin_defence_social_security_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Public administration and defence, compulsory social security". Unit: "percent (0 to 100)". Stored as text in this table. |
| `education_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Education". Unit: "percent (0 to 100)". Stored as text in this table. |
| `health_social_work_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Human health and social work activities". Unit: "percent (0 to 100)". Stored as text in this table. |
| `arts_entertainment_recreation_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Arts, entertainment and recreation". Unit: "percent (0 to 100)". Stored as text in this table. |
| `other_service_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Other service activities". Unit: "percent (0 to 100)". Stored as text in this table. |
| `activities_of_household_employers_goods_services_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use". Unit: "percent (0 to 100)". Stored as text in this table. |
| `extraterritorial_orgs_perc` | `character varying` | Source field; percentage of usual residents aged 16-74 in employment classified as "Activities of extraterritorial organisations and bodies". Unit: "percent (0 to 100)". Stored as text in this table. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Boundary geometry joined at load. |
| `fid` | `bigint` |  |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Unit: hectares. Stale if geometry is later edited. |
