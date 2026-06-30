# OS OpenMap Local Functional Sites - polygon features for sites of functions or activities, October 2024

<p class="layer-short">Functional Sites</p>

`blt_os_functional_sites_oct2024`

<img src="../../maps/blt_os_functional_sites_oct2024.png" alt="Styling preview of blt_os_functional_sites_oct2024" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Ordnance Survey (OS), Open Map Local product.

**DOCUMENTATION**

- Product page : https://osdatahub.os.uk/data/downloads/open/OpenMapLocal
- Product guide : https://www.ordnancesurvey.co.uk/documents/os-open-map-local-product-guide.pdf

**DEFINITIONS**

- "A polygon feature that represents the area or extent of certain types of function or activity with appropriate attribution." (OS OpenMap Local Product Guide, Land Use / FunctionalSite)
- "Each site has a theme, classification and is named (where appropriate)." (OS OpenMap Local Product Guide, Functional Sites)

**SCOPE**

- Great Britain (England, Wales, Scotland).
- 37,618 distinct functional sites (by id_original) represented across 46,532 polygon rows (avg ratio ~1.24 - most sites are single polygons; a small fraction are multipolygon sites that have been exploded).

**CRS**

- EPSG:27700 (British National Grid / BNG).

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data (c) Crown copyright and database right [year]" required).

**DATA QUALITY CAVEATS**

- id_original is NOT strictly unique per row - 37,618 distinct values across 46,532 rows. Multipolygon sites have been exploded at load.
- lad22cd / lad22nm are NULL for Scottish sites in this load.

**ENRICHMENT**

- `msoa21hclnm` — House of Commons Library readable MSOA name, assigned at load via the polygon's 2021 MSOA (representative interior point in uk_baseline.adm_ons_msoa_boundary_2021). Open Parliament Licence.
- lad22cd, lad22nm : spatial intersect with ONS 2022 LAD boundaries. NULL for Scottish sites in this load.
- wd21cd, wd21nm : spatial intersect with ONS 2021 Ward boundaries (Scottish S-codes populated where applicable).
- area_ha : derived from geom at load (area in hectares, computed from the geometry at load).

**LOADED INTO uk_baseline**

- Loaded October 2024.

MSOA SPLIT (added 30 June 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key.
- Features lying within a single MSOA are kept whole (one row, primary-tagged); only features spanning more than one MSOA are split into per-MSOA pieces.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `classification` | `character varying` |  |
| `distinctive_name` | `character varying` |  |
| `feature_code` | `integer` |  |
| `site_theme` | `character varying` |  |
| `id_original` | `character varying` |  |
| `wd21nm` | `character varying` |  |
| `wd21cd` | `character varying` |  |
| `area_ha` | `double precision` |  |
| `msoa21cd` | `text` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `text` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `character varying` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `character varying` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` |  |
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.blt_os_functional_sites_oct2024__preswap_jun30 (non-unique here: a feature spanning N MSOAs has N rows). |
| `gid` | `bigint` |  |
