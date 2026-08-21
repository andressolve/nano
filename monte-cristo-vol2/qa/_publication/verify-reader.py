#!/usr/bin/env python3
"""Mechanical verification for the finished Volume II reader and catalog."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[2]
REPO = PROJECT.parent

EXPECTED_TITLES = [
    "Three Roofs",
    "The Banker First",
    "Janina",
    "The Real Reason",
    "I Shall Enjoy It",
    "The Invitation",
    "Albert de Morcerf",
    "Greece",
    "Two Handshakes",
    "My Father",
    "Fruit from Her Garden",
    "She Knows",
    "Since 1815",
    "The First Lie",
    "Appetite Intact",
    "Warn Nobody",
    "The Pleasure",
    "The Receipt",
    "Janina, 1822",
    "The Price",
    "The Market",
    "Her Right to Speak",
    "The Room",
    "Danglars Decides",
    "The Reply from Janina",
    "In Print",
    "The Truth, Not a Retraction",
    "She Has Known",
    "Beauchamp Returns",
    "The Public Stair",
    "The Chamber of Peers",
    "The Door Opens",
    "Haydée Testifies",
    "Still Wearing the Decorations",
    "At the End of It",
    "The Challenge",
    "After Victory",
    "Edmond",
    "Stand Still",
    "The Night Before",
    "Four Hours Before Dawn",
    "Albert Withdraws",
    "His Mother's Name",
    "It Changes Nothing",
    "The Empty Glass",
    "I Am Edmond Dantès",
    "The Shot",
    "They Take Nothing",
    "One",
]

EXPECTED_MOVEMENTS = [
    ("I · The Invitation", 1, 7),
    ("II · The House of Morcerf", 8, 17),
    ("III · What Happened at Janina", 18, 25),
    ("IV · The Fall", 26, 34),
    ("V · The Son", 35, 44),
    ("VI · The Cost", 45, 49),
]


def main() -> int:
    problems: list[str] = []

    page_files = sorted((PROJECT / "pages").glob("page-*.png"))
    expected_files = [PROJECT / "pages" / f"page-{n:02d}.png" for n in range(1, 50)]
    if page_files != expected_files:
        problems.append("canonical page set must be exactly page-01.png through page-49.png")

    try:
        from PIL import Image

        for path in expected_files:
            if not path.exists():
                continue
            with Image.open(path) as image:
                if image.size != (1024, 1536):
                    problems.append(f"{path.name}: expected 1024x1536, got {image.size}")
                if image.mode != "RGB":
                    problems.append(f"{path.name}: expected RGB, got {image.mode}")
    except ImportError:
        problems.append("Pillow is unavailable; page dimensions and modes were not verified")

    reader_path = PROJECT / "index.html"
    if not reader_path.exists():
        problems.append("index.html is missing")
        reader = ""
    else:
        reader = reader_path.read_text(encoding="utf-8")

    title_match = re.search(r"const\s+titles\s*=\s*\[(.*?)\];", reader, re.S)
    if not title_match:
        problems.append("reader must expose const titles = [...] for 49 pages")
    else:
        try:
            titles = json.loads("[" + title_match.group(1) + "]")
            if titles != EXPECTED_TITLES:
                problems.append("reader title array does not match the approved 49-title manifest")
        except json.JSONDecodeError as error:
            problems.append(f"reader title array is not JSON-compatible: {error}")

    movement_match = re.search(r"const\s+movements\s*=\s*\[(.*?)\];", reader, re.S)
    if not movement_match:
        problems.append("reader must expose const movements = [...] for six movements")
    else:
        movements = [
            (title, int(start), int(end))
            for title, start, end in re.findall(
                r'\{\s*title:\s*"([^"]+)",\s*start:\s*(\d+),\s*end:\s*(\d+)\s*\}',
                movement_match.group(1),
            )
        ]
        if movements != EXPECTED_MOVEMENTS:
            problems.append("reader movement array must cover the approved six ranges exactly")

    required_reader_terms = [
        "The Count of Monte Cristo — Volume II: The House of Morcerf",
        "nano:monte-cristo-vol2:page",
        "nano:monte-cristo-vol2:bookmarks",
        "../monte-cristo-expanded/index.html",
        "../index.html",
        "End of Volume II",
        "Test your understanding",
        "localStorage",
        "requestFullscreen",
        "touchstart",
        "hashchange",
    ]
    for term in required_reader_terms:
        if term not in reader:
            problems.append(f"reader is missing required term/feature: {term}")

    boundary_checks = [
        'const END_HASH = "#end";',
        'const QUIZ_HASH = "#quiz";',
        'if (hash === END_HASH || hash === "#page-50") return titles.length;',
        'if (hash === QUIZ_HASH || hash === "#page-51") return titles.length + 1;',
        'return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;',
        'const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;',
        'localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));',
    ]
    for term in boundary_checks:
        if term not in reader:
            problems.append(f"reader boundary routing is missing: {term}")

    stale_reader_terms = [
        "Page 1 of 55",
        "55 pages",
        "nano:monte-cristo-expanded:page",
        "nano:monte-cristo-expanded:bookmarks",
    ]
    for term in stale_reader_terms:
        if term in reader:
            problems.append(f"reader contains stale Volume I term: {term}")

    ids = re.findall(r'\bid="([^"]+)"', reader)
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    if duplicate_ids:
        problems.append("duplicate element IDs: " + ", ".join(duplicate_ids))
    references = set(re.findall(r'getElementById\(["\']([^"\']+)["\']\)', reader))
    missing_references = sorted(references - set(ids))
    if missing_references:
        problems.append("missing DOM IDs referenced by script: " + ", ".join(missing_references))

    question_count = len(re.findall(r'class="question"', reader))
    answer_count = len(re.findall(r'data-answer="[abc]"', reader))
    if question_count != 5 or answer_count != 5:
        problems.append(f"quiz must contain five questions and answers; found {question_count}/{answer_count}")

    stories_path = REPO / "stories.js"
    stories = stories_path.read_text(encoding="utf-8") if stories_path.exists() else ""
    entry_match = re.search(
        r'\{\s*slug:\s*"monte-cristo-vol2"(?P<body>.*?)\n\s*\},', stories, re.S
    )
    if not entry_match:
        problems.append("stories.js is missing the monte-cristo-vol2 entry")
    else:
        entry = entry_match.group(0)
        for term in [
            'title: "The Count of Monte Cristo — Volume II: The House of Morcerf"',
            'cover: "monte-cristo-vol2/pages/page-01.png"',
            'published: "2026-08-21"',
            'category: "Myth & Literature"',
            'series: "The Count of Monte Cristo · Volume II"',
        ]:
            if term not in entry:
                problems.append(f"catalog entry is missing: {term}")
        if re.search(r'status:\s*"(?:hidden|draft|superseded)"', entry):
            problems.append("catalog entry must be public")

    ignore_path = REPO / ".gitignore"
    ignore_text = ignore_path.read_text(encoding="utf-8") if ignore_path.exists() else ""
    if "monte-cristo-vol2/qa/**/*.png" not in ignore_text:
        problems.append(".gitignore does not protect Volume II raw QA PNGs")

    adjudication = PROJECT / "qa" / "continuity" / "continuity-pass-01-49-adjudication.md"
    if not adjudication.exists() or "CLEARED — APPROVED" not in adjudication.read_text(encoding="utf-8"):
        problems.append("final continuity adjudication is not cleared")
    handoff = (PROJECT / "HANDOFF.md").read_text(encoding="utf-8")
    if "all final gates are cleared" not in handoff:
        problems.append("HANDOFF.md does not record cleared final gates")

    if problems:
        for problem in problems:
            print(f"PROBLEM: {problem}")
        return 1

    print("CLEAN")
    print("49 canonical RGB pages · 49 titles · 6 movements · 5 quiz questions · catalog entry present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
