# uk_baseline data catalogue

A plain-English, browsable catalogue of every spatial layer held in the
`uk_baseline` database — what each layer is, where it came from, its licence,
and a description of every column.

**Browse the catalogue:** https://ponienchenpp.github.io/PP_uk_baseline/

## What this is

The catalogue is **generated automatically** from each database table's own
documentation, so it always reflects the live data. Each layer page shows:

- a one-line description (source organisation, what it is, edition date);
- where the data came from (source, documentation links, licence);
- the area and level of detail it covers;
- a table of every column with its meaning and units.

Layers are grouped into themes (Administrative & Planning Boundaries, Built
Environment & Land Use, Demographics & Socio-Economic, and so on).

## How it is built

The site is a [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
project. The page content under `docs/` is produced by an internal generator
from the database metadata — please do not hand-edit it; changes are made in
the database and the catalogue is regenerated.

To preview locally:

```bash
pip install mkdocs-material
mkdocs serve
```

To rebuild and publish:

```bash
mkdocs gh-deploy
```
