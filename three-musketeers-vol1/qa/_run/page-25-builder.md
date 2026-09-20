# PAGE 25 — builder packet

## Fresh zero-history builder contract

You are a fresh builder for page 25, candidate vK, mode `BASE|TARGETED|FULL_PROMPT_RESET`.
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

## PAGE 25

Dramatic. Athos's bare whitewashed room: one chair with Athos in it, one table with Aramis on its edge holding his book, one bed, a single sword on the wall, and Porthos filling the window. The boy stands in the middle holding up the small blue-sealed letter: two days to the sea, a day to London, back by Monday, it can be done, the Cardinal will try to stop him. What does the letter say? I don't know. Good, then nobody can make us tell. Porthos turns from the window delighted: London, he has never once beaten an Englishman. Aramis closes his book: in theory four riders are more than one, in practice the Cardinal will not let four through. Athos: that's why it takes four, so that one arrives. The boy looks from face to face: you haven't asked me why, not one of you. Porthos: why would we, you're going, that's the why. The dominant turn is three men deciding to ride for a reason none of them asks. Porthos gets the line. The reader turns because they are about to say the thing.

## Builder-only page prompt

## PAGE 25 — so that one arrives

### Reader turn
Three Musketeers agree to ride to London for a letter none of them has read, and when the boy notices nobody asked why, Porthos tells him why.

### Ordered moments
This is one continuous conversation in Athos's room, never an arrival, introduction, Paris overview, writing scene, character-sheet montage, or collage. Use four full-width panels stacked top to bottom so no panel carries both the long plan and the three-line question-and-answer exchange.

1. Panel one, establishing: the bare whitewashed room. Athos in the one chair on the RIGHT, still; Porthos filling the window at the back; Aramis on the edge of the table at LEFT with his book; the boy standing in the middle, nearest the viewer, visibly holding up the small blue-sealed letter. One balloon only: the boy's complete plan, high over him, with its tail unobstructed to his mouth.
2. Panel two, tight two-shot: the boy on the LEFT still holding the blue-sealed letter and Athos seated on the RIGHT. Three short balloons descend in a single zigzag: Athos's question upper right, the boy's answer middle left, Athos's answer lower right; each tail goes to the visible mouth of its owner.
3. Panel three, the dominant panel: the three answering faces, Porthos on the LEFT turning from the window delighted, Aramis in the MIDDLE closing his book, Athos on the RIGHT still in his chair. Three balloons descend left-centre-right: Porthos first, Aramis second, Athos third; each line remains whole in one balloon and each tail reaches its owner's unobstructed mouth.
4. Panel four: the boy on the LEFT looks from face to face, the blue-sealed letter still visible in his hand; Porthos on the RIGHT is large and open-armed. The boy's line is upper left; Porthos's answer is lower right after it. Both mouths and both tails are unobstructed.

### Exact strings
D'ARTAGNAN: `Two days to the sea, a day to London, and back by Monday. It can be done. The Cardinal will try to stop me.`
ATHOS: `What does the letter say?`
D'ARTAGNAN: `I don't know.`
ATHOS: `Good. Then nobody can make us tell.`
PORTHOS: `London! I have never once beaten an Englishman. I've always wanted to.`
ARAMIS: `In theory, four riders are more than one. In practice, the Cardinal will not let four through.`
ATHOS: `That's why it takes four. So that one arrives.`
D'ARTAGNAN: `You haven't asked me why. Not one of you.`
PORTHOS: `Why would we? You're going. That's the why.`

Render exactly these 9 strings once each, in this order, with clear ownership; no other text anywhere on the page.

### Character locks
d'Artagnan, keyed to his sheet: eighteen, long narrow face, sharp chin, long straight nose, close-set quick dark eyes, clean-shaven with no moustache, black unruly hair in his eyes, lean and narrow-shouldered, weight forward, one hand on a plain swept-hilt rapier too long for him; faded ochre-yellow doublet, brown breeches and boots, grey felt hat with one broken feather, no cloak (default state, pp 1–32). Athos, keyed to his sheet's default views: thirty, the tallest man in the book, long pale face, hooded level grey eyes, lines beside the mouth, dark hair straight to the shoulder, a short pointed dark beard and neat moustache, lean; blue cassock with the white cross over a black doublet, black hat with one white plume; NO sling (default state, pp 18–49); hands folded on the pommel of his grounded sword when still; the one man in any panel not moving. Porthos, keyed to his sheet: thirty-five, enormous, the widest man in the book, barrel chest, round ruddy face, small bright eyes, big nose, red-brown curls to the collar, a great red-brown moustache waxed to points, no beard; chest out, fists on hips; blue cassock with the white cross over a crimson doublet, a wide baldric embroidered with gold across the front, black hat with three red ostrich plumes, the largest hat in the book, a gilt-hilted sword; a hand smoothing the baldric. Aramis, keyed to his sheet: twenty-four, slim, fine oval face, small straight nose, large dark eyes, pale skin, fine blond curls to the collar always in order, a small neat blond moustache and lip tuft, no beard; weight on one hip, two fingers at his moustache; immaculate blue cassock with the white cross over dove grey with a wide white lace collar, black hat with one white plume, slim silver-hilted sword, a small book at his belt. The three Musketeers are separated by mass, hair colour, and facial hair before anything else: Athos tall, dark, pointed beard, still; Porthos huge, red-brown curls, waxed moustache, gold baldric, red plumes; Aramis slim, blond, small moustache, lace collar, book. The Queen's letter, keyed to the letters plate: a SMALL folded letter sealed in BLUE wax with a crown impressed in the seal; never the cream letter with the red seal.

### Consequential exclusions
The Queen's letter is not attached; draw it from words: a small folded letter sealed in blue wax with a crown pressed into the seal, no writing. Constance, Rochefort, the Cardinal, and Buckingham are absent. Athos has no sling. The room holds one chair, one table, one bed, and one sword on the wall, nothing else on the walls. Every panel remains inside this same room during this same conversation: no exterior Paris view, doorway entrance, introductions, royal summons, memory scene, travel montage, or anyone writing. The letter is small and blue-sealed with no legible writing. No blood; no sword drawn. No lettering except the nine spoken strings.

### Approved image inputs
1. `refs/approved/01-dartagnan.png`
2. `refs/approved/02-athos.png`
3. `refs/approved/03-porthos.png`
4. `refs/approved/04-aramis.png`
5. `refs/approved/set-athos-room.png`

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

- Candidate: `qa/production/page-25/candidates/page-25-vK.png`
- Prompt: `qa/production/page-25/prompts/page-25-vK.md`
- Audit: `qa/production/page-25/audits/page-25-vK.md`
- Proofs: `qa/production/page-25/proofs/page-25-vK-600x900.png` and `…-768x1152.png`

Generate with the workspace wrapper, which enforces the manifest, the ceiling
and the billing decision, saves the issued prompt, and derives both proofs:

```
python3 tools/imagegen.py three-musketeers-vol1 25 K --prompt-file PROMPT.md --ref REF1 --ref REF2 …
```

Then run `python3 tools/check_candidate.py three-musketeers-vol1 25 K`.

The audit stays under 180 words and uses exactly these headings:

`## Intent read` — what happens and who owns the page, from the 600 × 900 proof.

`## Exact text check` — exact transcription, or concise discrepancies.

`## Technical facts` — canvas/mode and obvious focal integrity issues.

`## Submission` — `SUBMITTED TO INDEPENDENT CRITIC`.

Return only the five output paths, candidate dimensions/mode, and file hashes.
Do not approve, promote, or write to `pages/`.
