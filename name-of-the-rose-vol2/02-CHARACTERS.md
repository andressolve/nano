# Characters — The Name of the Rose, Book Two: The Fire

**This is a DELTA against Book One's characters doc.** Read [`~/Documents/nano/name-of-the-rose/02-CHARACTERS.md`](../name-of-the-rose/02-CHARACTERS.md) **first**. The seven character refs and one architectural ref locked in Book One **carry forward unchanged** into Book Two and **must be reused, not regenerated**. This document defines only the new refs and composite refs Book Two needs.

## Reuse from Book One (8 existing refs — do NOT regenerate)

| Ref | Path | Used in Book Two on |
|---|---|---|
| William of Baskerville | `~/Documents/nano/name-of-the-rose/refs/ref_william.png` | P3, P4, P8, P13, P14, P16, P17, P18 (inset), P19, P22 — and in composites `composite_chapter_house_disputation` and `composite_finis_africae` |
| Adso of Melk | `~/Documents/nano/name-of-the-rose/refs/ref_adso.png` | P4, P6, P8, P12 (waking foreground only), P13, P14, P16, P17, P19, P22 — and in composite `composite_finis_africae` |
| Abbot Abo of Fossanova | `~/Documents/nano/name-of-the-rose/refs/ref_abbot.png` | P3, P14 — and in composite `composite_chapter_house_disputation`. Dies offscreen on Day 7 (sealed in passage); no Abbot body on-page. |
| Jorge of Burgos | `~/Documents/nano/name-of-the-rose/refs/ref_jorge.png` | P17, P18 (inset), P19 — and in composite `composite_finis_africae`. Central in the Day 7 finale. |
| Salvatore of Montferrat | `~/Documents/nano/name-of-the-rose/refs/ref_salvatore.png` | P6 (condemnation) — and in composite `composite_condemnation`. Execution summarized in P7 parchment panel; not rendered on-page. |
| Bernard Gui | `~/Documents/nano/name-of-the-rose/refs/ref_gui.png` | P3, P5, P6 — and in composites `composite_chapter_house_disputation` and `composite_condemnation`. Central in Day 5. |
| The village girl | `~/Documents/nano/name-of-the-rose/refs/ref_girl.png` | P6 (condemnation) — and in composite `composite_condemnation`. Execution summarized in P7 parchment panel; not rendered on-page. |
| The Aedificium | `~/Documents/nano/name-of-the-rose/refs/ref_aedificium.png` | Cover, P20 (engulfed at night), P22 (smoking behind William and Adso), P23 (ruins decades later) |

**Pre-flight rule for every page that attaches a reused ref:** Re-Read the actual PNG before writing the prompt. Do not work from memory of Book One. Re-Read happens in every sub-session that touches that character — not once per volume. The Book One P10 slog burned four regens because the agent worked from memory rather than re-Reading `ref_adso.png`; do not repeat that failure.

## New single refs — 4 character refs + 1 artifact ref

These must be built and gated **before** any page generation begins. Same gate criteria as Book One refs.

---

### 1. Old Adso of Melk

**Lock block:**

> **OLD ADSO OF MELK** — Benedictine monk, age about 80, German, writing the manuscript of these events in his cell at the abbey of Melk in Austria, decades after the events of the seven days. Tall and slightly stooped now (a man who was once a slight novice of 18, now an old monk). Long white beard down to his chest, fine and slightly unkempt. Bald on the crown (no longer a tonsure — the hair has gone). Pale skin marked by age spots. Gnarled hands with prominent knuckles, knuckles of the right hand ink-stained. Heavy-lidded eyes, watery but clear-sighted, the same light-grey as the young Adso in `ref_adso.png`. Wears the plain black wool habit of the Benedictine order, dark cloth belt, simple sandals, a small wooden cross on a leather cord at his throat (the same cross he wore as a novice — now darkened by sixty years of wear). Expression concentrated, sad, alive — the look of a man writing about the worst thing he ever saw, and the best thing he ever felt.

**Continuity check (mandatory before generation):** Read `~/Documents/nano/name-of-the-rose/pages/page-01.png` and verify the new ref matches the Old Adso glimpsed inside that page's historiated initial. Same person, same age, same cell, same desk, same quill. If the new ref shows a different Old Adso (wrong beard color, wrong age, wrong habit), regenerate before passing the gate.

**Reference-sheet prompt** (generates `refs/ref_old_adso.png`):

> Reference sheet, 3:2 landscape (1536×1024), painted in oil-painting realism, muted palette, plain warm-grey background, soft single light from the upper left. Two studies of the same man side by side, full-page composition.
>
> LEFT half: full-body portrait standing in the black Benedictine habit, the small wooden cross at his throat, slightly stooped posture with the upright dignity of a man who has spent sixty years standing for prayer eight times a day. Hands clasped at his waist, the gnarled knuckles and ink-stained fingertips of the right hand visible.
>
> RIGHT half: seated three-quarter view at a small oak writing-desk, quill in his right hand, a sheet of cream vellum before him, the same beeswax candle and small round-arched window high in the wall behind him that appear in Book One P1's historiated initial. Concentrated, sad, alive expression. Long white beard catching the candlelight.
>
> [OLD ADSO lock block — paste verbatim above.]
>
> NOT a children's book. Serious mature graphic novel, realistic proportions, natural lighting. NO halftones, NO cel shading, NO ink linework. Painted brushwork. No text, no labels, no captions, no border.

---

### 2. Remigio of Varagine

**Lock block** (lifted from Book One's description-only block and expanded into a full lock):

> **REMIGIO OF VARAGINE** — Benedictine monk, the abbey's cellarer (head of kitchens and supplies), age about 50, Italian. Heavy-set, broad-shouldered, broad-bellied, double-chinned, the body of a man who has lived comfortably off the abbey's pantry for thirty years. Round fleshy face, small shrewd watchful eyes, dark cropped hair around the tonsure with grey at the temples, smooth-shaven jowls. Skin ruddy. Wears the black wool habit of the Benedictine order straining slightly at the belt, a small iron key-ring at his hip (smaller than Malachi's — Remigio's keys are for the cellars and storerooms, not the library). A small worn wooden cross at his neck. Expression usually watchful and accommodating in public — the cellarer of a great abbey is a politician — but the watchfulness becomes fear in private. He is a former follower of the heretic **Fra Dolcino**, hiding his past behind comfortable service. Salvatore is his weak point.

**Reference-sheet prompt** (generates `refs/ref_remigio.png`):

> Reference sheet, 3:2 landscape, painted in oil-painting realism, muted palette, plain warm-grey background, late-afternoon warm kitchen-light from one side.
>
> LEFT half: full-body portrait standing in the black Benedictine habit straining slightly at the belt, the iron key-ring at his hip, hands clasped at his waist. Posture upright, slight forward lean of a man used to receiving instructions and giving them. Wooden cross at the throat.
>
> RIGHT half: head-and-shoulders portrait, three-quarter view, watchful expression — the cellarer measuring a stranger. Small shrewd dark eyes, double-chin visible, ruddy complexion.
>
> [REMIGIO lock block — paste verbatim above.]
>
> NOT a children's book. Serious mature graphic novel, realistic proportions, natural lighting. NO halftones, NO cel shading, NO ink linework. Painted brushwork. No text, no labels, no border.

---

### 3. Malachi of Hildesheim

**Lock block** (lifted from Book One's description-only block and expanded into a full lock):

> **MALACHI OF HILDESHEIM** — Benedictine monk, the abbey's chief librarian, age about 50, German. Very tall (~6'2"), gaunt, long-jawed, hollow-cheeked, deep-set dark eyes under heavy brows, sparse dark hair around the tonsure going grey at the temples, thin pressed mouth. Skin pale and slightly waxen — a man who lives indoors and rarely sees direct sun. Long-fingered ascetic hands. Wears the black wool habit of the Benedictine order, dark cloth belt, a **heavy iron ring of keys at his belt** (his identifier in any scene — the keys to the library, the catalogue cabinet, and the hidden stair). A small dark wooden cross at his throat. Posture upright but slightly bent forward at the shoulders, the body language of a man who has been carrying a secret for a long time. Always watching. Speaks reluctantly. Controlled by Jorge for decades; dies on Day 6 of the same poison that killed Venantius and Berengar.

**Reference-sheet prompt** (generates `refs/ref_malachi.png`):

> Reference sheet, 3:2 landscape, painted in oil-painting realism, muted palette, plain cool-grey background, the cold flat daylight of the scriptorium.
>
> LEFT half: full-body portrait standing in the black Benedictine habit, slightly bent at the shoulders, the heavy iron ring of keys prominent at his belt, long-fingered hands clasped in front. Tall and gaunt.
>
> RIGHT half: head-and-shoulders portrait, three-quarter view, deep-set dark eyes under heavy brows, hollow cheeks, the suspicious watching expression. Sparse dark tonsured hair going grey at the temples.
>
> [MALACHI lock block — paste verbatim above.]
>
> NOT a children's book. NO halftones, NO cel shading, NO ink linework. Painted brushwork. No text, no labels, no border.

---

### 4. Severinus of Sankt Wendel

**Lock block** (lifted from Book One's description-only block and expanded into a full lock):

> **SEVERINUS OF SANKT WENDEL** — Benedictine monk, the abbey's master herbalist and infirmarian, age about 55, German. Medium build, weathered hands stained with plant dyes (faint blue, green, ochre marks on the knuckles and fingertips), neat short grey beard, short grey tonsured hair, kind direct hazel eyes, faint smile lines at the corners of the mouth. Skin tanned for a monk — Severinus walks outdoors collecting plants. Wears the black wool habit of the Benedictine order with a heavy **brown leather apron** worn over it when working (the apron is his identifier — the only monk in the abbey who routinely covers his habit with a leather apron). A small wooden cross at his throat. Posture relaxed, the calm of a man who works with quiet attention. The friendliest monk in the abbey. Murdered on Day 5 in his herbarium.

**Reference-sheet prompt** (generates `refs/ref_severinus.png`):

> Reference sheet, 3:2 landscape, painted in oil-painting realism, muted palette, plain warm-grey background, soft warm light as from the single oil lamp in the herbarium.
>
> LEFT half: full-body portrait standing in the black Benedictine habit with the heavy brown leather apron worn over it, hands at his sides showing the stained knuckles and fingertips, a small bundle of dried herbs held loosely in one hand. Relaxed upright posture.
>
> RIGHT half: head-and-shoulders portrait, three-quarter view, the calm direct hazel eyes meeting the viewer, faint smile lines at the mouth, neat grey beard catching the warm lamp light.
>
> [SEVERINUS lock block — paste verbatim above.]
>
> NOT a children's book. NO halftones, NO cel shading, NO ink linework. Painted brushwork. No text, no labels, no border.

---

### 5. The Aristotle codex — artifact ref

**Lock block:**

> **THE ARISTOTLE CODEX (Aristotle, *Poetics*, Book II — the lost treatise on comedy)** — a vellum codex of about 80 leaves, bound in dark brown leather over wooden boards, brass clasps at the fore-edge, slightly worn at the corners from centuries of careful handling. When closed: a plain leather face with no title (medieval codices did not have spine titles), brass clasps visible. When open: two facing vellum leaves, each ruled into TWO columns of Greek text written in 14th-century **Greek minuscule script** (small, even, neatly spaced — copied by a skilled scribe). The Greek is **attested opening lines of the existing *Poetics* Book One**, used here as a stand-in since Book II is lost in real history; the script will provide the verbatim Greek string for the page where the codex is open. **The corners of two facing pages are faintly dark-stained** — the contact poison Jorge has painted into the corners so that anyone wetting a finger to turn the page dies. The stain is subtle, the kind of mark a casual reader would dismiss as old water damage. A small reading-stand of dark oak, plain, set on a stone surface in candlelight.

**Reference-sheet prompt** (generates `refs/ref_aristotle_codex.png`):

> Reference image, 3:2 landscape, painted in oil-painting realism, muted palette, dim candlelight from one side throwing the codex into soft chiaroscuro, plain dark stone surface beneath.
>
> Two views of the same codex, side by side full-page composition.
>
> LEFT half: the codex CLOSED on the reading-stand, plain dark brown leather face, brass clasps engaged at the fore-edge, slight wear at the corners. Set at three-quarter angle so the spine and the fore-edge are both visible.
>
> RIGHT half: the codex OPEN on the reading-stand, two facing vellum leaves visible, each ruled into two columns of 14th-c. Greek minuscule script, the text small and even, the corners of both pages faintly dark-stained at the fore-edge (a subtle gum-stain that does not call attention to itself but is visible). Candlelight catches the vellum and the gold-tooled edge of the binding.
>
> [ARISTOTLE CODEX lock block — paste verbatim above.]
>
> NOT a children's book. NO halftones, NO cel shading, NO ink linework. Painted brushwork. No text on the binding, no labels in the image, no border. The Greek script on the open pages is artwork; it does NOT need to be a real legible passage at this ref-sheet stage (the readable Greek text will be specified verbatim in the P18 primary-source-page prompt).

---

## Composite reference plates — 3, built upfront

Per the Book One retrospective RULE 1: **any page with 3+ named cast members must be generated against a composite reference plate, and the composites must be built BEFORE first page generation, not as a panic-fix on audit.** Three composites for Book Two:

### Composite 1 — `refs/composite_chapter_house_disputation.png`

**Used by:** P3 (Day 5 disputation in the chapter house — William speaks for the Franciscan position on Christ's poverty; Bernard Gui and the Abbot listen). Possibly P14 (Abbot defies William's investigation in the Abbot's chamber, depending on framing).

**Reference input:** Use all three refs directly if the current image tool supports multi-reference editing: `ref_william.png`, `ref_abbot.png`, and `ref_gui.png`. If the tool path only accepts one reference, anchor on `~/Documents/nano/name-of-the-rose/refs/ref_gui.png` because Bernard Gui is the only real-historical figure in the cast and gpt-image-2 can drift toward stock-photo Wikipedia portraits if his face is not anchored verbatim.

**Procedure (mandatory before generation):**
1. Re-Read `ref_gui.png`. Write a one-line verbatim observation into the working notes: *"looking at ref_gui.png: tall lean upright Dominican, white tunic + long white scapular + black mantle + hood, iron-grey neat tonsure, hooked aquiline nose, pale grey-green unblinking eyes, leather-bound Practica book at hip, silver cross on black cord."*
2. Re-Read `ref_william.png`. Write a one-line verbatim observation: *"looking at ref_william.png: tall gaunt English Franciscan ~50, brown wool habit + rope belt with three knots, sandals, reddish-grey tonsure + beard going silver at chin, sharp light-blue eyes, riveted-leather spectacles."*
3. Re-Read `ref_abbot.png`. Write a one-line verbatim observation: *"looking at ref_abbot.png: round-faced well-fed Italian Benedictine ~60, fine-cut black habit with dark trim, large gold pectoral cross studded with garnets on heavy chain, enameled ring on right hand, smooth-shaven, smooth grey hair around tonsure."*
4. Compose the composite prompt: horizontal landscape triptych, three full-body figures on one canvas, same painter / same light / same scale, plain warm-grey background. Left: William. Center: the Abbot. Right: Bernard Gui. Each with a thin painted name label below: `Fra Guglielmo` (William's Italian form, period-correct), `Abate Abone` (Abbot Abo's Italian form), `Frate Bernardo` (Gui's Italian form). The labels are for the agent reading the composite later, not for the model rendering downstream pages.
5. Generate/edit the composite at size `1536x1024`, quality `high`, save as `~/Documents/nano/name-of-the-rose-vol2/refs/composite_chapter_house_disputation.png`.
6. Cast-check: all three faces match their single refs? Habits the correct colors (brown / black with gold cross / white-and-black)? Same painter / same light / same scale? Pass the gate before P3 generation.

### Composite 2 — `refs/composite_condemnation.png`

**Used by:** P5 (Bernard Gui interrogates Remigio in the chapter house), P6 (the three condemned — Remigio, Salvatore, the village girl — led across the snowy courtyard under Gui's eye).

**Reference input:** Use all four refs directly if the current image tool supports multi-reference editing: `ref_gui.png`, `ref_remigio.png`, `ref_salvatore.png`, and `ref_girl.png`. If the tool path only accepts one reference, anchor on `~/Documents/nano/name-of-the-rose/refs/ref_gui.png` for the same reason as composite 1.

**Procedure:**
1. Re-Read `ref_gui.png`, `ref_remigio.png` (just built), `ref_salvatore.png`, `ref_girl.png`. Write a one-line verbatim observation per character into the working notes. Do not skip any.
2. Compose the composite prompt: horizontal landscape **quadtych** — four full-body figures on one canvas, same painter / same light / same scale, plain cool-grey background suggesting the cold chapter-house light. Left to right: Bernard Gui (tall upright Dominican, *Practica* book at hip); Remigio (heavy-set Benedictine cellarer, iron key-ring at hip); Salvatore (short hunched lay-brother, two-color eyes and scar, dirty short habit, bare feet); the village girl (small thin peasant, rag-wrapped feet, patched brown wool dress, brown headscarf, frayed shawl). Painted name labels below each: `Frate Bernardo`, `Frate Remigio`, `Salvatore`, `la giovane` (Italian for "the young woman", since the girl has no name in the story).
3. Generate/edit the composite at size `1536x1024`, quality `high`, save as `~/Documents/nano/name-of-the-rose-vol2/refs/composite_condemnation.png`.
4. Cast-check: all four faces match their single refs? The girl rendered with the restraint already locked in the Book One ref (NOT romanticized, actually thin from hunger, no glamour)? Salvatore's two-color eyes both visible and the scar across the cheek visible? Pass the gate before P5 generation.

### Composite 3 — `refs/composite_finis_africae.png`

**Used by:** P17 (William and Adso enter the *finis Africae*; Jorge is waiting in the candlelight), P19 (Jorge eats the pages, knocks over the lantern, the fire begins). Possibly P16 if the framing benefits from a multi-character composite at the door.

**Reference input:** Use all three refs directly if the current image tool supports multi-reference editing: `ref_william.png`, `ref_adso.png`, and `ref_jorge.png`. If the tool path only accepts one reference, anchor on `~/Documents/nano/name-of-the-rose/refs/ref_william.png` because William's near-bald reddish-grey tonsure and Franciscan rope-belted habit are the most-drift-prone of the three faces.

**Procedure:**
1. Re-Read `ref_william.png`, `ref_adso.png`, `ref_jorge.png`. Write a one-line verbatim observation per character.
2. Compose the composite prompt: horizontal landscape triptych, three full-body figures on one canvas, same painter / same light / same scale, dim candlelight from one side throwing all three into soft chiaroscuro (the *finis Africae* is candlelit and small — composite light should suggest that). Left to right: William (brown Franciscan, spectacles in one hand, satchel crosswise); Adso (slight, black Benedictine novice habit, wax tablet held); Jorge (very tall, slightly bent at the shoulders, white beard to chest, milky blind eyes, leaning on the long pale ashwood staff). Painted name labels below: `Fra Guglielmo`, `Adso`, `Frate Jorge`.
3. Generate/edit the composite at size `1536x1024`, quality `high`, save as `~/Documents/nano/name-of-the-rose-vol2/refs/composite_finis_africae.png`.
4. Cast-check: all three faces match their single refs? Jorge's milky blind eyes prominent and white beard down to chest? Adso looks 18 (not a child, not an adult monk)? William has the riveted-leather spectacles visible? Pass the gate before P17 generation.

---

## Casting checks — gate before any page generation (combined)

For each of the 5 new single refs AND the 3 composite refs, apply the gate criteria from the Book One characters doc PLUS the additional checks above:

**Single refs:**
- [ ] Age right? (Old Adso 80, Remigio 50, Malachi 50, Severinus 55)
- [ ] Habit color right? (Benedictine black for the three monks; the Aristotle codex is a binding, not a habit)
- [ ] Distinctive marker visible? (Old Adso's white beard and gnarled writing hand; Remigio's iron key-ring at hip and double chin; Malachi's heavy iron key-ring and tall gaunt frame; Severinus's brown leather apron and stained hands; the Aristotle codex's faint dark-stained page corners)
- [ ] Register matches Book One refs and Newton / Honda / da Vinci?
- [ ] Period-accurate (no modern artifacts in the artifact ref — vellum + brass clasps + Greek minuscule script)?
- [ ] **Old Adso continuity:** matches the Old Adso glimpsed inside Book One P1's historiated initial?

**Composite refs:**
- [ ] All named characters present and recognizable against their single refs?
- [ ] Same painter / same light / same scale across the composite?
- [ ] Faces oriented forward (three-quarter view, not in profile)?
- [ ] Plain neutral background?
- [ ] Name labels readable as thin painted serif (not modern type, not block lettering)?
- [ ] Habits correctly colored (Franciscan brown vs Benedictine black vs Dominican white-and-black)?
- [ ] Signature accessories on every figure (Gui's *Practica*, Remigio's keys, Salvatore's two-color eyes and scar, the girl's rag-wrapped feet, William's spectacles, Adso's wax tablet, Jorge's ashwood staff)?

If any ref or composite fails, regenerate before proceeding. The composite rule is harder: a drifted single ref poisons every page that uses that single ref; a drifted composite poisons every page in the entire scene group it covers.
