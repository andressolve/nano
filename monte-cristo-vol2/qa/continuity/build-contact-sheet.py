#!/usr/bin/env python3
"""Build a deterministic promoted-page thumbnail contact sheet."""

import argparse

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
COLS = 5
THUMB = (120, 180)
LABEL_H = 24
GUTTER = 8

parser = argparse.ArgumentParser()
parser.add_argument("--start", type=int, default=1)
parser.add_argument("--end", type=int, default=10)
parser.add_argument("--output", default="contact-sheet.png")
args = parser.parse_args()

if args.start < 1 or args.end < args.start:
    raise SystemExit("invalid page range")

page_count = args.end - args.start + 1
rows = (page_count + COLS - 1) // COLS
width = GUTTER + COLS * (THUMB[0] + GUTTER)
height = GUTTER + rows * (THUMB[1] + LABEL_H + GUTTER)
sheet = Image.new("RGB", (width, height), (28, 25, 23))
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default()

for page in range(args.start, args.end + 1):
    source = ROOT / "pages" / f"page-{page:02d}.png"
    with Image.open(source) as image:
        thumb = image.convert("RGB").resize(THUMB, Image.Resampling.LANCZOS)
    index = page - args.start
    col = index % COLS
    row = index // COLS
    x = GUTTER + col * (THUMB[0] + GUTTER)
    y = GUTTER + row * (THUMB[1] + LABEL_H + GUTTER)
    sheet.paste(thumb, (x, y))
    label = f"PAGE {page:02d}"
    bbox = draw.textbbox((0, 0), label, font=font)
    label_x = x + (THUMB[0] - (bbox[2] - bbox[0])) // 2
    draw.text((label_x, y + THUMB[1] + 6), label, fill=(235, 228, 213), font=font)

output = ROOT / "qa" / "continuity" / args.output
sheet.save(output, format="PNG", optimize=False)
print(output)
