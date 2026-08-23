# SESSION-START

This file runs from `dialogue/works/<project>/`. Read only this project,
`../../PLAYBOOK.md`, and `../../PROMPTING.md`. Current state is `HANDOFF.md`.

Before any reference or page generation, run
`python3 -B ../../tools/check_adaptation.py .` and require `ADAPTATION READY`.
That result requires the exact owner-approved script and contract paths and a
`Status: LOCKED` marker inside each document; folder contents alone are not
approval.
Do not open research dossiers or re-litigate source fidelity during production.
Then confirm owner-approved complete script/page contract;
exact-text, causality, and readability approval; casting anti-collision and
approved identity/object references; style anchor; `manifest.toml`; current
promoted page; active batch; and scoped worktree status. Do not generate a
prototype, use API billing, alter story documents, or add overlay lettering.

Assemble the current page with explicit script, intent, builder prompt, card,
version-neutral review paths, page/version/mode, and approved references:

```sh
python3 -B ../../tools/assemble.py SCRIPT INTENT PROMPT CARD run \
  --candidate review/current/candidate.png \
  --proof review/current/proof-600x900.png \
  --proof review/current/proof-768x1152.png \
  --reference refs/approved/REQUIRED.png \
  --page NN --version K --mode BASE
python3 -B ../../tools/preflight.py run \
  --script SCRIPT --intent INTENT --card CARD
```

Dispatch one fresh builder, check its production folder with
`check_candidate.py`, copy only its candidate/proofs to the version-neutral
review capsule, then dispatch one fresh blind critic. Validate the report and
route its JSON history with `route.py`. Stop on invalid report or owner hold.
