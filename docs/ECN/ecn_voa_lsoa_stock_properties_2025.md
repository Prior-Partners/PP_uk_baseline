# Valuation Office Agency (VOA) Stock of Properties at Lower Super Output Area (LSOA), 2025

`ecn_voa_lsoa_stock_properties_2025`

<iframe src="../maps/ecn_voa_lsoa_stock_properties_2025.html" title="Interactive preview map of ecn_voa_lsoa_stock_properties_2025" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/ecn_voa_lsoa_stock_properties_2025.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Valuation Office Agency (VOA) Non-Domestic Rating (NDR), gov.uk publication 2025-06 (reference date 31 March 2025). Source ZIP: ndr_stock_oa_2025.zip (10 CSVs: SOP_OA_counts_all.csv.. SOP_OA_rv_other.csv).

**DOCUMENTATION**

- Dataset page : https://www.gov.uk/government/statistics/non-domestic-rating-stock-of-properties-2025
- Background information : https://www.gov.uk/government/statistics/non-domestic-rating-stock-of-properties-2025/non-domestic-rating-stock-of-properties-background-information

**DEFINITIONS**

- Stock of Properties: "The statistics provide information on the number and value of the stock of rateable properties (known as 'hereditaments'), broken down by sector, geographic location, Special Category (SCat), property type and rateable value band." (gov.uk background-information page)
- Hereditament: "A rateable property is a property on which rates may be charged and is the unit to which the VOA assigns RV. In general, rateable properties are buildings or premises within buildings, appropriate for or used for single occupation. Rateable properties can be occupied or vacant." (gov.uk background-information page)
- Rateable Value (RV): "The RV of a property is broadly the value at which a property might be expected to be let for one year." (gov.uk background-information page)
- Rating list mapping: "those for 2011-2017 are based on the 2010 rating list; 2018-2023 are based on the 2017 rating list and 2024-2025 are based on the 2023 rating list." (gov.uk background-information page)

**SCOPE**

- Lower Super Output Area (LSOA) 2021 boundaries, England and Wales. 35,672 rows (E: 33,755; W: 1,917). Source CSV rows filtered to geography = 'LSOA'.

**CRS**

- EPSG:27700 (British National Grid).

**LICENCE**

- Open Government Licence v3.0 (OGL). © Crown copyright. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

**DATA QUALITY CAVEATS**

- VOA disclosure-suppressed cells ('[c]' in source CSVs) preserved as NULL, not 0.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `lsoa21cd` | `character varying(20)` | Source field `area_code` |
| `lsoa21nm` | `character varying(255)` | Source field `area_name` |
| `count_all_2011` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2011` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2011` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2011` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2011` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2011` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2011` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2011` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2011` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2011` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2012` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2012` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2012` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2012` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2012` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2012` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2012` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2012` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2012` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2012` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2013` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2013` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2013` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2013` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2013` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2013` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2013` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2013` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2013` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2013` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2014` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2014` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2014` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2014` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2014` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2014` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2014` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2014` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2014` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2014` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2015` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2015` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2015` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2015` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2015` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2015` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2015` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2015` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2015` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2015` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2016` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2016` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2016` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2016` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2016` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2016` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2016` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2016` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2016` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2016` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2017` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2017` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2017` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2017` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2017` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2017` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2017` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2017` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2017` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2017` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2018` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2018` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2018` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2018` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2018` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2018` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2018` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2018` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2018` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2018` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2019` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2019` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2019` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2019` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2019` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2019` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2019` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2019` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2019` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2019` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2020` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2020` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2020` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2020` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2020` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2020` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2020` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2020` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2020` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2020` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2021` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2021` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2021` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2021` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2021` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2021` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2021` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2021` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2021` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2021` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2022` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2022` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2022` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2022` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2022` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2022` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2022` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2022` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2022` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2022` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2023` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2023` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2023` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2023` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2023` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2023` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2023` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2023` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2023` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2023` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2024` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2024` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2024` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2024` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2024` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2024` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2024` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2024` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2024` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2024` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `count_all_2025` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_retail_2025` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_office_2025` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_industrial_2025` | `integer` | Unit: "Number of rateable properties (count)" |
| `count_other_2025` | `integer` | Unit: "Number of rateable properties (count)" |
| `rateable_value_all_2025` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_retail_2025` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_office_2025` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_industrial_2025` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `rateable_value_other_2025` | `integer` | Unit: "total rateable value (£ in thousands)" |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_lsoa_boundary_2021 |
