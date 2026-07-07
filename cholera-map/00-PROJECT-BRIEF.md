# 00 — PROJECT BRIEF

## The Riddle of the Well
### How a Map, a Doctor, and a Skeptical Priest Traced a Plague to a Single Pump

- **Shelf:** Intellectual detective stories — **Volume 2** (Vol 1: *The Riddle of the
  Stone*, Champollion & the Rosetta Stone, shipped, user-QA PASSED "BRAVO!!!").
  True stories told as genuine mysteries; the deduction IS the story.
- **Chassis:** Narrative mystery comic — TRUE multi-panel dialogue comic, **3:2 landscape
  (1536×1024)**, one-shot whole-page bake, generous in-image text. NOT the biography
  chassis, NOT a text-led essay. Paced as a whodunit: clues are planted on-page, in the
  reader's plain sight, so the reader can race the detective.
- **One-sentence window:** From late August 1854, when an invisible killer explodes
  through a few streets of Soho in ten days, to 1866–1965, when a rival statistician,
  a new sewer system, and a forgotten Italian microscope slide all quietly confirm what
  one doctor's map had already shown.
- **The mystery, stated as a case:** People are dying by the dozen, on the same few
  streets, within days of each other. The victim: an entire neighbourhood, and the
  reputation of "bad air" as the official cause of disease. The evidence: a map made of
  black bars, each one a death, piling up around a single water pump. The false trail:
  the era's respected miasma theory, held even by serious scientists. The rival
  detective: a young priest who set out to *disprove* the map and instead found the
  leak that explained it. The predictive test: a brewery, a workhouse, and a widow
  three miles away, none of whom should have gotten sick if the theory was wrong — and
  didn't, or did, exactly as the theory predicted. The reveal: a cesspool three feet
  from a well. The twist: officialdom rejected the answer anyway, and the truth was
  confirmed only after the detective was already dead.
- **Audience:** the standing project audience; serious, clear, never dumbed down.
  Milestone-first and research-honest; the facts carry it. Dignified-death discipline
  throughout — cholera kills by dehydration, not spectacle, and the youngest victim is a
  baby who never appears on-page as a body.
- **Image model:** gpt-image-2 standard, `quality: high`, `size: 1536x1024`.
  Multi-ref `edit_image` (`imagePaths`, 1–16) is the default ref strategy (Strategy 0).
- **Page count:** cover + 19 pages + quiz (5 WHY-questions). Page count is a target, not
  a contract.
- **Reader:** dark flipper, landscape width `min(1400px, 96vw)`, footer **CASE-FILE
  strip**, stages renamed for this case (see style guide).
- **Accent color:** well-water teal `#4a9b95` — cool, clean, water-as-the-clue, distinct
  from Vol 1's lamplight gold `#d9a441` (the shelf's shared register still carries amber
  lamplight for evidence/discovery moments; the reader chrome accent differs per volume).

## Structure (whodunit beats → pages)

| Beat | Pages |
|---|---|
| The fear (cholera's reputation; no one knows how it travels) | P1 |
| The outbreak explodes (Soho, late Aug–early Sept 1854, ten days, 500 dead) | P2–P3 |
| The false trail (miasma theory; Farr's serious, numbers-based rival case) | P4–P5 |
| The detective and his method (Snow; the 1849 idea nobody believed; door to door) | P6–P7 |
| The map takes shape (case-file splash; bars piling up around one pump) | P8 |
| The predictive test #1 (brewery + workhouse spared — their own wells) | P9 |
| The predictive test #2 (the Hampstead widow, three miles away, same water) | P10 |
| The reader-race page (the full map, the reader finds the pump first) | P11 |
| The confrontation (Snow before the Vestry Board of Guardians, 7 Sept) | P12 |
| The pump handle (8 Sept — the iconic gesture) | P13 |
| The honest doubt (Snow's own words: the outbreak was already waning) | P14 |
| The second detective (Whitehead sets out to disprove Snow) | P15 |
| The mechanism found (the cesspool, three feet from the well) | P16 |
| The number-proof (the Grand Experiment — two water companies, one comparison) | P17 |
| Officialdom says no (1855 Board of Health rejects the theory; Snow dies unvindicated) | P18 |
| The world changes (sewers, Farr's own conversion, Pacini's ignored microscope) | P19 |

## Key production notes

1. **Research is the law.** Every date/quote in `RESEARCH.md`, web-verified 2026-07-06.
   No fake quotes. Snow's own honest words on the pump handle's effect, Farr's 1852
   "most important theory" line, and the Grand Experiment's 315-vs-37-per-10,000 figures
   are the verbatim/exact set.
2. **The Broad Street death map is the volume's central image risk**, exactly as the
   cartouches were for Vol 1. It must be **PIL-built from real historical death-location
   geometry**, never freehanded by the model — see `tools/build_broad_street_map.py` and
   01-STYLE-GUIDE §5. Prototype the reader-race exhibit page (P11) FIRST.
3. **Ref strategy:** ONE master cast plate in a SINGLE generation — Snow, Whitehead,
   Farr, and the Map itself (4 entities, faces/map large) — plus solo refs; pass
   master plate + relevant solos natively via multi-ref per page.
4. **Reader-race discipline:** every clue Snow used (the pump-centered cluster, the
   brewery/workhouse exceptions, the Hampstead widow) is shown to the reader before he
   states his conclusion. P11's map exhibit is left **UNANNOTATED except for the pump
   markers** so the reader can spot the pattern before the caption confirms it.
5. **Register:** reuse the shelf's validated "ink & lamplight" register (Register-B
   ink-line + flat color, nocturnal case-file palette) — the shelf's shared identity.
   Reader accent differs per volume (see above).
6. **Dignified-death discipline (load-bearing, read RESEARCH.md editorial cautions):**
   Baby Frances Lewis and Constable Lewis are never shown as sick or dying on-page —
   closed doors, black ribbon, a name in a register, nothing more. No vomiting, no
   graphic dehydration. Cholera's danger is conveyed through empty streets, chalked
   doors, and the map's black bars — not bodies.

## Deliberate editorial choices

- The book opens on ordinary streets on an ordinary evening (the reader does not yet
  know what's coming) and closes on the same streets in the present day, where a
  memorial pump still stands outside a pub named for the detective — silence-to-
  monument bookending, same device as Vol 1's silence-to-speech frame.
- William Farr is a genuine rival detective, not a strawman: his elevation-based miasma
  theory was serious, numbers-driven science for its time, and it is credited honestly.
  His own later conversion (1866) is the volume's best "whose key was it" beat.
- Reverend Whitehead gets real, undiluted credit: he found the mechanism (the cesspool)
  that Snow's map implied but could not itself prove. The book does not let Snow's name
  eclipse his.
- The pump handle is kept as the iconic gesture, but immediately followed by Snow's own
  scientifically honest doubt about how much it actually did — the shelf's honesty rule
  applied to its own hero moment.
- Filippo Pacini appears only in the closing pages as the story's quiet double — a
  bacterium seen and ignored in the very year of Broad Street, vindicated only in 1965.
  No invented dialogue for him; his beat is narration-only.
- No modern epidemiological jargon (R0, germ theory formalism) projected backward onto
  1854 — Snow and Whitehead speak and reason in period terms; the closing pages name
  what came after as "later," not as something they knew.

## Cost envelope

Refs: 1 master plate + ~4 solos + 1 PIL death-map exhibit (free) ≈ $1.05.
Pages: cover + 19 × ~$0.21 ≈ $4.20. Prototypes/regens buffer ≈ $0.65.
**Target ≈ $5.90**, in line with the detective-shelf envelope.
