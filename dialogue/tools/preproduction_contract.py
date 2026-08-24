#!/usr/bin/env python3
"""Shared parsers and hashes for the Dialogue Studio pre-production contract."""

from __future__ import annotations

import hashlib
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


PLACEHOLDER = re.compile(
    r"<[^>\n]+>|\[placeholder\]|\b(?:TBD|TODO)\b", re.IGNORECASE
)
SCRIPT_PAGE = re.compile(r"(?m)^## Page (\d{2,}) — ([A-Z][A-Z /_-]*)\s*$")
CONTRACT_PAGE = re.compile(r"(?m)^## Page (\d{2,})\s*$")
PANEL = re.compile(r"(?m)^### Panel (\d+)\s*$")
TEXT_ITEM = re.compile(r"^- ([A-Z][A-Z_-]*) \| ([^|\n]+?) \| (.+)$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")

SCRIPT_MODES = {"DRAMATIC", "ILLUSTRATED_PROSE", "SPECTACLE_SILENCE"}
TEXT_KINDS = {"DIALOGUE", "CAPTION", "NARRATION", "SOUND", "LETTER", "OBJECT"}

SCRIPT_PAGE_FIELDS = (
    "Entering state",
    "Dominant event",
    "Exiting state",
    "Reason to turn",
    "Panel count",
)
PANEL_FIELDS = (
    "Purpose",
    "Setting/time",
    "Visible characters",
    "Action",
    "Framing/reader order",
    "Continuity",
    "Reader inference",
)
CONTRACT_FIELDS = (
    "Mode",
    "Entering state",
    "Dominant event",
    "Decisive continuity",
    "Exiting state",
    "Reason to turn",
    "Location count",
    "Panel count",
)

FORBIDDEN_BUILDER_CONTEXT = (
    "generation prompt",
    "builder audit",
    "reference manifest",
    "refs/approved/",
    "rejected history",
    "rejected candidate",
    ".png",
)


@dataclass(frozen=True)
class ScriptPage:
    number: int
    mode: str
    body: str
    fields: dict[str, str]
    panels: tuple[str, ...]
    text_items: tuple[tuple[str, str, str], ...]


@dataclass(frozen=True)
class ContractPage:
    number: int
    body: str
    fields: dict[str, str]


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_capsule_digest(entries: tuple[tuple[str, str], ...]) -> str:
    """Hash an ordered allowlist of project-relative paths and byte hashes."""
    digest = hashlib.sha256()
    for relative, value in entries:
        if not relative or not SHA256.fullmatch(value):
            raise ValueError("input capsule entry is invalid")
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update(value.encode())
        digest.update(b"\n")
    return digest.hexdigest()


APPROVED_FAILURE_LANGUAGE = re.compile(
    r"(?i)\bfail(?:s|ed|ure)?\b|\brequires?\s+reread(?:ing)?\b|\bimpossible\b|"
    r"\bindistinguishable\b|\bconfus(?:e|ed|ing|ion)\b|\bunclear\b|\bambiguous\b|"
    r"\bmissing\b|\bcontradict(?:s|ed|ion|ory)?\b|\bunreadable\b|\bbroken\b|"
    r"\bwrong\b|\bdefect\b|\bblocking\b|\bcollid(?:e|es|ed|ing)\b|\bcannot\b"
)


def reject_approved_failure_language(text: str, label: str) -> None:
    """Reject material-failure prose that contradicts an APPROVED verdict."""
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        for match in APPROVED_FAILURE_LANGUAGE.finditer(line):
            before = line[: match.start()]
            clause = re.split(r"[,;:.]", before)[-1]
            if re.search(
                r"(?i)\b(?:no|not|without|never|none|zero|avoids?|absence)\b",
                clause,
            ):
                continue
            raise ValueError(f"{label} contains failure language under an APPROVED verdict")


def field(text: str, name: str) -> str:
    matches = re.findall(rf"(?mi)^{re.escape(name)}:\s*(.*?)\s*$", text)
    if len(matches) != 1 or not matches[0].strip():
        raise ValueError(f"requires exactly one non-empty {name} field")
    return matches[0].strip()


def bullet_field(text: str, name: str) -> str:
    matches = re.findall(rf"(?mi)^- {re.escape(name)}:\s*(.+?)\s*$", text)
    if len(matches) != 1 or not matches[0].strip():
        raise ValueError(f"panel requires exactly one non-empty {name} field")
    return matches[0].strip()


def require_headings(text: str, headings: tuple[str, ...], path: str) -> None:
    positions = []
    for heading in headings:
        if text.count(heading) != 1:
            raise ValueError(f"{path} must contain exactly one {heading}")
        positions.append(text.index(heading))
    if positions != sorted(positions):
        raise ValueError(f"{path} headings are out of order")


def read_complete(project: Path, relative: str) -> str:
    candidate = PurePosixPath(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError(f"unsafe project-relative path: {relative}")
    path = project / candidate
    if not path.is_file():
        raise ValueError(f"missing {relative}")
    text = path.read_text()
    if not text.strip():
        raise ValueError(f"empty {relative}")
    if PLACEHOLDER.search(text):
        raise ValueError(f"unresolved placeholder in {relative}")
    return text


def safe_document_path(value: str, directory: str) -> str:
    candidate = PurePosixPath(value)
    if (
        candidate.is_absolute()
        or ".." in candidate.parts
        or not candidate.parts
        or candidate.parts[0] != directory
        or candidate.suffix.lower() not in {".md", ".txt", ".toml"}
    ):
        raise ValueError(f"path must name a safe document inside {directory}/: {value}")
    return candidate.as_posix()


def _numbered_blocks(text: str, pattern: re.Pattern[str]) -> list[tuple[re.Match[str], str]]:
    matches = list(pattern.finditer(text))
    blocks = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match, text[match.end() : end].strip()))
    return blocks


def _require_sequence(numbers: list[int], count: int, label: str) -> None:
    expected = list(range(1, count + 1))
    if numbers != expected:
        raise ValueError(f"{label} must contain sequential pages 01-{count:02d}; found {numbers}")


def _closed_header(text: str, first_block: int, label: str, count: int) -> None:
    lines = [line.strip() for line in text[:first_block].splitlines() if line.strip()]
    if lines != [lines[0] if lines else "", "Status: LOCKED", f"Page count: {count}"]:
        raise ValueError(f"{label} header must contain only title, locked status, and page count")
    if not re.fullmatch(r"# [^#].+", lines[0]):
        raise ValueError(f"{label} requires one H1 title")


def _closed_fields(text: str, names: tuple[str, ...], label: str, *, bullets: bool) -> None:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    prefix = "- " if bullets else ""
    if len(lines) != len(names):
        raise ValueError(f"{label} contains an unrecognized or missing field")
    for line, name in zip(lines, names):
        marker = f"{prefix}{name}:"
        if not line.startswith(marker) or not line[len(marker) :].strip():
            raise ValueError(f"{label} fields must be complete and in canonical order")
    lowered = text.lower()
    if any(value in lowered for value in FORBIDDEN_BUILDER_CONTEXT):
        raise ValueError(f"{label} contains builder, reference, or rejected-history context")


def parse_script(text: str, expected_pages: int) -> dict[int, ScriptPage]:
    if field(text, "Status") != "LOCKED":
        raise ValueError("full script status must be LOCKED")
    try:
        declared = int(field(text, "Page count"))
    except ValueError as exc:
        raise ValueError("full script Page count must be an integer") from exc
    if declared != expected_pages:
        raise ValueError(f"full script Page count must be {expected_pages}")

    parsed: dict[int, ScriptPage] = {}
    blocks = _numbered_blocks(text, SCRIPT_PAGE)
    if blocks:
        _closed_header(text, blocks[0][0].start(), "full script", expected_pages)
    numbers = [int(match.group(1)) for match, _ in blocks]
    _require_sequence(numbers, expected_pages, "full script")
    for (match, body), number in zip(blocks, numbers):
        if match.group(2).strip() not in SCRIPT_MODES:
            raise ValueError(f"script page {number:02d} has an unsupported mode")
        first_panel = PANEL.search(body)
        if not first_panel:
            raise ValueError(f"script page {number:02d} has no panel blocks")
        _closed_fields(
            body[: first_panel.start()],
            SCRIPT_PAGE_FIELDS,
            f"script page {number:02d}",
            bullets=False,
        )
        page_fields = {name: field(body, name) for name in SCRIPT_PAGE_FIELDS}
        try:
            panel_count = int(page_fields["Panel count"])
        except ValueError as exc:
            raise ValueError(f"script page {number:02d} Panel count must be an integer") from exc
        if panel_count < 1:
            raise ValueError(f"script page {number:02d} must contain at least one panel")

        panel_blocks = _numbered_blocks(body, PANEL)
        panel_numbers = [int(panel_match.group(1)) for panel_match, _ in panel_blocks]
        if panel_numbers != list(range(1, panel_count + 1)):
            raise ValueError(
                f"script page {number:02d} panels must be sequential 1-{panel_count}"
            )
        text_items: list[tuple[str, str, str]] = []
        panels: list[str] = []
        for panel_match, panel_body in panel_blocks:
            panel_number = int(panel_match.group(1))
            if re.findall(r"(?m)^#{3,4} .+$", panel_body) != ["#### Exact text"]:
                raise ValueError(
                    f"script page {number:02d} panel {panel_number} has an unexpected section"
                )
            metadata = panel_body.split("#### Exact text", 1)[0]
            _closed_fields(
                metadata,
                PANEL_FIELDS,
                f"script page {number:02d} panel {panel_number}",
                bullets=True,
            )
            for name in PANEL_FIELDS:
                try:
                    bullet_field(panel_body, name)
                except ValueError as exc:
                    raise ValueError(
                        f"script page {number:02d} panel {panel_number}: {exc}"
                    ) from exc
            if panel_body.count("#### Exact text") != 1:
                raise ValueError(
                    f"script page {number:02d} panel {panel_number} requires one #### Exact text section"
                )
            exact = panel_body.split("#### Exact text", 1)[1]
            next_heading = re.search(r"(?m)^#{3,4} ", exact)
            if next_heading:
                exact = exact[: next_heading.start()]
            entries = [line.strip() for line in exact.splitlines() if line.strip()]
            if entries == ["- NONE"]:
                panel_items: list[tuple[str, str, str]] = []
            else:
                panel_items = []
                if not entries:
                    raise ValueError(
                        f"script page {number:02d} panel {panel_number} has empty exact text"
                    )
                for entry in entries:
                    item = TEXT_ITEM.fullmatch(entry)
                    if not item:
                        raise ValueError(
                            f"script page {number:02d} panel {panel_number} has invalid text item: {entry}"
                        )
                    kind, owner, exact_text = (part.strip() for part in item.groups())
                    if kind not in TEXT_KINDS:
                        raise ValueError(
                            f"script page {number:02d} panel {panel_number} has unsupported text kind {kind}"
                        )
                    if not owner:
                        raise ValueError(
                            f"script page {number:02d} panel {panel_number} has an empty text owner"
                        )
                    if not exact_text or exact_text == "NONE":
                        raise ValueError(
                            f"script page {number:02d} panel {panel_number} has empty exact text item"
                        )
                    panel_items.append((kind, owner, exact_text))
            text_items.extend(panel_items)
            panels.append(panel_body)

        parsed[number] = ScriptPage(
            number=number,
            mode=match.group(2).strip(),
            body=body,
            fields=page_fields,
            panels=tuple(panels),
            text_items=tuple(text_items),
        )
    return parsed


def parse_contract(text: str, expected_pages: int) -> dict[int, ContractPage]:
    if field(text, "Status") != "LOCKED":
        raise ValueError("page contract status must be LOCKED")
    try:
        declared = int(field(text, "Page count"))
    except ValueError as exc:
        raise ValueError("page contract Page count must be an integer") from exc
    if declared != expected_pages:
        raise ValueError(f"page contract Page count must be {expected_pages}")
    blocks = _numbered_blocks(text, CONTRACT_PAGE)
    if blocks:
        _closed_header(text, blocks[0][0].start(), "page contract", expected_pages)
    numbers = [int(match.group(1)) for match, _ in blocks]
    _require_sequence(numbers, expected_pages, "page contract")
    parsed = {}
    for (_, body), number in zip(blocks, numbers):
        _closed_fields(
            body,
            CONTRACT_FIELDS,
            f"contract page {number:02d}",
            bullets=False,
        )
        values = {name: field(body, name) for name in CONTRACT_FIELDS}
        for numeric in ("Location count", "Panel count"):
            try:
                number_value = int(values[numeric])
            except ValueError as exc:
                raise ValueError(
                    f"contract page {number:02d} {numeric} must be an integer"
                ) from exc
            if number_value < 1 or (numeric == "Location count" and number_value > 2):
                raise ValueError(
                    f"contract page {number:02d} {numeric} is outside the studio contract"
                )
        parsed[number] = ContractPage(number=number, body=body, fields=values)
    return parsed


def cross_check_script_contract(
    script: dict[int, ScriptPage], contract: dict[int, ContractPage]
) -> None:
    shared = (
        "Entering state",
        "Dominant event",
        "Exiting state",
        "Reason to turn",
        "Panel count",
    )
    for number, script_page in script.items():
        contract_page = contract[number]
        if contract_page.fields["Mode"] != script_page.mode:
            raise ValueError(f"page {number:02d} mode differs between script and contract")
        for name in shared:
            if contract_page.fields[name] != script_page.fields[name]:
                raise ValueError(
                    f"page {number:02d} {name} differs between script and contract"
                )


def extract_script_page(text: str, page: str | int) -> str:
    """Return one page block from a full script; preserve legacy single-page inputs."""
    matches = list(SCRIPT_PAGE.finditer(text))
    if not matches:
        return text.rstrip()
    number = int(page)
    for index, match in enumerate(matches):
        if int(match.group(1)) == number:
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            return text[match.start() : end].strip()
    raise ValueError(f"full script has no page {number:02d}")


def extract_contract_page(text: str, page: str | int) -> str:
    """Return one page block from a full page contract."""
    matches = list(CONTRACT_PAGE.finditer(text))
    if not matches:
        return text.rstrip()
    number = int(page)
    for index, match in enumerate(matches):
        if int(match.group(1)) == number:
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            return text[match.start() : end].strip()
    raise ValueError(f"page contract has no page {number:02d}")


def page_file(directory: Path, number: int) -> Path:
    return directory / f"page-{number:02d}.md"


def validate_page_sources(
    script_path: Path,
    contract_path: Path,
    intent_path: Path,
    prompt_path: Path,
    card_path: Path,
    page: str,
) -> tuple[Path, str]:
    """Bind a transport to one canonical page and its exact locked siblings."""
    if not re.fullmatch(r"\d{2}", page) or int(page) < 1:
        raise ValueError("page must be a positive two-digit page number")
    number = int(page)
    script_path = script_path.resolve()
    project = script_path.parent.parent
    expected_paths = (
        (script_path, project / "script" / "FULL-SCRIPT.md"),
        (contract_path.resolve(), project / "contract" / "PAGE-CONTRACT.md"),
        (intent_path.resolve(), project / "intent" / f"page-{page}.md"),
        (prompt_path.resolve(), project / "prompts" / f"page-{page}.md"),
        (card_path.resolve(), project / "cards" / f"page-{page}.md"),
    )
    for actual, expected in expected_paths:
        if actual != expected.resolve():
            raise ValueError(
                f"page {page} transport source must be {expected.relative_to(project).as_posix()}"
            )
        if not actual.is_file() or not actual.read_text().strip():
            raise ValueError(f"missing or empty source: {actual}")

    manifest_path = project / "manifest.toml"
    if not manifest_path.is_file():
        raise ValueError("page transport requires project manifest.toml")
    manifest = tomllib.loads(manifest_path.read_text())
    project_table = manifest.get("project")
    page_count = project_table.get("pages") if isinstance(project_table, dict) else None
    if not isinstance(page_count, int) or isinstance(page_count, bool) or page_count < number:
        raise ValueError(f"manifest does not declare page {page}")

    script_text = script_path.read_text()
    contract_text = contract_path.read_text()
    script = parse_script(script_text, page_count)
    contract = parse_contract(contract_text, page_count)
    cross_check_script_contract(script, contract)
    script_hash = sha256_path(script_path)
    contract_hash = sha256_path(contract_path)
    expected_sources = {
        "Status": "LOCKED",
        "Page": page,
        "Source script": "script/FULL-SCRIPT.md",
        "Script SHA-256": script_hash,
        "Source contract": "contract/PAGE-CONTRACT.md",
        "Contract SHA-256": contract_hash,
    }
    for path in (intent_path, prompt_path, card_path):
        text = path.read_text()
        for name, expected in expected_sources.items():
            if field(text, name) != expected:
                raise ValueError(
                    f"{path.relative_to(project).as_posix()} has incorrect {name} binding"
                )
    card_text = card_path.read_text()
    expected_intent = f"intent/page-{page}.md"
    if field(card_text, "Source intent") != expected_intent:
        raise ValueError(f"card page {page} names the wrong intent")
    if field(card_text, "Intent SHA-256") != sha256_path(intent_path):
        raise ValueError(f"card page {page} has a stale intent hash")
    return project, page


def packet_digest(project: Path, page_count: int) -> str:
    digest = hashlib.sha256()
    for directory in ("intent", "prompts", "cards"):
        for number in range(1, page_count + 1):
            relative = f"{directory}/page-{number:02d}.md"
            path = project / relative
            if not path.is_file():
                raise ValueError(f"missing {relative}")
            digest.update(relative.encode())
            digest.update(b"\0")
            digest.update(hashlib.sha256(path.read_bytes()).hexdigest().encode())
            digest.update(b"\n")
    return digest.hexdigest()
