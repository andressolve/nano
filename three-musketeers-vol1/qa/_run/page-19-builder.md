# PAGE 19 — builder packet

## Fresh zero-history builder contract

You are a fresh builder for page 19, candidate vK, mode `BASE|TARGETED|FULL_PROMPT_RESET`.
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

## PAGE 19

Dramatic, two locations because the jump is the turn: the attic window, and the street below. Night, rain. Above, the boy at the open window in his shirt, cleaning the sword. Below, a cart, a lantern on a bracket, and four men in plain cloaks closing on Constance at her own door, one hand reaching for her mouth, the basket falling; she shouts for help and gets half his name out. He goes out of the window, not the stair: one hand on the sill, the sword in the other, dropping two floors through the rain onto the cart roof with a bang. He lands between the men and the door, sword out, hair in his eyes, and across the street in a dark doorway a fifth figure in black with a red feather stands with his arms folded and does not move. The dominant turn is the men taking Constance and the boy going out of the window. The reader turns because it is one boy, four men, one lantern, and rain.

## Builder-only page prompt

## PAGE 19 — out of the window

### Reader turn
Men seize Constance at her door in the rain, and the boy comes out of the attic window two floors up rather than down the stair.

### Ordered moments
1. Panel one, about 25%, a tall strip that holds both locations: at the top, the boy in a white shirt at the open attic window, sword and cloth in his hands, looking down; at the bottom, in the rain-lit street, a cart, a lantern on a bracket, and four men in plain dark cloaks closing on Constance at the house door on the RIGHT, one hand reaching toward her mouth, her basket falling. Constance's cry beside her, tail to her mouth. The men are silent.
2. Panel two, the dominant panel, about 50%, tall: the boy going out of the window, one hand on the sill, the sword in the other, dropping two floors through the rain toward the roof of the cart, the lantern's light catching him. His one-word shout beside him, tail to his mouth; the sound cue at the cart roof below, large.
3. Panel three, about 25%: the boy landed, on the ground between the four men (LEFT) and Constance at the door (RIGHT), sword out, hair in his eyes, the men turning to him. Across the street behind them, in a dark doorway, a fifth figure all in black with one red feather, arms folded, not moving; his scar catches the lantern. The boy's line beside him, tail to his mouth.

### Exact strings
CONSTANCE: `Let go of me! Help! d'Art—`
D'ARTAGNAN: `Constance!`
SOUND: `WHAM`
D'ARTAGNAN: `Four of you for one girl. Let her go, and it's only four of you for me.`

Render exactly these 4 strings once each, in this order, with clear ownership; no other text anywhere on the page.

### Character locks
d'Artagnan in shirt sleeves (pp 19–21): the same clean-shaven boy, black hair in his eyes, lean, in a plain white shirt with no doublet, brown breeches and boots, no hat, the too-long plain-hilted rapier in his hand; weight forward. Constance, keyed to her sheet: twenty, small and quick, a head shorter than the boy, round face, soft chin, short straight nose, wide-set hazel eyes, dark brows, a scatter of freckles, dark brown curls pinned up under a white linen cap with strands escaping; slight, straight-backed, hands never idle; a plain dove-grey dress with white cuffs and a white apron whose bib carries one small embroidered gold crown; a ring of iron keys at her waist; a covered wicker basket on her arm (default state, pp 17–27); habitual gesture: chin lifted, looking up a stair. Rochefort, keyed to his sheet: forty, square hard face, heavy black brows, a pale scar from the LEFT temple to the corner of the mouth visible in every panel; straight black hair to the collar, a thin black moustache, no beard; compact, weight back, chin up; black doublet, black cloak, black hat with a single red feather, the only colour on him (default state, pp 3–34). (in the doorway across the street, arms folded, still; silent on this page). The four men: plain dark cloaks and hats, faces generic, no feather, no scar, no cassock; silent.

### Consequential exclusions
Athos, Porthos, Aramis, and the Cardinal are absent. No blood; nobody is struck on this page. The boy wears no doublet and no hat. Rochefort does not draw and does not move. The lantern is still lit and on its bracket on this page. No lettering on the house or the cart; only the three spoken strings and the one sound cue.

### Approved image inputs
1. `refs/approved/01-dartagnan.png`
2. `refs/approved/05-constance.png`
3. `refs/approved/07-rochefort.png`
4. `refs/approved/set-house.png`

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

- Candidate: `qa/production/page-19/candidates/page-19-vK.png`
- Prompt: `qa/production/page-19/prompts/page-19-vK.md`
- Audit: `qa/production/page-19/audits/page-19-vK.md`
- Proofs: `qa/production/page-19/proofs/page-19-vK-600x900.png` and `…-768x1152.png`

Generate with the workspace wrapper, which enforces the manifest, the ceiling
and the billing decision, saves the issued prompt, and derives both proofs:

```
python3 tools/imagegen.py three-musketeers-vol1 19 K --prompt-file PROMPT.md --ref REF1 --ref REF2 …
```

Then run `python3 tools/check_candidate.py three-musketeers-vol1 19 K`.

The audit stays under 180 words and uses exactly these headings:

`## Intent read` — what happens and who owns the page, from the 600 × 900 proof.

`## Exact text check` — exact transcription, or concise discrepancies.

`## Technical facts` — canvas/mode and obvious focal integrity issues.

`## Submission` — `SUBMITTED TO INDEPENDENT CRITIC`.

Return only the five output paths, candidate dimensions/mode, and file hashes.
Do not approve, promote, or write to `pages/`.
