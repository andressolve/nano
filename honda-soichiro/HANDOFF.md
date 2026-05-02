# Honda Soichiro — Session Handoff

**Source of truth across restarts.** Read this top-to-bottom before resuming. Update checkboxes and notes as work proceeds.

---

## ✅ SHIPPED 2026-05-02

Vol 1 ("The Boy Who Chased Engines · Soichiro Honda · Part One") is complete: 10 refs, cover + 24 pages, 5-question quiz, dark-themed reader at `index.html`, landing card added to repo root `index.html`. Total image cost ~$7.50 on gpt-image-2 standard. See `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/project_honda_retrospective.md` for the full retrospective.

The historical pre-ship handoff (planning state, prototype spec, environment check) is preserved below for context.

---

## (HISTORICAL) ⏭ NEXT SESSION — START HERE

**Status as of 2026-05-02:** Planning complete. Brief and full 24-page script written. NO image generation has happened yet. Codex's `honda/` folder is the research archive; this `honda-soichiro/` folder is the production project.

### Step 0 — Verify environment (do FIRST, before any image calls)

1. Check Gemini MCP availability. Try a `ToolSearch` query for `gemini`. The active MCP for this project is the custom `gemini-pro-thin` (built 2026-05-02, removes the upstream 2000-char prompt cap). Tool names: `mcp__gemini-pro-thin__{generate_image,edit_image,compose_images}`. If those don't appear, ensure the project MCP is registered and Claude Code has been restarted. The upstream `gemini-nanobanana-mcp` is no longer the default. See `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/reference_gemini_pro_thin_mcp.md`.
2. Verify endpoint is Pro for the nano project:
   ```
   grep -A2 GEMINI_IMAGE_ENDPOINT ~/.claude.json | head -10
   ```
   The `/Users/andresrodriguez/Documents/nano` block must show `gemini-3-pro-image-preview:generateContent`. If it shows Flash, do NOT generate refs on Flash — the script is calibrated to Pro's T5 ceiling. Stop and ask user to switch.
3. If a fresh smoke is desired, call `mcp__gemini-pro-thin__generate_image` with a >2000-char prompt and save under `output/imagegen/smoke/`. The 2026-05-02 baseline smoke is at `output/imagegen/smoke/gemini-pro-thin-smoke-2026-05-02.png`.

### Step 1 — Generate 6 character refs (sequential, verify each)

All on Pro. Save to `honda-soichiro/refs/`. Read the saved PNG after each one, verify against the spec, then proceed. If a ref drifts toward children's-book aesthetic or wrong era, regenerate before moving on — do NOT generate downstream refs from a drifted upstream one.

| # | File | Subject | Spec source |
|---|------|---------|-------------|
| 1 | `refs/01-honda-boy.png` | Soichiro age 8, 1914, Komyo Village | Prompt drafted (see "Boy Honda prompt" below) |
| 2 | `refs/02-honda-teen.png` | Soichiro age 17, 1923, Tokyo apprentice | Adapt from `honda/reference-plan.md` §2 |
| 3 | `refs/03-honda-young-shop.png` | Soichiro age 22-30, late 1920s-1936, Hamamatsu shop owner / piston-ring inventor | Adapt from `honda/reference-plan.md` §3 |
| 4 | `refs/04-honda-postwar.png` | Soichiro age 39-42, 1946-1949, postwar founder | Adapt from `honda/reference-plan.md` §4 |
| 5 | `refs/05-honda-middle-aged.png` | Soichiro age 42-55, 1949-1963, engineer-founder | Adapt from `honda/reference-plan.md` §5 |
| 6 | `refs/06-fujisawa.png` | Takeo Fujisawa age 38-52, 1949-1963 | Adapt from `honda/reference-plan.md` §6 |

**Boy Honda prompt** (drafted on 2026-05-02, ready to use):

```
Character reference sheet, 3:2 landscape, 1536x1024, serious mature historical graphic-novel realism. NOT a children's book. NOT cute, NOT mascot proportions, NOT oversized eyes. Realistic child anatomy.

SUBJECT: Soichiro Honda as a Japanese rural boy, age 8, year 1914, Komyo Village in Shizuoka Prefecture. Lean small build, sun-browned skin from outdoor village life. Short dark hair, slightly unkempt, cut by his mother. Intense curious eyes — focused, alert, the eyes of a child who already watches machines more closely than he watches faces. Slightly serious, not smiling. Practical rural early-20th-century Japanese work clothing: a simple dark indigo cotton kimono-style shirt tucked into loose trousers, bare feet or simple straw sandals. A small smudge of forge soot on one cheek.

LAYOUT: Three views arranged across the landscape sheet, evenly spaced.
- LEFT: Full-body neutral standing pose, three-quarter angle, hands at his sides, one slightly clenched.
- CENTER: Full-body running/chasing pose, leaning forward, both arms swinging, one foot planted and one mid-stride. The pose of a boy chasing something he wants to catch.
- RIGHT: Head-and-shoulders close-up, three-quarter view, looking off toward something out of frame with intense focused curiosity.

BACKGROUND: Soft warm off-white sheet background, very subtle workshop tones (forge orange hint, indigo). No story scenery. No props beyond clothing. No other characters.

PALETTE: forge orange, bicycle black, rural dust, indigo work clothes, sun-browned skin tones.

NO TEXT anywhere on the sheet. No labels, no name tags, no watermarks, no signs, no fake Japanese characters. The sheet itself is purely visual reference.
```

For refs 2-6: write similar prompts following the same structure (3-view layout, no text, off-white sheet bg, era-specific clothing, "NOT a children's book" framing). Use `honda/reference-plan.md` for canonical age phase descriptions, then add: 3-view layout language, the "NO TEXT" clause, and 2000-char check before calling.

### Step 2 — Generate 4 machine/object refs

All on Pro for consistency. Save to `honda-soichiro/refs/`. Read each, verify era plausibility.

| # | File | Subject |
|---|------|---------|
| 7 | `refs/07-early-automobile.png` | Primitive open-bodied early 1910s automobile on a rural Japanese road |
| 8 | `refs/08-piston-and-ring.png` | Educational object plate: piston, piston ring, and cylinder cutaway, no labels |
| 9 | `refs/09-dream-d-type.png` | 1949 Dream D-Type motorcycle, maroon, late-1940s Japan |
| 10 | `refs/10-super-cub.png` | 1958 Super Cub C100, step-through frame, leg shield, cream and red |

### Step 3 — Generate 3 prototype pages

All on Pro. Use `compose_images` (multi-ref) since each page features 1-2 locked characters.

| Page | File | Refs to feed | Density | Goal |
|------|------|--------------|---------|------|
| 1 | `pages/page-01.png` | 01-honda-boy + 07-early-automobile | T4 | Validate landscape format + cinematic page + native lettering |
| 7 | `pages/page-07.png` | 03-honda-young-shop + 08-piston-and-ring | T5 | Validate dense failure-and-study page (3 captions + 3 bubbles, ~135 words) |
| 12 | `pages/page-12.png` | 05-honda-middle-aged + 06-fujisawa | T5 | Validate two-character partnership page (caption + 4 bubbles + caption, ~115 words) |

Page prompts: derived from `04-SCRIPT.md`. Watch the 2000-char prompt limit — distill the script's panel description + lettering placement + exact text strings into a tight prose prompt. Do NOT use the "lock list" format (`[1]`, `[2]`...) — that backfired on the T5 test.

### Step 4 — Decide

After 3 prototypes:
- All three ship-ready → continue to remaining 21 pages + cover + reader.
- Text rendering issues at T5 → diagnose: was it composition, ref drift, or pure text rendering? Adjust prompt format and re-run the affected prototype before continuing.
- Style inconsistency between the three → tighten ref descriptions in subsequent page prompts.

### Step 5+ (later, after prototypes pass)

- Generate cover.
- Generate remaining 21 pages in script order, choosing model per density tier.
- Build `index.html` reader (dark theme, page-flipping, arrow keys, quiz at end). Match `pythagoras-vol1/index.html` structure.
- Add card to repo root `index.html` landing page.
- Update MEMORY.md inventory + retrospective notes.

---

## What's already written

| File | Purpose |
|------|---------|
| `00-PROJECT-BRIEF.md` | Diagnosis of Codex's drops, what we keep from `honda/`, what we change, budget estimate (~$5 total) |
| `04-SCRIPT.md` | Full 24-page script with T3-T5 tags per page, model recommendations, exact image text, lettering placement, two experimental page formats called out (Page 14 primary-source letter, Page 19 annotated-breakthrough callouts) |
| `HANDOFF.md` | This file |

**Not yet written** (write only if needed during production; the brief and script may be enough):
- `01-STYLE-GUIDE.md` — pointer to `honda/style-guide.md` is sufficient
- `02-CHARACTERS.md` — pointer to `honda/reference-plan.md` is sufficient
- `03-SETTINGS.md` — same; settings detail lives in script panel descriptions
- `05-PRODUCTION-LOG.md` — start when generation begins

## What's already decided (from user 2026-05-02)

- **Format:** 3:2 landscape, 1536×1024 — kept from Codex.
- **Page count:** 24 — trimmed from Codex's 34. User said "trust your judgement, but don't cram; we'll see prototypes and go from there." So if a prototype reveals a page is overstuffed, splitting is on the table.
- **Quiz:** yes, 5 questions, drafted in script.
- **Title:** "The Boy Who Chased Engines · Soichiro Honda · Part One" — kept.

## Codex pipeline collision warning

User confirmed Codex was also running on the Gemini MCP, which is what knocked the tool off this session on 2026-05-02. User said they'd tell Codex to stop. **Before generating, confirm Gemini MCP is available** (try `ToolSearch nanobanana`). If unavailable mid-run, fall back to `mcp__openai-image-2__generate_image` rather than aborting — gpt-image-2 is the validated alternative (Newton Vol 1 ran entirely on it).

## Why this project exists / standard to honor

User's standing complaint about Codex's prototypes: **"no terse crap. readable. insightful. engaging. the reader should not be filling in blanks/gaps."**

This is the same standard as MEMORY.md's "CRITICAL FRAMING RULE": write so a first-time reader who has never heard of Honda can follow on first read. No info-withholding. No jigsaw-puzzle reading. The script's T4-T5 density per page is the operationalization of this standard. If you find yourself shortening captions to fit a prompt limit, push composition out, not text.

## Cost ledger (planned)

| Phase | Items | Est. cost |
|-------|-------|-----------|
| Refs | 6 character + 4 object on Pro | ~$1.30 |
| Prototypes | 3 hero pages on Pro | ~$0.40 |
| Production | Cover + 21 pages, mix Pro/Flash | ~$3.00 |
| Repairs | Buffer for re-rolls | ~$0.50 |
| **Total** | | **~$5.20** |
