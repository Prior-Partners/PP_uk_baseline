# OpenStreetMap roads for Great Britain, May 2025

<p class="layer-short">Roads</p>

`mob_osm_roads_may2025`<button class="md-clipboard md-icon" data-clipboard-text="mob_osm_roads_may2025" title="Copy table name" aria-label="Copy table name" data-search-exclude></button>
{: .layer-table }

<img src="../../maps/mob_osm_roads_may2025.png" alt="Styling preview of mob_osm_roads_may2025" loading="lazy" class="layer-map layer-map--day"><img src="../../maps/night/mob_osm_roads_may2025.png" alt="Styling preview of mob_osm_roads_may2025" loading="lazy" class="layer-map layer-map--night">

**SOURCE**
{: .sec-label }

- OpenStreetMap contributors, distributed as a roads extract (Geofabrik). The fclass road categories derive from OpenStreetMap highway tags.

**DOCUMENTATION**
{: .sec-label }

- OpenStreetMap       : https://www.openstreetmap.org/about
- Geofabrik downloads : https://download.geofabrik.de/

**DEFINITIONS**
{: .sec-label }

- OpenStreetMap is "the project that creates and distributes free geographic data for the world." (OpenStreetMap Wiki)

**SCOPE**
{: .sec-label }

- Great Britain. 6,431,723 rows.

**CRS**
{: .sec-label }

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**
{: .sec-label }

- Open Database Licence (ODbL). (c) OpenStreetMap contributors.

MSOA SPLIT (added 4 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Geometry outside every MSOA (offshore or outside England & Wales) is retained as rows with NULL geography columns, so the layer holds the complete source geometry.

**DATA QUALITY CAVEATS**
{: .sec-label }

- The row count counts split pieces, not source features: this layer was split by Middle Layer Super Output Area, so it holds one row per feature per MSOA piece, plus whole and remainder rows to keep 100% of the source geometry. 6,777,436 rows represent 6,430,883 source features, measured 25 August 2026. `source_fid` identifies the originating feature.
- Geography keys are NULL on 10,097 of 6,777,436 rows, measured 25 August 2026: 5,831 fall inside an England or Wales district and could carry one, so their keys are a gap rather than an absence; 3,687 are residual fragments left by the MSOA split, each under 100 sqm or 10 m; 544 are in Scotland or Northern Ireland, outside the England and Wales lookup; 35 fall outside every district — offshore, inter-tidal, or beyond Great Britain.
- County and Spatial Development Strategy columns are England and Wales only; rows elsewhere carry no county or SDS. Wales and the Isles of Scilly carry a county but no SDS. Rows with no Local Authority District code are NULL in all four columns.

**ENRICHMENT**
{: .sec-label }

- `sds_name` / `sds_group` — Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy, joined at load on the row's Local Authority District 2025 code via uk.ref_lad25_ctyua25_sds_lu_jul2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.mob_osm_roads_may2025__preswap_jul04 (non-unique here: a feature spanning N MSOAs has N rows). |
| `osm_id` | `character varying(12)` | Source field "osm_id"; OpenStreetMap feature identifier. |
| `code` | `integer` | Source field "code"; Geofabrik numeric road-class code. |
| `fclass` | `character varying(28)` | Source field "fclass"; road class derived from the OpenStreetMap highway tag. Observed values include "service", "footway", "residential", "unclassified", "track", "path", "tertiary", "cycleway", "primary", "trunk". |
| `name` | `character varying(100)` | Source field "name"; road name. |
| `ref` | `character varying(20)` | Source field "ref"; road reference number. |
| `oneway` | `character varying(1)` | Source field "oneway"; one-way indicator. |
| `maxspeed` | `integer` | Source field "maxspeed"; maximum speed as tagged in OpenStreetMap. |
| `layer` | `bigint` | Source field "layer"; relative vertical layer (OpenStreetMap layer tag). |
| `bridge` | `character varying(1)` | Source field "bridge"; bridge indicator. |
| `tunnel` | `character varying(1)` | Source field "tunnel"; tunnel indicator. |
| `id_original` | `integer` | Original feature id preserved at load. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `length_m` | `double precision` | Length in metres. |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiLineString,27700)` | LineString in EPSG:27700. Road centreline geometry. |
| `gid` | `bigint` |  |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
