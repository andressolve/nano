# The Count of Monte Cristo — Production Log

## Current Milestone

**Volume I production completed and locally QA-passed on 2026-07-25.**

- Creative mandate locked.
- Velvet Cinema selected from three generated style directions.
- Five-volume dramatic architecture locked as a working production plan.
- Full 32-page Volume I script completed and lettering-audited.
- Nineteen Volume I reference plates accepted.
- Three hard dialogue prototypes accepted.
- Cover and all 32 finished story pages accepted.
- Landscape reader, end interstitial, five-question quiz, and library card
  completed.
- Every accepted production image validates at **1536 × 1024, 3:2 landscape**.
- Desktop and 390 × 844 mobile-browser QA passed with no page errors.

## Generation Path

All production visuals were generated with the built-in Codex image-generation
path covered by the user's Codex/ChatGPT subscription entitlement.

- No `OPENAI_API_KEY` was used.
- No bundled image-generation CLI was used.
- No direct separately billed OpenAI API request was used.
- Originals remain in the Codex generated-image store; accepted copies live
  under `style-exploration/`, `refs/`, and `pages/`.

## Locked Graphic Direction

The selected direction is **Velvet Cinema**:

- layered matte gouache and opaque watercolor;
- broad economical brushwork and sparse charcoal;
- bold shadow masses;
- selective crisp detail around eyes, mouths, hands, and story objects;
- restrained period palettes with controlled accent colors;
- cinematic blocking that prioritizes faces, gesture, power, and danger.

Avoid photorealism, glossy digital rendering, anime, ornamental engraving
texture, generic pirate imagery, and fantasy-dungeon shorthand.

The production canvas is permanently locked to **1536 × 1024 landscape**. Do
not generate portrait or square story pages, do not crop a landscape page into
another aspect ratio, and do not approve a page whose generated dimensions have
not been checked.

## Accepted Style Exploration

- [`style-exploration/01-romantic-engraving.png`](style-exploration/01-romantic-engraving.png)
- [`style-exploration/02-abyssal-ink.png`](style-exploration/02-abyssal-ink.png)
- [`style-exploration/03-velvet-cinema.png`](style-exploration/03-velvet-cinema.png) — selected
- [`style-exploration/STYLE-EXPLORATION.md`](style-exploration/STYLE-EXPLORATION.md)

## Accepted References

Character locks:

- [`refs/01-edmond-young.png`](refs/01-edmond-young.png)
- [`refs/02-edmond-prison.png`](refs/02-edmond-prison.png)
- [`refs/03-count.png`](refs/03-count.png)
- [`refs/04-faria.png`](refs/04-faria.png)
- [`refs/05-villefort-1815.png`](refs/05-villefort-1815.png)
- [`refs/06-mercedes-1838.png`](refs/06-mercedes-1838.png)
- [`refs/09-mercedes-1815.png`](refs/09-mercedes-1815.png)
- [`refs/10-louis-dantes.png`](refs/10-louis-dantes.png)
- [`refs/11-danglars-1815.png`](refs/11-danglars-1815.png)
- [`refs/12-fernand-1815.png`](refs/12-fernand-1815.png)
- [`refs/13-caderousse-1815.png`](refs/13-caderousse-1815.png)
- [`refs/14-morrel-household.png`](refs/14-morrel-household.png)
- [`refs/15-jacopo-captain.png`](refs/15-jacopo-captain.png)
- [`refs/16-busoni-wilmore.png`](refs/16-busoni-wilmore.png)

Object and setting locks:

- [`refs/07-key-objects.png`](refs/07-key-objects.png)
- [`refs/08-dialogue-settings.png`](refs/08-dialogue-settings.png)
- [`refs/17-pharaon.png`](refs/17-pharaon.png)
- [`refs/18-chateau-dif-escape.png`](refs/18-chateau-dif-escape.png)
- [`refs/19-monte-cristo-treasure.png`](refs/19-monte-cristo-treasure.png)

## Accepted Dialogue Prototypes

1. [`pages/prototype-01-examination.png`](pages/prototype-01-examination.png)
   proves a tense legal exchange with native lettering and correct dramatic
   geography.
2. [`pages/prototype-02-faria-conspiracy.png`](pages/prototype-02-faria-conspiracy.png)
   proves a dense reasoning scene. The final version uses one visible speaker
   per panel after the opening to make eight balloons structurally unambiguous.
3. [`pages/prototype-03-mercedes-recognizes-edmond.png`](pages/prototype-03-mercedes-recognizes-edmond.png)
   proves the later emotional style: nine balloons, withheld recognition, and
   a turn carried by faces and dialogue rather than caption explanation.

## Repairs and Lessons

- The first Villefort sheet drifted too close to Edmond. His face was
  regenerated before downstream use.
- The first examination composition leaked prison imagery into the prosecutor's
  office. The setting was corrected, then the guard balloon tail was corrected.
- Tail-only repairs did not make the first Faria prototype reliably readable.
  The full page was restaged with one speaker per panel after the opening.
- The successful prototype grammar is now: stage speakers in reading order,
  prefer one visible speaker per dense panel, use A–B–A tiers only when needed,
  and inspect every balloon for exact text, count, ownership, and tail endpoint.
- Page 5 was regenerated to correct Louis Dantès's toast attribution.
- Page 14 was fully regenerated to repair the jailer identity and remove a
  duplicate Edmond.
- Page 20 was fully regenerated after a reader audit found Edmond's balloons in
  Panels 1 and 3 pointing left toward Faria. The accepted replacement locks
  Faria on the left and Edmond on the right throughout, with every balloon kept
  on its speaker's side.
- Page 21 was fully regenerated after a reader audit found both opening-panel
  balloons visually swapped. The accepted replacement puts Edmond's “Stay with
  me” on the right and Faria's reply on the left with unambiguous opposing
  tails.
- Page 25 required repeated full-page restaging to lock the captain, Jacopo,
  and Edmond identities and the Edmond–Jacopo–Edmond balloon order.
- Page 31's first prompt was safety-blocked. The scene was restaged around a
  closed pistol case, farewell, clock, and interruption without weakening the
  dramatic turn.
- Do not crop-patch tails, faces, or words. If attribution or identity fails,
  regenerate the full page with clearer blocking.

## Finished Volume I

- [`pages/cover.png`](pages/cover.png)
- [`pages/page-01.png`](pages/page-01.png) through
  [`pages/page-32.png`](pages/page-32.png)
- [`index.html`](index.html) — landscape reader and quiz

The finished-page set contains **33 production images**: one cover and 32 story
pages. Each file is exactly 1536 × 1024. All story lettering is native to the
generated images; the reader adds no story dialogue or captions.

## Reader and Library QA

The local reader passed:

- sequential controls, keyboard controls, click zones, and swipe navigation;
- hash deep links from cover through story, end interstitial, and quiz;
- page title, page count, and progress updates;
- fullscreen control;
- all five quiz questions, answer feedback, and reset behavior;
- responsive rendering at desktop size and a 390 × 844 mobile viewport;
- 3:2 image preservation with no horizontal overflow on mobile.

The root library passed catalog QA with the Monte Cristo card at the top of
“New on the shelf,” the correct cover and summary, and a working link to
`monte-cristo/index.html`. No browser console errors were observed.

## Authoritative Production Set

Use these files together for continuity, repair, or future volumes:

1. [`CREATIVE-MANDATE.md`](CREATIVE-MANDATE.md)
2. [`01-STYLE-GUIDE.md`](01-STYLE-GUIDE.md)
3. [`02-CHARACTERS.md`](02-CHARACTERS.md)
4. [`03-SETTINGS-OBJECTS.md`](03-SETTINGS-OBJECTS.md)
5. [`05-PROTOTYPE-SCRIPTS.md`](05-PROTOTYPE-SCRIPTS.md)
6. [`06-VOLUME-1-SCRIPT.md`](06-VOLUME-1-SCRIPT.md)
7. the accepted reference images named above.

The script's exact dialogue remains authoritative. Lettering stays baked into
the page images. The reader remains navigation and quiz infrastructure only.

## Next Gate

Volume I is complete locally. The next external gate is publication, but only
when explicitly requested. Follow the repository rule: publish routine finished
work directly on `main`, stage only the Monte Cristo and catalog paths, push
`origin main`, then verify the GitHub Pages library and reader.
