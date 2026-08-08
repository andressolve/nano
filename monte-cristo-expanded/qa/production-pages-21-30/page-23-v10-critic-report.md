# Page 23 v10 — Independent Critic Report

## Verdict

# REVISE

Page 23 v10 is not ready for promotion. It passes the exact nine-text gate,
speaker/source attribution, Prison Edmond identity, dominant Panel 4, final
hand-only reveal, anatomy, period setting, and normal desktop/tablet reading.
It nevertheless has two mandatory failures: Panel 3 reveals a broad open
tunnel before the scripted stone-shift reveal in Panel 4, and several balloons
breach the locked 64 px outer safe margin. Both require complete-page
regeneration, never patching or local replacement.

This review was made from the approved Page 23 script, canonical Page 22,
identity/style/object authorities, the typography/readability contracts, and
Workflow 29. The builder's prompt, self-audit, desired verdict, and reported
measurements were not used as approval evidence.

## Candidate identity

- Full-resolution candidate:
  `monte-cristo-expanded/qa/production-pages-21-30/page-23-v10.png`
- Full-resolution metadata: 1024 × 1536, 8-bit RGB PNG, no alpha,
  non-interlaced
- Full-resolution SHA-256:
  `ccf68e01155b4c4c40355b7ddda23859bde5d807a20dc6c5b8c44134977755dd`
- Binding desktop proof:
  `monte-cristo-expanded/qa/production-pages-21-30/page-23-v10-desktop.png`
- Desktop metadata: 600 × 900, 8-bit RGB PNG, no alpha
- Desktop SHA-256:
  `5c01a9430b9f045f51cbdbc6472fc4d9062697e88c54192b3b74029f94c4db7a`
- Secondary tablet proof:
  `monte-cristo-expanded/qa/production-pages-21-30/page-23-v10-tablet.png`
- Tablet metadata: 768 × 1152, 8-bit RGB PNG, no alpha
- Tablet SHA-256:
  `071c5f2241c012589f082e637d4a0cbc3604b23e25f33d84b2d4b275fb5fb2e6`
- Verification: fresh 600 × 900 and 768 × 1152 derivations from the source were
  byte-identical to the supplied proofs.

## Mandatory findings

### M1 — Panel 3 preempts the scripted floor-stone reveal

Panel 3 already contains a broad, black, person-width floor opening. It reads
as an exposed tunnel mouth rather than the scripted crack through which the
unseen voice is first heard. That breaks the locked five-step visual engine:
code at wall → mortar/tool work → voice through crack → dominant floor stone
shifts to expose the tunnel → living hand.

The current image makes the later lines `My tunnel is beneath you.` and
`Beneath me?` visually redundant, because the large downward opening is already
plainly visible in Panel 3. It also turns Panel 4 into enlargement of a hole
rather than the page's first decisive revelation that a misdirected tunnel is
beneath Edmond.

Required regeneration behavior:

- Panel 2 may show only the worked mortar seam and improvised tool.
- Panel 3 must keep the owner wholly unseen and show only a narrow floor crack
  or minimally loosened seam capable of carrying the voice; it must not show a
  traversable black cavity or an already open tunnel mouth.
- Panel 4 must be the first panel in which the slab visibly shifts/lifts and a
  clear tunnel opening appears beneath it.
- Panel 5 must then continue from that same new opening with the silent living
  hand.

This requires complete-page regeneration. Do not crop-patch the Panel 3 floor,
replace a panel, or paint over the opening.

### M2 — The 64 px outer safe margin is not respected

The locked portrait typography system requires a 64 px outer safe margin on
every side. In the source image, the Panel 1 balloon begins only roughly
20–30 px from the top and left page edges, with its essential lettering also
starting above the 64 px top boundary. The left balloons in Panels 2, 3, and 4
likewise extend to roughly 25–35 px from the page edge. These are deliberate
outer-page placements, not internal-panel gutter placements.

Nothing is clipped in the supplied proofs, but surviving a particular resize
does not satisfy the production-safe composition contract. Regenerate the
whole page with every balloon and all essential lettering inside the 64 px
outer safe area while preserving the correct speaker lanes and source tails.
Do not shrink the lettering below the 40 px minimum or repair the existing page
by moving/copying balloons.

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

### Five-panel hierarchy and ordering: PARTIAL / M1

- The page has exactly five horizontal panels with functional shares close to
  18% / 19% / 18% / 29% / 14%.
- Panel 4 is correctly dominant and contains the largest physical change.
- Panel 5 is a distinct silent coda.
- Panels 1 and 2 establish code and tool work clearly.
- Panel 3's broad opening breaks the required crack-before-opening progression,
  as detailed in M1.

### Speaker lanes, tails, sounds, and silence: PASS

- Panel 1 reads Edmond's question followed by one tail-free `scrape` at the
  wall, correctly answering yes under the stated code.
- All four Edmond balloons terminate in open space locally beside his visible
  mouth and cannot be assigned to the unseen voice.
- All four voice balloons point to the relevant floor seam/opening rather than
  Edmond, a visible mouth, the door, or empty mid-distance.
- Panel 4 preserves the required voice → Edmond → voice A-B-A reading order.
- No balloon is assigned to the silent hand in Panel 5.

### Identity and Page 22 continuity: PASS

- Edmond retains the accepted Prison Edmond identity: deep-set dark eyes,
  strong straight brow, long clean nose, high cheekbones, tangled dark hair,
  rough beard, torn cream linen, worn dark vest, and depleted but alert body.
- His profile, kneeling views, bare feet, clothing damage, and alertness
  continue canonical Page 22 without a youth, grooming, costume, or body-mass
  reset.
- The same damp mineral cell, closed iron-studded door, floor, and wall palette
  carry forward the Page 22 scrape into the floor investigation.
- Edmond does not drift toward Faria, the jailer, Caderousse, Jacopo, or
  Villefort.

### No-Faria-reveal boundary: PASS

- No face, eyes, white hair, beard, head, shoulder, torso, silhouette, name, or
  lamp reveals Faria.
- Panel 3 keeps the speaker visually absent.
- Panel 5 shows one hand and wrist emerging from darkness, with no visible
  owner or second hand.
- The page preserves Page 24's lamp-first and face-reveal work.

### Period props, setting, and action: PASS

- Edmond uses crude, narrow metal fragments against a mortar/floor seam; no
  modern drill, tool kit, pristine chisel, pickaxe, or anachronistic fixture
  appears.
- Worked mortar, loosened debris, damp masonry, rough slab, and the closed cell
  door make the prison action physically credible.
- No guard is shown, so the guard's return remains voice-provided timing rather
  than a premature visible event.

### Velvet Cinema continuity: PASS

- Mineral black-green, earth brown, rust, worn cream, and restrained amber
  match canonical Page 22 and the accepted Château d'If sequence.
- Matte gouache/opaque-watercolor masses, tactile stone/cloth/skin, broad
  shadow, and selective hard edges remain within the established Velvet Cinema
  family.
- The page does not make a material photographic, glossy game-art,
  cel-animation, steampunk, or separate-illustrator shift.

### Typography and display comfort: PARTIAL / M2

- The upright dark hand-lettered family, warm-ivory balloons, line spacing,
  padding, and sound lettering are consistent and comfortably readable at the
  binding 600 × 900 desktop proof and secondary 768 × 1152 tablet proof.
- No text is cropped, malformed, duplicated, or hidden by a decisive object.
- The outer-safe-area placements fail M2.
- Phone/390 performance was not used as an approval gate, per Workflow 29.

### Anatomy and generation integrity: PASS

- Panel 5 contains one living hand with exactly four fingers and one thumb,
  credible joints, nails, palm, and wrist continuity into the dark opening.
- It reads as purposeful emergence, not a severed, dead, floating, or monstrous
  hand.
- Edmond's repeated face, working hands, kneeling body, legs, and bare feet show
  no approval-blocking duplication, fusion, extra/missing limb, or malformed
  anatomy.
- The tool, slab, opening, door, balloons, and tails contain no decisive broken
  object or orphan fragment.

### One-read comprehension: PARTIAL / M1

A first-time desktop reader can understand that Edmond establishes a one/yes,
two/no code; receives a single-scrape confirmation; learns the guard's bell
timing; works the floor with an improvised tool; speaks with an unseen prisoner;
moves a floor stone; and sees a living hand emerge. However, because a large
tunnel mouth already exists in Panel 3, the reader learns visually that the
source is beneath him before the script's `My tunnel is beneath you.` reveal.
The stone shift therefore does not deliver the intended discovery cleanly.

## Nonblocking notes

- Panel 1 implies listening through its close profile, wall placement, and
  wall-side `scrape`, but the ear-to-stone contact is less explicit than the
  locked panel description. During the required regeneration, making physical
  ear/wall contact unmistakable would strengthen the first beat; this is not a
  separate blocker.
- Surface texture is slightly more insistent than in the Prison Edmond
  reference, but it remains consistent with canonical Page 22. Do not increase
  it further on later pages.

## Disposition

Page 23 v10 is rejected for complete-page regeneration under M1 and M2. This
report does not promote the candidate or edit canonical pages or the reader.
