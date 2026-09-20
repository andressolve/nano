# PAGE 12 — builder packet

## Fresh zero-history builder contract

You are a fresh builder for page 12, candidate vK, mode `BASE|TARGETED|FULL_PROMPT_RESET`.
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

## PAGE 12

Dramatic. The field behind the Carmelite convent at noon: long grass, a high wall of yellow stone, one big tree, a stone trough, and a gap in the wall. Athos under the tree, arm in the sling, good hand on the pommel of his grounded sword. The boy arrives, hat off; Athos observes that most boys don't come; the boy says he said he would and that Athos's friends aren't here; they are. Porthos and Aramis come through the gap and stop dead: that's my one o'clock; that is my two o'clock; he's my noon. The three look at one another and laugh, Porthos with his head back, Aramis behind his hand, Athos with one corner of his mouth, and the boy does not laugh; and behind all four, coming through the gap, five red cloaks with white crosses and, in front of them, in black, the scar, who forbids duelling, will take their swords, and will take the Gascon himself. The dominant turn is the three working it out and laughing, and the red cloaks coming round the wall. The reader turns because it is five red against three blue, one of them one-armed, and the scar has just claimed the boy.

## Builder-only page prompt

## PAGE 12 — noon, and five red cloaks

### Reader turn
The three Musketeers discover the boy has challenged all of them and laugh, and the Cardinal's guards come through the wall behind them with the scar in front.

### Ordered moments
1. Panel one, about 25%, a strip: the meadow at noon, Athos on the RIGHT under the big tree, LEFT arm in the sling, good hand on the pommel, sword point on the ground; the boy on the LEFT arriving, hat off. Three balloons A–B–A: Athos upper right, the boy middle left, Athos's two words lower right, clearly third, tails to each mouth.
2. Panel two, about 30%, as single-speaker beats read left to right in a strip cut in three: Porthos on the LEFT stopped dead in the gap in the wall with his line; Aramis in the MIDDLE beside him with his; Athos on the RIGHT under the tree with his. One balloon each, each tail to its own mouth, read left to right.
3. Panel three, the dominant panel, about 45%, close and tall, built as two stacked beats read top to bottom. Upper beat: the three Musketeers in the foreground looking at one another and laughing, Porthos head back, Aramis behind his hand, Athos with one corner of his mouth, the boy among them not laughing; Porthos's whole line, all three sentences in ONE balloon, upper left with its tail to Porthos's mouth, and no other balloon in this beat. Lower beat, clearly below it: through the gap in the yellow wall behind them, five guards in red cassocks with white crosses and, in front of them, Rochefort in black with the red feather, the scar toward the viewer; Rochefort's two lines stacked on the right beside him, the forbidding line above the claiming line, both tails to his mouth, both plainly lower on the page than Porthos's balloon. Porthos's line is never split into two balloons.

### Exact strings
ATHOS: `You came. Most boys don't.`
D'ARTAGNAN: `I said I would. Your friends aren't here.`
ATHOS: `They are.`
PORTHOS: `That's my one o'clock!`
ARAMIS: `That is my two o'clock.`
ATHOS: `He's my noon.`
PORTHOS: `All three of us? In one afternoon? Athos, I like him.`
ROCHEFORT: `Gentlemen. Duelling is forbidden. The Cardinal's guards will take your swords.`
ROCHEFORT: `And the Gascon. I'll take him myself.`

Render exactly these 9 strings once each, in this order, with clear ownership; no other text anywhere on the page.

### Character locks
d'Artagnan, keyed to his sheet: clean-shaven boy, black hair in his eyes, ochre doublet, no cloak, too-long sword. Athos, keyed to his sheet's sling view: tallest, long pale face, dark pointed beard, blue cassock, white plume, LEFT arm in a black sling, hand on pommel. Porthos, keyed to his sheet: enormous, red-brown curls, waxed moustache, no beard, gold-fronted baldric, three red plumes. Aramis, keyed to his sheet: slim, blond curls to the collar, small moustache, lace collar, blue cassock, book at belt. Rochefort, keyed to his sheet: square face, thin black moustache, no beard, a scar from temple to mouth on one cheek, all black, one red feather. The three Musketeers separate by mass, hair colour, and facial hair; Athos and Rochefort separate by beard against moustache, scar, height, blue against black, white plume against red feather. The Cardinal's guards: red cassocks with white crosses, faces turned away, no feather, no scar, silent.

### Consequential exclusions
The field is not attached; draw it from words: a meadow of long dry grass behind a high wall of yellow stone with a gap in it, one big tree, a stone trough by the wall, flat bright noon. ATHOS HAS NO SCAR: his long pale face is unmarked; the one and only scar on the page is Rochefort's, on the man in black with the red feather. A scar on Athos or on anyone but Rochefort is wrong. Constance is absent. No blood; no sword is drawn on this page except Athos's grounded one. The guards stay behind Rochefort and carry no balloons. The trough is present but unfocal. No lettering on the wall or the convent; only the nine spoken strings.

### Approved image inputs
1. `refs/approved/01-dartagnan.png`
2. `refs/approved/02-athos.png`
3. `refs/approved/03-porthos.png`
4. `refs/approved/04-aramis.png`
5. `refs/approved/07-rochefort.png`

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

- Candidate: `qa/production/page-12/candidates/page-12-vK.png`
- Prompt: `qa/production/page-12/prompts/page-12-vK.md`
- Audit: `qa/production/page-12/audits/page-12-vK.md`
- Proofs: `qa/production/page-12/proofs/page-12-vK-600x900.png` and `…-768x1152.png`

Generate with the workspace wrapper, which enforces the manifest, the ceiling
and the billing decision, saves the issued prompt, and derives both proofs:

```
python3 tools/imagegen.py three-musketeers-vol1 12 K --prompt-file PROMPT.md --ref REF1 --ref REF2 …
```

Then run `python3 tools/check_candidate.py three-musketeers-vol1 12 K`.

The audit stays under 180 words and uses exactly these headings:

`## Intent read` — what happens and who owns the page, from the 600 × 900 proof.

`## Exact text check` — exact transcription, or concise discrepancies.

`## Technical facts` — canvas/mode and obvious focal integrity issues.

`## Submission` — `SUBMITTED TO INDEPENDENT CRITIC`.

Return only the five output paths, candidate dimensions/mode, and file hashes.
Do not approve, promote, or write to `pages/`.
