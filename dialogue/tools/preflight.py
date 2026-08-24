#!/usr/bin/env python3
"""Verify exact authority transport and prohibit builder-context leakage."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from assemble import approved_reference, neutral_path, prompt_references, render_packets
from check_preproduction import check as check_preproduction
from preproduction_contract import (
    extract_contract_page,
    extract_script_page,
    validate_page_sources,
)


FORBIDDEN_PHRASES = (
    "APPROVED REFERENCE PATHS", "BUILDER AUDIT", "BUILDER-ONLY GENERATION PROMPT",
    "GENERATION PROMPT", "ISSUED PROMPT", "PRIOR CRITIC REPORT", "REFERENCE MANIFEST",
    "REJECTED CANDIDATE", "REPORT HISTORY", "ROUTE MODE",
)


def extract_block(text: str, label: str) -> str:
    start = f"--- {label} START ---\n"
    end = f"\n--- {label} END ---"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"authority requires one {label} block")
    return text.split(start, 1)[1].split(end, 1)[0]


def check(
    root: Path,
    script_path: Path,
    intent_path: Path,
    card_path: Path,
    *,
    prompt_path: Path,
    page: str,
    contract_path: Path,
) -> None:
    project, page = validate_page_sources(
        script_path, contract_path, intent_path, prompt_path, card_path, page
    )
    check_preproduction(project, allow_ephemeral_fixture_run=True)
    expected_files = {"builder.md", "critic.md", "authority.md"}
    actual_files = {path.name for path in root.iterdir() if path.is_file()}
    if actual_files != expected_files:
        raise ValueError(f"run packet must contain exactly {sorted(expected_files)}; found {sorted(actual_files)}")
    blind = (root / "critic.md").read_text()
    authority = (root / "authority.md").read_text()
    if not blind.startswith("TRANSPORT: CRITIC_BLIND_STAGE\n"):
        raise ValueError("bad blind-stage marker")
    if not authority.startswith("TRANSPORT: CRITIC_AUTHORITY_STAGE\n"):
        raise ValueError("bad authority-stage marker")
    match = re.search(
        r"--- NEUTRAL MANIFEST START ---\n(.+?)\n--- NEUTRAL MANIFEST END ---", blind, re.S
    )
    if not match:
        raise ValueError("missing neutral manifest")
    try:
        manifest = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise ValueError("neutral manifest is not valid JSON") from exc
    if set(manifest) != {"transport", "candidate", "proofs", "opened_after_blind"}:
        raise ValueError("neutral manifest has unexpected fields")
    if manifest["transport"] != "CRITIC_BLIND_STAGE" or manifest["opened_after_blind"] != "authority.md":
        raise ValueError("invalid blind-to-authority handoff")
    if not isinstance(manifest["proofs"], list) or len(manifest["proofs"]) != 2:
        raise ValueError("neutral manifest requires exactly two proofs")
    if manifest["candidate"] != "review/current/candidate.png" or set(manifest["proofs"]) != {
        "review/current/proof-600x900.png",
        "review/current/proof-768x1152.png",
    }:
        raise ValueError("neutral manifest does not use the canonical candidate/proof roles")
    for value in (manifest["candidate"], *manifest["proofs"]):
        if not isinstance(value, str):
            raise ValueError("neutral paths must be strings")
        neutral_path(value)

    combined = f"{blind}\n{authority}".upper()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in combined:
            raise ValueError(f"prohibited critic context: {phrase}")
    if re.search(r"\bVERSION\s*:\s*\d+\b|(?:^|\s)V\d+(?:\s|$)", combined):
        raise ValueError("candidate version leaked into critic transport")

    script = extract_block(authority, "EXACT OWNER SCRIPT")
    intent = extract_block(authority, "READER INTENT")
    card = extract_block(authority, "NUMBERED CRITIC CARD")
    source_script = script_path.read_text()
    expected_script = extract_script_page(source_script, page)
    if script != expected_script:
        raise ValueError("authority script does not match owner script")
    if intent != intent_path.read_text().rstrip():
        raise ValueError("authority intent does not match source intent")
    if card != card_path.read_text().rstrip():
        raise ValueError("authority card does not match source card")
    builder = (root / "builder.md").read_text()
    if extract_block(builder, "OWNER SCRIPT") != expected_script:
        raise ValueError("builder script does not match owner script")
    if extract_block(builder, "READER INTENT") != intent_path.read_text().rstrip():
        raise ValueError("builder intent does not match source intent")
    expected_prompt = prompt_path.read_text().rstrip()
    if extract_block(builder, "BUILDER-ONLY GENERATION PROMPT") != expected_prompt:
        raise ValueError("builder prompt does not match locked prompt")
    reference_marker = "--- APPROVED REFERENCE PATHS ---\n"
    if builder.count(reference_marker) != 1:
        raise ValueError("builder packet requires one approved-reference block")
    reference_body = builder.split(reference_marker, 1)[1].split("\n\n", 1)[0].strip()
    expected_references = prompt_references(expected_prompt)
    expected_references = [
        approved_reference(value, page=int(page), project=project)
        for value in expected_references
    ]
    expected_reference_body = "\n".join(f"- {value}" for value in expected_references) or "- NONE"
    if reference_body != expected_reference_body:
        raise ValueError("builder references do not match locked prompt")
    contract = extract_block(builder, "OWNER PAGE CONTRACT")
    expected_contract = extract_contract_page(contract_path.read_text(), page)
    if contract != expected_contract:
        raise ValueError("builder page contract does not match owner contract")
    metadata = re.match(
        r"\AROLE: FRESH BUILDER\n\nPAGE: (\d{2})\nVERSION: ([1-4])\n"
        r"MODE: (BASE|TARGETED|FULL_PROMPT_RESET)\n\n",
        builder,
    )
    if not metadata or metadata.group(1) != page:
        raise ValueError("builder packet has invalid page/version/mode metadata")
    expected_builder, expected_blind, expected_authority = render_packets(
        script=expected_script,
        contract=expected_contract,
        intent=intent_path.read_text(),
        prompt=prompt_path.read_text(),
        card=card_path.read_text(),
        candidate="review/current/candidate.png",
        proofs=[
            "review/current/proof-600x900.png",
            "review/current/proof-768x1152.png",
        ],
        reference_values=expected_references,
        page=page,
        version=int(metadata.group(2)),
        mode=metadata.group(3),
    )
    actual_packets = {
        "builder.md": builder,
        "critic.md": blind,
        "authority.md": authority,
    }
    expected_packets = {
        "builder.md": expected_builder,
        "critic.md": expected_blind,
        "authority.md": expected_authority,
    }
    for name in expected_packets:
        if actual_packets[name] != expected_packets[name]:
            raise ValueError(f"{name} differs from its canonical byte-exact envelope")
    criteria = re.findall(r"^### (C[1-9]\d*) — ", card, re.M)
    if not criteria or len(criteria) != len(set(criteria)):
        raise ValueError("critic card needs unique numbered criteria")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("--script", required=True)
    parser.add_argument("--intent", required=True)
    parser.add_argument("--card", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--page", required=True)
    parser.add_argument("--contract", required=True)
    args = parser.parse_args()
    try:
        check(
            Path(args.root),
            Path(args.script),
            Path(args.intent),
            Path(args.card),
            prompt_path=Path(args.prompt),
            page=args.page,
            contract_path=Path(args.contract),
        )
    except (OSError, ValueError) as exc:
        raise SystemExit(f"PREFLIGHT FAILED: {exc}") from exc
    print("PREFLIGHT CLEAN")


if __name__ == "__main__":
    main()
