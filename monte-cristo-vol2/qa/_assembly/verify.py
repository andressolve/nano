#!/usr/bin/env python3
"""Mechanical checks on 12-PRODUCTION-PLAN.md against 08-FULL-SCRIPT.md."""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parents[2]
script = (root / "08-FULL-SCRIPT.md").read_text()
plan = (root / "12-PRODUCTION-PLAN.md").read_text()
run_dir = root / "qa" / "_run"
asm = root / "qa" / "_assembly"

CRITIC_ONLY = ["10-", "11-", "12-", "13-", "14-", "15-", "16-", "22-"]
problems = []

# --- split script into pages ---
sblocks = {}
parts = re.split(r"^## PAGE (\d+) · ", script, flags=re.M)
for i in range(1, len(parts), 2):
    sblocks[int(parts[i])] = parts[i + 1]

# --- split plan section 5 into pages ---
sec5 = plan.split("# 5 · Page prompts", 1)[1].split("\n# 6 ·", 1)[0]
pblocks = {}
pparts = re.split(r"^## PAGE (\d+) — ", sec5, flags=re.M)
for i in range(1, len(pparts), 2):
    pblocks[int(pparts[i])] = pparts[i + 1]

missing = [n for n in range(1, 50) if n not in pblocks]
if missing:
    problems.append(f"section 5 missing pages: {missing}")

# --- appendices ---
sec6 = plan.split("\n# 6 ·", 1)[1].split("\n# 7 ·", 1)[0]
appx = set(int(m) for m in re.findall(r"^## Page (\d+) — appendix", sec6, flags=re.M))
missa = [n for n in range(1, 50) if n not in appx]
if missa:
    problems.append(f"section 6 missing appendices: {missa}")

# --- string fidelity: every quoted script string must appear in its prompt ---
def script_strings(body):
    lines = re.findall(r"^> .*", body, flags=re.M)
    out = []
    for ln in lines:
        for q in re.findall(r'"([^"]*)"', ln):
            out.append(q)
    # join multi-line quoted prose fields: handle unbalanced quotes
    return out

def norm(t):
    """Normalize for comparison: markdown emphasis is markup, not text."""
    t = t.replace("*", "")
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def clean_fragment(value):
    return re.sub(r"\n\s*---\s*$", "", value).strip()


for n in sorted(sblocks):
    if n not in pblocks:
        continue
    flat_p = norm(pblocks[n])
    # a long script string may be lettered as two linked units (two paragraphs of
    # a prose field, or two same-speaker balloons). Nothing may be lost, so the
    # concatenated backticked strings must still contain it.
    pool = "".join(norm(x) for x in re.findall(r"`([^`]+)`", pblocks[n])).replace(" ", "")
    raw = re.sub(r"^> ?", "", "\n".join(re.findall(r"^>.*", sblocks[n], flags=re.M)), flags=re.M)
    for q in re.findall(r'"(.*?)"', raw, flags=re.S):
        # a multi-paragraph prose field is lettered as separate paragraphs
        for para in re.split(r"\n\s*\n", q):
            frag = norm(para)
            if len(frag) < 12:
                continue
            if frag not in flat_p and frag.replace(" ", "") not in pool:
                problems.append(f"p{n}: string not found verbatim in prompt: {frag[:70]!r}")

# --- critic-only boards must not be manifested ---
for n, pb in pblocks.items():
    for m in re.findall(r"refs/approved/(\d\d)-[a-z0-9\-]+\.png", pb):
        if m in ("10", "11", "12", "13", "14", "15", "16", "22"):
            problems.append(f"p{n}: critic-only board {m} appears in a manifest")

# --- in-app transport cap: at most five numbered reference inputs per page ---
for n, pb in pblocks.items():
    marker = "## Reference images" if "## Reference images" in pb else "### Approved image inputs"
    if marker not in pb:
        problems.append(f"p{n}: missing reference-image manifest")
        continue
    manifest = pb.split(marker, 1)[1]
    count = len(re.findall(r"^>?\s*\d+\.\s+`", manifest, flags=re.M))
    if count > 5:
        problems.append(f"p{n}: {count} reference inputs exceed the in-app cap of 5")

if 33 in pblocks:
    carrier = "refs/approved/23-page-33-chamber-objects-carrier.png"
    if carrier not in pblocks[33]:
        problems.append("p33: deterministic Chamber + objects carrier missing")
    for prohibited in ("refs/approved/19-set-chamber.png", "refs/approved/21-objects.png"):
        if prohibited in pblocks[33]:
            problems.append(f"p33: separate input remains after carrier amendment: {prohibited}")

# --- intent-first role packets: separate builder and blind critic transport ---
intent_text = (asm / "intent-first-intents-33-49.md").read_text()
intent_parts = re.split(r"^## PAGE (\d+)\s*$", intent_text, flags=re.M)
intents = {int(intent_parts[i]): intent_parts[i + 1].strip()
           for i in range(1, len(intent_parts), 2)}

for n in range(33, 50):
    bp = run_dir / f"page-{n:02d}-builder.md"
    cp = run_dir / f"page-{n:02d}-critic.md"
    cc = run_dir / f"page-{n:02d}-critic-card.md"
    if not bp.exists() or not cp.exists() or not cc.exists():
        problems.append(f"p{n}: missing intent-first builder/critic/card packet")
        continue
    page_plan = (root / "qa" / "_plan" / f"page-{n:02d}.md").read_text()
    page_sec5 = page_plan.split("# 5 · Page prompts", 1)[1].split("\n# 6 ·", 1)[0]
    prompt_match = re.search(rf"^## PAGE {n} — .*?(?=^## PAGE \d+ — |\Z)", page_sec5, flags=re.M | re.S)
    if not prompt_match:
        problems.append(f"p{n}: per-page plan has no rewritten prompt")
        continue
    prompt = prompt_match.group(0).strip()
    app_match = re.search(rf"^## Page {n} — appendix.*?(?=^# 7 ·)", page_plan, flags=re.M | re.S)
    script_match = re.search(rf"^## PAGE {n} · .*?(?=^## PAGE \d+ · |\Z)", script, flags=re.M | re.S)
    if not app_match:
        problems.append(f"p{n}: per-page plan has no numbered critic card")
    if not script_match:
        problems.append(f"p{n}: protected script page missing")
    builder_text = bp.read_text()
    critic_text = cp.read_text()
    card_text = cc.read_text()
    source_clean = clean_fragment(prompt)
    if norm(source_clean) not in norm(builder_text):
        problems.append(f"p{n}: builder packet does not contain exact rewritten prompt")
    if n not in intents or norm(intents[n]) not in norm(builder_text):
        problems.append(f"p{n}: builder packet does not contain exact page intent")
    if n not in intents or norm(intents[n]) not in norm(card_text):
        problems.append(f"p{n}: critic card does not contain exact page intent")
    if app_match and norm(clean_fragment(app_match.group(0))) not in norm(card_text):
        problems.append(f"p{n}: critic card does not contain exact numbered source card")
    if script_match and norm(clean_fragment(script_match.group(0))) not in norm(card_text):
        problems.append(f"p{n}: critic card does not contain exact script section")
    for label, packet in (("builder", builder_text), ("critic", critic_text),
                          ("critic-card", card_text)):
        if len(packet) >= 15_000:
            problems.append(f"p{n}: {label} packet is {len(packet):,} chars (target under 15 KB)")
        for other in (n - 1, n + 1):
            if 33 <= other <= 49 and re.search(rf"## PAGE {other}(?: —| ·|\s*$)|## Page {other} — appendix", packet, flags=re.M):
                problems.append(f"p{n}: {label} packet leaks neighbouring page {other}")
    if "Builder-only page prompt" in critic_text or "Builder-only page prompt" in card_text:
        problems.append(f"p{n}: generation prompt leaked into critic transport")
    if "builder-audit.md" in critic_text or "builder-audit.md" in card_text:
        problems.append(f"p{n}: builder audit path leaked into critic transport")
    criteria = re.findall(r"^### (C\d+) — ", card_text, flags=re.M)
    if len(criteria) < 4 or len(criteria) != len(set(criteria)):
        problems.append(f"p{n}: critic card needs unique numbered criteria")
    for required in ("Material reader harm", "Redraw justification", "600 × 900"):
        if required not in critic_text:
            problems.append(f"p{n}: critic entrypoint missing {required!r} contract")

for start, end in ((31, 40), (41, 49)):
    packet = run_dir / f"batch-{start:02d}-{end:02d}-script.md"
    if not packet.is_file():
        problems.append(f"missing milestone script packet {packet.name}")
        continue
    packet_text = packet.read_text()
    for n in range(start, end + 1):
        match = re.search(rf"^## PAGE {n} · .*?(?=^## PAGE \d+ · |\Z)", script, flags=re.M | re.S)
        if not match or norm(clean_fragment(match.group(0))) not in norm(packet_text):
            problems.append(f"{packet.name}: missing exact Page {n} script")
    for neighbour in (start - 1, end + 1):
        if re.search(rf"^## PAGE {neighbour} · ", packet_text, flags=re.M):
            problems.append(f"{packet.name}: leaks Page {neighbour}")

gate_dir = root / "qa" / "_intent-first"
for gate in (
    "GATE-31-40-SEQUENCE.md",
    "GATE-1-40-COLD-READ.md",
    "GATE-31-40-CONTINUITY.md",
    "GATE-41-49-SEQUENCE.md",
    "GATE-1-49-COLD-READ.md",
    "GATE-1-49-CONTINUITY.md",
    "GATE-WHOLE-BOOK.md",
):
    if not (gate_dir / gate).is_file():
        problems.append(f"missing milestone role packet: {gate}")

# --- canvas + register present in every legacy prompt; new prompts carry the
# shared generation frame in the emitted builder packet. ---
for n, pb in pblocks.items():
    if n >= 33:
        builder_path = run_dir / f"page-{n:02d}-builder.md"
        if not builder_path.is_file():
            continue
        builder = builder_path.read_text()
        for required in ("1024 × 1536", "Velvet Cinema", "600 × 900",
                         "Attach only these"):
            if required not in builder:
                problems.append(f"p{n}: builder packet missing {required!r}")
        continue
    if "1024 ×\n> 1536" not in pb and "1024 × 1536" not in pb:
        problems.append(f"p{n}: canvas 1024 x 1536 not stated")
    if "prestige-oil" not in pb:
        problems.append(f"p{n}: missing 'Not smooth prestige-oil realism' negative")
    has_text = bool(re.search(r"^> ", sblocks.get(n, ""), flags=re.M))
    if has_text and "40 px" not in pb:
        problems.append(f"p{n}: missing the 40 px floor")
    if not has_text and "no text of any kind" not in pb:
        problems.append(f"p{n}: textless page without an explicit zero-strings instruction")
    if "DOMINANT" not in pb.upper():
        problems.append(f"p{n}: no dominant panel declared")
    expected_version = 14 if n == 8 else 1
    if f"page-{n:02d}/candidates/page-{n:02d}-v{expected_version}.png" not in pb:
        problems.append(f"p{n}: output path missing or wrong")

# --- audit trail: every candidate reached the critic, and no page ran past v4 ---
# Two pages predate these checks. Recorded, not excused — they are why the checks
# exist, and nothing after page 10 may be added to this set.
#   page 4  — v1 killed in self-audit ("STOP — NOT PLAUSIBLE FOR INDEPENDENT-CRITIC
#             SUBMISSION") over two real script defects. Real or not, that verdict
#             was the critic's to make. 2 candidates, 1 report.
#   page 8  — 14 candidates, 4 reports; v1,3,4,5,6,7,9,10,11,13 never reviewed.
# Eleven candidates in total were destroyed without review before 2026-08-16.
GRANDFATHERED = {4, 8}

prod = root / "qa" / "production"
for pagedir in sorted(prod.glob("page-*")) if prod.is_dir() else []:
    n = int(pagedir.name.split("-")[1])
    cands = sorted(pagedir.glob("candidates/page-*-v*.png"))
    # only true verdicts count; owner overrides and re-judgements are suffixed
    reports = [p for p in pagedir.glob("critic-v*.md")
               if re.fullmatch(r"critic-v\d+\.md", p.name)]
    if n in GRANDFATHERED:
        continue
    if n == 32 and (pagedir / "intent-pilot" / "owner-promotion.md").exists():
        # Owner-directed historical exception: the failed pre-pilot run includes
        # one assembled component without a critic report and exceeded v4 before
        # the intent-pilot architecture was tested. Evidence is retained; Page
        # 32's canonical promotion is separately recorded and byte-verified.
        continue
    if len(cands) != len(reports):
        problems.append(
            f"p{n}: {len(cands)} candidates but {len(reports)} critic reports "
            f"— a candidate was withheld from the critic"
        )
    if len(cands) > 4:
        problems.append(
            f"p{n}: {len(cands)} generations exceeds the v4 ceiling "
            f"(the count never resets; a redesign is not a new page)"
        )

# --- per-page plan files: present, current, and materially smaller ---
# These remain audit artifacts; Pages 33-49 production roles open qa/_run.
plan_dir = root / "qa" / "_plan"
if not plan_dir.is_dir():
    problems.append("qa/_plan/ missing — run assemble.py")
else:
    per_page = sorted(plan_dir.glob("page-*.md"))
    absent = [n for n in range(1, 50) if not (plan_dir / f"page-{n:02d}.md").exists()]
    if absent:
        problems.append(f"qa/_plan/ missing pages: {absent}")
    if len(per_page) != 49:
        problems.append(f"qa/_plan/ holds {len(per_page)} files, expected 49")
    for f in per_page:
        n = int(f.stem.split("-")[1])
        body = f.read_text()
        if len(body) > len(plan) // 4:
            problems.append(f"qa/_plan/{f.name}: {len(body):,} chars is not "
                            f"materially smaller than the master — split is broken")
        if f"## PAGE {n} — " not in body:
            problems.append(f"qa/_plan/{f.name}: does not carry page {n}'s prompt")
        if f"## Page {n} — appendix" not in body:
            problems.append(f"qa/_plan/{f.name}: does not carry page {n}'s appendix")
        for other in (n - 1, n + 1):
            if 1 <= other <= 49 and f"## PAGE {other} — " in body:
                problems.append(f"qa/_plan/{f.name}: leaks page {other}'s prompt")
    if per_page and plan_dir.stat().st_mtime < (root / "12-PRODUCTION-PLAN.md").stat().st_mtime - 5:
        problems.append("qa/_plan/ is older than the master plan — re-run assemble.py")

print(f"pages in plan: {len(pblocks)}  appendices: {len(appx)}  "
      f"per-page files: {len(list((root / 'qa' / '_plan').glob('page-*.md')))}")
if problems:
    print(f"\n{len(problems)} PROBLEMS\n")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("CLEAN")
