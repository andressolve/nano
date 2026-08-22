#!/usr/bin/env python3
"""Rebuild deterministic, non-art PNG fixtures and their hash receipt."""

from __future__ import annotations

import hashlib
import json
import struct
import zlib
from pathlib import Path


def chunk(kind: bytes, payload: bytes) -> bytes:
    return (
        struct.pack(">I", len(payload))
        + kind
        + payload
        + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)
    )


def write_png(path: Path, width: int, height: int) -> None:
    row = b"\0" + b"\xff\xff\xff" * width
    raw = row * height
    data = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, level=9))
        + chunk(b"IEND", b"")
    )
    path.write_bytes(data)


def main() -> None:
    root = Path(__file__).resolve().parent
    candidate = root / "candidate"
    candidate.mkdir(exist_ok=True)
    sizes = {
        "candidate.png": (1024, 1536),
        "proof-600x900.png": (600, 900),
        "proof-768x1152.png": (768, 1152),
    }
    for name, dimensions in sizes.items():
        write_png(candidate / name, *dimensions)
    (candidate / "prompt.md").write_text("Deterministic framework fixture; no story art.\n")
    (candidate / "audit.md").write_text(
        "## Intent read\nFramework fixture only.\n\n"
        "## Exact text check\nNo story text.\n\n"
        "## Technical facts\nRGB fixture dimensions verified.\n\n"
        "## Submission\nSUBMITTED TO INDEPENDENT CRITIC\n"
    )
    hashes = {
        name: hashlib.sha256((candidate / name).read_bytes()).hexdigest()
        for name in sizes
    }
    (candidate / "hashes.json").write_text(json.dumps(hashes, indent=2) + "\n")


if __name__ == "__main__":
    main()
