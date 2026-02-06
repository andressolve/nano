# Salt and Stone — Graphic Novel Project Brief

## Overview

**Title:** Salt and Stone
**Subtitle:** A Graphic Novel in Three Lives
**Chapter:** Life One — The Boy
**Target Audience:** Francisco (9) and Sebastian (7) — advanced readers who enjoy historically grounded action stories (Troy, Thermopylae, Teutoburg Forest)
**Image Generation Model:** Google Nano Banana Pro (Gemini 3 Pro Image) via MCP
**Pages:** Cover + 15 story pages + back cover (17 total images)

---

## Project Structure

This folder contains everything needed to produce Chapter 1 of "Salt and Stone":

| File | Purpose |
|------|---------|
| `00-PROJECT-BRIEF.md` | This file — overview and workflow |
| `01-STYLE-GUIDE.md` | Art style block, color palette, visual rules |
| `02-CHARACTERS.md` | Character lock blocks for all characters |
| `03-SETTINGS.md` | Setting lock blocks for recurring locations |
| `04-SCRIPT.md` | Full page-by-page script with panel breakdowns |

---

## Production Workflow

Follow this sequence exactly. Do not skip steps.

### Phase 1: Reference Generation

1. Read `01-STYLE-GUIDE.md` — internalize the style block
2. Read `02-CHARACTERS.md` — each character has a full lock block
3. **Generate character reference sheets FIRST, before any story pages**
   - Generate one reference sheet per character using the prompts in `02-CHARACTERS.md`
   - Each reference sheet = 4:3 landscape, two views (portrait + full body)
   - **Save each generated image to `refs/`**
   - Naming: `ref-nikos-boy.png`, `ref-father.png`, `ref-hasdrubal.png`, etc.
4. Review each reference for quality. Regenerate if:
   - Face is unclear or inconsistent between portrait and full body
   - Signature marks are not visible
   - Style doesn't match the style guide

### Phase 2: Page Generation

5. Read `04-SCRIPT.md` — the full page-by-page script
6. Generate pages **sequentially**, one at a time (Page 1, then Page 2, etc.)
7. For EVERY page generation:
   - **Upload the relevant character reference image(s)** as reference
   - **Paste the style block verbatim** from `01-STYLE-GUIDE.md`
   - **Paste the character lock block verbatim** from `02-CHARACTERS.md`
   - **Include the phrase:** "featuring the same character shown in the reference image"
   - Use the exact prompt from `04-SCRIPT.md`
8. Save each page to `pages/`
   - Naming: `page-00-cover.png`, `page-01.png`, `page-02.png`, etc.
9. After generating each page, verify:
   - Character face matches reference sheet
   - Colors match palette
   - Text is legible
   - Panel layout matches the script
   - Mood/atmosphere is correct

### Phase 3: Assembly

10. Once all pages are generated, collect all final outputs in `output/`

---

## Key Reminders

- **Character consistency is the #1 priority.** Always upload reference images.
- **Copy style and character blocks VERBATIM.** Do not paraphrase or abbreviate.
- **This is NOT a children's book.** The protagonist is 9 years old but the visual treatment is adult — serious, cinematic, realistic proportions, natural lighting. If any generation looks soft, cartoonish, rounded, "cute," or whimsical, regenerate immediately. AI image models drift toward children's book aesthetics when the subject is a child. Fight this actively.
- **Nano Banana Pro generates full multi-panel pages in one shot.** Do not break pages into individual panels unless a page fails repeatedly.
- **Keep dialogue under 15 words per speech bubble.**
- **Specify [No Text] explicitly for silent panels.**
- **All story pages use 2:3 vertical aspect ratio. Reference sheets use 4:3 landscape.**
- **If a generation fails or drifts, regenerate before moving to the next page.** Do not accumulate drift.
