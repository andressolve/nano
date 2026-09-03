#!/usr/bin/env python3
"""Mechanical verification for the finished Monkey King Vol. I reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 48
EXPECTED_TITLES = ["The Stone Splits","Old Ma's Hand","The Dare","The Water Curtain Cave","Handsome Monkey King","Kings Die Too","The Raft","Out of a Rock","Years of the Broom","Three Taps","The Third Watch","The First Somersault","The Pine Tree","Home in One Leap","Down Through the Water","The Pillar Named","Smaller","Take It and Go","The Hall of Jade","Come Back","The South Gate","Keeper of the Heavenly Horses","The Stables","Below Rank","The Banner","The Army Comes Down","Give Him the Words","Because They Said It","A House of Gold","The Peach Garden","Am I Invited?","The Empty Hall","The Five Gourds","Send Erlang","Which One Do I Hit First?","Shape for Shape","The Temple and the Flagpole","The Ring from Behind","Equals Don't Kneel","The Furnace Sentence","Forty-Nine Days","The Lid","Send for the Buddha","The Wager","The Five Pillars","The Writing on the Finger","The Hand Comes Down","Someone Will Come"]
EXPECTED_MOVEMENTS = [("I · The Stone and the Waterfall",1,7),("II · The Master",8,14),("III · The Staff",15,19),("IV · The Stable Boy",20,29),("V · The Peaches",30,34),("VI · Erlang",35,38),("VII · The Furnace and the Hand",39,48)]

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
            if json.loads("[" + m.group(1) + "]") != EXPECTED_TITLES: problems.append("title array does not match the 48-title manifest")
        except json.JSONDecodeError as e: problems.append(f"title array not JSON-compatible: {e}")
    m = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const movements = [...]")
    else:
        mv = [(t, int(a), int(b)) for t, a, b in re.findall(r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}', m.group(1))]
        if mv != EXPECTED_MOVEMENTS: problems.append("movement array must cover the seven approved ranges exactly")
    for term in ["Monkey King, Volume I: Havoc in Heaven","monte_inspired:monkey-king-vol1:page","monte_inspired:monkey-king-vol1:bookmarks","End of Volume I","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-49") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-50") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Monte Cristo","monte-cristo","nano:","Morcerf","Volume II:","stories.js","../index.html","page-49.png","#page-51"]:
        if term in reader: problems.append(f"stale or foreign term present: {term}")
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
