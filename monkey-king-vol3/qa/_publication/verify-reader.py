#!/usr/bin/env python3
"""Mechanical verification for the finished Monkey King Volume III reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 49
EXPECTED_TITLES = ["Still Walking West", "One Bite", "I Can Fly Peaches", "Rice and Noodles", "The Skull Under the Smile", "Look in Her Basket", "He Fooled Me Once", "Like a Walnut", "Same Skull", "Did You See the Mist?", "Gold, Hold Fast", "Behind", "I'm Asking You First", "You'll Be Alive to Do It", "Faster Than the Mist", "Read It!", "Not My Disciple", "Four Bows", "The Whole Way Home", "The King Comes Home", "Leave the Robe", "Looking at the Weather", "A Pagoda!", "No Monks", "May Not!", "He's, Um, Busy", "One Breath", "I Sent Him Away", "Claws and Teeth", "Paws Together", "Before He Was a Horse", "The Cage", "Listen to Me", "Only When It Matters", "The Worst Flyer in the Sky", "I Don't Know Any Pigs", "Try Again", "The True One", "On a Cloud Like Yours", "He Waited for the Pig", "The First Disciple", "Krang", "A Star That Ran Away", "Going Home", "Any Face", "Not Even a Tiger", "I Heard You", "Wrong Together", "Just a Lady with Lunch"]
EXPECTED_MOVEMENTS = [('I · The Ridge', 1, 5), ('II · Three Faces', 6, 19), ('III · Home', 20, 22), ('IV · The Yellow Robe', 23, 34), ('V · Going Back', 35, 40), ('VI · The Star in the Pagoda', 41, 49)]

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
            if json.loads("[" + m.group(1) + "]") != EXPECTED_TITLES: problems.append("title array does not match the 49-title manifest")
        except json.JSONDecodeError as e: problems.append(f"title array not JSON-compatible: {e}")
    m = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const movements = [...]")
    else:
        mv = [(t, int(a), int(b)) for t, a, b in re.findall(r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}', m.group(1))]
        if mv != EXPECTED_MOVEMENTS: problems.append("movement array must cover the six approved ranges exactly")
    for term in ["Volume III","monte_inspired:monkey-king-vol3:page","monte_inspired:monkey-king-vol3:bookmarks","End of Volume III","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-50") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-51") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Beowulf","beowulf","Hrothgar","Grendel","Wiglaf","Heorot","Unferth","Wealhtheow","Hrunting","King Arthur","king-arthur","Merlin","Excalibur","Camelot","Three Kingdoms","three-kingdoms","Liu Bei","Musketeers","three-musketeers","d'Artagnan","nano:","monte-cristo-vol3","monte-cristo","Villefort","Valentine","Monte Cristo","stories.js","page-50.png","monkey-king-vol2:","Five Hundred Years","Then He Waited","Chronicle"]:
        if term in reader: problems.append(f"stale or foreign term present: {term}")
    if reader.count('href="../index.html"') < 2: problems.append("publication copy must link back to the library from the toolbar and the ending")
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
