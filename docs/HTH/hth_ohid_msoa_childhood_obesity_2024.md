# Office for Health Improvement and Disparities (OHID) childhood obesity and overweight prevalence at Middle-layer Super Output Area (MSOA) 2011, period 2021/22-2023/24

`hth_ohid_msoa_childhood_obesity_2024`

<a href="http://localhost:7800/?layer=uk_baseline.hth_ohid_msoa_childhood_obesity_2024" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

From the National Child Measurement Programme via the Fingertips platform.

**SOURCE**

- Office for Health Improvement and Disparities (OHID), via the Fingertips public health data platform. Underlying source: National Child Measurement Programme (NCMP).

**DOCUMENTATION**

- Fingertips                           : https://fingertips.phe.org.uk/
- National Child Measurement Programme : https://www.gov.uk/government/collections/national-child-measurement-programme

**DEFINITIONS**

- "Fingertips is a large public health data collection. Data is organised into themed profiles." (Office for Health Improvement and Disparities, Fingertips)
- "The National Child Measurement Programme (NCMP) is a nationally mandated public health programme in England. It provides data to monitor the patterns and trends, and the prevalence, of underweight, healthy weight, overweight and obesity in children as well as data on child height." (gov.uk, National Child Measurement Programme)

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
| `reception_prevalence_of_obesity_perc` | `double precision` | Percentage of "reception prevalence of obesity" in the MSOA. Unit: "percent (0 to 100)". |
| `reception_prevalence_of_obesity_count` | `double precision` | Count of "reception prevalence of obesity" in the MSOA. |
| `reception_prevalence_of_obesity_denominator` | `double precision` | Denominator (population base) for "reception prevalence of obesity". |
| `reception_prevalence_of_overweight_perc` | `double precision` | Percentage of "reception prevalence of overweight" in the MSOA. Unit: "percent (0 to 100)". |
| `reception_prevalence_of_overweight_count` | `double precision` | Count of "reception prevalence of overweight" in the MSOA. |
| `reception_prevalence_of_overweight_denominator` | `double precision` | Denominator (population base) for "reception prevalence of overweight". |
| `year_6_prevalence_of_obesity_perc` | `double precision` | Percentage of "year 6 prevalence of obesity" in the MSOA. Unit: "percent (0 to 100)". |
| `year_6_prevalence_of_obesity_count` | `double precision` | Count of "year 6 prevalence of obesity" in the MSOA. |
| `year_6_prevalence_of_obesity_denominator` | `double precision` | Denominator (population base) for "year 6 prevalence of obesity". |
| `year_6_prevalence_of_overweight_perc` | `double precision` | Percentage of "year 6 prevalence of overweight" in the MSOA. Unit: "percent (0 to 100)". |
| `year_6_prevalence_of_overweight_count` | `double precision` | Count of "year 6 prevalence of overweight" in the MSOA. |
| `year_6_prevalence_of_overweight_denominator` | `double precision` | Denominator (population base) for "year 6 prevalence of overweight". |
| `wd22cd` | `character varying` | Joined at load from ONS Ward 2022 lookup; 2022 Ward GSS code. |
| `wd22nm` | `character varying` | Joined at load from ONS Ward 2022 lookup; 2022 Ward name. |
| `fid` | `bigint` |  |
