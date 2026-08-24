# Dialogue studio rules

This directory is a self-contained kit for long-form, dialogue-driven graphic
novels. Do not depend on wider repository history.

For a new work launched from this directory, read `NEW-WORK.md`, `AUDIENCE.md`,
`ADAPTATION.md`, and `PREPRODUCTION.md`, initialize it under
`works/<project-slug>/`, and conduct only bounded research and adaptation.
Research creates understanding, not
narrative obligations. The target is ultra-premium storytelling for the owner-
named audience—not academic completeness, default fidelity, prestige, or
illustrated plot summary. The owner-facing greenlight proposal must include how
the story will be told and its graphical direction. No reference or page
generation opens before explicit story approval and a clean adaptation-
readiness check. Page production remains closed until casting/references,
page packets, context boundaries, and the second owner production approval pass
the separate pre-production gate.

During adaptation, authority is owner purpose and decisions; locked audience
promise, adaptation, architecture, graphical direction, script, and contract;
declared protected claims; then research and sources as evidence. A source
departure is not a defect unless it breaks an explicit protected claim or
creates cultural, ethical, or story harm.

During production, authority is owner-approved script, page contract, and
references; `PLAYBOOK.md`; `PROMPTING.md`; current page intent, builder prompt,
and numbered card; then case studies as historical evidence. Never edit
owner-controlled story documents to make generation easier.

Each project has `NEW-WORK.md` for adaptation and pre-production, one active
`SESSION-START.md` for production, and one dynamic `HANDOFF.md`. Keep builder
prompts, audits, and critic packets separate. The builder submits every
technically valid candidate; the blind critic judges reader harm, not prompt or
source compliance. Only the orchestrator promotes. One page is in flight; no
v5 after a v4 revision.

Use subscription-backed Codex in-app image generation only; no API-key or other
billing fallback without owner approval. Do not make throwaway prototype story
pages: validate the first real risky page and promote that candidate if
approved. Lettering is baked into the page image; never HTML/SVG overlay,
crop-patch, reletter, or composite. Exact comfortable transcription at 600×900
is the readability test; numeric type size is not a gate. After three critic
failures, propose a split before a sixth panel, while respecting resistant-
defect and v4 owner holds.

`check_adaptation.py` opens only bounded reference preparation.
`check_preproduction.py` is the sole mechanical authority that may open story
page production. The gates are non-transitive.
