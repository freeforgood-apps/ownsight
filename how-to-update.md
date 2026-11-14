# How to update Ownsight

This repo (freeforgood-apps/ownsight) is the source. `index.html` is the whole app. `rebuild.py` (in this repo) refreshes the privacy lock and sets the version.

## Steps for any change
1. Get the current files from this repo.
2. Edit `index.html`. Keep the app in one file.
3. Run `python3 rebuild.py <new version>` in the repo folder (or `python3 rebuild.py` to refresh the lock only). It refreshes the privacy lock and sets the version in `index.html` and `sw.js`. `python3 rebuild.py --check` changes nothing and says if the lock or the versions are out of date.
4. Test everything the "Verify" rule in PROGRESS.md lists. Run the toolkit's accessibility checker on every tab (set the toolkit up first, see its README):
   ```
   node /tmp/toolkit/a11y-check.mjs http://127.0.0.1:8770/index.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-patterns' http://127.0.0.1:8770/index.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-decide' http://127.0.0.1:8770/index.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-me' http://127.0.0.1:8770/index.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' http://127.0.0.1:8770/index.html
   ```
   Add a line for every new sheet or screen. A `matched nothing` error means the taps changed, so fix the list.
5. Save the changed files to this repo, plus a new CHANGELOG.md entry, an update to PROGRESS.md, and README.md (a new headless Chrome row at the top of **Tested on**, and any feature or wording change). All files sit flat at the top of the repo, except the tag workflow. They can also be uploaded by hand from a phone.
6. The "Tag new versions" workflow adds the `vX.Y.Z` tag when a new version reaches main. Check its run passed.
7. Open the live site on a real iPhone and do the Done when check in PROGRESS.md.

From 1.0 on (the safety-net stage), the self-test and the toolkit's `release-check.sh` join these steps, and `rebuild.py` builds `selftest.html` too.

## Things that must not break
- **The privacy lock.** `index.html` carries a Content-Security-Policy that only lets scripts run whose exact sha256 fingerprint is listed, and blocks every outside request (`connect-src 'none'`). Any edit to a script changes its fingerprint. Always run `rebuild.py` after editing, or the app won't start.
- **Names that never change, or people lose their data.** Small settings use localStorage keys starting `ownsight-v1-` (so far `ownsight-v1-size` for text size and `ownsight-v1-install` for the Home Screen card). Entries will live in the IndexedDB database `ownsight-v1`. Backup codes will start `OWNSIGHT1:`, and backup files will be named `ownsight-backup-YYYY-MM-DD.json`.
- **The offline cache name** must start with `ownsight-`. The site shares freeforgood-apps.github.io with Till Payday, Study Coach and other apps, and `sw.js` only clears its own caches. Nothing in the app may ever clear storage it doesn't own (no `localStorage.clear()`, no deleting every database or cache).
- **The offline copy is only the app.** `sw.js` saves a page for offline use only when it's the app itself (`./` or `index.html`), so opening another page here (like the self-test, later) can't replace it.
- **No outside requests.** Fonts are built in (Atkinson Hyperlegible, Bricolage Grotesque, DM Mono, all SIL Open Font License), the same as Till Payday's. Don't add Google Fonts or any CDN. The lock would block them anyway.
- **APP_VERSION** in the app and the version in `sw.js` must match. `rebuild.py` sets both. The tagging workflow (`.github/workflows/tag-new-versions.yml`, a copy of Best Guess's) reads it to add the version tag, so keep it written as `APP_VERSION = "X.Y.Z"`.
- **Anything from saved data or typing goes on screen as text only,** through the toolkit's `el()` or `textContent`, never `innerHTML`. Backups get checked with the toolkit's `parseBackup()` before restoring.
- **The tab bar is fixed at the bottom.** Page content keeps enough space below it (`.wrap`'s bottom padding and `scroll-padding-bottom`, both from `--bar-h`), so nothing hides behind the bar. If the bar gets taller, raise `--bar-h`.
- **Colors are variables** with light and dark values. After changing one, recompute its contrast in code: 4.5:1 for text, 3:1 for large text, icons and borders that matter.
- **Spoken names match the screen.** A button with an aria-label must include the words on it (WCAG 2.5.3), and every text box needs a label you can see.

## Phone steps
- **Turn on the website** (once): repo **Settings** → **Pages** → under **Build and deployment**, set **Source** to **Deploy from a branch**, branch **main**, folder **/ (root)** → **Save**. Then check **Enforce HTTPS**.
- **Upload files by hand:** repo → **Add file** → **Upload files**.
- **Install it:** open the link in Safari → **Share** → **Add to Home Screen**.

What changed in each version, and how it was tested, is in CHANGELOG.md.
