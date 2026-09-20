# PAGE 29 — builder packet

## Fresh zero-history builder contract

You are a fresh builder for page 29, candidate vK, mode `BASE|TARGETED|FULL_PROMPT_RESET`.
Open only this packet and the explicitly listed local image inputs. Do not open
the critic card, another page's packet, another candidate, the full script, or
any prior role task. Never use a rejected candidate as an image input.

Generate with Codex in-app image generation billed to the ChatGPT subscription. Do not use an API key, the bundled image CLI, or any separately billed path.

The exact script strings, page intent, reference manifest, and story facts are
locked. Never edit `07-PAGE-CONTRACT.md` or `08-FULL-SCRIPT.md`. If the
generator will not honour a number, compensate in the prompt and nowhere else.

Generate exactly one completed candidate. Your audit reports whether the
reader-facing intent appears to land; it is a report, not a verdict, and it
never gates submission. **Submit every readable, correctly sized, non-corrupt
candidate to the independent critic — including one you are certain has
failed.** Regenerate before criticism only for a failed *generation*: wrong
canvas, corrupt or truncated output, or gross focal anatomical breakage.
Preserve the failed file and report it. A misspelled string, a wrong speaker, a
weak composition: those are the critic's to call. Write them in your audit and
submit.

Measure nothing. Do not report percentages or pixel sizes in the audit. The
generator undershoots every geometric target it is given and the pages are
fine anyway; a number in the prompt is a steering value, never a spec to audit.

The version ceiling is v6 and the count never resets. You do not
number your own versions; the orchestrator holds the count.

## Shared generation frame

### Canvas and status

One finished, flattened story page, **1024 × 1536 portrait, 2:3**, lettering baked in natively. This is a canonical production candidate for a printed illustrated novel, not a prototype, mockup, sample sheet, spread, or layout study. It is never a montage, model sheet, portrait board, or collage of the attached reference images: the references supply identity and place only, and the output is a new staged scene in which those people act, with the scripted balloons lettered in. Never landscape, never square. No page number, title, production label, speaker name, or editorial text of any kind appears on the page: the only visible text is the exact strings the page prompt lists. **Speaker names are never lettered.** The owner tag beside each exact string (a character's name, CAPTION, PROSE FIELD 1, SOUND, PRINTED OBJECT) says whose balloon or field it is; it is never rendered, never used as a prefix inside a balloon, and never placed beside one. Ownership is carried by placement and tail alone. The strings are listed in reading order and their sequence carries that order; no numeral, letter, bullet, or tag from this prompt is ever lettered on the page.

### Register — *Lantern and Steel*

Lantern and Steel. Brush-and-ink line on warm laid paper with opaque, matte gouache washes: lamp-black line, raw umber and yellow ochre, Prussian blue for the Musketeers, vermilion for the Cardinal, lead white for lace and collars, a little gold. Seventeenth-century France lit like a lantern film: candle and lantern light indoors with real cast shadows and real depth, rain-grey and river-grey outdoors, dust and dawn on the road. Visible brush line, visible paper grain, gouache drying chalky at the edge of a wash; wool, leather, wet stone, steel, and wax. Not smooth prestige-oil realism. No glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no anime proportions, no children's-book softness, no plastic 3D render.

Two colours own the book and oppose each other on every page they share: Musketeer blue (the cassock with the white cross) and the Cardinal's red (his robe, his guards' cassocks, the one feather in Rochefort's hat); d'Artagnan's ochre-yellow belongs to him and his horse alone. The road is ochre, dust, and dawn; Paris is grey-blue slate, brown river, and mud under an overcast sky; the house in the Rue des Fossoyeurs and the inns are warm candle and lantern light against blue-dark streets; the Carmelite field is flat bright noon on long grass and yellow stone; the quay at Calais is grey sea, wind, and spray. Two locations must look like a different world: the Cardinal's study (red hangings, black desk, one candle, no window, no daylight ever) and Buckingham's palace (white, gold, and mirror, no shadow anywhere). The Louvre ballroom is gold and a thousand candles with one column of red in it.

### The lettering law — construction numbers for the builder

Outer safe margin 64 px on every side; no essential text below 72 px from the bottom edge; minimum panel gutter 24 px; no balloon, caption, or prose field crosses a panel border. Speech lettering 44–50 px tall, short replies 48–54 px, **never below the 40 px floor**; comfortable balloon width 240–390 px; at most about 24 words in one balloon; warm ivory balloon fill, restrained dark painted outline; tails end in open space beside the speaker's mouth; silent figures get no balloon and no tail fragment. Illustrated-prose fields: lettering 36–42 px, 38–52 characters per line, paragraphs of 2–5 lines, one or two fields per page at 78–88% of the canvas width, at least 42 px internal padding, a matte parchment field in the page's palette, left-aligned with a calm ragged right edge, never over faces, hands, busy art, maps, or documents. Captions and sound cues use the same family, simplified and enlarged. One restrained editorial lettering family at three levels: speech (large, upright, hand-lettered mixed case), narrative prose (legible literary serif), small sound or object label. **Dialogue face, every page, no exceptions:** rounded hand-lettered upright mixed case, warm and slightly irregular, inside organic oval balloons with soft outlines; never a serif, never italic, never a typeset book face, never a rectangular or rounded-rectangle box. The only serif on any page is the prose field. Banned: condensed comic-display faces, geometric UI fonts, cursive body text, all-capital prose, distressed letterforms, thin old-style italics, tiny handwritten documents carrying facts. These numbers steer the generator; the only text test at the gate is whether every string reads from the **600 × 900** proof.

### Hierarchy and staging

One dominant image plainly owns the page; the share named in the prompt is a construction target, and the generator should build a clear hierarchy rather than a stack of equal bands. When the page's turn is a quiet beat (an answer, a sentence, a face changing) and another panel carries action or a crowd, the quiet panel is still the largest image on the page by far, close and tall, and the busy panel is a shallow strip seen from far back with small figures; this generator favors action tableaux and must be told otherwise. At most two small reaction insets unless causality needs a strip. A clear top-to-bottom reading path. The first speaker in a panel stands on the LEFT; opposed speakers stand on opposite sides with each balloon on its owner's side; in a three-line exchange, A upper on A's side, B middle on B's side, A's second line lower on A's side; a reply is never readable before the line that prompts it and sits clearly lower than it, never level. Every balloon's tail ends beside its own speaker's mouth; a tail into open space, into a crowd, or toward an animal is a defect. Every visible speaker's mouth is visible and its tail corridor is clear of hands, props, and bystanders. Any exchange of two short lines in one panel where either line could plausibly be spoken by either character (a question and its answer, a check and its confirmation, a one-word address) is staged as two single-speaker beats, the questioner alone with mouth visible and the balloon beside that mouth, then the answerer alone the same way, as stacked strips or a strip cut into two panels read left to right; a shared two-shot with crossing tails is the most common attribution failure on this generator. A focal action uses exactly two hands, named. Consequential objects that the story counts (five of something, three of something) are drawn in a spaced row so the reader can count them, and the prompt says "count them". Sound cues render the exact letters given, with no added punctuation or extra words; the run length of a repeated letter is not a defect. Words painted on a story object (a banner, a plaque, a sign) are object text: they must read exactly as scripted, and the same object seen in two panels may carry them twice. Nothing else is lettered: no laugh lines, no invented captions, no labels. Vertical accumulation for time, consequence, descent, isolation, aftermath. Unnamed figures never carry a complete reserved identity stack: The Cardinal's guards wear the red cassock with the white cross and plain steel morions or wide hats with no feather, faces generic and turned away, never a scar; other Musketeers in the street wear the blue cassock and are clean-shaven or full-bearded, never a dark pointed beard, never a red-brown waxed moustache, never blond curls; innkeepers, stable boys, and sailors are bareheaded and aproned; the sergeant at Calais is a red cassock with a paper in his hand; the court at the ball is gold and silver silk and nobody in it wears red, ochre, or a black doublet; the Queen is a figure in white and silver with a small crown, seen from behind or at a distance, face never close; the King is a crowned figure seated on the dais, no face; the jeweler is an old man at a bench with a loupe. No background man is beardless and black-haired in ochre. No background man has a scar. No background figure ever carries a balloon.

### How each kind of input binds

Attached character sheets are identity locks: the face, build, posture, costume state, and habitual gesture on the sheet are reproduced exactly, and the prompt's lock clause names which traits must survive at page scale. Setting plates bind architecture, palette, light logic, and the location's accent; they carry no figures, and the page adds the people. Object plates bind the state and silhouette of consequential objects. **Promoted pages are never attached as inputs:** a lettered page is a copy target for this generator (Volume I's page 3 reproduced page 2 wholesale), and continuity across the page turn rests on the sheets and plates, which is what the locks are for. Boards are never inputs. The model draws what it is shown: never attach a lookalike as a negative example, never attach a rejected candidate.

### Image generation path

Generate with Codex's built-in image generation on the ChatGPT subscription. Do not use an API key, the bundled image CLI, or any separately billed path.

## Page intent

## PAGE 29

Dramatic. Dusk, a stone bridge over a brown river. At the far end, men with picks and a line of stones dragged across the road; the three riders slowing. Aramis: road workers at dusk with their picks pointed at us; as the Fathers tell us, no. The horses drive through the gap in the stones; the men swing; Aramis's horse goes down on the planks and Aramis rolls clear onto his feet, sword out, the lace handkerchief already wound round his hand; the other two horses are through and beyond; six men close on the one in blue. Go on, both of you, don't turn around; Aramis, there are six of them; six, and a bridge is narrow, so they come one at a time; I'll hold the road, go. The dominant turn is Aramis's horse going down and Aramis choosing the bridge. Aramis owns the page. The reader turns because Aramis is holding a bridge alone against six and you are riding away from him. The road workers are scenery with picks; the horse is not hurt.

## Builder-only page prompt

## PAGE 29 — I'll hold the road

### Reader turn
An ambush on a bridge at dusk brings Aramis's horse down, and he sends the other two on and turns to hold the bridge alone against six.

### Ordered moments
1. Panel one, about 30%, wide: the stone bridge at dusk, the brown river beneath, the three riders on the LEFT slowing; at the far RIGHT end a line of stones across the road and six men with picks behind it, faces shadowed. Aramis's single line beside him, tail to his mouth.
2. Panel two, the dominant panel, about 45%, tall: the moment on the bridge: the men swinging; Aramis's horse going down on the planks in the centre, unhurt, Aramis rolling clear onto his feet on the RIGHT with his slim sword out and the white lace handkerchief wound round his sword hand; the other two horses through the gap and beyond on the LEFT. Put d'Artagnan nearest the viewer at lower left, twisted in the saddle and looking back in clean profile, with his mouth fully visible above the horse's neck and clear of hat brim, mane, and the other rider; Athos is farther away and carries no balloon. The sound cue sits at the horse on the planks. Aramis's shout is upper right with its tail visibly meeting his mouth; after it, place the boy's cry immediately beside his visible face at lower left with a short direct tail visibly meeting his mouth, never the horse, his back, or empty air.
3. Panel three, about 25%, close: Aramis alone with his back to the bridge rail on the RIGHT, calm, two fingers of his free hand at his moustache, the handkerchief on his sword hand; six men crowding in from the LEFT, small and faceless. Aramis's long line beside him, tail to his mouth.

### Exact strings
ARAMIS: `Road workers. At dusk. With their picks pointed at us. As the Fathers tell us: no.`
SOUND: `KRAK`
ARAMIS: `Go on! Both of you! Don't turn around!`
D'ARTAGNAN: `Aramis! There are six of them!`
ARAMIS: `Six. And a bridge is narrow, so they'll have to come at me one at a time. I'll hold the road. Go!`

Render exactly these 5 strings once each, in this order, with clear ownership; no other text anywhere on the page.

### Character locks
d'Artagnan, keyed to his sheet: eighteen, long narrow face, sharp chin, long straight nose, close-set quick dark eyes, clean-shaven with no moustache, black unruly hair in his eyes, lean and narrow-shouldered, weight forward, one hand on a plain swept-hilt rapier too long for him; faded ochre-yellow doublet, brown breeches and boots, grey felt hat with one broken feather, no cloak (default state, pp 1–32; road-dusty from page 28, mud to the waist from page 33). Athos, keyed to his sheet's default views: thirty, the tallest man in the book, long pale face, hooded level grey eyes, lines beside the mouth, dark hair straight to the shoulder, a short pointed dark beard and neat moustache, lean; blue cassock with the white cross over a black doublet, black hat with one white plume; NO sling (default state, pp 18–49); hands folded on the pommel of his grounded sword when still; the one man in any panel not moving. Aramis, keyed to his sheet: twenty-four, slim, fine oval face, small straight nose, large dark eyes, pale skin, fine blond curls to the collar always in order, a small neat blond moustache and lip tuft, no beard; weight on one hip, two fingers at his moustache; immaculate blue cassock with the white cross over dove grey with a wide white lace collar, black hat with one white plume, slim silver-hilted sword, a small book at his belt. The risky pair by presence is Aramis against the absent Buckingham; keep Aramis slim, in blue serge with the lace collar, curls to the collar only, so he can never be taken for the golden Duke. The six road workers: rough coats, picks, faces shadowed or turned, no cassocks, no feathers, no scars; silent.

### Consequential exclusions
d'Artagnan and Athos are not attached: they are mounted riders drawn from words, the boy clean-shaven in an ochre doublet and grey hat on a tall bay, Athos tall with a dark pointed beard in a blue cassock and white plume on a dark horse; both are on horseback in every panel and never dismount. Nobody stands in a group; this is an ambush on a bridge with horses moving. Porthos is absent from this page (he stayed at Chantilly); Constance, Rochefort, the Cardinal, and Buckingham are absent. Athos has no sling. No blood; the horse goes down and is not hurt; no blade touches anyone. Exactly six men. The handkerchief carries a small monogram, no legible letters. No lettering on the bridge; only the four spoken strings and the one sound cue.
In panel two, d'Artagnan's warning must have a short unambiguous tail touching his visible mouth; no tail may end on a horse, body, or empty space.

### Approved image inputs
1. `refs/approved/04-aramis.png`
2. `refs/approved/set-beauvais-bridge.png`

Attach only these images.

## Version and revision mode

The orchestrator supplies the exact candidate version and one mode:

- `BASE`: use the shared frame and builder-only prompt as issued.
- `TARGETED`: open only the most recent issued prompt and the latest validated
  critic report, at the paths the orchestrator gives you. Change the prompt only
  for the cited criteria and preserve the successful reader facts the report's
  blind read recorded. Do not add unrelated improvements. Never attach the
  rejected image.
- `FULL_PROMPT_RESET`: do not open any earlier issued prompt or rejected image.
  Rewrite the complete generation prompt and composition strategy from this
  packet plus the compact validated findings the orchestrator gives you.
  Preserve exact strings, intent, story facts, and this reference manifest.
  You may rethink framing, staging, hierarchy and panel grammar. You may not
  change the page count, the text, or the card.

Write the exact complete prompt sent to image generation as the issued prompt.
Do not edit this packet, the intent, or critic material.

## Issued paths

- Candidate: `qa/production/page-29/candidates/page-29-vK.png`
- Prompt: `qa/production/page-29/prompts/page-29-vK.md`
- Audit: `qa/production/page-29/audits/page-29-vK.md`
- Proofs: `qa/production/page-29/proofs/page-29-vK-600x900.png` and `…-768x1152.png`

Generate with the workspace wrapper, which enforces the manifest, the ceiling
and the billing decision, saves the issued prompt, and derives both proofs:

```
python3 tools/imagegen.py three-musketeers-vol1 29 K --prompt-file PROMPT.md --ref REF1 --ref REF2 …
```

Then run `python3 tools/check_candidate.py three-musketeers-vol1 29 K`.

The audit stays under 180 words and uses exactly these headings:

`## Intent read` — what happens and who owns the page, from the 600 × 900 proof.

`## Exact text check` — exact transcription, or concise discrepancies.

`## Technical facts` — canvas/mode and obvious focal integrity issues.

`## Submission` — `SUBMITTED TO INDEPENDENT CRITIC`.

Return only the five output paths, candidate dimensions/mode, and file hashes.
Do not approve, promote, or write to `pages/`.
