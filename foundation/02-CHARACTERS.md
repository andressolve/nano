# Characters — Foundation: The Plan

Locks written from the OBSERVED pixels of the two validated style-test pages, not from imagination. Never put the famous name inside a prompt's lock block — the visual description is the lock.

## GAAL DORNICK (Act 1 POV — P1 done, P2, P3, P4, P7)

**Lock (paste verbatim):**
> Young man in his early twenties, deep brown skin, short tight black curls, large dark earnest eyes, smooth boyish face, slender build, plain charcoal-grey high-collared tunic. Wide-eyed provincial newcomer's energy. Realistic young-adult anatomy, NOT cute, NOT mascot proportions.

**Ref:** `refs/ref_gaal.png` — extract via `edit_image` anchored on `style-tests/test-trantor-airbrush.png` (he is the young man in the right of panel 1 and the close-up of panel 2).

## HARI SELDON (P3, P4 (led away), P5 done, P6, P7; hologram P13–P14)

**Lock (paste verbatim):**
> Elderly man in his late seventies, thin and upright, balding crown with wispy white hair at the temples, deeply lined gentle face, calm knowing faint smile, plain pale-grey high-collared scholar's robe, austere and serene.

**Ref:** `refs/ref_seldon.png` — extract via `edit_image` anchored on `style-tests/test-trial-airbrush-v4.png` (the serene old man in the dock / center panel close-up).

### Seldon HOLOGRAM variant (P13, P14)

**Lock addition:**
> The same elderly man rendered as a luminous pale blue-white hologram, faint glow halo, slightly translucent, seated in a sleek powered wheelchair with a closed book on his lap. He is the only light source in the room.

**Ref:** `refs/ref_seldon_hologram.png` — built via `edit_image` anchored on `ref_seldon.png` (dedicated apparatus ref: the Icarus winged-Daedalus lesson — never fight a recurring apparatus per-page).

## THE ADVOCATE (P5 only — page already done)

No ref needed. Observed for the record: middle-aged man, slicked-back black hair with sharp widow's peak, gaunt angular face, hooked nose, heavy dark brows, ornate navy-blue high-collared imperial uniform with gold braid and epaulettes.

## LINGE CHEN, Chief Commissioner (P6)

**Prose lock (P6 only):**
> The central and eldest of the five commissioners on the high tribunal bench: a lean ancient face, hooded unreadable eyes, thin silver hair beneath a close-fitting dark judicial cap, scarlet-and-gold robe. He speaks with motionless authority; the other commissioners lean back to listen.

**Ref:** `refs/ref_bench_commissioners.png` — a straight PIL crop of the validated P5 page (`p5.crop((0.56w, 0.50h, w, 0.73h))`): the five distinct commissioner faces as actually rendered. QA LESSON (round 2): anchoring P6 on the *whole finished P5 page* preserved the hall but the model reinvented the five faces as clones. Crop the validated group pixels and pass THEM as the ref, with "FIVE CLEARLY DIFFERENT elderly men — reproduce their five distinct faces exactly as shown; do NOT repeat the same face."

## SALVOR HARDIN (Act 2 lead — P8–P15)

**Lock (paste verbatim):**
> Man in his mid-thirties, sandy-brown hair cut short and practical, strong jaw, alert grey eyes, wry confident half-smile, sturdy shoulders; plain dark utilitarian jacket over an open-collared shirt — frontier practicality, no ornament, no uniform.

**Ref:** `refs/ref_hardin.png` — fresh generate (portrait + full body, 3:2, neutral warm background, no text).

## LEWIS PIRENNE (P9, P10, P12, P13–14 background, P15)

**Lock (paste verbatim):**
> Gaunt scholar in his late sixties, high forehead, receding white hair combed straight back, neat pointed white beard, thin disapproving mouth, small round wire spectacles, formal high-collared academic tunic in slate blue with a bronze scholar's clasp.

**Ref:** `refs/ref_pirenne.png` — fresh generate.

## ANSELM HAUT RODRIC (P9 only — prose lock)

> Barrel-chested military aristocrat around fifty, florid face, bristling dark waxed mustache, heavy maroon dress uniform crusted with gold braid and medals, high boots, ceremonial sidearm holstered; swaggering, pleased with himself.

## LORD DORWIN (P11 only — prose lock)

> Soft plump imperial aristocrat, elaborately curled grey-brown hair obviously artificial, fluffy blond sideburns, heavy-lidded amused eyes, pastel lavender-and-gold brocade coat with lace cuffs, holding a small jeweled snuff box delicately in two fingers.

## YOHAN LEE (P12, P15 — prose lock)

> Compact hard-faced man in his forties, close-cropped black hair, watchful narrow eyes, plain dark workman's coat; stands slightly behind the Mayor, arms folded.

## JORD FARA, Board trustee (P10 f2, P12 f2)

**Lock (paste verbatim):**
> Frail trustee around eighty, bald crown with thin white side wisps, clean-shaven deeply wrinkled face, hollow cheeks, prominent ears, anxious watery eyes, slate blue-grey high-collared tunic, stooped posture.

**Ref:** `refs/ref_fara.png` — extracted via `edit_image` from P10's own first rendering (the bald trustee as actually painted = canon; maximally distinct from Pirenne).

QA LESSON (round 2, user-caught): this character was originally an "anonymous elderly trustee" locked in prose only — he rendered as two different old men on P10 and P12 and read as a continuity error. **There is no such thing as "anonymous" in a recurring room. Any character who appears on 2+ pages gets a ref. RELYING ON TEXT PROMPTS FOR CHARACTER LOCK IS NOT ACCEPTABLE** (user directive, 2026-07-05).

## Composite plates (PIL local stitch — method A)

- `refs/composite_act1_gaal_seldon.png` — [ref_gaal | ref_seldon], thin labels "REFERENCE A" / "REFERENCE B". Anchor for P2, P3, P4, P7.
- `refs/composite_act2_hardin_pirenne.png` — [ref_hardin | ref_pirenne]. Anchor for P9, P15.
- `refs/composite_p6_bench_seldon.png` — [bench crop | ref_seldon]. Anchor for P6 (repair).
- `refs/composite_p10_hardin_pirenne_fara.png` — [ref_hardin | ref_pirenne | ref_fara]. Anchor for P10 (repair).
- `refs/composite_p12_hardin_fara.png` — [ref_hardin | ref_fara]. Anchor for P12 (repair).
- Vault pages (P13, P14) anchor on `ref_seldon_hologram`; the Board is background prose (Pirenne named but small — glasses + white pointed beard carry him).

Every plate prompt must include: "This input is a REFERENCE SHEET, not a layout to keep — paint ONE NEW unified single-scene image using the references; do not reproduce the sheet's split layout; ignore any printed labels."
