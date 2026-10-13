#!/usr/bin/env python3
"""Mechanical verification for the finished King Arthur Vol. I reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 59
EXPECTED_TITLES = ["The Storm", "My Arthur", "Thirteen Years", "A Rider from London", "That Isn't an Answer", "London", "Who Built the Walls?", "The Sword in the Stone", "Where's My Sword?", "The Locked Inn", "Like a Stick out of Snow", "Kay Knows That Sword", "Swear on the Book", "I'm Not Your Father", "All I've Got Is a Sword", "When Nobody's Listening", "Don't Make a Song of It", "Alone with the Sword", "Did It Really Happen?", "The King of the Hens", "We Will Have Arthur", "The Crowning", "A Gift of Swords", "Uther's Son", "I'd Do It Again", "All of Us, Together", "Was There a Real Arthur?", "The Night Before", "Bedegraine", "Alone, Too Far", "You're Very Bad at This", "Thirty Torches", "It Doesn't Look Like Winning", "What It Cost", "The Songs", "Shining Armour", "Kings Send Knights", "Alone at Midnight", "The Knight at the Fountain", "The Sword Breaks", "Kings Don't Yield", "Me", "Nearly Died for a Song", "The Arm in the Lake", "Whatever You Ask", "Excalibur", "Sword or Scabbard", "That's Cheating", "Every Day", "Two Magic Swords?", "A Knife over a Chair", "That's a Cartwheel", "Nine Oak Trees", "Names in Gold", "Level with Nobody", "I'll Swear First", "The Empty Chair", "Goodnight, Father", "Who Made It Up?"]
EXPECTED_MOVEMENTS = [('I · The Hidden King', 1, 7), ('II · The Sword in the Stone', 8, 19), ('III · The Kings Who Laughed', 20, 27), ('IV · The First Battle', 28, 36), ('V · The Knight at the Fountain', 37, 43), ('VI · The Lady of the Lake', 44, 50), ('VII · The Round Table', 51, 59)]

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
            if json.loads("[" + m.group(1) + "]") != EXPECTED_TITLES: problems.append("title array does not match the 59-title manifest")
        except json.JSONDecodeError as e: problems.append(f"title array not JSON-compatible: {e}")
    m = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const movements = [...]")
    else:
        mv = [(t, int(a), int(b)) for t, a, b in re.findall(r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}', m.group(1))]
        if mv != EXPECTED_MOVEMENTS: problems.append("movement array must cover the seven approved ranges exactly")
    for term in ["King Arthur, Volume I: The Sword and the Table","monte_inspired:king-arthur-vol1:page","monte_inspired:king-arthur-vol1:bookmarks","End of Volume I","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-60") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-61") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Monte Cristo","monte-cristo","nano:","Morcerf","Volume II:","stories.js","page-60.png","#page-62","Three Kingdoms","three-kingdoms","Peach Garden","Liu Bei","Musketeers","three-musketeers","d'Artagnan","Queen's Diamonds"]:
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
