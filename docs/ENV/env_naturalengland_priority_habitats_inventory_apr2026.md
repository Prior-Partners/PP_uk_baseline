# Natural England Priority Habitats Inventory (England), April 2026

<p class="layer-short">Priority Habitats Inventory</p>

`env_naturalengland_priority_habitats_inventory_apr2026`

<img src="../../maps/env_naturalengland_priority_habitats_inventory_apr2026.png" alt="Styling preview of env_naturalengland_priority_habitats_inventory_apr2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Natural England, via the NE Open Data Hub. Priority Habitats Inventory (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/
- data.gov.uk PHI  : https://www.data.gov.uk/dataset/4b6ddab7-6c0f-4407-946e-d6499f19fcde/priority-habitats-inventory-england

**DEFINITIONS**

- "The Priority Habitat Inventory is a spatial dataset that maps priority habitats identified in the UK Biodiversity Action Plan" - habitats "listed as being of principal importance for the purpose of conserving or enhancing biodiversity, under Section 41 of the Natural Environment and Rural Communities Act (2006)." (data.gov.uk, Priority Habitats Inventory (England), Natural England)

**SCOPE**

- England. 910,679 rows.

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
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_naturalengland_priority_habitats_inventory_apr2026__preswap (non-unique here: a feature spanning N MSOAs has N rows). |
| `fid_original` | `integer` | Original source feature identifier, preserved at load. |
| `mainhabs` | `character varying` | Source field `mainhabs`; main priority habitat type(s) for the parcel. |
| `habcodes` | `character varying` | Source field `habcodes`; priority habitat code(s) (e.g. "DWOOD" deciduous woodland, "SALTM" saltmarsh, "UHEAT"/"LHEAT" upland/lowland heath). |
| `featdesc` | `character varying` | Source field `featdesc`; feature description / habitat detail (often blank). |
| `featcodes` | `character varying` | Source field `featcodes`; feature code(s) (often blank). |
| `otherclass` | `character varying` | Source field `otherclass`; other classifications, e.g. Annex I or Phase 1 habitat codes (often blank). |
| `addhabs` | `character varying` | Source field `addhabs`; additional habitat(s) recorded for the parcel. |
| `primsource` | `character varying` | Source field `primsource`; primary data source of the habitat mapping. |
| `areaha` | `double precision` | Source field `areaha`; area of the whole source feature in hectares. |
| `version` | `character varying` | Source field `version`; inventory version. |
| `uid` | `character varying` | Source field `uid`; unique feature identifier from the source. |
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
| `geom` | `geometry(MultiPolygon,27700)` | Priority habitat polygon geometry in EPSG:27700 (British National Grid); one part per MSOA (2021) after the split. |
| `gid` | `bigint` | Surrogate primary key, added at the MSOA split (see ENRICHMENT). |
