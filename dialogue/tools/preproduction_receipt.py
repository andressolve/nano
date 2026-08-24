#!/usr/bin/env python3
"""Print stable hashes needed for Dialogue Studio pre-production approvals."""

from __future__ import annotations

import argparse
import json
import tomllib
from pathlib import Path

from check_adaptation import MANIFEST_PREPRODUCTION_PATHS, _positive_page_count
from preproduction_contract import (
    cross_check_script_contract,
    packet_digest,
    parse_contract,
    parse_script,
    sha256_path,
)


def receipt(project: Path) -> dict:
    project = project.resolve()
    manifest = tomllib.loads((project / "manifest.toml").read_text())
    page_count = _positive_page_count(manifest)
    configured = manifest.get("preproduction")
    if configured != MANIFEST_PREPRODUCTION_PATHS:
        raise ValueError("manifest preproduction path contract is incomplete or noncanonical")
    script_path = project / MANIFEST_PREPRODUCTION_PATHS["full_script"]
    contract_path = project / MANIFEST_PREPRODUCTION_PATHS["page_contract"]
    script = parse_script(script_path.read_text(), page_count)
    contract = parse_contract(contract_path.read_text(), page_count)
    cross_check_script_contract(script, contract)
    documents = {}
    for key, relative in MANIFEST_PREPRODUCTION_PATHS.items():
        path = project / relative
        documents[key] = {
            "path": relative,
            "sha256": sha256_path(path) if path.is_file() else None,
        }
    return {
        "page_count": page_count,
        "documents": documents,
        "page_packet_sha256": packet_digest(project, page_count),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    args = parser.parse_args()
    try:
        value = receipt(Path(args.project))
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        raise SystemExit(f"PREPRODUCTION RECEIPT BLOCKED: {exc}") from exc
    print(json.dumps(value, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
