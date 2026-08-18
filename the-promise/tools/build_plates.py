"""Build every load-bearing exhibit plate for "The Promise".

Nothing in these plates is drawn by an image model. Every numeral is computed
here and rendered as text, so the arithmetic on the page is the arithmetic.
"""

import os
import random
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "plates")
os.makedirs(OUT, exist_ok=True)

S = 2  # supersample factor

PAPER = (243, 236, 221)
INK = (38, 34, 30)
FAINT = (176, 168, 152)
LAPIS = (46, 92, 138)
VERM = (180, 68, 46)
GOLD = (176, 140, 62)

F = "/System/Library/Fonts/Supplemental/"


def font(name, size):
    return ImageFont.truetype(F + name, size * S)


SERIF = "Georgia.ttf"
SERIF_B = "Georgia Bold.ttf"
SERIF_I = "Georgia Italic.ttf"


def draw_math(d, x, y, spec, size, fill=INK, bold=False, measure=False):
    """Set a line of mathematics properly.

    spec is a list of (kind, text) or (kind, text, fill):
      't'  upright text        'v'  italic variable
      's'  superscript         'sv' italic superscript
      'o'  binary operator (gets its own spacing on both sides)

    Returns the advance width, so a line can be measured before it is drawn.
    """
    up = font(SERIF_B if bold else SERIF, size)
    it = font(SERIF_I, size)
    ssz = max(9, int(round(size * 0.62)))
    sup_up = font(SERIF_B if bold else SERIF, ssz)
    sup_it = font(SERIF_I, ssz)
    # Align on baselines, not on the top of the glyph box: the superscript sits
    # a third of an em above the baseline it belongs to.
    rise = size * 0.36 - (up.getmetrics()[0] - sup_up.getmetrics()[0]) / S
    gap = size * 0.30

    cx = x
    for tok in spec:
        kind, text = tok[0], tok[1]
        col = tok[2] if len(tok) > 2 else fill
        if kind == "o":
            cx += gap
            f, dy = up, 0
        elif kind == "v":
            f, dy = it, 0
        elif kind == "s":
            f, dy = sup_up, -rise
        elif kind == "sv":
            f, dy = sup_it, -rise
        else:
            f, dy = up, 0
        if not measure:
            d.text((cx * S, (y + dy) * S), text, font=f, fill=col)
        cx += d.textlength(text, font=f) / S
        if kind == "o":
            cx += gap
    return cx - x


def math_width(d, spec, size, bold=False):
    return draw_math(d, 0, 0, spec, size, bold=bold, measure=True)


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factor(n):
    fs, d = [], 2
    while d * d <= n:
        while n % d == 0:
            fs.append(d)
            n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs


def comma(n):
    return f"{n:,}"


def canvas(w, h):
    img = Image.new("RGB", (w * S, h * S), PAPER)
    d = ImageDraw.Draw(img)
    return img, d


def texture(img):
    """Faint paper grain and edge warmth so plates sit on a page, not a screen."""
    px = img.load()
    w, h = img.size
    rnd = random.Random(7)
    for _ in range((w * h) // 40):
        x, y = rnd.randrange(w), rnd.randrange(h)
        r, g, b = px[x, y]
        k = rnd.randint(-7, 4)
        px[x, y] = (max(0, min(255, r + k)), max(0, min(255, g + k)), max(0, min(255, b + k)))
    return img


def finish(img, name):
    img = texture(img)
    img = img.resize((img.width // S, img.height // S), Image.LANCZOS)
    path = os.path.join(OUT, name)
    img.save(path)
    print("wrote", path, img.size)


def center(d, y, text, fnt, fill=INK, w=None):
    tw = d.textlength(text, font=fnt)
    d.text(((w - tw) / 2, y), text, font=fnt, fill=fill)


def title_block(d, w, title, sub=None):
    center(d, 54 * S, title.upper(), font(SERIF_B, 30), INK, w * S)
    y = 100 * S
    if sub:
        center(d, y, sub, font(SERIF_I, 19), (110, 102, 92), w * S)
        y += 34 * S
    d.line([(w * S * 0.30, y + 8 * S), (w * S * 0.70, y + 8 * S)], fill=FAINT, width=2 * S)


def footer(d, w, h, text, fill=(110, 102, 92)):
    center(d, (h - 62) * S, text, font(SERIF_I, 19), fill, w * S)


# ---------------------------------------------------------------- plate 1
def plate_rectangles():
    """What a prime IS - shown as dots, before any notation exists."""
    w, h = 1500, 1000
    img, d = canvas(w, h)
    title_block(d, w, "Numbers that refuse to be rectangles",
                "Every number is a pile of dots. Try to arrange each pile into a full rectangle.")

    nums = list(range(2, 14))
    cols, x0, y0 = 4, 120, 210
    cw, ch = 330, 205
    r = 7

    for i, n in enumerate(nums):
        cx = x0 + (i % cols) * cw
        cy = y0 + (i // cols) * ch
        prime = is_prime(n)

        # best (most square) arrangement
        best = (1, n)
        for a in range(1, int(n ** 0.5) + 1):
            if n % a == 0:
                best = (a, n // a)
        rows, per = best

        d.text((cx * S, cy * S), str(n), font=font(SERIF_B, 27), fill=LAPIS if prime else INK)

        dx, dy = cx + 52, cy + 8
        gap = 18
        # long primes wrap visually as one unbroken line, kept inside the cell
        for k in range(n):
            rr, cc = (k // per, k % per) if not prime else (0, k)
            px = dx + cc * gap
            py = dy + rr * gap
            col = LAPIS if prime else (120, 112, 100)
            d.ellipse([(px - r) * S, (py - r) * S, (px + r) * S, (py + r) * S], fill=col)

        label = f"{rows} × {per}" if not prime else "only 1 × %d" % n
        d.text((cx * S, (cy + 118) * S), label, font=font(SERIF, 17),
               fill=LAPIS if prime else (140, 132, 120))

    d.line([(120 * S, 828 * S), ((w - 120) * S, 828 * S)], fill=FAINT, width=2 * S)
    center(d, 858 * S, "The blue ones can only ever be a single line.", font(SERIF_B, 25), LAPIS, w * S)
    center(d, 902 * S, "Those are the primes. They cannot be built out of smaller numbers,",
           font(SERIF, 21), INK, w * S)
    center(d, 934 * S, "which is why everything else can be built out of them.",
           font(SERIF, 21), INK, w * S)
    finish(img, "plate-01-rectangles.png")


# ---------------------------------------------------------------- plate 2
def plate_thinning():
    """The honest evidence: primes thin out. This is what makes the question real."""
    w, h = 1500, 1180
    img, d = canvas(w, h)
    title_block(d, w, "They are running out",
                "Every dot is a number. The blue dots are prime.")

    y = 208
    counts = []
    for band in range(10):
        lo = band * 100 + 1
        hi = (band + 1) * 100
        c = 0
        d.text((120 * S, (y + 12) * S), f"{comma(lo)}-{comma(hi)}", font=font(SERIF, 17), fill=(120, 112, 100))
        for k in range(100):
            n = lo + k
            px = 340 + (k % 50) * 17
            py = y + (k // 50) * 17
            if is_prime(n):
                c += 1
                d.ellipse([(px - 5) * S, (py - 5) * S, (px + 5) * S, (py + 5) * S], fill=LAPIS)
            else:
                d.ellipse([(px - 2) * S, (py - 2) * S, (px + 2) * S, (py + 2) * S], fill=(210, 202, 186))
        counts.append(c)
        d.text((1250 * S, (y + 12) * S), f"{c:>2} primes", font=font(SERIF_B, 19),
               fill=INK if c > 14 else VERM)
        y += 48

    # the jump to a million
    d.line([(340 * S, (y + 10) * S), (1180 * S, (y + 10) * S)], fill=FAINT, width=2 * S)
    center(d, (y + 24) * S, ". . .   nine hundred and ninety-nine thousand numbers later   . . .",
           font(SERIF_I, 19), (140, 132, 120), w * S)
    y += 68
    lo, hi = 999901, 1000000
    c = sum(1 for n in range(lo, hi + 1) if is_prime(n))
    d.text((120 * S, (y + 12) * S), "999,901-1,000,000", font=font(SERIF, 17), fill=(120, 112, 100))
    for k in range(100):
        n = lo + k
        px = 340 + (k % 50) * 17
        py = y + (k // 50) * 17
        if is_prime(n):
            d.ellipse([(px - 5) * S, (py - 5) * S, (px + 5) * S, (py + 5) * S], fill=LAPIS)
        else:
            d.ellipse([(px - 2) * S, (py - 2) * S, (px + 2) * S, (py + 2) * S], fill=(210, 202, 186))
    d.text((1250 * S, (y + 12) * S), f"{c:>2} primes", font=font(SERIF_B, 19), fill=VERM)

    y += 92
    center(d, y * S, "Twenty-five in the first hundred. Eight in the hundred before a million.",
           font(SERIF_B, 23), INK, w * S)
    y += 40
    center(d, y * S, "They get rarer the further you walk. So it is perfectly reasonable to wonder",
           font(SERIF, 20), INK, w * S)
    y += 32
    center(d, y * S, "whether they eventually stop altogether.", font(SERIF, 20), INK, w * S)
    footer(d, w, h, "(The thinning is not tidy: the fifth hundred holds 17, more than the 16 before it.)")
    finish(img, "plate-02-thinning.png")


# ---------------------------------------------------------------- plate 3
def plate_euclid_machine():
    """The proof, run six times, including the case that breaks the pretty pattern."""
    w, h = 1560, 1060
    img, d = canvas(w, h)
    title_block(d, w, "Euclid's machine",
                "Hand it any finite list of primes. It hands back a prime the list does not contain.")

    cols = [110, 470, 700, 1040]
    heads = ["THE LIST YOU HAND IT", "MULTIPLY, ADD ONE", "WHAT THAT NUMBER IS", "THE NEW PRIME(S)"]
    for x, t in zip(cols, heads):
        d.text((x * S, 205 * S), t, font=font(SERIF_B, 16), fill=(140, 132, 120))
    d.line([(110 * S, 232 * S), ((w - 110) * S, 232 * S)], fill=INK, width=2 * S)

    ps = [2, 3, 5, 7, 11, 13]
    y = 254
    N = 1
    for k in range(6):
        N *= ps[k]
        val = N + 1
        fs = factor(val)
        prime = len(fs) == 1
        last = k == 5
        col = VERM if last else INK

        if last:
            d.rectangle([(96 * S, (y - 14) * S), ((w - 96) * S, (y + 74) * S)], fill=(250, 240, 233))

        d.text((cols[0] * S, y * S), " × ".join(str(p) for p in ps[:k + 1]),
               font=font(SERIF, 24), fill=INK)
        d.text((cols[1] * S, y * S), comma(val), font=font(SERIF_B, 26), fill=col)
        if prime:
            d.text((cols[2] * S, y * S), "prime itself", font=font(SERIF_I, 23), fill=LAPIS)
            d.text((cols[3] * S, y * S), comma(val), font=font(SERIF_B, 24), fill=LAPIS)
        else:
            d.text((cols[2] * S, y * S), " × ".join(comma(f) for f in fs),
                   font=font(SERIF_B, 24), fill=VERM)
            d.text((cols[3] * S, y * S), " and ".join(comma(f) for f in fs),
                   font=font(SERIF_B, 24), fill=LAPIS)
        if last:
            d.text((cols[2] * S, (y + 34) * S), "NOT prime — the pattern breaks here",
                   font=font(SERIF_I, 19), fill=VERM)
            d.text((cols[3] * S, (y + 34) * S), "neither is on the list",
                   font=font(SERIF_I, 19), fill=(110, 102, 92))
        y += 88 if not last else 108

    d.line([(110 * S, (y + 6) * S), ((w - 110) * S, (y + 6) * S)], fill=INK, width=2 * S)
    y += 40
    center(d, y * S, "The sixth row is the one that matters.", font(SERIF_B, 26), VERM, w * S)
    y += 44
    center(d, y * S, "30,031 is not prime — so the machine does not work the way it first appears.",
           font(SERIF, 21), INK, w * S)
    y += 32
    center(d, y * S, "It does not promise a new prime. It promises a new prime FACTOR.",
           font(SERIF, 21), INK, w * S)
    y += 32
    center(d, y * S, "59 and 509 were not on the list either. The machine still wins.",
           font(SERIF, 21), INK, w * S)
    footer(d, w, h, "The modern form of Elements, Book IX, Proposition 20. Euclid's own version used three primes.")
    finish(img, "plate-03-euclid-machine.png")


# ---------------------------------------------------------------- plate 4
def plate_fermat():
    """Five cases were not enough - for the finest arithmetician of his century."""
    w, h = 1500, 940
    img, d = canvas(w, h)
    center(d, 54 * S, "FIVE CASES WERE NOT ENOUGH", font(SERIF_B, 30), INK, w * S)
    sub = [("v", "Numbers of the form "), ("t", "2"), ("sv", "k"), ("o", "+"), ("t", "1"),
           ("v", ", where the exponent "), ("v", "k"), ("v", " is itself a power of two.")]
    sw = math_width(d, sub, 19)
    draw_math(d, (w - sw) / 2, 100, sub, 19, fill=(110, 102, 92))
    d.line([(w * S * 0.30, 142 * S), (w * S * 0.70, 142 * S)], fill=FAINT, width=2 * S)

    # the expression column is right-aligned on its "=", the values left-aligned after it
    xeq, xv = 560, 1000
    d.text((452 * S, 206 * S), "EACH EXPONENT DOUBLES", font=font(SERIF_B, 14), fill=(158, 150, 138))

    y = 252
    for i in range(6):
        k = 2 ** i
        val = 2 ** k + 1
        col = LAPIS if i < 5 else VERM
        expr = [("t", "2"), ("s", str(k)), ("o", "+"), ("t", "1")]
        ew = math_width(d, expr, 26)
        draw_math(d, xeq - 34 - ew, y, expr, 26)
        d.text(((xeq - 22) * S, y * S), "=", font=font(SERIF, 26), fill=INK)
        draw_math(d, xeq + 22, y - 2, [("t", comma(val))], 28, fill=col, bold=True)
        if i < 5:
            d.text((xv * S, (y + 2) * S), "prime", font=font(SERIF_I, 21), fill=LAPIS)
        y += 60

    fs = factor(2 ** 32 + 1)
    fac = [("o", "="), ("t", comma(fs[0])), ("o", "×"), ("t", comma(fs[1]))]
    draw_math(d, xeq + 22, y - 24, fac, 28, fill=VERM, bold=True)
    d.text((xv * S, (y - 20) * S), "not prime", font=font(SERIF_I, 21), fill=VERM)

    y += 76
    d.line([(150 * S, y * S), ((w - 150) * S, y * S)], fill=FAINT, width=2 * S)
    y += 34
    center(d, y * S, "It took ninety-odd years and Leonhard Euler to find the crack.",
           font(SERIF_B, 24), INK, w * S)
    y += 44
    center(d, y * S, "Four thousand million is a large number to be wrong about,",
           font(SERIF, 21), INK, w * S)
    y += 32
    center(d, y * S, "and Fermat was as good at arithmetic as anyone who has ever lived.",
           font(SERIF, 21), INK, w * S)
    footer(d, w, h, "Checking cases is how you find a rule. It is not how you know one.")
    finish(img, "plate-04-fermat.png")


# ---------------------------------------------------------------- plate 5
def plate_forty_one():
    """Forty straight successes, then failure - the cleanest possible warning."""
    w, h = 1500, 1000
    img, d = canvas(w, h)
    center(d, 54 * S, "THE FORMULA THAT WORKED FORTY TIMES", font(SERIF_B, 30), INK, w * S)
    sub = [("v", "Choose a whole number "), ("v", "n"), ("v", ".  Work out  "),
           ("v", "n"), ("sv", "2"), ("o", "+"), ("v", "n"), ("o", "+"), ("t", "41"),
           ("v", ".  Ask whether the answer is prime.")]
    sw = math_width(d, sub, 19)
    draw_math(d, (w - sw) / 2, 100, sub, 19, fill=(110, 102, 92))
    d.line([(w * S * 0.30, 142 * S), (w * S * 0.70, 142 * S)], fill=FAINT, width=2 * S)

    x0, y0 = 150, 220
    colw, rowh = 168, 40
    for n in range(0, 40):
        val = n * n + n + 41
        cx = x0 + (n % 8) * colw
        cy = y0 + (n // 8) * rowh
        d.text((cx * S, cy * S), f"{n:>2}", font=font(SERIF, 17), fill=(170, 162, 148))
        d.text(((cx + 34) * S, cy * S), comma(val), font=font(SERIF, 19), fill=LAPIS)

    y = y0 + 5 * rowh + 34
    center(d, y * S, "Forty numbers in a row. Every single one prime.", font(SERIF_I, 22),
           (110, 102, 92), w * S)

    y += 66
    val = 40 * 40 + 40 + 41
    assert val == 41 * 41
    d.rectangle([(280 * S, (y - 22) * S), ((w - 280) * S, (y + 162) * S)], fill=(250, 240, 233))

    lead = [("v", "and then, at "), ("v", "n"), ("o", "="), ("t", "40")]
    lw = math_width(d, lead, 19)
    draw_math(d, (w - lw) / 2, y, lead, 19, fill=(150, 142, 130))

    fail = [("t", "40"), ("s", "2"), ("o", "+"), ("t", "40"), ("o", "+"), ("t", "41"),
            ("o", "="), ("t", comma(val)), ("o", "="), ("t", "41"), ("s", "2")]
    fw = math_width(d, fail, 32, bold=True)
    draw_math(d, (w - fw) / 2, y + 34, fail, 32, fill=VERM, bold=True)

    # the reason, which was in the expression the whole time
    r1 = [("v", "n"), ("sv", "2"), ("o", "+"), ("v", "n"), ("o", "+"), ("t", "41"),
          ("v", "   is the same as   "), ("v", "n"), ("t", "("), ("v", "n"), ("o", "+"),
          ("t", "1"), ("t", ")"), ("o", "+"), ("t", "41")]
    r2 = [("v", "so at "), ("v", "n"), ("o", "="), ("t", "40"), ("v", " it is   "),
          ("t", "40"), ("o", "×"), ("t", "41"), ("o", "+"), ("t", "41"), ("o", "="),
          ("t", "41"), ("o", "×"), ("t", "41")]
    for i, spec in enumerate((r1, r2)):
        rw = math_width(d, spec, 20)
        draw_math(d, (w - rw) / 2, y + 96 + i * 32, spec, 20, fill=(140, 100, 86))

    y += 200
    d.line([(150 * S, y * S), ((w - 150) * S, y * S)], fill=FAINT, width=2 * S)
    y += 34
    center(d, y * S, "Forty pieces of evidence, and the forty-first says no.",
           font(SERIF_B, 25), INK, w * S)
    y += 44
    center(d, y * S, "If you had stopped at thirty-nine you would have been certain,",
           font(SERIF, 21), INK, w * S)
    y += 32
    center(d, y * S, "and you would have been wrong. Certain is not the same as right.",
           font(SERIF, 21), INK, w * S)
    footer(d, w, h, "The formula is Euler's. He knew better than to call it a law.")
    finish(img, "plate-05-forty-one.png")


# ---------------------------------------------------------------- plate 6
def plate_parallels():
    """Euclid's fifth postulate is a CHOICE - three consistent answers, drawn exactly."""
    import math

    w, h = 1560, 1000
    img, d = canvas(w, h)
    title_block(d, w, "Three answers, all consistent",
                "Through a point beside a straight line, how many parallels can you draw?")

    panels = [(140, "FLAT", "EXACTLY ONE"), (660, "CURVED OUTWARD", "NONE"),
              (1120, "CURVED INWARD", "MANY")]
    py = 250
    pw, ph = 340, 330

    for px, name, answer in panels:
        d.rectangle([(px * S, py * S), ((px + pw) * S, (py + ph) * S)], outline=FAINT, width=2 * S)
        tw = d.textlength(name, font=font(SERIF_B, 17)) / S
        d.text(((px + (pw - tw) / 2) * S, (py - 34) * S), name,
               font=font(SERIF_B, 17), fill=(140, 132, 120))

    # --- panel 1: the flat plane
    px = 140
    cy = py + 200
    d.line([((px + 40) * S, cy * S), ((px + pw - 40) * S, cy * S)], fill=INK, width=3 * S)
    ppx, ppy = px + pw / 2, cy - 90
    for k in range(0, pw - 80, 14):
        d.line([((px + 40 + k) * S, ppy * S), ((px + 40 + k + 7) * S, ppy * S)], fill=LAPIS, width=3 * S)
    d.ellipse([(ppx - 6) * S, (ppy - 6) * S, (ppx + 6) * S, (ppy + 6) * S], fill=VERM)
    d.text(((px + 44) * S, (cy + 14) * S), "the line", font=font(SERIF_I, 16), fill=(140, 132, 120))
    d.text(((ppx + 14) * S, (ppy - 34) * S), "the point", font=font(SERIF_I, 16), fill=VERM)

    # --- panel 2: the sphere (an octant with three right angles)
    px = 660
    cx, cyy, R = px + pw / 2, py + 150, 104
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    pts = []
    for a in range(180, 271):  # silhouette: pole down to the left of the equator
        t = math.radians(a)
        pts.append(((cx + R * math.cos(t)) * S, (cyy + R * math.sin(t)) * S))
    pts = [((cx + R * math.cos(math.radians(a))) * S, (cyy + R * math.sin(math.radians(a))) * S)
           for a in range(270, 181, -1)]
    eq = [((cx + R * math.cos(math.radians(a))) * S, (cyy + 0.34 * R * math.sin(math.radians(a))) * S)
          for a in range(180, 91, -1)]
    poly = pts + eq + [(cx * S, (cyy - R) * S)]
    od.polygon(poly, fill=(46, 92, 138, 46))
    img.paste(Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB"), (0, 0))
    d = ImageDraw.Draw(img)

    d.ellipse([(cx - R) * S, (cyy - R) * S, (cx + R) * S, (cyy + R) * S], outline=INK, width=3 * S)
    d.ellipse([(cx - R) * S, (cyy - 0.34 * R) * S, (cx + R) * S, (cyy + 0.34 * R) * S],
              outline=(150, 142, 130), width=2 * S)
    d.line([(cx * S, (cyy - R) * S), (cx * S, (cyy + 0.34 * R) * S)], fill=LAPIS, width=3 * S)
    d.line([((cx - R) * S, cyy * S), (cx * S, cyy * S)], fill=(150, 142, 130), width=1 * S)
    for a in range(180, 271):
        t = math.radians(a)
        d.ellipse([((cx + R * math.cos(t)) - 1.5) * S, ((cyy + R * math.sin(t)) - 1.5) * S,
                   ((cx + R * math.cos(t)) + 1.5) * S, ((cyy + R * math.sin(t)) + 1.5) * S], fill=LAPIS)
    for a in range(180, 91, -1):
        t = math.radians(a)
        d.ellipse([((cx + R * math.cos(t)) - 1.5) * S, ((cyy + 0.34 * R * math.sin(t)) - 1.5) * S,
                   ((cx + R * math.cos(t)) + 1.5) * S, ((cyy + 0.34 * R * math.sin(t)) + 1.5) * S], fill=LAPIS)
    # the near half of the equator is "the line", in ink, as in the other two panels
    eqf = [((cx + R * math.cos(math.radians(a))) * S, (cyy + 0.34 * R * math.sin(math.radians(a))) * S)
           for a in range(0, 181)]
    d.line(eqf, fill=INK, width=4 * S)
    # the pole is "the point" - every straight line through it meets the equator
    d.ellipse([(cx - 6) * S, (cyy - R - 6) * S, (cx + 6) * S, (cyy - R + 6) * S], fill=VERM)
    d.text(((px + 26) * S, (py + ph - 62) * S), "every line through the point meets it",
           font=font(SERIF_I, 16), fill=(140, 132, 120))

    # --- panel 3: hyperbolic plane, drawn exactly as a Poincare disk.
    # In this model a "straight line" is an arc of a circle meeting the rim at
    # right angles: centre C with |C|^2 = 1 + r^2.
    px = 1120
    cx, cyy, R = px + pw / 2, py + 150, 104

    def to_px(x, y):
        return ((cx + x * R) * S, (cyy - y * R) * S)

    def geodesic(Cx, Cy):
        r = math.sqrt(Cx * Cx + Cy * Cy - 1.0)
        pts = []
        for a in range(0, 3601):
            t = math.radians(a / 10.0)
            x, y = Cx + r * math.cos(t), Cy + r * math.sin(t)
            if x * x + y * y <= 1.0:
                pts.append(to_px(x, y))
        return pts, r

    def meets(C1, r1, C2, r2):
        dist = math.hypot(C1[0] - C2[0], C1[1] - C2[1])
        if dist > r1 + r2 or dist < abs(r1 - r2):
            return False
        a = (r1 * r1 - r2 * r2 + dist * dist) / (2 * dist)
        hh = r1 * r1 - a * a
        if hh < 0:
            return False
        hh = math.sqrt(hh)
        mx = C1[0] + a * (C2[0] - C1[0]) / dist
        my = C1[1] + a * (C2[1] - C1[1]) / dist
        ux, uy = -(C2[1] - C1[1]) / dist, (C2[0] - C1[0]) / dist
        for s in (1, -1):
            x, y = mx + s * hh * ux, my + s * hh * uy
            if x * x + y * y < 0.999:
                return True
        return False

    d.ellipse([(cx - R) * S, (cyy - R) * S, (cx + R) * S, (cyy + R) * S],
              outline=(196, 188, 172), width=3 * S)

    Lc = (0.0, -1.9)
    Lpts, Lr = geodesic(*Lc)
    d.line(Lpts, fill=INK, width=4 * S)

    # Two geodesics can miss each other and still appear to touch near the rim,
    # which would contradict the caption. Require visible daylight, not just
    # the analytic test.
    def clearance(pts, ref):
        best = 1e18
        for i in range(0, len(pts), 2):
            x1, y1 = pts[i]
            for j in range(0, len(ref), 2):
                dd = (x1 - ref[j][0]) ** 2 + (y1 - ref[j][1]) ** 2
                if dd < best:
                    best = dd
        return math.sqrt(best) / S

    Px, Py = 0.0, 0.34
    Cy = (Px * Px + Py * Py + 1) / (2 * Py)
    cands = []
    for i in range(-40, 41):
        Cx = i * 0.12
        pts, r = geodesic(Cx, Cy)
        if len(pts) < 20 or meets((Cx, Cy), r, Lc, Lr):
            continue
        if clearance(pts, Lpts) < 15:
            continue
        cands.append((Cx, pts))
    # keep three well-spread members of the pencil
    for k in (0, len(cands) // 2, len(cands) - 1):
        d.line(cands[k][1], fill=LAPIS, width=3 * S)

    hx, hy = to_px(Px, Py)
    d.ellipse([hx - 6 * S, hy - 6 * S, hx + 6 * S, hy + 6 * S], fill=VERM)
    d.text(((px + 26) * S, (py + ph - 62) * S), "all of them miss the black line",
           font=font(SERIF_I, 16), fill=(140, 132, 120))

    for px_, _, answer in panels:
        tw = d.textlength(answer, font=font(SERIF_B, 26)) / S
        d.text(((px_ + (pw - tw) / 2) * S, (py + ph + 26) * S), answer,
               font=font(SERIF_B, 26), fill=LAPIS)

    y = py + ph + 96
    d.line([(140 * S, y * S), ((w - 140) * S, y * S)], fill=FAINT, width=2 * S)
    y += 32
    center(d, y * S, "Euclid assumed the first answer. For two thousand years people tried to prove it.",
           font(SERIF, 21), INK, w * S)
    y += 34
    center(d, y * S, "It cannot be proved — because the other two are just as consistent.",
           font(SERIF_B, 24), VERM, w * S)
    y += 40
    center(d, y * S, "Which one the world actually obeys is not a question arithmetic can answer.",
           font(SERIF, 21), INK, w * S)
    footer(d, w, h, "Lobachevsky, published 1829–30  ·  Bolyai, 1832  ·  Gauss, who had it first and never published")
    finish(img, "plate-06-parallels.png")


if __name__ == "__main__":
    plate_rectangles()
    plate_thinning()
    plate_euclid_machine()
    plate_fermat()
    plate_forty_one()
