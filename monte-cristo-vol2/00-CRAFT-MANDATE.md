# Craft Mandate — the readability authority
## Project-local copy — The Count of Monte Cristo, Volume II

**This is a copy, not a pointer.** It governs `monte-cristo-vol2/`.

### Parent authorities — carried forward, not replaced

This volume is a sequel. Per the sequel trap, its parent authorities are named
here by filename and its numbers are inherited verbatim:

| Parent authority | What this volume inherits |
|---|---|
| `monte-cristo-expanded/00-READABILITY-MANDATE.md` | the central readability standard |
| `monte-cristo-expanded/06-PORTRAIT-TYPOGRAPHY-SYSTEM.md` | **every typography number, unchanged** — see `06-TYPOGRAPHY-SYSTEM.md` |
| `monte-cristo-expanded/19-ANTI-TERSE-DIALOGUE-MANDATE.md` | the anti-terse rules and the five-word audit |
| `monte-cristo-expanded/20-EFFORTLESS-STORY-CRITIC-MANDATE.md` | "recoverable" is a revision flag, not a passing grade |
| `monte-cristo/01-STYLE-GUIDE.md` | the Velvet Cinema register and the world palettes |
| `monte-cristo-expanded/refs/` | the approved Volume I faces this volume ages forward |

**This volume relaxes no parent rule.** No clause below lowers a number, widens
a tolerance, or softens a gate relative to Volume I. If a future editor adds
one, that clause must name the parent rule it relaxes and why, in the clause
itself.

### Volume-specific numbers

| | |
|---|---|
| Page count | **49** |
| Canvas | 1024 × 1536, 2:3 portrait |
| Lettering floor | **40 px**, inherited from Volume I — a builder target, never measured at the gate |
| Cast ceiling | **8 locked characters — hard** |
| Mode balance | 33 dramatic · 8 illustrated prose · 7 spectacle |
| Engine | *A man who spent fourteen years turning himself into a weapon walks into the house of the men who made him — and discovers how much he is going to enjoy this.* |

### The specific failure this volume exists to avoid

An earlier Volume II (`monte-cristo-vol2-abandoned/`) passed five complete
script gates unconditionally and was written off by the reader as unreadable.
Its dialogue was **logistics** and **aphorism** and nothing else; it narrated
its largest spectacle off-panel while characters discussed its meaning
on-panel; and it carried ~175 lines of metadata per page around ~5% actual
writing.

**§8b below is the gate that would have caught it. Weight §8b above §8.** Do
not read, cite, or reuse anything in that folder.

---

This is the authority every other file in this skill serves. It is generalized
from `monte-cristo-expanded/00-READABILITY-MANDATE.md`,
`19-ANTI-TERSE-DIALOGUE-MANDATE.md`, and `20-EFFORTLESS-STORY-CRITIC-MANDATE.md`
in the `nano` repo, which together produced the only long-form volume of this
kind the reader has judged a success.

**Read this before the gates.** The gates exist to enforce this. A run that
executes every gate perfectly while ignoring this file produces exactly the
failure this skill was built to prevent — see `failure-modes.md`.

---

## 0. You are writing an adaptation. Start there.

**This is the first rule because it is the one that gets abandoned first.**

You are not reproducing a source. You are writing **a new book** that happens to
be built from one. The source is raw material — a quarry, not a blueprint. It has
no authority over what belongs on the page. The only authority is whether a
first-time reader who will never read the original experiences a complete,
gripping story.

Say this out loud at Phase 1, in writing, before any planning doc exists:

> *This volume is an adaptation. Fidelity to the source is not a goal, not a
> tiebreaker, and not a defense. Every element earns its place by what it does
> for this reader in this book, or it is cut.*

### Fidelity anxiety — the failure this rule prevents

The recognizable symptom is **solving a production problem that a script decision
should have deleted.** It sounds like craft. It is not.

- *"Six robed immortals will collide visually — how do we differentiate them?"*
  → Wrong question. **Cut them to two.** The reader does not know the celestial
  bureaucracy exists and will never miss four of them.
- *"This subplot is famous, we should find room."* → Fame is not a reason. Does
  it change what the protagonist wants or believes? No? Cut it.
- *"The source explains it in this order."* → Irrelevant. Order it for the
  reader.
- *"We can compress it to fit."* → Compression is the tax you pay for refusing
  to cut. Cut instead. See §11.

Fidelity anxiety never announces itself as fidelity anxiety. It arrives as
diligence, as respect for the source, as *"but that's what happens."* Treat
"but that's what happens in the original" as an admission that you have no
in-book reason for the element.

### The one thing you owe the source

Not its incidents — its **engine**. The thing that makes people still tell this
story: Monkey's appetite outrunning his cleverness; Dantès discovering that
revenge and justice are not the same. Identify the engine at Phase 1, protect it
absolutely, and hold everything else loosely.

**A cut list is a sign of health.** A Phase 1 that cuts nothing has not begun.

---

## 1. The central standard

> The reader may wonder what a secret means. The reader must never wonder
> whether a necessary piece of the story was omitted.

> The reader should experience the story, not solve the adaptation.

Readability means a first-time reader who has never read the source can always
understand:

1. where and when the scene is happening;
2. who the important people are;
3. what each person currently wants;
4. what information each person knows or conceals;
5. why a decision is made;
6. what changed because of that decision;
7. why the next scene follows.

**"Recoverable," "eventually clear," and "understandable after looking back" are
not passing grades. They are revision flags.** This wording is load-bearing. An
earlier critic pass accepted a confusing page as recoverable from context; the
reader's own review overturned it and the standard was tightened permanently.

---

## 2. The form

A **cinematic illustrated novel**: a deliberate hybrid of graphic novel,
illustrated prose, and nearly silent visual spectacle. It is not a conventional
comic and it is not a picture book.

Production canvas: **1024 × 1536, 2:3 portrait.** Never generate or approve a
landscape or square story page in this form. Do not mix portrait and landscape
story canvases inside one reader.

Every delivered page is a single finished, flattened image with lettering baked
in natively. No HTML, SVG, or other post-hoc lettering layer may repair a page.

---

## 3. The three page modes — the rule Vol 2 dropped

Every page is assigned exactly one dominant mode **in the script, before any
image exists**. A page may combine modes, but each page needs one dominant
reading experience.

### Mode 1 — Dramatic scene
- Usually three to five panels.
- Dialogue, gesture, opposition, discovery, and decision carry the page.
- Each visible speaker is staged clearly.
- Dialogue does not carry information that would sound unnatural merely because
  the reader needs it.

### Mode 2 — Illustrated prose
- One dominant illustration, or a small sequence of quiet images.
- Usually 50–120 words, with 140 words as an exceptional ceiling.
- Used for time, travel, interior experience, consequence, reorientation, and
  transitions between major scenes.
- Prose occupies a designed reading field with generous margins and line length.
  It is not placed over visually busy art.
- These pages are **designed as illustrated prose from the beginning.** They are
  not blank comic captions created as a lettering workaround, and they do not
  imitate speech balloons.

### Mode 3 — Spectacle or silence
- A full-width image, full-page image, or sparse cinematic sequence.
- Little or no text.
- Used for arrival, dread, discovery, escape, wonder, grief, and aftermath.
- Silence is earned by clarity in the pages before it.

### Mode balance

Across a volume, target approximately:

| Mode | Share of pages |
|---|---|
| Led by live dramatic scenes | ~60% |
| Led by illustrated prose or prose-image combinations | ~20% |
| Led by spectacle, silence, or visual aftermath | ~13% |

(In the 55-page reference volume: 32–34 dramatic, 10–12 prose, 6–8 spectacle.)

**A volume whose pages are all dramatic scenes has lost the form.** The prose
and spectacle pages are what buy the dramatic pages their room to breathe. If a
script has no illustrated-prose pages, that is a script-gate blocker, not a
stylistic preference.

---

## 4. Pacing rules

1. **Enter clearly.** The first page of a scene establishes place, important
   people, and the immediate desire or danger.
2. **Let the turn happen.** Important decisions receive enough panels and
   dialogue to feel chosen rather than reported.
3. **Stay for the consequence.** Betrayal, death, revelation, and rescue receive
   reaction or aftermath before the plot moves on.
4. **Do not confuse compression with momentum.** A quick succession of major
   events can feel *slower* than a clearly motivated sequence, because the
   reader must stop and reconstruct it.
5. **One dominant turn per page.** A page may contain several beats, but the
   reader must know what changed.
6. **Reintroduce naturally.** A returning character is identified through name,
   relationship, behavior, or context *before* the plot depends on recognition.
7. **Make plans legible.** When a character uses a disguise, document, debt, or
   intermediary, show what they want, what step they are taking, and the visible
   result.
8. **Protect emotional duration.** Do not place grief, ingenious mechanics, and
   the next major revelation on the same page.

---

## 5. Portrait page grammar

- Use **one dominant image or panel that plainly owns the page.** Roughly 45–70%
  of the page's visual attention is where good pages tend to land; write that into
  the prompt so the model builds hierarchy instead of a stack of equal bands.
- Use no more than two small reaction insets unless causality requires a
  sequential strip.
- Build a clear top-to-bottom reading path.
- Wide internal panels remain available for ships, harbors, offices, tables,
  cells, islands, and opposed speakers.
- Use vertical accumulation for time, consequence, descent, isolation, and
  emotional aftermath.

**This is craft guidance, not a gate. Panel size blocks nothing, at any stage.**
A page of four to six roughly equal bands has no panel in charge and usually no
dominant turn either — so build hierarchy deliberately, and say so in the prompt.
But do not convert that into a number anyone is held against.

*Owner instruction, 2026-08-16: cut entirely.* This rule was written as a 45–70%
band, and the band blocked page 1 at 73% — for being* more *dominant than the
ceiling allowed — and page 8 at 42%, whose single dominant field was three times
any other panel. Both needed owner overrides. The one genuine hierarchy defect it
is credited with, page 5's three competing stages, was **seen by eye on the
rendered page** and only afterwards argued in share points. Judgment caught it;
the number caught nothing and cost two pages.

Note what the old justification for this rule actually was: *equal bands → type
shrinks to fit → the page becomes unreadable.* That is the lettering-size
argument, and readability is now settled by the transcription test, which is
evidence rather than an estimate. When the text gate was replaced, this rule lost
its reason to exist and kept running on inertia.

### Locations per page

A page normally occupies **one location.** Two is permitted when the page's
dominant turn *is* the transition. Three or more distinct locations on one
portrait page is a blocker: it guarantees equal bands, guarantees no dominant
panel, and turns a story page into a summary montage.

---

## 5b. The typography law — numeric, and load-bearing

These numbers are on the **1024 × 1536 canvas**. They are not stylistic
preferences; dropping them is the single clearest cause of the failed run.

### Speech balloons

| Property | Value |
|---|---|
| Normal lettering height | **44–50 px** |
| Short-reply lettering height | **48–54 px** when space allows |
| **Minimum approved lettering height** | **40 px — a hard floor** |
| Comfortable balloon width | **240–390 px** |
| Maximum words in one balloon | **~24** |
| Internal padding | ~one capital-letter height between text and outline |

Warm ivory fill, never pure digital white. Restrained charcoal-brown outline.
Tails point into open space immediately beside the speaker's mouth. A balloon
belongs unmistakably to the person on its own side of the panel.

When a panel has opposed speakers: first speaker takes the upper position on
their own side; the reply takes the opposite upper or middle position; a second
line from the first speaker drops lower on the original side. **If that pattern
is still ambiguous, split the exchange across panels.**

### Illustrated-prose fields

| Property | Value |
|---|---|
| Prose lettering height | **36–42 px** |
| Line length | **38–52 characters** including spaces |
| Paragraph length | **2–5 lines** |
| Fields per page | **one or two** — never scatter sentences across many boxes |
| Field width | **78–88% of canvas** |
| Minimum internal padding | **42 px** |

Left-aligned with a calm ragged right edge. No busy art, faces, hands, maps, or
documents behind the prose.

### Hierarchy

Story text has exactly **three** visible levels: narrative prose, speech, and
small sound or object label. Production titles, page titles, scene titles,
speaker names, density codes, and editorial labels **never** appear in finished
art.

**Boldface, italics, enlarged shouting, and decorative color are exceptional.**
Meaning comes first from staging, expression, silence, and the words themselves.

Banned: condensed comic-display lettering; modern geometric UI fonts; cursive
body text; all-capital prose; faux-aged or distressed letterforms; tiny
handwritten documents carrying essential facts.

### How this interacts with the essentials gate

The gate makes pixel measurement of lettering nonblocking **at every size**,
because a strict gate rejected pages over sub-40px glyph measurements and drove
one page to v77 — and in this volume it held page 1 through four rejections that
each conceded the text was fully readable. Reconcile it this way:

- **The type numbers above are builder instructions, not gate criteria.** They
  go in every page prompt. They are never checked against a rendered page.
- **Never measure lettering, at any size.** Not on the source, not on the proof.
- **The transcription test is the entire text gate.** A string that reads is big
  enough. A string that does not read is blocking whatever it measures.

A floor plus the transcription test (`gates.md` §5) is enough. Measuring against
targets above the floor is the tolerance-exercise failure mode.

**The failed volume rendered at ~27 px per line** — a ~5 px x-height at the
600 × 900 desktop proof — in a thin old-style *italic* serif, on pages its own
critic passed 29 times for "reading comfort."

---

## 6. Narrative voice

The prose voice is third-person and close to the protagonist whenever possible;
emotionally exact without explaining the moral in advance; literary but
immediately comprehensible when read aloud; concrete about bodies, places,
objects, time, and consequences; restrained around secrets the drama has not
earned the right to reveal.

> Narration carries the reader **between rooms.** Dialogue lets the reader
> **live inside them.**

Narration **may**: establish time and place; bridge travel or elapsed time;
identify what changed between scenes; reveal a private belief that cannot be
spoken naturally; remind the reader of a returning person or significant object;
show accumulation of time or education; make the consequence of an earlier
choice explicit.

Narration **may not**: summarize a confrontation that should be dramatized;
lecture on history or the source's importance; repeat what picture and dialogue
already make clear; announce what the reader should feel; turn a character's
transformation into a list of acquired abilities; conceal a missing causal step
beneath elegant language.

---

## 7. The anti-terse rule

> Brevity is welcome. Incompleteness is not.

There is no requirement to minimize dialogue. Use more words, more balloons, a
larger prose field, a restaged panel, or an additional page when that is what
effortless comprehension requires.

### Binding rules

1. **Give important questions an object.** A question that causes a choice,
   plan, promise, revelation, or page turn must name what is being asked.
2. **Do not float fragments.** A one- or two-word line may not carry necessary
   plot logic unless its meaning is uniquely determined by the immediately
   preceding line and the visible action.
3. **Name the action.** Prefer "Will you marry me tomorrow?" to "Tomorrow?";
   "Did Fernand send it?" to "Him?"; "Do you want me to stay?" to "Stay?"
4. **Protect antecedents.** `it`, `him`, `her`, `this`, `that` fail when more
   than one visible person, object, promise, or action could be the referent.
5. **Do not use poetry to conceal logistics.** A lyrical reply may deepen a
   concrete decision; it may not replace the decision.
6. **Do not confuse speed with omission.** Three or four clarifying words beat
   making the reader pause and reconstruct the scene.
7. **Let characters finish consequential thoughts.** Invitations, accusations,
   bargains, refusals, plans, and promises normally contain a subject,
   meaningful verb, and object or complement.
8. **Read the exchange aloud without notes.** If a listener asks "Tomorrow for
   what?" or "Who is 'he'?", the dialogue fails even if the writer can explain
   it.
9. **Do not ration useful text.** A complete natural sentence outranks a terse
   fragment. If the complete exchange no longer fits comfortably, **restage or
   split the material; never shrink type or remove causal language.**

### The founding case

Rejected:

> **Edmond:** "Tomorrow?"
> **Mercédès:** "For the wedding—and everything after."

`Tomorrow?` has no stated object. It could mean the wedding, the house, moving
in, the captaincy, or the beginning of their life together.

Approved:

> **Edmond:** "Will you marry me tomorrow?"
> **Mercédès:** "Tomorrow—and every day after."

Same tenderness, same rhythm, action and commitment now explicit.

### Short lines that remain welcome

Short dialogue is powerful when the setup makes its meaning singular: `Father!`
works when the speaker is visibly embracing his father. `Never.` works as a
direct answer to a complete question in the same panel. `I am.` works when an
officer has just asked which man is Edmond Dantès. The same words fail when the
reader must invent the missing question.

### The five-word audit

**Every balloon of five words or fewer receives an explicit ambiguity audit:**

- Is this a complete thought, or an intentional answer to a complete thought?
- Can it refer to only one visible person, object, action, time, or promise?
- Would a first-time listener understand it without the script notes?
- Is the brevity emotionally forceful, or merely compressed?

Any necessary line failing one of these is a **BLOCKER**.

---

## 8. The ten binding story tests

Applied at the script gate to every page and every page-to-page transition, and
again at the page gate to the rendered result.

1. **Effortless first read.** A first-time reader understands the page in normal
   reading order without rereading, consulting notes, or knowing the source.
2. **Natural spoken dialogue.** Characters speak from desire, fear, love, anger,
   or strategy. Dialogue existing mainly to explain a procedure or historical
   fact fails even when the information is correct.
3. **One dominant dramatic turn per page.** Several beats are fine; one
   important choice, revelation, reversal, or consequence must govern them.
4. **No tiny-prop dependency.** Essential causality may not depend on
   distinguishing two similar scraps, noticing subtle handwriting, or decoding a
   small background action at reduced size.
5. **Choice over procedure.** Dialogue carries desire, decision, conflict,
   consequence. Narration may carry concise orientation, elapsed time, or
   mechanical connective tissue when dramatizing it would clutter the scene.
6. **Complete causal chain.** The page and its neighbors establish who acts,
   what they choose, why, what changes, and why the next scene follows.
7. **Natural completeness over terseness.** A technically correct line still
   fails if it sounds clipped, evasive, archaically compressed, or like an
   outline. Apply §7 in full.
8. **No text scarcity.** The critic must not reward low word count. Add words,
   balloons, prose, panels, or pages when they create clarity and emotional
   duration. **Never solve density by shrinking type.**
9. **Story, not treatise.** Historical context appears only when a character's
   immediate situation needs it. The page stays driven by people in conflict.
10. **Paraphrase test.** After one read, a cold reader can say in plain language
    what happened, why, and what changed, without reopening the page.

---

## 8b. The presence tests — is this script actually alive?

**§8 is ten absence tests. A script can pass all ten and be dead on the page.**
That is not hypothetical: the abandoned Monte Cristo Volume II script passed
five complete script gates unconditionally, and it is inert. These tests exist
because nobody was asked the only question that finally matters — *would anyone
want to read this?*

Absence tests are easy to check, so effort flows to them. Presence is what the
reader actually buys. Weight these accordingly.

### The two dead registers

Almost all bad adaptation dialogue collapses into one of two, and a script often
contains both while containing nothing else.

**1. Logistics.** Characters reciting arrangements — rooms, routes, schedules,
staffing, protocols, what is behind which door. It looks like competence because
it is specific and continuity-safe.

> ALBERT: "Rome for Carnival. You know Italy; I trust you to find us rooms."
> BERTUCCIO: "The Piazza room is secured. The coachman has the clear route."
> COUNT: "One calls my valet, two the majordomo, three my steward."

That is an entire volume opening on hotel booking and a page spent on a
bell-ringing system. **Logistics is never the drama.** Arrangements belong in
narration, in a single line, or nowhere.

**2. Aphorism.** Characters trading polished epigrams about the theme.

> "Because judgment reveals what comfort conceals."
> "A duel gives the guilty man an equal chance to win. That is hazard, not
> judgment."
> "Convictions are rarely born without a wound."

Nobody speaks like this. It is the writer talking through mouths, and it reads
as a seminar. **If a line would work equally well in any other character's
mouth, it belongs to no one.** A theme is what the story *does*, never what the
characters *say about* what the story does.

### The tests

1. **The want-from test.** In every scene, name what each speaking character
   wants **from the other person, in this room, right now** — not their arc
   goal. If the honest answer is "to inform them" or "to agree with them," the
   scene has no engine.
2. **The subtext test.** At least somewhere on most dramatic pages, someone says
   something other than exactly what they mean — evades, deflects, lies,
   understates, changes the subject. A script in which every line is fully
   sincere and fully explicit is a briefing.
3. **The attribution-strip test.** Strip the speaker names off a page of
   dialogue. Can you still tell who is talking? If every character is equally
   articulate, equally composed, and equally epigrammatic, you have one voice
   in several bodies.
4. **The enacted-not-narrated test.** The most dramatic thing on the page must
   be the thing that is *shown*. If a spectacle happens off-panel while people
   discuss its meaning on-panel, the page is inverted. Dramatize the event;
   let the meaning be inferred.
5. **The heat test.** Something must be at stake between the people present.
   Name it in one sentence. "They disagree about justice" is not stakes.
   "He is deciding whether to trust the man who will destroy his father" is.
6. **The appetite test.** Characters must *want* palpably — and the protagonist's
   appetite is usually the engine of the book. If the protagonist reads as
   serene, controlled, and above it all for pages at a stretch, the appetite has
   been written out.
7. **The page-turn test.** At the bottom of each page, name the reason a reader
   turns it. "The next scene follows" is not a reason. A question, a threat, a
   promise, or an appetite is.
8. **The would-you-read-it test.** Holistic, unfalsifiable, and mandatory. Read
   the movement as a reader, not an auditor. Is it any good? If the honest
   answer is "it is correct," that is a failing grade.

### The scaffolding rule

**Write the scene first; specify it second.** A page's script entry leads with
the actual writing — the panel action and the exact spoken lines. The metadata
(reader state, continuity, identity controls) follows, and stays compact.

The abandoned volume inverted this: ~175 lines of specification per page around
~5% actual writing, and the writing is what starved. **If the metadata for a page
is longer than the page's dramatized content, the document has become an audit
artifact and the story is not being written.**

---

## 9. Adaptation freedom — the operational rules

This is §0 applied. Read §0 first; it is the stance, and this is the toolkit.

Readability and emotional truth outrank chapter-by-chapter fidelity, always,
without needing to be argued for on a case-by-case basis.

### Cutting comes first

Before combining, reordering, or inventing, ask what can simply **go**. Cutting
is the primary adaptation tool and the most underused. A source written as a
serialized novel, an oral epic, or a play carries structure that served its
original delivery and serves this book not at all — episodic repetition, large
functional casts, digressions, and framing apparatus.

Default cuts, made without ceremony:

- **any character who does not change what the protagonist wants, knows, or
  chooses** — no matter how beloved;
- **repeated episodes that make the same point** — keep the best one, cut the
  rest, and let the survivor carry the weight of all of them;
- **institutional and bureaucratic casts** — collapse to the smallest number of
  faces that can hold the conflict, usually one or two;
- **framing devices** that cost pages and deliver no turn;
- **any incident retained because it is famous.**

Merging two characters into one is not a compromise. It is usually an upgrade:
the survivor gets twice the presence and half the introduction cost.

The adaptation **may**: combine minor characters; reorder discoveries; invent
bridge dialogue and private moments; let the reader understand a mechanism
earlier than the source does; repeat names and relationships naturally; simplify
legal, political, maritime, or financial processes; enlarge an emotional beat
while compressing a transaction; preserve a character's dramatic function
without preserving every incident.

The adaptation **must preserve**: the distinct moral responsibility of each
antagonist (the conspiracy must never collapse into "three jealous men"); the
protagonist's core moral position; every major character's agency, especially
women characters, who must remain active choosers; the bond between an act and
its emotional consequence, which may never be split across a volume boundary or
buried under unrelated material; and the volume's final image and moral fork.

Note what is **not** on that list: plot events, chapter order, episode count,
minor characters, place names, and the source's own explanations. None of those
are protected. If you find yourself defending one of them, you are defending the
source, not the book.

Each named antagonist needs a *distinct* motive, stated in the character doc and
visible on the page. Each disguise or alias must have a clear dramatic function
the reader can name, and must read as the protagonist's deliberate tool rather
than a newly introduced character.

---

## 10. The acceptance test

After every movement, a cold reader answers without coaching:

- Who acted?
- What did that person want?
- What choice was made?
- Why was it made?
- Who was affected?
- What does the protagonist now believe?
- Why are we going to the next scene?

**A page or movement fails if the correct response depends on information
present only in planning notes, source knowledge, or the reader's guess.**

---

## 11. Length

Never compress a source to fit a predetermined page count. Partition at arc
boundaries and use as many volumes as the material needs. The reference volume
grew from 32 pages (rushed, first edition) to 55 (expanded, successful) and the
expansion *was* the fix. If a movement will not fit, add pages or split the
volume — do not tighten the script until it fits.
