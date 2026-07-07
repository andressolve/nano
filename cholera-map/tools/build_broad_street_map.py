#!/usr/bin/env python3
"""Build the Broad Street death-map and evidence exhibit plates locally.

The map's geometry (street layout, pump positions, death-bar density) is the
volume's central image risk -- it is drawn deterministically here from a
simplified schematic matching the real historical pattern (dense death-bar
cluster around the Broad Street pump, thinning with distance; brewery/
workhouse-area pumps essentially spared) rather than left for the model to
freehand. Not a literal facsimile of Snow's 1855 engraving -- a legible,
stylized period exhibit board.
"""
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
REFS = HERE.parent / "refs"

CREAM = (245, 236, 215)
CARD_EDGE = (208, 196, 168)
INK = (30, 36, 48)
GOLD = (217, 164, 65)
LABEL_INK = (90, 76, 50)
STREET = (150, 138, 112)
DEATH_BAR = (30, 36, 48)

random.seed(7)


def serif_font(size: int) -> ImageFont.FreeTypeFont:
    for cand in (
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
        "/System/Library/Fonts/Times.ttc",
    ):
        try:
            return ImageFont.truetype(cand, size)
        except OSError:
            continue
    return ImageFont.load_default(size)


def new_card(w, h):
    img = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, w - 7, h - 7], outline=CARD_EDGE, width=3)
    return img, d


def title(d, w, text, y=28, size=40):
    f = serif_font(size)
    l, t, r, b = d.textbbox((0, 0), text, font=f)
    d.text(((w - (r - l)) / 2, y), text, font=f, fill=LABEL_INK)


# ---------------------------------------------------------------------------
# Street geometry -- a simplified schematic, streets meeting at odd angles,
# matching 01-STYLE-GUIDE.md Sec5 / 02-CHARACTERS.md street list.
# ---------------------------------------------------------------------------

STREETS = {
    "BROAD STREET":       [(120, 560), (900, 520), (1300, 500)],
    "CAMBRIDGE STREET":   [(560, 120), (600, 520), (650, 940)],
    "POLAND STREET":      [(880, 100), (900, 520), (940, 940)],
    "BERWICK STREET":     [(300, 140), (330, 520), (370, 960)],
    "MARLBOROUGH STREET": [(760, 960), (900, 700), (1180, 480)],
}

# The Broad Street / Cambridge Street junction -- the index pump.
BROAD_ST_PUMP = (600, 520)

# Secondary neighbourhood pumps, all clear of the Broad Street cluster.
OTHER_PUMPS = [
    (330, 250, "BERWICK ST PUMP"),
    (940, 250, "POLAND ST PUMP"),
    (1180, 620, "MARLBOROUGH ST PUMP"),
    (370, 820, "BERWICK ST (S) PUMP"),
    (900, 850, "MARLBOROUGH ST (S) PUMP"),
]


def draw_streets(d):
    for pts in STREETS.values():
        d.line(pts, fill=STREET, width=10)


def draw_street_labels(d, f):
    labels = {
        "BROAD STREET": (140, 566, 0),
        "CAMBRIDGE STREET": (566, 130, 90),
        "POLAND STREET": (886, 105, 90),
        "BERWICK STREET": (222, 145, 90),
        "MARLBOROUGH STREET": (990, 820, -35),
    }
    for name, (x, y, angle) in labels.items():
        if angle == 0:
            d.text((x, y - 34), name, font=f, fill=LABEL_INK)
        else:
            txt_img = Image.new("RGBA", (300, 40), (0, 0, 0, 0))
            td = ImageDraw.Draw(txt_img)
            td.text((0, 0), name, font=f, fill=LABEL_INK)
            rot = txt_img.rotate(angle, expand=True)
            d.bitmap((x, y), rot.convert("1"), fill=LABEL_INK) if False else None
            # paste with alpha so rotation renders correctly
            d._image.paste(rot, (x, y), rot) if hasattr(d, "_image") else None


def paste_rotated_label(img, name, x, y, angle, f):
    txt_img = Image.new("RGBA", (340, 46), (0, 0, 0, 0))
    td = ImageDraw.Draw(txt_img)
    td.text((0, 0), name, font=f, fill=LABEL_INK)
    bbox = txt_img.getbbox()
    if bbox:
        txt_img = txt_img.crop(bbox)
    rot = txt_img.rotate(angle, expand=True, resample=Image.BICUBIC)
    img.paste(rot, (x, y), rot)


def draw_pump(d, x, y, r=16):
    d.ellipse([x - r, y - r, x + r, y + r], outline=INK, width=5, fill=CREAM)
    d.line([x - r, y, x + r, y], fill=INK, width=5)
    d.line([x, y - r, x, y + r], fill=INK, width=5)


def label_halo(d, x, y, text, font, pad=6):
    """Cream halo box behind a label so it reads over death bars."""
    l, t, r, b = d.textbbox((x, y), text, font=font)
    d.rectangle([l - pad, t - pad, r + pad, b + pad], fill=CREAM, outline=CARD_EDGE, width=2)
    d.text((x, y), text, font=font, fill=LABEL_INK)


def death_bar_positions(center, n, spread, seed_offset):
    rnd = random.Random(1000 + seed_offset)
    pts = []
    tries = 0
    while len(pts) < n and tries < n * 20:
        tries += 1
        ang = rnd.uniform(0, 6.283)
        dist = abs(rnd.gauss(0, spread))
        x = center[0] + dist * (1 if rnd.random() < 0.5 else -1) * abs(_cos(ang))
        y = center[1] + dist * (1 if rnd.random() < 0.5 else -1) * abs(_sin(ang))
        pts.append((x, y))
    return pts


import math
def _cos(a): return math.cos(a)
def _sin(a): return math.sin(a)


def death_cluster(center, n, max_r, seed):
    """n bars scattered with density falling off from center, capped at max_r."""
    rnd = random.Random(seed)
    pts = []
    for _ in range(n):
        # bias distance toward center (sqrt gives denser near 0)
        dist = (rnd.random() ** 1.8) * max_r
        ang = rnd.uniform(0, 2 * math.pi)
        x = center[0] + dist * math.cos(ang)
        y = center[1] + dist * math.sin(ang)
        pts.append((x, y))
    return pts


def draw_death_bars(d, pts):
    for (x, y) in pts:
        h = random.Random(int(x * 7 + y * 13)).randint(10, 22)
        d.rectangle([x - 3, y - h, x + 3, y], fill=DEATH_BAR)


def build_map(path, title_text, labeled: bool, solved: bool):
    w, h = 1500, 1050
    img, d = new_card(w, h)
    draw_streets(d)

    f_label = serif_font(24)
    f_small = serif_font(20)

    if labeled:
        paste_rotated_label(img, "BROAD STREET", 150, 590, 0, f_label)
        paste_rotated_label(img, "CAMBRIDGE STREET", 566, 130, -85, f_label)
        paste_rotated_label(img, "POLAND STREET", 886, 105, -85, f_label)
        paste_rotated_label(img, "BERWICK STREET", 222, 145, -85, f_label)
        paste_rotated_label(img, "MARLBOROUGH STREET", 980, 830, 32, f_label)
        d = ImageDraw.Draw(img)

    # dense death cluster around the Broad Street pump
    main_cluster = death_cluster(BROAD_ST_PUMP, 210, 140, seed=42)
    # thinning outward ring
    outer_cluster = death_cluster(BROAD_ST_PUMP, 40, 340, seed=99)
    draw_death_bars(d, main_cluster)
    draw_death_bars(d, outer_cluster)

    # a handful of scattered bars near the far pumps -- sparse, illustrating
    # "their own pump, spared" by comparison, never zero (real pattern).
    for (px, py, _name) in OTHER_PUMPS:
        sparse = death_cluster((px, py), 3, 60, seed=int(px + py))
        draw_death_bars(d, sparse)

    draw_pump(d, *BROAD_ST_PUMP, r=20)
    for (px, py, name) in OTHER_PUMPS:
        draw_pump(d, px, py)
        if labeled:
            label_halo(d, px - 60, py + 24, name, f_small)

    if labeled:
        label_halo(d, BROAD_ST_PUMP[0] - 70, BROAD_ST_PUMP[1] - 66,
                   "BROAD STREET PUMP", f_small)

    if solved:
        rr = 60
        d.ellipse([BROAD_ST_PUMP[0] - rr, BROAD_ST_PUMP[1] - rr,
                   BROAD_ST_PUMP[0] + rr, BROAD_ST_PUMP[1] + rr],
                  outline=GOLD, width=10)

    title(d, w, title_text, size=42)
    if labeled:
        note = "Each bar = one death, at the house where it occurred. Circle = a public pump."
        f_note = serif_font(22)
        l, t, r, b = d.textbbox((0, 0), note, font=f_note)
        d.text(((w - (r - l)) / 2, h - 46), note, font=f_note, fill=LABEL_INK)

    img.save(path)
    print(f"wrote {path} ({w}x{h})")


def build_cesspool_diagram(path):
    w, h = 1400, 950
    img, d = new_card(w, h)
    title(d, w, "THE CESSPOOL EXHIBIT — CROSS-SECTION", size=38)

    ground_y = 260
    d.line([(60, ground_y), (w - 60, ground_y)], fill=INK, width=6)

    # houses above ground, simple facade shapes
    for hx in (140, 260, 380):
        d.rectangle([hx, ground_y - 130, hx + 100, ground_y], outline=INK, width=4)
        d.polygon([(hx - 10, ground_y - 130), (hx + 50, ground_y - 175),
                    (hx + 110, ground_y - 130)], outline=INK, width=4)

    # well shaft
    well_x = 620
    well_top_w = 70
    d.rectangle([well_x - well_top_w, ground_y - 20, well_x + well_top_w, ground_y + 10],
                outline=INK, width=5)
    d.rectangle([well_x - 40, ground_y, well_x + 40, ground_y + 640], outline=INK, width=6)
    # water at the bottom of the well
    d.rectangle([well_x - 36, ground_y + 560, well_x + 36, ground_y + 636],
                fill=(163, 197, 200))
    f_lbl = serif_font(28)
    d.text((well_x - 30, ground_y - 60), "WELL", font=f_lbl, fill=LABEL_INK)

    # cesspool, brick-lined pit, ~3ft (drawn as a clearly narrow gap) away
    cess_x = well_x + 210
    d.rectangle([cess_x, ground_y + 40, cess_x + 160, ground_y + 340],
                outline=INK, width=6)
    # brick coursing lines
    for by in range(ground_y + 60, ground_y + 330, 26):
        d.line([(cess_x, by), (cess_x + 160, by)], fill=CARD_EDGE, width=3)
    # foul contents tint
    d.rectangle([cess_x + 8, ground_y + 200, cess_x + 152, ground_y + 332],
                fill=(120, 108, 70))
    d.text((cess_x + 10, ground_y - 60), "CESSPOOL", font=f_lbl, fill=LABEL_INK)

    # the leak: a crack in the cesspool wall nearest the well, gold arrow to the well
    crack_x = cess_x
    crack_y = ground_y + 230
    d.line([(crack_x, crack_y - 20), (crack_x - 6, crack_y), (crack_x + 4, crack_y + 22),
            (crack_x - 4, crack_y + 40)], fill=GOLD, width=6)
    d.line([(cess_x - 4, crack_y + 10), (well_x + 40, ground_y + 300)],
           fill=GOLD, width=6)
    for (gx, gy) in [(cess_x - 4, crack_y + 10), (well_x + 40, ground_y + 300)]:
        d.ellipse([gx - 10, gy - 10, gx + 10, gy + 10], fill=GOLD, outline=INK, width=2)

    # dimension marker between well and cesspool, well clear of the ground line
    dim_y = ground_y + 130
    d.line([(well_x + 40, dim_y), (cess_x, dim_y)], fill=INK, width=3)
    d.line([(well_x + 40, dim_y - 10), (well_x + 40, dim_y + 10)], fill=INK, width=3)
    d.line([(cess_x, dim_y - 10), (cess_x, dim_y + 10)], fill=INK, width=3)
    f_dim = serif_font(30)
    d.text(((well_x + 40 + cess_x) / 2 - 70, dim_y - 46), "ABOUT 3 FEET",
           font=f_dim, fill=INK)

    caption = "The well and the cesspool stood a few feet apart. The brickwork between them had failed."
    f_cap = serif_font(24)
    l, t, r, b = d.textbbox((0, 0), caption, font=f_cap)
    d.text(((w - (r - l)) / 2, h - 60), caption, font=f_cap, fill=LABEL_INK)

    img.save(path)
    print(f"wrote {path} ({w}x{h})")


def build_grand_experiment_table(path):
    w, h = 1300, 800
    img, d = new_card(w, h)
    title(d, w, "THE GRAND EXPERIMENT", size=44)
    sub = "Deaths from cholera per 10,000 houses, by water company"
    f_sub = serif_font(26)
    l, t, r, b = d.textbbox((0, 0), sub, font=f_sub)
    d.text(((w - (r - l)) / 2, 96), sub, font=f_sub, fill=LABEL_INK)

    col_w = w // 2
    f_name = serif_font(30)
    f_num = serif_font(120)
    f_unit = serif_font(24)

    cols = [
        ("SOUTHWARK & VAUXHALL", "315", (col_w // 2, 0)),
        ("LAMBETH", "37", (col_w // 2 + col_w, 0)),
    ]
    d.line([(col_w, 170), (col_w, h - 90)], fill=CARD_EDGE, width=3)

    for name, num, (cx, _off) in cols:
        l, t, r, b = d.textbbox((0, 0), name, font=f_name)
        d.text((cx - (r - l) / 2, 180), name, font=f_name, fill=LABEL_INK)
        l, t, r, b = d.textbbox((0, 0), num, font=f_num)
        color = GOLD if num == "315" else INK
        d.text((cx - (r - l) / 2, 300), num, font=f_num, fill=color)
        unit = "deaths per 10,000 houses"
        l, t, r, b = d.textbbox((0, 0), unit, font=f_unit)
        d.text((cx - (r - l) / 2, 560), unit, font=f_unit, fill=LABEL_INK)

    caption = "Same streets. Same houses. Different water company, different pipes -- and a nine-fold difference in deaths."
    f_cap = serif_font(24)
    l, t, r, b = d.textbbox((0, 0), caption, font=f_cap)
    d.text(((w - (r - l)) / 2, h - 60), caption, font=f_cap, fill=LABEL_INK)

    img.save(path)
    print(f"wrote {path} ({w}x{h})")


if __name__ == "__main__":
    REFS.mkdir(exist_ok=True)
    build_map(REFS / "plate_map_unannotated.png", "SOHO — AUGUST 1854",
               labeled=False, solved=False)
    build_map(REFS / "plate_map_full.png", "THE DEATH MAP — SOHO, 1854",
               labeled=True, solved=False)
    build_map(REFS / "plate_map_solved.png", "THE DEATH MAP — SOHO, 1854",
               labeled=True, solved=True)
    build_cesspool_diagram(REFS / "plate_cesspool_diagram.png")
    build_grand_experiment_table(REFS / "plate_grand_experiment_table.png")
