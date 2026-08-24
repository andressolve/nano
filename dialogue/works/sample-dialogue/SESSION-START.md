# SESSION-START

This is an image-free framework fixture, not a production authorization. Run
the rehearsal only in a disposable copy so no run capsule remains here:

```sh
studio_tools="$(cd ../.. && pwd)/tools"
rehearsal_root="$(mktemp -d)"
rehearsal_project="$rehearsal_root/sample-dialogue"
cp -R . "$rehearsal_project"
cd "$rehearsal_project"

python3 -B "$studio_tools/check_adaptation.py" .
python3 -B "$studio_tools/check_preproduction.py" .
python3 -B "$studio_tools/assemble.py" \
  script/FULL-SCRIPT.md intent/page-01.md prompts/page-01.md cards/page-01.md run \
  --contract contract/PAGE-CONTRACT.md \
  --candidate review/current/candidate.png \
  --proof review/current/proof-600x900.png \
  --proof review/current/proof-768x1152.png \
  --page 01 --version 1 --mode BASE
python3 -B "$studio_tools/preflight.py" run \
  --script script/FULL-SCRIPT.md --contract contract/PAGE-CONTRACT.md \
  --intent intent/page-01.md --prompt prompts/page-01.md \
  --card cards/page-01.md --page 01
python3 -B "$studio_tools/check_candidate.py" "$studio_tools/fixtures/candidate" \
  --manifest "$studio_tools/fixtures/manifest.toml" \
  --receipt "$studio_tools/fixtures/candidate/hashes.json"
python3 -B "$studio_tools/validate_report.py" reports/valid.md cards/page-01.md
python3 -B "$studio_tools/route.py" reports/history-approved.json
python3 -B "$studio_tools/verify_rehearsal.py" . --write
python3 -B "$studio_tools/verify_rehearsal.py" .
```

`verify_rehearsal.py` confirms both readiness gates, rejects
`reports/invalid.md`, derives and verifies the receipt/handoff in the
disposable copy, and requires zero project PNGs. The deterministic white PNG
under `tools/fixtures/` is a file-contract fixture, not a story page,
reference, or prototype.
