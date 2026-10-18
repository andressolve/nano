#!/usr/bin/env python3
"""Mechanical verification for the finished Three Musketeers Volume II reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
N = 58
EXPECTED_TITLES = ["Only Three Blue Cloaks", "The Boy from Gascony", "Something Nobody Can Forget", "Boys Tell Me Everything", "Noon on the River Road", "By the Front Door", "Ladies Who Are Kind", "Two of Those", "How Very Clever of Her", "The Empty Chair", "I Don't Know That Name", "She Was Not Alone", "The Lily", "Nobody Said Anything About Windows", "Which Shoulder?", "A Friend of Mine", "It Was You", "The March to La Rochelle", "A Bottle from Your Friends", "That Was Good Grass", "The Red Dovecote", "The Broken Stovepipe", "Then I Shall Do a Great Deal", "Do You Know Me?", "On the Road to the Sea", "Hate Me on the Road", "Are You Hungry?", "Who'll Bet Against Us?", "Breakfast Under the Guns", "The Cardinal's Paper", "I Haven't Finished My Chicken", "All for One, and Push!", "Everybody Was Running", "One Minute More", "In My Red or in the Ground", "Half a Day", "The Kind Widow", "You Were Right to Warn Him", "One Way or Another", "Nobody Else Would Ride That Colour", "To d'Artagnan", "The Back Gate", "You Promised, and You Came", "The Roses", "You Didn't Pour the Wine Either", "The Storm", "Not Like This", "Judge Me from the Bank", "Nobody Let Go", "Never", "The Lantern Goes Out", "Good", "The Sixth Time", "I Did Not Pour the Wine", "Men Who Can't Be Bought", "There. D'Artagnan.", "The Lamp at the Door", "Four Blue Cloaks"]
EXPECTED_MOVEMENTS = [('I · The Lady in the Carriage', 1, 9), ('II · The Lily', 10, 18), ('III · The Red Dovecote', 19, 25), ('IV · The Bastion', 26, 36), ('V · Béthune', 37, 45), ('VI · The River', 46, 52), ('VII · The Paper', 53, 58)]

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
            if json.loads("[" + m.group(1) + "]") != EXPECTED_TITLES: problems.append("title array does not match the 58-title manifest")
        except json.JSONDecodeError as e: problems.append(f"title array not JSON-compatible: {e}")
    m = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not m: problems.append("reader must expose const movements = [...]")
    else:
        mv = [(t, int(a), int(b)) for t, a, b in re.findall(r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}', m.group(1))]
        if mv != EXPECTED_MOVEMENTS: problems.append("movement array must cover the seven approved ranges exactly")
    for term in ["Volume II","monte_inspired:three-musketeers-vol2:page","monte_inspired:three-musketeers-vol2:bookmarks","End of Volume II","Test your understanding","localStorage","requestFullscreen","touchstart","hashchange"]:
        if term not in reader: problems.append(f"missing required term/feature: {term}")
    for term in ['const END_HASH = "#end";','const QUIZ_HASH = "#quiz";','if (hash === END_HASH || hash === "#page-59") return titles.length;','if (hash === QUIZ_HASH || hash === "#page-60") return titles.length + 1;','return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;','const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;','localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));']:
        if term not in reader: problems.append(f"boundary routing missing: {term}")
    for term in ['let renderRequest = 0;','let displayedPage = null;','const pendingPageLoads = new Map();','await image.decode();','aria-busy']:
        if term not in reader: problems.append(f"race-safe loading missing: {term}")
    for term in ["Beowulf", "Hrothgar", "Grendel", "King Arthur", "Merlin", "Excalibur", "Three Kingdoms", "Liu Bei", "Monkey King", "monkey-king", "Wukong", "Bajie", "Sanzang", "Monte Cristo", "monte-cristo", "Villefort", "nano:", "stories.js",  "page-59.png", "three-musketeers-vol1:", "Queen's Diamonds\"", "Chronicle", "Buckingham"]:
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
    # quiz answer balance (owner rule 2026-10-17)
    qs = re.findall(r'<li class="question" data-answer="([abc])">(.*?)</li>', reader, re.S)
    longest_correct = 0; letters = []
    for ans, block in qs:
        opts = re.findall(r'value="([abc])"[^>]*>\s*(?:<[^>]+>\s*)*([^<]+)', block)
        if len(opts) >= 3:
            lens = {k: len(v.strip()) for k, v in opts[:3]}
            if lens.get(ans, 0) == max(lens.values()): longest_correct += 1
        letters.append(ans)
    if longest_correct > 2: problems.append(f"quiz: correct option is the longest in {longest_correct} of {len(qs)} questions (max 2)")
    if letters and (len(set(letters)) < 3 or any(letters[i]==letters[i+1]==letters[i+2] for i in range(len(letters)-2))): problems.append(f"quiz: answer letters not varied: {letters}")
    for p in problems: print("PROBLEM:", p)
    print("CLEAN" if not problems else f"NOT CLEAN — {len(problems)} problem(s)")
    return 0 if not problems else 1

if __name__ == "__main__":
    sys.exit(main())
