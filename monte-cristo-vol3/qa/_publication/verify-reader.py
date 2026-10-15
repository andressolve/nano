#!/usr/bin/env python3
"""Mechanical verification for the finished Monte Cristo Volume III reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 56
EXPECTED_TITLES = ["The Second Man", "What Was in the Box", "I Was the Priest", "That Chair's Taken", "Prince Andrea Cavalcanti", "The King's Attorney", "Down the Hill", "One Drop", "Villefort's Problem", "The House in the Faubourg", "Grandfather's Eyes", "I Was the Sailor", "Do You Want Me to Stop?", "The Red Purse", "If I Ever Find Him", "Valentine de Villefort", "Every Floor of It", "Three Invitations", "The Iron Gate", "To Fathers", "A Story about This House", "Two in the Morning", "A Cup of Warm Milk", "Don't Tell Me", "Such a Comfort", "Did You See the Milk?", "The Steps of the Opéra", "Bitter, Like Your Medicine", "Help Her", "It Was My Bottle", "Inside the Wall", "Red Drops", "Every Night Until You Are Dead", "So You Will Die", "The House Believed It", "One Name, Letter by Letter", "You Promised Me", "The Tomb at Night", "She Did Not Wake", "A Good Story Needs a Date", "Use It", "All Paris Came", "A Very Big Tree", "My Father Is You", "You Didn't Look", "It Is True", "Faster", "I Did What You Told Me", "The Closed Door", "I Am Edmond Dantès", "Nothing Left in It", "Every Garden in Paris", "He Could Not Say It", "Keep This One Too", "One Month", "She's Holding On"]
EXPECTED_MOVEMENTS = [('I · What Was Buried', 1, 8), ("II · The King's Attorney's House", 9, 18), ('III · Dinner at Auteuil', 19, 27), ('IV · Valentine', 28, 39), ('V · The Trial', 40, 47), ('VI · The Bill', 48, 56)]

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
            if json.loads("[" + m.group(1) + "]") != EXPECTED_TITLES: problems.append("title array does not match the 56-title manifest")
        except json.JSONDecodeError as e: problems.append(f"title array not JSON-compatible: {e}")
    m = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const movements = [...]")
    else:
        mv = [(t, int(a), int(b)) for t, a, b in re.findall(r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}', m.group(1))]
        if mv != EXPECTED_MOVEMENTS: problems.append("movement array must cover the six approved ranges exactly")
    for term in ["Volume III","monte_inspired:monte-cristo-vol3:page","monte_inspired:monte-cristo-vol3:bookmarks","End of Volume III","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-57") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-58") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Beowulf","beowulf","Hrothgar","Grendel","Wiglaf","Heorot","Unferth","Wealhtheow","Hrunting","King Arthur","king-arthur","Merlin","Excalibur","Camelot","Three Kingdoms","three-kingdoms","Liu Bei","Musketeers","three-musketeers","d'Artagnan","nano:","monte-cristo-vol2","House of Morcerf","stories.js","page-57.png","#page-60","Chronicle"]:
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
