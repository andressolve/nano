# The Count of Monte Cristo — Pages 21–30 Production QA

## Status

**BATCH APPROVED. Pages 21–30 are individually approved, canonical, and passed
the fresh uninterrupted sequence gate on 2026-08-07. Production may continue
at Page 31.**

Display target for future pages: desktop monitor first, tablet second. The
Page 21 390 × 585 proof remains part of its historical audit trail, but phone
comfort is not a gate for Page 23 onward.

Typography correction from Andres on 2026-08-07: do not reject a page merely
because some native glyph bands miss a nominal source-pixel target. Exact text
and comfortable normal desktop/tablet reading are binding. Pixel measurements
are diagnostic unless the displayed text is actually cramped, tiring,
malformed, cropped, ambiguous, or requires zoom.

Critic-scope correction from Andres on 2026-08-07: keep the gate reasonable and
essential. Block for script unfaithfulness, incorrect speech/sound attribution,
or obvious generation-integrity failures such as extra/missing/fused limbs,
digits, faces, bodies, or actors. Do not create new full-page revisions over
font pixels, exact panel ratios, tiny safe-margin differences, exact tail-gap
measurements, or phone rendering when the normal desktop/tablet page reads
clearly.

This batch uses the independent builder/critic loop defined in
[`29-PAGES-21-55-BUILDER-CRITIC-WORKFLOW.md`](29-PAGES-21-55-BUILDER-CRITIC-WORKFLOW.md).
Every generated page remains under `qa/production-pages-21-30/` until a
separate critic grants unconditional approval.

## Page 21 — The Years Without an Answer

Canonical page: [`pages/page-21.png`](pages/page-21.png)

Approved candidate: `qa/production-pages-21-30/page-21-v7.png`

Independent approval:
[`qa/production-pages-21-30/page-21-v7-critic-report.md`](qa/production-pages-21-30/page-21-v7-critic-report.md)

Canonical mobile proof:
`qa/mobile-pages-21-30/page-21-mobile.png`

### Iteration record

| Version | Disposition | Reason |
| --- | --- | --- |
| v1 | Builder rejected | Duplicated the distant jailer. |
| v2 | Critic `REVISE` | Prose allocation was too compressed at 390 px, the sole tail ended far from Edmond's mouth, and speech used the wrong family/scale. |
| v3 | Builder rejected | Improved allocation and speech but violated the top safe margin and retained the remote tail. |
| v4 | Builder rejected | Fixed the safe margin; tail remained remote. |
| v5 | Builder rejected | Tail stopped at Edmond's hair rather than open space beside his mouth. |
| v6 | Critic `REVISE` | All prior blockers passed, but the refusal hand had six digits. |
| v7 | Critic `APPROVED` | Exact text, layout, typography, tail attribution, five-digit anatomy, identity, style, period detail, mobile readability, and comprehension all passed. |

No failed page was patched, cropped, composited, relettered, or partially
repainted. Every change was a complete subscription-backed ImageGen
regeneration.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-21.png` | `a2401a04fe1ea57055cf5b2069efda5283bda43a8872f545bd9e889880345764` |
| `qa/mobile-pages-21-30/page-21-mobile.png` | `926efdcc99374e46f566135044a648dafa02e72692569aafd4113295a6d363c8` |

Byte comparison confirmed that both canonical files are identical to the
critic-approved source and mobile proof.

## Page 22 — The Sound

Canonical page: [`pages/page-22.png`](pages/page-22.png)

Approved candidate: `qa/production-pages-21-30/page-22-v77.png`

Independent approval:
[`qa/production-pages-21-30/page-22-v77-critic-report.md`](qa/production-pages-21-30/page-22-v77-critic-report.md)

Display proofs:

- `qa/production-pages-21-30/page-22-v77-desktop.png` — 600 × 900
- `qa/production-pages-21-30/page-22-v77-tablet.png` — 768 × 1152

### Iteration record

Page 22 required an unusually long but fully non-destructive production loop.
The original builder preserved v1–v48, including critic revisions at v9 and
v23, before documenting a coupled layout/attribution impasse. A fresh builder
then restarted from the approved script, canonical Page 21, and accepted
identity/style references only. It generated v49–v77 without using rejected
Page 22 images as references. V77 was the first fresh candidate to pass builder
QA and the independent critic's complete regression gate.

The approved page passes:

- all eight exact text elements once and in causal order;
- the four-panel food refusal → stillness → answer sequence;
- jailer/Edmond speaker ownership and local mouth-directed tails;
- a full first-sound pause and the final `Who` → double scrape → `Again` order;
- Prison Edmond and jailer identity, period setting, Velvet Cinema continuity,
  anatomy, the five-digit wall hand, and the no-Faria/no-tunnel boundary;
- desktop and tablet reader comfort without using phone size as a binding gate.

No failed page was patched, cropped, composited, relettered, or partially
repainted. Every image change was a complete subscription-backed ImageGen
regeneration.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-22.png` | `605440eebb95a02b23d362fc7b352a651ec80ec9635afd9b40f4b09975ab7f95` |
| `qa/production-pages-21-30/page-22-v77-desktop.png` | `34b9f722fdb07faca3ac525c53679f7b0405f900e1e4d380064fd00f5698523c` |
| `qa/production-pages-21-30/page-22-v77-tablet.png` | `3051da2aa22ee52deff20672a7b21a959ef5144ba6b8dff4423daf81b21170a7` |

Byte comparison confirmed that `pages/page-22.png` is identical to the
critic-approved v77 source. The critic independently re-derived and
byte-verified both display proofs.

## Page 23 — Beneath the Stone

Canonical page: [`pages/page-23.png`](pages/page-23.png)

Approved candidate:
`qa/production-pages-21-30/page-23-reset-v1.png`

Independent approval:
[`qa/production-pages-21-30/page-23-reset-v1-fresh-critic-report.md`](qa/production-pages-21-30/page-23-reset-v1-fresh-critic-report.md)

Display proofs:

- `qa/production-pages-21-30/page-23-reset-v1-desktop.png` — 600 × 900
- `qa/production-pages-21-30/page-23-reset-v1-tablet.png` — 768 × 1152

Prompt and last builder audit:

- `qa/production-pages-21-30/page-23-reset-v1-prompt.md`
- `qa/production-pages-21-30/page-23-reset-v1-builder-rejection.md`

The reset builder initially rejected this page only because several source
glyph bands measured about 33–38 px. That disposition predated Andres's
typography-gate correction. A fresh independent critic applied the corrected
reasonable-essentials gate and approved the candidate unconditionally because
the exact lettering is comfortable at desktop and tablet sizes and the page
has no script, attribution, or generation-integrity defect.

Reset v1 otherwise passed the builder's complete locked gate:

- exact 1024 × 1536 RGB source and all nine exact strings once, in order and
  sentence case;
- exactly five panels, with Panel 4 largest and Panel 5 shortest/silent;
- every connected ivory field inside the real 64 px safe area, including the
  first field at y=110;
- Edmond's attached exposed ear visibly pressed to and partly occluded by the
  scrape-bearing stone while his mouth remains visible;
- short crude period tool, closed floor seam in Panel 3, first clear opening in
  Panel 4, and both hidden-Voice tails entering that opening;
- mouth-local Edmond tails, including `Beneath me?`;
- one living five-digit hand in Panel 5, with no owner, Faria, lamp, second
  figure, or extra text visible;
- comfortable and unambiguous 600 × 900 desktop and 768 × 1152 tablet proofs.

Recorded hashes:

| File | SHA-256 |
| --- | --- |
| `qa/production-pages-21-30/page-23-reset-v1.png` | `dc1ae679a47fd748bea75ce144d07c5724c6e9c348dbf3b2f6c95d8edd7e87f4` |
| `qa/production-pages-21-30/page-23-reset-v1-desktop.png` | `302f9175f44b3c4a9ba0fdd3ed6a131ebdf6c4409f6b985c43662b1408128b10` |
| `qa/production-pages-21-30/page-23-reset-v1-tablet.png` | `d75aad8a79f4a8bf6afaeeae4371761d1a7abd9ba3a2b4e26cccbacd08f10f89` |

The approved source was promoted byte-for-byte to `pages/page-23.png`. All
prior generations, prompts, desktop/tablet proofs, and rejection notes remain
preserved in the same QA directory.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-23.png` | `dc1ae679a47fd748bea75ce144d07c5724c6e9c348dbf3b2f6c95d8edd7e87f4` |

Byte comparison confirmed that `pages/page-23.png` is identical to the
critic-approved reset-v1 source.

## Page 24 — Prisoner Twenty-Seven

Canonical page: [`pages/page-24.png`](pages/page-24.png)

Approved candidate: `qa/production-pages-21-30/page-24-v1.png`

Independent approval:
[`qa/production-pages-21-30/page-24-v1-critic-report.md`](qa/production-pages-21-30/page-24-v1-critic-report.md)

The builder performed one practical essentials audit and submitted the first
candidate without cosmetic regeneration. The independent critic approved it
unconditionally: all eight exact lines, Faria-left/Edmond-right attribution,
the four-panel first meeting, character identity, cell continuity, anatomy,
and desktop/tablet comfort passed.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-24.png` | `928b921dc0ad25cc15449e7309ee99a38fd5168954e89d31969a5c2130350caf` |

Byte comparison confirmed that `pages/page-24.png` is identical to the
critic-approved v1 source.

## Page 25 — North, Not East

Canonical page: [`pages/page-25.png`](pages/page-25.png)

Approved candidate: `qa/production-pages-21-30/page-25-v1.png`

Independent approval:
[`qa/production-pages-21-30/page-25-v1-critic-report.md`](qa/production-pages-21-30/page-25-v1-critic-report.md)

The first candidate passed the builder's single essentials check and the
independent critic unconditionally. All nine exact lines, the north-tower
deduction, Faria/Edmond attribution, corrected route, actor identity, anatomy,
and desktop/tablet comfort passed. The critic kept minor sea-impact emphasis
and tail geometry nonblocking because neither affected the visible story or
speaker ownership.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-25.png` | `4c576c4f591238cb5ed90d20b7127f09239b2e94c86bfdfe1a3b30682ee3e30a` |

Byte comparison confirmed that `pages/page-25.png` is identical to the
critic-approved v1 source.

## Page 26 — We

Canonical page: [`pages/page-26.png`](pages/page-26.png)

Approved candidate: `qa/production-pages-21-30/page-26-v1.png`

Independent approval:
[`qa/production-pages-21-30/page-26-v1-critic-report.md`](qa/production-pages-21-30/page-26-v1-critic-report.md)

The dense twelve-balloon first candidate passed the builder's single
essentials check and the independent critic unconditionally. Exact text, the
five-panel work cycle, both A-B-A exchanges, the silent guard fragment,
Edmond/Faria identity, anatomy, decisive props, and desktop/tablet comfort all
passed. Minor painterly tail placement remained nonblocking because ownership
was unmistakable.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-26.png` | `14a1c8b8d348205b4adeefbd9f44787b6d14d81fccc4eff994062cc0ddc443a8` |

Byte comparison confirmed that `pages/page-26.png` is identical to the
critic-approved v1 source.

## Page 27 — Italian First

Canonical page: [`pages/page-27.png`](pages/page-27.png)

Approved candidate: `qa/production-pages-21-30/page-27-v4.png`

Independent approval:
[`qa/production-pages-21-30/page-27-v4-critic-report.md`](qa/production-pages-21-30/page-27-v4-critic-report.md)

V1 was preserved after a materially contradictory arithmetic prop. V2 reached
the critic, who returned `REVISE` because Panels 2 and 4 reversed the scripted
cause-and-response order. V3 preserved that same Panel 4 blocker. The complete
v4 redraw resolved both vertical sequences and passed the critic
unconditionally. Exact accent contrast, attribution, arithmetic lesson,
identity, generation integrity, and desktop/tablet comfort passed; the critic
treated painterly stone spacing and tail geometry as nonblocking.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-27.png` | `4e6289ada818b551d64cb6d3e5258fe9433c6c4d2c8ca6f10fcfeadeb41f5007` |

Byte comparison confirmed that `pages/page-27.png` is identical to the
critic-approved v4 source.

## Page 28 — The School Beneath the Prison

Canonical page: [`pages/page-28.png`](pages/page-28.png)

Approved candidate: `qa/production-pages-21-30/page-28-v1.png`

Independent approval:
[`qa/production-pages-21-30/page-28-v1-critic-report.md`](qa/production-pages-21-30/page-28-v1-critic-report.md)

The first candidate passed the builder and critic unconditionally. The full
prose field is exact, comfortable, and uncropped; the lower montage clearly
reads as five successive stages of education, tunnel work, argument, affection,
and care. Identity, elapsed-time repetition, anatomy, props, and
desktop/tablet hierarchy passed without a cosmetic rerun.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-28.png` | `140deaaef0694cc93a8c62589e8ee1a3c611feb6bc2dd1abc21e96b82ed620d5` |

Byte comparison confirmed that `pages/page-28.png` is identical to the
critic-approved v1 source.

## Page 29 — A New Mind

Canonical page: [`pages/page-29.png`](pages/page-29.png)

Approved candidate: `qa/production-pages-21-30/page-29-v1.png`

Independent approval:
[`qa/production-pages-21-30/page-29-v1-critic-report.md`](qa/production-pages-21-30/page-29-v1-critic-report.md)

The first candidate passed unconditionally. All eleven strings, the em dash in
`wants—or`, silent symbolic insets, P4 A-B-A exchange, reversed Page 5 lanes,
final moral interruption, identity, anatomy, and desktop/tablet comfort passed.
Painterly tail geometry and inset detail remained appropriately nonblocking.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-29.png` | `d70c99d31540fc2a9f25fba2069c17bd8efa5b6534cf2ef2ecf1b282b168b562` |

Byte comparison confirmed that `pages/page-29.png` is identical to the
critic-approved v1 source.

## Page 30 — Tell Me the Story

Canonical page: [`pages/page-30.png`](pages/page-30.png)

Approved candidate: `qa/production-pages-21-30/page-30-v1.png`

Independent approval:
[`qa/production-pages-21-30/page-30-v1-critic-report.md`](qa/production-pages-21-30/page-30-v1-critic-report.md)

The first candidate passed unconditionally. Exact text and accents, protected
Edmond-first/Faria-second causal tiers, silent evidence objects, attribution,
fact-first investigation, identity, anatomy, and desktop/tablet comfort all
passed. Minor gutter overlap and tentative diagram marks remained nonblocking.

### Promoted-file identity

| File | SHA-256 |
| --- | --- |
| `pages/page-30.png` | `4dff2aac810b75b102a69f649f5f45915cf1b7625f6055637581e754ab6000d3` |

Byte comparison confirmed that `pages/page-30.png` is identical to the
critic-approved v1 source.

## Pages 21–30 sequence gate

Independent report:
[`qa/production-pages-21-30/pages-21-30-sequence-gate.md`](qa/production-pages-21-30/pages-21-30-sequence-gate.md)

Contact sheet:
`qa/production-pages-21-30/pages-21-30-contact-sheet.png`

Verdict: `APPROVED` with no mandatory findings. The ten-page movement passes
story continuity and emotional rhythm, Edmond/Faria identity and setting/object
continuity, speech/source attribution, generation integrity, and desktop/tablet
comfort. Minor finish, framing, lettering-family, wall geometry, and palette
differences were correctly kept nonblocking.

## Next

Begin Page 31 under the same builder/critic loop.
