#!/usr/bin/env python3
"""Bundled deterministic file, image, proof, and hash checks for one candidate."""

import hashlib
import re
import sys
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


if len(sys.argv) != 3:
    raise SystemExit("usage: check-candidate.py PAGE VERSION")

page = int(sys.argv[1])
version = int(sys.argv[2])
if not 33 <= page <= 49 or not 1 <= version <= 4:
    raise SystemExit("PAGE must be 33-49 and VERSION must be 1-4")

base = ROOT / "qa" / "production" / f"page-{page:02d}"
paths = {
    "candidate": base / "candidates" / f"page-{page:02d}-v{version}.png",
    "prompt": base / "prompts" / f"page-{page:02d}-v{version}.md",
    "audit": base / "audits" / f"page-{page:02d}-v{version}.md",
    "desktop": base / "proofs" / f"page-{page:02d}-v{version}-600x900.png",
    "tablet": base / "proofs" / f"page-{page:02d}-v{version}-768x1152.png",
}

for label, path in paths.items():
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"MISSING {label}: {path}")

expected = {
    "candidate": ((1024, 1536), "RGB"),
    "desktop": ((600, 900), "RGB"),
    "tablet": ((768, 1152), "RGB"),
}
for label, (size, mode) in expected.items():
    with Image.open(paths[label]) as image:
        image.load()
        if image.size != size or image.mode != mode or image.format != "PNG":
            raise SystemExit(
                f"INVALID {label}: size={image.size} mode={image.mode} format={image.format}"
            )

audit = paths["audit"].read_text()
for heading in ("## Intent read", "## Exact text check", "## Technical facts", "## Submission"):
    if len(re.findall(rf"^{re.escape(heading)}$", audit, flags=re.M)) != 1:
        raise SystemExit(f"INVALID audit: requires exactly one {heading}")
if "SUBMITTED TO INDEPENDENT CRITIC" not in audit:
    raise SystemExit("INVALID audit: missing submission statement")

print("VALID CANDIDATE")
for label, path in paths.items():
    print(f"{label.upper()} {path.relative_to(ROOT)} SHA256={digest(path)}")
