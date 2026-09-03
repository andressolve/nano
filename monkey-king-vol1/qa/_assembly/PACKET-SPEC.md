# Packet spec — how to write intents, prompts, and cards for this book

Read first, in this order: `method/04-PAGE-LOOP.md` §1 and §5, `method/05-PROMPT-CRAFT.md` §1–3, `method/06-TYPOGRAPHY.md` (the text budget table only), then the book's `08-FULL-SCRIPT.md` (your movement's pages), `07-PAGE-CONTRACT.md` (your rows), `04-CHARACTER-LEDGER.md`, `05-SETTINGS-AND-OBJECTS.md`, `09-REFERENCE-PLAN.md` (the manifest table only, for approved file names), and `qa/_assembly/frame.md` (what every page already gets, so the prompt does not repeat it).

Write three files for your movement under `qa/_assembly/parts/`: `mov-<N>-intents.md`, `mov-<N>-prompts.md`, `mov-<N>-cards.md`. Each contains one section per page in your range, in page order, in exactly these header forms, which the assembler parses:

- intents: `## PAGE 7` (nothing after the number)
- prompts: `## PAGE 7 — the raft and the Master's mountain` (an em dash, then a short title)
- cards: `## Page 7 — card` (capital P, lowercase card)

Use no other `##` headers. Subsections inside a page use `###`.

## The intent (builder and critic both see it)

80–160 words of plain prose. What happens on the page, who owns it, what changes, why the reader turns, and what stays subordinate. Name the mode. Name the page's one dominant turn from the contract row. No reference file names, no generation instructions, no history, no numbers.

## The prompt (builder only)

Derived from the exact script block, the contract row, the ledger, the settings, and the frame. Structure, in this order, with these `###` headings:

1. `### Reader turn` — one sentence.
2. `### Ordered moments` — the panels, numbered, each with who is visibly left and right and what they do; name the dominant panel and its share from the contract row as a steering target ("about 50% of the page"). Keep it moderate: essentials only, let the generator solve the image. For a prose page, describe the dominant illustration and where the prose field sits (over plain ground, never over faces). For a spectacle page, the single image and where the one caption sits.
3. `### Exact strings` — every rendered string from the script block, once, in reading order, numbered, in backticks, with its owner: balloons (`WUKONG:`), captions, prose field paragraphs (each paragraph its own numbered string, all belonging to `PROSE FIELD 1`), sound cues, printed objects (`PRINTED BANNER:`). Copy them character for character from the script, including punctuation. The owner tag is notation, never text: write it outside the backticks, and never as a `NAME:` prefix inside them. The count of strings must equal what the script block renders. State "Render exactly these N strings once each, in this order, with clear ownership; no other text anywhere on the page."
4. `### Character locks` — one clause per visible named character, keyed to the attached sheet: face shape, brow, eyes, hair or fur, build, posture, costume state for this page (Wukong: stone-born pp 1–17, Great Sage pp 18–40, tempered pp 41–47), habitual gesture. For any risky pair on the page (Wukong/Old Ma; Subhuti/Laozi never share a page; Jade Emperor/Laozi; Wukong/Erlang; Buddha/Subhuti never share a page) add verbatim: *their faces must remain structurally distinct even in profile, reduced scale, grayscale, partial hair, and travel clothes.* Name every silent figure as silent so the model gives it no balloon.
5. `### Consequential exclusions` — absent named characters named as absent; objects that must stay in a given state (the split stone stays split; the banner flies; the five gourds; the ring; the needle behind the ear; the staff's size on this page); props that must not become focal; the reserved identity stacks that no background figure may wear.
6. `### Approved image inputs` — a numbered list, each line a backticked path: every locked character sheet for a character visible on the page (`refs/approved/01-wukong.png`, or `refs/approved/09-wukong-tempered.png` instead of 01 on pp 41–47), the setting plate for the location, the object plate when a consequential object is focal, and the promoted predecessor `pages/page-NN.png` (NN = this page minus one) when the page continues the same room, costume state, or object state across the turn. **At most 6 inputs.** Only paths under `refs/approved/` or `pages/page-NN.png` with NN < this page. End with the line "Attach only these images."

Approved file names: `01-wukong`, `02-old-ma`, `03-subhuti`, `04-laozi`, `05-jade-emperor`, `06-ao-guang`, `07-erlang`, `08-buddha`, `09-wukong-tempered`, `set-peak`, `set-cave`, `set-courtyard`, `set-sea-palace`, `set-south-gate`, `set-hall-of-jade`, `set-stables`, `set-peach-garden`, `set-laboratory`, `set-edge-of-world`, `set-five-elements`, `obj-banner-seal-peach`, `obj-gourds-ring`. Boards are never inputs. There is no staff plate: the staff and the needle are on the Wukong sheets.

Locations → plates: Flower-Fruit peak/waterfall/pool → `set-peak`; Water Curtain Cave → `set-cave`; the Master's courtyard and cave → `set-courtyard`; the sea and Ao Guang's hall/treasury → `set-sea-palace`; South Gate → `set-south-gate`; Hall of Jade, banquet, terrace → `set-hall-of-jade`; stables → `set-stables`; peach garden → `set-peach-garden`; laboratory/furnace → `set-laboratory`; the sky battlefield over the mountain → `set-peak`; edge of the world → `set-edge-of-world`; the hand-mountain → `set-five-elements`; the Great Sage's mansion (p29) → `set-hall-of-jade` for Heaven's palette (no plate exists for the mansion; describe it in the prompt); the western sea sky (p12) and the raft (p7) → `set-peak` for palette only.

Do not put the frame's content in the prompt (canvas, register, lettering numbers, staging rules, input-binding rules); the assembler prepends the frame. Do not put anything in the prompt that the critic could grade against; the critic never sees it. No history, no compensation notes.

## The card (critic only, after the blind read)

Three to eight numbered criteria, each `### Cn — short title` followed by two or three sentences: the reader-facing failure it names, and its nonblocking tolerance. Always include, as C1, the transcription criterion: every listed string reads exactly from the 600 × 900 proof, once, in causal order, owned by the right mouth, no extra text; a string that does not read is blocking, a string that reads is not to be measured. Then criteria for: the page's dominant turn landing by eye (one panel owns the page; the declared mode rendered); attribution and reading order across the specific exchanges on this page (name the exchange, e.g. "Old Ma's 'Of all of us.' must be readable only after Wukong's 'King. Of all of you?'"); identity of each named character present and separation of any risky pair; consequential continuity and object state specific to this page; focal generation integrity (faces, hands of speakers, the dominant figure). Derive the card from the script and intent, never from the prompt. **Never include a percentage, a pixel size, a panel share, or any measurement**; those void the card. Do not mention references, the prompt, versions, or history.

## Budget and hygiene

Keep each page's prompt under about 450 words and each card under about 250. Write nothing into any file outside `qa/_assembly/parts/`. Do not edit the script, the contract, the ledger, or the plan. When done, reply with the three file paths and the page numbers covered, nothing else.
