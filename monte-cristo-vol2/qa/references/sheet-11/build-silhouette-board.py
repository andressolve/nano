#!/usr/bin/env python3
"""Build Sheet 11 deterministically from approved full-length figures."""

from __future__ import annotations

from collections import deque
import hashlib
import json
from pathlib import Path
from statistics import median

from PIL import Image, ImageFilter


ROOT = Path(__file__).resolve().parents[4]
QA_DIR = ROOT / "monte-cristo-vol2/qa/references/sheet-11"
OUTPUT = ROOT / "monte-cristo-vol2/refs/11-silhouette-board.png"
MANIFEST = QA_DIR / "manifest-v1.json"

CANVAS = (1536, 1024)
CELL_WIDTH = 192
TARGET_BODY_HEIGHT = 370
TARGET_FLOOR_Y = 697
GROUND_RGB = (224, 219, 211)
SILHOUETTE_RGB = (38, 36, 34)
RESAMPLE = Image.Resampling.LANCZOS

# Each rectangle encloses only the approved default full-length standing view.
# The seed is a point inside that figure's torso. Hard-coded head/floor landmarks
# normalize height without any pose correction or reshaping.
SOURCES = [
    {
        "id": "01",
        "character": "Count",
        "path": "monte-cristo-vol2/refs/approved/01-count-1838.png",
        "sha256": "2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0",
        "crop_box": [560, 30, 900, 1005],
        "seed_xy": [720, 450],
        "head_top_y": 55,
        "floor_y": 985,
        "threshold": 48,
        "extra_seed_xys": [[720, 125]],
    },
    {
        "id": "02",
        "character": "Mercédès",
        "path": "monte-cristo-vol2/refs/approved/02-mercedes-1838.png",
        "sha256": "8113d7b65a0916c8bf75d12bd1fcf180fc9a31152a11c3f2151eb968e4210821",
        "crop_box": [400, 75, 845, 1010],
        "seed_xy": [630, 450],
        "head_top_y": 100,
        "floor_y": 990,
        "threshold": 48,
        "extra_seed_xys": [[630, 180]],
    },
    {
        "id": "03",
        "character": "Fernand",
        "path": "monte-cristo-vol2/refs/approved/03-fernand-1838.png",
        "sha256": "487f21e1de98136ddc16fcd7aa44d69d0fd659178de417ed282dd30486ea0a40",
        "crop_box": [510, 30, 930, 1005],
        "seed_xy": [720, 450],
        "head_top_y": 55,
        "floor_y": 985,
        "threshold": 48,
        "extra_seed_xys": [[720, 130]],
    },
    {
        "id": "04",
        "character": "Albert",
        "path": "monte-cristo-vol2/refs/approved/04-albert.png",
        "sha256": "3ff9d03308e7f79d5b217f90e8437067a8e407c0f3347902a87db4fb0f54dbee",
        "crop_box": [500, 30, 870, 1005],
        "seed_xy": [690, 400],
        "head_top_y": 50,
        "floor_y": 985,
        "threshold": 48,
        "extra_seed_xys": [[690, 120], [650, 720], [735, 720]],
    },
    {
        "id": "05",
        "character": "Haydée",
        "path": "monte-cristo-vol2/refs/approved/05-haydee.png",
        "sha256": "0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf",
        "crop_box": [490, 55, 860, 1000],
        "seed_xy": [680, 450],
        "head_top_y": 80,
        "floor_y": 980,
        "threshold": 48,
        "extra_seed_xys": [[680, 160], [680, 720]],
    },
    {
        "id": "06",
        "character": "Danglars",
        "path": "monte-cristo-vol2/refs/approved/06-danglars-1838.png",
        "sha256": "626f71c601069032624654958a24b06dfc33974d290d6c9d09d627f3f1e4beb9",
        "crop_box": [480, 50, 880, 1000],
        "seed_xy": [690, 450],
        "head_top_y": 75,
        "floor_y": 980,
        "threshold": 48,
        "extra_seed_xys": [[690, 160]],
    },
    {
        "id": "07",
        "character": "Beauchamp",
        "path": "monte-cristo-vol2/refs/approved/07-beauchamp.png",
        "sha256": "58ba63bf5b77fdf31c585da888461c143474c750d0fa8b2bf7cdab218f38d834",
        "crop_box": [485, 20, 815, 1005],
        "seed_xy": [650, 450],
        "head_top_y": 35,
        "floor_y": 990,
        "threshold": 48,
        "extra_seed_xys": [[650, 120]],
    },
    {
        "id": "08",
        "character": "Villefort",
        "path": "monte-cristo-vol2/refs/approved/08-villefort-1838.png",
        "sha256": "46e31557dd3fd34d3a103e028721869dba5dc0b16874bb40dc00f0982c262e75",
        "crop_box": [640, 50, 990, 1005],
        "seed_xy": [800, 400],
        "head_top_y": 75,
        "floor_y": 985,
        "threshold": 48,
        "extra_seed_xys": [[800, 150]],
    },
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def estimate_background(crop: Image.Image) -> tuple[int, int, int]:
    """Estimate the plain ground from a 10-pixel border around the crop."""
    width, height = crop.size
    pixels = []
    for y in range(height):
        for x in range(width):
            if x < 10 or x >= width - 10 or y < 10 or y >= height - 10:
                pixels.append(crop.getpixel((x, y)))
    return tuple(int(median(channel)) for channel in zip(*pixels))


def nearest_foreground(mask: bytearray, width: int, height: int, x: int, y: int) -> tuple[int, int]:
    if mask[y * width + x]:
        return x, y
    for radius in range(1, 61):
        x0, x1 = max(0, x - radius), min(width - 1, x + radius)
        y0, y1 = max(0, y - radius), min(height - 1, y + radius)
        for px in range(x0, x1 + 1):
            for py in (y0, y1):
                if mask[py * width + px]:
                    return px, py
        for py in range(y0 + 1, y1):
            for px in (x0, x1):
                if mask[py * width + px]:
                    return px, py
    raise RuntimeError("No foreground pixel found near torso seed")


def connected_figure_mask(
    crop: Image.Image,
    background: tuple[int, int, int],
    threshold: int,
    seeds: list[tuple[int, int]],
) -> Image.Image:
    """Union source-connected figure components containing the supplied seeds."""
    width, height = crop.size
    threshold_sq = threshold * threshold
    candidate = bytearray(width * height)
    for index, (red, green, blue) in enumerate(crop.getdata()):
        distance_sq = (
            (red - background[0]) ** 2
            + (green - background[1]) ** 2
            + (blue - background[2]) ** 2
        )
        if distance_sq >= threshold_sq:
            candidate[index] = 1

    selected = bytearray(width * height)
    queue = deque()
    for seed in seeds:
        seed_x, seed_y = nearest_foreground(candidate, width, height, *seed)
        position = seed_y * width + seed_x
        if not selected[position]:
            selected[position] = 1
            queue.append((seed_x, seed_y))
    while queue:
        x, y = queue.popleft()
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height:
                position = ny * width + nx
                if candidate[position] and not selected[position]:
                    selected[position] = 1
                    queue.append((nx, ny))

    # Fill only small enclosed raster holes caused by paint texture. Large
    # negative spaces in the approved pose remain open and therefore unchanged.
    visited = bytearray(width * height)
    for start_y in range(height):
        for start_x in range(width):
            start = start_y * width + start_x
            if selected[start] or visited[start]:
                continue
            hole = []
            touches_border = False
            visited[start] = 1
            queue = deque([(start_x, start_y)])
            while queue:
                x, y = queue.popleft()
                hole.append((x, y))
                if x == 0 or y == 0 or x == width - 1 or y == height - 1:
                    touches_border = True
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < width and 0 <= ny < height:
                        position = ny * width + nx
                        if not selected[position] and not visited[position]:
                            visited[position] = 1
                            queue.append((nx, ny))
            if not touches_border and len(hole) <= 900:
                for x, y in hole:
                    selected[y * width + x] = 1

    mask = Image.new("L", crop.size, 0)
    mask.putdata([255 if value else 0 for value in selected])
    return mask


def solidify_interior(mask: Image.Image) -> Image.Image:
    """Seal tiny paint channels, then fill the flat silhouette interior."""
    width, height = mask.size
    closed = mask.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.MinFilter(9))
    closed_data = bytearray(1 if value else 0 for value in closed.getdata())
    external = bytearray(width * height)
    queue = deque()
    for x in range(width):
        for y in (0, height - 1):
            position = y * width + x
            if not closed_data[position] and not external[position]:
                external[position] = 1
                queue.append((x, y))
    for y in range(height):
        for x in (0, width - 1):
            position = y * width + x
            if not closed_data[position] and not external[position]:
                external[position] = 1
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height:
                position = ny * width + nx
                if not closed_data[position] and not external[position]:
                    external[position] = 1
                    queue.append((nx, ny))

    data = bytearray(1 if value else 0 for value in mask.getdata())
    for position in range(width * height):
        if not external[position]:
            data[position] = 1

    result = Image.new("L", mask.size, 0)
    result.putdata([255 if value else 0 for value in data])
    return result


def remove_floor_shadow(mask: Image.Image, floor_y: int) -> Image.Image:
    """Remove bottom-zone ground marks that have no vertical figure support."""
    width, height = mask.size
    pixels = mask.load()
    support = [False] * width
    support_top = max(0, floor_y - 160)
    support_bottom = max(0, floor_y - 65)
    for x in range(width):
        support[x] = any(pixels[x, y] for y in range(support_top, support_bottom + 1))

    allowed = [False] * width
    for x in range(width):
        left, right = max(0, x - 18), min(width, x + 19)
        allowed[x] = any(support[left:right])

    for y in range(max(0, floor_y - 64), height):
        for x in range(width):
            if y > floor_y or not allowed[x]:
                pixels[x, y] = 0
    return mask


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
        background = estimate_background(crop)
        seed_source_xys = [spec["seed_xy"], *spec["extra_seed_xys"]]
        seed_relatives = [
            (seed_x - crop_box[0], seed_y - crop_box[1])
            for seed_x, seed_y in seed_source_xys
        ]
        mask = connected_figure_mask(crop, background, spec["threshold"], seed_relatives)

        # Flat silhouettes retain the source-derived exterior contour while
        # removing interior paint/color gaps and foot-attached ground shadows.
        floor_relative = spec["floor_y"] - crop_box[1]
        mask = solidify_interior(mask)
        mask = remove_floor_shadow(mask, floor_relative)
        source_mask_bbox = mask.getbbox()
        if source_mask_bbox is None:
            raise RuntimeError(f"Empty mask for {spec['character']}")

        source_body_height = spec["floor_y"] - spec["head_top_y"]
        scale = TARGET_BODY_HEIGHT / source_body_height
        resized_size = (round(crop.width * scale), round(crop.height * scale))
        resized_mask = mask.resize(resized_size, RESAMPLE)
        resized_mask_bbox = resized_mask.getbbox()
        if resized_mask_bbox is None:
            raise RuntimeError(f"Empty resized mask for {spec['character']}")

        cell_x = index * CELL_WIDTH
        mask_center_x = (source_mask_bbox[0] + source_mask_bbox[2]) / 2
        placement_x = round(cell_x + CELL_WIDTH / 2 - mask_center_x * scale)
        floor_offset = (spec["floor_y"] - crop_box[1]) * scale
        placement_y = round(TARGET_FLOOR_Y - floor_offset)

        board.paste(SILHOUETTE_RGB, (placement_x, placement_y), resized_mask)
        placed_bbox = [
            placement_x + resized_mask_bbox[0],
            placement_y + resized_mask_bbox[1],
            placement_x + resized_mask_bbox[2],
            placement_y + resized_mask_bbox[3],
        ]
        if placed_bbox[0] < cell_x or placed_bbox[2] > cell_x + CELL_WIDTH:
            raise RuntimeError(f"Silhouette for {spec['character']} crosses its cell boundary: {placed_bbox}")
        if placed_bbox[1] < 0 or placed_bbox[3] > CANVAS[1]:
            raise RuntimeError(f"Silhouette for {spec['character']} crosses canvas boundary: {placed_bbox}")

        manifest_sources.append(
            {
                "order": index + 1,
                "id": spec["id"],
                "character": spec["character"],
                "source_path": spec["path"],
                "source_sha256": actual_sha,
                "source_size": [source.width, source.height],
                "source_mode": "RGB",
                "crop_box_xyxy": list(crop_box),
                "extraction": {
                    "method": "RGB distance from median 10-pixel crop border; union of four-connected source components containing explicit torso/garment seeds; fill small and source-enclosed interior paint gaps; remove only bottom-zone ground marks lacking vertical figure support; clear below recorded floor",
                    "estimated_background_rgb": list(background),
                    "rgb_distance_threshold": spec["threshold"],
                    "component_seed_source_xys": seed_source_xys,
                    "source_mask_bbox_in_crop": list(source_mask_bbox),
                },
                "normalization_landmarks": {
                    "head_top_y": spec["head_top_y"],
                    "floor_y": spec["floor_y"],
                },
                "scale": scale,
                "resized_crop_size": list(resized_size),
                "crop_placement_xy": [placement_x, placement_y],
                "placed_silhouette_bbox_xyxy": placed_bbox,
                "cell_xyxy": [cell_x, 0, cell_x + CELL_WIDTH, CANVAS[1]],
            }
        )

    if board.mode != "RGB" or board.size != CANVAS:
        raise RuntimeError(f"Invalid board metadata: mode={board.mode}, size={board.size}")

    board.save(OUTPUT, format="PNG", optimize=False, compress_level=9)
    output_sha = sha256(OUTPUT)
    manifest = {
        "artifact": "Sheet 11 — grayscale silhouette board",
        "version": 1,
        "method": "deterministic figure extraction, scale normalization, flat silhouette conversion, and placement",
        "generative_operation": False,
        "canvas": {"width": 1536, "height": 1024, "mode": "RGB", "format": "PNG"},
        "ground_rgb": list(GROUND_RGB),
        "silhouette_rgb": list(SILHOUETTE_RGB),
        "order": "01 Count, 02 Mercédès, 03 Fernand, 04 Albert, 05 Haydée, 06 Danglars, 07 Beauchamp, 08 Villefort",
        "normalization": {
            "target_body_height_px": TARGET_BODY_HEIGHT,
            "target_floor_y": TARGET_FLOOR_Y,
            "mask_resampling": "Pillow LANCZOS",
            "interior": "one flat dark RGB value; no source color or interior detail",
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
