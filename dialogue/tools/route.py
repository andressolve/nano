#!/usr/bin/env python3
"""Validate a numbered report history and choose the next deterministic route."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CRITERION = re.compile(r"^C[1-9]\d*$")


def normalize(history: object) -> list[tuple[str, set[str]]]:
    if not isinstance(history, list) or not 1 <= len(history) <= 4:
        raise ValueError("history must contain one through four reports")
    reports = []
    for index, item in enumerate(history, start=1):
        if not isinstance(item, dict) or set(item) != {"verdict", "criteria"}:
            raise ValueError(f"report {index} has an invalid schema")
        verdict, raw = item["verdict"], item["criteria"]
        if verdict not in {"APPROVED", "REVISE"} or not isinstance(raw, list):
            raise ValueError(f"report {index} has an invalid verdict/criteria")
        if len(raw) != len(set(raw)) or any(not isinstance(value, str) or not CRITERION.fullmatch(value) for value in raw):
            raise ValueError(f"report {index} has invalid criterion identifiers")
        criteria = set(raw)
        if (verdict == "APPROVED" and criteria) or (verdict == "REVISE" and not criteria):
            raise ValueError(f"report {index} has incoherent verdict/criteria")
        reports.append((verdict, criteria))
    if any(verdict == "APPROVED" for verdict, _ in reports[:-1]):
        raise ValueError("history continues after terminal approval")
    return reports


def route_history(history: object) -> str:
    try:
        reports = normalize(history)
    except ValueError:
        return "INVALID_CRITIC_REPORT"
    version = len(reports)
    verdict, current = reports[-1]
    if verdict == "APPROVED":
        return "PROMOTE"
    if version == 4:
        return "V4_OWNER_HOLD"
    if version == 1:
        return "TARGETED"
    if version == 2:
        return "FULL_PROMPT_RESET" if reports[0][1] & current else "TARGETED"
    reset_criteria = reports[0][1] & reports[1][1]
    if reset_criteria:
        return "RESISTANT_DEFECT_HOLD" if reset_criteria & current else "TARGETED"
    return "FULL_PROMPT_RESET" if reports[1][1] & current else "TARGETED"


def self_test() -> None:
    revise = lambda *criteria: {"verdict": "REVISE", "criteria": list(criteria)}
    approve = {"verdict": "APPROVED", "criteria": []}
    assert route_history([revise("C5")]) == "TARGETED"
    assert route_history([revise("C5"), revise("C6")]) == "TARGETED"
    assert route_history([revise("C5"), revise("C5")]) == "FULL_PROMPT_RESET"
    assert route_history([revise("C5"), revise("C5"), revise("C5")]) == "RESISTANT_DEFECT_HOLD"
    assert route_history([revise("C5"), revise("C6"), revise("C6")]) == "FULL_PROMPT_RESET"
    assert route_history([revise("C5"), revise("C6"), revise("C6"), revise("C6")]) == "V4_OWNER_HOLD"
    assert route_history([approve]) == "PROMOTE"
    print("ROUTER TEST CLEAN")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("history", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.history:
        raise SystemExit("usage: route.py HISTORY.json or route.py --self-test")
    try:
        history = json.loads(Path(args.history).read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"INVALID_CRITIC_REPORT: {exc}") from exc
    print(route_history(history))


if __name__ == "__main__":
    main()
