"""Ownsight rebuild tool. Run after editing the app, from the repo folder.

  python3 rebuild.py            refresh the privacy lock and rebuild the self-test
  python3 rebuild.py 1.2.3      also set the version everywhere (index.html, sw.js and the self-test)
  python3 rebuild.py --check    change nothing; exit 1 if the lock, the self-test or the versions are out of date

Why: the privacy lock (Content-Security-Policy) only lets scripts run whose exact
fingerprint (sha256) is listed. Any edit to a script changes its fingerprint, so the
lock must be refreshed, or the edited app won't start. Files are updated in place,
because the repo files are what the website publishes.

index.html is the source. selftest.html is made from it: the same app on its own storage
(database and settings named "ownsight-selftest-v1", never "ownsight-v1"), which drops any
self-test PIN when it opens, with the test runner added as its last script. The runner's
source is that last script in the current selftest.html. Its copy of the app's logic (between
its "logic copy" markers) is refreshed from index.html's logic markers every time, so the
self-test checks the logic as it ships.
"""
import base64
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SCRIPT = re.compile(r"<script>(.*?)</script>", re.S)
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
REAL_PREFIX = 'const PREFIX = "ownsight-v1";'
TEST_PREFIX = 'const PREFIX = "ownsight-selftest-v1";'
# The self-test always opens unlocked, so its Run button can be reached (only its own PIN goes; the real one is never touched)
NO_TEST_PIN = ('<script>try { localStorage.removeItem("ownsight-selftest-v1-pin"); '
               'localStorage.removeItem("ownsight-selftest-v1-pinwait"); } catch (e) {}</script>\n')


def lock(html):
    hashes = " ".join(
        "'sha256-" + base64.b64encode(hashlib.sha256(m.group(1).encode("utf-8")).digest()).decode() + "'"
        for m in SCRIPT.finditer(html)
    )
    new, n = re.subn(r"(script-src )[^;]*(;)", lambda m: m.group(1) + hashes + m.group(2), html, count=1)
    assert n == 1, "privacy lock not found in the page"
    return new


def one(text, old, new):
    assert text.count(old) == 1, "expected exactly one of: " + old[:60]
    return text.replace(old, new)


def between(text, start, end):
    a = text.index(start) + len(start)
    return a, text.index(end, a)


def set_version(index, sw, ver):
    index, n1 = re.subn(r'const APP_VERSION = "[^"]+";', 'const APP_VERSION = "%s";' % ver, index, count=1)
    sw, n2 = re.subn(r"\(version [^)]+\)", "(version %s)" % ver, sw, count=1)
    sw, n3 = re.subn(r'const CACHE = "ownsight-[^"]+";', 'const CACHE = "ownsight-%s";' % ver, sw, count=1)
    assert n1 == n2 == n3 == 1, "a version marker is missing"
    return index, sw


def app_version(html):
    m = re.search(r'const APP_VERSION = "([^"]+)";', html)
    return m.group(1) if m else None


def build_selftest(index, current):
    """The self-test page: the locked app on its own storage, plus the runner (its logic copy and version refreshed)."""
    runner = SCRIPT.findall(current)[-1]
    a, b = between(index, "// ==== logic: start ====\n", "  // ==== logic: end ====")
    logic = index[a:b]
    c, d = between(runner, "// ==== logic copy: start ====\n", "    // ==== logic copy: end ====")
    runner = runner[:c] + logic + runner[d:]
    runner, n = re.subn(r'const VERSION = "[^"]+";', 'const VERSION = "%s";' % app_version(index), runner, count=1)
    assert n == 1, "the runner's VERSION is missing"
    t = one(index, REAL_PREFIX, TEST_PREFIX)
    t = one(t, "<title>Ownsight</title>", "<title>Ownsight Self-Test</title>")
    t = one(t, '\n<script>\n"use strict";', "\n" + NO_TEST_PIN + '<script>\n"use strict";')
    end = t.rindex("</script>") + len("</script>")
    return lock(t[:end] + "\n<script>" + runner + "</script>" + t[end:])


def versions(index, sw, selftest):
    a = app_version(index)
    b = re.search(r'const CACHE = "ownsight-([^"]+)";', sw)
    c = re.search(r"\(version ([^)]+)\)", sw)
    d = app_version(selftest)
    e = re.search(r'const VERSION = "([^"]+)";', SCRIPT.findall(selftest)[-1]) if SCRIPT.findall(selftest) else None
    return [a, b and b.group(1), c and c.group(1), d, e and e.group(1)]


def main(argv):
    index_p, sw_p, st_p = HERE / "index.html", HERE / "sw.js", HERE / "selftest.html"
    index = index_p.read_text(encoding="utf-8")
    sw = sw_p.read_text(encoding="utf-8")
    selftest = st_p.read_text(encoding="utf-8")
    if argv[:1] == ["--check"]:
        problems = []
        if lock(index) != index:
            problems.append("the privacy lock is out of date (run python3 rebuild.py)")
        if build_selftest(lock(index), selftest) != selftest:
            problems.append("selftest.html is out of date (run python3 rebuild.py)")
        v = versions(index, sw, selftest)
        if len(set(v)) != 1 or None in v:
            problems.append("versions don't agree: app %s, sw cache %s, sw note %s, self-test app %s, self-test runner %s" % tuple(v))
        for p in problems:
            print("FAIL:", p)
        if not problems:
            print("OK: lock fresh, self-test up to date, version", v[0])
        return 1 if problems else 0
    if argv:
        ver = argv[0]
        if not VERSION_RE.match(ver):
            print("Version must look like 1.2.3")
            return 2
        index, sw = set_version(index, sw, ver)
        sw_p.write_text(sw, encoding="utf-8")
    index = lock(index)
    index_p.write_text(index, encoding="utf-8")
    st_p.write_text(build_selftest(index, selftest), encoding="utf-8")
    print("updated index.html and selftest.html" + (", and sw.js to " + argv[0] if argv else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
