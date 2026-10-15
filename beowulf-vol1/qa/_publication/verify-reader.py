#!/usr/bin/env python3
"""Mechanical verification for the finished Beowulf reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 57
EXPECTED_TITLES = ["Something in the Fen", "Heorot", "Out of the Fen", "Thirty Men", "Twelve Winters", "Who's Coming with Me?", "Who Were the Danes and the Geats?", "White Cliffs", "The Stone Road", "I'll Fight Him with These", "Seven Nights in the Water", "Nine Sea-Monsters", "What a Geat Can Do", "What Was a Hall Like?", "The Queen's Cup", "Nothing in His Hands", "Out of the Moor", "Looking for Me?", "He Left His Arm Behind", "The Claw over the Doors", "Like a Son", "A Song about Beowulf", "Who Was the King's Poet?", "Grendel Had a Mother", "She Came Anyway", "The Black Lake", "Hrunting", "She Was Waiting", "The Sword Would Not Bite", "A Sword Made by Giants", "Like Ice in Spring", "Did You Think I Wasn't Coming Back?", "A Good Sword", "They Come for Everyone", "Home", "Why Did a Sword Have a Name?", "The Old King", "One Golden Cup", "It Came Out Burning", "No Army", "Every Time", "Why Does a Dragon Sleep on Gold?", "Sickness, or the Sword", "This Isn't Your Fight", "Come Out, Dragon!", "The Fire Came Again", "We Promised Him!", "I Came Anyway", "Under the Fire", "Today I Did", "A Banner of Gold", "The Sea Wind in His Hair", "You've Lost Your Names", "Who Will Keep Us Safe Now?", "The Gentlest of Kings", "Beowulf's Barrow", "How Do We Still Know This Story?"]
CHRONICLE_PAGES = [7, 14, 23, 36, 42, 57]
EXPECTED_MOVEMENTS = [('I · The Hall That Sang', 1, 7), ('II · The Stranger Who Boasted', 8, 14), ('III · Grendel', 15, 23), ('IV · The Mother in the Mere', 24, 32), ("V · The Old King's Warning", 33, 36), ('VI · Fifty Winters', 37, 42), ('VII · The Dragon', 43, 57)]

def main() -> int:
    problems: list[str] = []
    if len(EXPECTED_TITLES) != N: problems.append(f"manifest has {len(EXPECTED_TITLES)} titles, expected {N}")
    covered = [p for _, a, b in EXPECTED_MOVEMENTS for p in range(a, b + 1)]
    if covered != list(range(1, N + 1)): problems.append("manifest movements do not cover pages 1-N exactly once")
    if any(not 1 <= p <= N for p in CHRONICLE_PAGES) or len(CHRONICLE_PAGES) != 6: problems.append("chronicle page list must be six pages within 1-N")
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
            if json.loads("[" + m.group(1) + "]") != EXPECTED_TITLES: problems.append("title array does not match the 57-title manifest")
        except json.JSONDecodeError as e: problems.append(f"title array not JSON-compatible: {e}")
    m = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const movements = [...]")
    else:
        mv = [(t, int(a), int(b)) for t, a, b in re.findall(r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}', m.group(1))]
        if mv != EXPECTED_MOVEMENTS: problems.append("movement array must cover the seven approved ranges exactly")
    for term in ["Beowulf: The Hall, the Mere, and the Dragon","monte_inspired:beowulf-vol1:page","monte_inspired:beowulf-vol1:bookmarks","The End","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-58") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-59") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Monte Cristo","monte-cristo","nano:","Morcerf","Volume II:","stories.js","page-58.png","#page-60","Volume I","End of Volume","Three Kingdoms","three-kingdoms","Peach Garden","Liu Bei","Musketeers","three-musketeers","d'Artagnan","Queen's Diamonds","King Arthur","king-arthur","Arthur","Merlin","Excalibur","Bedegraine","Round Table","Lady of the Lake","Camelot"]:
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
