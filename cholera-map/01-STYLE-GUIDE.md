# 01 — STYLE GUIDE

## §1 Register — "Ink & Lamplight" (shelf-shared, validated on Vol 1)

Same signature register as *The Riddle of the Stone* — the shelf's identity, not a
per-volume choice. **Register-B ink-line + flat color**, nocturnal scholar's/case-file
palette: deep ink blues and charcoal blacks, parchment cream, warm lamplight ambers.
Scenes live on foggy streets, in a physician's study, in a Vestry board room, by
candlelight. **One shared accent across the shelf: lamplight gold `#d9a441`** marks
EVIDENCE and UNDERSTANDING (the map lighting up as the pattern locks in, the cesspool
diagram, the moment the numbers align). Documents, maps, and tables render as crisp
cream "evidence insets" pinned into panels — the case-file look, unchanged from Vol 1.

**STYLE BLOCK (paste verbatim into every prompt):**
> Bold ink-line comic-book art with flat color, in the tradition of modern literary
> graphic novels. Clean confident black linework, flat color fills, minimal soft
> rendering. Nocturnal case-file palette: deep ink-blue and charcoal shadows, parchment
> cream, warm amber lamplight; fog-grey and wet-cobblestone tones for Soho street scenes.
> One accent color: lamplight gold on documents, maps, and diagrams at moments of
> discovery. Evidence — maps, tables, diagrams — appears as crisp cream inset panels,
> like exhibits in a case file.

**REGISTER GUARD (block 2):**
> NOT a children's book. Serious mature graphic novel, realistic proportions, natural
> lighting, cinematic composition. Serious mystery tone — a true intellectual detective
> story, not a cartoon caper. Public-health subject handled with dignity: no depicted
> illness, vomiting, or bodies — convey danger through empty streets, closed doors, and
> the evidence itself.

## §2 Format

- **3:2 landscape, 1536×1024**, gpt-image-2 standard, quality high. One-shot whole-page
  bake: all panels + all lettering in a single `generate_image`/`edit_image` call.
- 3–4 panels per page, explicit geometry in every prompt, clean solid-black borders,
  clear white gutters.
- Evidence pages (P8, P11, P16, P17) may break the grid: one large "case-file splash"
  with pinned exhibits instead of panels. State it explicitly.
- Text density: generous (narrative-mode rule). ~8 elements / ~75 words per page is
  proven; evidence pages run caption-heavy.

## §3 Prompt order (six blocks, do not reorder)

1. Layout spec (panel geometry / case-file splash)
2. STYLE BLOCK (verbatim, §1)
3. REGISTER GUARD (verbatim, §1)
4. RECURRING CHARACTERS lock block — "keep them IDENTICAL in every panel"; visual locks
   only, never the famous name; refs passed via `imagePaths`
5. Per-panel scene beats (who / where / action / camera)
6. `LETTERING — verbatim, render exactly:` … closing with the restrictions block:
   "All words spelled correctly. Do not duplicate text. Do not invent extra captions.
   NO modern logos, NO watermarks, NO spurious signage. Do not put quotation marks inside
   speech bubbles."

## §4 Ref strategy — multi-ref native (Strategy 0)

- **Master cast plate** (`refs/ref_cast_plate.png`): ONE single generation, 4 entities,
  faces/map large: Snow (~41), Whitehead (~29), Farr (~mid-forties), and THE MAP (a
  cream exhibit board with black death-bars and pump markers, shown as an object on an
  easel/table in the lineup). Thin name labels under each; prompt tells the model to
  ignore labels.
- **Solo refs:** one per human entity (3), generated after the plate passes the casting
  gate, each anchored on the plate via multi-ref so plate and solos agree. The Map's
  authoritative form lives in the PIL exhibit plates (§5), not a painted solo.
- Pre-flight rules unchanged: glob `refs/` before batches; Re-Read every involved ref and
  write a one-line verbatim observation before prompting.

## §5 Death-map fidelity plan (the volume's central image risk)

The clue is a specific, real geometry: real streets, a real pump location, and a real
density of death-bars clustered around it. The model must never freehand this map.

1. **Build the map plate locally (PIL), not by generation.** `tools/build_broad_street_
   map.py` draws a simplified period-style street grid (Broad Street, Cambridge Street,
   Poland Street, Berwick Street, Marlborough Street) with the 1854 public pumps marked,
   and death-bars clustered tightly and overwhelmingly around the Broad Street pump,
   thinning with distance — matching the real historical pattern (Wikipedia/UCLA epi
   sources) without claiming to be a literal facsimile of Snow's 1855 engraving.
2. Render at least two versions:
   - `refs/plate_map_full.png` — fully labeled exhibit (pump names, a scale note) for
     pages where Snow/Whitehead are actively explaining the map.
   - `refs/plate_map_unannotated.png` — pump locations marked but NO explanatory text
     circling the answer, for the P11 reader-race page (honest-mystery rule: the reader
     gets the same clue Snow had, not the answer pre-solved).
3. Pass the relevant plate via `imagePaths` on every page that exhibits it; the prompt
   says "copy the map layout EXACTLY from the reference — same streets, same pump
   positions, same bar clusters."
4. On-page map annotations (pump labels, the discovery ring around Broad Street) are
   part of the LETTERING block, added only on pages after the reveal.

## §6 Lettering rules

- Captions: cream case-file boxes, dark serif text; corner placement stated per caption.
- **CLUE BOXES** — shelf signature: a small cream box with a gold pin/corner tab reading
  `CLUE:` followed by the fact. Every clue the detective gets, the reader gets, on the
  page where he gets it.
- Speech bubbles: round, off-white, dark serif, tails explicitly aimed; no quotation
  marks inside bubbles.
- Period vocabulary glossed on first use in captions: cesspool, miasma, Vestry, Board of
  Guardians, epidemiology (used only in the closing/legacy pages, glossed as "the study
  of how disease spreads through a population").

## §7 Footer CASE-FILE strip (reader HTML, not in-image)

Persistent footer strip, teal-on-dark (`#4a9b95`), six stages; the active stage lights
per page:

`THE FEAR · THE OUTBREAK · THE FALSE TRAIL · THE MAP · THE REVEAL · THE CURE`

Mapping: P1 The Fear; P2–P3 The Outbreak; P4–P5 The False Trail; P6–P11 The Map
(investigation, cluster, both predictive tests, reader-race); P12–P17 The Reveal
(confrontation, pump handle, honest doubt, Whitehead, mechanism, Grand Experiment);
P18–P19 The Cure. Hidden on cover and quiz.

## §8 Moderation notes

Public-health/mortality subject — the shelf's first with a real death toll in the
hundreds, including a child. Discipline:
- No depicted illness (vomiting, dehydration, sickbed suffering) at any point.
- Baby Frances Lewis and Constable Lewis: closed doors, black mourning ribbon/crepe on a
  door-knocker, a name on a written register — never a body, never an on-page death
  scene, never an infant shown ill.
- Crowd/panic scenes (families fleeing) shown via loaded handcarts, shuttered shops,
  empty streets — not injured or dying figures.
- The pump itself is never shown dispensing anything but clear water — the contamination
  is conveyed through the cesspool diagram exhibit, not through visibly foul water.
