# Office for National Statistics (ONS) regions of England with Wales, full resolution clipped to the coastline, December 2022

<p class="layer-short">Region Boundary 2022</p>

`adm_ons_region_boundary_dec2022`

**SOURCE**

- Office for National Statistics (ONS), Open Geography Portal. Two boundary products combined into one table at load on the owner's instruction (23 September 2026): the nine English regions from Regions (December 2022) Boundaries EN BFC (V2), file Regions_December_2022_Boundaries_EN_BFC_V2.gpkg (23,437,312 bytes), and the Wales row from Countries (December 2022) Boundaries UK BFC, file Countries_December_2022_Boundaries_UK_BFC.gpkg (55,173,120 bytes). The source_product column records which file each row came from.

**DOCUMENTATION**

- Regions (December 2022) EN BFC (V2)   : https://geoportal.statistics.gov.uk/datasets/9ab00f1e709b4423a9f70c748ee5951e
- Countries (December 2022) UK BFC      : https://geoportal.statistics.gov.uk/datasets/1201c18fa59444ed9eecd3d9b81705fa
- ONS administrative geography, England : https://www.ons.gov.uk/methodology/geography/ukgeographies/administrativegeography/england
- ONS geography licences                : https://www.ons.gov.uk/methodology/geography/licences

**DEFINITIONS**

- "There are nine English regions which were established in 1994 and they are the highest tier of sub-national division in England." (ONS administrative geography page)
- "This file contains the digital vector boundaries for Regions in England as at December 2022." (ONS Open Geography Portal, Regions (December 2022) EN BFC (V2))
- "This file contains the digital vector boundaries for Countries, in the United Kingdom, as at December 2022." (ONS Open Geography Portal, Countries (December 2022) UK BFC)
- "(BFC) Full resolution - clipped to the coastline (Mean High Water mark)." (ONS Open Geography Portal, both products)

**SCOPE**

- England and Wales. 10 rows: the nine English regions (E12000001 to E12000009) and Wales (W92000004). The England, Scotland and Northern Ireland rows of the countries file are not loaded.

**CRS**

- EPSG:27700 (British National Grid), as supplied in both GeoPackages. No reprojection.

**LICENCE**

- Open Government Licence v3.0. Attribution required by ONS for digital boundary products: Source: Office for National Statistics licensed under the Open Government Licence v.3.0. Contains OS data © Crown copyright and database right 2022.

**DATA QUALITY CAVEATS**

- Wales is not an English region. Its row is the ONS country boundary, carried in rgn22cd and rgn22nm as W92000004 and Wales, so that the table matches statistics published for the English regions and Wales.
- The regions file is the second version (V2) of ONS's December 2022 regions, published on the portal on 2 August 2023; ONS does not state why it was reissued.
- globalid is empty on the Wales row: the countries file carries no GlobalID.

**ENRICHMENT**

- `source_product` - the ONS product each row came from, added at load on the owner's instruction (23 September 2026).

**NOT IN THIS DATASET**

- The countries file's Welsh-language name field (CTRY22NMW) is not carried.
- The England, Scotland and Northern Ireland outlines from the countries file.

**LOADED INTO uk_baseline**

- Loaded by PNC, 23 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `gid` | `integer` |  |
| `rgn22cd` | `character varying` | Source field `RGN22CD` (regions file); on the Wales row, `CTRY22CD` from the countries file (W92000004). |
| `rgn22nm` | `character varying` | Source field `RGN22NM` (regions file); on the Wales row, `CTRY22NM` from the countries file. |
| `bng_e` | `integer` | Source field `BNG_E`; ONS publishes no definition for it with the file. |
| `bng_n` | `integer` | Source field `BNG_N`; ONS publishes no definition for it with the file. |
| `long` | `real` | Source field `LONG`; ONS publishes no definition for it with the file. |
| `lat` | `real` | Source field `LAT`; ONS publishes no definition for it with the file. |
| `globalid` | `character varying` | Source field `GlobalID` (regions file only; empty on the Wales row). |
| `source_product` | `character varying` | Derived at load: the ONS product the row came from, Regions (December 2022) Boundaries EN BFC (V2) or Countries (December 2022) Boundaries UK BFC (owner decision, 23 September 2026). |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry as supplied in the ONS GeoPackages, MultiPolygon in EPSG:27700: the regions file for the nine English regions, the countries file for Wales. |
