#!/usr/bin/env python3
"""Build Sheet 23 from the two approved full-sheet rasters.

This is a deterministic reference-transport operation: full-source resize and
placement only. It performs no generation, crop, repaint, relighting, retouch,
labeling, border drawing, or invented-content operation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[4]
QA_DIR = ROOT / "monte-cristo-vol2/qa/references/sheet-23"
OUTPUT = ROOT / "monte-cristo-vol2/refs/23-page-33-chamber-objects-carrier.png"
MANIFEST = QA_DIR / "manifest-v1.json"

CANVAS = (1536, 1024)
SOURCE_SIZE = (1536, 1024)
REDUCED_SIZE = (759, 506)  # Exact 3:2 integer reduction; scale = 253 / 512.
GUTTER_WIDTH = 18
NEUTRAL_RGB = (215, 211, 201)
RESAMPLE = Image.Resampling.LANCZOS
Y = (CANVAS[1] - REDUCED_SIZE[1]) // 2

SOURCES = [
    {
        "role": "left — approved Sheet 19 Chamber of Peers",
        "path": "monte-cristo-vol2/refs/approved/19-set-chamber.png",
        "sha256": "f29a804117800ce50102cfd370ecfbc1907cca9696204cf1d363c2a7564108c5",
        "placement_xy": [0, Y],
    },
    {
        "role": "right — approved Sheet 21 key objects",
        "path": "monte-cristo-vol2/refs/approved/21-objects.png",
        "sha256": "1013330cd03e6e748cad7cb1a45671e042ee46bf1f7fe5b9d5d07634406e849a",
        "placement_xy": [REDUCED_SIZE[0] + GUTTER_WIDTH, Y],
    },
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if REDUCED_SIZE[0] * 2 + GUTTER_WIDTH != CANVAS[0]:
        raise RuntimeError("Horizontal placement does not fill the canvas exactly")
    if REDUCED_SIZE[0] * SOURCE_SIZE[1] != REDUCED_SIZE[1] * SOURCE_SIZE[0]:
        raise RuntimeError("Configured reduction is not exactly aspect-preserving")

    carrier = Image.new("RGB", CANVAS, NEUTRAL_RGB)
    manifest_sources = []

    for source_spec in SOURCES:
        source_path = ROOT / source_spec["path"]
        actual_sha = sha256(source_path)
        if actual_sha != source_spec["sha256"]:
            raise RuntimeError(
                f"Approved source hash mismatch for {source_path}: "
                f"expected {source_spec['sha256']}, got {actual_sha}"
            )

        with Image.open(source_path) as opened:
            source_format = opened.format
            source = opened.convert("RGB")

        if source_format != "PNG" or source.mode != "RGB" or source.size != SOURCE_SIZE:
            raise RuntimeError(
                f"Unexpected source metadata for {source_path}: "
                f"format={source_format}, mode={source.mode}, size={source.size}"
            )

        reduced = source.resize(REDUCED_SIZE, RESAMPLE)
        placement = tuple(source_spec["placement_xy"])
        carrier.paste(reduced, placement)

        manifest_sources.append(
            {
                "role": source_spec["role"],
                "source_path": source_spec["path"],
                "source_sha256": actual_sha,
                "source_format": source_format,
                "source_mode": source.mode,
                "source_size": list(source.size),
                "source_crop_box_xyxy": [0, 0, source.width, source.height],
                "crop_away": False,
                "resampling": "Pillow LANCZOS",
                "scale_exact": "253/512",
                "scale_decimal": REDUCED_SIZE[0] / SOURCE_SIZE[0],
                "resized_size": list(REDUCED_SIZE),
                "placement_xy": list(placement),
                "placement_box_xyxy": [
                    placement[0],
                    placement[1],
                    placement[0] + REDUCED_SIZE[0],
                    placement[1] + REDUCED_SIZE[1],
                ],
            }
        )

    if carrier.mode != "RGB" or carrier.size != CANVAS:
        raise RuntimeError(
            f"Invalid carrier metadata: mode={carrier.mode}, size={carrier.size}"
        )

    carrier.save(OUTPUT, format="PNG", optimize=False, compress_level=9)
    output_sha = sha256(OUTPUT)

    manifest = {
        "artifact": "Sheet 23 — Page 33 Chamber + objects carrier, unlettered",
        "version": 1,
        "method": "deterministic full-source direct-pixel resampling and placement",
        "generative_operation": False,
        "repainting_or_invented_content": False,
        "canvas": {
            "width": CANVAS[0],
            "height": CANVAS[1],
            "mode": "RGB",
            "format": "PNG",
            "neutral_ground_rgb": list(NEUTRAL_RGB),
        },
        "layout": {
            "order": "approved Sheet 19 left; approved Sheet 21 right",
            "gutter_width_px": GUTTER_WIDTH,
            "gutter_box_xyxy": [
                REDUCED_SIZE[0],
                0,
                REDUCED_SIZE[0] + GUTTER_WIDTH,
                CANVAS[1],
            ],
            "vertical_alignment": "centered",
            "top_padding_px": Y,
            "bottom_padding_px": CANVAS[1] - Y - REDUCED_SIZE[1],
            "labels_dividers_borders": False,
        },
        "sources": manifest_sources,
        "output_path": str(OUTPUT.relative_to(ROOT)),
        "output_sha256": output_sha,
    }
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"wrote {OUTPUT}")
    print(f"wrote {MANIFEST}")
    print(f"output_sha256 {output_sha}")


if __name__ == "__main__":
    main()
