#!/usr/bin/env python3
"""Deterministically gate Dialogue Studio page production."""

from __future__ import annotations

import argparse
import re
import tomllib
from pathlib import Path, PurePosixPath

from check_candidate import png_info
from check_adaptation import (
    MANIFEST_PREPRODUCTION_PATHS,
    _positive_page_count,
    check as check_adaptation,
)
from preproduction_contract import (
    SHA256,
    TEXT_ITEM,
    cross_check_script_contract,
    field,
    input_capsule_digest,
    packet_digest,
    page_file,
    parse_contract,
    parse_script,
    read_complete,
    reject_approved_failure_language,
    require_headings,
    sha256_path,
)


DOCUMENTS = {
    "casting_ledger": (
        "LOCKED",
        (
            "## Cast inventory",
            "## Identity locks",
            "## Collision matrix",
            "## Age, disguise, and state changes",
            "## Silent and background roles",
            "## Approval criteria",
        ),
    ),
    "setting_object_ledger": (
        "LOCKED",
        (
            "## Setting locks",
            "## Geography and time",
            "## Consequential objects",
            "## State transitions",
            "## Approval criteria",
        ),
    ),
    "reference_plan": (
        "LOCKED",
        (
            "## Scope",
            "## Source anchors",
            "## Generative sheets",
            "## Deterministic boards",
            "## Collision and live-pair tests",
            "## Settings and consequential objects",
            "## Page binding map",
            "## Promotion and hashes",
            "## Gate",
        ),
    ),
}

INTENT_HEADINGS = (
    "## Reader event and turn",
    "## Dominant dramatic relationship",
    "## Entering and exiting state",
    "## Essential causal action and continuity",
    "## Deliberately subordinate detail",
)

PROMPT_HEADINGS = (
    "## Use case and output",
    "## Approved references",
    "## Reader event and relationship",
    "## Ordered moments",
    "## Exact text and ownership",
    "## Style and output constraints",
    "## Consequential exclusions",
    "## Deliberately demoted detail",
    "## Native lettering and completion",
)

REFERENCE_REPORT_HEADINGS = (
    "## Stage 1: blind cast-system read",
    "## Structural separation",
    "## Collision and live-pair review",
    "## Age, disguise, silhouette, and grayscale review",
    "## Setting and object continuity",
    "## Stage 2: authority check",
    "## Findings",
)

CARD_CATEGORIES = {
    "EVENT", "TEXT", "IDENTITY", "CONTINUITY", "RELATIONSHIP", "INTEGRITY",
}

CONTEXT_RULES = {
    "## Authority": {
        "Reads": "owner purpose; locked adaptation; locked full script; locked page contract; recorded owner approvals",
        "Writes": "authority receipts only",
        "Never reads": "unprotected source-fidelity arguments",
        "Never does": "lower or rewrite owner-controlled authority",
    },
    "## Script builder": {
        "Reads": "locked adaptation; story architecture; graphical direction; current script and contract drafts",
        "Writes": "full script; page contract",
        "Never reads": "generation prompts; reference artifacts; critic history",
        "Never does": "approve its own work; generate images",
    },
    "## Readability critic": {
        "Reads": "complete full script; complete page contract",
        "Writes": "readability report",
        "Never reads": "builder history; research; sources; references; generation prompts; rejected candidates",
        "Never does": "rewrite the script; approve after rereading is required",
    },
    "## Packet builder": {
        "Reads": "one script page; matching contract page; graphical direction; approved page binding map",
        "Writes": "one page intent; one builder prompt; one critic card",
        "Never reads": "neighboring page bodies; research; sources; rejected history",
        "Never does": "change story authority; copy builder context into critic context",
    },
    "## Casting and reference builder": {
        "Reads": "casting ledger; setting and object ledger; graphical direction; reference plan; approved anchors",
        "Writes": "reference candidates; methods; hashes",
        "Never reads": "generation history from rejected references",
        "Never does": "edit story authority; approve outputs; generate story pages",
    },
    "## Reference critic": {
        "Reads": "neutral reference artifacts first; then casting ledger; setting and object ledger; reference plan; reference gate",
        "Writes": "reference report",
        "Never reads": "reference generation prompts; builder audits; rejected history",
        "Never does": "edit; generate; promote",
    },
    "## Production orchestrator": {
        "Reads": "clean gate receipts; owner production approval; compact handoff; current page packet",
        "Writes": "deterministic packets; ledger; promotion receipts; dynamic handoff",
        "Never reads": "research; sources; whole script; neighboring packets; rejected art",
        "Never does": "judge art; rewrite story authority; generate images",
    },
    "## Handoff boundary": {
        "Reads": "disk state only",
        "Writes": "paths; hashes; verdicts; page count; packet digest; holds; next bounded action",
        "Never reads": "task transcripts",
        "Never does": "carry hidden context across tasks",
    },
}

HANDOFF_FIELDS = (
    "Status",
    "Phase",
    "Page count",
    "Page packet SHA-256",
    "Owner production approval",
    "Owner production approval SHA-256",
    "Adaptation gate",
    "Preproduction gate",
    "Next page",
    "Batch boundaries",
    "Open holds",
    "Next bounded action",
)

FIXTURE_HANDOFF_RECEIPT = (
    "The receiving production context reads this compact handoff and the exact "
    "authority paths it names through the manifest; it does not inherit transcripts."
)
REAL_HANDOFF_RECEIPT = (
    "This is the sole resume point. Record disk-derived state, not task transcripts."
)

FIXTURE_NEXT_ACTION = (
    "Run the text-only mechanical rehearsal and stop without generating any image."
)
REAL_NEXT_ACTION = (
    "Assemble and preflight Page 01 only from the locked current-page packet."
)


def _section(text: str, heading: str) -> str:
    start = text.index(heading) + len(heading)
    next_heading = re.search(r"(?m)^## ", text[start:])
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()


def _require_exact_h2(text: str, expected: tuple[str, ...], relative: str) -> None:
    actual = re.findall(r"(?m)^## .+$", text)
    if actual != list(expected):
        raise ValueError(f"{relative} contains an unexpected or reordered section")


def _check_context_map(text: str, relative: str) -> None:
    if field(text, "Status") != "LOCKED":
        raise ValueError(f"{relative} status must be LOCKED")
    headings = tuple(CONTEXT_RULES)
    require_headings(text, headings, relative)
    actual_h2 = re.findall(r"(?m)^## .+$", text)
    if actual_h2 != list(headings):
        raise ValueError(f"{relative} contains an unexpected or reordered context section")
    field_order = ("Reads", "Writes", "Never reads", "Never does")
    for heading, expected in CONTEXT_RULES.items():
        body = _section(text, heading)
        lines = [line.strip() for line in body.splitlines() if line.strip()]
        expected_lines = [f"{name}: {expected[name]}" for name in field_order]
        if lines != expected_lines:
            raise ValueError(f"{relative} {heading} does not match the canonical context boundary")


def _check_reference_plan_gate(text: str, relative: str) -> None:
    if re.search(
        r"(?is)\b(?:builder\s+(?:prompt|audit|notes?|history)|"
        r"(?:failure|generation|prompt|report)\s+history|"
        r"copy.{0,50}rejected|rejected.{0,30}candidate|"
        r"discarded.{0,30}(?:attempt|draft))\b",
        text,
    ):
        raise ValueError(f"{relative} contains prohibited builder or rejected-history context")
    gate = _section(text, "## Gate")
    matches = list(re.finditer(r"(?m)^### (R[1-9]\d*) — (.+)$", gate))
    identifiers = [match.group(1) for match in matches]
    if len(matches) < 3 or len(identifiers) != len(set(identifiers)):
        raise ValueError(f"{relative} gate needs at least three unique numbered criteria")
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(gate)
        body = gate[match.end() : end]
        field(body, "Blocks when")
        field(body, "Nonblocking")


def _source_fields(
    text: str,
    number: int,
    *,
    script_path: str,
    script_hash: str,
    contract_path: str,
    contract_hash: str,
) -> None:
    if field(text, "Status") != "LOCKED":
        raise ValueError(f"page {number:02d} artifact status must be LOCKED")
    if field(text, "Page") != f"{number:02d}":
        raise ValueError(f"page {number:02d} artifact has wrong Page field")
    expected = {
        "Source script": script_path,
        "Script SHA-256": script_hash,
        "Source contract": contract_path,
        "Contract SHA-256": contract_hash,
    }
    for name, value in expected.items():
        if field(text, name) != value:
            raise ValueError(f"page {number:02d} artifact has stale or incorrect {name}")


def _check_intent(path: Path, text: str) -> None:
    if field(text, "Context receipt") != "CURRENT_PAGE_STORY_ONLY":
        raise ValueError(f"{path.as_posix()} has an invalid context receipt")
    require_headings(text, INTENT_HEADINGS, path.as_posix())
    _require_exact_h2(text, INTENT_HEADINGS, path.as_posix())
    lowered = text.lower()
    forbidden = (
        "refs/approved", "attach image", "candidate version", "pixel",
        "coordinate", "panel percentage", "generation prompt", "### panel",
        "## page ", "builder instruction", "builder prompt", "reference sheet",
        "reference manifest", "prior failed", "failed image", "rejected image",
        "rejected candidate", "generation instruction",
    )
    if any(value in lowered for value in forbidden):
        raise ValueError(f"{path.as_posix()} leaks builder instructions or references")
    if re.search(
        r"\b(?:builder|maker|creator|artist|illustrator|model|prompt|reference|refs|image|render|candidate|"
        r"version|audit|history|attempts?|failed|discarded|rejected|generation|production|"
        r"pixels?|coordinates?|instruction|sheet|scrapped|drafts?|sketches?|abandoned|"
        r"artwork|concept|guide)\b",
        lowered,
    ):
        raise ValueError(f"{path.as_posix()} leaks builder instructions or references")
    for heading in INTENT_HEADINGS:
        if not _section(text, heading):
            raise ValueError(f"{path.as_posix()} has empty {heading}")


def _text_items(section: str, label: str) -> tuple[tuple[str, str, str], ...]:
    lines = [line.strip() for line in section.splitlines() if line.strip()]
    if lines == ["- NONE"]:
        return ()
    if not lines:
        raise ValueError(f"{label} exact-text section is empty")
    values = []
    for line in lines:
        match = TEXT_ITEM.fullmatch(line)
        if not match:
            raise ValueError(f"{label} has invalid exact-text item: {line}")
        values.append(tuple(part.strip() for part in match.groups()))
    return tuple(values)


def _approved_references(section: str, page: int) -> set[str]:
    lines = [line.strip() for line in section.splitlines() if line.strip()]
    if lines == ["- NONE"]:
        return set()
    if not lines or any(not line.startswith("- ") for line in lines):
        raise ValueError(f"prompt page {page:02d} has invalid approved-reference list")
    values = {line[2:].strip() for line in lines}
    if len(values) != len(lines):
        raise ValueError(f"prompt page {page:02d} repeats an approved reference")
    for value in values:
        candidate = PurePosixPath(value)
        if candidate.is_absolute() or ".." in candidate.parts:
            raise ValueError(f"prompt page {page:02d} has unsafe reference path")
        if value.startswith("pages/"):
            expected = f"pages/page-{page - 1:02d}.png"
            if page == 1 or value != expected:
                raise ValueError(
                    f"prompt page {page:02d} may reference only its immediate promoted predecessor"
                )
        elif not value.startswith("refs/approved/"):
            raise ValueError(
                f"prompt page {page:02d} reference must be approved or immediate continuity"
            )
    return values


def _check_prompt(
    path: Path,
    text: str,
    page: int,
    expected_text: tuple[tuple[str, str, str], ...],
) -> set[str]:
    require_headings(text, PROMPT_HEADINGS, path.as_posix())
    _require_exact_h2(text, PROMPT_HEADINGS, path.as_posix())
    for heading in PROMPT_HEADINGS:
        if not _section(text, heading):
            raise ValueError(f"{path.as_posix()} has empty {heading}")
    actual_text = _text_items(_section(text, "## Exact text and ownership"), path.as_posix())
    if actual_text != expected_text:
        raise ValueError(f"prompt page {page:02d} exact text/ownership differs from script")
    exact_section = _section(text, "## Exact text and ownership")
    outside_exact = text.replace("## Exact text and ownership\n\n" + exact_section, "", 1)
    for _kind, _owner, exact in expected_text:
        if exact and re.search(rf"(?<!\w){re.escape(exact)}(?!\w)", outside_exact):
            raise ValueError(
                f"prompt page {page:02d} repeats exact render text outside its ownership section"
            )
    if re.search(r'[`"“”]', outside_exact):
        raise ValueError(f"prompt page {page:02d} places quoted/renderable text outside its exact-text section")
    if re.search(
        r"(?mi)^\s*(?:[-*]\s*)?(?:extra\s+)?"
        r"(?:caption|dialogue|sound|label|text|lettering)\s*:\s*\S+",
        outside_exact,
    ):
        raise ValueError(f"prompt page {page:02d} directs renderable text outside its exact-text section")
    if re.search(
        r"(?i)\b(?:add|render|write|letter)\s+(?:extra\s+)?(?:text|caption|dialogue|label)\b",
        outside_exact,
    ):
        raise ValueError(f"prompt page {page:02d} directs invented text outside its exact-text section")
    active_text = re.compile(
        r"(?i)\b(?:include|add|render|write|letter|display|put|set|show|inscribe|"
        r"etch|emblazon|print|paint|stamp|scrawl|spell|title)\b"
        r".{0,80}\b(?:subtitle|caption|dialogue|words?|text|label|sign|balloon|"
        r"letters?|lettering|placard|inscription|headline|logo|banner|poster|notice|writing)\b"
    )
    negative = re.compile(
        r"(?i)^\s*(?:[-*]\s*)?(?:do not|don't|never|no\b|without\b|avoid\b|must not)"
    )
    for line in outside_exact.splitlines():
        if line.lstrip().startswith("#"):
            continue
        if active_text.search(line) and not negative.search(line):
            raise ValueError(
                f"prompt page {page:02d} smuggles a renderable-text directive outside its exact-text section"
            )
        if re.search(
            r"(?i)\b(?:subtitle|caption|dialogue|words?|text|label|sign|balloon|"
            r"letters?|lettering|placard|inscription|headline|logo|banner|poster|notice|writing)\b",
            line,
        ) and not negative.search(line):
            raise ValueError(
                f"prompt page {page:02d} places a renderable-text carrier outside its exact-text section"
            )
    allowed_literals = {"LOCKED", "NONE", "SHA-256", "RGB", "BASE"}
    for kind, owner, exact in expected_text:
        for value in (kind, owner, exact):
            allowed_literals.update(re.findall(r"\b[A-Z][A-Z0-9_-]{1,}\b", value))
    for line in outside_exact.splitlines():
        if (
            line.lstrip().startswith("#")
            or line.strip().startswith("- refs/approved/")
            or re.match(
                r"^(?:Status|Page|Source script|Script SHA-256|Source contract|Contract SHA-256):",
                line,
            )
        ):
            continue
        for literal in re.findall(r"\b[A-Z][A-Z0-9_-]{1,}\b", line):
            if literal not in allowed_literals:
                raise ValueError(
                    f"prompt page {page:02d} contains unapproved literal text outside its exact-text section"
                )
    return _approved_references(_section(text, "## Approved references"), page)


def _check_card(
    path: Path,
    text: str,
    page: int,
    intent_path: str,
    intent_hash: str,
) -> None:
    if field(text, "Source intent") != intent_path or field(text, "Intent SHA-256") != intent_hash:
        raise ValueError(f"card page {page:02d} is stale relative to its intent")
    forbidden = (
        "generation prompt", "builder audit", "reference manifest", "prior report",
        "candidate version", "rejected candidate", "panel percentage", "type size",
        "refs/approved/", ".png", "approved reference", "reference path",
    )
    lowered = text.lower()
    if any(value in lowered for value in forbidden):
        raise ValueError(f"card page {page:02d} contains prohibited critic context")
    if re.search(r"(?m)^## ", text):
        raise ValueError(f"card page {page:02d} contains an unexpected authority section")
    matches = list(re.finditer(r"(?m)^### (C[1-9]\d*) — (.+)$", text))
    identifiers = [match.group(1) for match in matches]
    if (
        not 3 <= len(matches) <= 8
        or identifiers != [f"C{number}" for number in range(1, len(matches) + 1)]
    ):
        raise ValueError(f"card page {page:02d} needs three to eight unique criteria")
    expected_preamble = (
        "# Numbered critic card\n\n"
        f"Status: {field(text, 'Status')}\n"
        f"Page: {field(text, 'Page')}\n"
        f"Source script: {field(text, 'Source script')}\n"
        f"Script SHA-256: {field(text, 'Script SHA-256')}\n"
        f"Source contract: {field(text, 'Source contract')}\n"
        f"Contract SHA-256: {field(text, 'Contract SHA-256')}\n"
        f"Source intent: {field(text, 'Source intent')}\n"
        f"Intent SHA-256: {field(text, 'Intent SHA-256')}"
    )
    if text[: matches[0].start()].rstrip() != expected_preamble:
        raise ValueError(f"card page {page:02d} preamble is not the closed canonical envelope")
    categories = set()
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end() : end]
        category = field(body, "Category")
        if category not in CARD_CATEGORIES:
            raise ValueError(f"card page {page:02d} criterion has invalid category")
        categories.add(category)
        blocks = field(body, "Blocks when")
        nonblocking = field(body, "Nonblocking")
        expected_body = (
            f"Category: {category}\n"
            f"Blocks when: {blocks}\n"
            f"Nonblocking: {nonblocking}"
        )
        if body.strip() != expected_body:
            raise ValueError(f"card page {page:02d} criterion is not a closed canonical envelope")
    required = {"EVENT", "TEXT", "INTEGRITY"}
    if not required.issubset(categories):
        raise ValueError(
            f"card page {page:02d} must cover EVENT, TEXT, and INTEGRITY"
        )


def _check_lock_manifest(
    project: Path,
    path: Path,
    page_count: int,
    casting_path: str,
    world_path: str,
    plan_path: str,
    fixture: bool,
) -> tuple[set[str], dict[int, set[str]]]:
    locks = tomllib.loads(path.read_text())
    header = locks.get("reference_set")
    if not isinstance(header, dict):
        raise ValueError("reference locks are missing [reference_set]")
    expected_sources = {
        "casting_ledger": casting_path,
        "casting_sha256": sha256_path(project / casting_path),
        "setting_object_ledger": world_path,
        "setting_object_sha256": sha256_path(project / world_path),
        "reference_plan": plan_path,
        "reference_plan_sha256": sha256_path(project / plan_path),
    }
    for name, value in expected_sources.items():
        if header.get(name) != value:
            raise ValueError(f"reference locks have stale or incorrect {name}")
    references = locks.get("reference", [])
    if not isinstance(references, list):
        raise ValueError("reference locks [[reference]] entries are invalid")
    if header.get("count") != len(references):
        raise ValueError("reference lock count does not match entries")
    if not fixture and not references:
        raise ValueError("non-fixture page production requires at least one approved reference lock")
    paths: set[str] = set()
    ids: set[str] = set()
    by_page = {page: set() for page in range(1, page_count + 1)}
    for entry in references:
        if not isinstance(entry, dict):
            raise ValueError("reference lock entry must be a table")
        required = {"id", "path", "sha256", "kind", "binds", "pages"}
        if set(entry) != required:
            raise ValueError("reference lock entry has an invalid schema")
        ident = entry["id"]
        relative = entry["path"]
        digest = entry["sha256"]
        pages = entry["pages"]
        if not isinstance(ident, str) or not ident or ident in ids:
            raise ValueError("reference lock ids must be unique non-empty strings")
        ids.add(ident)
        candidate = PurePosixPath(relative) if isinstance(relative, str) else PurePosixPath("/")
        if (
            candidate.is_absolute()
            or ".." in candidate.parts
            or len(candidate.parts) < 3
            or candidate.parts[:2] != ("refs", "approved")
            or candidate.suffix.lower() != ".png"
            or relative in paths
        ):
            raise ValueError("reference lock path must be a unique PNG under refs/approved/")
        if not isinstance(digest, str) or not SHA256.fullmatch(digest):
            raise ValueError(f"reference {ident} has an invalid SHA-256")
        absolute = project / relative
        if not absolute.is_file() or sha256_path(absolute) != digest:
            raise ValueError(f"reference {ident} bytes do not match the approved hash")
        png_info(absolute)
        if not isinstance(pages, list) or not pages or any(
            not isinstance(page, int) or isinstance(page, bool) or not 1 <= page <= page_count
            for page in pages
        ):
            raise ValueError(f"reference {ident} pages are invalid")
        if len(pages) != len(set(pages)):
            raise ValueError(f"reference {ident} repeats a page binding")
        if not isinstance(entry["kind"], str) or not entry["kind"].strip():
            raise ValueError(f"reference {ident} kind is empty")
        if not isinstance(entry["binds"], str) or not entry["binds"].strip():
            raise ValueError(f"reference {ident} binds is empty")
        paths.add(relative)
        for page in pages:
            by_page[page].add(relative)
    return paths, by_page


def _check_reference_report(
    project: Path,
    text: str,
    *,
    casting_path: str,
    world_path: str,
    plan_path: str,
    locks_path: str,
    reference_paths: set[str],
    manifest_owner: str,
) -> None:
    if field(text, "VERDICT") != "APPROVED" or field(text, "Status") != "APPROVED":
        raise ValueError("reference report verdict and status must be APPROVED")
    if field(text, "Review context") != "FRESH_REFERENCE_SYSTEM":
        raise ValueError("reference report must record FRESH_REFERENCE_SYSTEM context")
    if field(text, "Context receipt") != "NEUTRAL_ARTIFACTS_THEN_LOCKED_AUTHORITY_ONLY":
        raise ValueError("reference report has an invalid context receipt")
    capsule_entries = [
        (casting_path, sha256_path(project / casting_path)),
        (world_path, sha256_path(project / world_path)),
        (plan_path, sha256_path(project / plan_path)),
        (locks_path, sha256_path(project / locks_path)),
    ]
    capsule_entries.extend(
        (relative, sha256_path(project / relative)) for relative in sorted(reference_paths)
    )
    expected_capsule = input_capsule_digest(tuple(capsule_entries))
    if field(text, "Input capsule SHA-256") != expected_capsule:
        raise ValueError("reference report has a stale or non-allowlisted input capsule")
    reviewer = field(text, "Reviewer")
    if reviewer.casefold() == manifest_owner.casefold():
        raise ValueError("reference reviewer must not be the manifest owner")
    if re.search(r"(?i)\b(?:builder|owner|packet|orchestrator)\b", reviewer):
        raise ValueError("reference reviewer must be an independent critic")
    prohibited = (
        "generation prompt", "builder audit", "rejected history",
        "rejected candidate", "prompt history", "generation history",
        "reference-builder", "builder notes", "builder history",
        "prior rejected", "prior failed", "rejected-image", "failed image",
    )
    if any(value in text.lower() for value in prohibited):
        raise ValueError("reference report admits prohibited builder or rejected context")
    if re.search(
        r"(?is)\b(?:read|saw|consulted|used|reviewed)\b.{0,80}"
        r"\b(?:builder|prompt|audit|notes?|rejected|failed|history|maker|"
        r"directions|discarded|drafts?)\b",
        text,
    ):
        raise ValueError("reference report admits prohibited review context")
    reject_approved_failure_language(text, "reference report")
    expected = {
        "Casting ledger": casting_path,
        "Casting SHA-256": sha256_path(project / casting_path),
        "Setting/object ledger": world_path,
        "Setting/object SHA-256": sha256_path(project / world_path),
        "Reference plan": plan_path,
        "Reference plan SHA-256": sha256_path(project / plan_path),
        "Reference locks": locks_path,
        "Reference locks SHA-256": sha256_path(project / locks_path),
    }
    for name, value in expected.items():
        if field(text, name) != value:
            raise ValueError(f"reference report has stale or incorrect {name}")
    require_headings(text, REFERENCE_REPORT_HEADINGS, "preproduction/REFERENCE-REPORT.md")
    if text.split("## Findings", 1)[1].strip() != "NONE":
        raise ValueError("approved reference report findings must be exactly NONE")


def _check_owner_release(
    project: Path,
    text: str,
    *,
    page_count: int,
    paths: dict[str, str],
    digest: str,
    expected_authorization: str,
    manifest_owner: str,
) -> None:
    if field(text, "Status") != "APPROVED" or field(text, "Authorization") != expected_authorization:
        raise ValueError(f"owner production approval must authorize {expected_authorization}")
    if field(text, "Approved by") != manifest_owner:
        raise ValueError("owner production approval Approved by must match manifest owner")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", field(text, "Approved on")):
        raise ValueError("owner production approval date must be YYYY-MM-DD")
    if field(text, "Approved page count") != str(page_count):
        raise ValueError("owner production approval page count does not match manifest")
    bindings = (
        ("Approved script", "Script SHA-256", "full_script"),
        ("Approved contract", "Contract SHA-256", "page_contract"),
        ("Approved readability report", "Readability SHA-256", "readability_report"),
        ("Approved casting ledger", "Casting SHA-256", "casting_ledger"),
        ("Approved setting/object ledger", "Setting/object SHA-256", "setting_object_ledger"),
        ("Approved reference plan", "Reference plan SHA-256", "reference_plan"),
        ("Approved reference report", "Reference report SHA-256", "reference_report"),
        ("Approved reference locks", "Reference locks SHA-256", "reference_locks"),
        ("Approved context map", "Context map SHA-256", "context_map"),
    )
    for path_field, hash_field, key in bindings:
        relative = paths[key]
        if field(text, path_field) != relative:
            raise ValueError(f"owner production approval has incorrect {path_field}")
        if field(text, hash_field) != sha256_path(project / relative):
            raise ValueError(f"owner production approval has stale {hash_field}")
    if field(text, "Page packet SHA-256") != digest:
        raise ValueError("owner production approval has stale page packet digest")
    field(text, "Approved scope")
    field(text, "Tolerated risk")


def _check_handoff(
    project: Path,
    text: str,
    *,
    page_count: int,
    digest: str,
    approval_path: str,
    fixture: bool,
) -> None:
    parts = text.rstrip().split("\n\n")
    if len(parts) != 3 or parts[0] != "# Pre-production handoff":
        raise ValueError("preproduction handoff must use the closed canonical envelope")
    field_lines = parts[1].splitlines()
    names = [line.split(":", 1)[0] for line in field_lines if ":" in line]
    if names != list(HANDOFF_FIELDS) or len(field_lines) != len(HANDOFF_FIELDS):
        raise ValueError("preproduction handoff has an unexpected or reordered field")
    receipt = re.sub(r"\s+", " ", parts[2]).strip()
    expected_receipt = FIXTURE_HANDOFF_RECEIPT if fixture else REAL_HANDOFF_RECEIPT
    if receipt != expected_receipt:
        raise ValueError("preproduction handoff has noncanonical trailing context")
    expected_phase = "FRAMEWORK_REHEARSAL_READY" if fixture else "PREPRODUCTION_COMPLETE"
    if field(text, "Status") != "READY" or field(text, "Phase") != expected_phase:
        raise ValueError(f"preproduction handoff must be READY and {expected_phase}")
    if field(text, "Page count") != str(page_count):
        raise ValueError("preproduction handoff page count does not match manifest")
    if field(text, "Page packet SHA-256") != digest:
        raise ValueError("preproduction handoff has stale page packet digest")
    if field(text, "Owner production approval") != approval_path:
        raise ValueError("preproduction handoff names the wrong production approval")
    if field(text, "Owner production approval SHA-256") != sha256_path(project / approval_path):
        raise ValueError("preproduction handoff has stale owner production approval hash")
    if field(text, "Adaptation gate") != "READY":
        raise ValueError("preproduction handoff adaptation gate must be READY")
    expected_gate = "REHEARSAL_READY" if fixture else "READY"
    if field(text, "Preproduction gate") != expected_gate:
        raise ValueError(f"preproduction handoff preproduction gate must be {expected_gate}")
    if field(text, "Next page") != "01":
        raise ValueError("preproduction handoff must release page 01 first")
    expected_batches = (
        "Page 01 is the sole rehearsal batch."
        if fixture
        else _canonical_batch_boundaries(page_count)
    )
    if field(text, "Batch boundaries") != expected_batches:
        raise ValueError("preproduction handoff batch boundaries are not canonical")
    if field(text, "Open holds") != "NONE":
        raise ValueError("a READY preproduction handoff must have no open holds")
    expected_action = FIXTURE_NEXT_ACTION if fixture else REAL_NEXT_ACTION
    if field(text, "Next bounded action") != expected_action:
        raise ValueError("preproduction handoff has an unsafe or unbounded next action")


def _canonical_batch_boundaries(page_count: int) -> str:
    ranges = []
    for start in range(1, page_count + 1, 10):
        end = min(start + 9, page_count)
        ranges.append(
            f"Page {start:02d}" if start == end else f"Pages {start:02d}-{end:02d}"
        )
    return "; ".join(ranges) + "."


IMAGE_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".heic", ".tif", ".tiff",
    ".svg", ".bmp", ".ico",
}
FIXTURE_ARTIFACT_DIRECTORIES = (
    "pages", "production", "proofs", "refs/approved", "review/current",
)


def check(project: Path, *, allow_ephemeral_fixture_run: bool = False) -> str:
    project = project.resolve()
    check_adaptation(project)
    manifest = tomllib.loads((project / "manifest.toml").read_text())
    page_count = _positive_page_count(manifest)
    project_table = manifest["project"]
    fixture = project_table.get("fixture", False)
    if not isinstance(fixture, bool):
        raise ValueError("manifest project.fixture must be boolean when present")
    expected_authorization = "FRAMEWORK_REHEARSAL" if fixture else "PAGE_PRODUCTION"
    manifest_owner = project_table.get("owner")
    if not isinstance(manifest_owner, str) or not manifest_owner.strip():
        raise ValueError("manifest project.owner must be a non-empty string")
    paths = MANIFEST_PREPRODUCTION_PATHS

    for key, (status, headings) in DOCUMENTS.items():
        relative = paths[key]
        text = read_complete(project, relative)
        if field(text, "Status") != status:
            raise ValueError(f"{relative} status must be {status}")
        require_headings(text, headings, relative)
    context_text = read_complete(project, paths["context_map"])
    _check_context_map(context_text, paths["context_map"])
    reference_plan_text = read_complete(project, paths["reference_plan"])
    _check_reference_plan_gate(reference_plan_text, paths["reference_plan"])

    script_text = read_complete(project, paths["full_script"])
    contract_text = read_complete(project, paths["page_contract"])
    script = parse_script(script_text, page_count)
    contract = parse_contract(contract_text, page_count)
    cross_check_script_contract(script, contract)
    script_hash = sha256_path(project / paths["full_script"])
    contract_hash = sha256_path(project / paths["page_contract"])

    locks_path = project / paths["reference_locks"]
    if not locks_path.is_file():
        raise ValueError(f"missing {paths['reference_locks']}")
    reference_paths, refs_by_page = _check_lock_manifest(
        project,
        locks_path,
        page_count,
        paths["casting_ledger"],
        paths["setting_object_ledger"],
        paths["reference_plan"],
        fixture,
    )
    if not fixture and any(not refs_by_page[number] for number in refs_by_page):
        raise ValueError("every real production page requires an approved reference binding")
    report = read_complete(project, paths["reference_report"])
    _check_reference_report(
        project,
        report,
        casting_path=paths["casting_ledger"],
        world_path=paths["setting_object_ledger"],
        plan_path=paths["reference_plan"],
        locks_path=paths["reference_locks"],
        reference_paths=reference_paths,
        manifest_owner=manifest_owner,
    )

    expected_page_files = {f"page-{number:02d}.md" for number in range(1, page_count + 1)}
    for directory in ("intent", "prompts", "cards"):
        root = project / directory
        actual = {path.name for path in root.iterdir() if path.is_file()} if root.is_dir() else set()
        if actual != expected_page_files:
            raise ValueError(
                f"{directory}/ must contain exactly {sorted(expected_page_files)}; found {sorted(actual)}"
            )

    for number in range(1, page_count + 1):
        intent_path = page_file(project / "intent", number)
        prompt_path = page_file(project / "prompts", number)
        card_path = page_file(project / "cards", number)
        for path in (intent_path, prompt_path, card_path):
            if not path.is_file():
                raise ValueError(f"missing {path.relative_to(project).as_posix()}")
            text = path.read_text()
            if not text.strip() or re.search(r"<[^>\n]+>|\b(?:TBD|TODO)\b", text, re.I):
                raise ValueError(f"incomplete {path.relative_to(project).as_posix()}")

        intent = intent_path.read_text()
        prompt = prompt_path.read_text()
        card = card_path.read_text()
        for artifact in (intent, prompt, card):
            _source_fields(
                artifact,
                number,
                script_path=paths["full_script"],
                script_hash=script_hash,
                contract_path=paths["page_contract"],
                contract_hash=contract_hash,
            )
        _check_intent(intent_path, intent)
        prompt_refs = _check_prompt(prompt_path, prompt, number, script[number].text_items)
        static_refs = {value for value in prompt_refs if value.startswith("refs/approved/")}
        if static_refs != refs_by_page[number]:
            raise ValueError(
                f"prompt page {number:02d} approved references differ from lock page bindings"
            )
        intent_relative = intent_path.relative_to(project).as_posix()
        _check_card(
            card_path,
            card,
            number,
            intent_relative,
            sha256_path(intent_path),
        )

    digest = packet_digest(project, page_count)
    approval = read_complete(project, paths["owner_production_approval"])
    _check_owner_release(
        project,
        approval,
        page_count=page_count,
        paths=paths,
        digest=digest,
        expected_authorization=expected_authorization,
        manifest_owner=manifest_owner,
    )
    handoff = read_complete(project, paths["handoff"])
    _check_handoff(
        project,
        handoff,
        page_count=page_count,
        digest=digest,
        approval_path=paths["owner_production_approval"],
        fixture=fixture,
    )
    if fixture:
        images = [path for path in project.rglob("*") if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES]
        if images:
            raise ValueError("framework rehearsal project must contain zero image artifacts")
        retained = []
        for relative in FIXTURE_ARTIFACT_DIRECTORIES:
            root = project / relative
            if root.is_dir():
                retained.extend(path for path in root.rglob("*") if path.is_file())
        run = project / "run"
        if not allow_ephemeral_fixture_run and run.is_dir():
            retained.extend(path for path in run.rglob("*") if path.is_file())
        if retained:
            raise ValueError("framework rehearsal project retains generated run, review, reference, proof, or page artifacts")
    return expected_authorization


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    args = parser.parse_args()
    try:
        authorization = check(Path(args.project))
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        raise SystemExit(f"PREPRODUCTION BLOCKED: {exc}") from exc
    if authorization == "FRAMEWORK_REHEARSAL":
        print("PREPRODUCTION READY FOR FRAMEWORK REHEARSAL")
    else:
        print("PREPRODUCTION READY FOR PAGE PRODUCTION")


if __name__ == "__main__":
    main()
