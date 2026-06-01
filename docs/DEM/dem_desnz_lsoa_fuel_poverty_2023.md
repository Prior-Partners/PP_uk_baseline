# Department for Energy Security and Net Zero (DESNZ) sub-regional fuel poverty estimates at LSOA (England), 2023

`dem_desnz_lsoa_fuel_poverty_2023`

**SOURCE**

- Department for Energy Security and Net Zero (DESNZ), formerly the Department for Business, Energy & Industrial Strategy (BEIS); department split April 2023.
- Modelled from the English Housing Survey (EHS) and aggregated to LSOA21 grain.

**DOCUMENTATION**

- Statistical release : https://www.gov.uk/government/statistics/sub-regional-fuel-poverty-2023-2021-data
- Methodology : https://www.gov.uk/government/publications/fuel-poverty-sub-regional-methodology-and-documentation/sub-regional-fuel-poverty-statistics-methodology
- data.gov.uk catalog : https://www.data.gov.uk/dataset/f3009590-2bc9-40d9-8dc3-571e6fddae45/fuel-poverty-in-england-sub-regional

**DEFINITIONS**

- "An interactive map for indicators of domestic energy efficiency and energy consumption is available which includes the percentage of households in fuel poverty down to Lower Layer Super Output Area." (DESNZ sub-regional release)
- LILEE definition (Low Income Low Energy Efficiency - the fuel-poverty measure used since 2021): a household is fuel-poor if it lives in a property rated EPC band D or below AND its disposable income after housing and fuel costs falls below the official poverty line.

**SCOPE**

- England only (DESNZ does not publish sub-regional fuel-poverty estimates for Scotland, Wales, or Northern Ireland - separate devolved publications).
- 33,890 rows at LSOA 2021 grain.

**CRS**

- EPSG:27700 (British National Grid / BNG). Geometry joined at load from the LSOA21 boundary set.

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- "Estimates of fuel poverty at Lower Super Output Area (LSOA) should be treated with caution and should only be used to look at general trends and identify areas of particularly high or low fuel poverty, not to identify trends over time within an LSOA or to compare LSOAs with similar fuel poverty levels due to very small sample sizes and consequent instability in estimates at this level." (DESNZ sub-regional methodology)

**ENRICHMENT**

- msoa21cd, msoa21nm : joined from ONS LSOA -> MSOA lookup.
- lad22cd, lad22nm : joined from ONS LSOA -> LAD lookup.
- msoa11cd, msoa11nm : joined from ONS LSOA -> 2011 MSOA lookup (kept for legacy cross-walks; DESNZ historically published at MSOA 2011 grain).
- wd21cd, wd21nm : joined from ONS LSOA -> Ward lookup.
- geom, area_ha : geometry from LSOA21 boundary; area_ha derived from geom at load.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `bigint` |  |
| `lsoa21cd` | `text` | Source field "LSOA21CD"; ONS GSS 9-character LSOA code (e.g. "E01000001"). |
| `lsoa21nm` | `text` | Source field "LSOA21NM"; human-readable LSOA name. |
| `msoa21cd` | `text` | Joined at load from ONS LSOA->MSOA lookup; 2021 MSOA GSS code. |
| `msoa21nm` | `text` | Joined at load from ONS LSOA->MSOA lookup; 2021 MSOA name. |
| `lad22cd` | `text` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD GSS code. |
| `lad22nm` | `text` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD name. |
| `msoa11cd` | `text` | Joined at load from ONS LSOA->MSOA2011 lookup; legacy 2011 MSOA code (kept for cross-walking to older DESNZ publications). |
| `msoa11nm` | `text` | Joined at load from ONS LSOA->MSOA2011 lookup; 2011 MSOA name. |
| `wd21cd` | `text` | Joined at load from ONS LSOA->Ward lookup; 2021 Ward GSS code. |
| `wd21nm` | `text` | Joined at load from ONS LSOA->Ward lookup; 2021 Ward name. |
| `region` | `text` | Source field "Region"; ONS region name (English regions). |
| `total_households` | `double precision` | Source field; total number of households in the LSOA. |
| `fuel_poor_households_count` | `double precision` | Source field; modelled count of households in fuel poverty (LILEE measure). |
| `fuel_poor_households_perc` | `double precision` | Source field; modelled share of households in fuel poverty. Unit: "per cent (0-100)". |
| `geom` | `geometry(MultiPolygon,27700)` | Joined at load from LSOA21 boundary set; MultiPolygon in EPSG:27700. |
| `fid` | `bigint` |  |
| `area_ha` | `double precision` | Derived at load from ST_Area(geom)/10000. Unit: "hectares". |
