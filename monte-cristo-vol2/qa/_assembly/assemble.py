#!/usr/bin/env python3
"""Assemble 12-PRODUCTION-PLAN.md from its fragments, and emit the compact
intent-first role packets used for Pages 33-49.

Idempotent: rebuilds sections 5-10 from the on-disk head (sections 1-4 +
pages 1-2) each time.

The legacy per-page files remain useful as source evidence. Production roles
open only qa/_run packets. The critic entrypoint is deliberately separate from
the script/intent/card packet so its first image read stays blind.
"""
import re, pathlib, shutil, datetime

root = pathlib.Path(__file__).resolve().parents[2]
asm = root / "qa" / "_assembly"
plan = root / "12-PRODUCTION-PLAN.md"
plan_dir = root / "qa" / "_plan"
run_dir = root / "qa" / "_run"

SEP = "\n\n---\n\n"


def split_sections(body, pattern):
    """{page number: section text} for every heading matching pattern."""
    found = {}
    hits = list(re.finditer(pattern, body, flags=re.M))
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
        chunk = body[m.start():end].strip().rstrip("-").strip()
        found[int(m.group(1))] = chunk
    return found


def selected_sections(body, pattern, keep):
    sections = split_sections(body, pattern)
    return SEP.join(sections[n] for n in sorted(sections) if keep(n))

text = plan.read_text()
# keep sections 1-4 and section 5's pages 1-2; everything after is rebuilt from
# the fragments. Cutting at "# 6 ·" instead would retain the previous run's own
# page prompts and append the fragments a second time.
assert text.count("\n## PAGE 3 — ") >= 1
head = text.split("\n## PAGE 3 — ", 1)[0].rstrip("\n").rstrip("-").rstrip("\n")
backup = asm / f"plan-before-assembly-{datetime.date.today()}.md"
if not backup.exists():
    shutil.copy(plan, backup)

legacy_prompt_frags = ["prompts-03-14.md", "prompts-15-26.md"]
legacy_appendix_frags = ["appendix-03-14.md", "appendix-15-26.md"]

# Pages 33-49 use the owner-approved intent-first rewrite. The old Page 33+
# tails remain on disk as historical evidence but are no longer assembly input.
prompt_sources = [(asm / name).read_text().strip()
                  for name in legacy_prompt_frags]
prompt_sources.append(selected_sections(
    (asm / "prompts-27-37.md").read_text(),
    r"^## PAGE (\d+) — ",
    lambda n: 27 <= n <= 32,
))
prompt_sources.append(selected_sections(
    (asm / "intent-first-prompts-33-49.md").read_text(),
    r"^## PAGE (\d+) — ",
    lambda n: 33 <= n <= 49,
))

appendix_sources = [(asm / name).read_text().strip()
                    for name in legacy_appendix_frags]
appendix_sources.append(selected_sections(
    (asm / "appendix-27-37.md").read_text(),
    r"^## Page (\d+) — appendix",
    lambda n: 27 <= n <= 32,
))
appendix_sources.append(selected_sections(
    (asm / "intent-first-cards-33-49.md").read_text(),
    r"^## Page (\d+) — appendix",
    lambda n: 33 <= n <= 49,
))

intent_source = (asm / "intent-first-intents-33-49.md").read_text()
intents = split_sections(intent_source, r"^## PAGE (\d+)\s*$")

parts = [head]
parts.extend(prompt_sources)

# section 6: current architecture + verbatim current operations + historical
# page-1/2 appendices. The old section-6 intro is retained on disk as evidence
# but is no longer assembled because it exposed prompts and audits to critics.
legacy_sec6 = (asm / "section-6-head.md").read_text()
page_1_2_appendices = "## Page 1 — appendix\n\n" + legacy_sec6.split(
    "## Page 1 — appendix", 1
)[1].strip()
crit = (root / "10-CRITIC-OPERATIONS.md").read_text()
crit = crit.split("\n# 1 · The page critic", 1)[1]
crit = "# 1 · The page critic" + crit
crit = re.sub(r"^## ", "#### ", crit, flags=re.M)
crit = re.sub(r"^# ", "### ", crit, flags=re.M)

sec6_intro = """# 6 · Intent-first builder / critic architecture

Pages 33-49 use three separate compact transports per page:

- the builder packet contains the shared generation frame, page intent,
  builder-only rewritten prompt, reference manifest, and output contract;
- the blind critic entrypoint contains only neutral image paths, staged review
  order, and the report schema;
- the critic-card packet, opened only after the blind read, contains the exact
  script, page intent, materiality threshold, and numbered blocking criteria.

The critic never receives the generation prompt or builder audit. The builder
audit never gates submission. The orchestrator is nonvisual and validates the
report contract and numbered retry route mechanically.

Each numbered criterion is a stable defect signature. A repeat after a targeted
correction triggers a clean prompt reset; persistence after that reset stops for
the owner. Any v4 REVISE remains an owner hold.

## Current operations, verbatim
"""

sec6 = SEP.join([
    sec6_intro.strip(),
    crit.strip(),
    """## How to use the numbered page cards

For Pages 33-49, use only the emitted `qa/_run/page-NN-critic-card.md` after the
blind image read. A finding must cite a numbered criterion, state material
reader harm, and justify a complete redraw. True but nonconsequential defects
are omitted and the page is approved.

Pages 1-32 below retain their historical appendices as production evidence;
they are not inputs to the remaining-page critic.""",
    page_1_2_appendices,
])
parts.append(sec6)

parts.extend(appendix_sources)

sections_7_10 = (asm / "sections-7-9.md").read_text().strip()
parts.append(sections_7_10)

out = SEP.join(parts) + "\n"
plan.write_text(out)
print(f"assembled {len(out.splitlines())} lines -> {plan}")


# ---------------------------------------------------------------- per-page files

# page prompts: pages 1-2 live in the head, 3-48 in the fragments
prompts = split_sections(head, r"^## PAGE (\d+) — ")
for source in prompt_sources:
    prompts.update(split_sections(source, r"^## PAGE (\d+) — "))

# sections 1-4 plus the section 5 intro: everything in the head before page 1
law = head.split("\n## PAGE 1 — ", 1)[0].rstrip("\n").rstrip("-").rstrip("\n")

# section 6 without the page-1/2 appendices, which are per-page content
sec6_law = sec6.split("\n## Page 1 — appendix", 1)[0].rstrip("\n").rstrip("-").rstrip("\n")

# appendices: pages 1-2 live in section-6-head, 3-48 in the fragments
appendices = split_sections(sec6, r"^## Page (\d+) — appendix")
for source in appendix_sources:
    appendices.update(split_sections(source, r"^## Page (\d+) — appendix"))

missing = sorted(set(prompts) ^ set(appendices))
assert not missing, f"prompt/appendix mismatch for pages {missing}"
assert sorted(intents) == list(range(33, 50)), "intent source must contain Pages 33-49"

plan_dir.mkdir(parents=True, exist_ok=True)
for stale in plan_dir.glob("page-*.md"):
    stale.unlink()

banner = (
    "> **This is the whole plan for this page.** It carries the same sections 1-4,\n"
    "> the same section 6 briefs and the same sections 7-10 as\n"
    "> `12-PRODUCTION-PLAN.md`, plus this page's prompt and this page's appendix\n"
    "> and nothing else. Do not open the master plan — it is the identical law for\n"
    "> forty-nine pages at once, and loading it is what the run's token cost was.\n"
    "> If you need a neighbouring page, open that page's file."
)

for n in sorted(prompts):
    body = SEP.join([
        f"# PAGE {n} — production plan",
        banner,
        law,
        prompts[n],
        sec6_law,
        appendices[n],
        sections_7_10,
    ]) + "\n"
    (plan_dir / f"page-{n:02d}.md").write_text(body)

# ---------------------------------------------------------------- intent-first role packets
# These are the only production inputs opened by fresh builders and critics.
# Builder and critic transport is deliberately separated: the critic never
# receives the generation prompt or builder audit.
script_text = (root / "08-FULL-SCRIPT.md").read_text()
script_blocks = {}
script_hits = list(re.finditer(r"^## PAGE (\d+) · ", script_text, flags=re.M))
for i, m in enumerate(script_hits):
    end = script_hits[i + 1].start() if i + 1 < len(script_hits) else len(script_text)
    script_blocks[int(m.group(1))] = script_text[m.start():end].strip()

run_dir.mkdir(parents=True, exist_ok=True)
for stale in run_dir.glob("page-*-builder.md"):
    stale.unlink()
for stale in run_dir.glob("page-*-critic.md"):
    stale.unlink()
for stale in run_dir.glob("page-*-critic-card.md"):
    stale.unlink()

builder_contract = """## Fresh zero-history builder contract

Open only this packet and the explicitly listed local image inputs. Do not open
the master plan, critic card, another page plan, another candidate, or any prior
role task. Never use a rejected candidate as an image input.
Use the built-in Codex in-app image generation path billed to the ChatGPT
subscription. Do not use an API key, bundled image CLI, or API fallback.
The exact script strings, page intent, reference manifest, and story facts are
locked. Never edit 07-PAGE-CONTRACT.md or 08-FULL-SCRIPT.md.

Generate exactly one completed candidate. Your audit reports whether the
reader-facing intent appears to land; it is not a prompt-compliance verdict and
never gates submission. Submit every readable, correctly sized, non-corrupt
candidate to the independent critic. Regenerate before criticism only for wrong
canvas, corrupt/truncated output, or gross focal anatomical breakage; preserve
the failed evidence and report it.
"""

generation_frame = """## Shared generation frame

Create one finished flattened canonical-production graphic-novel page at
exactly **1024 × 1536, 2:3 portrait, RGB PNG**. It is not a prototype, proof
sheet, component, mockup, or spread.

Use the established **Velvet Cinema** register: layered matte gouache and opaque
watercolor over sparse charcoal/ink construction, broad visible brushwork,
bold shadow masses, tactile period materials, and selective hard edges at the
story focus. Avoid smooth prestige-oil realism, glossy concept-art surfaces,
airbrushed skin, engraved cross-hatching, and children's-book softness.

All required lettering is baked into the page. Render every supplied string
exactly once, in the stated order and ownership, with comfortable mixed-case
transcription from a 600 × 900 reduction. Do not invent readable text. Numeric
panel shares, coordinates, and lettering sizes are composition guidance, never
reasons to sacrifice the page's reader event.

Use each approved image according to its filename: character sheets bind named
identity, set sheets bind architecture/palette, the objects sheet binds only
consequential object design, and `pages/page-NN.png` binds immediate continuity
from the promoted predecessor. Preserve named-character identity and
consequential continuity; do not copy a rejected composition.
"""

critic_contract = """## Fresh zero-history blind critic contract

You are a reader-facing release gate, not a defect collector. You are read-only:
never edit, regenerate, promote, or propose generation-prompt wording. Never
open or request the generation prompt, builder packet, builder audit, prior
candidate, prior critic report, reference manifest, master plan, or another
page's packet.

Stage 1: open only the neutral candidate and proofs. From the 600 × 900 proof,
record what happens, who owns the page, what changes, and the exact visible text
with speaker/source attribution.

Stage 2: only after that blind read, open the separate critic-card packet named
below. Apply only its exact script, page intent, numbered criteria, and
materiality threshold.

A visible flaw blocks only when it materially harms the reader event, exact
text/attribution, named identity, consequential continuity/object state, focal
generation integrity, or dominant dramatic relationship. Minor background,
cosmetic, tiny-prop, exact-geometry, hue, or prompt-fidelity issues do not
justify replacing an otherwise successful full page.

For `REVISE`, every finding must cite one numbered criterion and state the
visible observation, material reader harm, and why that harm is substantial
enough to risk a complete redraw. If that justification cannot be made
concretely, return `APPROVED`. Omit praise, suggestions, optional polish, and
minor observations.
"""

for n in range(33, 50):
    if n not in prompts or n not in appendices or n not in script_blocks or n not in intents:
        raise AssertionError(f"cannot emit role packets for page {n}")
    page_prompt = prompts[n]
    appendix = appendices[n]
    script_page = script_blocks[n]
    intent = intents[n]
    builder = "\n\n".join([
        f"# PAGE {n} — builder packet",
        builder_contract,
        generation_frame,
        f"## Page intent\n\n{intent}",
        f"## Builder-only page prompt\n\n{page_prompt}",
        f"""## Version and revision mode

The orchestrator supplies the exact candidate version and one mode:

- `BASE`: use the shared frame and builder-only prompt as issued.
- `TARGETED`: open only the most recent issued prompt and latest validated
  critic report paths supplied by the orchestrator. Change the prompt only for
  the cited material criteria and preserve the report's successful reader
  facts. Do not add unrelated improvements.
- `FULL_PROMPT_RESET`: do not open any earlier issued prompt or rejected image.
  Rewrite the complete generation prompt and composition strategy from this
  packet plus the compact validated findings supplied by the orchestrator.
  Preserve exact strings, intent, story facts, and this reference manifest.

Write the exact complete prompt sent to image generation as the issued prompt.
Do not edit this base packet, the intent, or critic material.""",
        f"""## Issued paths

- Candidate: `qa/production/page-{n:02d}/candidates/page-{n:02d}-vK.png`
- Prompt: `qa/production/page-{n:02d}/prompts/page-{n:02d}-vK.md`
- Audit: `qa/production/page-{n:02d}/audits/page-{n:02d}-vK.md`
- Proofs: `qa/production/page-{n:02d}/proofs/page-{n:02d}-vK-600x900.png` and `qa/production/page-{n:02d}/proofs/page-{n:02d}-vK-768x1152.png`

The audit stays under 180 words and uses exactly:

`## Intent read` — what happens and who owns the page from the 600 × 900 proof.

`## Exact text check` — exact transcription or concise discrepancies.

`## Technical facts` — canvas/mode and obvious focal integrity issues.

`## Submission` — `SUBMITTED TO INDEPENDENT CRITIC`.

Return only the five output paths, candidate dimensions/mode, and file hashes.
Do not approve, promote, or write to `pages/`.""",
    ])
    critic = "\n\n".join([
        f"# PAGE {n} — blind critic entrypoint",
        critic_contract,
        f"""## Neutral inputs and staged authority

Stage 1 images:

- `qa/_review/page-{n:02d}/current/candidate.png`
- `qa/_review/page-{n:02d}/current/desktop-600x900.png`
- `qa/_review/page-{n:02d}/current/tablet-768x1152.png`

Stage 2, only after the blind read:

- `qa/_run/page-{n:02d}-critic-card.md`

Write the report to the neutral path
`qa/_review/page-{n:02d}/current/critic-report.md`. The orchestrator archives
it after you exit, so you receive no version history.""",
        """## Report schema

Approval:

```text
VERDICT: APPROVED

## Blind read
[What happens, who owns the page, and what changes.]

## Visible text
[Exact transcription with attribution, or NONE.]

## Findings
NONE
```

Revision:

```text
VERDICT: REVISE

## Blind read
[What happens, who owns the page, and what changes.]

## Visible text
[Exact transcription with attribution, or NONE.]

## Findings

### Finding C2
- Observation: [visible defect]
- Material reader harm: [how it prevents the scripted intent from landing]
- Redraw justification: [why the harm is substantial enough to risk replacing the complete page]
```

Use only criterion numbers present in the critic card. After saving the report,
return only `APPROVED` or `REVISE`.""",
    ])
    critic_card = "\n\n".join([
        f"# PAGE {n} — exact script, intent, and critic card",
        "Open this file only after completing the blind image read. Numeric panel shares are builder construction guidance, not critic measurements.",
        f"## Page intent\n\n{intent}",
        f"## Exact owner-controlled script\n\n{script_page}",
        """## Materiality threshold

The critic is a release gate, not a defect collector. A visible issue is
blocking only when it materially harms the reader event, exact text or
attribution, named/focal identity, consequential continuity/object state, focal
generation integrity, or dominant dramatic relationship. Every correction
replaces the complete page. Minor background, cosmetic, tiny-prop, geometry,
color, texture, and prompt-fidelity observations are nonblocking. Omit them.

Each numbered criterion is also its stable retry signature. Cite it only when
the reader harm and redraw justification are concrete.""",
        f"## Numbered blocking criteria\n\n{appendix}",
    ])
    (run_dir / f"page-{n:02d}-builder.md").write_text(builder + "\n")
    (run_dir / f"page-{n:02d}-critic.md").write_text(critic + "\n")
    (run_dir / f"page-{n:02d}-critic-card.md").write_text(critic_card + "\n")

for stale in run_dir.glob("batch-*-script.md"):
    stale.unlink()
for start, end in ((31, 40), (41, 49)):
    batch_script = "\n\n---\n\n".join(script_blocks[n] for n in range(start, end + 1))
    (run_dir / f"batch-{start:02d}-{end:02d}-script.md").write_text(
        f"# Exact owner-controlled script — Pages {start}-{end}\n\n"
        "Read only after the uninterrupted blind sequence read.\n\n"
        + batch_script
        + "\n"
    )

sizes = [len((plan_dir / f"page-{n:02d}.md").read_text()) for n in prompts]
print(f"wrote {len(prompts)} per-page plans -> {plan_dir}")
print(f"wrote {17} intent-first builder/critic/card packet sets -> {run_dir}")
print(f"wrote 2 milestone script packets -> {run_dir}")
print(f"  master {len(out):,} chars | per-page avg {sum(sizes)//len(sizes):,} "
      f"max {max(sizes):,} | ~{len(out)//(sum(sizes)//len(sizes))}x smaller")
