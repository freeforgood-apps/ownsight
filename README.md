# Ownsight

A free, private app to understand how you think and what it means for your life. Works on any phone or computer. No account, no ads, no tracking.

**Open the app:** https://freeforgood-apps.github.io/ownsight/

**Early test version (0.1.0).** The frame of the app is in place: it installs, works offline and follows light and dark mode. Catching thoughts and seeing your own patterns come in the next update. A self-test page you can run yourself comes with the first full release (1.0).

## Who it's for

Anyone who wants to understand their own way of thinking: where it leans, where it gets stuck, how they decide, and what fuels and drains them. It's for the moments when a thought, a choice or a day needs sorting out, and for anyone who'd like a clearer picture of themselves over time. It's a mirror, not a diagnosis.

## What's inside

- **Five tabs in thumb reach:** Catch, Patterns, Decide, Me and More.
- **Works offline:** after the first visit, it opens without internet.
- **Light and dark:** follows your device's setting.
- **Text size:** normal, large or extra large, on the More tab.
- **Privacy lock:** built into the page, so it can't send anything over the internet.
- **Coming next:** catching thoughts in two taps and tagging each one with a stage of one thinking loop (Notice → Question → Idea → Plan → Do → Check), your patterns in plain counts, decisions you check back on, and your groundwork (how you decide, what fuels and drains you, and the Big Five).

## Add it to your home screen

- **iPhone or iPad:** open the link in Safari → tap **Share** → **Add to Home Screen**
- **Android:** open the link in Chrome → tap **⋮** → **Install app** (or **Add to Home screen**)
- **Computer:** in Chrome or Edge, click the install icon at the right end of the address bar

On iPhone and iPad, the Home Screen app keeps its own entries, apart from Safari, so it's best to add it before you start. Safari can also clear saved data from websites you haven't opened in 7 days. The Home Screen app avoids that.

## Tested on

Results are tied to the version and date they were run. When the app changes, these results only describe the version listed.

| Version | Date | Browser and device | Result |
|---|---|---|---|
| 0.1.0 | Nov 14, 2026 | Chrome (Blink engine) on Linux, headless: phone size and small phone size with extra large text, in light and dark, and desktop size | ✓ Passed, 49 automated checks |

**What the automated checks cover:** the page loads with no errors; the privacy lock blocks outside requests and added scripts; the tabs work by tap and by arrow keys; text size is kept after a reload; every saved name starts with the app's own prefix; it opens offline with the version shown; an update clears only Ownsight's own old offline copy; and nothing scrolls sideways or hides behind the tab bar. The accessibility checker (WCAG 2.2 AA) found nothing on all 5 tabs at 4 sizes in light and dark.

Chrome's engine also powers Microsoft Edge, Chromebooks, Android phones, Samsung Internet, Brave and Opera. Safari's engine powers Safari and nearly every other browser on iPhone and iPad.

## Privacy

- No accounts, ads, analytics, tracking or AI.
- What you add stays on this device. Nothing is sent anywhere.
- A privacy lock built into the page stops it from sending anything over the internet, even if it tried.
- Everything Ownsight needs, fonts included, comes from this one site.
- Nobody else, including the person who made it, can see what you write. There's no sharing feature.
- Like any site, GitHub Pages logs visitors' IP addresses for security; see the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Accessibility

Buttons are at least 44 pixels tall, every button and tab has a spoken name, and the text size choice goes up to extra large. It follows light and dark mode and your device's Reduce Motion and higher contrast settings. Text contrast meets WCAG 2.2 AA in both themes (computed for every color pair), and the tabs work with the arrow keys. It hasn't been checked with VoiceOver on a real iPhone yet. If anything is hard to use, please let us know (see Feedback below).

## Not therapy or professional advice

It's a mirror, not a diagnosis. Ownsight isn't therapy, a clinical test or professional advice.

## About the content

Ownsight is built with help from AI (Claude, made by Anthropic). Every version is checked with automated tests before it goes live, and the results are listed above and in CHANGELOG.md. Spot a mistake? Please tell us (see Feedback below).

## Feedback

Spotted a mistake, got stuck or have an idea? You don't need an account to reach us.

- **Email:** freeforgood-apps+ownsight@proton.me (private, no account needed)
- **GitHub:** open an issue in this repository's **Issues** tab (public, needs a free GitHub account)
- **In the app:** More → About Ownsight → the email link

Ownsight is a one-person volunteer project, so replies can take a while. Every message still helps, even if you don't hear back right away. Please don't include personal details you don't want to share.

## Files

| File | What it does |
|---|---|
| `index.html` | The whole app in one file (about 225 KB, fonts included) |
| `sw.js` | Lets the app work offline after the first visit. Keep it next to `index.html` |
| `manifest.webmanifest` | The app's install details: name, icons and how it opens |
| `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `apple-touch-icon.png`, `favicon-32.png` | The app icons |
| `rebuild.py` | Refreshes the privacy lock and sets the version after an edit |
| `README.md` | This page |
| `CHANGELOG.md` | What changed in each version, and how it was tested |
| `PROGRESS.md` | Where the project stands, and the rules for working on it |
| `how-to-update.md` | The steps for any change and release, and what must not break |
| `SECURITY.md` | How to report a security problem privately |
| `.gitignore` | Keeps private files, like keys, from being uploaded by mistake |
| `.github/workflows/tag-new-versions.yml` | Adds a version tag on GitHub whenever a new version reaches main |

## Updating the app

Follow [`how-to-update.md`](how-to-update.md), then upload the new files to this repository and commit. GitHub Pages updates the site within a minute or two, and everyone's saved entries carry over. After an update, add new rows to **Tested on**.

© 2026 Ownsight
