# Page 9 v2 manifest resolution

- Prompt source: `12-PRODUCTION-PLAN.md` §5, Page 9.
- Saved prompt: `prompts/page-09-v2.md`.
- Verification: the full current §5 Page 9 generation prompt remains byte-identical to `prompts/page-09-v1.md`, followed only by the authorized v2 correction naming the omitted opening `Danglars.` defect.
- Prompt SHA-256: `850fe2965adb9a1d334ae305a286f47612efcfcf56f8b4009b3193f587f435ad`.
- Manifest count: exactly five image inputs, at the production cap; no other image is permitted.

## Permanent approved inputs — resolved

1. `refs/approved/06-danglars-1838.png`
   - Exists: yes
   - SHA-256: `626f71c601069032624654958a24b06dfc33974d290d6c9d09d627f3f1e4beb9`
   - Canvas: 1536 × 1024, 8-bit RGB PNG
2. `refs/approved/08-villefort-1838.png`
   - Exists: yes
   - SHA-256: `46e31557dd3fd34d3a103e028721869dba5dc0b16874bb40dc00f0982c262e75`
   - Canvas: 1536 × 1024, 8-bit RGB PNG
3. `refs/approved/01-count-1838.png`
   - Exists: yes
   - SHA-256: `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`
   - Canvas: 1536 × 1024, 8-bit RGB PNG
4. `refs/approved/18-set-morcerf-house.png`
   - Exists: yes
   - SHA-256: `f69809a0cc54174ed7706af8ef3c83c9dbf0b5dcf763398953f477c412971e96`
   - Canvas: 1536 × 1024, 8-bit RGB PNG

## Required predecessor — resolved

5. `pages/page-08.png`
   - Exists: yes; exact 1024 × 1536, 8-bit RGB PNG.
   - SHA-256: `1bc3fe5585548b72e57b335daa3ca65e3d85e95ae3d2336cb763144d0d13e93e`.
   - Promotion record: Page 8 v14 unconditionally approved and promoted byte-for-byte.

## Release

Page 9 v2 generation is RELEASED. Attach exactly the five resolved inputs above: approved Danglars, approved Villefort, approved Count, approved Morcerf-house set, and promoted Page 8. Attach no rejected candidate, including Page 9 v1, and no unlisted image.
