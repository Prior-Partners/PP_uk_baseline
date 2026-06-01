# `hth_ohid_msoa_unemployment`

Office for Health Improvement and Disparities (OHID) unemployment at Middle-layer Super Output Area (MSOA) 2011, period 2021/22. Via the Fingertips platform.

**SOURCE**

- Office for Health Improvement and Disparities (OHID), via the Fingertips public health data platform.

**DOCUMENTATION**

- Fingertips : https://fingertips.phe.org.uk/

**DEFINITIONS**

- Unemployment (Office for National Statistics / International Labour Organization basis): people "without a job, have been actively seeking work in the past four weeks and are available to start work in the next two weeks." (Office for National Statistics, A guide to labour market statistics)

**SCOPE**

- England. 7,283 rows (MSOA 2011 grain).

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `msoa11cd` | `text` | Source field "MSOA11CD"; ONS GSS 9-character MSOA 2011 code. |
| `msoa11nm` | `text` | Source field "MSOA11NM"; MSOA 2011 name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. MSOA 2011 boundary geometry. |
| `lad22cd` | `text` | Joined at load from ONS MSOA->LAD 2022 lookup; 2022 LAD GSS code. |
| `lad22nm` | `text` | Joined at load from ONS MSOA->LAD 2022 lookup; 2022 LAD name. |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `data_source` | `text` | Fixed-string annotation added during an earlier Prior + Partners loading pass; same value every row. Value: "Office for Health Improvement & Disparities". |
| `data_resolution` | `text` | Fixed-string annotation (Prior + Partners load); same value every row. Value: "MSOA 2011". |
| `data_time_period` | `text` | Fixed-string annotation (Prior + Partners load); reporting period for this dataset, same value every row. |
| `data_web_link` | `text` | Fixed-string annotation (Prior + Partners load); source platform URL, same value every row. Value: "https://fingertips.phe.org.uk/". |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `unemployment_perc` | `double precision` | Percentage of "unemployment" in the MSOA. Unit: "percent (0 to 100)". |
| `unemployment_count` | `double precision` | Count of "unemployment" in the MSOA. |
| `unemployment_denominator` | `double precision` | Denominator (population base) for "unemployment". |
| `long_term_unemployment_rate_per_1000_working_age_population` | `double precision` | Long-term unemployment rate. Unit: "per 1,000 working-age population". |
| `long_term_unemployment_count` | `double precision` | Count of "long term unemployment" in the MSOA. |
| `long_term_unemployment_denominator` | `double precision` | Denominator (population base) for "long term unemployment". |
| `wd22cd` | `character varying` | Joined at load from ONS Ward 2022 lookup; 2022 Ward GSS code. |
| `wd22nm` | `character varying` | Joined at load from ONS Ward 2022 lookup; 2022 Ward name. |
| `fid` | `bigint` |  |
