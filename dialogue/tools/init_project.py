#!/usr/bin/env python3
"""Initialize a Dialogue Studio project without generating any images."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


STUDIO = Path(__file__).resolve().parents[1]
TEMPLATES = STUDIO / "templates"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

FILE_MAP = {
    "project/PROJECT-README.md": "README.md",
    "project/NEW-WORK.md": "NEW-WORK.md",
    "project/SESSION-START.md": "SESSION-START.md",
    "project/HANDOFF.md": "HANDOFF.md",
    "project/manifest.toml": "manifest.toml",
    "research/RESEARCH-BRIEF.md": "research/RESEARCH-BRIEF.md",
    "research/SOURCE-MAP.md": "research/SOURCE-MAP.md",
    "research/HANDOFF.md": "research/HANDOFF.md",
    "adaptation/AUDIENCE-PROMISE.md": "adaptation/AUDIENCE-PROMISE.md",
    "adaptation/ADAPTATION-BRIEF.md": "adaptation/ADAPTATION-BRIEF.md",
    "adaptation/STORY-ARCHITECTURE.md": "adaptation/STORY-ARCHITECTURE.md",
    "adaptation/VISUAL-DIRECTION.md": "adaptation/VISUAL-DIRECTION.md",
    "adaptation/AUDIENCE-REPORT.md": "adaptation/AUDIENCE-REPORT.md",
    "adaptation/GREENLIGHT.md": "adaptation/GREENLIGHT.md",
    "adaptation/OWNER-APPROVAL.md": "adaptation/OWNER-APPROVAL.md",
}

DIRECTORIES = (
    "research",
    "adaptation",
    "script",
    "contract",
    "refs/approved",
    "intent",
    "prompts",
    "cards",
    "pages",
    "production",
    "proofs",
    "reports",
    "run",
    "review/current",
    "gates",
)


def initialize(project: Path, *, slug: str, name: str, owner: str = "Andres") -> None:
    if not SLUG.fullmatch(slug):
        raise ValueError("slug must use lowercase letters, digits, and single hyphens")
    if not name.strip() or not owner.strip():
        raise ValueError("name and owner must be non-empty")
    if project.exists():
        raise ValueError(f"destination already exists: {project}")

    missing = [str(TEMPLATES / source) for source in FILE_MAP if not (TEMPLATES / source).is_file()]
    if missing:
        raise ValueError("missing studio templates: " + ", ".join(missing))

    for directory in DIRECTORIES:
        (project / directory).mkdir(parents=True, exist_ok=True)

    substitutions = {
        "<name>": name.strip(),
        "<slug>": slug,
        "<owner>": owner.strip(),
        'slug = "replace-me"': f'slug = "{slug}"',
    }
    for source_name, target_name in FILE_MAP.items():
        source = TEMPLATES / source_name
        text = source.read_text()
        for old, new in substitutions.items():
            text = text.replace(old, new)
        (project / target_name).write_text(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("--name", required=True)
    parser.add_argument("--owner", default="Andres")
    parser.add_argument("--works-root", default=str(STUDIO / "works"))
    args = parser.parse_args()
    project = Path(args.works_root).resolve() / args.slug
    try:
        initialize(project, slug=args.slug, name=args.name, owner=args.owner)
    except (OSError, ValueError) as exc:
        raise SystemExit(f"INITIALIZATION FAILED: {exc}") from exc
    print(f"INITIALIZED {project}")


if __name__ == "__main__":
    main()
