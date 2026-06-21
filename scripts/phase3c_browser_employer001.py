#!/usr/bin/env python3
"""Deterministic Playwright browser search for Phase 3C employer #1.

Replaces the flaky computerUse manual-clicking flow with a scripted,
repeatable browser pass over a single employer's career site.

Behavior:
  1. Reads employer #1 from the Phase 3C browser queue
     (Jobs/runs/phase3c_browser_queue_20260620.json). If that file is not on
     disk it is read directly from phase3c_sync_minimum.zip.
  2. Launches Chromium (Playwright).
  3. Opens the employer #1 career URL and waits for load.
  4. Tries the search terms one at a time: research, data, epidemiology.
     - No Boolean OR strings are used; each term is submitted on its own.
     - For each term: locate a search box, type the term, press Enter if a box
       is found, wait 3 seconds, capture page text, and extract plausible job
       titles + URLs from visible links.
  5. Writes outputs (does NOT touch authoritative inventory files):
       - browser_employer001_results.csv
       - browser_employer001_audit.md
       - browser_employer001_screenshot.png

If the browser fails to launch, the exact error is printed and the script exits
with a non-zero status without writing partial results.
"""
from __future__ import annotations

import csv
import io
import json
import sys
import time
import traceback
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
QUEUE_REL = "Jobs/runs/phase3c_browser_queue_20260620.json"
ZIP_NAME = "phase3c_sync_minimum.zip"

SEARCH_TERMS = ["research", "data", "epidemiology"]
WAIT_AFTER_SEARCH_SEC = 3

OUT_CSV = REPO_ROOT / "browser_employer001_results.csv"
OUT_AUDIT = REPO_ROOT / "browser_employer001_audit.md"
OUT_SHOT = REPO_ROOT / "browser_employer001_screenshot.png"

# Selectors tried (in order) to locate a free-text search box.
SEARCH_SELECTORS = [
    '[data-automation-id="keywordSearchInput"]',
    'input[data-automation-id*="search" i]',
    'input[type="search"]',
    '[role="searchbox"]',
    'input[name*="search" i]',
    'input[aria-label*="search" i]',
    'input[placeholder*="search" i]',
    'input[id*="search" i]',
    'input[name*="keyword" i]',
    'input[placeholder*="keyword" i]',
]

# Buttons commonly used for cookie/consent banners (dismissed deterministically).
CONSENT_TEXTS = [
    "Accept All", "Accept all", "Accept All Cookies", "Accept Cookies",
    "Accept", "I Agree", "Agree", "Got it", "Allow all",
]

JOB_URL_HINTS = (
    "job", "career", "requisition", "/req", "posting", "position", "opening",
    "vacancy", "jobid", "gh_jid", "/r-", "myworkdayjobs", "lever.co", "/jr",
)
JOB_TITLE_KEYWORDS = (
    "analyst", "scientist", "engineer", "manager", "specialist", "researcher",
    "epidemiolog", "associate", "director", "coordinator", "consultant",
    "writer", "statistician", "biostatist", "research", "data", "health",
    "outcomes", "economist", "fellow", "technician", "developer", "lead",
    "intern", "advisor", "officer", "nurse", "physician", "clinical",
)


def load_employer_one() -> dict:
    """Return the first employer in the Phase 3C queue (disk first, then zip)."""
    on_disk = REPO_ROOT / QUEUE_REL
    if on_disk.exists():
        data = json.loads(on_disk.read_text(encoding="utf-8"))
    else:
        zip_path = REPO_ROOT / ZIP_NAME
        if not zip_path.exists():
            raise FileNotFoundError(
                f"Neither {QUEUE_REL} nor {ZIP_NAME} found under {REPO_ROOT}"
            )
        with zipfile.ZipFile(zip_path) as zf:
            with zf.open(QUEUE_REL) as fh:
                data = json.loads(io.TextIOWrapper(fh, encoding="utf-8").read())
    queue = data["queue"] if isinstance(data, dict) else data
    if not queue:
        raise ValueError("Phase 3C queue is empty")
    return queue[0]


def dismiss_consent(page) -> str | None:
    """Best-effort deterministic dismissal of a cookie/consent banner."""
    for label in CONSENT_TEXTS:
        try:
            btn = page.get_by_role("button", name=label, exact=False)
            if btn.count() > 0 and btn.first.is_visible():
                btn.first.click(timeout=2000)
                page.wait_for_timeout(800)
                return label
        except Exception:
            continue
    return None


def find_search_box(page):
    """Return (locator, selector) for the first visible search box, or (None, None)."""
    for sel in SEARCH_SELECTORS:
        try:
            loc = page.locator(sel)
            n = loc.count()
            for i in range(min(n, 5)):
                cand = loc.nth(i)
                if cand.is_visible():
                    return cand, sel
        except Exception:
            continue
    return None, None


def extract_links(page) -> list[dict]:
    """Extract visible anchors as {title, url} dicts (deduped)."""
    base = page.url
    rows = []
    seen = set()
    try:
        anchors = page.locator("a")
        count = anchors.count()
    except Exception:
        return rows
    for i in range(min(count, 600)):
        a = anchors.nth(i)
        try:
            href = a.get_attribute("href")
            text = (a.inner_text(timeout=1000) or "").strip()
        except Exception:
            continue
        if not href or not text:
            continue
        text = " ".join(text.split())
        if len(text) < 3 or len(text) > 160:
            continue
        url = urljoin(base, href)
        if not urlparse(url).scheme.startswith("http"):
            continue
        key = (text.lower(), url)
        if key in seen:
            continue
        seen.add(key)
        rows.append({"title": text, "url": url})
    return rows


def is_plausible_job(title: str, url: str) -> bool:
    t, u = title.lower(), url.lower()
    if any(h in u for h in JOB_URL_HINTS):
        return True
    if any(k in t for k in JOB_TITLE_KEYWORDS):
        return True
    return False


def main() -> int:
    started = datetime.now(timezone.utc)
    emp = load_employer_one()
    employer = emp.get("employer", "UNKNOWN")
    url = emp.get("url", "")
    ats = emp.get("ats", "")
    print(f"Employer #1: {employer}")
    print(f"Career URL : {url}")
    print(f"ATS        : {ats}")

    # --- Browser launch (hard requirement: report exact error and stop on fail) ---
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:  # import failure counts as launch failure
        print("BROWSER LAUNCH FAILED (playwright import):", repr(exc), file=sys.stderr)
        return 2

    audit_terms: list[dict] = []
    all_rows: list[dict] = []
    browser_version = "unknown"
    shot_saved = False

    pw = None
    browser = None
    try:
        pw = sync_playwright().start()
        try:
            browser = pw.chromium.launch(headless=True)
        except Exception as exc:
            print("BROWSER LAUNCH FAILED:", file=sys.stderr)
            traceback.print_exc()
            print(f"\nExact error: {exc!r}", file=sys.stderr)
            return 2

        browser_version = browser.version
        print(f"Browser    : Chromium {browser_version}")
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1366, "height": 900},
        )
        page = context.new_page()

        # Step: open career URL + wait for load.
        nav_error = None
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except Exception as exc:
            nav_error = repr(exc)
            print("Navigation warning:", nav_error)
        try:
            page.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            pass
        page.wait_for_timeout(2000)

        consent = dismiss_consent(page)
        if consent:
            print(f"Dismissed consent banner via: {consent}")

        # Useful screenshot of the loaded landing page.
        try:
            page.screenshot(path=str(OUT_SHOT), full_page=True)
            shot_saved = True
        except Exception as exc:
            print("Screenshot warning:", repr(exc))

        # Step: each search term, one at a time.
        for term in SEARCH_TERMS:
            term_info = {
                "term": term,
                "search_box_selector": None,
                "submitted": False,
                "page_url": "",
                "text_len": 0,
                "links_total": 0,
                "plausible": 0,
                "error": None,
            }
            try:
                box, sel = find_search_box(page)
                if box is not None:
                    term_info["search_box_selector"] = sel
                    try:
                        box.click(timeout=5000)
                        box.fill("")
                        box.fill(term)
                        box.press("Enter")
                        term_info["submitted"] = True
                    except Exception as exc:
                        term_info["error"] = f"input_error: {exc!r}"
                # wait 3 seconds after each term
                page.wait_for_timeout(WAIT_AFTER_SEARCH_SEC * 1000)
                try:
                    page.wait_for_load_state("networkidle", timeout=8000)
                except Exception:
                    pass

                term_info["page_url"] = page.url
                try:
                    body_text = page.locator("body").inner_text(timeout=5000)
                except Exception:
                    body_text = ""
                term_info["text_len"] = len(body_text)

                links = extract_links(page)
                term_info["links_total"] = len(links)
                plausible = [
                    r for r in links if is_plausible_job(r["title"], r["url"])
                ]
                term_info["plausible"] = len(plausible)
                for r in plausible:
                    all_rows.append({
                        "employer": employer,
                        "employer_url": url,
                        "ats": ats,
                        "search_term": term,
                        "job_title": r["title"],
                        "job_url": r["url"],
                        "captured_at": datetime.now(timezone.utc).isoformat(),
                    })
                print(
                    f"  [{term}] box={'yes' if box else 'no'} "
                    f"links={len(links)} plausible={len(plausible)}"
                )
            except Exception as exc:
                term_info["error"] = repr(exc)
                print(f"  [{term}] ERROR: {exc!r}")
            audit_terms.append(term_info)

        context.close()
    finally:
        if browser is not None:
            try:
                browser.close()
            except Exception:
                pass
        if pw is not None:
            try:
                pw.stop()
            except Exception:
                pass

    # Dedupe rows across terms by (job_title, job_url).
    deduped = []
    seen = set()
    for r in all_rows:
        key = (r["job_title"].lower(), r["job_url"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)

    # --- Write results CSV (authoritative inventory files are never touched) ---
    fields = [
        "employer", "employer_url", "ats", "search_term",
        "job_title", "job_url", "captured_at",
    ]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(deduped)

    # --- Write audit markdown ---
    finished = datetime.now(timezone.utc)
    lines = [
        "# Phase 3C Browser Audit — Employer #1",
        "",
        f"- **Employer:** {employer}",
        f"- **Career URL:** {url}",
        f"- **ATS:** {ats}",
        f"- **Browser:** Chromium {browser_version} (Playwright, headless)",
        f"- **Started (UTC):** {started.isoformat()}",
        f"- **Finished (UTC):** {finished.isoformat()}",
        f"- **Search terms (tried one at a time):** {', '.join(SEARCH_TERMS)}",
        f"- **Boolean OR used:** no",
        f"- **computerUse manual clicking used:** no",
        f"- **Screenshot saved:** {'yes' if shot_saved else 'no'} "
        f"({OUT_SHOT.name})",
        f"- **Plausible job rows written:** {len(deduped)} ({OUT_CSV.name})",
        "",
        "## Per-term results",
        "",
        "| Term | Search box | Submitted | Visible links | Plausible jobs | Page URL | Error |",
        "|------|-----------|-----------|--------------:|---------------:|----------|-------|",
    ]
    for t in audit_terms:
        lines.append(
            f"| {t['term']} | {t['search_box_selector'] or 'not found'} | "
            f"{'yes' if t['submitted'] else 'no'} | {t['links_total']} | "
            f"{t['plausible']} | {t['page_url'] or '-'} | {t['error'] or '-'} |"
        )
    lines += ["", "## Sample plausible roles", ""]
    if deduped:
        for r in deduped[:25]:
            lines.append(f"- **{r['job_title']}** — {r['job_url']} (term: {r['search_term']})")
    else:
        lines.append(
            "_No plausible job links were extracted. The career landing page may "
            "require an embedded ATS (e.g. Workday) search UI, may be bot-protected, "
            "or may render results in an iframe/JS widget not reached by the generic "
            "search-box heuristics._"
        )
    lines.append("")
    OUT_AUDIT.write_text("\n".join(lines), encoding="utf-8")

    print("-" * 60)
    print(f"Wrote {OUT_CSV.name} ({len(deduped)} rows)")
    print(f"Wrote {OUT_AUDIT.name}")
    if shot_saved:
        print(f"Wrote {OUT_SHOT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
