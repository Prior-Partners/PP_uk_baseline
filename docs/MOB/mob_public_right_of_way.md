# Public Rights of Way (PRoW) for England, compiled from local surveying-authority definitive-map open data

<p class="layer-short">Public Rights of Way</p>

`mob_public_right_of_way`<button class="md-clipboard md-icon" data-clipboard-text="mob_public_right_of_way" title="Copy table name" aria-label="Copy table name" data-search-exclude></button>
{: .layer-table }

<img src="../../maps/mob_public_right_of_way.png" alt="Styling preview of mob_public_right_of_way" loading="lazy" class="layer-map layer-map--day"><img src="../../maps/night/mob_public_right_of_way.png" alt="Styling preview of mob_public_right_of_way" loading="lazy" class="layer-map layer-map--night">

**SOURCE**
{: .sec-label }

- Local surveying authorities (local highway authorities) of England, via their published definitive-map / PRoW open data, aggregated through the Public Rights of Way open-data project (osm.mathmos.net/prow). Per-row provenance in authority_name, source_url, source_licence and source_published_date.

**DOCUMENTATION**
{: .sec-label }

- PRoW open data project        : https://osm.mathmos.net/prow/open-data/
- gov.uk Use public rights of way : https://www.gov.uk/right-of-way-open-access-land/use-public-rights-of-way

**DEFINITIONS**
{: .sec-label }

- A public right of way is a highway over which the public has a right to pass and repass. Categories by permitted use (gov.uk): footpaths are "for walking, running, mobility scooters or powered wheelchairs"; bridleways are "for walking, horse riding, bicycles, mobility scooters or powered wheelchairs"; restricted byways are "for any transport without a motor and mobility scooters or powered wheelchairs"; byways open to all traffic are "for any kind of transport, including cars (but they're mainly used by walkers, cyclists and horse riders)." (gov.uk, Use public rights of way)

**SCOPE**
{: .sec-label }

- England. 509,469 rows.

**CRS**
{: .sec-label }

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**
{: .sec-label }

- Per row - see source_licence (observed "Open Government Licence (v3)" and "OS OpenData Licence"). Confirm per authority before re-publication.

**DATA QUALITY CAVEATS**
{: .sec-label }

- The row count counts split pieces, not source features: this layer was split by Middle Layer Super Output Area, so it holds one row per feature per MSOA piece, plus whole and remainder rows to keep 100% of the source geometry. 554,975 rows represent 508,819 source features, measured 25 August 2026. `source_fid` identifies the originating feature.
- Geography keys are NULL on 1,804 of 554,975 rows, measured 25 August 2026: 1,258 fall inside an England or Wales district and could carry one, so their keys are a gap rather than an absence; 365 are residual fragments left by the MSOA split, each under 100 sqm or 10 m; 7 are in Scotland or Northern Ireland, outside the England and Wales lookup; 174 fall outside every district — offshore, inter-tidal, or beyond Great Britain.
- County and Spatial Development Strategy columns are England and Wales only; rows elsewhere carry no county or SDS. Wales and the Isles of Scilly carry a county but no SDS. Rows with no Local Authority District code are NULL in all four columns.
- Compiled from many surveying authorities; completeness, attribute conventions and update dates vary by authority (see authority_name, source_published_date, update_date).

**ENRICHMENT**
{: .sec-label }

- `sds_name` / `sds_group` — Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy, joined at load on the row's Local Authority District 2025 code via uk.ref_lad25_ctyua25_sds_lu_jul2026.

**LOADED INTO uk_baseline**
{: .sec-label }

- Loaded by PNC, May 2026.

MSOA SPLIT (added 4 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Geometry outside every MSOA (offshore or outside England & Wales) is retained as rows with NULL geography columns, so the layer holds the complete source geometry.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.mob_public_right_of_way__preswap_jul04 (non-unique here: a feature spanning N MSOAs has N rows). |
| `authority_gss` | `text` | Source field; surveying authority ONS GSS code. |
| `authority_name` | `text` | Source field; surveying authority name (e.g. "Barnsley", "Bedford"). |
| `prow_ref` | `text` | Source field; the authority's PRoW reference for the segment. |
| `prow_type_norm` | `text` | Normalised PRoW type. Observed values: "footpath", "bridleway", "restricted_byway", "boat" (byway open to all traffic), "cycle_track", "other". |
| `prow_type_raw` | `text` | Source field; the authority's raw PRoW type value before normalisation. |
| `length_m` | `double precision` | Length in metres. |
| `source_url` | `text` | Source field; URL of the authority's source dataset for this segment. |
| `source_licence` | `text` | Source field; licence of the authority's source data. Observed values: "Open Government Licence (v3)", "OS OpenData Licence". |
| `source_published_date` | `date` | Source field; publication date of the authority's source data. |
| `source_sha256` | `text` | SHA-256 checksum of the source file the segment was loaded from. |
| `update_date` | `text` | Date the segment was loaded or last updated in uk_baseline. |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiLineString,27700)` | LineString in EPSG:27700. PRoW segment geometry. |
| `gid` | `bigint` |  |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
