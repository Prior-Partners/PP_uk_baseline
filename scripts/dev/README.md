# Catalogue development checks

These standard-library scripts check built MkDocs sites and the approved colour
tokens. They do not run the generator, access the database or change site inputs.
Python 3.13 is the project interpreter; no extra packages are needed by the scripts.

## Built-site preservation

```powershell
python scripts/dev/check_site.py <baseline_site> <candidate_site> --report <report.md>
python scripts/dev/check_site.py <baseline_site> <candidate_site> --labels <labels.json> --report <report.md>
```

Both inputs must be built site folders with `index.html` and
`search/search_index.json`, not source folders or `mkdocs.yml`. The checks are:

- Search: `config` equality and exact `json.dumps(docs, ensure_ascii=False,
  sort_keys=True)` equality. Array order, case, whitespace and punctuation stay
  significant. Reports identify missing/added locations, changed titles/text and
  their first differing character with surrounding excerpts. Duplicate locations
  are compared by occurrence; extra document fields and location order are checked.
- Routes: the set of relative `*.html` paths, including `404.html` if present.
- Navigation: links and section labels inside `nav.md-nav--primary` on every
  route present in both sites, in document order, including active sections and
  integrated tables of contents. Link hrefs are compared exactly. The home page
  must contain exactly one primary nav. Counts total entries across all pages;
  differences identify the route and entry index.
  Nested inline text and HTML entities are decoded and whitespace is collapsed.
  Drawer titles without `md-nav__link` and navigation outside the primary nav are
  excluded. This is an HTML check, not a browser visibility/computed-style check.
- Headings: the ordered ids on `h1`–`h6` inside each page's `article` elements.
- Map references: every map PNG image reference on each page, including duplicate
  references. Local relative URLs resolve against that page; query strings and
  fragments are ignored because they address the same file. External URLs remain
  exact. Reference order is checked as well as the page and target.
- Assets: streamed SHA-256 hashes and file sets for `maps/*.png` and
  `fonts/*.woff2`, including unreferenced files. The production baseline has four
  fonts; the checker compares whatever files each baseline actually contains.

Labels must be identical unless explicitly allowed with a UTF-8 JSON mapping
(with or without a byte-order mark):

```json
{
  "📕 Staff Handbook (PDF)": "Staff handbook (PDF) ↗"
}
```

Use exact, whitespace-collapsed baseline and candidate labels as keys and values.
Mappings permit a change; they do not require it. They never permit changed hrefs,
reordered navigation or other text changes. The caller must supply only approved
display-label renamings; there is no implicit allow-list.

Stdout contains eight one-line PASS/FAIL summaries with baseline, candidate and
difference counts. The nav-label summary also counts `permitted` changes (each
occurrence on each route) and `unused` mappings. A mapping is used only when it
permits an actual label change at the same entry kind and href; unchanged labels,
including identity mappings, leave it unused. Unused mappings are information only.
`--report` lists differences, permitted changes and unused mappings in Markdown. Its parent folder
must already exist, and the report must be outside both sites and must not replace
the label mapping. An existing report is replaced. Exit codes: **0** parity,
**1** preservation differences, **2** invalid input/arguments or report I/O errors.
Missing/added maps, fonts or routes are preservation differences, not input errors.
Errors are written to stderr. The checker does not validate image/font decoding or
compare arbitrary HTML body text outside the specified invariants; indexed text is
covered by search parity.

## Token contrast

```powershell
python scripts/dev/check_contrast.py
```

`ratio(fg, bg)` computes WCAG 2.x relative luminance and contrast. Supported CSS
formats are `#rgb`, `#rrggbb`, `hsl(h,s%,l%)` and `rgba(r,g,b,a)`. Numeric RGB values
are 0–255, alpha 0–1, and HSL percentages 0–100. Hue wraps at 360 degrees. Foreground
alpha is composited in sRGB over the opaque background before linearisation.
Unsupported colours, out-of-range/non-finite values and translucent backgrounds
raise `ValueError`.

The public `TOKEN_PAIRS` list can be extended. Each dictionary has
`mode`, `name`, `fg`, `bg` and `minimum`. The table records the approved Day/Night
palette, including the white-on-cobalt active chip: body, secondary and primary text; links;
dark text on the grey chip and pale-blue hover chip; active chip; orange kicker;
cobalt focus ring; non-text marks; and hairlines in Day/Night. Orange is also
checked on the Night background. Text requires **4.5:1**, focus rings and non-text
marks **3:1**. Hairlines have `minimum=None`: **decorative, reported only**.

Every ratio is printed to two decimals, but pass/fail uses the unrounded ratio.
Exit codes: **0** all required pairs pass, **1** a required pair fails,
**2** invalid arguments or token input. Tests fix each pair's foreground and
background values; `tests/test_extra_css_tokens.py` ties the table to
`scripts/assets/extra.css` (every colour checked here must be one the stylesheet
declares, and the stylesheet's tokens must equal the approved palette).

Live pages (needs Playwright and its Chromium):

```powershell
python scripts/dev/check_contrast.py --live <built_site> --report <failures.json>
```

`--live` serves the site and, in Night and Day at 1440 and 375 px, measures every
visible text node of the home page, a theme page and two layer pages against its
effective background (`contrast_live.js`), plus input placeholders. Text needs
4.5:1, large text (24 px, or 18.66 px bold) 3:1. Any failure makes the exit code 1.

## Browser behaviour

```powershell
python scripts/dev/check_browser.py <built_site> [--only header,chips,search,menu,copy,sticky,sideways] [--report <results.json>]
```

Playwright checks of the restyled site: the header wordmark and kicker; the NIGHT /
DAY chips (click, keyboard, kept after a reload and a page change, visible focus);
search at 1440 and 375 px; the menu (theme counts equal each theme page's line,
keyboard toggling, the phone drawer, the layer page's "Columns" entry); the copy
button (exact table name, also after a page change and after Back); the sticky
columns header; no sideways scrolling at 375 px.

## Screenshots and contact sheet

```powershell
python scripts/dev/shoot_contact_sheet.py <built_site> <output_folder> [--query battlefield]
```

Saves 16 screenshots (Night and Day × 1440 and 375 px × home, a theme page, a layer
page, search open) and `contact_sheet.png`; records console errors, failed
requests, the GT America faces in use and sideways scrolling, and checks that every
`maps/*.png` decodes. `report.json` holds the results.

## Local demo

```powershell
python scripts/dev/package_demo.py <built_site> <demo_folder> --shots <folder with contact_sheet.png and screens/>
```

Copies the built site (maps included), `serve_demo.py`, `start_demo.bat`, a short
`README.txt`, the contact sheet and the screenshots into a folder outside the
repository, so the demo keeps working whatever the repository has checked out.
It refuses a demo folder inside the repository and replaces only a previous
`site/` that is itself a built site.

`start_demo.bat` (CRLF line endings) finds `py -3` or `python` and runs
`serve_demo.py` from its own folder, so it works from anywhere.
`serve_demo.py` (standard library) serves `site/` on 127.0.0.1 at
http://localhost:8010/, or the next free port up to 8030 (exclusive binding, so an
occupied port is never shared), sends fixed content types, and opens the default
browser once it is listening. `--no-browser`, or `DEMO_NO_BROWSER=1`, serves without
opening a browser (for tests).

## Allowed label changes

`listed_labels.json` is the allow-list for `check_site.py --labels`: the menu labels
the restyle changes on purpose (the handbook entry and the twelve theme rows, which
now read code — name — count).

## Tests

```powershell
python -m pytest tests -q
```

Pytest uses its default system temporary folder for disposable test copies.
`tests/fixtures/sites/minimal/` is a small synthetic built site, copied into each
test's `tmp_path` before mutation. Its `.png`/`.woff2` files are labelled byte
placeholders for hash checks, not decodable images or fonts. Tests cover exact
search content, routes, nav order/labels, article anchors, map placement, asset
bytes, reports, invalid input, CLI exits, colour parsing, alpha compositing and
the supplied known contrast values.

For integration validation, compare a real baseline build with a candidate build.
Neither the synthetic tests nor these scripts need to rebuild or write to that
baseline. Strict MkDocs build validation remains part of the site-changing tasks.
