# Natural England Sites of Special Scientific Interest (SSSI) for England, April 2026

<p class="layer-short">Sssi</p>

`env_naturalengland_sssi_apr2026`

<img src="../../maps/env_naturalengland_sssi_apr2026.png" alt="Styling preview of env_naturalengland_sssi_apr2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Natural England, via the NE Open Data Hub. Sites of Special Scientific Interest (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub     : https://naturalengland-defra.opendata.arcgis.com/
- gov.uk SSSI guidance : https://www.gov.uk/guidance/protected-areas-sites-of-special-scientific-interest

**DEFINITIONS**

- "Natural England will 'notify' (or designate) the land as a site of special scientific interest (SSSI)" when "it believes the site has features of special interest, such as its: wildlife, geology, landform." (gov.uk, Protected areas: sites of special scientific interest)

**SCOPE**

- England. 8,810 rows across 4,128 distinct reference codes.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**ENRICHMENT**

- Geometry split to one row per source feature per MSOA (2021).
- Each row carries that MSOA's `msoa21cd`, `msoa21nm`, `msoa21hclnm`, `lad22cd`, `lad22nm`, `lad25cd`, `lad25nm`.
- The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key.
- Features with no MSOA overlap (offshore or outside England & Wales) are kept whole, with NULL geography columns.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_naturalengland_sssi_apr2026__preswap_jul03 (non-unique here: a feature spanning N MSOAs has N rows). |
| `fid_original` | `integer` | Original source feature identifier, preserved at load. |
| `ref_code` | `character varying` | Source field `ref_code`; Natural England SSSI reference code. |
| `name` | `character varying` | Source field `name`; SSSI name (e.g. "South Pennine Moors SSSI"). |
| `measure` | `double precision` | Source field `measure`; SSSI area as published. Unit: hectares. |
| `label` | `character varying` | Source field `label`; display label (e.g. "South Pennine Moors (SSSI)"). |
| `hyperlink` | `character varying` | Source field `hyperlink`; URL of the SSSI page (often blank). |
| `contact_no` | `character varying` | Source field `contact_no`; contact reference number. |
| `globalid` | `character varying` | Source field `GlobalID`; Esri global identifier of the source feature. |
| `area_ha` | `double precision` | Area of this row's geometry in hectares. |
| `rgn22cd` | `text` | Region 2022 GSS code (nine English regions), assigned via the ONS Region lookup. Open Government Licence v3.0. |
| `rgn22nm` | `text` | Region 2022 name, assigned via the ONS Region lookup. Open Government Licence v3.0. |
| `sds_boundary` | `text` | Spatial Development Strategy (SDS) area the feature falls in. NULL outside any SDS area. |
| `layer` | `character(100)` | Source field `layer`; source layer name. |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` | Site of Special Scientific Interest polygon geometry in EPSG:27700 (British National Grid); one part per MSOA (2021) after the split. |
| `gid` | `bigint` | Surrogate primary key, added at the MSOA split (see ENRICHMENT). |
