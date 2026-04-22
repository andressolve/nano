# NB2 verification procedure

**Purpose:** Confirm that image generation is hitting Nano Banana 2 (`gemini-3.1-flash-image-preview`) and not the old NB Pro or default NB Flash endpoint. The user wasn't sure every page in Vol 1 was on NB2.

**Status:** Baseline preserved. Awaiting Claude Code restart to run the test.

---

## What we already know (indirect evidence)

- `~/.claude.json` project-scoped MCP config for `/Users/andresrodriguez/Documents/nano` sets:
  ```
  GEMINI_IMAGE_ENDPOINT=https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent
  ```
- Config change timestamp: 2026-04-22 06:01:54 (backup at `~/.claude.json.bak.20260422-060154`).
- Running `gemini-nanobanana-mcp` server started at 06:14:33 — AFTER the config change, so it picked up the override at spawn.
- This Claude session (PID 69013) started 06:47 — after both.
- All 18 pages and 4 refs are visually consistent with each other and distinct from the `.nbpro.png.bak` files.

This is strong circumstantial evidence, but I can't read back the exact endpoint hit per MCP call from inside Claude Code. Hence the direct test below.

---

## Baseline (already captured)

- Current page-08.png MD5: `da599ffef6f27d735e9230bcf004d7ab` (size 703711, generated 06:27 this session)
- Copy preserved at: `pages/page-08.verify-original.png`
- Refs used for page 8 (young-man + magus):
  - `refs/pythagoras-young-man.png` MD5 `4d60cc1b936bca9f9df0169a8c988cc3`
  - `refs/babylonian-magus.png` MD5 `b6f0f93ee8a951150b79038911d578a9`

---

## Test procedure (after Claude Code restart)

1. Fully quit Claude Code, relaunch in this same directory.
2. Ask Claude to read this file and resume verification.
3. Regenerate page 8 using `compose_images` with the SAME two refs (young-man + magus) and the SAME prompt used originally. Page 8 = Babylon rooftop with the Magus, from `04-SCRIPT.md`. Output to `pages/page-08.verify-new.png` (NOT overwrite original).
4. Compare:
   - Visual A/B side by side.
   - If they share the same palette / detail density / brush texture signature as the rest of Vol 1, we're on NB2.
   - If the new one looks noticeably different from the original AND from the rest of Vol 1 — flag it; the original session may have drifted to another endpoint.
5. Also check MCP server PID at time of the new generation:
   ```
   ps -eo pid,ppid,lstart,command | grep -i nanobanana | grep -v grep
   ```
   Record the PID and start time — confirms which MCP instance served the call.

---

## Prompt for page 8 regeneration (for reuse)

From `04-SCRIPT.md` page 8 "Babylon rooftop". Condensed to under 2000 chars, same discipline as original generation:

- 2:3 vertical
- Painterly realism, graphic novel, NOT children's book
- Two characters: young-adult Pythagoras (age ~25, sparse edged beard, signature face-lock: thick straight brows + broad high forehead + strong aquiline nose) + Babylonian Magus (from ref)
- Setting: broad flat palace rooftop, low parapet, ziggurat of Marduk in silhouette under deep cobalt star-filled sky, bronze brazier amber glow in corner
- Magus holds a clay tablet with cuneiform; both look up at the stars
- Captions and dialogue EXACTLY from script page 8 (look up again when regenerating to avoid drift)

---

## Cleanup after verification

- If match: delete `pages/page-08.verify-original.png` and `pages/page-08.verify-new.png`. Note result in HANDOFF.md.
- If mismatch: keep both. Investigate which endpoint the original was hit on. Decide whether to regenerate all 18 pages on confirmed NB2.
