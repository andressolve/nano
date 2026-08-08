# Monte Cristo Expanded — Builder/Critic Run Notes

## Purpose and scope

This is a factual record of how the builder and critic agents were instructed
during the successful Pages 23–55 production run. It records the orchestration
used by the production lead; it is not a rubric inferred afterward from the
critic's reports.

These notes apply to this long-form narrative/dialogue-driven workflow. They do
not change the biographical graphic-novel workflow in `../bio.md`.

## Earlier critic gates used on preparation

The page-production critic loop was preceded by three distinct independent
critic jobs. These were not retrospective interpretations of page reports;
they were the actual review structures used before or during preparation.

### Complete script

The first script critic was asked to cold-read the full 52-page script in order
before consulting the readability mandate or page-intelligence contract. It
judged:

- story knowledge and causality, including whether Edmond knew only what the
  story had actually shown him learning;
- mechanical continuity of bodies, documents, time, travel, and the Morrel
  rescue;
- presence and placement of every speaking character;
- exact causal reading order, speaker side, silent figures, and the individual
  mouth/source endpoint or tail-free designation of every numbered line;
- movement-by-movement first-time-reader comprehension and age-appropriate
  read-aloud clarity.

The critic withheld approval, required the entire script to be resubmitted,
then cold-read the complete revision and re-audited every original blocker.
That two-round task and verdict are preserved in
[`11-SCRIPT-CRITIC-REPORT.md`](11-SCRIPT-CRITIC-REPORT.md).

After Andres's Pages 1–10 reader QA exposed that some technically recoverable
storytelling was still effortful, the production lead built a stricter script
critic from
[`20-EFFORTLESS-STORY-CRITIC-MANDATE.md`](20-EFFORTLESS-STORY-CRITIC-MANDATE.md).
The same critic was asked to audit the complete book again, including already
approved pages, and every page-to-page transition. Its checks were effortless
orientation, natural spoken dialogue, one dominant turn, no essential
tiny-prop dependency, choice over procedure, complete causal chains, natural
completeness rather than terseness, sufficient emotional duration, story
rather than treatise, and one-read paraphrase. Each finding had to name the
page, quote or describe the failure, explain what a first-time reader would
have to repair, and prescribe a concrete revision. Approval remained withheld
through five full or targeted verification rounds; the record is
[`21-COMPLETE-SCRIPT-EFFORTLESS-STORY-CRITIC.md`](21-COMPLETE-SCRIPT-EFFORTLESS-STORY-CRITIC.md).

### Character references and anti-collision system

The reference critic was asked to inspect the existing reference library,
prototype pages, character specifications, and the cast as a system rather
than admire sheets one at a time. Every principal recurring character was
tested through costume-free face crops, thumbnail silhouettes, grayscale,
multiple lighting conditions, profiles and reactions, age/disguise changes,
same-panel opposition, silent memory insets, and re-entry after a long absence.

The critic created a collision matrix and named exact redesign requirements for
Edmond/Villefort, Count/Villefort, Edmond/Jacopo, Louis/Faria, Fernand/Edmond,
Mercédès/Julie, and other risky pairs. It also rejected the library because
several causally important supporting roles had no permanent lock and because
there was no explicit nearest-lookalike prohibition system.

After redesign, the critic restarted from the images and inspected all native
reference sheets, retained authorities, the identity ledger, neutral head and
grayscale silhouette boards, four adversarial boards, and an unlettered Page
15 Edmond/Villefort live-pair proof. It repeated the checks at 390-pixel mobile
width and 160-pixel page-thumbnail width. Only then did it approve the
reference library, while explicitly stating that reference approval did not
approve generated pages or waive balloon attribution. The complete task and
two verdicts are in
[`12-CHARACTER-DISTINCTNESS-CRITIC-REPORT.md`](12-CHARACTER-DISTINCTNESS-CRITIC-REPORT.md).

### Format and continuous prototype

The portrait format, hybrid page grammar, typography system, page-intelligence
contract, and internal prototype QA were prepared as authorities and evidence.
They were not treated as independent critic approval.

The independent prototype critic was given finished Pages 12–18 for a cold read
before consulting the script and internal QA. It judged first-read causal
comprehension, actual reduced-size comfort, and every balloon's visible owner
across the continuous sequence. It withheld approval because Page 12's stakes
required too much inference and Page 13 visually assigned Edmond's flashback
speech to the silent dying Captain Leclère. This proved why an internal QA pass
and attractive prototypes were not sufficient. The task and findings are in
[`09-INDEPENDENT-CRITIC-REPORT.md`](09-INDEPENDENT-CRITIC-REPORT.md).

These preparation gates remained deliberately non-transitive:

- a clear script did not approve reference casting;
- approved references did not approve a prototype;
- an approved prototype did not approve later pages;
- individually approved pages did not approve an uninterrupted batch.

## How the two agents were separated

The builder and critic were distinct agents. The builder could generate and
self-audit a candidate but could not approve or promote it. The critic could
review and issue a verdict but was explicitly prohibited from editing or
promoting the art. The production lead alone promoted approved bytes and
released the next generation.

While the critic reviewed Page N, the builder was asked to prepare the Page N+1
prompt only. Generation of Page N+1 remained held until Page N was approved,
promoted byte-for-byte, and explicitly released.

## Builder task actually used

The repeated generation instruction was materially:

> Generate Page NN from the prepared prompt. Generate one candidate, run one
> practical essentials audit, make desktop/tablet proofs, and submit it to the
> critic. Do not reroll for cosmetic or numeric reasons. Stop after the first
> plausible candidate unless there is an actual story, attribution, or anatomy
> failure.

The repeated prompt-preparation instruction was materially:

> While the critic reviews Page NN, prepare only the Page NN+1 prompt from the
> exact approved script with the minimum references. Hold generation until the
> current page is approved, promoted, and released. Protect story order,
> attribution, identity, and consequential continuity; avoid cosmetic
> constraints that invite rerolls.

This is how builder self-judgment was bounded. It performed one practical check
and normally submitted the first plausible image instead of simulating a second
critic or optimizing typography, panel percentages, margins, tail distances,
phone proofs, or finish.

The builder did stop before critic review when it found an actual essentials
failure. In this run that included Page 46's reversed confession/response tiers
and Page 53's missing required line. Each failed image was preserved, followed
by one complete redraw aimed at the named defect only.

## Critic task actually used

The repeated core page-review instruction was materially:

> Independently review Page NN under the corrected essentials gate: exact
> script/story, clear attribution, obvious generation/anatomy integrity,
> consequential identity/continuity, and actual desktop/tablet comfort.
> Typography/cosmetic/numeric prompt deviations are nonblocking unless they
> materially harm reading or story. The candidate path is supplied; the prompt,
> builder audit, and desktop/tablet proofs are sibling files. Write a concise
> critic report in the QA folder and return APPROVED or REJECTED with mandatory
> findings only. Do not edit or promote the production art.

The production lead appended page-specific checks to that core brief. These
were concrete commitments from the page's script and generation prompt, not a
generic request to decide whether the art looked attractive. Examples from the
actual tasks included:

- exact dialogue or prose count and causal reading order;
- who speaks first, which side each speaker occupies, and whether a sound or
  response must appear earlier or lower;
- whether framed memories remain silent and visually separate from live action;
- whether Faria's body, Edmond's sack, the knife, and the guards obey the escape
  geography;
- whether Busoni and Wilmore read as constructed identities of the same Edmond;
- whether one diamond visibly transfers from Busoni to Caderousse;
- whether two evidence papers remain distinct through the Wilmore-to-Edmond
  reveal;
- whether the pistol case remains closed with no visible weapon or self-harm;
- whether the replacement *Pharaon* stays concealed until the final page and
  then carries the established phoenix continuity;
- whether explicit exclusions such as premature reveals, extra speakers,
  readable documents, or later-page actions were absent.

Thus the critic was given the page prompt and also received its material visual
requirements as an explicit page-specific checklist. The builder audit traveled
with the candidate as context, but the critic's instruction was to review
independently and return its own verdict.

## Critic output contract

For every page the critic had to:

1. save a concise report beside the candidate;
2. return exactly `APPROVED` or `REJECTED`/`REVISE`;
3. identify only mandatory findings in the verdict;
4. keep nonblocking observations separate;
5. make no edit, promotion, reader change, or replacement image.

An approval authorized the production lead—not the critic or builder—to copy
the exact candidate bytes into `pages/page-NN.png`, verify byte identity, update
the QA ledger/reader/handoff, and release the next page.

## What triggered another generation

A new generation normally required a critic finding that changed an essential
story read. During this run the critic required full redraws for:

- Page 27: correction balloons could be read before the mistakes/questions that
  caused them;
- Page 38: `I am ready.` could be read before the approaching `keys` cue.

The builder-side Page 46 and Page 53 catches happened before critic review and
used the same essentials boundary. No redraw was requested merely for nominal
typography size or cosmetic polish.

## Batch critic task actually used

After each canonical batch, the same critic received a separate sequence task:

> Review the canonical pages as one uninterrupted reader sequence under the
> corrected essentials gate: story and emotional continuity; identity,
> setting, and object continuity; speech/source attribution across transitions;
> obvious generation/anatomy integrity; and actual desktop/tablet comfort.
> Typography pixels, cosmetic polish, and nonconsequential variation are
> nonblocking. Create a contact sheet and concise sequence report. Return
> APPROVED or REJECTED with mandatory findings only. Do not edit or promote art
> or the reader.

This was run for Pages 21–30, 31–40, 41–50, and 51–55. The next batch was held
until the preceding sequence gate passed.

## Production lead control loop

The actual loop was:

1. release one prepared page prompt to the builder;
2. receive one candidate, builder audit, and desktop/tablet proofs;
3. send the candidate and page-specific critic brief to the independent critic;
4. ask the builder to prepare—but not generate—the next prompt;
5. inspect the candidate while waiting for the critic;
6. on approval, promote the candidate byte-for-byte and update reader/QA/handoff;
7. release the next page;
8. on a mandatory defect, preserve the failed image and make one complete redraw
   for the named defect;
9. run an uninterrupted sequence gate at each batch boundary.

This separation prevented builder perfectionism without weakening fidelity: the
builder stopped self-optimizing, the critic received the actual page-specific
story and visual requirements, and promotion remained outside both roles.
