#!/usr/bin/env python3
"""Validate an intent-first page-critic report without judging the artwork."""

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def fail(message: str) -> None:
    print(f"INVALID CRITIC REPORT: {message}")
    raise SystemExit(1)


if len(sys.argv) != 3:
    fail("usage: validate-report.py PAGE REPORT")

try:
    page = int(sys.argv[1])
except ValueError:
    fail("PAGE must be an integer")

if not 33 <= page <= 49:
    fail("PAGE must be between 33 and 49")

report_path = Path(sys.argv[2])
if not report_path.is_absolute():
    report_path = ROOT / report_path
if not report_path.is_file():
    fail(f"missing report: {report_path}")

card_path = ROOT / "qa" / "_run" / f"page-{page:02d}-critic-card.md"
if not card_path.is_file():
    fail(f"missing critic card: {card_path}")

text = report_path.read_text().strip()
if len(text) > 5_000:
    fail("report exceeds the concise 5,000-character ceiling")

allowed = set(re.findall(r"^### (C\d+) — ", card_path.read_text(), flags=re.M))
if not allowed:
    fail("critic card contains no numbered criteria")

first = text.splitlines()[0] if text else ""
if first not in {"VERDICT: APPROVED", "VERDICT: REVISE"}:
    fail("first line must be exactly VERDICT: APPROVED or VERDICT: REVISE")

for heading in ("## Blind read", "## Visible text", "## Findings"):
    if len(re.findall(rf"^{re.escape(heading)}$", text, flags=re.M)) != 1:
        fail(f"report must contain exactly one {heading}")

parts = re.split(r"^## (Blind read|Visible text|Findings)$", text, flags=re.M)
sections = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
for name in ("Blind read", "Visible text", "Findings"):
    if not sections.get(name):
        fail(f"{name} section is empty")

finding_ids = re.findall(r"^### Finding (C\d+)$", sections["Findings"], flags=re.M)

if first == "VERDICT: APPROVED":
    if sections["Findings"] != "NONE":
        fail("APPROVED requires Findings to be exactly NONE")
    if finding_ids:
        fail("APPROVED cannot contain finding blocks")
    print("VALID APPROVED CODES=-")
    raise SystemExit(0)

if not finding_ids:
    fail("REVISE requires at least one numbered finding")
if len(finding_ids) != len(set(finding_ids)):
    fail("REVISE repeats a criterion number")
unknown = sorted(set(finding_ids) - allowed)
if unknown:
    fail(f"out-of-card criteria: {', '.join(unknown)}")

blocks = re.split(r"^### Finding C\d+$", sections["Findings"], flags=re.M)[1:]
if len(blocks) != len(finding_ids):
    fail("finding block parse mismatch")

required_fields = ("Observation", "Material reader harm", "Redraw justification")
for finding_id, block in zip(finding_ids, blocks):
    for field in required_fields:
        matches = re.findall(rf"^- {re.escape(field)}:\s*(.+)$", block, flags=re.M)
        if len(matches) != 1:
            fail(f"Finding {finding_id} needs exactly one {field} field")
        value = matches[0].strip()
        if not value or value.upper() == "NONE" or "[" in value or "]" in value:
            fail(f"Finding {finding_id} has an empty or placeholder {field}")

print(f"VALID REVISE CODES={','.join(finding_ids)}")

