# Office for Health Improvement and Disparities (OHID) life expectancy at birth at Middle-layer Super Output Area (MSOA) 2011, period 2016-2020

`hth_ohid_msoa_life_expectancy_2020`

<a href="http://localhost:7800/?layer=uk_baseline.hth_ohid_msoa_life_expectancy_2020" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

Via the Fingertips platform.

**SOURCE**

- Office for Health Improvement and Disparities (OHID), via the Fingertips public health data platform.

**DOCUMENTATION**

- Fingertips : https://fingertips.phe.org.uk/

**DEFINITIONS**

- "A period life expectancy is defined as the average number of additional years a person can be expected to live for, if he or she experienced the age-specific mortality rates of the given area and time period for the rest of his or her life." (Office for National Statistics)

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
| `female_population` | `double precision` | Female population (base for the female figures). |
| `male_population` | `double precision` | Male population (base for the male figures). |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `male_life_expectancy` | `double precision` | Male period life expectancy at birth. Unit: "years". |
| `female_life_expectancy` | `double precision` | Female period life expectancy at birth. Unit: "years". |
| `avg_life_expectancy` | `double precision` | Combined (all-persons) period life expectancy at birth. Unit: "years". |
| `national_benchmark_male` | `text` | England benchmark male life expectancy at birth. Unit: "years". |
| `national_benchmark_female` | `text` | England benchmark female life expectancy at birth. Unit: "years". |
| `national_benchmark_combined` | `text` | England benchmark combined life expectancy at birth. Unit: "years". |
| `fid` | `bigint` |  |
