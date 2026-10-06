# PAGE 20 — builder packet

## Fresh zero-history builder contract

You are a fresh builder for page 20, candidate vK, mode `BASE|TARGETED|FULL_PROMPT_RESET`.
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

The version ceiling is v4 and the count never resets. You do not
number your own versions; the orchestrator holds the count.

## Shared generation frame

### Canvas and status

One finished, flattened story page, **1024 × 1536 portrait, 2:3**, lettering baked in natively. This is a canonical production candidate for a printed illustrated novel, not a prototype, mockup, sample sheet, spread, or layout study. It is never a montage, model sheet, portrait board, or collage of the attached reference images: the references supply identity and place only, and the output is a new staged scene in which those people act, with the scripted balloons lettered in. Never landscape, never square. No page number, title, production label, speaker name, or editorial text of any kind appears on the page: the only visible text is the exact strings the page prompt lists. **Speaker names are never lettered.** The owner tag beside each exact string (a character's name, CAPTION, PROSE FIELD 1, SOUND, PRINTED OBJECT) says whose balloon or field it is; it is never rendered, never used as a prefix inside a balloon, and never placed beside one. Ownership is carried by placement and tail alone. The strings are listed in reading order and their sequence carries that order; no numeral, letter, bullet, or tag from this prompt is ever lettered on the page.

### Register — *Lacquer and Dust*

Lacquer and Dust. Bold, wet brush-and-ink line on warm, toothed mulberry paper, with flat matte washes of earth and mineral pigment: lamp-black ink, raw umber, loess yellow-ochre and dust grey for the land; and, laid flat and strong where people and banners carry them, cinnabar vermilion, malachite green, indigo, imperial purple, ivory, and the dull bronze and iron of armor. Late-Han China lit like a war film: hard white noon and long dust, smoke-orange firelight, brazier light in lacquered halls with real cast shadows and real depth, cold blue dawn. Visible brush line, visible paper tooth, ink and wash pooling at the edges of a stroke; lamellar iron, lacquered leather, hemp, silk, horsehair, rammed earth, grey tile, steel. Not smooth prestige-oil realism. No glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no anime proportions, no children's-book softness, no plastic 3D render, no blue-green landscape-scroll prettiness, no gold leaf.

Colour belongs to people and their banners, one owner per colour: Liu Bei white, Guan Yu green, Zhang Fei black, Cao Cao indigo (black-and-indigo banners), Lü Bu vermilion (and Red Hare, blood-red), Dong Zhuo purple and gold (purple banners), Yuan Shao ivory and gold (the great gold banner), the Yellow Turbans yellow headbands. No named character wears yellow; the only other yellow is the boy emperor's robe. The land is loess yellow-brown, packed earth, rammed-earth walls, and grey tile under big skies: hot white noon, smoke-orange fire, cold blue dawn. Three places must look like a different world: the peach garden (the only soft colour in the book, pink and white blossom or green leaf), the palace (dark lacquer red, black, and gold, brazier light, too big for the people in it), and Hulao Gate (a grey stone fortress filling a mountain pass, so big that armies at its foot are grass). Deaths are real and never drawn: no blood, no wound, no body, no severed anything, ever; a blow lands between panels, a rider falls out of frame.

### The lettering law — construction numbers for the builder

Outer safe margin 64 px on every side; no essential text below 72 px from the bottom edge; minimum panel gutter 24 px; no balloon, caption, or prose field crosses a panel border. Speech lettering 44–50 px tall, short replies 48–54 px, **never below the 40 px floor**; comfortable balloon width 240–390 px; at most about 24 words in one balloon; warm ivory balloon fill, restrained dark painted outline; tails end in open space beside the speaker's mouth; silent figures get no balloon and no tail fragment. Illustrated-prose fields: lettering 36–42 px, 38–52 characters per line, paragraphs of 2–5 lines, one or two fields per page at 78–88% of the canvas width, at least 42 px internal padding, a matte parchment field in the page's palette, left-aligned with a calm ragged right edge, never over faces, hands, busy art, maps, or documents. Captions and sound cues use the same family, simplified and enlarged. One restrained editorial lettering family at three levels: speech (large, upright, hand-lettered mixed case), narrative prose (legible literary serif), small sound or object label. **Dialogue face, every page, no exceptions:** rounded hand-lettered upright mixed case, warm and slightly irregular, inside organic oval balloons with soft outlines; never a serif, never italic, never a typeset book face, never a rectangular or rounded-rectangle box. The only serif on any page is the prose field. Banned: condensed comic-display faces, geometric UI fonts, cursive body text, all-capital prose, distressed letterforms, thin old-style italics, tiny handwritten documents carrying facts. These numbers steer the generator; the only text test at the gate is whether every string reads from the **600 × 900** proof.

### Hierarchy and staging

One dominant image plainly owns the page; the share named in the prompt is a construction target, and the generator should build a clear hierarchy rather than a stack of equal bands. When the page's turn is a quiet beat (an answer, a sentence, a face changing) and another panel carries action or a crowd, the quiet panel is still the largest image on the page by far, close and tall, and the busy panel is a shallow strip seen from far back with small figures; this generator favors action tableaux and must be told otherwise. At most two small reaction insets unless causality needs a strip. A clear top-to-bottom reading path. The first speaker in a panel stands on the LEFT; opposed speakers stand on opposite sides with each balloon on its owner's side; in a three-line exchange, A upper on A's side, B middle on B's side, A's second line lower on A's side; a reply is never readable before the line that prompts it and sits clearly lower than it, never level. Every balloon's tail ends beside its own speaker's mouth; a tail into open space, into a crowd, or toward an animal is a defect. Every visible speaker's mouth is visible and its tail corridor is clear of hands, props, and bystanders. Any exchange of two short lines in one panel where either line could plausibly be spoken by either character (a question and its answer, a check and its confirmation, a one-word address) is staged as two single-speaker beats, the questioner alone with mouth visible and the balloon beside that mouth, then the answerer alone the same way, as stacked strips or a strip cut into two panels read left to right; a shared two-shot with crossing tails is the most common attribution failure on this generator. A focal action uses exactly two hands, named. Consequential objects that the story counts (five of something, three of something) are drawn in a spaced row so the reader can count them, and the prompt says "count them". Sound cues render the exact letters given, with no added punctuation or extra words; the run length of a repeated letter is not a defect. Words painted on a story object (a banner, a plaque, a sign) are object text: they must read exactly as scripted, and the same object seen in two panels may carry them twice. Nothing else is lettered: no laugh lines, no invented captions, no labels. Vertical accumulation for time, consequence, descent, isolation, aftermath. Unnamed figures never carry a complete reserved identity stack: Yellow Turbans wear yellow headbands over plain brown and grey, never a red face, never a long beard, never pheasant plumes; coalition lords other than Yuan Shao wear dull bronze and brown, are never in close-up, and never wear ivory, purple, indigo, green, vermilion, or a tall black hat; Dong Zhuo's soldiers wear dull iron under purple banners, faces generic; the boy emperor is a small figure in imperial yellow robes on a vast throne; the deposed emperor is a young man in yellow robes; the old lord Lü Bu stands behind is white-haired in grey, face never close; the champion at the gate is a dark rider in a plumed helmet seen only at a distance; the farmhouse family is an old woman and a young man in brown; messengers, smiths, grooms, and farmers are plain and bareheaded. No background man has a red face, long earlobes, a beard to the belt, bristling cheek whiskers with black armor, a pointed goatee in indigo, obesity in purple, a tall black lacquered hat, or two long pheasant plumes. No background figure ever carries a balloon.

### How each kind of input binds

Attached character sheets are identity locks: the face, build, posture, costume state, and habitual gesture on the sheet are reproduced exactly, and the prompt's lock clause names which traits must survive at page scale. Setting plates bind architecture, palette, light logic, and the location's accent; they carry no figures, and the page adds the people. Object plates bind the state and silhouette of consequential objects. **Promoted pages are never attached as inputs:** a lettered page is a copy target for this generator (Volume I's page 3 reproduced page 2 wholesale), and continuity across the page turn rests on the sheets and plates, which is what the locks are for. Boards are never inputs. The model draws what it is shown: never attach a lookalike as a negative example, never attach a rejected candidate.

### Image generation path

Generate with Codex's built-in image generation on the ChatGPT subscription. Do not use an API key, the bundled image CLI, or any separately billed path.

## Page intent

## PAGE 20

Dramatic. In a stable at night, by one lantern, Lü Bu is polishing his halberd when Dong Zhuo leads in a huge blood-red horse, Red Hare, and offers it to him. Lü Bu's cold face changes when his hand touches the horse's neck: he wants it, and that wanting is the page's centre. Dong Zhuo, close and smiling, a fat hand on his shoulder, goes after the old man who raised him, and Lü Bu says he has a father; Dong Zhuo answers, "Do you?" and offers gold armor to match the horse. The dominant turn: Red Hare; "I have a father." "Do you?" The reader turns because Lü Bu has been offered a horse for his father and has not said no. The stable and the lantern stay subordinate.

## Builder-only page prompt

## PAGE 20 — Red Hare

### Reader turn
Dong Zhuo offers Lü Bu a horse for his father, and Lü Bu wants the horse.

### Ordered moments
1. Panel one, about 30%: a stable lit by one lantern. LÜ BU on the left, seated, polishing his halberd. Through the door on the right, DONG ZHUO leading on a rope a huge blood-red horse with a darker mane. Dong Zhuo's balloon upper right above him, tail to his mouth.
2. Dominant panel, about 40% of the page, the largest image, close and tall: Lü Bu on the LEFT, his hand flat on the red horse's neck, his cold face changed, wanting it; the horse's head and neck fill the centre. His balloon upper left beside his mouth. Dong Zhuo at the right edge, face and mouth visible, his balloon at right, clearly lower than Lü Bu's.
3. Panel three, about 30%: Lü Bu on the LEFT turned to face Dong Zhuo; Dong Zhuo on the right, close, smiling, one fat hand on Lü Bu's shoulder. Lü Bu's balloon upper left beside his mouth; Dong Zhuo's longer balloon right and clearly lower, tail to his mouth. Exactly two hands in focus: Dong Zhuo's on the shoulder, Lü Bu's at his side.

### Exact strings
DONG ZHUO: `This is Red Hare. He can run from sunrise to sunset and never tire. There is no horse like him in the empire.`
LÜ BU: `I have never seen a horse like this.`
DONG ZHUO: `He's yours. What has the old man ever given you? A bed, and orders?`
LÜ BU: `He raised me. I have a father.`
DONG ZHUO: `Do you? A real father would give his son everything. Be my son, Lü Bu, and you'll have gold armor to match the horse.`

Render exactly these 5 strings once each, in this order, with clear ownership; no other text anywhere on the page.

### Character locks
LÜ BU: tall, lean, clean-shaven, long pale face, high cheekbones, cold wide-set eyes, two long pheasant plumes on a gold headdress; pre-gift state (dark bronze armor, vermilion war-robe, pp 18–19); halberd. DONG ZHUO: obese, jowled, small sunk eyes, thin drooping greying moustache, gold cap, purple and gold brocade, heavy rings, swaying. RED HARE, keyed to the object plate: huge, blood-red coat, darker mane, bare of saddle on this page, haltered on a rope.

### Consequential exclusions
Cao Cao, Yuan Shao, the old lord and the brothers are absent; no grooms. No gold armor on Lü Bu yet. The horse never carries a balloon or tail. One lantern only. No lettering on anything.

### Approved image inputs
1. `refs/approved/06-lu-bu.png`
2. `refs/approved/05-dong-zhuo.png`
3. `refs/approved/obj-red-hare.png`

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

- Candidate: `qa/production/page-20/candidates/page-20-vK.png`
- Prompt: `qa/production/page-20/prompts/page-20-vK.md`
- Audit: `qa/production/page-20/audits/page-20-vK.md`
- Proofs: `qa/production/page-20/proofs/page-20-vK-600x900.png` and `…-768x1152.png`

Generate with the workspace wrapper, which enforces the manifest, the ceiling
and the billing decision, saves the issued prompt, and derives both proofs:

```
python3 tools/imagegen.py three-kingdoms-vol1 20 K --prompt-file PROMPT.md --ref REF1 --ref REF2 …
```

Then run `python3 tools/check_candidate.py three-kingdoms-vol1 20 K`.

The audit stays under 180 words and uses exactly these headings:

`## Intent read` — what happens and who owns the page, from the 600 × 900 proof.

`## Exact text check` — exact transcription, or concise discrepancies.

`## Technical facts` — canvas/mode and obvious focal integrity issues.

`## Submission` — `SUBMITTED TO INDEPENDENT CRITIC`.

Return only the five output paths, candidate dimensions/mode, and file hashes.
Do not approve, promote, or write to `pages/`.
