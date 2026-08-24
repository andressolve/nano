#!/usr/bin/env python3
"""Verify the story authority that may open reference preparation."""

from __future__ import annotations

import argparse
import re
import tomllib
from pathlib import Path

from preproduction_contract import (
    cross_check_script_contract,
    field,
    input_capsule_digest,
    parse_contract,
    parse_script,
    read_complete,
    reject_approved_failure_language,
    require_headings,
    safe_document_path,
    sha256_path,
)


STATUS_FILES = {
    "research/RESEARCH-BRIEF.md": "COMPLETE",
    "research/SOURCE-MAP.md": "COMPLETE",
    "research/HANDOFF.md": "COMPLETE",
    "adaptation/AUDIENCE-PROMISE.md": "LOCKED",
    "adaptation/ADAPTATION-BRIEF.md": "LOCKED",
    "adaptation/STORY-ARCHITECTURE.md": "LOCKED",
    "adaptation/VISUAL-DIRECTION.md": "LOCKED",
    "adaptation/GREENLIGHT.md": "PRESENTED",
    "adaptation/OWNER-APPROVAL.md": "APPROVED",
}

HEADINGS = {
    "research/RESEARCH-BRIEF.md": (
        "## Questions", "## Boundaries", "## Source plan", "## Exclusions",
    ),
    "research/SOURCE-MAP.md": (
        "## Protected claims", "## Story options", "## Variants and uncertainty",
        "## Sensitive material", "## Background only", "## Sources",
    ),
    "research/HANDOFF.md": (
        "## Answers", "## Story opportunities", "## Unresolved", "## Source pointers",
    ),
    "adaptation/AUDIENCE-PROMISE.md": (
        "## Intended readers", "## Emotional promise", "## Story pleasures",
        "## Complexity budget", "## Non-goals",
    ),
    "adaptation/ADAPTATION-BRIEF.md": (
        "## Governing story", "## Story engine", "## Viewpoint and agency",
        "## Adaptation liberties", "## Protected claims", "## Exclusions",
    ),
    "adaptation/STORY-ARCHITECTURE.md": (
        "## Volume arc", "## Scene sequence", "## Ending payoff",
        "## Density and breathing",
    ),
    "adaptation/VISUAL-DIRECTION.md": (
        "## Story-world register", "## Character and world design",
        "## Palette and motifs", "## Page and lettering grammar",
        "## Historical anchors and stylization", "## Avoid", "## Reference plan",
    ),
    "adaptation/GREENLIGHT.md": (
        "## Audience promise and hook", "## Proposed story", "## How it will be told",
        "## Character arcs and relationships", "## Set pieces and emotional progression",
        "## Adaptation decisions", "## Protected claims and sensitivities",
        "## Graphical direction", "## Critic result and risks",
        "## Owner decisions requested", "## Proposed next step",
    ),
}

REPORT_HEADINGS = (
    "## Stage 1: Story-only read",
    "## Engagement map",
    "## Density and breathing",
    "## Stage 2: Protected-claim check",
    "## Findings",
)

READABILITY_HEADINGS = (
    "## Whole-script first read",
    "## Causality and character knowledge",
    "## Physical continuity",
    "## Dialogue and attribution",
    "## Density and breathing",
    "## Page reviews",
    "## Findings",
)

READABILITY_PAGE_FIELDS = (
    "First-read paraphrase",
    "Causality and knowledge",
    "Physical continuity",
    "Dialogue and attribution",
    "Reading load",
    "Turn",
    "Page verdict",
)

MANIFEST_ADAPTATION_PATHS = {
    "audience_promise": "adaptation/AUDIENCE-PROMISE.md",
    "brief": "adaptation/ADAPTATION-BRIEF.md",
    "architecture": "adaptation/STORY-ARCHITECTURE.md",
    "visual_direction": "adaptation/VISUAL-DIRECTION.md",
    "audience_report": "adaptation/AUDIENCE-REPORT.md",
    "greenlight": "adaptation/GREENLIGHT.md",
    "owner_approval": "adaptation/OWNER-APPROVAL.md",
}

MANIFEST_PREPRODUCTION_PATHS = {
    "full_script": "script/FULL-SCRIPT.md",
    "page_contract": "contract/PAGE-CONTRACT.md",
    "readability_report": "preproduction/READABILITY-REPORT.md",
    "casting_ledger": "preproduction/CASTING-LEDGER.md",
    "setting_object_ledger": "preproduction/SETTING-OBJECT-LEDGER.md",
    "reference_plan": "preproduction/REFERENCE-PLAN.md",
    "reference_report": "preproduction/REFERENCE-REPORT.md",
    "reference_locks": "preproduction/REFERENCE-LOCKS.toml",
    "owner_production_approval": "preproduction/OWNER-PRODUCTION-APPROVAL.md",
    "context_map": "preproduction/CONTEXT-MAP.md",
    "handoff": "preproduction/PREPRODUCTION-HANDOFF.md",
}


def _manifest_paths(manifest: dict, section: str, expected: dict[str, str]) -> None:
    values = manifest.get(section)
    if not isinstance(values, dict):
        raise ValueError(f"manifest is missing the {section} path contract")
    mismatched = {
        key: (values.get(key), target)
        for key, target in expected.items()
        if values.get(key) != target
    }
    if mismatched:
        raise ValueError(f"manifest {section} paths do not match the studio contract: {mismatched}")


def _positive_page_count(manifest: dict) -> int:
    project = manifest.get("project")
    if not isinstance(project, dict):
        raise ValueError("manifest is missing [project]")
    pages = project.get("pages")
    if not isinstance(pages, int) or isinstance(pages, bool) or pages < 1:
        raise ValueError("manifest project.pages must be a positive integer")
    return pages


def _check_readability(
    text: str,
    script_relative: str,
    script_hash: str,
    contract_relative: str,
    contract_hash: str,
    page_count: int,
    manifest_owner: str,
) -> None:
    name = "preproduction/READABILITY-REPORT.md"
    if field(text, "VERDICT") != "APPROVED" or field(text, "Status") != "APPROVED":
        raise ValueError("readability report verdict and status must be APPROVED")
    if field(text, "Script") != script_relative:
        raise ValueError("readability report Script does not name the locked full script")
    if field(text, "Script SHA-256") != script_hash:
        raise ValueError("readability report is stale relative to the full script")
    if field(text, "Contract") != contract_relative:
        raise ValueError("readability report Contract does not name the locked page contract")
    if field(text, "Contract SHA-256") != contract_hash:
        raise ValueError("readability report is stale relative to the page contract")
    if field(text, "Review context") != "FRESH_COMPLETE_SCRIPT":
        raise ValueError("readability report must record FRESH_COMPLETE_SCRIPT context")
    if field(text, "Reviewed page count") != str(page_count):
        raise ValueError("readability report page count does not match manifest")
    if field(text, "Context receipt") != "SCRIPT_AND_CONTRACT_ONLY":
        raise ValueError("readability report must record SCRIPT_AND_CONTRACT_ONLY context")
    expected_capsule = input_capsule_digest((
        (script_relative, script_hash),
        (contract_relative, contract_hash),
    ))
    if field(text, "Input capsule SHA-256") != expected_capsule:
        raise ValueError("readability report has a stale or non-allowlisted input capsule")
    reviewer = field(text, "Reviewer")
    if reviewer.casefold() == manifest_owner.casefold():
        raise ValueError("readability reviewer must not be the manifest owner")
    if re.search(r"(?i)\b(?:builder|owner|packet|orchestrator)\b", reviewer):
        raise ValueError("readability reviewer must be an independent critic")
    forbidden_context = (
        "builder audit",
        "builder prompt",
        "builder notes",
        "generation prompt",
        "generation notes",
        "rejected candidate",
        "rejected-image",
        "prior rejected",
        "prior failed",
        "reference manifest",
        "reference-builder",
        "report history",
        "source-fidelity",
        "source text",
    )
    lowered = text.lower()
    if any(value in lowered for value in forbidden_context):
        raise ValueError("readability report contains prohibited context")
    if re.search(
        r"(?is)\b(?:read|saw|consulted|used|reviewed)\b.{0,80}"
        r"\b(?:builder|prompt|audit|rejected|failed|history|generation notes?|"
        r"maker|directions|discarded|drafts?)\b",
        text,
    ):
        raise ValueError("readability report admits prohibited review context")
    reject_approved_failure_language(text, "readability report")
    require_headings(text, READABILITY_HEADINGS, name)
    page_area = text.split("## Page reviews", 1)[1].split("## Findings", 1)[0]
    matches = list(re.finditer(r"(?m)^### Page (\d{2,})\s*$", page_area))
    numbers = [int(match.group(1)) for match in matches]
    if numbers != list(range(1, page_count + 1)):
        raise ValueError("readability report must review every page in sequence")
    for index, match in enumerate(matches):
        number = numbers[index]
        end = matches[index + 1].start() if index + 1 < len(matches) else len(page_area)
        body = page_area[match.end() : end]
        for page_field in READABILITY_PAGE_FIELDS:
            value = field(body, page_field)
            if page_field not in {"First-read paraphrase", "Page verdict"}:
                if not value.startswith("PASS — "):
                    raise ValueError(
                        f"readability page {number:02d} {page_field} must begin PASS —"
                    )
        if field(body, "Page verdict") != "PASS":
            raise ValueError(f"readability page {number:02d} verdict must be PASS")
    if text.split("## Findings", 1)[1].strip() != "NONE":
        raise ValueError("approved readability report findings must be exactly NONE")


def _approved_document(
    project: Path,
    owner: str,
    path_field: str,
    hash_field: str,
    directory: str,
    expected_relative: str,
) -> None:
    relative = safe_document_path(field(owner, path_field), directory)
    if relative != expected_relative:
        raise ValueError(f"{path_field} must be {expected_relative}")
    actual = sha256_path(project / relative)
    if field(owner, hash_field) != actual:
        raise ValueError(f"{hash_field} is stale or incorrect")


def check(project: Path) -> None:
    project = project.resolve()
    manifest_path = project / "manifest.toml"
    if not manifest_path.is_file():
        raise ValueError("missing manifest.toml")
    manifest = tomllib.loads(manifest_path.read_text())
    _manifest_paths(manifest, "adaptation", MANIFEST_ADAPTATION_PATHS)
    _manifest_paths(manifest, "preproduction", MANIFEST_PREPRODUCTION_PATHS)
    page_count = _positive_page_count(manifest)
    manifest_owner = manifest["project"].get("owner")
    if not isinstance(manifest_owner, str) or not manifest_owner.strip():
        raise ValueError("manifest project.owner must be a non-empty string")

    for relative, expected in STATUS_FILES.items():
        text = read_complete(project, relative)
        if field(text, "Status") != expected:
            raise ValueError(f"{relative} status must be {expected}")
        if relative in HEADINGS:
            require_headings(text, HEADINGS[relative], relative)

    report_name = "adaptation/AUDIENCE-REPORT.md"
    report = read_complete(project, report_name)
    if field(report, "VERDICT") != "APPROVED":
        raise ValueError("audience report verdict must be APPROVED")
    require_headings(report, REPORT_HEADINGS, report_name)
    if report.split("## Findings", 1)[1].strip() != "NONE":
        raise ValueError("approved audience report findings must be exactly NONE")

    script_relative = MANIFEST_PREPRODUCTION_PATHS["full_script"]
    contract_relative = MANIFEST_PREPRODUCTION_PATHS["page_contract"]
    readability_relative = MANIFEST_PREPRODUCTION_PATHS["readability_report"]
    script_text = read_complete(project, script_relative)
    contract_text = read_complete(project, contract_relative)
    readability = read_complete(project, readability_relative)
    script = parse_script(script_text, page_count)
    contract = parse_contract(contract_text, page_count)
    cross_check_script_contract(script, contract)
    script_hash = sha256_path(project / script_relative)
    contract_hash = sha256_path(project / contract_relative)
    _check_readability(
        readability,
        script_relative,
        script_hash,
        contract_relative,
        contract_hash,
        page_count,
        manifest_owner,
    )

    owner = read_complete(project, "adaptation/OWNER-APPROVAL.md")
    for name in ("Approved by", "Approved scope", "Tolerated risk"):
        field(owner, name)
    if field(owner, "Approved by") != manifest_owner:
        raise ValueError("adaptation approval Approved by must match manifest owner")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", field(owner, "Approved on")):
        raise ValueError("owner approval date must be YYYY-MM-DD")
    if field(owner, "Approved page count") != str(page_count):
        raise ValueError("owner approval page count does not match manifest")
    story_bindings = (
        ("Approved audience promise", "Audience promise SHA-256", "audience_promise"),
        ("Approved adaptation brief", "Adaptation brief SHA-256", "brief"),
        ("Approved architecture", "Architecture SHA-256", "architecture"),
        ("Approved graphical direction", "Graphical direction SHA-256", "visual_direction"),
        ("Approved audience report", "Audience report SHA-256", "audience_report"),
        ("Approved greenlight", "Greenlight SHA-256", "greenlight"),
    )
    for path_field, hash_field, key in story_bindings:
        _approved_document(
            project,
            owner,
            path_field,
            hash_field,
            "adaptation",
            MANIFEST_ADAPTATION_PATHS[key],
        )
    _approved_document(
        project, owner, "Approved script", "Script SHA-256", "script", script_relative
    )
    _approved_document(
        project, owner, "Approved contract", "Contract SHA-256", "contract", contract_relative
    )
    _approved_document(
        project,
        owner,
        "Approved readability report",
        "Readability SHA-256",
        "preproduction",
        readability_relative,
    )
    scope = field(owner, "Approved scope")
    for relative, digest in (
        (script_relative, script_hash),
        (contract_relative, contract_hash),
        (readability_relative, sha256_path(project / readability_relative)),
    ):
        if relative not in scope or digest not in scope:
            raise ValueError(f"Approved scope must bind {relative} and its SHA-256")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    args = parser.parse_args()
    try:
        check(Path(args.project))
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        raise SystemExit(f"ADAPTATION BLOCKED: {exc}") from exc
    print("ADAPTATION READY FOR REFERENCE PREPARATION")


if __name__ == "__main__":
    main()
