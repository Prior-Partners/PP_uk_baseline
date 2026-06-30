# MHCLG English Enterprise Zone site boundaries, March 2016

<p class="layer-short">English Enterprise Zone Sites</p>

`ecn_mhclg_english_enterprise_zone_sites_mar2016`

<img src="../../maps/ecn_mhclg_english_enterprise_zone_sites_mar2016.png" alt="Styling preview of ecn_mhclg_english_enterprise_zone_sites_mar2016" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Ministry of Housing, Communities and Local Government (MHCLG), distributed via data.gov.uk dataset "English Enterprise Zone Sites" (publication 17 March 2016).

**DOCUMENTATION**

- Dataset landing page : https://www.data.gov.uk/dataset/9244b0fe-23ce-4d1c-895b-5716b441c4df/english-enterprise-zone-sites
- Enterprise Zones programme : https://www.gov.uk/guidance/enterprise-zones

**DEFINITIONS**

- "Enterprise Zones are designated areas aimed at stimulating economic growth by offering incentives to businesses to establish or expand their operations within them." (gov.uk "Enterprise Zones" guidance)
- Programme context: zones announced March 2011 and rolled out from 2012 onwards; the March 2016 dataset captures the position at that point with 48 zones operational.

**SCOPE**

- England. 535 polygon site features across 48 Enterprise Zones as of 17 March 2016.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Ordnance Survey Public Sector End User Licence - INSPIRE (per the data.gov.uk dataset metadata). Not standard Open Government Licence v3.0; check downstream re-use terms against the OS Public Sector / INSPIRE licence wording.

**DATA QUALITY CAVEATS**

- Geometry is MultiPolygonZ (carries Z coordinates inherited from the source shapefile). Z values are not analytically meaningful for these polygons; treat as 0 for any height-related use.
- This is a 2016 snapshot. The Enterprise Zones programme has since been extended (further zones added in 2016-2017) and some zones have wound down. Does not represent the current position.
- `date_start` is stored as text (varchar(20)), not a typed date.

**ENRICHMENT**

- `msoa21hclnm` — House of Commons Library readable MSOA name, assigned at load via the polygon's 2021 MSOA (representative interior point in uk_baseline.adm_ons_msoa_boundary_2021). Open Parliament Licence.

**UPDATE REQUIRED**

- This dataset is a 2016 release of an ongoing programme. The current Enterprise Zones position is published via gov.uk and the Cities and Local Growth Unit. If a current-edition layer is needed, refresh from the latest publication.

**LOADED INTO uk_baseline**

- Loaded by PNC, March 2026.

MSOA SPLIT (added 30 June 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key.
- Features lying within a single MSOA are kept whole (one row, primary-tagged); only features spanning more than one MSOA are split into per-MSOA pieces.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `ez` | `character varying(50)` |  |
| `shape_leng` | `double precision` |  |
| `shape_area` | `double precision` |  |
| `brd` | `character varying(5)` |  |
| `brr` | `character varying(5)` |  |
| `eca` | `character varying(5)` |  |
| `ldo` | `character varying(5)` |  |
| `ez_website` | `character varying(75)` |  |
| `sectors` | `character varying(150)` |  |
| `subez` | `character varying(50)` |  |
| `date_start` | `character varying(20)` |  |
| `ons_ez_cod` | `character varying(10)` |  |
| `poly_name` | `character varying(75)` |  |
| `desig_site` | `character varying(75)` |  |
| `msoa21cd` | `text` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `text` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` |  |
| `source_fid` | `integer` | Primary key of the source feature in the pre-split layer uk.ecn_mhclg_english_enterprise_zone_sites_mar2016__preswap_jun30 (non-unique here: a feature spanning N MSOAs has N rows). |
| `gid` | `bigint` |  |
