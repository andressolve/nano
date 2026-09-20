# Packet spec — how to write intents, prompts, and cards for this book

You are one of several fresh packet writers, each assigned one movement. Read first, in this order: `method/04-PAGE-LOOP.md` §1 and §5, `method/05-PROMPT-CRAFT.md` §1–3, `method/06-TYPOGRAPHY.md` (the text budget table only), then this book's `08-FULL-SCRIPT.md` (your movement's pages), `07-PAGE-CONTRACT.md` (your rows), `04-CHARACTER-LEDGER.md`, `05-SETTINGS-AND-OBJECTS.md`, `09-REFERENCE-PLAN.md` (the manifest table only, for approved file names), and `qa/_assembly/frame.md` (so you never repeat it). The lessons below were paid for on Monkey King Volume I (`books/monkey-king-vol1/10-PRODUCTION-MEMOIR.md`, Part VIII); they are not optional.

Write three files for your movement under `qa/_assembly/parts/`: `mov-<N>-intents.md`, `mov-<N>-prompts.md`, `mov-<N>-cards.md`. Each contains one section per page in your range, in page order, in exactly these header forms, which the assembler parses:

- intents: `## PAGE 7` (nothing after the number)
- prompts: `## PAGE 7 — a short title` (an em dash, then the title)
- cards: `## Page 7 — card` (capital P, lowercase card)

Use no other `##` headers. Subsections inside a page use `###`.

## The intent (builder and critic both see it)

80–160 words of plain prose. What happens on the page, who owns it, what changes, why the reader turns, and what stays subordinate. Name the mode. Name the page's one dominant turn from the contract row. No reference file names, no generation instructions, no history, no numbers.

## The prompt (builder only)

Derived from the exact script block, the contract row, the ledger, the settings, and the frame. Structure, in this order, with these `###` headings:

1. `### Reader turn` — one sentence.
2. `### Ordered moments` — the panels, numbered as prose (these numbers describe panels and are never lettered), each with who is visibly left and right, what they do, and where each balloon sits and where its tail goes (to which mouth). Name the dominant panel and its share from the contract row as a steering target ("about 50% of the page"). When the dominant beat is quiet and another panel is busy, say the quiet panel is "the largest image on the page by far, close and tall" and make the busy one "a shallow strip seen from far back with small figures". Put the first speaker on the LEFT. Stage any exchange where either line could plausibly be either character's, and any panel with three lines from two speakers, as single-speaker beats (each speaker alone, mouth visible, balloon beside that mouth; stacked strips or a strip cut in two read left to right). Name focal hands: "exactly two hands, one action". For a prose page, describe the dominant illustration and where the prose field sits (over plain ground, never over faces, hands, or busy art).
3. `### Exact strings` — every rendered string from the script block, once, in reading order, **one per line, with NO numeral, bullet, or letter in front of it** (a numbered list gets its numbers lettered into the balloons), in backticks, preceded by its owner tag and a colon: `WUKONG: \`…\``, `CAPTION: \`…\``, `PROSE FIELD 1: \`…\`` (each paragraph its own line), `SOUND: \`…\``, `PRINTED BANNER: \`…\``. Copy them character for character from the script, including punctuation. The owner tag is packet notation for who owns the string; it is never rendered. Close the list with one sentence: "Render exactly these N strings once each, in this order, with clear ownership; no other text anywhere on the page" and, if a story object carries painted words, say which object shows them and that they are object text, not a balloon.
4. `### Character locks` — one clause per visible named character, keyed to the attached sheet: face shape, brow, eyes, hair or fur, build, posture, costume state for this page (name the state and its page range from the ledger), habitual gesture. For any risky pair on the page (from the ledger's collision matrix), one sentence naming what carries the separation. Unnamed figures get one clause each describing their reserved-space-free look.
5. `### Consequential exclusions` — absent named characters named as absent; objects that must stay in a given state; counted objects ("exactly five, count them, in a spaced row"); props that must not become focal; the reserved identity stacks no background figure may wear; what must not be lettered (no laugh lines, no captions unless scripted, no name plaques, no readable words on objects unless scripted).
6. `### Approved image inputs` — a numbered list, each line a backticked path: every locked character sheet for a character visible on the page (the state sheet instead of the default when the ledger says so), the setting plate for the location, the object plate when a consequential object is focal. **Never a promoted page, never a board, never a candidate.** At most `max_refs_per_call` from `book.toml`. Close with "Attach only these images."

Approved file names: copy them exactly from the manifest table in `09-REFERENCE-PLAN.md`; map each script location to its plate in one line each. Boards (`board`, `adversarial`, `silhouette`, `live-pair`) are critic-only and must never appear here.

## The card (critic only, after the blind read)

Three to eight numbered criteria, each `### Cn — short title` followed by two or three sentences: the reader-facing failure it names, and its nonblocking tolerance. Always include, as C1, the transcription criterion: every listed string reads exactly from the 600 × 900 proof, once, in causal order, owned by the right mouth by tail and placement, no extra text; a string that does not read is blocking, a string that reads is not to be measured; if an object carries scripted words, say so, and say that the same object legible in a second panel is continuity, not a doubled string; the run length of a repeated letter in a sound cue is nonblocking. Then criteria for: the page's dominant turn landing by eye (one panel owns the page; the declared mode rendered; judge ownership by what the eye finds, never by area); attribution and reading order across the specific exchanges on this page (name the exchange, name each line's owner, and say each must hang from its own speaker's mouth by tail, not merely make sense as his); identity of each named character present and separation of any risky pair; consequential continuity and object state specific to this page (counted objects: "exactly five; more or fewer is blocking"); focal generation integrity (faces, hands of speakers, "exactly two hands"). Derive the card from the script and intent, never from the prompt. **Never include a percentage, a pixel size, a panel share, or any measurement**; those void the card. Do not mention references, the prompt, versions, or history.

## Budget and hygiene

Keep each page's prompt under about 450 words and each card under about 250. Write nothing into any file outside `qa/_assembly/parts/`. Do not edit the script, the contract, the ledger, or the plan. When done, reply with the three file paths and the page numbers covered, nothing else.
