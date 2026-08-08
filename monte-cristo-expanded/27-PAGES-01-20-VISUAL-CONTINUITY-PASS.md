# The Count of Monte Cristo — Pages 1–20 Visual Continuity Pass

## Status

**Approved and promoted on 2026-08-06.** Andres reviewed the complete set in
the expanded-edition reader, judged the continuity candidates materially
stronger, and approved them. The subsequent script-fidelity and cold-read /
visual gates both passed unconditionally. The exact approved files now occupy
canonical `pages/page-11.png` through `pages/page-20.png`; the former Round 10
canonical batch is preserved under
`qa/pre-visual-continuity-canonical-2026-08-06/`. The complete final gate and
hash map are recorded in
[`28-PAGES-11-20-VISUAL-CONTINUITY-FINAL-GATE.md`](28-PAGES-11-20-VISUAL-CONTINUITY-FINAL-GATE.md).

## Visual authority

The accepted opening sequence, Pages 1–10, is the authority for the expanded
edition's visual language. The fixed anchors for this pass are:

- **Page 5:** daylight character intimacy, warm skin, cloth, and Marseille
  environment;
- **Page 8:** low-light conspiracy, matte shadows, and controlled negative
  space;
- **Page 10:** immediate scene continuity into Page 11, ensemble blocking,
  native lettering, warm ivory balloons, and the predominant finished-page
  brush language;
- **Velvet Cinema selected style image:** medium and palette evidence only.

All Pages 11–20 candidates must share the opening's layered matte-gouache and
opaque-watercolor finish, broad visible brushwork, sparse charcoal/ink
construction, simplified interlocking color shapes, bold shadow masses, and
selective hard edges. Reject smooth airbrushed skin, glossy game-art polish,
generic prestige oil-painting realism, repeated digital texture overlays, and
anatomical micro-rendering that makes the second batch look like another
illustrator.

## Invariants

- Regenerate only complete pages; never patch a face, balloon, tail, word, or
  panel crop.
- Preserve the critic-approved script verbatim, once, in reading order.
- Preserve panel order, speaker sides, balloon attribution, and tail endpoints.
- Preserve the locked actor identities, ages, hair masses, costume value
  patterns, and forbidden-lookalike rules.
- Keep the exact 1024 × 1536 portrait canvas and mobile readability.
- Work non-destructively in `qa/visual-continuity-round-01/`. Do not replace a
  canonical page until the candidate passes both continuity and all earlier
  story/readability/anatomy gates.

## Why the drift became unusually large

1. Pages 11–20 went through many complete-page correction rounds. Each local
   story or lettering correction resampled the entire painting.
2. Later candidates were often derived from already-drifted candidates, so the
   smooth oil-painted finish compounded like a visual telephone game.
3. Inputs mixed actor sheets and pages from different generation runs. Those
   references carry incidental rendering style as well as intended identity.
4. “Velvet Cinema” was specified in words but a fixed accepted-page style
   anchor was not made dominant in every regeneration.
5. The critic gates correctly prioritized script fidelity, readability,
   attribution, anatomy, and actor distinctness, but did not score contact-sheet
   same-illustrator continuity.
6. Dense lettering and tail repairs encouraged cleaner, darker, more
   diagrammatic compositions, especially on Page 20.
7. The image generator is stochastic: without a fixed seed or style adapter, a
   narrowly requested correction can change brushwork, facial age, and overall
   finish.

## Pass sequence

Prototype the four hardest continuity burdens before the full run:

1. Page 11 — immediate warm-feast-to-cold-street transition;
2. Page 13 — opposed two-character examination and memory evidence;
3. Page 17 — exterior/transit montage and fortress geography;
4. Page 20 — four locations, four actor identities, dense dialogue, and prose.

If these establish one convincing visual family without breaking prior gates,
apply the same fixed-anchor method to the remaining Pages 12, 14–16, 18, and
19, then audit Pages 1–20 as a single contact sheet.

## Candidate map

| Page | Continuity candidate | Result |
| --- | --- | --- |
| 11 | `qa/visual-continuity-round-01/pages/page-11-vc01.png` | Pass — restores immediate Page 10 room, cast, lettering, and brush continuity |
| 12 | `qa/visual-continuity-round-01/pages/page-12-vc01.png` | Pass — keeps royalist privilege distinct without changing the medium |
| 13 | `qa/visual-continuity-round-01/pages/page-13-vc01.png` | Pass — examination and silent memory strip retain exact attribution |
| 14 | `qa/visual-continuity-round-01/pages/page-14-vc01.png` | Pass — separate accusation/letter logic and reversed final camera preserved |
| 15 | `qa/visual-continuity-round-01/pages/page-15-vc01.png` | Pass — A–B–A recognition exchange and silent hand/order beat preserved |
| 16 | `qa/visual-continuity-round-01/pages/page-16-vc01.png` | Pass — burn, blank order, trust, and Villefort-owned `Guard.` tail preserved |
| 17 | `qa/visual-continuity-round-01/pages/page-17-vc01.png` | Pass — same-Edmond transit strip and compact fortress geography preserved |
| 18 | `qa/visual-continuity-round-01/pages/page-18-vc02.png` | Pass after v2 — numeral `34` appears once in Panel 2; Panel 1 register is blank |
| 19 | `qa/visual-continuity-round-01/pages/page-19-vc01.png` | Pass — jailer/governor separation and unopened petition preserved |
| 20 | `qa/visual-continuity-round-01/pages/page-20-vc01.png` | Pass — four locations, cast separation, red purse, clerk silence, and file logic preserved |

## Internal audit result

- all ten canvases are exact 1024 × 1536 portrait PNGs;
- all ten 390 × 585 proofs remain readable in one normal top-to-bottom pass;
- every scripted speech/prose item is present once in order, with Page 18's
  permitted object numeral appearing once;
- speech tails remain attached to the intended visible speaker; silent guards,
  memory figures, guests, and clerk remain silent;
- no material extra-limb, fused-hand, malformed-face, actor-merge, or decisive-
  object failure was found;
- the Pages 1–20 contact sheet reads as one matte-gouache/opaque-watercolor
  production rather than an opening followed by a second oil-painted book.

Audit sheets:

- `qa/visual-continuity-round-01/pages-01-20-visual-continuity-contact-sheet.png`
- `qa/visual-continuity-round-01/pages-11-20-visual-continuity-contact-sheet.png`
- `qa/visual-continuity-round-01/mobile-pages-11-20-contact-sheet.png`

The first Page 18 continuity generation is retained for audit history; it was
rejected because it repeated the register numeral in Panels 1 and 2.

## Final promotion

On 2026-08-06, both required final gates returned exact approvals:

- `SCRIPT-FIDELITY APPROVED`
- `COLD-READ/VISUAL APPROVED`

The ten candidates in the map above were promoted byte-for-byte. Canonical
390 × 585 proofs and the Pages 11–20 contact sheet were rebuilt from the
promoted pages. Pages 1–20 are now locked as one visual production, and the
next production batch begins at Page 21.
