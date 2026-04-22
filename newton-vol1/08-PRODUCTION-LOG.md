# The Invisible Forces — Production Log

## Run 1: First-Wave Character References

### Date
2026-04-22

### Goal
Generate the first-wave character references defined in `05-PRODUCTION-PLAN.md`.

### Intended Model
`gpt-image-2`

### Actual Model Used
`gpt-image-1.5`

### Reason For Fallback
The API account returned a `403 PermissionDeniedError` for `gpt-image-2`, indicating the organization must be verified before that model can be used. Rather than stop the workflow, first-wave references were generated with `gpt-image-1.5` as provisional production assets.

### Generated References
- `ref-newton-young-scholar.png`
- `ref-newton-mature-professor.png`
- `ref-newton-child.png`
- `ref-newton-schoolboy.png`
- `ref-halley.png`
- `ref-hannah.png`
- `ref-grandmother-margery.png`

### Saved Locations
- Working outputs: `output/imagegen/newton-vol1/refs/`
- Promoted project refs: `newton-vol1/refs/`

### Initial Assessment
- **Young Scholar:** strong; good candidate as primary Newton look
- **Mature Professor:** strong; age progression reads clearly from Young Scholar
- **Child:** usable but slightly soft; watch for drift toward cuteness in story pages
- **Schoolboy:** usable; good bridge between child and scholar
- **Halley:** strong; good energy contrast with Newton
- **Hannah:** solid and restrained
- **Grandmother:** solid and period-plausible

### Follow-Up Implications
- These refs are sufficient to begin prototype-page work.
- If `gpt-image-2` access becomes available, the first two refs worth regenerating first are:
  1. `ref-newton-young-scholar.png`
  2. `ref-newton-child.png`
- For the current workflow, treat the child reference as the most likely one to need tightening during page work.

## Run 2: `gpt-image-2` Upgrade Pass

### Date
2026-04-22

### Goal
Regenerate the three highest-leverage Newton references after organization verification propagated and `gpt-image-2` became available.

### Regenerated On `gpt-image-2`
- `ref-newton-young-scholar-gpt2.png`
- `ref-newton-child-gpt2.png`
- `ref-newton-mature-professor-gpt2.png`

### Promotion Decision
The `gpt-image-2` versions replaced the project refs for:
- `ref-newton-young-scholar.png`
- `ref-newton-child.png`
- `ref-newton-mature-professor.png`

### Assessment
- **Young Scholar:** materially stronger than the `gpt-image-1.5` version; better face structure and stronger primary Newton look
- **Child:** stronger realism and less storybook softness, but still needs age vigilance during page generation so he does not drift too old
- **Mature Professor:** stronger and more severe; better match for late Book One tone

### Current Best Reference Set
- Newton Young Scholar — `gpt-image-2`
- Newton Child — `gpt-image-2`
- Newton Mature Professor — `gpt-image-2`
- Newton Schoolboy — `gpt-image-1.5` for now
- Halley — `gpt-image-1.5` for now
- Hannah — `gpt-image-1.5` for now
- Grandmother — `gpt-image-1.5` for now

### Implication For Next Phase
Prototype-page generation should now use the upgraded `gpt-image-2` Newton refs.

## Run 3: Prototype Page Pass 1

### Date
2026-04-22

### Prototype Pages Generated
- `page-10-proto-v1.png`
- `page-11-proto-v1.png`
- `page-14-proto-v1.png`
- `page-15-proto-v1.png`
- `page-23-proto-v1.png`
- `page-15-proto-v2.png`
- `page-23-proto-v2.png`

### Summary
- Pages 10 and 11 are already viable.
- Page 14 is workable and does not force redesign.
- Page 15 needed one revision to remove worksheet aesthetics; v2 is the correct direction.
- Page 23 needed one revision to reduce cosmic spectacle; v2 is the current best version.

### Main Finding
The science-heavy Newton Book One pages are viable on `gpt-image-2` without forcing structural redesign.

## Run 4: Custom MCP Smoke Test (standard mode)

### Date
2026-04-22

### Goal
Validate that the custom `openai-image-2` MCP (at `~/.claude/mcp-servers/openai-image-2/`) can produce a page-15 result equivalent to the Codex-generated `page-15-proto-current.png` using **default standard mode only** (no thinking), so the hybrid workflow does not require thinking-mode spend.

### Procedure
Edit call against `ref-newton-young-scholar.png` with the page-15 prototype prompt from `09-PROTOTYPE-PROMPTS.md`, reinforced with an explicit "two Earths at two different distances" clause. Size `1024x1536`, quality `high`, thinking unset.

### Output
`output/imagegen/smoke/page-15-mcp-standard-test.png`

### Comparison
- NB2 `page-15-proto-nb2.png`: second Earth missing, comparison broken
- Codex `page-15-proto-current.png`: strong, clean single diagram
- MCP standard `page-15-mcp-standard-test.png`: Newton vignettes on top panel, full near/far comparison on manuscript below — bold solid arrow for near pull, dashed faint arrow for far pull; weakening is visually explicit

### Result
**Standard mode matches (or slightly improves on) the Codex output.** Hybrid workflow validated — geometry-critical Newton pages can run on `gpt-image-2` standard at ~$0.21/page without opting in to thinking.

### Cost
1 call × gpt-image-2 standard high ≈ $0.21.

## Run 5: Reference Aesthetic Unification Pass

### Date
2026-04-22

### Rationale
After reviewing the full ref set, the Newton refs (Child, Schoolboy, Young Scholar, Mature Professor) on `gpt-image-2` would visibly clash with Halley/Hannah/Grandmother on `gpt-image-1.5` on shared-page scenes (pages 2, 3, 20). Decision: commit the whole book to a single `gpt-image-2` pipeline. Also regenerate the child ref tighter/younger because the original read closer to age 9-10 than the intended 6-7.

### Generated
- `ref-halley-gpt2-v2.png` — on gpt-image-2, with strict no-text constraint after first attempts added typography overlays
- `ref-hannah-gpt2-v2.png` — same
- `ref-grandmother-margery-gpt2-v2.png` — same
- `ref-newton-child-gpt2-v2.png` — younger (age ~6-7), face continuity preserved with older Newton refs
- `ref-prism-apparatus.png` — object plate: close-up prism + full two-prism setup
- `ref-reflecting-telescope.png` — object plate: compact reflector with yoke mount, workshop context

### First-pass issue encountered
Initial v1 generations for Halley/Hannah/Margery used the "Full character reference sheet" phrasing and triggered in-image typography (names, bio blocks, sketched diagrams). These would leak into page generations. Regenerated with explicit `ABSOLUTE NO-TEXT RULE` language — clean on the retry.

### Promoted to `newton-vol1/refs/`
- `ref-halley.png` (replaces gpt-1.5; old archived as `ref-halley-gpt15.png`)
- `ref-hannah.png` (replaces gpt-1.5; old archived as `ref-hannah-gpt15.png`)
- `ref-grandmother-margery.png` (replaces gpt-1.5; old archived as `ref-grandmother-margery-gpt15.png`)
- `ref-newton-child.png` (replaces older gpt-2 version; old archived as `ref-newton-child-v1.png`)
- `ref-prism-apparatus.png` (new)
- `ref-reflecting-telescope.png` (new)

### Still on gpt-image-1.5
- `ref-newton-schoolboy.png` — only remaining gpt-1.5 ref; appears on pages 4-6. Consider regenerating on gpt-image-2 before starting the main sequence if these pages share frames with other characters.

### Cost
9 calls × gpt-image-2 standard high ≈ $1.89.

### Hybrid workflow retired
Mixed NB2 + gpt-image-2 plan is now abandoned in favor of a single gpt-image-2 pipeline across all 24 pages. Projected book cost: ~24 × $0.21 ≈ $5.04 (plus refs already spent).

## Run 6: Full Production Pass

### Date
2026-04-22

### Scope
All 24 pages generated on gpt-image-2 standard mode (no thinking), edited from the unified gpt-image-2 reference set. Captions baked into each image.

### Pages
- Page 1 (cover) — edit from Young Scholar; large serif title "THE INVISIBLE FORCES" / "ISAAC NEWTON, BOOK ONE" rendered cleanly
- Pages 2-6 — childhood and farm refusal (Child, Hannah, Grandmother, Schoolboy refs)
- Pages 7-9 — Cambridge, Waste Book, plague withdrawal
- Pages 10-11 — prism beam + second-prism proof
- Pages 12-15 — fluxions, orchard question, moon-falling, inverse-square
- Pages 16-19 — private years, reflecting telescope, optics recoil, problem returns
- Page 20 — Halley arrives; two speech bubbles render cleanly ("What curve?" / "An ellipse. I have calculated it.")
- Pages 21-22 — De Motu and Principia writing/printing
- Page 23 — climax: "One law for the apple and the moon" with unified geometry rising from the Principia; Latin book title renders
- Page 24 — coda: Newton at window, closed Principia, quiet orchard/moon/prism echoes

### Caption render quality
All 24 pages produced correctly-spelled caption text on first pass. No re-rolls required for typography.

### Character continuity
Strong across all pages. The age ladder (Child → Schoolboy → Young Scholar → Mature Professor) reads as one person. Halley on page 20 reads as clearly distinct from Newton. Hannah and Grandmother on pages 3, 6 period-correct and restrained.

### Promoted
All 24 pages copied to `newton-vol1/pages/page-01.png` through `page-24.png`. Source drafts retained in `output/imagegen/newton-vol1/pages-01-05/` as `-v1` siblings.

### Cost
24 pages × gpt-image-2 standard high ≈ $5.04.
Total project image cost (refs + smoke + all pages) ≈ $7.35.

### Status
The Invisible Forces — Isaac Newton, Book One is image-complete. Pending: reader HTML + landing page card for `index.html`.
