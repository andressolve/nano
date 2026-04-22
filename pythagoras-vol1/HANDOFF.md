# Pythagoras Vol 1 — Session Handoff

**Last updated:** 2026-04-22 (afternoon session)
**Status:** ✅ Vol 1 shipped. Character refs regenerated on Nano Banana 2, all 18 pages generated, reader built, landing card added.

---

## Where we are in the workflow

1. ✅ All 10 planning markdown docs written (5 for Vol 1, 5 for Vol 2)
2. ✅ Character reference sheets regenerated on Nano Banana 2 (old NBPro versions kept as `.nbpro.png.bak`)
3. ✅ Cover + 17 pages generated on Nano Banana 2
4. ✅ `index.html` reader built (dark theme, page-flipping, end-of-volume interstitial, 5-question quiz)
5. ✅ Landing-page card added to `../index.html`
6. ⏸ **NEXT:** Vol 2 — refs (elder/Theano/Hippasus/Cylon), 22 pages, reader, card

## Character refs (in `refs/`)

| File | Subject | Status |
|------|---------|--------|
| `pythagoras-mature.png` | Age 40 — shared with Vol 2 (anchor ref) | ⚠️ Exists (Nano Banana Pro) — **regenerate on NB2** |
| `pythagoras-boy.png` | Age 10 — pages 1–3 | ⚠️ Exists (Nano Banana Pro) — **regenerate on NB2** |
| `pythagoras-young-man.png` | Age 20 — pages 4–10 | ⚠️ Exists (Nano Banana Pro) — **regenerate on NB2** |
| `babylonian-magus.png` | Magus — pages 8–10 | ⚠️ Exists (Nano Banana Pro) — **regenerate on NB2** |
| `pherecydes.png` | Optional (page 3 only) | Not made — prompt-only |
| `egyptian-priest.png` | Optional (page 6 only) | Not made — prompt-only |

**IMPORTANT — regenerate before page generation.** All four existing refs were produced on Nano Banana Pro (`gemini-3-pro-image-preview`) BEFORE the switch to Nano Banana 2 (`gemini-3.1-flash-image-preview`). To prevent aesthetic drift between refs and pages, regenerate all four on Nano Banana 2 as the first step of the next session, using the same prompts (see `02-CHARACTERS.md` for anchors). Keep the current files as backup until the NB2 versions are reviewed — e.g. `mv pythagoras-mature.png pythagoras-mature.nbpro.png.bak` before regenerating.

**Regeneration approach for the three Pythagoras ages:**
1. Generate `pythagoras-mature.png` first with `generate_image` (no ref needed — this is the anchor).
2. Generate `pythagoras-boy.png` with `edit_image` using the new NB2 mature ref as base, with the age-down prompt (see original prompt structure: child version of the same face, preserving thick brows / broad forehead / developing aquiline nose).
3. Generate `pythagoras-young-man.png` with `edit_image` using the new NB2 mature ref as base, with the age-20 prompt (sparse edged beard, NOT age 30+).
4. Generate `babylonian-magus.png` standalone with `generate_image`.

**Face lock for Pythagoras (all ages):** thick straight brows + broad high forehead + strong aquiline nose. Repeat in every page prompt. The boy and young-man refs are generated via `edit_image` using the mature ref as base, which preserves features well.

**Backup prompts reference:** original generation prompts (preserved for re-use on NB2) are captured in the git history of this session, but `02-CHARACTERS.md` has the prompt-anchor strings for each character. Use those anchors when writing the NB2 regeneration prompts.

## Image model in use

**Nano Banana 2** = `gemini-3.1-flash-image-preview`

- Project-scoped in `~/.claude.json` at `projects["/Users/andresrodriguez/Documents/nano"].mcpServers["gemini-nanobanana-mcp"].env.GEMINI_IMAGE_ENDPOINT`
- The MCP tool's *description text* still says "Gemini 2.5 Flash Image" — that's stale boilerplate in the npm package. Ignore it; the endpoint override is what matters.
- Switched from `gemini-3-pro-image-preview` (Nano Banana Pro) to `gemini-3.1-flash-image-preview` (Nano Banana 2) on 2026-04-22 for Pro-level quality at Flash speed.
- Config backup saved to `~/.claude.json.bak.20260422-060154` in case we need to revert.
- **The 4 character refs currently on disk were generated on Nano Banana Pro** (before the switch). They must be regenerated on NB2 before page generation begins — see the "Character refs" section above. Keep the old files as `.nbpro.png.bak` until the new versions are reviewed.

## Next session — restart checklist

1. Fully quit and reopen Claude Code so the MCP server picks up the new `GEMINI_IMAGE_ENDPOINT` env var (stdio MCP servers inherit env at spawn time).
2. `cd /Users/andresrodriguez/Documents/nano`
3. Verify model: test with one small image and check it feels right. If not, revert endpoint to `gemini-3-pro-image-preview`.
4. **Rename the existing Nano Banana Pro refs to `.nbpro.png.bak`** (so they aren't accidentally used as base images in `edit_image` calls):
   ```
   cd pythagoras-vol1/refs
   for f in pythagoras-mature.png pythagoras-boy.png pythagoras-young-man.png babylonian-magus.png; do
     mv "$f" "${f%.png}.nbpro.png.bak"
   done
   ```
5. **Regenerate the 4 Vol 1 character refs on Nano Banana 2** in this order: mature → boy → young-man → magus. Use `02-CHARACTERS.md` prompt anchors. Review each for face-lock consistency before moving on.
6. Once refs are approved, open `pythagoras-vol1/04-SCRIPT.md` and start generating pages sequentially.
7. Task list — tasks #26 (pages) and #27 (reader+card) remain. Add a new task for "Regenerate 4 refs on Nano Banana 2" at the top of that list.

## Page generation plan (Vol 1 — 18 images)

From `04-SCRIPT.md`. Aspect ratio: **2:3 vertical**. Every prompt should include:
- Character lock line with the signature features
- "NOT a children's book. Serious mature graphic novel, realistic proportions. Painterly realism."
- Panel layout with exact caption/dialogue text verbatim
- Relevant character ref image(s) via `edit_image` (1 character) or `compose_images` (2+ characters)

| # | Page | Key characters | Tool | Refs |
|---|------|----------------|------|------|
| Cover | Cover | Mature Pythagoras | edit_image | mature |
| 1 | Samos establishing | Boy | edit_image | boy |
| 2 | Hammers (12·9·8·6) | Boy + blacksmith | edit_image | boy |
| 3 | Pherecydes + tyrant | Boy (14) + Pherecydes | edit_image | boy |
| 4 | Departure | Young man | edit_image | young-man |
| 5 | Egypt arrival | Young man | edit_image | young-man |
| 6 | Rope-stretchers (3-4-5) | Young man + Egyptian priest | edit_image | young-man |
| 7 | Egypt falls | Young man | edit_image | young-man |
| 8 | Babylon rooftop | Young man + Magus | compose_images | young-man + magus |
| 9 | Numbers of the Sky | Young man + Magus | compose_images | young-man + magus |
| 10 | Years pass | Young man → transition | edit_image | young-man |
| 11 | Homecoming | Mature | edit_image | mature |
| 12 | Cave | Mature | edit_image | mature |
| 13 | Deciding | Mature | edit_image | mature |
| 14 | The crossing | Mature | edit_image | mature |
| 15 | Italy | Mature | edit_image | mature |
| 16 | Croton | Mature | edit_image | mature |
| 17 | The First Word | Mature | edit_image | mature |

## Reader and landing page (after pages done)

- Dark-themed reader, page-flipping, keyboard nav, mobile-friendly, 5-question quiz. Same DNA as Cogito, Relativity, Vol 2 will share.
- Pattern to copy: `../einstein/index.html` or `../descartes/index.html`.
- Landing card: add Vol 1 card to `../index.html`, matching the Vol 1 card format. Will eventually be two side-by-side entries when Vol 2 ships.

## Editorial reminders for page generation

- **2000-char prompt limit.** Condense style boilerplate. Keep character lock + exact text + panel layout + "NOT children's book" instruction.
- **Never paraphrase caption/bubble text.** Copy the script verbatim.
- **Watch for face drift.** If a page drifts to a generic "bearded Greek" face, regenerate composing TWO refs (age-specific + mature) with "keep the distinctive features" instruction.
- **NO on-panel violence.** Vol 1 doesn't have the bean field but does have Egypt-falling (p.7) and the crossing (p.14) — keep them atmospheric, not bloody.
- **The MCP sometimes appends `_1` to output filenames** instead of overwriting. After regenerating, `mv` the new file to the correct name.
- **Math rendering:** the 3-4-5 rope on page 6 is the only math diagram in Vol 1 (the theorem itself waits for Vol 2). Render the knots exactly: 12 knots, 3-4-5 triangle on the sand. Chalk-style label if needed.

## Vol 2 status

- All planning docs written (`../pythagoras-vol2/`).
- Refs NOT yet generated: `pythagoras-elder.png`, `theano.png`, `hippasus.png`, `cylon.png`. Also copy `pythagoras-mature.png` across or symlink.
- 22 pages to generate after Vol 1 ships.

## Files to read when starting a new session

Priority order:
1. This file (`HANDOFF.md`)
2. `CLAUDE.md` at repo root (project conventions)
3. `04-SCRIPT.md` (page-by-page script)
4. `01-STYLE-GUIDE.md` (palette, face-lock, what-to-avoid)
5. `02-CHARACTERS.md` (character sheets)
6. `03-SETTINGS.md` (location palettes)

The user's memory system at `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/MEMORY.md` is loaded automatically.
