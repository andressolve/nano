# Page 21 v1 — Subscription ImageGen Production Prompt

Built with the subscription-backed Codex ImageGen path. Every supplied image
is a casting, style, lettering, setting, or continuity reference, not an edit
target.

## Reference roles

1. `monte-cristo/refs/02-edmond-prison.png` — binding Prison Edmond identity:
   same deep-set black-brown eyes, straight strong brow, long clean nose, high
   cheekbones, and slight left-mouth asymmetry as young Edmond; progressively
   gaunt face, rough dark beard, long tangled black hair, and damaged posture.
2. Accepted Page 5 — broad matte-gouache Velvet Cinema finish, warm ivory
   lettering field, and young Edmond facial bones before prison.
3. Accepted Page 8 — stable integrated prose field, causal page rhythm, and
   native lettering.
4. Accepted Page 10 — principal speech-lettering family and finished portrait
   page grammar.
5. Accepted Page 19 — binding Château d'If cell continuity, Edmond's starting
   prison costume and face, the silent distant jailer, brush language, and the
   immediate visual state before the multi-year descent. Accepted Pages 11–20
   were inspected before prompt construction; the five-input tool limit makes
   Page 19 the strongest direct continuity reference for this generation.

## Generation prompt

Use case: illustration-story.

Asset type: one complete finished page for the expanded illustrated-novel
edition of *The Count of Monte Cristo*.

Create a complete new historical graphic-novel page at exactly **1024 × 1536
portrait, 2:3**. Do not edit or collage the references. Use them only to
preserve casting, finish, lettering, setting, and sequence continuity.

Use the locked **Velvet Cinema** finish seen in the accepted pages: mature
historical graphic-novel realism painted in layered **matte gouache and opaque
watercolor** over sparse charcoal and ink construction; broad visible
brushstrokes; simplified interlocking color shapes; bold shadow masses;
tactile damp stone, worn linen, paper, iron, scratched plaster, clay, and weak
window light; expressive anatomically credible faces; selective hard edges at
eyes, mouth, hands, bowl, petition, and wall scratches. Château d'If uses
mineral gray, damp moss, rust, black-green depth, worn linen, and a tiny cold
stripe of daylight with restrained amber near the distant passage. Avoid
smooth prestige-oil realism, glossy game art, airbrushed skin, photographic
lens effects, dense engraved cross-hatching, anime, children's-book softness,
steampunk, pirate shorthand, fantasy-dungeon decoration, and generic grimdark.

Narrative job: make years of failed hope physically and emotionally real
before Edmond gives up eating. This is a **continuous-time illustrated-prose
page**, not four separate prisoners and not a conventional four-panel comic.

Composition and reading path:

- Maintain a 64 px safe outer margin, calm hand-painted border treatment, and
  one unmistakable top-to-bottom reading path. No title, page number, speaker
  label, production note, signature, watermark, or stray text.
- Top 28%: one stable cool gray-beige matte parchment prose field, composed
  before the art. Set the full prose as one calm readable block in a dark,
  upright, highly legible literary serif, mixed case, generous internal
  padding, comfortable line length, and approximately 36–42 px lettering.
  Keep it entirely off busy art. Do not split it into captions.
- Middle 62%: one dominant uninterrupted vertical view of the same Château
  d'If cell across continuous time. Show **exactly four unmistakably successive
  representations of the same Edmond**, descending through the cell from
  earlier hope to final despair. The four appearances must share identical
  facial bones and eyes while hair, beard, gauntness, torn clothing, wall
  scratches, petitions, cold-light stripe, and posture visibly advance in
  chronological order. Use changing light and repeated architecture to make
  clear these are years in one cell, not four men together.
- Successive Edmond 1: nearest Page 19 continuity—still relatively upright,
  dark curls short enough to recall young Edmond, little or no beard, worn
  white shirt and indigo waistcoat still recognizable, listening at the iron
  door and calling outward. No balloon.
- Successive Edmond 2: beard beginning, hair longer, shirt and waistcoat
  thinner, seated writing petitions on crude paper; early scratches occupy
  part of one wall. Petition handwriting is not readable and contains no
  image text.
- Successive Edmond 3: visibly gaunter, rough beard and longer tangled hair,
  abandoned petitions nearby, scratches cover one wall and begin another;
  posture recoils from a distant footstep that no longer promises rescue. No
  balloon.
- Successive Edmond 4, the latest and emotionally dominant figure: same locked
  Prison Edmond face and bones, now very gaunt with rough dark beard, long
  tangled hair, frayed dirty linen and damaged posture. He pushes the food
  away and speaks the page's only balloon. Keep the balloon in the lower-left
  lane on his side, warm ivory with a restrained charcoal-brown painted
  outline; its tail ends only in open space immediately beside his mouth.
- A short, barrel-bodied jailer may pass only as one small silent distant
  silhouette in a narrow doorway slice, with bald crown, ruddy pear-shaped
  face, rust waistcoat, keys, and one-shoulder stoop. He receives no balloon
  and no tail fragment. No other people.
- Bottom 6%: a quiet final consequence strip containing the untouched food
  bowl in cold silence. No text, hand, face, tail, or extra object competes
  with it.

Binding Prison Edmond identity: across all four time states preserve deep-set
black-brown eyes, straight strong brow, long clean nose, high cheekbones, and
the slight asymmetry at the left corner of his mouth. Progress toward the gaunt
rough-bearded long-tangled-haired Prison Edmond sheet. Never drift toward
Faria's white mane, Caderousse's round mass, Jacopo's compact moustached face,
the jailer's bulbous ruddy face, or four unrelated generic prisoners. Do not
give Edmond white or gray hair. Hands must be anatomically credible, with five
fingers where visible; do not duplicate limbs, papers, bowls, scratches, or
figures.

Bake every word below into the finished image **verbatim, exactly once, and in
this order**. No other readable text anywhere. Preserve capitalization,
punctuation, accents, and apostrophes.

Prose field, exact text:

`Edmond counted meals, then days, then winters by the cold stripe of light on his wall. He called for Morrel and Mercédès. He wrote petitions until he no longer expected replies. His hair grew. His clothes thinned. The scratches covered one wall and began another. At first every footstep sounded like rescue. Later he hated himself for hoping. At last, he pushed away his food. If the prison intended to keep him until he died, he would choose the day himself.`

Only speech balloon, exact text:

`No one is coming.`

Final constraints: prose must remain comfortable at 390 px reader width; no
letter may be malformed, missing, duplicated, or substituted. The prose field
must not cover a face, hand, bowl, petition, door, or wall scratches. The
single balloon must unambiguously belong to the latest Edmond. Earlier Edmonds
and the distant jailer remain silent. The bottom bowl remains untouched and
silent. Output only the fully lettered flattened page at 1024 × 1536 portrait.
