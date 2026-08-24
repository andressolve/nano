#!/usr/bin/env python3
"""Derive and verify the text-only sample receipt and handoff from real checks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from check_adaptation import check as check_adaptation
from check_candidate import check as check_candidate
from check_preproduction import check as check_preproduction
from preflight import check as preflight
from route import route_history
from validate_report import validate


def derived_records(project: Path) -> tuple[str, str]:
    check_adaptation(project)
    check_preproduction(project, allow_ephemeral_fixture_run=True)
    script = project / "script" / "FULL-SCRIPT.md"
    contract = project / "contract" / "PAGE-CONTRACT.md"
    intent = project / "intent" / "page-01.md"
    prompt = project / "prompts" / "page-01.md"
    card = project / "cards" / "page-01.md"
    preflight(
        project / "run",
        script,
        intent,
        card,
        prompt_path=prompt,
        page="01",
        contract_path=contract,
    )

    fixtures = Path(__file__).resolve().parent / "fixtures"
    check_candidate(
        fixtures / "candidate",
        fixtures / "manifest.toml",
        fixtures / "candidate" / "hashes.json",
    )
    valid_criteria = validate((project / "reports" / "valid.md").read_text(), card.read_text())
    if valid_criteria:
        raise ValueError("approved rehearsal report unexpectedly contains criteria")
    try:
        validate((project / "reports" / "invalid.md").read_text(), card.read_text())
    except ValueError:
        invalid_rejected = True
    else:
        invalid_rejected = False
    if not invalid_rejected:
        raise ValueError("placeholder rehearsal report was accepted")

    history = json.loads((project / "reports" / "history-approved.json").read_text())
    route = route_history(history)
    if route != "PROMOTE":
        raise ValueError(f"approved rehearsal history routed to {route}")
    image_suffixes = {
        ".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".heic", ".tif", ".tiff",
    }
    images = [
        path for path in project.rglob("*")
        if path.is_file() and path.suffix.lower() in image_suffixes
    ]
    if images:
        raise ValueError("sample project must remain image-free")

    receipt = (
        "# Framework rehearsal receipt\n\n"
        "- Adaptation readiness: `CLEAN`; full panel script, page contract, whole-script readability, and hashed owner approval pass.\n"
        "- Pre-production readiness: `CLEAN`; casting/reference system, every page sibling, context map, second owner approval, and handoff pass.\n"
        "- Assembly/preflight: `CLEAN`; exact page script, page contract, intent, and card match.\n"
        "- Blind transport: version-neutral candidate and two proof paths only.\n"
        "- Candidate contract fixture: complete RGB PNGs, dimensions, and hashes valid.\n"
        "- Valid critic report: accepted. Placeholder report: rejected.\n"
        f"- Archived approved history route: `{route}`.\n"
        "- Project PNG count: `0`; image generation was not run.\n"
        "- Retention: the text-only run capsule is rehearsed in a temporary copy and is not retained in this fixture.\n"
    )
    handoff = (
        "# HANDOFF\n\n"
        "State: framework rehearsal complete.\n\n"
        f"Derived route: `{route}`. Promoted story pages: none. The adaptation "
        "and pre-production gates, exact page-script "
        "transport, deterministic candidate fixture, report validation, router, "
        "receipt, and handoff interfaces pass. The project contains no PNG and "
        "authorizes no story image or prototype. No run capsule is retained.\n"
    )
    return receipt, handoff


def verify(project: Path, *, write: bool) -> None:
    receipt, handoff = derived_records(project)
    receipt_path = project / "RECEIPT.md"
    handoff_path = project / "HANDOFF.md"
    if write:
        receipt_path.write_text(receipt)
        handoff_path.write_text(handoff)
    if not receipt_path.is_file() or receipt_path.read_text() != receipt:
        raise ValueError("RECEIPT.md does not match executed rehearsal results")
    if not handoff_path.is_file() or handoff_path.read_text() != handoff:
        raise ValueError("HANDOFF.md does not match executed rehearsal results")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        verify(Path(args.project).resolve(), write=args.write)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"REHEARSAL FAILED: {exc}") from exc
    print("REHEARSAL CLEAN")


if __name__ == "__main__":
    main()
