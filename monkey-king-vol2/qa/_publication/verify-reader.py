#!/usr/bin/env python3
"""Mechanical verification for the finished Monkey King Volume II reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 48
EXPECTED_TITLES = ["Five Hundred Years", "Get in Line", "Kings Get Paid", "He Kept Walking", "A Monkey in the Mountain", "Your Other Left", "Out", "Every Mile on the Ground", "The Spare Robe", "Is It Always This Slow?", "First Fight", "The Needle", "No Better Than He Is", "Tea with a Dragon", "The Shoe", "Gold, Hold Fast", "Don't Make a Speech", "Another Present", "Promise Me", "The Band", "It Was a Trap", "Yes", "I'm Sorry", "Gulp", "It Ate Your Horse", "Your Mother Was a Tadpole", "Oh No", "Saddle and All", "The White Horse", "Gao's Farm", "The Bride", "Darling, I'm Home", "Not Anymore", "Hello, Dumpling", "The Pilgrim?", "I Gave You a Robe", "Eight Rules", "Big Brother", "No Feather Floats", "Not One Mile", "Clang", "Soup", "Pilgrim!", "The Tenth One", "At My Back", "The Raft", "Slower Than a Shoe", "Then He Waited"]
EXPECTED_MOVEMENTS = [('I · Five Hundred Years', 1, 4), ('II · The Seal', 5, 10), ('III · The Robbers and the Shoe', 11, 17), ('IV · The Band', 18, 23), ('V · The Dragon in the Stream', 24, 29), ('VI · The Bride of Gao Village', 30, 37), ('VII · The River of Flowing Sand', 38, 48)]

def main() -> int:
    problems: list[str] = []
    if len(EXPECTED_TITLES) != N: problems.append(f"manifest has {len(EXPECTED_TITLES)} titles, expected {N}")
    covered = [p for _, a, b in EXPECTED_MOVEMENTS for p in range(a, b + 1)]
    if covered != list(range(1, N + 1)): problems.append("manifest movements do not cover pages 1-N exactly once")
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
    for term in ["Volume II","monte_inspired:monkey-king-vol2:page","monte_inspired:monkey-king-vol2:bookmarks","End of Volume II","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-49") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-50") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Beowulf","beowulf","Hrothgar","Grendel","Wiglaf","Heorot","Unferth","Wealhtheow","Hrunting","King Arthur","king-arthur","Merlin","Excalibur","Camelot","Three Kingdoms","three-kingdoms","Liu Bei","Musketeers","three-musketeers","d'Artagnan","nano:","monte-cristo-vol3","monte-cristo","Villefort","Valentine","Monte Cristo","stories.js","page-49.png","#page-57","#page-58","Chronicle"]:
        if term in reader: problems.append(f"stale or foreign term present: {term}")
    ids = re.findall(r'\bid="([^"]+)"', reader)
    dup = sorted({v for v in ids if ids.count(v) > 1})
    if dup: problems.append("duplicate element IDs: " + ", ".join(dup))
    refs = set(re.findall(r'getElementById\(["\']([^"\']+)["\']\)', reader))
    miss = sorted(refs - set(ids))
    if miss: problems.append("script references missing IDs: " + ", ".join(miss))
    q = len(re.findall(r'class="question"', reader)); a = len(re.findall(r'data-answer="[abc]"', reader))
    if q != 5 or a != 5: problems.append(f"quiz must have five questions and answers; found {q}/{a}")
    if reader.count('href="../index.html"') < 2: problems.append("publication copy must link back to the library from the toolbar and the ending")
    for p in problems: print("PROBLEM:", p)
    print("CLEAN" if not problems else f"NOT CLEAN — {len(problems)} problem(s)")
    return 0 if not problems else 1

if __name__ == "__main__":
    sys.exit(main())
