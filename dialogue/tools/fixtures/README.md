# Framework fixtures

`candidate/` contains deterministic white PNGs, prompt/audit text, and a hash
receipt. They are file-contract fixtures, not story art or prototypes.
`make_png_fixtures.py` rebuilds them from standard-library code.

`routes/` contains one archived JSON history for every terminal router outcome:
`PROMOTE`, `TARGETED`, `FULL_PROMPT_RESET`, `RESISTANT_DEFECT_HOLD`,
`V4_OWNER_HOLD`, and `INVALID_CRITIC_REPORT`. The test suite loads every file
and also exercises exact-script transport, authority leakage, placeholder
reports, generic `C5`/`C6` criteria, and IHDR-only truncation.
