# SESSION-START

This file runs from `dialogue/works/<project>/`. Read only this project,
`../../PLAYBOOK.md`, and `../../PROMPTING.md`. Current state is
`HANDOFF.md`.

Before story-page generation, run:

```sh
python3 -B ../../tools/check_preproduction.py .
```

Require `PREPRODUCTION READY FOR PAGE PRODUCTION`. The included adaptation
gate opens reference preparation only; it is not page-production authority.
Then read only `preproduction/PREPRODUCTION-HANDOFF.md`, the separate owner
production approval, `HANDOFF.md`, and current disk state. Do not open
research, the whole script, neighboring packets, or source-fidelity arguments.
Do not generate prototypes, use API billing, alter story authority, or add
overlay lettering.

Assemble the current page. The tool extracts one exact script and contract
block from the whole locked documents:

```sh
python3 -B ../../tools/assemble.py script/FULL-SCRIPT.md \
  intent/page-NN.md prompts/page-NN.md cards/page-NN.md run \
  --contract contract/PAGE-CONTRACT.md \
  --candidate review/current/candidate.png \
  --proof review/current/proof-600x900.png \
  --proof review/current/proof-768x1152.png \
  --reference refs/approved/REQUIRED.png \
  --page NN --version K --mode BASE
python3 -B ../../tools/preflight.py run \
  --script script/FULL-SCRIPT.md --contract contract/PAGE-CONTRACT.md \
  --intent intent/page-NN.md --prompt prompts/page-NN.md \
  --card cards/page-NN.md --page NN
```

Dispatch one fresh builder, check its production folder with
`check_candidate.py`, copy only candidate/proofs to the neutral review capsule,
then dispatch one fresh blind critic. Validate the report and route JSON history
with `route.py`. Stop on an invalid report or owner hold.
