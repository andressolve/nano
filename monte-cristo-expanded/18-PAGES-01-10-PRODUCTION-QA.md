# The Count of Monte Cristo — Pages 1–10 Production QA

## Current status

**The complete revised Pages 1–10 batch is approved as of 2026-08-02.** Andres's
reader QA first rejected the terse Page 5 question `Tomorrow?` and Page 8's
inferential two-paper trick. The approved pages now ask `Will you marry me
tomorrow?` / `Tomorrow—and every day after.`, give the family toast three safe
face-led panels, and follow one intact accusation from the tavern table into
official hands.

Pages 3–8 were regenerated in full after the 55-page script revision. All ten
current canvases under [`pages/`](pages/) are flattened **1024 × 1536 portrait
RGB PNGs** with native lettering. Matching 390 × 585 reader-size copies are
under [`qa/mobile-pages/`](qa/mobile-pages/).

The revised batch passed two sequential independent gates:

1. **Script fidelity:** Pages 3–8 passed after five rounds, including exact
   wording, panel order, speaker lanes, tail ownership, silent characters,
   identity locks, and format. See
   [`22-PAGES-03-08-SCRIPT-FIDELITY-CRITIC.md`](22-PAGES-03-08-SCRIPT-FIDELITY-CRITIC.md).
2. **Cold read and visual integrity:** Pages 1–10 passed on the first blind
   round for first-time-reader comprehension at 390 px, page-to-page causality,
   character recognition, anatomy, props, and generation defects. See
   [`23-PAGES-01-10-COLD-READ-VISUAL-CRITIC.md`](23-PAGES-01-10-COLD-READ-VISUAL-CRITIC.md).

The earlier reports in files 16 and 17 remain historical records for the
superseded pre-reader-QA batch.

## Accepted-version map

| Page | Accepted production version | Material regeneration history |
| --- | --- | --- |
| 1 | v1 | First candidate passed both gates |
| 2 | v1 | First candidate passed; short tail endpoints remain nonblocking |
| 3 | v4 | Replaced the superseded dialogue with the natural `you have grown thinner` and `there will always be food` exchange; food imagery now follows cause and time |
| 4 | v3 | Names Mercédès and Edmond, makes Edmond's harbor arrival explicit, and asks the concrete shared-life question |
| 5 | v10 | Adds the explicit marriage proposal; after repeated Louis-tail failures, the approved six-panel page resolves the toast as an Edmond → Mercédès → Louis triptych with one foreground speaker per panel |
| 6 | v2 | Replaces three expository soliloquies with one illustrated-prose field and four silent motive/convergence bands |
| 7 | v3 | Makes the innocent-man objection and police consequence explicit; regenerated once to move Caderousse's final warning tail from his hand to his speaker lane |
| 8 | v2 | Replaces the clunky two-paper trick with one intact accusation followed continuously from writing through official delivery |
| 9 | v3 | v1 contained Edmond-like male guests; v2 recast the crowd but placed the chorus in a low white strip; v3 keeps one Edmond, restores tied-hair Fernand, uses a distinct female toast speaker, and integrates the chorus inside the final panel |
| 10 | v3 | v1 contained Edmond-like doubles; v2 corrected the cast but let Morrel's tail land beside a silent woman; v3 isolates Morrel's speaker lane and passes attribution review |

Rejected and intermediate images remain under
[`qa/production-pages/`](qa/production-pages/) for auditability. They are not
story-page candidates.

## Cold-reader result

Without the script or production notes, the final critic could follow this
complete causal chain:

1. Edmond brings the *Pharaon* and its crew home after Leclère's death.
2. Morrel offers him command while Danglars marks the Elba stop as a threat.
3. Edmond discovers the cost of Louis's debt repayment and makes captaincy
   mean material security.
4. Mercédès rejects Fernand and visibly welcomes the newly arrived Edmond.
5. Edmond, Mercédès, and Louis define the life they expect tomorrow.
6. Danglars, Fernand, and Caderousse receive separate motives before meeting.
7. Danglars proposes using Edmond's Elba letter to make the police imprison him,
   while Caderousse objects that Edmond is innocent.
8. Danglars writes the accusation, Caderousse fails to stop it, and Fernand
   delivers the same paper to an official.
9. The family celebrates in ignorance while Fernand remains outside.
10. Officers interrupt the feast; Edmond expects only a brief examination by
    Villefort.

The delayed danger of Elba remains suspense. It no longer reads as omitted
story logic.

## Production cautions carried forward

- Enforce
  [`19-ANTI-TERSE-DIALOGUE-MANDATE.md`](19-ANTI-TERSE-DIALOGUE-MANDATE.md):
  every consequential short line needs an explicit action/object and a single
  unmistakable referent.
- Enforce
  [`20-EFFORTLESS-STORY-CRITIC-MANDATE.md`](20-EFFORTLESS-STORY-CRITIC-MANDATE.md):
  “recoverable” is not approval, natural dialogue outranks procedural
  explanation, and essential story logic cannot depend on tiny prop mechanics.
- Lock the predominant Pages 3–5 and 7–10 balloon-lettering family for Page 11
  onward. Do not continue alternating between that face and the more serifed
  Pages 1–2/6 face.
- On any future Page 1 regeneration, make the rope-and-sail action the dominant
  field rather than the harbor establishing image.
- On any future Page 2 regeneration, lengthen the short Danglars and Morrel
  tails into their mouth lanes and restore subtle silent crew in Panel 4.
- On any future Page 6 regeneration, preserve the single protected prose field
  and silent motive bands; lower the prose field if its upper margin tightens.
- Preserve Page 8's one intact accusation from table to Fernand to the
  uniformed official; no decoy, torn scrap, or subtle handwriting distinction
  may carry causality.
- Reuse Page 5's one-speaker-per-panel triptych whenever a group exchange makes
  tail ownership fragile. Solve attribution in staging, never by patching.
- On any future Page 10 regeneration, lower the short `I will follow.` tail tip
  closer to Morrel's mouth. Its current ownership is unambiguous and approved.
- Preserve the crowd discipline proven on Pages 9–10: no background figure may
  inherit a lead character's complete hair, face, age, silhouette, and costume
  stack.

## Production method

The pages were generated with the built-in subscription-backed Codex image
generation path. No API key, direct Image API billing, overlay lettering,
crop-patched tail, or face patch was used. Every failed page was regenerated
as a complete page.

The reproducible baseline prompt set is recorded in
[`15-PAGES-01-10-PRODUCTION-PROMPTS.md`](15-PAGES-01-10-PRODUCTION-PROMPTS.md).
The accepted regeneration deltas are the version notes above and the exact
repair prescriptions in the two critic reports.

## Production gate complete

Andres completed this checkpoint review on 2026-08-02. The same critic then
audited the complete Pages 1–55 script under
[`19-ANTI-TERSE-DIALOGUE-MANDATE.md`](19-ANTI-TERSE-DIALOGUE-MANDATE.md) and
[`20-EFFORTLESS-STORY-CRITIC-MANDATE.md`](20-EFFORTLESS-STORY-CRITIC-MANDATE.md).
Round 5 granted unconditional approval in
[`21-COMPLETE-SCRIPT-EFFORTLESS-STORY-CRITIC.md`](21-COMPLETE-SCRIPT-EFFORTLESS-STORY-CRITIC.md).
Pages 3–8 were then regenerated and the finished Pages 1–10 sequence passed
both image gates in reports 22 and 23. The next production batch begins at
Page 11; the historical Pages 12–13 prototypes must be regenerated from the
current approved script rather than reused.
