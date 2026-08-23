# SESSION-START

This text-only framework rehearsal runs from this directory and generates no
art. Execute the interfaces exactly:

```sh
python3 -B ../../tools/check_adaptation.py .
python3 -B ../../tools/assemble.py \
  script/page-01.md intent/page-01.md prompts/page-01.md cards/page-01.md run \
  --candidate review/current/candidate.png \
  --proof review/current/proof-600x900.png \
  --proof review/current/proof-768x1152.png \
  --page 01 --version 1 --mode BASE
python3 -B ../../tools/preflight.py run \
  --script script/page-01.md --intent intent/page-01.md --card cards/page-01.md
python3 -B ../../tools/check_candidate.py ../../tools/fixtures/candidate \
  --manifest ../../tools/fixtures/manifest.toml \
  --receipt ../../tools/fixtures/candidate/hashes.json
python3 -B ../../tools/validate_report.py reports/valid.md cards/page-01.md
python3 -B ../../tools/route.py reports/history-approved.json
python3 -B ../../tools/verify_rehearsal.py . --write
python3 -B ../../tools/verify_rehearsal.py .
```

`verify_rehearsal.py` also confirms the adaptation-readiness gate, rejects
`reports/invalid.md`, derives `RECEIPT.md` and `HANDOFF.md` from the executed
results, verifies them, and requires zero PNG files inside this project. Then
stop. The deterministic white PNG outside the project is a file-contract
fixture, not a story page or prototype.
