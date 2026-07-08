# Natural England Areas of Outstanding Natural Beauty (AONB) for England, November 2024

<p class="layer-short">Areas of Outstanding Natural Beauty (AONB)</p>

`env_naturalengland_aonb_nov2024`

<img src="../../maps/env_naturalengland_aonb_nov2024.png" alt="Styling preview of env_naturalengland_aonb_nov2024" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Natural England, via the NE Open Data Hub. Areas of Outstanding Natural Beauty (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/
- AONB designation : https://www.gov.uk/guidance/areas-of-outstanding-natural-beauty-aonbs-designation-and-management

**DEFINITIONS**

- "An area of outstanding natural beauty (AONB) is land protected by the Countryside and Rights of Way Act 2000 (CROW Act). It protects the land to conserve and enhance its natural beauty." (gov.uk, AONB designation and management)
- "'National Landscapes' is the rebranded name for areas of outstanding natural beauty (AONBs). This name change is not statutory." (gov.uk, Protected Landscapes Duty guidance)

**SCOPE**

- England. 1,290 rows (multiple polygon rows per AONB; 33 named AONBs).

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**ENRICHMENT**

- Geometry split to one row per source feature per MSOA (2021).
- Each row carries that MSOA's `msoa21cd`, `msoa21nm`, `msoa21hclnm`, `lad22cd`, `lad22nm`, `lad25cd`, `lad25nm`.
- The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key.
- Geometry outside every MSOA (offshore, estuarine, or beyond the coastline) is kept as rows with NULL geography columns, so the layer holds the complete source geometry.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_naturalengland_aonb_nov2024__preswap_jul03 (non-unique here: a feature spanning N MSOAs has N rows). |
| `fid_original` | `integer` | Original source feature identifier, preserved at load. |
| `code` | `character varying` | Source field `code`; AONB identifier code (e.g. "7" Cotswolds, "14" High Weald). |
| `name` | `character varying` | Source field `name`; AONB / National Landscape name (e.g. "Cotswolds", "Kent Downs"). |
| `desig_date` | `character varying` | Source field `desig_date`; designation date as month-year text (e.g. "Aug-66"). |
| `hotlink` | `character varying` | Source field `hotlink`; URL of the AONB / National Landscape body's website. |
| `stat_area` | `double precision` | Source field `stat_area`; statutory area of the whole AONB designation, as recorded in the source. |
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
| `geom` | `geometry(MultiPolygon,27700)` | Areas of Outstanding Natural Beauty polygon geometry in EPSG:27700 (British National Grid); one part per MSOA (2021) after the split. |
| `gid` | `bigint` | Surrogate primary key, added at the MSOA split (see ENRICHMENT). |
