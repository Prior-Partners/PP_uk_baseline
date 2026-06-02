# Catalogue generator scripts

The scripts that build the `uk_baseline` catalogue and its per-layer preview
maps. Committed here for reproducibility — they read the live PostGIS database
and regenerate everything the site publishes.

> **Note:** the maintainer's working copy currently lives outside this repo (in
> the `uk_baseline` working directory under `scripts/catalogue/`). This folder is
> the version-controlled snapshot; keep the two in sync, or consolidate onto this
> copy as the single source.

## Scripts

| Script | What it does |
|---|---|
| `build_catalogue.py` | Reads the live `uk_baseline` schema metadata and regenerates the Excel workbook, the standalone HTML, and the MkDocs `docs/` pages. |
| `build_maps.py` | Renders a standalone interactive Leaflet/folium preview map per layer to `catalogue/docs/maps/<table>.html`. Points and coloured polygons render at full England extent; dense layers are sampled; lines/coverage stay windowed. |
| `suggest_colour_by.py` | Read-only helper: writes `colour_by_candidates.md`, a shortlist of candidate colour-by columns per single-colour layer (from `pg_stats`, no table scans). |

## Connection

All three read PostGIS connection settings from a `.env` file (`PG_HOST`,
`PG_PORT`, `PG_DATABASE`, `PG_USER`, `PG_PASSWORD`). The path defaults to the
maintainer's local `.env`; override it on any machine with:

```bash
export UK_BASELINE_ENV=/path/to/.env      # PowerShell: $env:UK_BASELINE_ENV="..."
```

The database uses SSPI/Kerberos with an empty password — leave `PG_PASSWORD`
blank and the `password=` token is omitted from the connection string.

## Dependencies

`psycopg`, `python-dotenv`, `folium`, `branca` (maps); `openpyxl` (Excel).

## Refresh + deploy

```bash
python build_catalogue.py        # Excel + HTML + docs/  (only if layer metadata changed)
python build_maps.py             # (re)render all preview maps to docs/maps/
cd ..                            # into catalogue/
python -m mkdocs gh-deploy --force   # publish docs/ (incl. maps from disk) to gh-pages
```

For a maps-only change, skip `build_catalogue.py` and just re-render + `gh-deploy`.
