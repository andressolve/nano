# NEW-WORK

This file governs research, adaptation, and pre-production from the project
directory. Read `../../AUDIENCE.md`, `../../ADAPTATION.md`,
`../../PREPRODUCTION.md`, this project's `README.md`, current `HANDOFF.md`,
and the smallest relevant source set. Do not load production manuals or
historical archives unless a bounded question requires them.

Run fresh, question-bounded research tasks into `research/`. Synthesize their
results before adaptation; do not carry raw transcripts forward. Build the
audience promise, adaptation brief, architecture, graphical direction,
production-complete panel script, page contract, and whole-script readability
report. Use a fresh two-stage audience critic that sees the complete story
before protected claims and never grades general source fidelity.

End story design by directly presenting `adaptation/GREENLIGHT.md`. Do not
generate references, style explorations, story pages, or prototypes. After
explicit story approval, record exact audience, adaptation, architecture,
graphical direction, audience-report, greenlight, script, contract, and
readability paths and SHA-256 values plus page count in
`adaptation/OWNER-APPROVAL.md`, then run:

```sh
python3 -B ../../tools/check_adaptation.py .
```

A clean result opens bounded reference preparation only. Complete casting,
setting/object, reference, every-page sibling, context, second owner approval,
and pre-production handoff artifacts under `../../PREPRODUCTION.md`, then run:

```sh
python3 -B ../../tools/check_preproduction.py .
```

Only that exact clean result permits `SESSION-START.md`.
