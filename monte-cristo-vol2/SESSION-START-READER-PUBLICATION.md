# Monte Cristo Volume II — reader and publication

Run this as one new bounded task with the directory containing this file as the
workspace and current working directory.

## Model topology

- Orchestrator: GPT-5.6 Luna, medium.
- Implementation builder: one GPT-5.6 Luna, low. It may retain its coding
  context for one targeted correction round.
- Reader critic: fresh zero-history GPT-5.6 Sol, medium for each review.

No image generation is permitted. Do not reopen story-page production.

## Preflight

1. Read `HANDOFF.md` and confirm Pages 1–49 are complete and all final gates are
   cleared.
2. Run `python3 qa/_assembly/verify.py`; require `CLEAN`.
3. Confirm exactly 49 canonical page files and no Page 50.
4. Confirm the checkout is `main`. Preserve every unrelated dirty-worktree
   change.
5. Confirm `../.gitignore` contains `monte-cristo-vol2/qa/**/*.png` and that raw
   QA candidates/proofs are ignored before any staging.

## Build and review

1. Launch the Luna-low builder with only `qa/_publication/BUILDER.md` as its
   task packet.
2. Run `python3 qa/_publication/verify-reader.py`. Mechanical verification must
   print `CLEAN` before visual review.
3. Launch one fresh Sol-medium critic with only
   `qa/_publication/CRITIC.md` as its task packet.
4. If the critic returns `REVISE`, give the report to the same builder for one
   targeted correction, rerun the verifier, and use one fresh critic. If the
   second critic still returns `REVISE`, stop and report the blocker; do not
   drift into unbounded polish.
5. On `APPROVED`, write `READER-PUBLICATION-VERIFICATION.md` recording page
   integrity, manifest coverage, reader features, quiz coverage, critic verdict,
   and local desktop/tablet browser checks.
6. Update `HANDOFF.md` and `../MONTE-CRISTO-VOLUME-2-HANDOFF.md` to record the
   finished reader and publication state.

## Publish directly to main

The repository rule is binding: routine completed work publishes directly to
`main`.

1. Review the final status and diff. Stage only:
   - `../.gitignore`
   - `../stories.js`
   - `../MONTE-CRISTO-VOLUME-2-HANDOFF.md`
   - the complete nonignored `monte-cristo-vol2/` project directory
2. Do not stage unrelated modified files elsewhere in the repository. Never use
   `git add -A`, stash, reset, clean, or force-push.
3. Commit with a concise Volume II reader/publication message and push
   `origin main`.
4. Verify local `HEAD` equals `origin/main`.
5. Wait for GitHub Pages deployment using bounded checks, then verify both:
   - `https://andressolve.github.io/nano/`
   - `https://andressolve.github.io/nano/monte-cristo-vol2/index.html`
6. Confirm the public library card, reader assets, first/middle/final page,
   navigation, end state, quiz, and Volume I link work without console or 404
   failures.

Report the commit, public URL, verifier result, critic verdict, and deployment
verification. Stop after publication; Volume III planning is a separate task.
