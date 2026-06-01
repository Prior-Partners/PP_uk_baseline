# `blt_os_important_buildings`

OS OpenMap Local Important Buildings - generalised buildings of public importance.

**SOURCE**

- Ordnance Survey (OS), Open Map Local product.

**DOCUMENTATION**

- Product page : https://osdatahub.os.uk/data/downloads/open/OpenMapLocal
- Product guide : https://www.ordnancesurvey.co.uk/documents/os-open-map-local-product-guide.pdf

**DEFINITIONS**

- ImportantBuilding feature type: "A generalised building that belongs to a FunctionalSite." (OS OpenMap Local Product Guide, Land Use / ImportantBuilding)
- "Buildings that fall within the extent of a functional site are identified as Important Buildings. These buildings share attribution with their associated functional site." (OS OpenMap Local Product Guide)
- "Not all Important Building are represented within a functional site. Those without a functional site are deemed as important for navigational aid." (OS OpenMap Local Product Guide)
- Building themes (11): Attraction and Leisure, Air Transport, Cultural Facility, Education facility, Emergency Services, Medical Facility, Religious Building, Retail, Road Transport, Sports and Leisure Facility, Water Transport.

**SCOPE**

- Great Britain (England, Wales, Scotland).
- 238,089 distinct buildings by id; 238,730 rows total (641 id duplicates carried from upstream - see caveats).

**CRS**

- EPSG:27700 (British National Grid / BNG).

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data (c) Crown copyright and database right [year]" required).

**DATA QUALITY CAVEATS**

- 641 id values appear more than once (238,089 distinct id across 238,730 rows). Cause not investigated; likely upstream artifacts of partial-update cycles.
- The OS Product Guide says BuildingTheme uses the "SiteThemeType code list", but the BuildingTheme code list contains 11 values while SiteTheme contains only 5 - the published code lists are different. Use the actual values observed in the column rather than the SiteTheme list. at load time.

**ENRICHMENT**

- lad22cd, lad22nm : spatial intersect with ONS 2022 LAD boundaries.
- wd21cd, wd21nm : spatial intersect with ONS 2021 Ward boundaries.
- area_ha : derived from geom at load (area in hectares, computed from the geometry at load).


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `character varying` | Source field "id" (UUID); upstream OS identifier. 641 duplicates exist - see caveats. |
| `building_theme` | `character varying` | Source field "BuildingTheme". "A description of the theme that a particular site falls under (that is, air transport, education, medical care and so on.)." (OS Product Guide). 11 valid values (see table comment). |
| `classification` | `character varying` | Source field "classification". "A description of the actual function of a site (that is, airfield, junior school, hospital and so on.) The valid values are defined in the SiteClassification code list. For sites with multiple functions, the values will be provided together and separated by a ','." (OS Product Guide). Length 90. |
| `distinctive_name` | `character varying` | Source field "distinctiveName". "The name of the site (for example, 'Brighton College'). Note this may be null if the captured value is a house number." (OS Product Guide). Length 120. |
| `feature_code` | `bigint` | Source field "featureCode". "A unique feature code to facilitate styling." (OS Product Guide). |
| `fid_original` | `integer` | Source numeric identifier preserved at load. |
| `lad22nm` | `character varying` | Joined at load from spatial intersection with ONS 2022 LAD boundaries; LAD name. |
| `lad22cd` | `character varying` | Joined at load from spatial intersection with ONS 2022 LAD boundaries; LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from spatial intersection with ONS 2021 Ward boundaries; Ward name. |
| `wd21cd` | `character varying` | Joined at load from spatial intersection with ONS 2021 Ward boundaries; Ward GSS code. |
| `geom` | `geometry(Polygon,27700)` | Source field "geometry". "Polygon representing the generalised important building." (OS Product Guide). EPSG:27700. |
| `area_ha` | `double precision` | Derived at load from ST_Area(geom)/10000. Unit: "hectares". Stale if geometry edited later. |
| `fid` | `bigint` |  |
