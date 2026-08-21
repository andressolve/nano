#!/usr/bin/env python3
"""Build Sheet 10 from approved source pixels only.

This script performs deterministic crop, scale, background-only matting, and
placement. It does not generate, repaint, relight, retouch, or reshape faces.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from statistics import median

from PIL import Image, ImageChops, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[4]
QA_DIR = ROOT / "monte-cristo-vol2/qa/references/sheet-10"
OUTPUT = ROOT / "monte-cristo-vol2/refs/10-head-board.png"
MANIFEST = QA_DIR / "manifest-v1.json"

CANVAS = (1536, 1024)
CELL_WIDTH = 192
TARGET_HEAD_HEIGHT = 250
TARGET_HEAD_TOP = 330
GROUND_RGB = (146, 137, 126)
RESAMPLE = Image.Resampling.LANCZOS

# The crop rectangles isolate the approved three-quarter head-and-shoulders
# view at the left of each source sheet. head_top, chin_y, and head_center_x are
# hand-checked landmarks used only to normalize scale and align the row.
SOURCES = [
    {
        "id": "01",
        "character": "Count",
        "path": "monte-cristo-vol2/refs/approved/01-count-1838.png",
        "sha256": "2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0",
        "crop_box": [85, 20, 465, 960],
        "head_top": 35,
        "chin_y": 555,
        "head_center_x": 280,
    },
    {
        "id": "02",
        "character": "Mercédès",
        "path": "monte-cristo-vol2/refs/approved/02-mercedes-1838.png",
        "sha256": "8113d7b65a0916c8bf75d12bd1fcf180fc9a31152a11c3f2151eb968e4210821",
        "crop_box": [75, 80, 405, 960],
        "head_top": 100,
        "chin_y": 550,
        "head_center_x": 240,
    },
    {
        "id": "03",
        "character": "Fernand",
        "path": "monte-cristo-vol2/refs/approved/03-fernand-1838.png",
        "sha256": "487f21e1de98136ddc16fcd7aa44d69d0fd659178de417ed282dd30486ea0a40",
        "crop_box": [80, 110, 435, 960],
        "head_top": 140,
        "chin_y": 625,
        "head_center_x": 260,
    },
    {
        "id": "04",
        "character": "Albert",
        "path": "monte-cristo-vol2/refs/approved/04-albert.png",
        "sha256": "3ff9d03308e7f79d5b217f90e8437067a8e407c0f3347902a87db4fb0f54dbee",
        "crop_box": [75, 20, 455, 960],
        "head_top": 45,
        "chin_y": 560,
        "head_center_x": 260,
    },
    {
        "id": "05",
        "character": "Haydée",
        "path": "monte-cristo-vol2/refs/approved/05-haydee.png",
        "sha256": "0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf",
        "crop_box": [100, 70, 455, 960],
        "head_top": 90,
        "chin_y": 575,
        "head_center_x": 275,
    },
    {
        "id": "06",
        "character": "Danglars",
        "path": "monte-cristo-vol2/refs/approved/06-danglars-1838.png",
        "sha256": "626f71c601069032624654958a24b06dfc33974d290d6c9d09d627f3f1e4beb9",
        "crop_box": [65, 150, 405, 960],
        "head_top": 180,
        "chin_y": 640,
        "head_center_x": 235,
    },
    {
        "id": "07",
        "character": "Beauchamp",
        "path": "monte-cristo-vol2/refs/approved/07-beauchamp.png",
        "sha256": "58ba63bf5b77fdf31c585da888461c143474c750d0fa8b2bf7cdab218f38d834",
        "crop_box": [70, 10, 485, 960],
        "head_top": 35,
        "chin_y": 600,
        "head_center_x": 275,
    },
    {
        "id": "08",
        "character": "Villefort",
        "path": "monte-cristo-vol2/refs/approved/08-villefort-1838.png",
        "sha256": "46e31557dd3fd34d3a103e028721869dba5dc0b16874bb40dc00f0982c262e75",
        "crop_box": [120, 70, 488, 960],
        "head_top": 90,
        "chin_y": 590,
        "head_center_x": 305,
    },
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def estimate_background(source: Image.Image) -> tuple[int, int, int]:
    """Use the robust median of the source's empty top strip."""
    strip = source.crop((0, 0, source.width, 20))
    pixels = list(strip.getdata())
    return tuple(int(median(channel)) for channel in zip(*pixels))


def background_matte(crop: Image.Image, background: tuple[int, int, int]) -> Image.Image:
    """Create a crop-edge matte that never classifies or removes facial pixels."""
    # The approved source grounds differ slightly in value and texture. A soft
    # portrait-shaped edge matte prevents hard crop-boundary bands while every
    # RGB pixel inside the crop remains an exact resample of the approved sheet.
    width, height = crop.size
    edge_matte = Image.new("L", crop.size, 0)
    draw = ImageDraw.Draw(edge_matte)
    draw.ellipse((-30, -25, width + 30, 320), fill=255)
    draw.polygon(
        [
            (26, 215),
            (3, 305),
            (15, height - 1),
            (width - 15, height - 1),
            (width - 3, 305),
            (width - 26, 215),
        ],
        fill=255,
    )
    edge_matte = edge_matte.filter(ImageFilter.GaussianBlur(radius=8.0))
    return edge_matte


def main() -> None:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    board = Image.new("RGB", CANVAS, GROUND_RGB)
    manifest_sources = []

    for index, spec in enumerate(SOURCES):
        source_path = ROOT / spec["path"]
        actual_sha = sha256(source_path)
        if actual_sha != spec["sha256"]:
            raise RuntimeError(
                f"Approved source hash mismatch for {source_path}: "
                f"expected {spec['sha256']}, got {actual_sha}"
            )

        with Image.open(source_path) as opened:
            source = opened.convert("RGB")
        if source.size != (1536, 1024):
            raise RuntimeError(f"Unexpected source dimensions for {source_path}: {source.size}")

        crop_box = tuple(spec["crop_box"])
        crop = source.crop(crop_box)
        source_head_height = spec["chin_y"] - spec["head_top"]
        scale = TARGET_HEAD_HEIGHT / source_head_height
        resized_size = (
            round(crop.width * scale),
            round(crop.height * scale),
        )
        resized = crop.resize(resized_size, RESAMPLE)

        background = estimate_background(crop)
        matte = background_matte(resized, background)

        cell_x = index * CELL_WIDTH
        head_center_offset = round((spec["head_center_x"] - crop_box[0]) * scale)
        head_top_offset = round((spec["head_top"] - crop_box[1]) * scale)
        placement_x = cell_x + CELL_WIDTH // 2 - head_center_offset
        placement_y = TARGET_HEAD_TOP - head_top_offset

        if placement_x < cell_x or placement_x + resized.width > cell_x + CELL_WIDTH:
            raise RuntimeError(f"Crop for {spec['character']} crosses its cell boundary")
        if placement_y < 0 or placement_y + resized.height > CANVAS[1]:
            raise RuntimeError(f"Crop for {spec['character']} crosses the canvas boundary")

        board.paste(resized, (placement_x, placement_y), matte)
        manifest_sources.append(
            {
                "order": index + 1,
                "id": spec["id"],
                "character": spec["character"],
                "source_path": spec["path"],
                "source_sha256": actual_sha,
                "source_mode": "RGB",
                "source_size": [source.width, source.height],
                "crop_box_xyxy": list(crop_box),
                "head_landmarks": {
                    "head_top_y": spec["head_top"],
                    "chin_y": spec["chin_y"],
                    "head_center_x": spec["head_center_x"],
                },
                "scale": scale,
                "resized_crop_size": list(resized_size),
                "placement_xy": [placement_x, placement_y],
                "cell_xyxy": [cell_x, 0, cell_x + CELL_WIDTH, CANVAS[1]],
                "estimated_crop_background_rgb": list(background),
            }
        )

    if board.mode != "RGB" or board.size != CANVAS:
        raise RuntimeError(f"Invalid board metadata: mode={board.mode}, size={board.size}")

    board.save(OUTPUT, format="PNG", optimize=False, compress_level=9)
    output_sha = sha256(OUTPUT)

    manifest = {
        "artifact": "Sheet 10 — neutral head board",
        "version": 1,
        "method": "deterministic approved-pixel crop, scale, matte, and placement",
        "generative_operation": False,
        "canvas": {"width": 1536, "height": 1024, "mode": "RGB", "format": "PNG"},
        "ground_rgb": list(GROUND_RGB),
        "order": "01 Count, 02 Mercédès, 03 Fernand, 04 Albert, 05 Haydée, 06 Danglars, 07 Beauchamp, 08 Villefort",
        "normalization": {
            "target_head_height_px": TARGET_HEAD_HEIGHT,
            "target_head_top_y": TARGET_HEAD_TOP,
            "resampling": "Pillow LANCZOS",
            "background_matte": "deterministic soft portrait edge matte only; no color-based classification or removal of facial pixels",
            "identity_pixels": "source RGB retained except deterministic LANCZOS resizing and alpha compositing onto the neutral ground",
        },
        "sources": manifest_sources,
        "output_path": str(OUTPUT.relative_to(ROOT)),
        "output_sha256": output_sha,
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {OUTPUT}")
    print(f"wrote {MANIFEST}")
    print(f"output_sha256 {output_sha}")


if __name__ == "__main__":
    main()
