# Salt and Stone — Life Two: The Youth

## Overview

**Title:** Salt and Stone — Life Two: The Youth
**Subtitle:** A Graphic Novel in Three Lives
**Chapter:** Life Two — The Youth (age 14-15)
**Target Audience:** Francisco and Sebastian
**Image Generation Model:** Google Nano Banana Pro (Gemini 3 Pro Image) via MCP
**Pages:** Cover + 15 story pages + back cover (17 total images)

---

## What Happened in Life One

Nikos was a 9-year-old Greek boy on a small Aegean island. His father Alexios was a shipbuilder. A Persian raid destroyed the island. Alexios put Nikos on a trade ship to save him; the ship was wrecked in a storm. Nikos washed ashore near Sidon, a Phoenician city allied with Persia. He was taken in by Hasdrubal, a Phoenician shipwright. He discovered that Hasdrubal builds ships for the same Persian navy that destroyed his home. He chose to stay. He rebuilt his life.

Visual throughlines from Life One that MUST carry into Life Two:
- **Shell necklace** on leather cord (from his mother — never removed)
- **Scar on left palm** (from chisel slip as a child)
- **The carved wooden ship** (Greek-style, pocket-sized — made by his father)

---

## Life Two Story Summary

Five years have passed. Nikos is now 14-15, living in Sidon, working in Hasdrubal's shipyard. He is Phoenician in everything but blood. Then Xerxes calls the fleet — Phoenician ships are conscripted for the invasion of Greece. Nikos is conscripted as crew. He finds himself fighting against Greeks at the Battle of Salamis. His ship is rammed. He's in the water — again. Pulled from the sea by Athenian sailors, he survives because he speaks Greek. He ends up in Athens during its post-war golden age. A man who has fought on both sides of the defining war of his age.

**Theme:** *There are no clean sides. Everyone believes they're right.*

---

## Project Structure

| File | Purpose |
|------|---------|
| `00-PROJECT-BRIEF.md` | This file — overview and workflow |
| `01-STYLE-GUIDE.md` | Updated art style block with Life Two palette |
| `02-CHARACTERS.md` | Character lock blocks (LEAN) + reference sheet prompts |
| `03-SETTINGS.md` | Setting lock blocks for Life Two locations |
| `04-SCRIPT.md` | Full page-by-page script with panel breakdowns |

---

## CRITICAL: Prompt Length Rules

Life One had prompt-too-long errors. Life Two prompts are designed leaner. Follow these rules:

### Reference Images Do the Heavy Lifting
- The character lock blocks in `02-CHARACTERS.md` are SHORT (4-5 lines)
- Character consistency comes from **uploading the reference image**, not from long text descriptions
- Every page prompt MUST include: "featuring the same characters shown in the reference images"
- The reference image + that phrase = 80% of character locking

### Keep Prompts Tight
- 3-4 panels per page maximum
- Panel descriptions: 1-2 sentences each, no atmospheric padding
- Dialogue: under 15 words per bubble
- Caption text: under 20 words per caption box
- NO redundant description of things the style block already covers

### What NOT to Paste Inline
- Do NOT paste the full style guide into each prompt — just the 3-line style block
- Do NOT paste setting descriptions into prompts — describe the scene directly
- Do NOT repeat character details that are visible in the reference image

---

## Production Workflow

### Phase 1: Reference Generation

1. Read `01-STYLE-GUIDE.md` — internalize the style block
2. Read `02-CHARACTERS.md` — each character has a lean lock block + reference prompt
3. **If you have the Life One Nikos (boy) reference image, upload it when generating the Life Two Nikos (youth) reference** — this helps maintain facial continuity across age
4. Generate reference sheets in this order:
   - Nikos (Youth, age 14-15) — **most important, generate first**
   - Hasdrubal (same as Life One but upload Life One ref if available)
   - Captain Mazaeus (new character)
   - Deon (new character)
5. Save each to `~/nano/salt-and-stone-life-two/refs/`
6. Review each. Regenerate if face is unclear or signature marks missing.

### Phase 2: Page Generation

7. Read `04-SCRIPT.md`
8. Generate pages sequentially (Cover → Page 1 → Page 2 → ... → Back Cover)
9. For EVERY page:
   - **Upload the relevant character reference image(s)** as input
   - Paste the 3-line style block from `01-STYLE-GUIDE.md`
   - Paste the lean character lock block from `02-CHARACTERS.md`
   - Include: "featuring the same characters shown in the reference images"
   - Use the exact prompt from `04-SCRIPT.md`
10. Save pages to `~/nano/salt-and-stone-life-two/pages/` (page-00-cover.png, page-01.png, etc.)
11. If generation drifts from reference, regenerate before moving on.

### Anti-Drift Rules

If any page trends toward soft/children's book aesthetics, add:
```
STYLE REINFORCEMENT: This is NOT a children's book. Render in serious, mature graphic novel style with realistic proportions and cinematic composition.
```

Life Two has MORE battle content than Life One. Watch for:
- Salamis battle pages going "cartoon violence" instead of grounded, visceral realism
- Nikos at 14-15 being rendered as 10-11 (he should look like a young man, not a boy)
- Athens pages going "bright tourist postcard" instead of gritty, crowded, real

---

## File Dependencies

Life Two can be generated standalone, but if Life One reference images are available:
- Upload Life One Nikos (boy) ref from `~/nano/salt-and-stone/refs/` when generating Life Two Nikos (youth) ref
- Upload Life One Hasdrubal ref from `~/nano/salt-and-stone/refs/` when generating Life Two Hasdrubal ref
- This maintains facial continuity across the age jump
