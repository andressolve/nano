#!/usr/bin/env python3
"""Build the cartouche exhibit plates from verified Gardiner sign sequences.

Signs are rendered from Noto Sans Egyptian Hieroglyphs via unicodedata lookup —
the model never freehands a load-bearing glyph string. Sequences verified in
RESEARCH.md against British Museum teaching diagrams.
"""
import unicodedata
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
REFS = HERE.parent / "refs"
GLYPH_FONT_PATH = HERE / "NotoSansEgyptianHieroglyphs-Regular.ttf"

CREAM = (245, 236, 215)
CARD_EDGE = (208, 196, 168)
INK = (30, 36, 48)
GOLD = (217, 164, 65)
LABEL_INK = (90, 76, 50)

def glyph(code: str) -> str:
    return unicodedata.lookup(f"EGYPTIAN HIEROGLYPH {code}")

# (gardiner_code, letter_annotation or None)
PTOLEMY = [
    ("Q003", "P"), ("X001", "T"), ("V004", "O"), ("E023", "L"),
    ("G017", "M"), ("M017", "I"), ("M017", "I"), ("S029", "S"),
]
CLEOPATRA = [
    ("N029", "K"), ("E023", "L"), ("M017", "E"), ("V004", "O"),
    ("Q003", "P"), ("G001", "A"), ("D046", "T"), ("D021", "R"),
    ("G001", "A"), ("X001", None), ("H008", None),
]
RAMESSES = [("N005", None), ("F031", None), ("S029", None), ("S029", None)]
THUTMOSE = [("G026", None), ("F031", None), ("S029", None)]

CLUE_KEY = [
    ("E023", "LION = L"),
    ("S029", "FOLDED CLOTH = S"),
    ("N005", "SUN DISC = RA"),
    ("G026", "IBIS = THOTH"),
]

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

def glyph_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(GLYPH_FONT_PATH), size)

GSIZE = 84
GFONT = glyph_font(GSIZE)
SLOT_W = 118          # fixed slot per sign so annotations align
SIGN_BAND_H = 150

def draw_sign(draw: ImageDraw.ImageDraw, code: str, cx: int, cy: int):
    ch = glyph(code)
    l, t, r, b = draw.textbbox((0, 0), ch, font=GFONT)
    draw.text((cx - (l + r) / 2, cy - (t + b) / 2), ch, font=GFONT, fill=INK)

def draw_cartouche(draw, x, y, signs, annotate: bool, letter_font,
                   ann_gap=46) -> list[tuple[int, int]]:
    """Draw one horizontal cartouche at (x, y) top-left of the sign band.
    Returns list of sign center (cx, cy) coordinates."""
    n = len(signs)
    inner_w = n * SLOT_W
    pad = 34
    oval_l, oval_t = x, y
    oval_r, oval_b = x + inner_w + 2 * pad, y + SIGN_BAND_H
    # cartouche rope: rounded rect + end bar
    draw.rounded_rectangle([oval_l, oval_t, oval_r, oval_b],
                           radius=SIGN_BAND_H // 2, outline=INK, width=7)
    draw.line([(oval_r + 12, oval_t + 14), (oval_r + 12, oval_b - 14)],
              fill=INK, width=9)
    centers = []
    cy = (oval_t + oval_b) // 2
    for i, (code, letter) in enumerate(signs):
        cx = oval_l + pad + i * SLOT_W + SLOT_W // 2
        draw_sign(draw, code, cx, cy)
        centers.append((cx, cy))
        if annotate and letter:
            l, t, r, b = draw.textbbox((0, 0), letter, font=letter_font)
            draw.text((cx - (r - l) / 2, oval_b + ann_gap - (b - t) / 2),
                      letter, font=letter_font, fill=LABEL_INK)
    return centers

def new_card(w, h):
    img = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, w - 7, h - 7], outline=CARD_EDGE, width=3)
    return img, d

def title(d, w, text, y=34, size=40):
    f = serif_font(size)
    l, t, r, b = d.textbbox((0, 0), text, font=f)
    d.text(((w - (r - l)) / 2, y), text, font=f, fill=LABEL_INK)

def cartouche_width(n):
    return n * SLOT_W + 2 * 34 + 20  # signs + oval padding + end bar

def build_single(path, label, signs, annotate):
    n = len(signs)
    cw = cartouche_width(n)
    w = max(cw + 160, 900)
    h = 430 if annotate else 360
    img, d = new_card(w, h)
    title(d, w, label)
    lf = serif_font(44)
    draw_cartouche(d, (w - cw) // 2, 130, signs, annotate, lf)
    img.save(path)
    print(f"wrote {path} ({w}x{h})")

def build_ramesses_thutmose(path):
    w, h = 1100, 640
    img, d = new_card(w, h)
    lf = serif_font(40)
    f = serif_font(36)
    title(d, w, "TWO ROYAL NAMES — ABU SIMBEL", size=40)
    cw1 = cartouche_width(len(RAMESSES))
    cw2 = cartouche_width(len(THUTMOSE))
    d.text((80, 132), "FIRST NAME:", font=f, fill=LABEL_INK)
    draw_cartouche(d, (w - cw1) // 2, 180, RAMESSES, False, lf)
    d.text((80, 392), "SECOND NAME:", font=f, fill=LABEL_INK)
    draw_cartouche(d, (w - cw2) // 2, 440, THUTMOSE, False, lf)
    img.save(path)
    print(f"wrote {path} ({w}x{h})")

def build_clue_key(path):
    w, h = 1500, 380
    img, d = new_card(w, h)
    title(d, w, "THE CLUE KEY", size=42)
    f = serif_font(34)
    cell = w // len(CLUE_KEY)
    for i, (code, caption) in enumerate(CLUE_KEY):
        cx = cell * i + cell // 2
        # gold pin dot above each entry
        d.ellipse([cx - 9, 108, cx + 9, 126], fill=GOLD, outline=INK, width=2)
        big = glyph_font(110)
        ch = glyph(code)
        l, t, r, b = d.textbbox((0, 0), ch, font=big)
        d.text((cx - (l + r) / 2, 220 - (t + b) / 2), ch, font=big, fill=INK)
        l, t, r, b = d.textbbox((0, 0), caption, font=f)
        d.text((cx - (r - l) / 2, 300), caption, font=f, fill=LABEL_INK)
    img.save(path)
    print(f"wrote {path} ({w}x{h})")

def build_exhibit_p10(path):
    """Cross-check splash exhibit: both cartouches stacked, gold connector
    lines on the shared P / O / L signs, T-wrinkle flagged."""
    w, h = 1600, 1000
    img, d = new_card(w, h)
    title(d, w, "THE CROSS-CHECK", y=30, size=46)
    f = serif_font(36)
    lf = serif_font(42)
    cw_p = cartouche_width(len(PTOLEMY))
    cw_c = cartouche_width(len(CLEOPATRA))
    d.text((90, 128), "NAME ONE — FROM THE STONE:", font=f, fill=LABEL_INK)
    top = draw_cartouche(d, (w - cw_p) // 2, 185, PTOLEMY, True, lf)
    lbl2 = "NAME TWO — FROM THE OBELISK:"
    l, t, r, b = d.textbbox((0, 0), lbl2, font=f)
    d.text((w - (r - l) - 90, 560), lbl2, font=f, fill=LABEL_INK)
    bot = draw_cartouche(d, (w - cw_c) // 2, 620, CLEOPATRA, True, lf)
    # gold connectors: P (ptol 0 -> cleo 4), O (2 -> 3), L (3 -> 1)
    # start below the top letter row, end just above the bottom cartouche
    for pi, ci in [(0, 4), (2, 3), (3, 1)]:
        (x1, y1), (x2, y2) = top[pi], bot[ci]
        d.line([(x1, y1 + SIGN_BAND_H // 2 + 110), (x2, y2 - SIGN_BAND_H // 2 - 16)],
               fill=GOLD, width=8)
        for (gx, gy) in [(x1, y1 + SIGN_BAND_H // 2 + 110),
                         (x2, y2 - SIGN_BAND_H // 2 - 16)]:
            d.ellipse([gx - 11, gy - 11, gx + 11, gy + 11],
                      fill=GOLD, outline=INK, width=2)
    verdict = "SAME SIGN, SAME SOUND, IN BOTH NAMES."
    vf = serif_font(40)
    l, t, r, b = d.textbbox((0, 0), verdict, font=vf)
    d.text(((w - (r - l)) / 2, 910), verdict, font=vf, fill=INK)
    img.save(path)
    print(f"wrote {path} ({w}x{h})")

if __name__ == "__main__":
    REFS.mkdir(exist_ok=True)
    build_single(REFS / "plate_ptolemy.png",
                 "THE KING'S NAME — EXHIBIT A", PTOLEMY, annotate=True)
    build_single(REFS / "plate_ptolemy_clean.png",
                 "THE SEALED NAME", PTOLEMY, annotate=False)
    build_single(REFS / "plate_cleopatra.png",
                 "THE QUEEN'S NAME — EXHIBIT B", CLEOPATRA, annotate=True)
    build_ramesses_thutmose(REFS / "plate_ramesses_thutmose.png")
    build_clue_key(REFS / "plate_clue_key.png")
    build_exhibit_p10(REFS / "exhibit_p10.png")
