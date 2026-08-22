#!/usr/bin/env python3
"""Validate a neutral critic report against a supplied numbered card."""
import re, sys
from pathlib import Path

def validate(report: str, card: str) -> set[str]:
    if len(report) > 5000: raise ValueError("report exceeds 5,000 characters")
    first = report.splitlines()[0] if report.splitlines() else ""
    if first not in {"VERDICT: APPROVED", "VERDICT: REVISE"}: raise ValueError("bad verdict")
    for heading in ("## Blind read", "## Visible text", "## Findings"):
        if len(re.findall(rf"^{re.escape(heading)}$", report, re.M)) != 1: raise ValueError(f"missing {heading}")
    blind_at = report.index("## Blind read")
    visible_at = report.index("## Visible text")
    findings_at = report.index("## Findings")
    if not (blind_at < visible_at < findings_at):
        raise ValueError("report must preserve blind-read, visible-text, findings order")
    blind_text = report[blind_at + len("## Blind read") : visible_at].strip()
    visible_text = report[visible_at + len("## Visible text") : findings_at].strip()
    if not blind_text or not visible_text:
        raise ValueError("blind read and visible text must be recorded before findings")
    allowed = set(re.findall(r"^### (C\d+) — ", card, re.M))
    findings = report.split("## Findings", 1)[1].strip()
    ids = re.findall(r"^### Finding (C\d+)$", findings, re.M)
    if first == "VERDICT: APPROVED":
        if findings != "NONE" or ids: raise ValueError("approved must have NONE findings")
        return set()
    if not ids or len(ids) != len(set(ids)): raise ValueError("revise needs unique numbered findings")
    if set(ids) - allowed: raise ValueError("out-of-card criterion")
    blocks = re.split(r"^### Finding C\d+$", findings, flags=re.M)[1:]
    for ident, block in zip(ids, blocks):
        for field in ("Observation", "Material reader harm", "Redraw justification"):
            m = re.findall(rf"^- {re.escape(field)}:\s*(.+)$", block, re.M)
            value = m[0].strip() if len(m) == 1 else ""
            words = re.findall(r"[A-Za-z0-9]+", value)
            if (
                len(m) != 1
                or len(value) < 20
                or len(words) < 4
                or value.upper() in {"NONE", "N/A", "TBD", "PLACEHOLDER"}
                or "[" in value
                or "]" in value
            ):
                raise ValueError(f"Finding {ident} missing substantive {field}")
    return set(ids)

if __name__ == "__main__":
    if len(sys.argv) != 3: raise SystemExit("usage: validate_report.py REPORT CARD")
    try: print("VALID", ",".join(sorted(validate(Path(sys.argv[1]).read_text(), Path(sys.argv[2]).read_text())) or ["-" ]))
    except (OSError, ValueError) as e: raise SystemExit(f"INVALID CRITIC REPORT: {e}")
