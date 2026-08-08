# French Comics

This is Nano’s learner-facing collection of short comics using language from Francisco’s French Starter course.

## Published structure

- `index.html` — collection landing page
- `catalog.js` — single source of truth for published French comics
- `<comic-slug>/index.html` — finished reader
- `<comic-slug>/pages/` — published comic page images

Production references and notes may live inside an accepted comic’s folder, but the collection page exposes only the reader and finished page.

## Collection rules

- One short, complete comic page per entry unless a later format is explicitly approved.
- Language comes from lessons the students have already completed.
- Natural situations first; no manufactured mystery, twist, or vocabulary gimmick.
- Dialogue is baked into the generated comic page.
- Optional comprehension checks remain secondary to the comic.
- Only finished, accepted comics are added to `catalog.js`.
- Failed experiments and abandoned concepts remain outside this learner-facing catalog.

## Adding a comic

1. Create the finished project at `french/<comic-slug>/`.
2. Verify its reader, page, language, and lesson alignment.
3. Add one entry to `catalog.js`.
4. Do not add each individual comic to Nano’s main `stories.js`; that catalog contains one entry for the French Comics collection itself.
