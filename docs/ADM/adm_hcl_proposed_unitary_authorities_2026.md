# House of Commons Library boundaries of the new unitary authorities proposed by the government in 2026, England, August 2026

<p class="layer-short">Proposed Unitary Authorities 2026</p>

`adm_hcl_proposed_unitary_authorities_2026`

**SOURCE**

- House of Commons Library (HCL), research briefing CBP-10608, Proposed unitary authorities 2026: Maps, published 18 August 2026, page updated 11 September 2026. File proposed_unitary_authorities_2.gpkg (19,308,544 bytes), layer merged, loaded as published.

**DOCUMENTATION**

- Proposed unitary authorities 2026: Maps   : https://commonslibrary.parliament.uk/research-briefings/cbp-10608/
- GeoPackage download                      : https://researchbriefings.files.parliament.uk/documents/CBP-10608/proposed_unitary_authorities_2.gpkg
- ONS administrative geography, England    : https://www.ons.gov.uk/methodology/geography/ukgeographies/administrativegeography/england
- Open Parliament Licence                  : https://www.parliament.uk/site-information/copyright-parliament/open-parliament-licence/

**DEFINITIONS**

- "This page contains maps of the new unitary authorities proposed by the government in 2026." (House of Commons Library, CBP-10608)
- Unitary authorities are single-tier administrations with responsibility for all areas of local government (ONS administrative geography page, England).

**SCOPE**

- England only: 55 rows, one per proposed unitary authority, in 19 county areas (column area): Derbyshire, Devon, East Sussex, Essex, Gloucestershire, Hampshire, Hertfordshire, Kent, Lancashire, Leicestershire, Lincolnshire, Norfolk, Nottinghamshire, Oxfordshire, Staffordshire, Suffolk, Surrey, Warwickshire, Worcestershire. The rest of England, including the Isle of Wight, has no row.

**CRS**

- EPSG:27700 (British National Grid), as supplied in the GeoPackage. No reprojection.

**LICENCE**

- Open Parliament Licence v3.0. Attribution required: Contains Parliamentary information licensed under the Open Parliament Licence v3.0.

**DATA QUALITY CAVEATS**

- Proposed boundaries, not legal ones. On 7 September 2026 the government withdrew its decisions for Essex, Suffolk, Norfolk, and Hampshire and the Isle of Wight (15 of the 55 rows: area Essex, Suffolk, Norfolk and Hampshire); the decisions for all other areas are under review (House of Commons Library page note).
- The column area holds the county area name (for example Essex), not a size.
- The Library corrected the Lincoln boundary on 4 August 2026 to include Metheringham ward; this file includes the correction, checked at load.
- On the coast the outlines run to low water (the extent of the realm), not to the coastline.
- 26 pairs of proposed authorities overlap slightly as supplied (largest 7.7 ha, 5 over 2 ha). They are not repaired.

**UPDATE REQUIRED**

- Yes. The status of these proposals is changing (withdrawals of 7 September 2026 and a review of the rest). Check the Library page before use and reload if the Library republishes the file.

**NOT IN THIS DATASET**

- The populations and areas in square kilometres shown on the Library's interactive map are not in the file.
- The Library's parish and ward lookup spreadsheet for the proposed authorities is not loaded.

**LOADED INTO uk_baseline**

- Loaded by PNC, 14 October 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `gid` | `integer` |  |
| `name` | `character varying` | Source field `Name`; the House of Commons Library publishes no field definitions. Values are the names of the proposed unitary authorities, for example Greater Norwich. |
| `area` | `character varying` | Source field `Area`; the House of Commons Library publishes no field definitions. Values are county area names, for example Essex, not a size. |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry as supplied in the House of Commons Library GeoPackage, MultiPolygon in EPSG:27700. |
