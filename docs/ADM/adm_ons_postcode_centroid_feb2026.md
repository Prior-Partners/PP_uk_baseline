# ONS Postcode Directory (ONSPD), United Kingdom, February 2026 edition

`adm_ons_postcode_centroid_feb2026`

<iframe src="../../maps/adm_ons_postcode_centroid_feb2026.html" title="Interactive preview map of adm_ons_postcode_centroid_feb2026" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/adm_ons_postcode_centroid_feb2026.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Office for National Statistics (ONS), ONS Geography. Postcode centroids derived from Code-Point Open (Ordnance Survey) and Royal Mail postcode data via the Gridlink process. Northern Ireland grid references from Land and Property Services (LPS) 'Pointer'.

**DOCUMENTATION**

- Dataset      : https://geoportal.statistics.gov.uk/datasets/3080229224424c9cb53c0b48f5a64d27
- Postcode products : https://www.ons.gov.uk/methodology/geography/geographicalproducts/postcodeproducts
- User Guide   : "ONSPD User Guide February 2026" (bundled with the release zip)

**DEFINITIONS**

- "The ONS Postcode Directory (ONSPD) relates both current and terminated postcodes in the United Kingdom to a range of current statutory administrative, electoral, health and other area geographies." (ONSPD User Guide)
- Postcode centroid positional quality is given per row by `gridind`; the grid reference is the mean of the postcode's addresses snapped to the closest address.

**SCOPE**

- 2,723,596 unit postcodes (live and terminated), UK + Channel Islands + Isle of Man.
- 915,867 are terminated postcodes (retained by ONS, with `doterm` set).

**CRS**

- EPSG:27700 (OSGB36 British National Grid). `geom` is populated for Great Britain postcodes only, directly from `east1m`/`north1m`. Northern Ireland grid references use the Irish National Grid and Channel Islands / Isle of Man have no grid reference, so those rows carry NULL geom; their WGS84 `lat`/`long` are retained.

**LICENCE**

- Open Government Licence v3.0. Attribution required: "Contains OS data (c) Crown copyright and database right 2026"; "Contains Royal Mail data (c) Royal Mail copyright and database right 2026"; "Source: Office for National Statistics licensed under the Open Government Licence v.3.0". Northern Ireland (BT) postcodes require a separate Land and Property Services licence for commercial use.

**DATA QUALITY CAVEATS**

- Postcode-to-area assignment can be imprecise near boundaries (straddling) or for new postcodes (imputed grid references); see `gridind`.
- This is a postcode-centroid reference layer for joining postcode-only datasets (e.g. HM Land Registry Price Paid Data) to coordinates and admin geographies; it is not address-level.

**LOADED INTO uk_baseline**

- Loaded by PNC, 1 June 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `pcd7` | `text` | Source field `pcd7`. Unit postcode, fixed 7-character form. |
| `pcd8` | `text` | Source field `pcd8`. Unit postcode, fixed 8-character form. |
| `pcds` | `text` | Source field `pcds`. Unit postcode, variable-length single-space (e-Gif) form: "2, 3 or 4-character outward code; Single space; 3-character inward code". Primary key. |
| `dointr` | `text` | Source field `dointr`. "The most recent occurrence of the postcode's date of introduction." Format YYYYMM. |
| `doterm` | `text` | Source field `doterm`. "If present, the most recent occurrence of the postcode's date of termination, otherwise: null = 'live' postcode." Format YYYYMM. Blank string = live postcode. |
| `cty25cd` | `text` | Source field `cty25cd`. |
| `ced25cd` | `text` | Source field `ced25cd`. |
| `lad25cd` | `text` | Source field `lad25cd`. Local authority district the postcode is assigned to (GSS code). |
| `wd25cd` | `text` | Source field `wd25cd`. |
| `parncp25cd` | `text` | Source field `parncp25cd`. |
| `usrtypind` | `text` | Source field `usrtypind`. Postcode user type: 0 = small user, 1 = large user. |
| `east1m` | `text` | Source field `east1m`. "The OS grid reference Easting to 1 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish National Grid." |
| `north1m` | `text` | Source field `north1m`. "The OS grid reference Northing to 1 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish National Grid." |
| `gridind` | `text` | Source field `gridind`. Grid reference positional quality indicator: 1 = within the building closest to the postcode mean; 3 = within 50 m; 4 = postcode unit mean; 5 = imputed by ONS; 6 = postcode sector mean (mainly PO Boxes); 8 = terminated prior to Gridlink, last known grid reference; 9 = no grid reference available. |
| `hlth19cd` | `text` | Source field `hlth19cd`. |
| `nhser24cd` | `text` | Source field `nhser24cd`. |
| `ctry25cd` | `text` | Source field `ctry25cd`. Country GSS code (E92000001 England, W92000004 Wales, S92000003 Scotland, N92000002 Northern Ireland, L93000001 Channel Islands, M83000003 Isle of Man). |
| `rgn25cd` | `text` | Source field `rgn25cd`. Region (former Government Office Region) GSS code (E12 England); pseudo codes for Wales, Scotland, Northern Ireland, Channel Islands and Isle of Man. |
| `ssr95cd` | `text` | Source field `ssr95cd`. Former Standard Statistical Region: 1-8 = England regions; 9 = Wales (pseudo); 0 = not in England or Wales (pseudo). |
| `pcon24cd` | `text` | Source field `pcon24cd`. Westminster parliamentary constituency GSS code. |
| `eer20cd` | `text` | Source field `eer20cd`. European Electoral Region GSS code. |
| `educ23cd` | `text` | Source field `educ23cd`. Local Learning and Skills Council (England) / Department for Children, Education, Lifelong Learning and Skills (Wales) / Enterprise Region (Scotland) code. |
| `ttwa15cd` | `text` | Source field `ttwa15cd`. 2011 Census Travel to Work Area code. |
| `pco19cd` | `text` | Source field `pco19cd`. Primary Care Organisation code: Primary Care Trust/Care Trust (England), Local Health Board (Wales), Community Health Partnership (Scotland), Local Commissioning Group (Northern Ireland), Primary Healthcare Directorate (Isle of Man). |
| `itl25cd` | `text` | Source field `itl25cd`. International Territorial Level (former NUTS) LAU1-equivalent code. |
| `wdstl05cd` | `text` | Source field `wdstl05cd`. 2005 'statistical' ward (England and Wales only), used for statistical analysis. |
| `oa01cd` | `text` | Source field `oa01cd`. 2001 Census Output Area code. |
| `wdcas03cd` | `text` | Source field `wdcas03cd`. 2003 Census Area Statistics (CAS) ward code (sub-threshold wards assigned to their receiving ward). |
| `npark16cd` | `text` | Source field `npark16cd`. National park code (England, Wales, Scotland); pseudo / non-national-park codes elsewhere. |
| `lsoa01cd` | `text` | Source field `lsoa01cd`. 2001 Census Lower Layer Super Output Area (England & Wales), Data Zone (Scotland) or Super Output Area (Northern Ireland) code. |
| `msoa01cd` | `text` | Source field `msoa01cd`. 2001 Census Middle Layer Super Output Area (England & Wales) or Intermediate Zone (Scotland) code. |
| `ruc01ind` | `text` | Source field `ruc01ind`. 2001 Census urban/rural classification of the Output Area (England & Wales 1-8; Scotland 1-8; Northern Ireland A-H). |
| `oac01ind` | `text` | Source field `oac01ind`. 2001 Census Output Area Classification (supergroup/group/subgroup) code. |
| `oa11cd` | `text` | Source field `oa11cd`. 2011 Census Output Area (Great Britain) / Small Area (Northern Ireland) code. |
| `lsoa11cd` | `text` | Source field `lsoa11cd`. 2011 Census Lower Layer Super Output Area (England & Wales), Data Zone (Scotland) or Super Output Area (Northern Ireland) code. |
| `msoa11cd` | `text` | Source field `msoa11cd`. 2011 Census Middle Layer Super Output Area (England & Wales) or Intermediate Zone (Scotland) code. |
| `wz11cd` | `text` | Source field `wz11cd`. 2011 Census Workplace Zone code. |
| `sicbl24cd` | `text` | Source field `sicbl24cd`. Sub ICB Location (England, formerly Clinical Commissioning Group) / Local Health Board (Wales) / Community Health Partnership (Scotland) / Local Commissioning Group (Northern Ireland) / Primary Healthcare Directorate (Isle of Man) code. |
| `bua24cd` | `text` | Source field `bua24cd`. 2021 Census Built-up Area code (England & Wales); cross-border codes for areas straddling the England/Wales border. |
| `ruc11ind` | `text` | Source field `ruc11ind`. 2011 Census rural-urban classification of the Output Area (England & Wales A1-F2; Scotland 1-8). |
| `oac11ind` | `text` | Source field `oac11ind`. 2011 Census Output Area Classification (supergroup/group/subgroup) code. |
| `lat` | `text` | Source field `lat`. WGS84 latitude to six decimal places; 99.999999 for Channel Islands / Isle of Man and for postcodes with no grid reference. |
| `long` | `text` | Source field `long`. WGS84 longitude to six decimal places; 0.000000 for Channel Islands / Isle of Man and for postcodes with no grid reference. |
| `lep21cd1` | `text` | Source field `lep21cd1`. Primary Local Enterprise Partnership code (England); pseudo codes elsewhere. |
| `lep21cd2` | `text` | Source field `lep21cd2`. Secondary Local Enterprise Partnership code where Local Enterprise Partnerships overlap (England); blank or pseudo otherwise. |
| `pfa23cd` | `text` | Source field `pfa23cd`. Police Force Area code. |
| `imd20ind` | `text` | Source field `imd20ind`. Index of Multiple Deprivation rank of the postcode's 2011 LSOA/OA/Data Zone, where 1 = most deprived. Ranks are country-specific (England 1-32,844; Wales 1-1,909; Scotland 1-6,976; Northern Ireland 1-890) and not comparable across countries. |
| `cal24cd` | `text` | Source field `cal24cd`. Cancer Alliance code (England); pseudo codes elsewhere. |
| `icb23cd` | `text` | Source field `icb23cd`. Integrated Care Board code (England, formerly Sustainability and Transformation Partnership); pseudo codes elsewhere. |
| `oa21cd` | `text` | Source field `oa21cd`. 2021 Census Output Area / Data Zone code. |
| `lsoa21cd` | `text` | Source field `lsoa21cd`. 2021 Census Lower Layer Super Output Area / Super Data Zone code (England, Wales, Scotland). |
| `msoa21cd` | `text` | Source field `msoa21cd`. 2021 Census Middle Layer Super Output Area code (England, Wales, Scotland). |
| `ruc21ind` | `text` | Source field `ruc21ind`. |
| `geom` | `geometry(Point,27700)` | Point geometry in EPSG:27700, derived at load from `east1m`/`north1m` for Great Britain postcodes (England, Wales, Scotland) only. NULL for Northern Ireland (grid is Irish National Grid, not BNG), Channel Islands, Isle of Man, and postcodes with no grid reference. |
