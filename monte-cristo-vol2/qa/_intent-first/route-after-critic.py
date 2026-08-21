#!/usr/bin/env python3
"""Choose the next production route from validated numbered critic findings."""

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def verdict_and_codes(path: Path):
    text = path.read_text()
    verdict = re.search(r"^VERDICT: (APPROVED|REVISE)$", text, flags=re.M)
    if not verdict:
        raise ValueError(f"unvalidated verdict in {path}")
    codes = set(re.findall(r"^### Finding (C\d+)$", text, flags=re.M))
    return verdict.group(1), codes


def choose_route(version, reports):
    current_verdict, current_codes = reports[-1]
    if current_verdict == "APPROVED":
        return "PROMOTE", current_codes, set()
    if not current_codes:
        raise ValueError("REVISE report has no validated criteria")
    if version == 4:
        return "V4_OWNER_HOLD", current_codes, set()
    if version == 1:
        return "TARGETED", current_codes, set()

    previous_codes = reports[-2][1]
    repeated = previous_codes & current_codes
    if version == 2:
        route = "FULL_PROMPT_RESET" if repeated else "TARGETED"
        return route, current_codes, repeated

    # version == 3. If v3 was the reset after a v1/v2 repeat, any criterion
    # that survives from v2 is resistant and stops before v4. Otherwise a
    # v2/v3 repeat receives the one available clean reset at v4.
    v1_v2_repeat = reports[0][1] & reports[1][1]
    if v1_v2_repeat and repeated:
        return "RESISTANT_DEFECT_HOLD", repeated, repeated
    if repeated:
        return "FULL_PROMPT_RESET", current_codes, repeated
    return "TARGETED", current_codes, set()


if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
    A = ("REVISE", {"C1"})
    B = ("REVISE", {"C1"})
    C = ("REVISE", {"C1"})
    D = ("REVISE", {"C2"})
    assert choose_route(1, [A])[0] == "TARGETED"
    assert choose_route(2, [A, B])[0] == "FULL_PROMPT_RESET"
    assert choose_route(3, [A, B, C])[0] == "RESISTANT_DEFECT_HOLD"
    assert choose_route(2, [A, D])[0] == "TARGETED"
    assert choose_route(3, [A, D, D])[0] == "FULL_PROMPT_RESET"
    assert choose_route(4, [A, D, D, D])[0] == "V4_OWNER_HOLD"
    assert choose_route(2, [A, ("APPROVED", set())])[0] == "PROMOTE"
    print("ROUTER SELF-TEST CLEAN")
    raise SystemExit(0)

if len(sys.argv) != 3:
    raise SystemExit("usage: route-after-critic.py PAGE VERSION")

page = int(sys.argv[1])
version = int(sys.argv[2])
if not 33 <= page <= 49 or not 1 <= version <= 4:
    raise SystemExit("PAGE must be 33-49 and VERSION must be 1-4")

reports = []
for number in range(1, version + 1):
    path = ROOT / "qa" / "production" / f"page-{page:02d}" / f"critic-v{number}.md"
    if not path.is_file():
        raise SystemExit(f"missing archived report: {path}")
    reports.append(verdict_and_codes(path))

route, criteria, repeated = choose_route(version, reports)
print(f"ROUTE: {route}")
if route in {"TARGETED", "FULL_PROMPT_RESET"}:
    print(f"NEXT_VERSION: {version + 1}")
print(f"CRITERIA: {','.join(sorted(criteria)) if criteria else '-'}")
if version in {2, 3} and route != "PROMOTE":
    print(f"REPEATED: {','.join(sorted(repeated)) if repeated else '-'}")
