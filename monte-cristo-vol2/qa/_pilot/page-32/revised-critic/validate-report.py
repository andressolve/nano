#!/usr/bin/env python3
"""Validate the revised Page 32 critic report contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ALLOWED = {f"C{i}" for i in range(1, 7)}


def validate(text: str) -> tuple[str | None, list[str]]:
    errors: list[str] = []
    verdict_match = re.search(r"(?m)^VERDICT: (APPROVED|REVISE)\s*$", text)
    verdict = verdict_match.group(1) if verdict_match else None
    if verdict is None:
        errors.append("missing exact verdict")
    for heading in ("## Blind cold read", "## Visible text", "## Findings"):
        if heading not in text:
            errors.append(f"missing {heading}")

    findings_match = re.search(r"(?ms)^## Findings\s*\n(.*)\Z", text)
    findings = findings_match.group(1).strip() if findings_match else ""
    hits = list(
        re.finditer(
            r"(?ms)^### Finding (C\d+)\s*\n"
            r"- Observation:\s*(.+?)\s*\n"
            r"- Material reader harm:\s*(.+?)\s*\n"
            r"- Redraw justification:\s*(.+?)(?=\n### Finding C\d+|\Z)",
            findings,
        )
    )
    codes = [hit.group(1) for hit in hits]
    unknown = sorted(set(codes) - ALLOWED)
    if unknown:
        errors.append(f"unknown criterion: {', '.join(unknown)}")
    if len(codes) != len(set(codes)):
        errors.append("duplicate criterion")

    if verdict == "APPROVED" and findings != "NONE":
        errors.append("APPROVED requires Findings NONE")
    if verdict == "REVISE" and not hits:
        errors.append("REVISE requires a complete C1-C6 finding")

    if hits:
        consumed = "\n".join(hit.group(0).strip() for hit in hits)
        if re.sub(r"\s+", " ", findings).strip() != re.sub(
            r"\s+", " ", consumed
        ).strip():
            errors.append("extra text in Findings")
        for hit in hits:
            for label, value in zip(
                ("observation", "material harm", "redraw justification"),
                hit.groups()[1:],
            ):
                if len(value.strip()) < 16:
                    errors.append(f"{hit.group(1)} {label} is not concrete")
    return verdict, errors


def self_test() -> int:
    approved = """VERDICT: APPROVED

## Blind cold read
The Chamber turns and Haydée owns the occupied room.

## Visible text
NONE

## Findings
NONE
"""
    revise = """VERDICT: REVISE

## Blind cold read
Haydée appears in an empty private room.

## Visible text
NONE

## Findings

### Finding C2
- Observation: The lower hall contains no visible assembly.
- Material reader harm: The public reveal becomes a private entrance and the page event changes.
- Redraw justification: Restoring the missing audience is essential to the story and outweighs the risk of replacing the page.
"""
    incomplete = revise.replace(
        "- Redraw justification: Restoring the missing audience is essential to the story and outweighs the risk of replacing the page.\n",
        "",
    )
    cases = ((approved, True), (revise, True), (incomplete, False))
    for index, (sample, expected) in enumerate(cases, 1):
        _, errors = validate(sample)
        if (not errors) != expected:
            print(f"self-test {index} failed: {errors}", file=sys.stderr)
            return 1
    print("SELF-TEST CLEAN")
    return 0


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) != 2:
        print("usage: validate-report.py REPORT.md | --self-test", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"INVALID: report not found: {path}", file=sys.stderr)
        return 1
    verdict, errors = validate(path.read_text())
    if errors:
        for error in errors:
            print(f"INVALID: {error}", file=sys.stderr)
        return 1
    print(f"VALID {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
