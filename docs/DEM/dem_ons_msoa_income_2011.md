# ONS small area model-based income estimates at Middle-layer Super Output Area (MSOA) 2011

`dem_ons_msoa_income_2011`

<iframe src="../../maps/dem_ons_msoa_income_2011.html" title="Interactive preview map of dem_ons_msoa_income_2011" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/dem_ons_msoa_income_2011.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Office for National Statistics (ONS), "Small Area Income Estimates for Middle layer Super Output Areas, England and Wales". Reference period 2011/12 (financial year ending 2012). Loaded via an earlier Prior + Partners pass.

**DOCUMENTATION**

- ONS Small Area Income landing : https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/bulletins/smallareamodelbasedincomeestimates
- ONS methodology : https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/methodologies/estimatingdistributionsofhouseholdincomeformiddlelayersuperoutputareasin2011usingsmallareaestimationmethods

**DEFINITIONS**

- "Net weekly household income adjusted for household size and composition (equivalised), after housing costs." (ONS Small Area Income methodology)
- "Equivalised income represents the income level of every individual in the household. Equivalisation considers the household size and composition, and acknowledges that, for example, two people do not need double the income of one person to have the same living standards." (ONS Small Area Income bulletin)
- These are MODEL-BASED estimates, not survey-direct measurements. ONS combined administrative tax records with the Family Resources Survey using small-area estimation methods to produce MSOA-level estimates.

**SCOPE**

- England and Wales. MSOA 2011 boundary; 7,201 distinct msoa11cd.
- Reference period: financial year 2011/12.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- ONS methodology warning: "The modelling process tends to shrink estimates towards the average level, so the true distribution of MSOA average incomes will have more extreme high and low values than the estimated values." (ONS methodology page) Translation: high-income areas under-stated, low-income areas over-stated. Use with care.
- ONS methodology warning: "Care is needed when ranking areas due to uncertainty surrounding estimates." (ONS methodology) The 90% confidence intervals overlap heavily between adjacent MSOAs.
- 2011/12 — significantly out of date for current analysis (14 years old at audit). ONS has not published an LSOA-level update since.

**LOADED INTO uk_baseline**

- Data: 2011/12 (ONS publication 2014/2015).


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `msoa11cd` | `text` | Joined at load from ONS LSOA->MSOA 2011 lookup; 2011 MSOA GSS code. |
| `msoa11nm` | `text` | Joined at load from ONS LSOA->MSOA 2011 lookup; 2011 MSOA name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Boundary geometry joined at load. |
| `lad22cd` | `text` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD GSS code. |
| `lad22nm` | `text` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD name. |
| `rgn22cd` | `text` | Joined at load from ONS LSOA->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LSOA->Region lookup; 2022 Region name. |
| `data_source` | `text` | Added during an earlier Prior + Partners loading pass. Fixed-string annotation; same value every row. |
| `data_resolution` | `text` | Added during an earlier Prior + Partners loading pass. Fixed-string annotation; same value every row. |
| `data_time_period` | `text` | Added during an earlier Prior + Partners loading pass. Fixed annotation; same value every row. |
| `data_web_link` | `text` | Added during an earlier Prior + Partners loading pass. Fixed annotation; URL to the ONS dataset page. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Unit: hectares. Stale if geometry is later edited. |
| `total_annual_income` | `bigint` | Source field; modelled total annual household income for the MSOA. Unit: "GBP per year". Reference period 2011/12. Model-based estimate — see DATA QUALITY CAVEATS. |
| `net_annual_income` | `bigint` | Source field; modelled net annual household income (after direct taxes and benefits). Unit: "GBP per year". Reference period 2011/12. |
| `net_annual_income_before_housing_costs` | `bigint` | Source field; modelled net annual household income before housing costs. Unit: "GBP per year". Reference period 2011/12. |
| `net_annual_income_after_housing_costs` | `bigint` | Source field; modelled net annual household income after housing costs. Unit: "GBP per year". Reference period 2011/12. |
| `wd22cd` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward GSS code. |
| `wd22nm` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward name. |
| `fid` | `bigint` |  |
