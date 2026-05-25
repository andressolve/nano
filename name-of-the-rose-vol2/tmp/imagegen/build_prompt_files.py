#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "04-SCRIPT.md"
OUT_DIR = ROOT / "tmp" / "imagegen" / "page-prompts"

BASE_WRAPPER = """STYLE: Finished page art for a serious mature historical graphic novel, 3:2 landscape, 1536x1024. Oil-painting realism for all painted scenes: muted cold stone grey, deep burgundy, candle amber, snow white, ink black, vellum cream; natural light only; heavy chiaroscuro; painterly brushwork; late-November 1327 in a cold Italian Apennine abbey.

NOT a children's book. Serious mature graphic novel, realistic human proportions, period-realistic faces. NOT a modern comic: no halftones, no cel shading, no ink-line cartooning.

If the page is an illuminated manuscript page, follow the script's illuminated-folio layout: gold leaf, lapis, border ornament, Gothic blackletter tags, and a realistic painted miniature inside the page. If the page is a hybrid teaching page, preserve the requested split layout and readable teaching text. If the page uses the dream register, preserve the slightly skewed, uneasy medieval dream look while keeping oil-painting realism. If the page uses the fire palette, keep the warm orange fire restrained and meaningful against the cold blue-grey world unless the script explicitly says the whole building is burning.

REFERENCE IMAGES: any input images supplied to this generation are visual locks for faces, clothing, architecture, artifacts, body type, and signature accessories only. Preserve those identities and objects, but do not copy reference labels, reference-sheet borders, neutral reference backgrounds, or lineup poses into the final page.

LETTERING RULES: The PROJECT SCRIPT below is authoritative. Render every caption, speech bubble, Latin tag, English helper, map label, and page note exactly as supplied in the script. Text inside markdown backticks is the text to draw; do not draw the backtick characters. Asterisks around a title or word indicate italic styling; do not draw the asterisks themselves unless the script explicitly asks for visible asterisks. Do not draw markdown bullets, blockquote marks, headings, or explanatory parentheticals as page lettering. No quotation marks inside speech bubbles unless the script explicitly includes them. Use large high-contrast parchment caption boxes and readable dark serif ink. Do not duplicate text. Do not invent extra captions, labels, signatures, watermarks, or signage.

PERIOD RULES: Romanesque round arches only, no Gothic pointed arches. Vellum codices and scrolls only, no printed books. No modern eyeglasses; William's spectacles are riveted leather-and-glass medieval spectacles. No modern clothing, no Renaissance clothing, no modern logos.

PROJECT SCRIPT FOR THIS PAGE:
"""


def slug_for(title: str) -> str:
    if title == "COVER":
        return "page-00-cover"
    match = re.match(r"P(\d+)", title)
    if not match:
        raise ValueError(f"Unexpected section title: {title}")
    return f"page-{int(match.group(1)):02d}"


def main() -> None:
    text = SCRIPT.read_text()
    pattern = re.compile(r"^## (COVER|P\d+\b[^\n]*)", re.M)
    matches = list(pattern.finditer(text))
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    written = []
    skipped = []
    for i, match in enumerate(matches):
        header = match.group(1)
        title = "COVER" if header == "COVER" else re.match(r"P\d+", header).group(0)
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else text.find("\n## Notes for production", start)
        if end == -1:
            end = len(text)
        section = text[start:end].strip()
        out_path = OUT_DIR / f"{slug_for(title)}.txt"
        if out_path.exists():
            skipped.append(out_path.name)
            continue
        out_path.write_text(BASE_WRAPPER + "\n\n" + section + "\n")
        written.append(out_path.name)

    print(f"written {len(written)} prompt files")
    for name in written:
        print(f"W {name}")
    print(f"skipped {len(skipped)} existing prompt files")
    for name in skipped:
        print(f"S {name}")


if __name__ == "__main__":
    main()
