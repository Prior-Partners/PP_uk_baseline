# Defra - Department for Environment, Food and Rural Affairs — Environment Agency Historic Landfill Sites for England

<p class="layer-short">Historic Landfill Site</p>

`env_defra_historic_landfill_site`

<img src="../../maps/env_defra_historic_landfill_site.png" alt="Styling preview of env_defra_historic_landfill_site" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Environment Agency (EA), part of the Department for Environment, Food and Rural Affairs (Defra). Historic Landfill dataset.

**DOCUMENTATION**

- EA Historic Landfill dataset (data.gov.uk) : https://www.data.gov.uk/dataset/17edf94f-6de3-4034-b66b-004ebd0dd010/historic-landfill-sites
- EA dataset record (env data portal)        : https://environment.data.gov.uk/dataset/17edf94f-6de3-4034-b66b-004ebd0dd010

**DEFINITIONS**

- "This data is a national historic landfill dataset that defines the location of and provides specific attributes for known historic landfill sites." (data.gov.uk Summary)
- "An historic landfill is a site where there is no environmental permit in force." (data.gov.uk Summary)

**SCOPE**

- England. 25,187 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0. © Environment Agency.

**ENRICHMENT**

- `msoa21hclnm` — House of Commons Library readable MSOA name, assigned at load via the polygon's 2021 MSOA (representative interior point in uk_baseline.adm_ons_msoa_boundary_2021). Open Parliament Licence.

MSOA SPLIT (added 30 June 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key.
- Features lying within a single MSOA are kept whole (one row, primary-tagged); only features spanning more than one MSOA are split into per-MSOA pieces.
- Keep-everything (3 July 2026): geometry outside every MSOA — offshore, estuarine, or beyond the generalised coastline — is retained as rows with NULL geography columns (source_fid links the parts), so the layer holds the complete source geometry.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `hld_ref` | `character varying` |  |
| `site_name` | `character varying` |  |
| `site_add` | `character varying` |  |
| `ea_wmlr` | `integer` |  |
| `regis_no` | `character varying` |  |
| `wrc_ref` | `character varying` |  |
| `bgs_num` | `character varying` |  |
| `site_ref` | `character varying` |  |
| `lic_hold` | `character varying` |  |
| `licholdadd` | `character varying` |  |
| `siteopname` | `character varying` |  |
| `siteopadd` | `character varying` |  |
| `os_prefix` | `character varying` |  |
| `easting` | `integer` |  |
| `northing` | `integer` |  |
| `ea_region` | `character varying` |  |
| `ea_area` | `character varying` |  |
| `lic_issue` | `timestamp without time zone` |  |
| `lic_surren` | `timestamp without time zone` |  |
| `firstinput` | `timestamp without time zone` |  |
| `lastinput` | `timestamp without time zone` |  |
| `inert` | `character varying` |  |
| `industrial` | `character varying` |  |
| `commercial` | `character varying` |  |
| `household` | `character varying` |  |
| `special` | `character varying` |  |
| `liqsludge` | `character varying` |  |
| `wasteunk` | `character varying` |  |
| `gascontrol` | `character varying` |  |
| `leachatcnt` | `character varying` |  |
| `exempt` | `character varying` |  |
| `licenced` | `character varying` |  |
| `nolicreq` | `character varying` |  |
| `buff_point` | `character varying` |  |
| `gdb_geomattr_data` | `character varying` |  |
| `id_original` | `character varying` |  |
| `wd21nm` | `character varying` |  |
| `wd21cd` | `character varying` |  |
| `area_ha` | `double precision` |  |
| `fid` | `bigint` |  |
| `msoa21cd` | `text` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `text` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `character varying` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `character varying` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` |  |
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_defra_historic_landfill_site__preswap_jun30 (non-unique here: a feature spanning N MSOAs has N rows). |
| `gid` | `bigint` |  |
