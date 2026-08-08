# The Count of Monte Cristo — Prototype Image Prompts

## Purpose

Reusable production prompt set for expanded Pages 12–18.

The exact page text, panel proportions, speaker ordinals, and tail endpoints
remain authoritative in
[`05-PROTOTYPE-PAGES-12-18.md`](05-PROTOTYPE-PAGES-12-18.md). The typography
rules remain authoritative in
[`06-PORTRAIT-TYPOGRAPHY-SYSTEM.md`](06-PORTRAIT-TYPOGRAPHY-SYSTEM.md).

Each final prompt consists of:

1. the common production block below;
2. the page-specific input roles;
3. the page-specific panel map;
4. the exact image text from the prototype script;
5. the page-specific attribution and continuity constraints below.

## Common Production Block

> Use case: illustration-story
>
> Asset type: finished story page for a historical graphic novel
>
> Create a complete new 1024 × 1536 portrait page. Input images are identity,
> setting, object, palette, lettering, and continuity references—not edit
> targets.
>
> Exactly 1024 × 1536 portrait, 2:3. Finished Velvet Cinema historical
> graphic-novel realism: layered matte gouache and opaque watercolor over
> sparse charcoal and ink construction; broad visible brushstrokes;
> simplified interlocking color shapes; bold shadow masses; tactile cloth,
> stone, wood, paper, wax, metal, flame, and water; expressive anatomically
> credible faces; selective hard edges at eyes, mouths, hands, and decisive
> objects.
>
> Avoid glossy game-concept-art surfaces, steampunk, anime, children's-book
> softness, generic grimdark, pirate fantasy, photographic lens effects, and
> dense engraved cross-hatching.
>
> Keep a clear top-to-bottom reading path, 64 px safe outer margins, calm
> gutters, and one dominant panel or image. No title and no page number.
>
> Bake every word into the finished image verbatim and exactly once. Use large,
> comfortable reader-size lettering. Speech balloons are warm ivory with
> restrained charcoal-brown painted outlines and dark upright hand-lettered
> mixed-case text. Prose uses a dark literary serif on a stable matte
> parchment field. Keep balloons on the named speaker's side. Every tail ends
> in open space immediately beside the correct speaker's mouth. No blank
> balloons, no extra text, no signature, and no watermark.

## Page 12 — Two Betrothals

### Inputs

1. `../monte-cristo/refs/05-villefort-1815.png` — Villefort identity.
2. `../monte-cristo/pages/page-08.png` — Renée, Saint-Méran room, balloons,
   palette, and finish.
3. `../monte-cristo/refs/07-key-objects.png` — accusation, paper, and red wax.

### Page-specific instructions

- Use the four-part portrait map in the exact script: prose field, dominant
  couple panel, Marquise/Villefort opposition, official entering with paper.
- Speaking order and sides:
  - Renée left → Villefort right;
  - Marquise left → Villefort right;
  - official left → Villefort right.
- Background guests are silent.
- Renée is silent in the final two panels.
- No Edmond and no guards.
- Preserve spellings: Renée, Saint-Méran, Gérard, Noirtier, Bonapartist, Elba.

## Page 13 — A Dying Captain's Word

### Inputs

1. `../monte-cristo/refs/01-edmond-young.png` — Edmond identity.
2. `../monte-cristo/refs/05-villefort-1815.png` — Villefort identity.
3. `../monte-cristo/refs/08-dialogue-settings.png` — examination room.
4. `pages/page-12.png` — immediate page continuity.

### Page-specific instructions

- Use the five-part portrait map in the exact script.
- Captain Leclère appears only as a silent, subordinate memory-image inside the
  dominant panel.
- Present-time speakers are only Villefort and Edmond.
- Preserve the intact sealed letter.
- Preserve spellings: Edmond Dantès, *Pharaon*, Captain Leclère, Grand Marshal
  Bertrand, Elba.

## Page 14 — Innocent

### Inputs

1. `../monte-cristo/refs/01-edmond-young.png` — Edmond identity.
2. `../monte-cristo/refs/05-villefort-1815.png` — Villefort identity.
3. `../monte-cristo/refs/08-dialogue-settings.png` — examination room.
4. `pages/page-13.png` — immediate page continuity.

### Page-specific instructions

- Use the four-part portrait map in the exact script.
- Panels 1–2: Villefort left, Edmond right.
- Panel 3: Villefort alone with the unsigned accusation.
- **Critical final-panel correction:** Edmond is physically left beside the
  door and asks first from upper-left. Villefort is physically right behind
  the desk and answers second from lower-right.
- The sealed true letter remains intact and separate from the unsigned
  accusation.
- No other people.
- Preserve spellings: Napoleon, Mercédès, Elba, Danglars.

## Page 15 — Noirtier

### Inputs

1. `../monte-cristo/refs/01-edmond-young.png` — Edmond identity.
2. `../monte-cristo/refs/05-villefort-1815.png` — Villefort identity and
   recognition range.
3. `../monte-cristo/refs/07-key-objects.png` — letter, wax, pen, and paper.
4. `pages/page-14.png` — immediate page continuity.

### Page-specific instructions

- Use the five-part recognition descent in the exact script.
- Villefort is left and Edmond right whenever both appear.
- Dominant-panel dialogue is A–B–A:
  - Villefort upper-left;
  - Edmond upper-right;
  - Villefort lower-left.
- Panel 3 is silent: Villefort's right hand becomes still above the blank
  order.
- Bottom strip ends on Edmond's unanswered “Then I may go?”
- No guards and no additional characters.
- Do not burn the letter or sign the order yet.
- Preserve spellings: Monsieur Noirtier, Rue Coq-Héron, Paris.

## Page 16 — The Choice

### Inputs

1. `../monte-cristo/refs/01-edmond-young.png` — Edmond identity.
2. `../monte-cristo/refs/05-villefort-1815.png` — Villefort identity.
3. `../monte-cristo/refs/07-key-objects.png` — fire, letter, wax, pen, order.
4. `pages/page-15.png` — immediate page continuity.

### Page-specific instructions

- Use the four-part “one paper burns, another is signed” map.
- Villefort remains left and Edmond right.
- Burn the true letter completely in Panel 1.
- Place the silent decision after Edmond's trust in Panel 3; Villefort then
  signs the separate detention order.
- Exactly one guard appears only in the final panel and remains silent.
- The “Guard.” balloon belongs to Villefort, not the visible guard.
- No readable handwriting.
- Preserve spelling: Noirtier.

## Page 17 — The Black Island

### Inputs

1. `../monte-cristo/refs/01-edmond-young.png` — Edmond identity.
2. `../monte-cristo/refs/18-chateau-dif-escape.png` — fortress and landing.
3. `../monte-cristo/pages/page-11.png` — night boat and guard.
4. `pages/page-16.png` — immediate page continuity.

### Page-specific instructions

- Use the five-part geography-before-consequence map.
- The prose field remains unillustrated and stable.
- The continuous-time strip shows the same Edmond in corridor, barred
  carriage, and harbor—not three prisoners.
- Exactly two speakers: Edmond left and the principal guard right.
- Additional guards and rowers are silent.
- Château d'If is the dominant visual fact and follows the accepted reference
  geometry.
- The lower gate strip is silent.
- Preserve spellings: Villefort, Edmond, Château d'If.

## Page 18 — Prisoner Thirty-Four

### Inputs

1. `../monte-cristo/refs/01-edmond-young.png` — young Edmond identity.
2. `../monte-cristo/refs/18-chateau-dif-escape.png` — prison interior.
3. `../monte-cristo/pages/page-12.png` — clerk, jailer, register, bars.
4. `pages/page-17.png` — immediate page continuity.

### Page-specific instructions

- Use the four-part register → key → door map.
- Panels 1–2: clerk left, Edmond right.
- Panel 2 uses A–B–A speaker order.
- **Threshold correction:** Edmond is physically left and speaks first; the
  jailer is physically right and answers second.
- Final panel repeats Edmond left inside and jailer right outside.
- One background guard may appear only in Panels 1–2 and remains silent.
- Edmond remains clean-shaven and nineteen; do not use his later bearded prison
  design.
- The only permitted object text is the numeral `34`; essential classification
  remains spoken.
- Preserve spellings: Edmond Dantès, Prisoner Thirty-four, Bonapartist,
  Villefort, Morrel, Mercédès.

## Regeneration Rule

If any text, attribution, tail, identity, dimension, or causal panel order
fails, regenerate the complete page from the same accepted references. Never
patch a balloon, tail, face, or panel crop into an otherwise accepted page.
