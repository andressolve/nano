# 00 — PROJECT BRIEF

## The Riddle of the Stone
### How One Man Read a Language No One Alive Had Ever Heard

- **Shelf:** Intellectual detective stories — **Volume 1** (new shelf, first volume).
  True stories told as genuine mysteries; the deduction IS the story. Vol 2 leading
  candidate: John Snow's cholera map.
- **Chassis:** Narrative mystery comic — TRUE multi-panel dialogue comic (Icarus/Foundation
  lineage), **3:2 landscape (1536×1024)**, one-shot whole-page bake, generous in-image text.
  NOT the biography chassis, NOT a text-led essay. Paced as a whodunit: clues are planted
  on-page, in the reader's plain sight, so the reader can race the detective.
- **One-sentence window:** From the last hieroglyph carved at Philae in AD 394 to
  Champollion reading temple walls aloud in Nubia in 1829 — with the case itself running
  1799 (the stone) → 1822 (the reveal) → 1824 (the whole system).
- **The mystery, stated as a case:** A whole civilization wrote everything down, then the
  readers died out. The victim: a language. The evidence: a broken stone that says the same
  thing three ways. The false trail: fourteen centuries of believing the signs were magic
  symbols, not sounds. The rival detectives: the cleverest man in England and a poor,
  obsessed French linguist. The break in the case: two royal names sharing letters. The
  reveal: a pharaoh's name, three thousand years old, that sounds itself out.
- **Audience:** the standing project audience; serious, clear, never dumbed down.
  Milestone-first and research-honest per the brilliant-exemplars bar; the facts carry it.
- **Image model:** gpt-image-2 standard, `quality: high`, `size: 1536x1024`.
  **Multi-ref `edit_image` (`imagePaths`, 1–16) is available and is the default ref
  strategy** (Strategy 0, per gemini_thin.md C.7).
- **Page count:** cover + 17 pages + quiz (5 WHY-questions). Page count is a target, not a
  contract.
- **Reader:** dark flipper, landscape width `min(1400px, 96vw)`, footer **CASE-FILE strip**
  (see style guide) — the detective-shelf sibling of the kill-chain/prayer-hours strips.
- **Accent color:** lamplight gold on ink — `#d9a441` (provisional; locked in style guide).

## Structure (whodunit beats → pages)

| Beat | Pages |
|---|---|
| The victim (a silent language, 1,400 years) | P1 |
| The evidence appears (the stone, 1799) | P2–P3 |
| The false trail (symbols-not-sounds; everyone fails) | P4 |
| The two detectives (Champollion's arsenal; Young's brilliance) | P5–P7 |
| The blind spot (Champollion himself refuses phonetics till 1821) | P8 |
| The break (Cleopatra; the cross-check the reader can verify) | P9–P10 |
| The doubt (all cracked names are foreign — Young could still be right) | P11 |
| The reveal (Abu Simbel; the reader races him; Ramesses) | P12–P13 |
| The confession scene (Lettre à Dacier, Young in the room) | P14 |
| Whose key was it? (the dispute, handled honestly) | P15 |
| The whole answer (the Précis; why everyone was partly right) | P16 |
| The country speaks again (Egypt 1828–29; death at 41; the reader can now read) | P17 |

## Key production notes

1. **Research is the law.** Every date/quote in `RESEARCH.md`, web-verified 2026-07-05.
   No fake quotes. "Je tiens mon affaire !", "notre alphabet est bon", the Young/Champollion
   dispute quotes, and the 1824 Précis definition are the verbatim set. Fourier's promise
   and the days-long faint are framed "the story is told" (Hartleben tradition).
2. **Cartouche fidelity is the volume's central image risk.** The clues ARE specific glyphs
   (lion = L, folded cloth = S, sun disc = Ra, ibis = Thoth). Real glyph strings must come
   from locked reference plates built from verified sources, not from the model's memory.
   See 01-STYLE-GUIDE "Cartouche-fidelity plan." Prototype the hardest evidence pages FIRST
   (P10 cross-check, P12 reader-race).
3. **Ref strategy (user directive):** ONE master cast plate in a SINGLE generation — young
   Champollion, adult Champollion, Jacques-Joseph, Thomas Young, THE STONE itself (5
   entities, faces large) — plus solo refs; pass master plate + relevant solos natively
   via multi-ref per page. Text-prompt-only locks are banned for recurring cast.
4. **Reader-race discipline:** clue boxes are honest — everything Champollion knew, the
   reader is given BEFORE the solve. P12 ends on a cliffhanger with all pieces on the page.
5. **Register:** proposed "ink & lamplight" (style guide §1) — Register-B ink-line machinery
   tuned to a nocturnal scholar's palette. Alternative floated in planning: period-engraving/
   expedition-notebook. DECISION OPEN — prototype before committing (user review gate).
6. **STOP GATE:** no image spend until the user reviews these docs + the script.

## Deliberate editorial choices

- The book opens in AD 394 (the last writer) and closes in 1829 (the first new reader,
  Champollion in Nubia) — silence bookended by speech. Inside that frame, chronology is
  respected; no reordering was needed, the true sequence is already a perfect mystery.
- Young is a genuine rival detective, not a villain: his real finds (script family,
  cartouches, 13 values, demotic) are credited on-page, his scoreboard shown honestly,
  and the priority dispute gets its own page with both men's verbatim words.
- Champollion's own 1821 blind spot is kept — the detective who almost refused the answer
  is better drama AND better history.
- Engineering-of-thought focus; no politics of antiquities repatriation — different book.
- Champollion's death (stroke, 41) is one dignified caption, not a scene.

## Cost envelope

Refs: 1 master plate + ~5 solos + 2–3 cartouche plates (PIL/local, ~free) ≈ $1.30.
Pages: cover + 17 × ~$0.21 ≈ $3.80. Prototypes/regens buffer ≈ $0.60.
**Target ≈ $5.70**, in line with the myth/narrative envelope.
