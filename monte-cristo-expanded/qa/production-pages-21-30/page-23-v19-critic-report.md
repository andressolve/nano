# Page 23 v19 — Independent Critic Report

## Verdict

# REVISE

Page 23 v19 repairs both v10 mandatory findings: Panel 3 is now a closed
hairline floor seam and Panel 4 supplies the first clear tunnel opening; every
balloon and essential text field is also inside the locked 64 px outer safe
area. The revised page is still not ready for promotion because the native
lettering is materially below the 40 px minimum and Panel 1 does not show the
scripted ear-to-wall listening action. Both are mandatory whole-page
regeneration issues.

This review was made from the approved Page 23 script, canonical Page 22,
identity/style/object authorities, the typography/readability contracts,
Workflow 29, and the v10 independent report. The builder's prompt, self-audit,
desired verdict, and reported measurements were not used as approval evidence.

## Candidate identity

- Full-resolution candidate:
  `monte-cristo-expanded/qa/production-pages-21-30/page-23-v19.png`
- Full-resolution metadata: 1024 × 1536, 8-bit RGB PNG, no alpha,
  non-interlaced
- Full-resolution SHA-256:
  `7f52c955b4a86303dbe90984c0ef32e1fff8f2fd6f2d86fb5f2a1deca8e1156a`
- Binding desktop proof:
  `monte-cristo-expanded/qa/production-pages-21-30/page-23-v19-desktop.png`
- Desktop metadata: 600 × 900, 8-bit RGB PNG, no alpha
- Desktop SHA-256:
  `911092c5ece163d7708c038a6f5fd8055edf3c495c34fe6a22719b8a03ba4aab`
- Secondary tablet proof:
  `monte-cristo-expanded/qa/production-pages-21-30/page-23-v19-tablet.png`
- Tablet metadata: 768 × 1152, 8-bit RGB PNG, no alpha
- Tablet SHA-256:
  `1cf7dc03d08f25bb45bc758d02e7708942ca338d60039e48d680ce69bf42dbb3`
- Verification: fresh 600 × 900 and 768 × 1152 derivations from the source were
  byte-identical to the supplied proofs.

## Mandatory findings

### M1 — Dialogue lettering is below the locked 40 px minimum

The portrait typography system sets 44–50 px as the normal native speech
target and 40 px as the minimum approved lettering height on the 1024 × 1536
source. Full-resolution inspection of representative lines, including
`Quiet. The guard returns after the bell.`, `I can hear everything except
freedom.`, and the Panel 1 code, places typical glyph height only in roughly
the high-20s to low-30s. At the binding 600 × 900 proof, the same letters reduce
to roughly the mid-to-high teens.

The text remains decipherable, but it is noticeably smaller and less
effortless than canonical Page 22 and fails the explicit native minimum. The
safe-area repair cannot be bought by shrinking the lettering.

Required regeneration behavior:

- Restore all dialogue to a genuine 44–50 px native target, never below 40 px.
- Preserve verbatim text, comfortable leading, generous internal padding, and
  the accepted upright hand-lettered family.
- Keep all balloons and essential text within the 64 px outer safe area.
- Recompose balloon widths, line breaks, figure scale, and negative space as
  needed; do not enlarge or replace text on the existing raster.

This requires complete-page regeneration. No overlay, localized balloon swap,
or typography patch is permitted.

### M2 — Panel 1 does not show Edmond's ear against the wall

The locked first beat is `ear-to-wall code`: Edmond physically listens through
the stone while testing one scrape for yes and two for no. In v19, Edmond is
shown in left profile facing the wall with his nose and mouth toward it; his
visible ear is on the far side of his head, away from the wall, and no ear-wall
contact is shown. The pose reads as speaking toward or looking at the wall,
not listening through it.

Regenerate Panel 1 as part of the complete page with Edmond's ear unmistakably
pressed to the same stone source that carries the tail-free `scrape`. His
mouth must remain visible enough for the code balloon's local tail, and the
speech must still precede the single answering scrape. Do not crop-patch or
replace only the head/panel.

## Prior v10 mandatory-finding verification

### v10 M1 — Crack before tunnel opening: PASS

- Panel 2 shows tool work at a closed floor seam.
- Panel 3 retains only a narrow, closed hairline seam. It contains no black
  cavity, traversable opening, hand, face, body, or silhouette.
- Panel 4 is the first panel to expose a clear black tunnel opening; the large
  displaced/raised slab and Edmond's recoil make it the dominant physical
  change.
- Panel 5 continues from that opening with the silent hand.
- The lines `My tunnel is beneath you.` and `Beneath me?` therefore deliver the
  intended discovery instead of repeating information already shown.

### v10 M2 — 64 px outer safe area: PASS

- The Panel 1 code balloon and `scrape` sit comfortably inside the top, left,
  and right 64 px boundaries.
- The leftmost balloons in Panels 2, 3, and 4 begin just inside the 64 px outer
  boundary; their outlines and essential text remain contained.
- `Regrettably.` is also inset safely, and no bottom text exists in Panel 5.
- No balloon or essential text is cropped or exposed to the reader edge at
  desktop or tablet size.
- This safe-area pass does not cure the separate undersized-lettering failure
  in M1.

## Full regression gate

### Exact text and omission/duplication: PASS

All nine scripted items appear exactly once, in correct order, spelling,
capitalization, and punctuation:

1. `One scrape for yes. Two for no. Are you a prisoner?`
2. `scrape`
3. `Quiet. The guard returns after the bell.`
4. `You can hear the bell?`
5. `I can hear everything except freedom.`
6. `Tell me where to dig.`
7. `Move away from the stone. My tunnel is beneath you.`
8. `Beneath me?`
9. `Regrettably.`

The title, page number, speaker labels, Faria's name, extra dialogue, extra
sound text, and Page 24 material are absent. Panel 5 is silent.

### Five-panel hierarchy and causality: PARTIAL / M2

- The page has exactly five top-to-bottom panels.
- Panel 1 contains the code and its single-scrape answer, but fails the required
  ear-to-wall physical action under M2.
- Panel 2 clearly shows improvised tool work at the mortar/floor seam and
  introduces the guard's bell timing.
- Panel 3 keeps the speaker unseen and the floor closed while Edmond asks where
  to dig.
- Panel 4 is correctly dominant, preserves voice → Edmond → voice order, and
  makes the first clear tunnel opening beneath the lifted/displaced slab.
- Panel 5 is a distinct silent coda with one living hand.

### Speaker lanes, tails, sounds, and silence: PASS

- Panel 1's code balloon points toward Edmond's visible mouth; the single
  lowercase `scrape` is tail-free and embedded at the stone source.
- In Panels 2–4, Edmond's four balloons point toward his visible mouth and
  remain distinct from the unseen source.
- The four voice balloons terminate toward the relevant seam/opening, never a
  visible mouth, the door, Edmond's torso, or the guard.
- Panel 4 preserves the required voice → Edmond → voice A-B-A reading order.
- Panel 5 has no balloon, caption, sound, or readable object text.

### Identity and Page 22 continuity: PASS

- Edmond retains the accepted Prison Edmond identity: deep-set dark eyes,
  strong straight brow, long clean nose, high cheekbones, tangled dark hair,
  rough beard, torn cream linen, worn dark vest, and depleted but alert body.
- His profile, crouching views, bare feet, clothing damage, and body mass
  continue canonical Page 22 without a youth, grooming, costume, or health
  reset.
- The damp mineral cell, closed iron-studded door, floor, and wall palette carry
  Page 22's scrape naturally into the floor investigation.
- Edmond does not drift toward Faria, the jailer, Caderousse, Jacopo, or
  Villefort.

### No-Faria-reveal boundary: PASS

- No face, eyes, white hair, beard, head, shoulder, torso, silhouette, name, or
  lamp reveals Faria.
- Panels 2–4 keep the voice's owner wholly unseen.
- Panel 5 shows one hand and wrist emerging from darkness, with no visible
  owner or second hand.
- Page 24 retains its lamp-first and face-reveal work.

### Period props, setting, and action: PASS

- Edmond uses a crude narrow metal spike at mortar/floor seams; no modern
  drill, tool kit, pristine industrial tool, pickaxe, or anachronistic fixture
  appears.
- Worked seams, grit, damp masonry, the heavy slab, and the closed cell door
  make the action period-credible.
- No guard is shown, so the guard's return remains voice-provided timing.

### Velvet Cinema continuity: PASS

- Mineral black-green, earth brown, rust, worn cream, and restrained amber
  match canonical Page 22 and the accepted Château d'If sequence.
- Matte gouache/opaque-watercolor masses, tactile stone/cloth/skin, broad
  shadow, and selective hard edges remain inside the established Velvet Cinema
  family.
- The page does not make a material photographic, glossy game-art,
  cel-animation, steampunk, or separate-illustrator shift.

### Typography and display comfort: REVISE / M1

- The upright dark hand-lettered family, warm-ivory balloons, restrained
  outlines, padding, and tail forms remain stylistically consistent.
- All text is decipherable at the binding desktop proof and secondary tablet
  proof, with correct order and no clipping.
- The dialogue is nevertheless undersized at source and correspondingly too
  small for the locked effortless-reading standard at normal desktop fit.
- Phone/390 performance was not used as an approval gate, per Workflow 29.

### Anatomy and generation integrity: PASS

- Panel 5 contains one living hand with exactly four fingers and one thumb,
  credible nails, joints, palm, and wrist continuity into the dark opening.
- It reads as purposeful emergence, not a severed, dead, floating, or monstrous
  hand.
- Edmond's repeated face, working/support hands, crouching body, legs, and bare
  feet show no approval-blocking duplication, fusion, extra/missing limb, or
  malformed anatomy.
- The tool, slab, seam, opening, door, balloons, and tails contain no decisive
  broken object or orphan fragment.

### One-read comprehension: PARTIAL / M2

A first-time desktop reader can understand that Edmond states a one/yes,
two/no code; receives one scrape; learns the guard's bell timing; works the
floor with an improvised tool; speaks with an unseen prisoner; discovers the
tunnel beneath him; moves clear as the slab opens; and sees a living hand
emerge. The only visual-action ambiguity is the opening pose: he is not shown
listening with his ear to the wall as explicitly required. The reduced type
also makes this otherwise sound causal sequence less effortless than the
binding mandate allows.

## Nonblocking notes

- Several speech tails end farther from mouths than on canonical Page 22, but
  their directions and ownership remain unambiguous at desktop and tablet
  size. During the mandatory regeneration, keep endpoints as locally adjacent
  to visible mouths as composition allows; this is not a separate blocker in
  v19.
- Surface texture is slightly more insistent than in the Prison Edmond
  reference, but it remains consistent with canonical Page 22. Do not increase
  it further on later pages.

## Disposition

Page 23 v19 is rejected for complete-page regeneration under M1 and M2. This
report does not promote the candidate or edit canonical pages or the reader.
