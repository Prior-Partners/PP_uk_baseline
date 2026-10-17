# Catalogue generator scripts

The scripts that build the `uk_baseline` catalogue. They read the live PostGIS
database (read only) and regenerate everything the site publishes.

> **Single source:** `build_catalogue.py` and `assets/` in this folder are the
> generator's single source. The maintainer's older working copy (in the
> `uk_baseline` working directory under `scripts/catalogue/`) is kept unchanged
> until the switch-over, when it becomes a small shim that calls this copy.
> `build_maps.py` here is an older snapshot of the working copy (16 October 2026).

## Scripts

| Script | What it does |
|---|---|
| `build_catalogue.py` | Reads the live `uk_baseline` schema metadata and regenerates the Excel workbook and the standalone HTML on the practice share, and the MkDocs `docs/` pages and `mkdocs.yml` here. |
| `assets/` | The site skin: `extra.css` and the GT America `fonts/`, copied into `docs/` on every build. Edit the skin here, never in `docs/`. |
| `build_maps.py` | Older snapshot of the preview-map renderer. The live previews are static PNGs, `docs/maps/<table>.png`, rendered outside this repo. |
| `suggest_colour_by.py` | Read-only helper: writes `colour_by_candidates.md`, a shortlist of candidate colour-by columns per single-colour layer (from `pg_stats`, no table scans). |
| `dev/` | Development checks (for example `parity_t01.py`, which proves this copy renders exactly what the old working copy renders). Never part of a refresh. |

## Options of `build_catalogue.py`

With no options it runs the full refresh, exactly as before.

| Option | Effect |
|---|---|
| `--site-only` | Writes only `docs/`, `mkdocs.yml` and `.catalogue_fingerprint.json`. The Excel and HTML on the share are never written. Use it for every development build. |
| `--out-dir <folder>` | Writes `docs/`, `mkdocs.yml` and the fingerprint into another folder (default: this repository). |
| `--maps-dir <folder>` | Reads the preview PNGs from another folder (default: `docs/maps/`). |
| `--save-snapshot <json>` | Saves the exact render inputs — records with short names, approved themes, the map list and the build date. Keep the file outside this public repository. |
| `--from-snapshot <json>` | Renders from a saved snapshot: no database, register or styles file is read. |
| `--built "<DD Month YYYY>"` | The "last updated" date (default: the snapshot's date, else today). |

Example development build (nothing on the share is touched):

```bash
python scripts/build_catalogue.py --site-only --save-snapshot <work>/records.json   # one database read
python scripts/build_catalogue.py --from-snapshot <work>/records.json --site-only   # any later build
python -m mkdocs build --strict -d <work>/site
```

`<work>` is any folder outside this repository.

## Connection

The database readers take PostGIS connection settings from a `.env` file
(`PG_HOST`, `PG_PORT`, `PG_DATABASE`, `PG_USER`, `PG_PASSWORD`). The path defaults
to the maintainer's local `.env`; override it on any machine with:

```bash
export UK_BASELINE_ENV=/path/to/.env      # PowerShell: $env:UK_BASELINE_ENV="..."
```

The database uses SSPI/Kerberos with an empty password — leave `PG_PASSWORD`
blank and the `password=` token is omitted from the connection string. The
session is opened read only.

## Dependencies

`psycopg`, `python-dotenv`, `openpyxl`; `pytest` for the tests in `tests/`.

## Tests

```bash
python -m pytest tests -q
```

## Refresh + deploy

```bash
python scripts/build_catalogue.py        # Excel + HTML on the share + docs/ (only if layer metadata changed)
python -m mkdocs gh-deploy --force       # publish docs/ (incl. maps from disk) to gh-pages
```

For a maps-only change, re-render the previews and run `gh-deploy`.
