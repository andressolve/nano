#!/usr/bin/env python3
"""Validate the Page 32 intent-pilot critic report contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ALLOWED_CRITERIA = {f"C{i}" for i in range(1, 7)}
FORBIDDEN_GROUNDS = (
    "seal",
    "document",
    "prompt",
    "panel percentage",
    "panel share",
    "coordinate",
    "pixel",
)


def validate(text: str) -> tuple[str | None, list[str]]:
    errors: list[str] = []
    verdict_match = re.search(r"(?m)^VERDICT: (APPROVED|REVISE)\s*$", text)
    verdict = verdict_match.group(1) if verdict_match else None
    if verdict is None:
        errors.append("missing exact VERDICT line")

    for heading in ("## Blind cold read", "## Visible text", "## Findings"):
        if heading not in text:
            errors.append(f"missing section: {heading}")

    findings_match = re.search(r"(?ms)^## Findings\s*\n(.*)\Z", text)
    findings = findings_match.group(1).strip() if findings_match else ""
    finding_hits = list(
        re.finditer(
            r"(?ms)^### Finding (C\d+)\s*\n"
            r"- Observation:\s*(.+?)\s*\n"
            r"- Reader harm:\s*(.+?)(?=\n### Finding C\d+|\Z)",
            findings,
        )
    )

    cited = [hit.group(1) for hit in finding_hits]
    unknown = sorted(set(cited) - ALLOWED_CRITERIA)
    if unknown:
        errors.append(f"unknown criterion: {', '.join(unknown)}")
    if len(cited) != len(set(cited)):
        errors.append("a criterion is cited more than once")

    if verdict == "APPROVED" and findings != "NONE":
        errors.append("APPROVED requires Findings to be exactly NONE")
    if verdict == "REVISE" and not finding_hits:
        errors.append("REVISE requires at least one complete C1-C6 finding")

    if finding_hits:
        consumed = "\n".join(hit.group(0).strip() for hit in finding_hits)
        normalized_findings = re.sub(r"\s+", " ", findings).strip()
        normalized_consumed = re.sub(r"\s+", " ", consumed).strip()
        if normalized_findings != normalized_consumed:
            errors.append("Findings contains text outside the required finding blocks")

    for hit in finding_hits:
        observation = hit.group(2).strip()
        reader_harm = hit.group(3).strip()
        if len(observation) < 12:
            errors.append(f"{hit.group(1)} observation is not concrete")
        if len(reader_harm) < 12:
            errors.append(f"{hit.group(1)} reader harm is not explained")

    lower_findings = findings.lower()
    for phrase in FORBIDDEN_GROUNDS:
        if phrase in lower_findings:
            errors.append(f"out-of-card ground appears in Findings: {phrase}")

    return verdict, errors


def self_test() -> int:
    approved = """VERDICT: APPROVED

## Blind cold read
The chamber turns and Haydée owns the occupied hall.

## Visible text
NONE

## Findings
NONE
"""
    revise = """VERDICT: REVISE

## Blind cold read
The lower image reads as an empty private room.

## Visible text
NONE

## Findings

### Finding C2
- Observation: The lower chamber contains no visible audience.
- Reader harm: Haydée appears to enter an empty room, breaking the public reveal.
"""
    invalid = revise.replace(
        "The lower chamber contains no visible audience.",
        "The seal is not sufficiently legible.",
    )
    cases = ((approved, True), (revise, True), (invalid, False))
    failures = 0
    for index, (sample, expected_valid) in enumerate(cases, start=1):
        _, errors = validate(sample)
        if (not errors) != expected_valid:
            print(f"self-test {index} failed: {errors}", file=sys.stderr)
            failures += 1
    if failures:
        return 1
    print("SELF-TEST CLEAN")
    return 0


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) != 2:
        print(
            "usage: validate-critic-report.py REPORT.md | --self-test",
            file=sys.stderr,
        )
        return 2

    report_path = Path(sys.argv[1])
    if not report_path.is_file():
        print(f"INVALID: report not found: {report_path}", file=sys.stderr)
        return 1

    verdict, errors = validate(report_path.read_text())
    if errors:
        for error in errors:
            print(f"INVALID: {error}", file=sys.stderr)
        return 1

    print(f"VALID {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
