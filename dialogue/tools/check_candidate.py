#!/usr/bin/env python3
"""Validate complete PNG candidates/proofs and their SHA-256 receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import tomllib
import zlib
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
COLOR_CHANNELS = {2: ("RGB", 3), 6: ("RGBA", 4)}


def png_info(path: Path) -> tuple[int, int, str]:
    data = path.read_bytes()
    if len(data) < 57 or not data.startswith(PNG_SIGNATURE):
        raise ValueError(f"not a complete PNG: {path.name}")
    position = len(PNG_SIGNATURE)
    ihdr = None
    compressed = bytearray()
    saw_iend = False
    while position < len(data):
        if position + 12 > len(data):
            raise ValueError(f"truncated PNG chunk: {path.name}")
        length = struct.unpack(">I", data[position : position + 4])[0]
        chunk_type = data[position + 4 : position + 8]
        chunk_end = position + 12 + length
        if chunk_end > len(data):
            raise ValueError(f"truncated PNG data: {path.name}")
        payload = data[position + 8 : position + 8 + length]
        expected_crc = struct.unpack(">I", data[position + 8 + length : chunk_end])[0]
        if zlib.crc32(chunk_type + payload) & 0xFFFFFFFF != expected_crc:
            raise ValueError(f"PNG CRC failure: {path.name}")
        if chunk_type == b"IHDR":
            if ihdr is not None or length != 13 or position != 8:
                raise ValueError(f"invalid IHDR: {path.name}")
            ihdr = struct.unpack(">IIBBBBB", payload)
        elif chunk_type == b"IDAT":
            compressed.extend(payload)
        elif chunk_type == b"IEND":
            if length != 0 or chunk_end != len(data):
                raise ValueError(f"invalid IEND/trailing bytes: {path.name}")
            saw_iend = True
            position = chunk_end
            break
        position = chunk_end
    if ihdr is None or not compressed or not saw_iend:
        raise ValueError(f"PNG lacks IHDR, IDAT, or IEND: {path.name}")
    width, height, depth, color_type, compression, filter_method, interlace = ihdr
    if depth != 8 or color_type not in COLOR_CHANNELS:
        raise ValueError(f"unsupported PNG mode: {path.name}")
    if (compression, filter_method, interlace) != (0, 0, 0):
        raise ValueError(f"unsupported PNG encoding: {path.name}")
    try:
        raw = zlib.decompress(bytes(compressed))
    except zlib.error as exc:
        raise ValueError(f"undecodable PNG pixels: {path.name}") from exc
    mode, channels = COLOR_CHANNELS[color_type]
    row_length = 1 + width * channels
    if len(raw) != row_length * height:
        raise ValueError(f"wrong decompressed pixel length: {path.name}")
    if any(raw[row * row_length] > 4 for row in range(height)):
        raise ValueError(f"invalid PNG row filter: {path.name}")
    return width, height, mode


def load_output_spec(manifest_path: Path) -> dict[str, tuple[int, int, str]]:
    manifest = tomllib.loads(manifest_path.read_text())
    try:
        output = manifest["output"]
        mode = output["mode"]
        return {
            "candidate.png": (output["width"], output["height"], mode),
            "proof-600x900.png": (output["desktop_width"], output["desktop_height"], mode),
            "proof-768x1152.png": (output["tablet_width"], output["tablet_height"], mode),
        }
    except (KeyError, TypeError) as exc:
        raise ValueError("manifest lacks complete [output] dimensions/mode") from exc


def check(root: Path, manifest_path: Path, receipt_path: Path) -> None:
    required = {"candidate.png", "prompt.md", "audit.md", "proof-600x900.png", "proof-768x1152.png"}
    missing = sorted(name for name in required if not (root / name).is_file() or not (root / name).stat().st_size)
    if missing:
        raise ValueError("missing: " + ", ".join(missing))
    specs = load_output_spec(manifest_path)
    hashes = {}
    for name, expected in specs.items():
        actual = png_info(root / name)
        if actual != expected:
            raise ValueError(f"wrong dimensions/mode for {name}: {actual} != {expected}")
        hashes[name] = hashlib.sha256((root / name).read_bytes()).hexdigest()
    try:
        receipt = json.loads(receipt_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("missing or invalid SHA-256 receipt") from exc
    if receipt != hashes:
        raise ValueError("SHA-256 receipt mismatch")
    audit = (root / "audit.md").read_text()
    headings = ("## Intent read", "## Exact text check", "## Technical facts", "## Submission")
    if any(audit.count(heading) != 1 for heading in headings):
        raise ValueError("audit headings do not match the required schema")
    if "SUBMITTED TO INDEPENDENT CRITIC" not in audit:
        raise ValueError("audit did not submit the candidate")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--receipt", required=True)
    args = parser.parse_args()
    try:
        check(Path(args.root), Path(args.manifest), Path(args.receipt))
    except (OSError, ValueError) as exc:
        raise SystemExit(f"INVALID CANDIDATE: {exc}") from exc
    print("VALID CANDIDATE")


if __name__ == "__main__":
    main()
