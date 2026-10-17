"""T01 parity check: the repository generator renders exactly what the live copy renders.

Input/output CRS: n/a (metadata only). Data layer: catalogue generation (development check).

Renders one frozen snapshot twice and compares the two trees byte for byte:

  1. with the live working copy's ``render_mkdocs`` — its output paths redirected
     into the work folder; its ``main()`` is never called, so nothing is written to
     the share (importing it reads the styles file, read only);
  2. with this repository's script, ``--from-snapshot --site-only --out-dir``.

Any byte difference fails, line endings included.

With ``--against-commit <rev>`` the second render is also compared with the
``docs/`` and ``mkdocs.yml`` committed at ``<rev>`` (database drift check). Git
stores text with LF line endings (``core.autocrlf=true``) while the generator
writes CRLF on Windows, so text files are compared with CRLF folded to LF on both
sides; binary files are compared byte for byte. The only committed file allowed
to be missing from the render is the handbook PDF, which the generator never
writes.

Usage:
    python scripts/dev/parity_t01.py --live <live build_catalogue.py> --snapshot <json>
        --work <work folder> [--against-commit 971a0abd]
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "scripts" / "build_catalogue.py"
# Committed under docs/ but never written by the generator.
NOT_GENERATED = frozenset({"docs/PP_Staff_Data_Management_Handbook.pdf"})
TEXT_SUFFIXES = frozenset({".md", ".yml", ".yaml", ".css", ".html", ".js", ".json", ".txt"})

Result = tuple[list[str], list[str], list[str], list[str]]


def generated_tree(root: Path) -> dict[str, bytes]:
    """Relative path -> bytes for everything under ``root/docs`` plus ``mkdocs.yml``."""
    files = {p.relative_to(root).as_posix(): p.read_bytes()
             for p in (root / "docs").rglob("*") if p.is_file()}
    files["mkdocs.yml"] = (root / "mkdocs.yml").read_bytes()
    return files


def committed_tree(repo: Path, rev: str) -> dict[str, bytes]:
    """Relative path -> blob bytes for ``docs/`` and ``mkdocs.yml`` at ``rev``."""
    names = subprocess.run(
        ["git", "-C", str(repo), "ls-tree", "-r", "--name-only", rev, "--", "docs", "mkdocs.yml"],
        check=True, capture_output=True, text=True, encoding="utf-8").stdout.splitlines()
    request = "".join(f"{rev}:{name}\n" for name in names).encode("utf-8")
    out = subprocess.run(["git", "-C", str(repo), "cat-file", "--batch"], input=request,
                         check=True, capture_output=True).stdout
    files: dict[str, bytes] = {}
    pos = 0
    for name in names:
        header_end = out.index(b"\n", pos)
        size = int(out[pos:header_end].split()[2])
        files[name] = out[header_end + 1:header_end + 1 + size]
        pos = header_end + 1 + size + 1          # skip the blob and its trailing newline
    return files


def fold_text(tree: dict[str, bytes]) -> dict[str, bytes]:
    """Fold CRLF to LF in text files, as git stores them; leave binaries alone."""
    return {k: (v.replace(b"\r\n", b"\n") if Path(k).suffix.lower() in TEXT_SUFFIXES else v)
            for k, v in tree.items()}


def compare(a: dict[str, bytes], b: dict[str, bytes]) -> Result:
    """(only in a, only in b, differ in content, text files differing in line endings only)."""
    only_a = sorted(set(a) - set(b))
    only_b = sorted(set(b) - set(a))
    content, endings = [], []
    for key in sorted(set(a) & set(b)):
        if a[key] == b[key]:
            continue
        if (Path(key).suffix.lower() in TEXT_SUFFIXES
                and a[key].replace(b"\r\n", b"\n") == b[key].replace(b"\r\n", b"\n")):
            endings.append(key)
        else:
            content.append(key)
    return only_a, only_b, content, endings


def is_identical(result: Result) -> bool:
    """True only when nothing differs at all, line endings included."""
    return not any(result)


def drift_check(render: dict[str, bytes], committed: dict[str, bytes],
                exempt: frozenset[str] = NOT_GENERATED) -> Result:
    """Compare a render with a commit's blobs; only ``exempt`` may be missing from the render."""
    committed = {k: v for k, v in committed.items() if k not in exempt}
    return compare(fold_text(render), fold_text(committed))


def fresh_dir(path: Path, work: Path) -> Path:
    """Empty ``path``, refusing anything outside the work folder."""
    path = path.resolve()
    if work.resolve() not in path.parents:
        raise SystemExit(f"refusing to clear {path}: not inside {work}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
    return path


def render_live(live_script: Path, snap: dict, out: Path, maps_stub: Path) -> None:
    """Run only the live copy's ``render_mkdocs`` on the snapshot, into ``out``."""
    spec = importlib.util.spec_from_file_location("live_build_catalogue", live_script)
    if not spec or not spec.loader:
        raise SystemExit(f"cannot load {live_script}")
    live = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(live)
    # The live has_map() looks for <table>.png in MAPS_DIR: give it exactly the
    # snapshot's map list, so both renders see the same maps.
    for table in snap["maps"]:
        (maps_stub / f"{table}.png").write_bytes(b"")
    live.OUT = out
    live.DOCS = out / "docs"
    live.MAPS_DIR = maps_stub
    live.APPROVED = set(snap["approved"])
    live.render_mkdocs(copy.deepcopy(snap["records"]), snap["built"])


def render_repo(snapshot: Path, out: Path) -> None:
    """Run this repository's script on the snapshot, site only, into ``out``."""
    subprocess.run([sys.executable, str(SCRIPT), "--from-snapshot", str(snapshot),
                    "--site-only", "--out-dir", str(out)], check=True)


def report(label: str, result: Result) -> bool:
    """Print one verdict line plus the differing paths; return True if identical."""
    ok = is_identical(result)
    print(f"{label}: {'IDENTICAL' if ok else 'DIFFERENT'}")
    for name, items in zip(("only in first", "only in second", "content differs", "line endings differ"),
                           result):
        if items:
            print(f"  {name} ({len(items)}): " + ", ".join(items[:12]) + (" ..." if len(items) > 12 else ""))
    return ok


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--live", type=Path, required=True, help="the live working copy of build_catalogue.py")
    p.add_argument("--snapshot", type=Path, required=True, help="snapshot JSON from --save-snapshot")
    p.add_argument("--work", type=Path, required=True, help="work folder for the two renders")
    p.add_argument("--against-commit", metavar="REV",
                   help="also compare with docs/ and mkdocs.yml committed at REV (e.g. 971a0abd)")
    args = p.parse_args(argv)

    snap = json.loads(args.snapshot.read_text(encoding="utf-8"))
    live_out = fresh_dir(args.work / "t01_live", args.work)
    repo_out = fresh_dir(args.work / "t01_repo", args.work)
    maps_stub = fresh_dir(args.work / "t01_maps_stub", args.work)

    render_live(args.live, snap, live_out, maps_stub)
    render_repo(args.snapshot, repo_out)
    ok = report("live render vs repository render (byte for byte)",
                compare(generated_tree(live_out), generated_tree(repo_out)))

    if args.against_commit:
        ok = report(f"repository render vs docs/ committed at {args.against_commit} (drift)",
                    drift_check(generated_tree(repo_out), committed_tree(REPO, args.against_commit))) and ok
        print(f"  exempt, never generated: {', '.join(sorted(NOT_GENERATED))}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
