#!/usr/bin/env python3
"""Mechanical verification for the finished Three Kingdoms Vol. I reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 50
EXPECTED_TITLES = ['The Yellow Sky', 'The Notice on the Wall', 'Why Not Do Something?', 'Wine, and Quickly', 'Real Brothers', 'The Oath', 'Third Brother', 'A Weapon for Each Brother', 'A Hundred Each', 'The Ambush', 'The Grass Begins to Glow', 'Somebody Stole Our Battle', "You're Late", "The Emperor's Banner", 'A Bag of Rice', 'The Fat General', 'Up the Palace Stairs', "Do You Think Mine Isn't?", 'The Giant Behind the Old Man', 'Red Hare', 'Father', 'A Dagger in His Sleeve', 'Wake Me When the Horse Comes', 'A Gift', 'Out of the Gate', "Your Father's Son", 'Tie the Legs Tight', 'The Old Man Never Came Home', 'A Letter to Every Lord', 'We Go', 'Hulao Gate', 'The End of the Bench', 'I Will Bring His Helmet', 'Before It Is Cold', 'The Drums', 'Still Warm', 'With Me, Not with Yuan Shao', 'Give Me the Gate', 'Among Men, Lü Bu', 'Is There No One?', 'Slave of Three Fathers', 'Fifty Times', 'Third Brother, I Am Here', 'Not on a Hill', 'Three Against One', 'The Gate Slams', 'We Are Brothers', 'Two Heroes', 'What He Wanted', 'He Did Not Turn Around']
EXPECTED_MOVEMENTS = [('I · The Peach Garden', 1, 9), ('II · Five Hundred', 10, 16), ('III · The Red Horse', 17, 22), ('IV · The Dagger', 23, 30), ('V · Eighteen Lords', 31, 38), ('VI · Lü Bu', 39, 46), ('VII · The Gate', 47, 50)]

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
            if json.loads("[" + m.group(1) + "]") != EXPECTED_TITLES: problems.append("title array does not match the 50-title manifest")
        except json.JSONDecodeError as e: problems.append(f"title array not JSON-compatible: {e}")
    m = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const movements = [...]")
    else:
        mv = [(t, int(a), int(b)) for t, a, b in re.findall(r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}', m.group(1))]
        if mv != EXPECTED_MOVEMENTS: problems.append("movement array must cover the seven approved ranges exactly")
    for term in ["Three Kingdoms, Volume I: The Peach Garden Oath","monte_inspired:three-kingdoms-vol1:page","monte_inspired:three-kingdoms-vol1:bookmarks","End of Volume I","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-51") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-52") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Monte Cristo","monte-cristo","nano:","Morcerf","Volume II:","stories.js","page-51.png","#page-53","Musketeers","three-musketeers","d'Artagnan","Queen's Diamonds"]:
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
