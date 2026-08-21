#!/usr/bin/env python3
"""Page 22 splits in two. Every page reference from 23 up shifts by one.

Only numbers in 23..48 are touched, and only where they are unambiguously page
references, so years (1838, 1822), ages, percentages and word counts are safe.
"""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parents[2]
LOW, HIGH = 23, 48


def bump(n):
    n = int(n)
    return str(n + 1) if LOW <= n <= HIGH else str(n)


PATTERNS = [
    # script + plan page headings
    (r"(## PAGE )(\d+)( ·)", 2),
    (r"(## PAGE )(\d+)( —)", 2),
    # prose references: "page 25", "Page 25", "pages 41–43", "Pages 30-33"
    (r"(\b[Pp]ages? )(\d+)", 2),
    (r"([Pp]ages? \d+\s*[–-]\s*)(\d+)", 2),
    # compact references: P25, P31–32, P23–25
    (r"(\bP)(\d+)\b", 2),
    (r"(\bP\d+\s*[–-]\s*)(\d+)\b", 2),
    # paths and filenames: page-25, page-25.png, page-25/
    (r"(page-)(\d+)", 2),
]

# only the page contract has table rows whose first cell is a page number
TABLE_PATTERN = (r"(^\| )(\d+)( \|)", 2)

# "pages 37, 38, 40 and 42", "pages 8 and 10–12" — every number in the run is a
# page reference, so the whole tail is bumped at once.
LIST_PATTERN = r"\b([Pp]ages?|pp\.?) (\d+(?:\s*(?:,|and|&|–|-|—)\s*\d+)+)"


def shift(text, tables=False):
    # lists are bumped first and parked behind a token, so the single-reference
    # patterns below cannot bump their leading number a second time
    parked = []

    def list_rep(m):
        tail = re.sub(r"\d+", lambda d: bump(d.group()), m.group(2))
        parked.append(f"{m.group(1)} {tail}")
        return f"\x00{len(parked) - 1}\x00"
    text = re.sub(LIST_PATTERN, list_rep, text)

    for pat, grp in PATTERNS + ([TABLE_PATTERN] if tables else []):
        def rep(m, grp=grp):
            parts = list(m.groups())
            parts[grp - 1] = bump(parts[grp - 1])
            return "".join(parts)
        text = re.sub(pat, rep, text, flags=re.M)

    return re.sub(r"\x00(\d+)\x00", lambda m: parked[int(m.group(1))], text)


def repad(text):
    """page-07 style zero padding survives the shift."""
    return re.sub(r"page-(\d+)", lambda m: f"page-{int(m.group(1)):02d}", text)


if __name__ == "__main__":
    for rel in sys.argv[1:]:
        tables = rel.endswith("07-PAGE-CONTRACT.md")
        p = root / rel
        s = p.read_text()
        out = repad(shift(s, tables=tables))
        p.write_text(out)
        print(f"{rel}: renumbered")
