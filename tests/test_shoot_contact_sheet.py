"""Tests for the map check in scripts/dev/shoot_contact_sheet.py.

Input/output CRS: n/a (preview PNG files only). Data layer: catalogue development checks (tests).

``decode_maps`` must fully decode every PNG: a file whose chunk checksums are
valid but whose image stream is broken passes Pillow's ``verify()`` and must
still be reported.
"""
from __future__ import annotations

import importlib.util
import struct
import sys
import zlib
from pathlib import Path
from types import ModuleType

import pytest
from PIL import Image

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "dev" / "shoot_contact_sheet.py"


def load() -> ModuleType:
    pytest.importorskip("playwright.sync_api")       # the script imports Playwright at the top
    spec = importlib.util.spec_from_file_location("shoot_contact_sheet_under_test", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["shoot_contact_sheet_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


def chunk(kind: bytes, data: bytes) -> bytes:
    """One PNG chunk with a correct CRC."""
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def broken_png() -> bytes:
    """A 4 × 4 RGB PNG whose checksums are valid but whose IDAT is not a zlib stream."""
    header = struct.pack(">IIBBBBB", 4, 4, 8, 2, 0, 0, 0)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header)
            + chunk(b"IDAT", b"this is not a zlib stream") + chunk(b"IEND", b""))


def test_decode_maps_catches_a_broken_image_stream(tmp_path: Path) -> None:
    maps = tmp_path / "maps"
    maps.mkdir()
    Image.new("RGB", (4, 4), (255, 81, 29)).save(maps / "good.png")
    (maps / "broken.png").write_bytes(broken_png())
    with Image.open(maps / "broken.png") as img:       # structure and checksums alone pass
        img.verify()

    count, problems = load().decode_maps(tmp_path)

    assert count == 2
    assert len(problems) == 1
    assert problems[0].startswith("broken.png")
