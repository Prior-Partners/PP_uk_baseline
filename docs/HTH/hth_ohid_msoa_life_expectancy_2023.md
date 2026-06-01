# Office for Health Improvement and Disparities (OHID) Life expectancy at birth by sex for Middle Layer Super Output Areas (MSOA), England: 2019 to 2023

`hth_ohid_msoa_life_expectancy_2023`

**SOURCE**

- Office for Health Improvement and Disparities (OHID), Department of Health and Social Care, via Fingertips Public Health Profiles. Indicator 93283. Numerator and denominator originate from Office for National Statistics (ONS) annual births and mortality extracts.
- Boundary attributes (LAD May 2022, Region 2022) joined from ONS Open Geography Portal best-fit lookup.
- Geometry inherited from uk_baseline.adm_ons_msoa_boundary_2021.

**DOCUMENTATION**

- Indicator data (API)     : https://fingertips.phe.org.uk/api/all_data/csv/by_indicator_id?indicator_ids=93283&child_area_type_id=3&parent_area_type_id=15
- Indicator metadata (API) : https://fingertips.phe.org.uk/api/indicator_metadata/csv/by_indicator_id?indicator_ids=93283
- Indicator profile page   : https://fingertips.phe.org.uk/profile/local-health/data#page/0/gid/1938133185/pat/15000/par/E92000001/ati/3/iid/93283/age/1/sex/4/cat/-1/ctp/-1/yrr/5/cid/4
- MSOA21->LAD22->RGN22 LU  : https://geoportal.statistics.gov.uk/datasets/ons::msoa-2021-to-bua-to-lad-to-region-december-2022-best-fit-lookup-in-ew-v2/about

**DEFINITIONS**

- "Life expectancy is the average number of years a person would expect to live based on contemporary mortality rates. For a particular area and time period, it is an estimate of the average number of years a newborn baby would survive if he or she experienced the age specific mortality rates for that area and time period throughout his or her life. Figures reflect mortality among those living in an area in each time period, rather than mortality among those born in the area. The figures are not therefore the number of years a baby born in the area could actually expect to live, both because the mortality rates of the area are likely to change in the future and because many of those born in the area will live elsewhere for at least some part of their lives." (Fingertips indicator 93283 metadata, Definition)

**SCOPE**

- England. 6,856 MSOAs (2021 boundary).
- Time period: 2019 to 2023 (5-year pooled).

**CRS**

- EPSG:27700 (British National Grid).

**LICENCE**

- Open Government Licence v3.0, additionally constrained by Fingertips terms: "Non commercial use only. Any reuse of these data must carry the recognition of Crown Copyright and acknowledge the Office for National Statistics and the Office for Health Improvement and Disparities as the data source." (Fingertips indicator 93283 metadata, Data re-use)

**DATA QUALITY CAVEATS**

- Suppression rule: "Life expectancy values have not been presented for areas where: the person-years in any given age interval is zero; the population is less than 5,000; there are no deaths in the 90 years and over age group; the number of deaths in an age group is greater than the population estimate for that age group; the confidence interval around the life expectancy value is greater than 20 years." (Fingertips indicator 93283 metadata, Disclosure control). Where suppression applies, the value columns are NULL and the corresponding *_value_note column carries the publisher's suppression text.
- Boundary attributes (lad22cd, lad22nm, rgn22cd, rgn22nm) are LAD May 2022 / Region 2022 vintage. The April 2023 LAD reorganisations (creation of Cumberland, Westmorland and Furness, North Yorkshire UA, Somerset UA, and the Buckinghamshire merger) are not reflected. Region codes E12000001 to E12000009 are stable across vintages, so rgn22cd values would be identical if labelled rgn23cd or rgn24cd.

**LOADED INTO uk_baseline**

- Loaded by PNC, 29 May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `bigint` |  |
| `msoa21cd` | `text` | Source field `Area Code` from Fingertips (MSOA 2021 code). |
| `msoa21nm` | `text` | Geometry attribute from uk_baseline.adm_ons_msoa_boundary_2021 (canonical MSOA 2021 name; Fingertips' Area Name records the LAD name instead). |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_msoa_boundary_2021. |
| `lad22cd` | `text` | Best-fit join from uk.ref_msoa21_lad22_rgn22_lu_dec2022_v2.lad22cd (LAD May 2022 boundary). |
| `lad22nm` | `text` | Best-fit join from uk.ref_msoa21_lad22_rgn22_lu_dec2022_v2.lad22nm. |
| `rgn22cd` | `text` | Best-fit join from uk.ref_msoa21_lad22_rgn22_lu_dec2022_v2.rgn22cd. Codes E12000001 to E12000009 are stable across vintages. |
| `rgn22nm` | `text` | Best-fit join from uk.ref_msoa21_lad22_rgn22_lu_dec2022_v2.rgn22nm. |
| `bua22cd` | `text` | Best-fit join from uk.ref_msoa21_lad22_rgn22_lu_dec2022_v2.bua22cd (Built-Up Area 2022). |
| `bua22nm` | `text` | Best-fit join from uk.ref_msoa21_lad22_rgn22_lu_dec2022_v2.bua22nm. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Goes stale if the geometry is later edited. |
| `indicator_id` | `text` | Source field `Indicator ID`. Constant 93283 for every row. |
| `indicator_name` | `text` | Source field `Indicator Name`. Constant "Life expectancy at birth". |
| `parent_area_code` | `text` | Source field `Parent Code`. Constant E92000001 (England). |
| `parent_area_name` | `text` | Source field `Parent Name`. Constant "England". |
| `fingertips_area_name` | `text` | Source field `Area Name`. Note: Fingertips populates this with the LAD name, not the MSOA name; kept verbatim from source. |
| `area_type` | `text` | Source field `Area Type`. Constant "MSOA". |
| `age_group` | `text` | Source field `Age`. Constant "All ages" for this indicator. |
| `category_type` | `text` | Source field `Category Type`. Empty for this indicator. |
| `category` | `text` | Source field `Category`. Empty for this indicator. |
| `time_period` | `text` | Source field `Time period`. |
| `time_period_sortable` | `text` | Source field `Time period Sortable`. |
| `time_period_range` | `text` | Source field `Time period range`. |
| `male_life_expectancy` | `double precision` | Male: Source field `Value`. Unit: "Years". |
| `female_life_expectancy` | `double precision` | Female: Source field `Value`. Unit: "Years". |
| `male_life_exp_ci95_lower` | `double precision` | Male: Source field `Lower CI 95.0 limit`. Unit: "Years". |
| `female_life_exp_ci95_lower` | `double precision` | Female: Source field `Lower CI 95.0 limit`. Unit: "Years". |
| `male_life_exp_ci95_upper` | `double precision` | Male: Source field `Upper CI 95.0 limit`. Unit: "Years". |
| `female_life_exp_ci95_upper` | `double precision` | Female: Source field `Upper CI 95.0 limit`. Unit: "Years". |
| `male_life_exp_ci998_lower` | `double precision` | Male: Source field `Lower CI 99.8 limit`. Unit: "Years". Empty for the 2019-23 release. |
| `female_life_exp_ci998_lower` | `double precision` | Female: Source field `Lower CI 99.8 limit`. Unit: "Years". Empty for the 2019-23 release. |
| `male_life_exp_ci998_upper` | `double precision` | Male: Source field `Upper CI 99.8 limit`. Unit: "Years". Empty for the 2019-23 release. |
| `female_life_exp_ci998_upper` | `double precision` | Female: Source field `Upper CI 99.8 limit`. Unit: "Years". Empty for the 2019-23 release. |
| `male_case_count` | `double precision` | Male: Source field `Count`. Renamed from the source name `Count` to avoid clash with the SQL function. |
| `female_case_count` | `double precision` | Female: Source field `Count`. Renamed from the source name `Count` to avoid clash with the SQL function. |
| `male_denominator` | `double precision` | Male: Source field `Denominator`. |
| `female_denominator` | `double precision` | Female: Source field `Denominator`. |
| `male_data_note` | `text` | Male: Source field `Value note`. Note attached to the life expectancy estimate (provisional-population or suppression flag from the publisher). |
| `female_data_note` | `text` | Female: Source field `Value note`. Note attached to the life expectancy estimate (provisional-population or suppression flag from the publisher). |
| `male_recent_trend` | `text` | Male: Source field `Recent Trend`. |
| `female_recent_trend` | `text` | Female: Source field `Recent Trend`. |
| `male_vs_england` | `text` | Male: Source field `Compared to England value or percentiles`. |
| `female_vs_england` | `text` | Female: Source field `Compared to England value or percentiles`. |
| `male_vs_percentile` | `text` | Male: Source field `Compared to percentiles`. |
| `female_vs_percentile` | `text` | Female: Source field `Compared to percentiles`. |
| `male_new_data` | `text` | Male: Source field `New data`. |
| `female_new_data` | `text` | Female: Source field `New data`. |
| `male_vs_goal` | `text` | Male: Source field `Compared to goal`. |
| `female_vs_goal` | `text` | Female: Source field `Compared to goal`. |
