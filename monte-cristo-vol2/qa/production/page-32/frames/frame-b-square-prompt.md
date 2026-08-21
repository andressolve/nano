# Page 32 — Frame B square-safe production prompt

Use case: illustration-story
Asset type: canonical production graphic-novel component raster; Page 32 dominant lower-panel art; fresh square generation, not a prototype, proof sheet, page, spread, edit, repair, or assembled 1024 × 1072 panel

## Inputs

Use only these generation inputs:

1. `refs/approved/05-haydee.png` — Haydée identity, costume, and silhouette only.
2. `refs/approved/03-fernand-1838.png` — Fernand identity and heavy decorated silhouette only.
3. `refs/approved/19-set-chamber.png` — approved architecture and material only.
4. `refs/approved/21-objects.png` — approved folded document and red wax seal only.
5. `pages/page-31.png` — canonical continuity for the exact hall, cold high daylight, crimson bench value, dark oak, gilded plaster, far-end bar, and Velvet Cinema finish.

Use no other input image. In particular, do not open, attach, inspect, imitate, edit, crop, or use `qa/production/page-32/frames/candidates/frame-b-v1.png`, either of its proofs, or any other rejected Page 32 candidate or proof as a generation input. The only retained evidence from that failed generation is nonvisual file metadata: the built-in tool returned a 1254 × 1254 RGB PNG when asked for 1024 × 1072.

## Primary request and square geometry

Generate one finished, flattened, square RGB panel illustration, requested at 1024 × 1024. Compose natively for a 1:1 square with no outer border, matte, lettering, or internal panel division. The complete square is final story art; keep all required content comfortably inside it and do not rely on later cropping, outpainting, extension, or repair.

If the built-in tool returns a different square pixel dimension, the builder may preserve that output as the raw result and uniformly scale the complete square once to exactly 1024 × 1024. No crop or nonuniform stretch is permitted. The approved 1024 × 1024 square will later be centered unchanged inside the fixed 1024 × 1072 lower rectangle, with deterministic 24-pixel matte bands above and below supplied by assembly. Do not draw those bands into the generated square.

## Scene and exact story

The same enormous 1838 parliamentary hall as canonical Page 31, seconds later: heavy gilded plaster, dark waxed oak, deep crimson baize benches, tiers receding in strong perspective, and cold high daylight from above. The complete distant back doorway is open.

Exactly two human figures exist in the entire square:

1. **Haydée:** the only woman and only doorway figure. Show one small, solitary, full figure standing inside and fully enclosed by the complete distant open doorway. The lintel, both jambs, both open door leaves, and threshold must all be visible around her. She is remote—about one-tenth to one-eighth of the square height, never a foreground or midground portrait. Preserve her approved cues at architectural distance: age 27, slight loose vertical silhouette, olive-gold skin, long unbound black hair, deep crimson-and-gold Epirote open long coat over a straight pale underdress, no corsetry, no French 1838 waist, coiffure, bonnet, or hat. Her direct stillness, full body, and both feet are visible.
2. **Fernand:** the only man. Show exactly one tiny remote figure at the far end, physically anchored to the parliamentary bar and partly hidden behind its dark-oak/brass rail. He is much smaller and less prominent than Haydée, readable through a compact heavy black silhouette, moustache mass if visible, and one minute restrained decoration glint—not through a portrait face. No second black-coated person exists anywhere.

## Key object at final proof scale

Haydée alone holds one large pale folded document in one hand down by her side. Keep the packet entirely outside her crimson silhouette and against a clean dark doorway value. Affix one saturated, high-chroma red wax seal to the visible outer fold as a distinct red disk with a tiny highlight and dark rim. The pale packet and red seal must remain unmistakably separate but connected physical details at the isolated 600 × 600 square proof and at the assembled 600 × 900 whole-page proof. Achieve this with value contrast, a clean silhouette, saturation, and uncluttered placement. Do not enlarge Haydée beyond the remote architectural scale.

## Composition

Use a remote elevated architectural establishing view, never a character portrait. The vast hall and long empty tiers dominate. Strong receding bench rails and a long uninterrupted floor or aisle establish great distance between doorway Haydée and tiny far-end Fernand. Haydée stays visibly inside the complete doorway, not in front of it or between giant cropped door leaves. Fernand stays at the extreme far bar and remains partly bar-occluded. The architecture supplies spectacle; both figures remain small.

Because the generated component is square, use the added horizontal breadth for empty architecture, receding tiers, and distance—not for extra people, a larger Haydée, a nearer Fernand, or a second focal vertical. Keep the full doorway and both required figures away from the extreme top and bottom edges so the square remains compositionally complete without the assembly mattes.

## Style, light, and color

Velvet Cinema painterly realism: layered matte gouache and opaque watercolor over sparse charcoal and ink construction; broad visible brushwork; bold charcoal/ink edge language and shadow masses; tactile crimson baize, waxed dark oak, heavy gilded plaster, gold thread on wool, old handled paper, and wax. Use selective hard edges only at the complete doorway, Haydée's small silhouette, the pale packet/red seal, and the tiny bar figure. Avoid smooth prestige-oil realism, glossy concept art, airbrushed skin, engraved cross-hatching, and children's-book softness.

Use the same cold high daylight as Page 31 and a solemn, charged stillness: a small solitary witness commanding an enormous chamber through presence, not physical scale. Match Page 31's deep oxblood-crimson benches, near-black coats, dark waxed oak, restrained old gold, cool pale skylight, and charcoal/ink edges. Haydée's crimson must match or rhyme with the bench crimson. Keep the document pale and the wax seal saturated red without warming the daylight.

## Zero-text and exclusion lock

Text (verbatim): none. Zero strings. No balloons, captions, prose fields, speech, title, date, sound word, signature, page number, signage, labels, watermark, handwriting, document marks, or lettering anywhere. The folded paper is visually blank except for the red wax seal.

Exactly one Haydée, exactly one Fernand, exactly two live human figures total. No crowd, guard, attendant, official, witness, silhouette, gallery person, second woman, duplicated Haydée, duplicated hand, Count, Albert, Mercédès, Beauchamp, Villefort, Danglars, soldier, or other human vertical. No conspicuous black standing figure, person-shaped black column, Count-like silhouette, portrait-scale Fernand, foreground Fernand, central Fernand, or person behind Haydée. No cropped doorway, heroic near-threshold Haydée, enlarged Haydée, loose seal, missing document, document carrier, weapon, torch, candle, warm light, readable marks, generated matte, outer frame, or text. Architectural sculpture, if retained from the approved hall, must be unmistakably gilded fixed sculpture and never resemble a live human presence.

## Downstream integrity rule

The square raster must contain every final story pixel for Frame B: both figures, complete doorway, document, seal, hall, and bar. Later processing may only preserve the raw square, uniformly scale the complete square to exactly 1024 × 1024 if needed, derive whole-image proofs, byte-for-byte promote the independently approved 1024-square component, and place it at the locked assembly coordinates. It may never crop, reframe, repaint, patch, heal, extend, add or remove people or objects, enlarge the seal or Haydée, alter architecture, selectively recolor, or add lettering.
