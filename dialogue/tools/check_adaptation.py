#!/usr/bin/env python3
"""Mechanically verify that a project may leave adaptation for production."""

from __future__ import annotations

import argparse
import re
import tomllib
from pathlib import Path


PLACEHOLDER = re.compile(r"<[^>\n]+>|\[placeholder\]|\b(?:TBD|TODO)\b", re.IGNORECASE)

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

MANIFEST_PATHS = {
    "audience_promise": "adaptation/AUDIENCE-PROMISE.md",
    "brief": "adaptation/ADAPTATION-BRIEF.md",
    "architecture": "adaptation/STORY-ARCHITECTURE.md",
    "visual_direction": "adaptation/VISUAL-DIRECTION.md",
    "audience_report": "adaptation/AUDIENCE-REPORT.md",
    "greenlight": "adaptation/GREENLIGHT.md",
    "owner_approval": "adaptation/OWNER-APPROVAL.md",
}


def field(text: str, name: str) -> str:
    match = re.search(rf"(?mi)^{re.escape(name)}:\s*(.+?)\s*$", text)
    if not match:
        raise ValueError(f"missing {name} field")
    return match.group(1).strip()


def require_headings(text: str, headings: tuple[str, ...], path: str) -> None:
    positions = []
    for heading in headings:
        if text.count(heading) != 1:
            raise ValueError(f"{path} must contain exactly one {heading}")
        positions.append(text.index(heading))
    if positions != sorted(positions):
        raise ValueError(f"{path} headings are out of order")


def read_complete(project: Path, relative: str) -> str:
    path = project / relative
    if not path.is_file():
        raise ValueError(f"missing {relative}")
    text = path.read_text()
    if not text.strip():
        raise ValueError(f"empty {relative}")
    if PLACEHOLDER.search(text):
        raise ValueError(f"unresolved placeholder in {relative}")
    return text


def check(project: Path) -> None:
    project = project.resolve()
    manifest_path = project / "manifest.toml"
    if not manifest_path.is_file():
        raise ValueError("missing manifest.toml")
    manifest = tomllib.loads(manifest_path.read_text())
    adaptation_paths = manifest.get("adaptation")
    if not isinstance(adaptation_paths, dict):
        raise ValueError("manifest is missing the adaptation path contract")
    mismatched = {
        key: (adaptation_paths.get(key), expected)
        for key, expected in MANIFEST_PATHS.items()
        if adaptation_paths.get(key) != expected
    }
    if mismatched:
        raise ValueError(f"manifest adaptation paths do not match the studio contract: {mismatched}")

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
    findings = report.split("## Findings", 1)[1].strip()
    if findings != "NONE":
        raise ValueError("approved audience report findings must be exactly NONE")

    owner = read_complete(project, "adaptation/OWNER-APPROVAL.md")
    for name in ("Approved by", "Approved scope", "Tolerated risk"):
        if not field(owner, name):
            raise ValueError(f"owner approval has empty {name}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", field(owner, "Approved on")):
        raise ValueError("owner approval date must be YYYY-MM-DD")

    for directory in ("script", "contract"):
        files = sorted(
            path for path in (project / directory).rglob("*")
            if path.is_file() and path.suffix.lower() in {".md", ".txt"}
        )
        if not files or not any(path.read_text().strip() for path in files):
            raise ValueError(f"{directory}/ must contain a non-empty owner-approved document")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    args = parser.parse_args()
    try:
        check(Path(args.project))
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        raise SystemExit(f"ADAPTATION BLOCKED: {exc}") from exc
    print("ADAPTATION READY")


if __name__ == "__main__":
    main()
