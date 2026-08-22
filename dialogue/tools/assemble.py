#!/usr/bin/env python3
"""Assemble compact, transport-separated builder and critic packets."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath


FORBIDDEN_CRITIC_PATH_PARTS = {
    "audit", "history", "production", "prompt", "ref", "refs", "reference", "references",
    "rejected", "report", "reports",
}


def neutral_path(value: str) -> str:
    path = PurePosixPath(value)
    lowered = value.lower()
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"critic path must be project-relative: {value}")
    if any(part.lower() in FORBIDDEN_CRITIC_PATH_PARTS for part in path.parts):
        raise ValueError(f"critic path discloses prohibited context: {value}")
    if re.search(r"(?:^|[-_/])v\d+(?:$|[-_/\.])", lowered):
        raise ValueError(f"critic path discloses candidate version: {value}")
    return path.as_posix()


def block(label: str, text: str) -> str:
    return f"--- {label} START ---\n{text.rstrip()}\n--- {label} END ---"


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
) -> None:
    if len(proofs) != 2:
        raise ValueError("exactly two neutral proof paths are required")
    candidate = neutral_path(candidate)
    proofs = [neutral_path(path) for path in proofs]
    for source in (script_path, intent_path, prompt_path, card_path):
        if not source.is_file() or not source.read_text().strip():
            raise ValueError(f"missing or empty source: {source}")

    out.mkdir(parents=True, exist_ok=True)
    for stale in ("critic-card.md", "transport.json"):
        stale_path = out / stale
        if stale_path.exists():
            stale_path.unlink()

    script = script_path.read_text()
    intent = intent_path.read_text()
    prompt = prompt_path.read_text()
    card = card_path.read_text()
    reference_lines = "\n".join(f"- {path}" for path in references) or "- NONE"
    builder = "\n\n".join((
        "ROLE: FRESH BUILDER",
        f"PAGE: {page}\nVERSION: {version}\nMODE: {mode}",
        block("OWNER SCRIPT", script),
        block("READER INTENT", intent),
        block("BUILDER-ONLY GENERATION PROMPT", prompt),
        f"--- APPROVED REFERENCE PATHS ---\n{reference_lines}",
        "Submit one technically valid candidate, issued prompt, non-gating audit, "
        "600x900 proof, 768x1152 proof, and SHA-256 receipt. Do not approve or promote.",
    ))
    (out / "builder.md").write_text(builder + "\n")

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
    (out / "critic.md").write_text(critic)
    authority = "\n\n".join((
        "TRANSPORT: CRITIC_AUTHORITY_STAGE",
        block("EXACT OWNER SCRIPT", script),
        block("READER INTENT", intent),
        block("NUMBERED CRITIC CARD", card),
    ))
    (out / "authority.md").write_text(authority + "\n")


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
    args = parser.parse_args()
    try:
        assemble(
            Path(args.script), Path(args.intent), Path(args.prompt), Path(args.card), Path(args.out),
            candidate=args.candidate, proofs=args.proof, references=args.reference,
            page=args.page, version=args.version, mode=args.mode,
        )
    except (OSError, ValueError) as exc:
        raise SystemExit(f"ASSEMBLY FAILED: {exc}") from exc
    print(f"ASSEMBLED {args.out}")


if __name__ == "__main__":
    main()
