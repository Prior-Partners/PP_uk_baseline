# ONS Housing Affordability Ratio at Local Authority District (LAD), 2025

`ecn_ons_housing_affordability_ratio_2025`

<iframe src="../maps/ecn_ons_housing_affordability_ratio_2025.html" title="Interactive preview map of ecn_ons_housing_affordability_ratio_2025" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/ecn_ons_housing_affordability_ratio_2025.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Office for National Statistics (ONS), "Housing affordability in England and Wales" bulletin 2025 release.

**DOCUMENTATION**

- ONS bulletin : https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingaffordabilityinenglandandwales/2025
- ONS dataset : https://www.ons.gov.uk/peoplepopulationandcommunity/housing/datasets/ratioofhousepricetoworkplacebasedearningslowerquartileandmedian

**DEFINITIONS**

- "Dividing house prices by annual earnings to create a ratio that enables comparisons across time and between areas. A higher number indicates less affordable housing." (ONS Housing affordability in England and Wales 2025 bulletin)
- "Ratios compare median house prices from a 12-month period ending in September against median annual earnings from mid-April of the same year. The bulletin uses a threshold of five years of earnings as a broad indicator of affordability." (ONS Housing affordability in England and Wales 2025 bulletin)

**SCOPE**

- England only (all 296 rows carry an "E"-prefixed lad25cd). 296 LADs at the May 2025 LAD boundary; 296 distinct lad25cd (no multipolygon explosion).
- 10 years of data: 2016 through 2025.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0 (OGL v3.0).

**DATA QUALITY CAVEATS**

- Earnings come from the Annual Survey of Hours and Earnings (ASHE), a 1% sample survey of employee earnings - small-area estimates carry sampling uncertainty that ONS quantifies via confidence intervals (not loaded into this table).
- Workplace-based earnings (not residence-based). For commuter LADs this can diverge meaningfully from the earnings of residents who live there.
- Median price-to-earnings ratio is sensitive to the median pivot; lower-income households face a worse picture than the median ratio implies. The `lqratio_YYYY` columns are the lower-quartile cut and are usually a better indicator for low-income affordability.
- House prices are from HM Land Registry Price Paid Data (a complete administrative record), 12-month moving window ending in September of the reference year.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `integer` |  |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. LAD May 2025 boundary geometry joined at load. |
| `fid` | `bigint` |  |
| `lad25cd` | `character varying(9)` | Source field "LAD25CD"; ONS GSS 9-character LAD code. |
| `lad25nm` | `character varying(100)` | Source field "LAD25NM"; human-readable LAD name. |
| `rgn22cd` | `character varying` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `character varying` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `character varying` | Internal categorisation: Spatial Development Strategy (SDS) area where the geometry falls. Blank or NULL where the geometry is outside any SDS area. |
| `medprice_2016` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2016. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2017` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2017. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2018` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2018. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2019` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2019. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2020` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2020. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2021` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2021. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2022` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2022. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2023` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2023. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2024` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2024. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medprice_2025` | `double precision` | Source field; median house price in LAD for the 12-month period ending September 2025. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `medearn_2016` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2016. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2017` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2017. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2018` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2018. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2019` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2019. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2020` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2020. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2021` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2021. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2022` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2022. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2023` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2023. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2024` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2024. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medearn_2025` | `double precision` | Source field; median gross annual earnings for full-time employees in LAD, mid-April 2025. Source: ONS Annual Survey of Hours and Earnings (ASHE), workplace-based. Unit: "GBP per year". |
| `medratio_2016` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2016. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2017` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2017. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2018` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2018. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2019` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2019. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2020` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2020. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2021` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2021. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2022` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2022. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2023` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2023. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2024` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2024. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medratio_2025` | `double precision` | Source field; median house price divided by median gross annual earnings ratio for LAD, year 2025. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqprice_2016` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2016. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2017` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2017. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2018` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2018. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2019` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2019. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2020` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2020. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2021` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2021. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2022` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2022. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2023` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2023. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2024` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2024. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqprice_2025` | `double precision` | Source field; lower-quartile (25th percentile) house price in LAD for the 12-month period ending September 2025. Source: HM Land Registry Price Paid Data. Unit: "GBP". |
| `lqearn_2016` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2016. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2017` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2017. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2018` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2018. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2019` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2019. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2020` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2020. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2021` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2021. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2022` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2022. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2023` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2023. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2024` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2024. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqearn_2025` | `double precision` | Source field; lower-quartile (25th percentile) gross annual earnings for full-time employees in LAD, mid-April 2025. Source: ONS ASHE, workplace-based. Unit: "GBP per year". |
| `lqratio_2016` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2016. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2017` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2017. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2018` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2018. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2019` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2019. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2020` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2020. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2021` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2021. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2022` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2022. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2023` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2023. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2024` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2024. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `lqratio_2025` | `double precision` | Source field; lower-quartile house price divided by lower-quartile gross annual earnings ratio for LAD, year 2025. Higher = less affordable. Unit: "ratio (dimensionless)". |
| `medprice_pct_2016-2025` | `double precision` | Derived at load; percentage change in medprice from 2016 to 2025 calculated as (medprice_2025 - medprice_2016) / medprice_2016 * 100. Positive = price rose. Unit: "percent change". |
| `medearn_pct_2016-2025` | `double precision` | Derived at load; percentage change in medearn from 2016 to 2025 calculated as (medearn_2025 - medearn_2016) / medearn_2016 * 100. Positive = earnings rose. Unit: "percent change". |
| `medratio_pts_2016-2025` | `double precision` | Derived at load; absolute change in medratio (ratio points) from 2016 to 2025 calculated as medratio_2025 - medratio_2016. Positive = ratio rose (less affordable). Unit: "ratio points". |
| `lqprice_pct_2016-2025` | `double precision` | Derived at load; percentage change in lqprice from 2016 to 2025 calculated as (lqprice_2025 - lqprice_2016) / lqprice_2016 * 100. Positive = price rose. Unit: "percent change". |
| `lqearn_pct_2016-2025` | `double precision` | Derived at load; percentage change in lqearn from 2016 to 2025 calculated as (lqearn_2025 - lqearn_2016) / lqearn_2016 * 100. Positive = earnings rose. Unit: "percent change". |
| `lqratio_pts_2016-2025` | `double precision` | Derived at load; absolute change in lqratio (ratio points) from 2016 to 2025 calculated as lqratio_2025 - lqratio_2016. Positive = ratio rose (less affordable). Unit: "ratio points". |
| `medprice_2016-2025` | `integer` | Derived at load; absolute change in medprice from 2016 to 2025 calculated as medprice_2025 - medprice_2016. Unit: "GBP". |
| `lqprice_2016-2025` | `integer` | Derived at load; absolute change in lqprice from 2016 to 2025 calculated as lqprice_2025 - lqprice_2016. Unit: "GBP". |
