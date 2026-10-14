# Office for National Statistics (ONS) parishes and non-civil parished areas of England with the communities of Wales, full resolution clipped to the coastline, May 2026

<p class="layer-short">Parish and Non-Civil Parished Area Boundary 2026</p>

`adm_ons_parish_non_civil_parished_area_may2026`

**SOURCE**

- Office for National Statistics (ONS), Open Geography Portal. Parishes and Non-Civil Parished Areas (May 2026) Boundaries EW BFC, file PARNCP_MAY_2026_EW_BFC_-1299597603504015581.gpkg (314,183,680 bytes), layer PARNCP_MAY_2026_EW_BFC, loaded as published.

**DOCUMENTATION**

- Parishes and Non-Civil Parished Areas (May 2026) EW BFC : https://open-geography-portalx-ons.hub.arcgis.com/datasets/ons::parishes-and-non-civil-parished-areas-may-2026-boundaries-ew-bfc
- Catalogue record, data.gov.uk                            : https://ckan.publishing.service.gov.uk/dataset/parishes-and-non-civil-parished-areas-may-2026-boundaries-ew-bfc
- ONS administrative geography, England                    : https://www.ons.gov.uk/methodology/geography/ukgeographies/administrativegeography/england
- ONS administrative geography, Wales                      : https://www.ons.gov.uk/methodology/geography/ukgeographies/administrativegeography/wales
- ONS geography licences                                   : https://www.ons.gov.uk/methodology/geography/licences

**DEFINITIONS**

- "The smallest type of administrative area in England is the parish (aka 'civil parish'); the equivalent unit in Wales is the community." (ONS administrative geography page, England)
- "Non-civil parish areas (NCP) refer to the area in a local authority not comprised of parishes, that is unparished areas." (ONS administrative geography page, England)
- "Parishes are confined within local authority district boundaries but are not contiguous with electoral wards." (ONS administrative geography page, England)
- "The Welsh equivalent of parishes are communities, which fit into and change with unitary authorities." (ONS administrative geography page, Wales)
- "This file contains the digital vector boundaries for Parishes and Non-Civil Parished Areas, in England and Wales, as at May 2026." (ONS Open Geography Portal)
- "(BFC) Full resolution - clipped to the coastline (Mean High Water mark)." (ONS Open Geography Portal)

**SCOPE**

- England and Wales. 11,542 rows, one per area: 10,464 parishes in England (codes E04), 200 non-civil parished areas in England (codes E43, each named "<district>, unparished area") and 878 communities in Wales (codes W04). Each row carries its local authority district (318 districts).

**CRS**

- EPSG:27700 (British National Grid), as supplied in the GeoPackage. No reprojection.

**LICENCE**

- Open Government Licence v3.0. Attribution required by ONS for digital boundary products: Source: Office for National Statistics licensed under the Open Government Licence v.3.0. Contains OS data © Crown copyright and database right 2026.

**DATA QUALITY CAVEATS**

- parncp26nw holds Welsh-language names on the 878 Welsh rows only (455 of them the same as the English name); on the 10,664 English rows ONS supplies a single space, not an empty value.
- lad26cd and lad26nm match the May 2025 district codes and names for all 318 districts, so they join directly to adm_ons_lad_boundary_may2025.
- Boundaries are clipped to the coastline (Mean High Water). The district boundaries in uk_baseline reach beyond it, so parish areas total about 98% of district area and fall short in coastal districts.
- Names are not unique: 575 names recur across 1,443 rows, 17 of them within the same district, and 6 rows are named Lands common to followed by two or more parish names. Join on parncp26cd, not the name.
- 363 of the 14,460 polygon parts are smaller than 1 sqm, in 37 rows. They are kept as supplied, not repaired.

**LOADED INTO uk_baseline**

- Loaded by PNC, 14 October 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `gid` | `integer` |  |
| `parncp26cd` | `character varying` | Source field `PARNCP26CD`: parish (E04), non-civil parished area (E43) or Welsh community (W04) code. |
| `parncp26nm` | `character varying` | Source field `PARNCP26NM`: name of the parish, non-civil parished area or community. |
| `parncp26nw` | `character varying` | Source field `PARNCP26NW`; ONS publishes no definition for it with the file. Welsh-language names on Welsh rows (455 of 878 the same as the English name); a single space on English rows, as published. |
| `lad26cd` | `character varying` | Source field `LAD26CD`: local authority district code, 2026 code set. |
| `lad26nm` | `character varying` | Source field `LAD26NM`: local authority district name, 2026. |
| `bng_e` | `integer` | Source field `BNG_E`; ONS publishes no definition for it with the file. Measured: with bng_n it gives a point inside the area, not its centroid. |
| `bng_n` | `integer` | Source field `BNG_N`; ONS publishes no definition for it with the file. Measured: with bng_e it gives a point inside the area, not its centroid. |
| `long` | `real` | Source field `LONG`; ONS publishes no definition for it with the file. |
| `lat` | `real` | Source field `LAT`; ONS publishes no definition for it with the file. |
| `globalid` | `character varying` | Source field `GlobalID`, typed by the ONS ArcGIS service as a GlobalID field; ONS publishes no definition for it with the file. |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry as supplied in the ONS GeoPackage, MultiPolygon in EPSG:27700, full resolution clipped to the coastline (Mean High Water mark). |
