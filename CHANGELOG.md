# Changelog

What changed in each version, newest first, and how it was tested.

## 0.1.0 (Nov 14, 2026)
- First version, for testing the frame of the app (stage 1). Not shared yet.
- Installs to the Home Screen with its own icon, opens full screen, works offline after the first visit, and follows light and dark mode. It's built to fit around the notch and the Home bar.
- Five tabs at the bottom, in thumb reach: Catch, Patterns, Decide, Me and More. The first four say what's coming.
- More has a text size choice (normal, large, extra large), steps for adding Ownsight to your Home Screen, and About with the version, the privacy promise and the feedback address.
- A card on Catch suggests adding Ownsight to your Home Screen, with an Install button where the browser offers one. **Got it** hides it for good.
- A privacy lock built into the page blocks it from sending anything over the internet or running any script but its own.
- Tested: 49 browser checks passed in headless Chrome: the page loads with no errors, the privacy lock blocks an outside request, an outside image and an added script, the tabs work by tap and by arrow keys, text size and **Got it** are kept after a reload (a damaged saved size falls back to normal), every saved name starts with `ownsight-v1-`, it opens offline with the version shown, an update clears only Ownsight's old offline copy (another app's stays), and nothing scrolls sideways or hides behind the tab bar at phone size, small phone size with extra large text, and desktop size, in light and dark. 4 of 4 planted bugs were caught (an offline helper that clears other apps' copies, a setting saved without the app's prefix, a script edit with a stale privacy lock, and content hidden under the tab bar). The accessibility checker found nothing on all 5 tabs at 4 sizes in light and dark. Text contrast was computed for every color pair in both themes: all 4.5:1 or more. On a real iPhone (Nov 14): added to the Home Screen from Safari, it opened full screen with its own icon, nothing hid under the notch or the Home bar, and in Airplane Mode it still opened with the version shown.
