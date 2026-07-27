# Office for Health Improvement and Disparities (OHID) life expectancy at birth at Middle-layer Super Output Area (MSOA) 2011, period 2016-2020

<p class="layer-short">Life Expectancy</p>

`hth_ohid_msoa_life_expectancy_2020`

<img src="../../maps/hth_ohid_msoa_life_expectancy_2020.png" alt="Styling preview of hth_ohid_msoa_life_expectancy_2020" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

Via the Fingertips platform.

**SOURCE**

- Office for Health Improvement and Disparities (OHID), via the Fingertips public health data platform.

**DOCUMENTATION**

- Fingertips : https://fingertips.phe.org.uk/

**DEFINITIONS**

- "A period life expectancy is defined as the average number of additional years a person can be expected to live for, if he or she experienced the age-specific mortality rates of the given area and time period for the rest of his or her life." (Office for National Statistics)

**SCOPE**

- England. 7,283 rows (MSOA 2011 level).

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- This table is published on 2011 MSOA boundaries and its values are 2011-vintage; `msoa21hclnm` is a readable label for the corresponding 2021 MSOA and does not re-aggregate any value onto 2021 geography. For MSOAs unchanged in 2021 the name is exact. For the small number of 2011 MSOAs that were split, the column lists every successor name separated by a semicolon, so those rows carry more than one name and cannot be joined to a single msoa21cd. No 2021 geography codes are recorded on this table.

**ENRICHMENT**

- `msoa21hclnm` — House of Commons Library readable MSOA name for the 2021 MSOA corresponding to this row's 2011 MSOA, joined at load via uk.ref_msoa11_msoa21_name_lu. Open Parliament Licence.


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
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name for the 2021 MSOA corresponding to this row's 2011 MSOA, joined at load on the 2011 code via uk.ref_msoa11_msoa21_name_lu. Where the MSOA is unchanged in 2021 (the great majority) the name is exact. Where a 2011 MSOA was split into several 2021 MSOAs this records all successor names, separated by a semicolon. Where a 2011 MSOA was merged into a larger 2021 MSOA, or its code was reissued, it records that single successor name. Open Parliament Licence. |
