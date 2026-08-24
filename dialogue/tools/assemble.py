#!/usr/bin/env python3
"""Assemble compact, transport-separated builder and critic packets."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tomllib
from pathlib import Path, PurePosixPath

from check_candidate import png_info
from check_preproduction import check as check_preproduction
from preproduction_contract import (
    extract_contract_page,
    extract_script_page,
    validate_page_sources,
)


FORBIDDEN_CRITIC_PATH_PARTS = {
    "audit", "history", "production", "prompt", "ref", "refs", "reference", "references",
    "rejected", "report", "reports",
}

NEUTRAL_FILES = {
    "candidate.png",
    "proof-600x900.png",
    "proof-768x1152.png",
}

PROMOTION_LEDGER = "production/PROMOTION-LEDGER.toml"


def _validate_promoted_predecessor(relative: str, *, page: int, project: Path) -> None:
    predecessor = page - 1
    absolute = project / relative
    if not absolute.is_file():
        raise ValueError(f"missing promoted continuity reference: {relative}")
    png_info(absolute)
    digest = hashlib.sha256(absolute.read_bytes()).hexdigest()

    ledger_path = project / PROMOTION_LEDGER
    if not ledger_path.is_file():
        raise ValueError(f"missing {PROMOTION_LEDGER}")
    ledger = tomllib.loads(ledger_path.read_text())
    if ledger.get("promotion_ledger") != {"version": 1}:
        raise ValueError("promotion ledger header must be the canonical version 1 contract")
    entries = ledger.get("promotion", [])
    if not isinstance(entries, list):
        raise ValueError("promotion ledger entries are invalid")
    matches = [
        entry for entry in entries
        if isinstance(entry, dict) and entry.get("page") == predecessor
    ]
    if len(matches) != 1:
        raise ValueError(f"promotion ledger requires one page {predecessor:02d} entry")
    entry = matches[0]
    required = {"page", "path", "sha256", "receipt", "receipt_sha256", "status"}
    if set(entry) != required or entry.get("status") != "PROMOTED":
        raise ValueError(f"promotion ledger page {predecessor:02d} entry is not canonical")
    receipt_relative = f"production/page-{predecessor:02d}/PROMOTION.md"
    if entry.get("path") != relative or entry.get("sha256") != digest:
        raise ValueError(f"promoted predecessor hash binding mismatch: {relative}")
    if entry.get("receipt") != receipt_relative:
        raise ValueError(f"promotion ledger page {predecessor:02d} names the wrong receipt")
    receipt_path = project / receipt_relative
    if not receipt_path.is_file():
        raise ValueError(f"missing promotion receipt: {receipt_relative}")
    if entry.get("receipt_sha256") != hashlib.sha256(receipt_path.read_bytes()).hexdigest():
        raise ValueError(f"stale promotion receipt hash: {receipt_relative}")
    receipt_lines = receipt_path.read_text().rstrip().splitlines()
    expected_lines = [
        "# Promotion receipt",
        "",
        "Status: PROMOTED",
        f"Page: {predecessor:02d}",
        f"Canonical: {relative}",
        f"Canonical SHA-256: {digest}",
        "Critic verdict: APPROVED",
        "Owner decision: APPROVED",
        f"Next page released: {page:02d}",
    ]
    if receipt_lines != expected_lines:
        raise ValueError(f"promotion receipt is not the closed approved envelope: {receipt_relative}")


def neutral_path(value: str) -> str:
    path = PurePosixPath(value)
    lowered = value.lower()
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"critic path must be project-relative: {value}")
    if any(part.lower() in FORBIDDEN_CRITIC_PATH_PARTS for part in path.parts):
        raise ValueError(f"critic path discloses prohibited context: {value}")
    if re.search(r"(?:^|[-_/])v\d+(?:$|[-_/\.])", lowered):
        raise ValueError(f"critic path discloses candidate version: {value}")
    if path.parts[:2] != ("review", "current") or path.name not in NEUTRAL_FILES:
        raise ValueError(f"critic path must use the canonical neutral PNG capsule: {value}")
    return path.as_posix()


def prompt_references(text: str) -> list[str]:
    heading = "## Approved references"
    if text.count(heading) != 1:
        raise ValueError("builder prompt requires exactly one approved-reference section")
    section = text.split(heading, 1)[1]
    next_heading = re.search(r"(?m)^## ", section)
    if next_heading:
        section = section[: next_heading.start()]
    lines = [line.strip() for line in section.splitlines() if line.strip()]
    if lines == ["- NONE"]:
        return []
    if not lines or any(not line.startswith("- ") for line in lines):
        raise ValueError("builder prompt has an invalid approved-reference list")
    values = [line[2:].strip() for line in lines]
    if len(values) != len(set(values)):
        raise ValueError("builder prompt repeats an approved reference")
    return values


def approved_reference(value: str, *, page: int, project: Path) -> str:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"reference must be project-relative: {value}")
    relative = path.as_posix()
    absolute = project / relative
    if relative.startswith("pages/"):
        expected = f"pages/page-{page - 1:02d}.png"
        if page == 1 or relative != expected:
            raise ValueError("only the immediate promoted predecessor may be a page reference")
        _validate_promoted_predecessor(relative, page=page, project=project)
        return relative
    if not relative.startswith("refs/approved/") or path.suffix.lower() != ".png":
        raise ValueError(f"reference is outside refs/approved/: {value}")
    locks_path = project / "preproduction" / "REFERENCE-LOCKS.toml"
    if not locks_path.is_file():
        raise ValueError("missing preproduction/REFERENCE-LOCKS.toml")
    locks = tomllib.loads(locks_path.read_text()).get("reference", [])
    matches = [item for item in locks if isinstance(item, dict) and item.get("path") == relative]
    if len(matches) != 1 or page not in matches[0].get("pages", []):
        raise ValueError(f"reference is not approved for page {page:02d}: {relative}")
    if not absolute.is_file():
        raise ValueError(f"missing approved reference: {relative}")
    png_info(absolute)
    digest = hashlib.sha256(absolute.read_bytes()).hexdigest()
    if matches[0].get("sha256") != digest:
        raise ValueError(f"approved reference hash mismatch: {relative}")
    return relative


def block(label: str, text: str) -> str:
    return f"--- {label} START ---\n{text.rstrip()}\n--- {label} END ---"


def render_packets(
    *,
    script: str,
    contract: str,
    intent: str,
    prompt: str,
    card: str,
    candidate: str,
    proofs: list[str],
    reference_values: list[str],
    page: str,
    version: int,
    mode: str,
) -> tuple[str, str, str]:
    """Return the three canonical, byte-exact transport envelopes."""
    reference_lines = "\n".join(f"- {path}" for path in reference_values) or "- NONE"
    builder = "\n\n".join((
        "ROLE: FRESH BUILDER",
        f"PAGE: {page}\nVERSION: {version}\nMODE: {mode}",
        block("OWNER SCRIPT", script),
        block("OWNER PAGE CONTRACT", contract),
        block("READER INTENT", intent),
        block("BUILDER-ONLY GENERATION PROMPT", prompt),
        f"--- APPROVED REFERENCE PATHS ---\n{reference_lines}",
        "Submit one technically valid candidate, issued prompt, non-gating audit, "
        "600x900 proof, 768x1152 proof, and SHA-256 receipt. Do not approve or promote.",
    )) + "\n"
    manifest = {
        "transport": "CRITIC_BLIND_STAGE",
        "candidate": candidate,
        "proofs": proofs,
        "opened_after_blind": "authority.md",
    }
    critic = (
        "TRANSPORT: CRITIC_BLIND_STAGE\n"
        "CANDIDATE_AND_PROOF_PATHS_ONLY\n"
        "--- NEUTRAL MANIFEST START ---\n"
        + json.dumps(manifest, indent=2)
        + "\n--- NEUTRAL MANIFEST END ---\n"
        "Blind-read the 600x900 proof before opening authority.md.\n"
    )
    authority = "\n\n".join((
        "TRANSPORT: CRITIC_AUTHORITY_STAGE",
        block("EXACT OWNER SCRIPT", script),
        block("READER INTENT", intent),
        block("NUMBERED CRITIC CARD", card),
    )) + "\n"
    return builder, critic, authority


def assemble(
    script_path: Path,
    intent_path: Path,
    prompt_path: Path,
    card_path: Path,
    out: Path,
    *,
    candidate: str,
    proofs: list[str],
    references: list[str],
    page: str,
    version: int,
    mode: str,
    contract_path: Path,
) -> None:
    if len(proofs) != 2:
        raise ValueError("exactly two neutral proof paths are required")
    candidate = neutral_path(candidate)
    proofs = [neutral_path(path) for path in proofs]
    if candidate != "review/current/candidate.png" or set(proofs) != {
        "review/current/proof-600x900.png",
        "review/current/proof-768x1152.png",
    }:
        raise ValueError("candidate/proofs must use the complete canonical neutral capsule")
    proofs = [
        "review/current/proof-600x900.png",
        "review/current/proof-768x1152.png",
    ]
    project, page = validate_page_sources(
        script_path, contract_path, intent_path, prompt_path, card_path, page
    )
    check_preproduction(project, allow_ephemeral_fixture_run=True)

    out.mkdir(parents=True, exist_ok=True)
    for stale in ("critic-card.md", "transport.json"):
        stale_path = out / stale
        if stale_path.exists():
            stale_path.unlink()

    script = extract_script_page(script_path.read_text(), page)
    contract = extract_contract_page(contract_path.read_text(), page)
    intent = intent_path.read_text()
    prompt = prompt_path.read_text()
    card = card_path.read_text()
    reference_values = [
        approved_reference(value, page=int(page), project=project) for value in references
    ]
    if prompt_references(prompt) != reference_values:
        raise ValueError("issued reference paths differ from the locked builder prompt")
    builder, critic, authority = render_packets(
        script=script,
        contract=contract,
        intent=intent,
        prompt=prompt,
        card=card,
        candidate=candidate,
        proofs=proofs,
        reference_values=reference_values,
        page=page,
        version=version,
        mode=mode,
    )
    (out / "builder.md").write_text(builder)
    (out / "critic.md").write_text(critic)
    (out / "authority.md").write_text(authority)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("script")
    parser.add_argument("intent")
    parser.add_argument("prompt")
    parser.add_argument("card")
    parser.add_argument("out")
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--proof", action="append", required=True)
    parser.add_argument("--reference", action="append", default=[])
    parser.add_argument("--page", required=True)
    parser.add_argument("--version", type=int, required=True, choices=range(1, 5))
    parser.add_argument("--mode", required=True, choices=("BASE", "TARGETED", "FULL_PROMPT_RESET"))
    parser.add_argument("--contract", required=True)
    args = parser.parse_args()
    try:
        assemble(
            Path(args.script), Path(args.intent), Path(args.prompt), Path(args.card), Path(args.out),
            candidate=args.candidate, proofs=args.proof, references=args.reference,
            page=args.page, version=args.version, mode=args.mode,
            contract_path=Path(args.contract),
        )
    except (OSError, ValueError) as exc:
        raise SystemExit(f"ASSEMBLY FAILED: {exc}") from exc
    print(f"ASSEMBLED {args.out}")


if __name__ == "__main__":
    main()
