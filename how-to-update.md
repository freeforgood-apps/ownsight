# How to update Ownsight

This repo (freeforgood-apps/ownsight) is the source. `index.html` is the whole app. `rebuild.py` (in this repo) refreshes the privacy lock and sets the version.

## Steps for any change
1. Get the current files from this repo.
2. Edit `index.html`. Keep the app in one file.
3. Run `python3 rebuild.py <new version>` in the repo folder (or `python3 rebuild.py` to refresh the lock only). It refreshes the privacy lock and sets the version in `index.html` and `sw.js`. `python3 rebuild.py --check` changes nothing and says if the lock or the versions are out of date.
4. Test everything the "Verify" rule in PROGRESS.md lists. Run the toolkit's accessibility checker on every tab (set the toolkit up first, see its README):
   ```
   node /tmp/toolkit/a11y-check.mjs http://127.0.0.1:8770/index.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' http://127.0.0.1:8770/index.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' http://127.0.0.1:8770/index.html
   node /tmp/toolkit/a11y-check.mjs --click '#writeStages button[data-stage="thinking"]' http://127.0.0.1:8770/index.html
   ```
   Add a line for every new sheet or screen. A `matched nothing` error means the taps changed, so fix the list.

   The full See tab, the sheets and the card after saving need saved thoughts or typed words, and the checker can only tap, not type. Until the self-test can do this (the safety-net stage), serve a test copy of the app on another port from a scratch folder, **never this repo** (a page that writes made-up thoughts must never be published, since it would replace someone's real ones). In that folder put:
   - `seed.html`, which saves about 23 made-up thoughts into record `state` of database `ownsight-v1` (store `data`, value `{ rev: 1, json }`), then opens `index.html`. The data is version 2: `{ v: 2, thoughts: [{ id, text, stage, feel, at, steps: [{ stage, at, note }] }], settings: {} }`. Spread them over the last 8 or 9 days, with most at `thinking`, some at `planning` and a few at `did` (each with its steps, some notes empty), some `feel` set to `lifts` or `weighs`, and the newest at `did`. With `?kind=damaged` it saves `json: "{oops"` instead.
   - `draft.html`, a copy of `index.html` with made-up words already inside the `writeText` box (only the markup changes, so the privacy lock still fits). Tapping a stage there saves, so the card after saving can be checked.

   Then run:
   ```
   node /tmp/toolkit/a11y-check.mjs http://127.0.0.1:8771/seed.html 'http://127.0.0.1:8771/seed.html?kind=damaged'
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#recentList button.entry' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#recentList li:nth-child(2) button.entry' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#recentList li:nth-child(6) button.entry' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' --click '#waitGo' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' --click '#waitGo' --click '#sheetBody button.next' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' --click '#waitGo' --click '#sheetBody button.next' --click '#sheetBody .actions button.primary' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#recentList button.entry' --click '#sheetBody .actions.sep button:first-child' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#recentList button.entry' --click '#sheetBody .actions.sep button:nth-child(2)' http://127.0.0.1:8771/seed.html
   node /tmp/toolkit/a11y-check.mjs --click '#writeStages button[data-stage="thinking"]' http://127.0.0.1:8771/draft.html
   node /tmp/toolkit/a11y-check.mjs --click '#writeStages button[data-stage="planning"]' --click '#undoFeel button[data-feel="lifts"]' http://127.0.0.1:8771/draft.html
   ```
   Those are: Write with thoughts and the warning card; the full See tab; a thought at Did it; one with Lifts me pressed; one at Planning it; the thought Show me one opens (at Thinking about it); Make a plan; the Undo bar after a move; Edit; the Undo bar after Delete; the card after saving; and that card with a choice pressed. Your week only shows from Friday to Sunday, so run the See line on one of those days to cover it. Check once that each really opened (its heading or card is on the page) before trusting a clean result.
5. Save the changed files to this repo, plus a new CHANGELOG.md entry, an update to PROGRESS.md, and README.md (a new headless Chrome row at the top of **Tested on**, and any feature or wording change). All files sit flat at the top of the repo, except the tag workflow. They can also be uploaded by hand from a phone.
6. The "Tag new versions" workflow adds the `vX.Y.Z` tag when a new version reaches main. Check its run passed.
7. Open the live site on a real iPhone and do the Done when check in PROGRESS.md.

From 1.0 on (the safety-net stage), the self-test and the toolkit's `release-check.sh` join these steps, and `rebuild.py` builds `selftest.html` too.

## Things that must not break
- **The privacy lock.** `index.html` carries a Content-Security-Policy that only lets scripts run whose exact sha256 fingerprint is listed, and blocks every outside request (`connect-src 'none'`). Any edit to a script changes its fingerprint. Always run `rebuild.py` after editing, or the app won't start.
- **Names that never change, or people lose their data.** Small settings use localStorage keys starting `ownsight-v1-` (so far `ownsight-v1-size` for text size and `ownsight-v1-install` for the Home Screen card). Entries live in the IndexedDB database `ownsight-v1`, version 1, store `data`: record `state` holds `{ rev, json }` (the save count and the saved data as JSON), and records `damaged-<rev>` hold data that couldn't be read, set aside. Windows tell each other about saves on the BroadcastChannel `ownsight-v1` (a number only, never any data). Backup codes will start `OWNSIGHT1:`, and backup files will be named `ownsight-backup-YYYY-MM-DD.json`.
- **Saved data is version 2** (`{ v: 2, thoughts, settings }`). Version 1 (0.2.0 and 0.3.0: `entries`, six stages, topics) moves up in `readSaved()` when it's read: Notice, Question and Idea → `thinking`, Plan → `planning`, Do and Check → `did`. It's written as version 2 with the next change, never before. Any later change to what's saved gets a new `v` and one more small step in `readSaved()`, tested against saved samples of every older version.
- **Saving stays safe.** A save only goes ahead when the stored `rev` still matches this window's (`dbWrite`), so an out-of-date window can't save over newer thoughts. Every save is read back (`trySave`). Data that can't be read is set aside and never saved over (`hold = "damaged"`), and data with a newer `v` is shown but never saved over (`hold = "newer"`). Nothing can change until the saved data has loaded. `readSaved()` keeps every field, so an older version never trims what a later stage added, and it never copies `__proto__`, `constructor` or `prototype`.
- **The logic markers.** The plain functions sit between `// ==== logic: start ====` and `// ==== logic: end ====`, with no screen or storage inside, so tests can pull them out and run them on their own. Keep them that way.
- **The offline cache name** must start with `ownsight-`. The site shares freeforgood-apps.github.io with Till Payday, Study Coach and other apps, and `sw.js` only clears its own caches. Nothing in the app may ever clear storage it doesn't own (no `localStorage.clear()`, no deleting every database or cache).
- **The offline copy is only the app.** `sw.js` saves a page for offline use only when it's the app itself (`./` or `index.html`), so opening another page here (like the self-test, later) can't replace it.
- **No outside requests.** Fonts are built in (Atkinson Hyperlegible, Bricolage Grotesque, DM Mono, all SIL Open Font License), the same as Till Payday's. Don't add Google Fonts or any CDN. The lock would block them anyway.
- **APP_VERSION** in the app and the version in `sw.js` must match. `rebuild.py` sets both. The tagging workflow (`.github/workflows/tag-new-versions.yml`, a copy of Best Guess's) reads it to add the version tag, so keep it written as `APP_VERSION = "X.Y.Z"`.
- **Anything from saved data or typing goes on screen as text only,** through the toolkit's `el()` or `textContent`, never `innerHTML`. Backups get checked with the toolkit's `parseBackup()` before restoring.
- **The tab bar is fixed at the bottom.** Page content keeps enough space below it (`.wrap`'s bottom padding and `scroll-padding-bottom`, both from `--bar-h`), so nothing hides behind the bar. If the bar gets taller, raise `--bar-h`. The Undo bar (and the card after saving, which is the same element) sits above it: while it shows, `--undo-h` is set to its measured height (`sizeUndo()`), and what has focus is scrolled clear of it (`keepClear()`).
- **Colors are variables** with light and dark values. After changing one, recompute its contrast in code: 4.5:1 for text, 3:1 for large text, icons and borders that matter.
- **Spoken names match the screen.** A button with an aria-label must include the words on it (WCAG 2.5.3), and every text box needs a label you can see.

## Phone steps
- **Turn on the website** (once): repo **Settings** → **Pages** → under **Build and deployment**, set **Source** to **Deploy from a branch**, branch **main**, folder **/ (root)** → **Save**. Then check **Enforce HTTPS**.
- **Upload files by hand:** repo → **Add file** → **Upload files**.
- **Install it:** open the link in Safari → **Share** → **Add to Home Screen**.

What changed in each version, and how it was tested, is in CHANGELOG.md.
