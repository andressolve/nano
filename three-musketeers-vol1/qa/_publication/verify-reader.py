#!/usr/bin/env python3
"""Mechanical verification for the finished Three Musketeers Vol. I reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 49
EXPECTED_TITLES = ['The Yellow Horse', 'Three Gifts at the Gate', 'The Man in the Window', 'The Stool and the Letter', 'Then So Do I', 'Paris', 'The Door and the Scar', 'A Shoulder in the Way', 'The Baldric', 'The Handkerchief', 'A Quarter to Twelve', 'Noon, and Five Red Cloaks', 'Four of Us', 'The Best Fight of His Life', 'The Third Time, You Stay', 'Four Abreast', 'Two Livres a Week', 'Weeks', 'Out of the Window', 'The Lantern in the Puddle', 'She Only Carries It', 'Only Two', 'She Gave Them Away', 'Are You Asking?', 'So That One Arrives', 'All for One', 'The Saint-Denis Gate', 'I Drink to the Queen', "I'll Hold the Road", 'He Held the Road', 'I Have the Wine and I Have the Door', 'The Sea', 'Closed by Order of the Cardinal', 'Steel on a Plank', 'The Bearer', 'The Richest Man in England', 'Ten', 'Send for My Jeweler', 'Tell Her', 'The Road Home', 'The Kitchen Door', 'Ten Is Ten', 'The Queen Came In', 'Twelve', "d'Artagnan", 'The Ring', 'Did You Arrive?', 'A Fair Trade', 'A Man in Red at a Window']
EXPECTED_MOVEMENTS = [('I · The Yellow Horse', 1, 7), ('II · Three Duels at Noon', 8, 16), ('III · The Girl Downstairs', 17, 22), ('IV · All for One', 23, 27), ('V · The Road', 28, 35), ('VI · London', 36, 40), ('VII · Twelve', 41, 49)]

def main() -> int:
    problems: list[str] = []
    expected_files = [PROJECT / "pages" / f"page-{n:02d}.png" for n in range(1, N + 1)]
    page_files = sorted((PROJECT / "pages").glob("page-*.png"))
    if page_files != expected_files:
        problems.append(f"canonical page set must be exactly page-01.png through page-{N:02d}.png")
    try:
        from PIL import Image
        for path in expected_files:
            if path.exists():
                with Image.open(path) as im:
                    if im.size != (1024, 1536): problems.append(f"{path.name}: expected 1024x1536, got {im.size}")
    except ImportError:
        problems.append("Pillow unavailable; page dimensions not verified")
    reader_path = PROJECT / "index.html"
    reader = reader_path.read_text(encoding="utf-8") if reader_path.exists() else ""
    if not reader: problems.append("index.html is missing")
    m = re.search(r"const\s+titles\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const titles = [...]")
    else:
        try:
            if json.loads("[" + m.group(1) + "]") != EXPECTED_TITLES: problems.append("title array does not match the 49-title manifest")
        except json.JSONDecodeError as e: problems.append(f"title array not JSON-compatible: {e}")
    m = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const movements = [...]")
    else:
        mv = [(t, int(a), int(b)) for t, a, b in re.findall(r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}', m.group(1))]
        if mv != EXPECTED_MOVEMENTS: problems.append("movement array must cover the seven approved ranges exactly")
    for term in ["The Three Musketeers, Volume I: The Queen's Diamonds","monte_inspired:three-musketeers-vol1:page","monte_inspired:three-musketeers-vol1:bookmarks","End of Volume I","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-50") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-51") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Monte Cristo","monte-cristo","nano:","Morcerf","Volume II:","stories.js","page-50.png","#page-52"]:
        if term in reader: problems.append(f"stale or foreign term present: {term}")
    if reader.count('href="../index.html"') != 2: problems.append("expected library return links in toolbar and ending")
    ids = re.findall(r'\bid="([^"]+)"', reader)
    dup = sorted({v for v in ids if ids.count(v) > 1})
    if dup: problems.append("duplicate element IDs: " + ", ".join(dup))
    refs = set(re.findall(r'getElementById\(["\']([^"\']+)["\']\)', reader))
    miss = sorted(refs - set(ids))
    if miss: problems.append("script references missing IDs: " + ", ".join(miss))
    q = len(re.findall(r'class="question"', reader)); a = len(re.findall(r'data-answer="[abc]"', reader))
    if q != 5 or a != 5: problems.append(f"quiz must have five questions and answers; found {q}/{a}")
    for p in problems: print("PROBLEM:", p)
    print("CLEAN" if not problems else f"NOT CLEAN — {len(problems)} problem(s)")
    return 0 if not problems else 1

if __name__ == "__main__":
    sys.exit(main())
