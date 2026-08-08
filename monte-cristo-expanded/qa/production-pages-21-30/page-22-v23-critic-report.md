# Page 22 v23 — Independent Critic Report

## Verdict

# REVISE

Page 22 v23 repairs the v9 ending order: Panel 4 now reads `Who is there?` →
`scrape · scrape` → `Again.`. It also preserves the lone Panel 3 scrape and a
clear final mouth-connected `Again.` inset. Three mandatory failures remain:
`Take it.` is visually attributed to the jailer instead of Edmond, the first-
sound panel has been compressed to roughly half its scripted height, and the
`Who is there?` tail ends near Edmond's hair/forehead rather than beside his
mouth.

This report was made against the locked Page 22 rubric and the v9 regression
gate. The builder's prompt and self-audit were not used as approval evidence.

## Candidate identity

- Full-resolution candidate:
  `monte-cristo-expanded/qa/production-pages-21-30/page-22-v23.png`
- Full-resolution metadata: 1024 × 1536, 8-bit RGB PNG, no alpha,
  non-interlaced
- Full-resolution SHA-256:
  `d49638fee46a19516c180fd405bcf3e32b62e644209ab2dc0eb5ce85b5c8dc04`
- Binding desktop proof:
  `monte-cristo-expanded/qa/production-pages-21-30/page-22-v23-desktop.png`
- Desktop metadata: 600 × 900, RGB PNG, no alpha
- Desktop SHA-256:
  `84628e67a73bfcd3b43972e78eb6e42fb41e15358260df397cc2ee813d739fed`
- Secondary tablet proof:
  `monte-cristo-expanded/qa/production-pages-21-30/page-22-v23-tablet.png`
- Tablet metadata: 768 × 1152, RGB PNG, no alpha
- Tablet SHA-256:
  `2b485600e0a978a05f0f1844d8732be6c7da2aece6fa7243c692ac01e804d7f9`
- Verification: fresh 600 × 900 and 768 × 1152 derivations from the source were
  byte-identical to the supplied proofs.

## Mandatory findings

### M1 — `Take it.` is attributed to the jailer instead of Edmond

**Visible evidence:** In Panel 1, both balloons are centered over the left half
of the exchange and both tails point left. `Eat.` correctly points toward the
jailer's mouth. The separate `Take it.` tail also projects left toward the
jailer rather than right toward Edmond. Edmond is on the far right with no
connector from his mouth to his scripted reply.

This reverses visible speaker ownership. A reader can infer from the words that
Edmond probably refuses the bowl, but inference is not a pass: the authoritative
speaker map requires Jailer `Eat.` upper-left followed by Edmond `Take it.`
upper-right, each with its own mouth-adjacent tail.

**Required complete-page regeneration:** Keep the jailer on the left and Edmond
on the right. Place `Eat.` in the jailer's upper-left lane with a short tail
beside his lips. Place `Take it.` in Edmond's upper-right lane with a separate
short tail ending in open space immediately beside Edmond's visible lips. The
two tails must point in opposite speaker directions and must not share a lane.
Regenerate the complete page; do not move or patch only the balloon/tail.

### M2 — Panel 3 is too compressed to carry the scripted stillness and first sound

**Visible evidence:** The candidate's approximate panel shares are 28% / 24% /
12% / 36%. The approved map is 25% / 28% / 23% / 20%. Panel 3—the dark-cell
pause and the first lone `scrape`—has been reduced to about half its assigned
height, while Panel 4 has expanded to nearly twice its assigned share.

The four panels remain distinct, but the page's essential pause is no longer
given the planned duration. The first sound becomes a thin connective strip
between the jailer scene and the large answering tableau instead of the
smallest interruption breaking prolonged stillness. This weakens the page's
spectacle/dialogue rhythm and violates the exact relative-size map.

**Required complete-page regeneration:** Restore functional proximity to the
25% / 28% / 23% / 20% hierarchy. Panel 3 must receive a genuine quiet field,
approximately one-fifth to one-quarter of the page, so Edmond's stillness and
the single small scrape register before the answer. Panel 4 must remain large
enough for its three vertical text tiers but must not consume more than a third
of the page by taking space from Panel 3. Preserve four separate panels and one
top-to-bottom path.

### M3 — `Who is there?` does not have the required mouth-adjacent tail

**Visible evidence:** In Panel 4, the `Who is there?` balloon's short lower-left
tail ends in dark space above and to the right of Edmond's hairline/forehead.
It does not reach open space beside his lips. The gap and vertical offset are
obvious at source size and remain visible at the desktop proof.

Edmond is the only visible speaker, so ownership can be recovered. The binding
tail rule nevertheless requires a distinct mouth-adjacent connector for every
live balloon, and the prior Pages 11–21 gate repeatedly treated remote
head/hair/empty-space tails as blocking.

**Required complete-page regeneration:** Preserve `Who is there?` at the
upper-left tier, but route a short, unmistakable tail into open space
immediately beside Edmond's visible mouth. Do not point at hair, forehead,
shoulder, arm, wall, or empty mid-distance. Retain a separate mouth-connected
tail for the lower `Again.` balloon.

## v9 blocker verification

### Panel 4 `Who` → double scrape → `Again` order: PASS

- `Who is there?` is encountered first at upper-left.
- `scrape · scrape` is clearly next at middle-right on the wall.
- `Again.` is isolated at the bottom-left/bottom inset and is encountered last.
- The double scrape therefore reads as an answer to Edmond's question before
  he commands the unseen source to repeat it.

## Other passed checks

### Exact text and omission/duplication

- All eight scripted items appear once with correct spelling, case, and
  punctuation.
- Panel 3 contains exactly one lowercase, tail-free `scrape` and no second
  sound or invented word.
- Panel 4 contains exactly `Who is there?`, `scrape · scrape`, and `Again.` in
  the correct vertical order.
- No title, page number, speaker label, ordinal, stray prop text, extra sound,
  or invented dialogue appears.

### Remaining panel causality

- Panel 1 shows the jailer offering a clearly visible bowl to Edmond; the
  action makes the clipped food exchange concrete despite M1's tail error.
- Panel 2 shows Edmond turning away from the food while the jailer invokes
  tomorrow.
- Panel 3 removes the jailer and shows only Edmond at the solid interior wall
  when the lone sound occurs.
- Panel 4 shows Edmond alert with his hand against the wall, the answering
  double scrape, and the final demand.

### Remaining balloon lanes, tails, and silence

- `Eat.` belongs visibly to the jailer.
- Both Panel 2 balloons have unambiguous mouth-adjacent ownership.
- Both sound texts are integrated into stone, tail-free, and outside speech
  balloons.
- The final `Again.` balloon is clearly last, stays within the bottom safe
  area, and its long narrow tail reaches open space beside Edmond's mouth.
- No jailer, guard, Faria, second prisoner, or other silent figure is visible
  when the sounds occur.

### Identity and continuity

- Edmond remains the canonical Page 21 Prison Edmond: gaunt dark face, deep-
  set eyes, strong brow, long clean nose, high cheekbones, tangled dark hair,
  rough beard, torn linen, and worn dark vest.
- The jailer retains his short barrel silhouette, ruddy balding head, bulbous
  nose, gray-red stubble, rust/prison-brown clothing, keys, and stoop.
- Neither actor collides with Faria, the navy escort guard, Leclère,
  Caderousse, Jacopo, or Villefort.

### Sound source and Page 23 boundary

- The lone and double scrapes clearly originate from interior stone, not the
  door, bowl, jailer, ceiling, or Edmond.
- The wall remains solid. There is no tunnel, hole, loose floor stone,
  revealing crack, emerging hand, visible prisoner, voice, or Faria.
- The source is not prematurely identified as below Edmond.

### Period setting and Velvet Cinema continuity

- Damp stone, iron door, prison bowl/food, torn linen, jailer keys, and
  restrained lamp glow are period-credible and causally legible.
- The mineral/black-green/rust palette and matte, tactile finish continue
  canonical Page 21 and accepted Pages 18–20.
- The candidate does not create a material smooth-oil, glossy game-art,
  photographic, steampunk, or separate-illustrator break.

### Typography and display comfort

- Dialogue uses the locked upright hand-lettered family in warm-ivory,
  charcoal-outlined balloons; sound text is visually distinct and integrated
  into the stone.
- Every word is comfortably readable without zooming at the binding 600 × 900
  desktop proof and the secondary 768 × 1152 tablet proof.
- No text is cropped, malformed, or below a normal desktop/tablet comfort
  threshold. Phone/390 performance was not used as a gate.

### Anatomy and generation integrity

- Both wall-contact hands have four fingers plus one thumb, credible joints,
  wrists, and stone contact.
- The jailer's bowl-holding hands, Edmond's other visible hand, faces, bodies,
  keys, bowl, door, wall, and borders have no approval-blocking malformed,
  fused, duplicated, floating, or cropped element.
- No extra/missing limb, duplicate actor, broken face, or orphan tail fragment
  was found beyond the intentionally long connected `Again.` tail.

### One-read comprehension

At desktop size the reader understands the complete intended story: the jailer
orders Edmond to eat; Edmond refuses the meal and tomorrow; after the jailer
leaves, a lone scrape comes from the wall; Edmond asks who is there; a double
scrape answers; Edmond demands repetition. The page therefore prepares the
Page 23 contact attempt. M1–M3 remain fidelity/reading-system blockers even
though this causal gist is recoverable.

## Nonblocking notes

- The `Again.` tail is very long and visually prominent. It does connect to
  Edmond's mouth and preserves the corrected reading order, so it is not a
  blocker. The required regeneration should retain ownership while shortening
  or calming the connector if the restored panel proportions permit it.
- Stone, skin, and cloth retain dense ink texture continuous with canonical
  Page 21. Avoid increasing that texture so broad matte color/shadow masses
  remain dominant.

## Disposition

Do not promote v23 or edit canonical pages/the reader. Produce a complete new
Page 22 version that preserves the corrected Panel 4 order, lone Panel 3
scrape, identities, text, style, anatomy, and display comfort while repairing
M1–M3. The next candidate requires a fresh source, desktop, and tablet audit of
the entire page.
