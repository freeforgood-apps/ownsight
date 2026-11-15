# Ownsight

A free, private app to understand how you think and what it means for your life. Works on any phone or computer. No account, no ads, no tracking.

**Open the app:** https://freeforgood-apps.github.io/ownsight/

**Version 1.0.0, the first full release.** Write your thoughts, move them along, see your own counts, back them up, lock it with a PIN if you like, and run a self-test right on your phone.

## Who it's for

Anyone who wants to understand themselves a little better, in the most straightforward way: what's on their mind, what they act on, and what lifts them or weighs on them. It's for the moments when a thought or a day needs sorting out, and for anyone who'd like a clearer picture of themselves over time. It's a mirror, not a diagnosis.

## What's inside

- **Save a thought in one tap:** write what's on your mind, then tap where it's at: **Thinking about it**, **Planning it** or **Did it**. That tap saves it. **Undo** is right there if a tap went wrong.
- **Lifts me or weighs on me:** right after saving, you can tap whether it lifts you or weighs on you. It's optional, and you can set or change it later.
- **Move it along:** open a thought and tap its next step: **Make a plan** ("What will you do about it?"), then **I did it** ("How did it go?"). Each asks for an optional line. You can also edit the words or delete a thought, with Undo.
- **See, in plain counts:** after 5 thoughts, where your thoughts sit, what lifts you and what weighs on you, and how many are waiting for a plan. **Show me one** opens the oldest one waiting.
- **Your week:** from Friday to Sunday, See starts with a look back at your last 7 days: what you wrote and did, and what lifted you or weighed on you.
- **Saves on your device:** every save is checked by reading it back. If saving stops working, Ownsight says so. A second open window can't save over newer thoughts. Thoughts saved by 0.2.0, 0.3.0 or 0.4.0 carry over.
- **Backups:** save a backup file or copy a backup code, with an optional password, and restore it on any phone. Every backup is checked to restore before it's handed out. Gentle reminders say when it's been a while.
- **Automatic copies:** a copy from each of the last 3 days you opened it, kept on your device. Two taps bring one back, with Undo.
- **Lock with a PIN (optional):** Ownsight asks for your PIN when it opens and after a minute away, so someone else using your phone doesn't see your thoughts. A wrong PIN never changes anything. It hides your thoughts but doesn't cover backups, so give a backup a password to keep it private too.
- **Delete everything:** two taps remove every thought, copy and setting Ownsight saved on your device, the PIN lock too, and nothing from any other app.
- **Three tabs in thumb reach:** Write, See and More.
- **Works offline:** after the first visit, it opens without internet.
- **Light and dark:** follows your device's setting.
- **Text size:** normal, large or extra large, on the More tab.
- **Privacy lock:** built into the page, so it can't send anything over the internet.
- **A self-test you can run yourself:** More → About → Run the self-test. It taps through Ownsight in your browser on its own separate storage, so your thoughts aren't touched, and shows a report you can send in.

## Add it to your home screen

- **iPhone or iPad:** open the link in Safari → tap **Share** → **Add to Home Screen**
- **Android:** open the link in Chrome → tap **⋮** → **Install app** (or **Add to Home screen**)
- **Computer:** in Chrome or Edge, click the install icon at the right end of the address bar

On iPhone and iPad, the Home Screen app keeps its own thoughts, apart from Safari, so it's best to add it before you start. Already started in Safari? Copy a backup code first (More tab), then restore it in the Home Screen app. Safari can also clear saved data from websites you haven't opened in 7 days. The Home Screen app avoids that.

## Tested on

Results are tied to the version and date they were run. When the app changes, these results only describe the version listed.

| Version | Date | Browser and device | Result |
|---|---|---|---|
| 1.0.0 | Nov 14, 2026 | Chrome (Blink engine) on Linux, headless: the self-test at phone (light), small phone (dark) and desktop sizes, in 13 time zones and on 4 different days of the week | ✓ Passed, 368 self-test checks each run, 16 of 16 planted bugs caught |
| 0.5.0 | Nov 14, 2026 | Chrome (Blink engine) on Linux, headless: phone, small phone and desktop sizes, in light and dark, over 6 made-up days for the automatic copies | ✓ Passed, 167 browser checks and 17 logic tests (in 12 time zones) |
| 0.4.0 | Nov 14, 2026 | Safari on a real iPhone, on the live site (the owner's quick check) | ✓ Passed: saving in one tap, Make a plan, and See at a glance |
| 0.4.0 | Nov 14, 2026 | Chrome (Blink engine) on Linux, headless: phone, small phone with extra large text in dark, and desktop sizes, in 3 time zones for Your week | ✓ Passed, 191 browser checks and 19 logic tests (in 12 time zones) |
| 0.3.0 | Nov 14, 2026 | Chrome (Blink engine) on Linux, headless: the same sizes and themes as 0.2.0 | ✓ Passed, 124 browser checks and 20 logic tests |
| 0.2.0 | Nov 14, 2026 | Chrome (Blink engine) on Linux, headless: phone, small phone with extra large text, iPad with large text and desktop sizes, in light and dark | ✓ Passed, 107 browser checks and 19 logic tests |
| 0.1.0 | Nov 14, 2026 | Chrome (Blink engine) on Linux, headless: phone size and small phone size with extra large text, in light and dark, and desktop size | ✓ Passed, 49 automated checks |

**What the automated checks cover (1.0.0):** everything the self-test checks (the main flows, backups and restore, automatic copies, reminders, older data and backups, damaged and newer data, two windows, the PIN lock, the privacy lock, the offline copy and Delete everything, with the counts, dates and reminder timing worked out a second way), plus the PIN lock on the real app: locked before any thought shows when Ownsight opens, Esc can't close it, a minute away with a thought open behind it, two windows, and the keyboard. The accessibility checker (WCAG 2.2 AA) found nothing on every screen and sheet, the PIN screen and the PIN card, and the self-test page, at 4 sizes in light and dark.

**What the automated checks cover (0.5.0):** backing up as a file or a code, with and without a password, and every backup checked before it's handed out; restoring from a file or a code, with two taps when it would replace thoughts, and Undo; wrong passwords, other apps' backups, newer and damaged backups, and booby-trapped backups staying plain text; automatic copies made each day and before the first change of a day, keeping the newest 3, and two taps to bring one back; backup reminders and Later, checked a second way against Till Payday's timing; bringing back a copy or a backup when saved data can't be read; Delete everything removing only Ownsight's own data; two windows; the clipboard being blocked; data from 0.3.0 and 0.4.0; offline; and the main flows again (saving in one tap, lifts me, Undo, Make a plan and See). The accessibility checker (WCAG 2.2 AA) found nothing on all 3 tabs, See with Your week, every sheet, the card after saving, the Undo bar, the warning cards, the backup reminders, and every part of backups, restore, copies and Delete everything, at 4 sizes in light and dark.

**What the automated checks cover (0.4.0):** saving a thought in one tap and reading the save back; lifts me or weighs on me, from the card after saving and from the thought; Undo; opening a thought, making a plan and moving it to Did it, each with its optional line and Undo; editing and deleting with Undo; See before and after 5 thoughts, with the counts checked a second way; lifts and weighs; Show me one and focus coming back to it; Your week shown only from Friday to Sunday, over the last 7 days, at the midnight edges, across month ends, a leap day, the year end and daylight saving changes, in 12 time zones; thoughts saved by 0.2.0 and 0.3.0 carrying over, with an open 0.3.0 window never saving over the new data; showing 20 at a time in Recent, and the 10,000 limit; typed HTML and scripts showing as plain text; a second window picking up new thoughts, and an out-of-date window never saving over newer ones; damaged saved data set aside and never saved over; data from a newer version left alone; keyboard only; offline; every saved name starting with the app's own prefix; and nothing scrolling sideways or hiding behind the bars. The accessibility checker (WCAG 2.2 AA) found nothing on all 3 tabs, See with Your week, every sheet, the card after saving, the Undo bar and the warning card, at 4 sizes in light and dark.

Chrome's engine also powers Microsoft Edge, Chromebooks, Android phones, Samsung Internet, Brave and Opera. Safari's engine powers Safari and nearly every other browser on iPhone and iPad.

## Privacy

- No accounts, ads, analytics, tracking or AI.
- What you add stays on this device. Nothing is sent anywhere.
- A backup goes only where you put it, like the Files app or Notes. The automatic copies stay on your device.
- The PIN lock, if you turn it on, keeps only a scrambled form of your PIN on your device, never the PIN itself. It's a privacy screen for a shared phone, not encryption.
- The self-test runs on its own separate storage on your device. Its report goes only where you send it.
- A privacy lock built into the page stops it from sending anything over the internet, even if it tried.
- Everything Ownsight needs, fonts included, comes from this one site.
- Nobody else, including the person who made it, can see what you write. There's no sharing feature.
- Like any site, GitHub Pages logs visitors' IP addresses for security; see the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Accessibility

Buttons are at least 44 pixels tall, every button and tab has a spoken name, and the text size choice goes up to extra large. It follows light and dark mode and your device's Reduce Motion and higher contrast settings. Text contrast meets WCAG 2.2 AA in both themes, and text boxes and buttons have edges that stand out (computed for every color pair). The tabs work with the arrow keys, everything works with a keyboard, sheets close with Esc and put you back where you were, and saves, Undo and problems are read out. The bar on See has the same counts in words next to it, and a pressed choice shows a ring and a check mark, not just a color. The PIN screen's box has a label you can see, works with paste and the keyboard, and a wait after wrong tries is read out once, not counted down. It hasn't been checked with VoiceOver on a real iPhone yet. If anything is hard to use, please let us know (see Feedback below).

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
| `index.html` | The whole app in one file (about 340 KB, fonts included) |
| `selftest.html` | The self-test: the same app on its own separate storage, plus the test runner. Made from `index.html` by `rebuild.py` |
| `sw.js` | Lets the app work offline after the first visit. Keep it next to `index.html` |
| `manifest.webmanifest` | The app's install details: name, icons and how it opens |
| `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `apple-touch-icon.png`, `favicon-32.png` | The app icons |
| `rebuild.py` | Refreshes the privacy lock, sets the version and builds the self-test after an edit |
| `README.md` | This page |
| `CHANGELOG.md` | What changed in each version, and how it was tested |
| `PROGRESS.md` | Where the project stands, and the rules for working on it |
| `how-to-update.md` | The steps for any change and release, and what must not break |
| `SECURITY.md` | How to report a security problem privately |
| `.gitignore` | Keeps private files, like keys, from being uploaded by mistake |
| `.github/workflows/tag-new-versions.yml` | Adds a version tag on GitHub whenever a new version reaches main |

## Updating the app

Follow [`how-to-update.md`](how-to-update.md), then upload the new files to this repository and commit. GitHub Pages updates the site within a minute or two, and everyone's saved thoughts carry over. After an update, add new rows to **Tested on**.

© 2026 Ownsight
