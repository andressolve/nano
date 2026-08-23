import hashlib
import json
import shutil
import struct
import sys
import tempfile
import zlib
from pathlib import Path

import pytest

TOOLS = Path(__file__).parents[1]
FIXTURES = TOOLS / "fixtures"
SAMPLE = TOOLS.parent / "works" / "sample-dialogue"
sys.path.insert(0, str(TOOLS))

from assemble import assemble
from check_adaptation import check as check_adaptation
from check_candidate import check as check_candidate
from init_project import initialize
from preflight import check as preflight
from route import route_history
from validate_report import validate
from verify_rehearsal import verify as verify_rehearsal


def write_png(path: Path, width: int, height: int) -> None:
    def chunk(kind, payload):
        return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)
    raw = (b"\0" + b"\xff\xff\xff" * width) * height
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw))
        + chunk(b"IEND", b"")
    )


def source_files(root: Path):
    values = {
        "script.md": "# Exact owner script\nA bell rings.\n",
        "intent.md": "# Intent\nA quiet morning turns wary.\n",
        "prompt.md": "# Builder-only prompt\nCreate the finished page.\n",
        "card.md": "# Card\n### C5 — Event\nThe turn is clear.\n### C6 — Integrity\nThe page is intact.\n",
    }
    for name, text in values.items():
        (root / name).write_text(text)
    return tuple(root / name for name in ("script.md", "intent.md", "prompt.md", "card.md"))


def assemble_fixture(root: Path):
    script, intent, prompt, card = source_files(root)
    run = root / "run"
    assemble(
        script, intent, prompt, card, run,
        candidate="review/current/candidate.png",
        proofs=["review/current/proof-600x900.png", "review/current/proof-768x1152.png"],
        references=["refs/approved/person.png"], page="01", version=2, mode="TARGETED",
    )
    return script, intent, card, run


def load_route(name: str):
    return json.loads((FIXTURES / "routes" / f"{name}.json").read_text())


def test_assembly_transports_exact_script_and_neutral_paths():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        script, intent, card, run = assemble_fixture(root)
        preflight(run, script, intent, card)
        authority = (run / "authority.md").read_text()
        critic = (run / "critic.md").read_text()
        assert script.read_text().rstrip() in authority
        assert intent.read_text().rstrip() in authority
        assert "v2" not in critic.lower() and "prompt" not in critic.lower()


def test_adaptation_gate_accepts_approved_sample_and_rejects_draft():
    check_adaptation(SAMPLE)
    with tempfile.TemporaryDirectory() as directory:
        project = Path(directory) / "sample-dialogue"
        shutil.copytree(SAMPLE, project)
        greenlight = project / "adaptation" / "GREENLIGHT.md"
        greenlight.write_text(greenlight.read_text().replace("Status: PRESENTED", "Status: DRAFT"))
        with pytest.raises(ValueError):
            check_adaptation(project)
        greenlight.write_text(greenlight.read_text().replace("Status: DRAFT", "Status: PRESENTED"))
        report = project / "adaptation" / "AUDIENCE-REPORT.md"
        report.write_text(report.read_text().replace("## Findings\n\nNONE", "## Findings\n\nC1 remains unresolved"))
        with pytest.raises(ValueError):
            check_adaptation(project)


def test_initializer_creates_draft_image_free_project_once():
    with tempfile.TemporaryDirectory() as directory:
        project = Path(directory) / "first-story"
        initialize(project, slug="first-story", name="First Story", owner="Andres")
        assert (project / "NEW-WORK.md").is_file()
        assert (project / "adaptation" / "GREENLIGHT.md").is_file()
        assert (project / "research" / "SOURCE-MAP.md").is_file()
        assert not list(project.rglob("*.png"))
        with pytest.raises(ValueError):
            check_adaptation(project)
        with pytest.raises(ValueError):
            initialize(project, slug="first-story", name="First Story", owner="Andres")


def test_preflight_rejects_authority_leak_and_script_substitution():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        script, intent, card, run = assemble_fixture(root)
        (run / "authority.md").write_text((run / "authority.md").read_text() + "\nBUILDER AUDIT\n")
        with pytest.raises(ValueError):
            preflight(run, script, intent, card)
        assemble_fixture(root)
        script.write_text("# Changed owner script\n")
        with pytest.raises(ValueError):
            preflight(run, script, intent, card)


def test_candidate_accepts_complete_png_and_hash_receipt():
    check_candidate(FIXTURES / "candidate", FIXTURES / "manifest.toml", FIXTURES / "candidate" / "hashes.json")


def test_candidate_rejects_ihdr_only_png_and_manifest_mismatch():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for name in ("prompt.md", "audit.md"):
            source = FIXTURES / "candidate" / name
            (root / name).write_bytes(source.read_bytes())
        for name in ("candidate.png", "proof-600x900.png", "proof-768x1152.png"):
            (root / name).write_bytes((FIXTURES / "candidate" / name).read_bytes())
        (root / "candidate.png").write_bytes((root / "candidate.png").read_bytes()[:33])
        hashes = {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in ("candidate.png", "proof-600x900.png", "proof-768x1152.png")}
        (root / "hashes.json").write_text(json.dumps(hashes))
        with pytest.raises(ValueError):
            check_candidate(root, FIXTURES / "manifest.toml", root / "hashes.json")
        for name in ("candidate.png", "proof-600x900.png", "proof-768x1152.png"):
            (root / name).write_bytes((FIXTURES / "candidate" / name).read_bytes())
        hashes = {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in ("candidate.png", "proof-600x900.png", "proof-768x1152.png")}
        (root / "hashes.json").write_text(json.dumps(hashes))
        wrong_manifest = root / "wrong-manifest.toml"
        wrong_manifest.write_text(
            "[output]\nwidth=999\nheight=1536\nmode='RGB'\n"
            "desktop_width=600\ndesktop_height=900\n"
            "tablet_width=768\ntablet_height=1152\n"
        )
        with pytest.raises(ValueError):
            check_candidate(root, wrong_manifest, root / "hashes.json")


def test_report_approval_and_material_revision_schema():
    card = "### C5 — Event\n### C6 — Integrity\n"
    approved = "VERDICT: APPROVED\n## Blind read\nThe event is clear.\n## Visible text\nNo text.\n## Findings\nNONE\n"
    revise = (
        "VERDICT: REVISE\n## Blind read\nThe event is unclear.\n## Visible text\nThe required line is obscured.\n## Findings\n"
        "### Finding C6\n- Observation: The focal figure is visibly duplicated in the final panel.\n"
        "- Material reader harm: The duplicate changes who performs the decisive action.\n"
        "- Redraw justification: The false actor breaks the page turn enough to risk replacement.\n"
    )
    assert validate(approved, card) == set()
    assert validate(revise, card) == {"C6"}


def test_report_rejects_placeholders():
    card = "### C5 — Event\n"
    bad = "VERDICT: REVISE\n## Blind read\nx\n## Visible text\ny\n## Findings\n### Finding C5\n- Observation: short\n- Material reader harm: [placeholder]\n- Redraw justification: none\n"
    with pytest.raises(ValueError):
        validate(bad, card)


def test_report_rejects_reordered_headings():
    card = "### C5 — Event\n"
    reordered = (
        "VERDICT: REVISE\n## Findings\n### Finding C5\n"
        "- Observation: The focal action is visibly missing from the page.\n"
        "- Material reader harm: The reader cannot understand what causes the turn.\n"
        "- Redraw justification: The missing action breaks causality enough to replace the page.\n"
        "## Visible text\nThe required line is present.\n"
        "## Blind read\nThe page appears to contain no decisive event.\n"
    )
    with pytest.raises(ValueError):
        validate(reordered, card)


@pytest.mark.parametrize(
    ("fixture", "expected"),
    [
        ("approved", "PROMOTE"),
        ("targeted", "TARGETED"),
        ("full-prompt-reset", "FULL_PROMPT_RESET"),
        ("resistant-defect-hold", "RESISTANT_DEFECT_HOLD"),
        ("v4-owner-hold", "V4_OWNER_HOLD"),
        ("invalid-critic-report", "INVALID_CRITIC_REPORT"),
    ],
)
def test_archived_route_fixtures(fixture, expected):
    assert route_history(load_route(fixture)) == expected


def test_router_accepts_generic_c5_c6_criteria():
    assert route_history([{"verdict": "REVISE", "criteria": ["C5", "C6"]}]) == "TARGETED"


def test_text_only_sample_rehearses_every_interface():
    with tempfile.TemporaryDirectory() as directory:
        project = Path(directory) / "sample-dialogue"
        shutil.copytree(SAMPLE, project)
        run = project / "run"
        script = project / "script" / "page-01.md"
        intent = project / "intent" / "page-01.md"
        prompt = project / "prompts" / "page-01.md"
        card = project / "cards" / "page-01.md"
        assemble(
            script, intent, prompt, card, run,
            candidate="review/current/candidate.png",
            proofs=["review/current/proof-600x900.png", "review/current/proof-768x1152.png"],
            references=[], page="01", version=1, mode="BASE",
        )
        verify_rehearsal(project, write=True)
        verify_rehearsal(project, write=False)
        (project / "HANDOFF.md").write_text("stale handoff\n")
        with pytest.raises(ValueError):
            verify_rehearsal(project, write=False)
