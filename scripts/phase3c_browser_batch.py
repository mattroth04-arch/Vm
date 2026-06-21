#!/usr/bin/env python3
"""Reusable deterministic Playwright browser search for a Phase 3C employer range.

Generalizes scripts/phase3c_browser_employer001.py to process a *range* of
employers from the Phase 3C queue, deterministically (no computerUse / manual
clicking).

For each employer in the range it:
  1. Opens the career URL and waits for load (auto-dismisses consent banners).
  2. Detects whether a free-text search box exists (page + iframes).
  3. If no search box is found, follows an *obvious* link to the real jobs
     portal (known ATS domains or explicit "search jobs"-style links) and
     re-detects a search box there.
  4. If a search box exists, submits each search term one at a time
     (no Boolean OR), pressing Enter, waiting 3s, capturing page text, and
     extracting plausible job titles + URLs. If no search box exists even after
     following links, the reachable page is captured once.
  5. Saves progress (results CSV + audit MD) after EVERY employer.

Authoritative inventory files (current_results.csv, applied_jobs.csv,
master_seen_jobs.csv) are never read or written.

If the browser fails to launch, the exact error is printed and the script exits
non-zero without writing partial results.

Usage:
  python3 scripts/phase3c_browser_batch.py [--start 26] [--end 50]
                                           [--out-prefix browser_batch02]
                                           [--headed]
Range is 1-indexed and inclusive (defaults to employers 26-50).
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
import traceback
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
QUEUE_REL = "Jobs/runs/phase3c_browser_queue_20260620.json"
ZIP_NAME = "phase3c_sync_minimum.zip"

SEARCH_TERMS = [
    "research",
    "data",
    "epidemiology",
    "HEOR",
    "medical writer",
    "public health",
    "biostatistics",
    "outcomes research",
]
WAIT_AFTER_SEARCH_SEC = 3
MAX_PORTAL_HOPS = 2

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
    'input[aria-label*="keyword" i]',
]

CONSENT_TEXTS = [
    "Accept All", "Accept all", "Accept All Cookies", "Accept Cookies",
    "Accept", "I Agree", "Agree", "Got it", "Allow all", "OK",
]

# Known ATS / job-portal host fragments and explicit portal link texts.
JOBS_PORTAL_DOMAINS = (
    "myworkdayjobs.com", "greenhouse.io", "lever.co", "icims.com",
    "phenompeople.com", "phenom", "taleo.net", "oraclecloud.com",
    "jobvite.com", "smartrecruiters.com", "ashbyhq.com", "workable.com",
    "bamboohr.com", "successfactors", "brassring.com", "avature.net",
    "recruiting.ultipro.com", "paycomonline.net", "jobs.",
)
PORTAL_LINK_TEXTS = (
    "search jobs", "search all jobs", "search openings", "search careers",
    "view all jobs", "view jobs", "see all jobs", "browse jobs", "all jobs",
    "open positions", "open roles", "current openings", "current opportunities",
    "view opportunities", "explore jobs", "explore opportunities",
    "find jobs", "job search", "view open roles", "all openings",
    "view openings", "see open roles", "search for jobs",
)

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
    "heor", "rwe", "evidence", "biostatistics",
)


def load_queue() -> list:
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
    return data["queue"] if isinstance(data, dict) else data


def dismiss_consent(page) -> str | None:
    for label in CONSENT_TEXTS:
        try:
            btn = page.get_by_role("button", name=label, exact=False)
            if btn.count() > 0 and btn.first.is_visible():
                btn.first.click(timeout=2000)
                page.wait_for_timeout(700)
                return label
        except Exception:
            continue
    return None


def find_search_box(page):
    """Return (locator, selector) for the first visible search box across the
    main page and all frames, or (None, None)."""
    frames = [page] + [f for f in page.frames]
    for ctx in frames:
        for sel in SEARCH_SELECTORS:
            try:
                loc = ctx.locator(sel)
                n = loc.count()
                for i in range(min(n, 5)):
                    cand = loc.nth(i)
                    if cand.is_visible():
                        return cand, sel
            except Exception:
                continue
    return None, None


def _anchor_rows_from(ctx, base_url) -> list[dict]:
    rows = []
    try:
        anchors = ctx.locator("a")
        count = anchors.count()
    except Exception:
        return rows
    for i in range(min(count, 800)):
        a = anchors.nth(i)
        try:
            href = a.get_attribute("href")
            text = (a.inner_text(timeout=800) or "").strip()
        except Exception:
            continue
        if not href or not text:
            continue
        text = " ".join(text.split())
        if len(text) < 3 or len(text) > 160:
            continue
        url = urljoin(base_url, href)
        if not urlparse(url).scheme.startswith("http"):
            continue
        rows.append({"title": text, "url": url})
    return rows


def extract_links(page) -> list[dict]:
    """Visible anchors across main page + frames, deduped by (title, url)."""
    rows = []
    seen = set()
    for ctx in [page] + [f for f in page.frames]:
        base = getattr(ctx, "url", page.url)
        for r in _anchor_rows_from(ctx, base):
            key = (r["title"].lower(), r["url"])
            if key in seen:
                continue
            seen.add(key)
            rows.append(r)
    return rows


def find_jobs_portal_link(page) -> str | None:
    """Return an obvious jobs-portal link to follow, or None.

    Scoring: known ATS domain (+3), explicit portal link text (+2),
    'search'+job/career in path (+1). Follow only if score >= 2 ("obvious").
    """
    best_url, best_score = None, 0
    current_host = urlparse(page.url).netloc.lower()
    for r in extract_links(page):
        url, text = r["url"], r["title"].lower()
        host = urlparse(url).netloc.lower()
        path = urlparse(url).path.lower()
        score = 0
        if any(d in host for d in JOBS_PORTAL_DOMAINS) and host != current_host:
            score += 3
        if any(t in text for t in PORTAL_LINK_TEXTS):
            score += 2
        if "search" in path and ("job" in path or "career" in path):
            score += 1
        # prefer external job portals over same-page anchors
        if url.rstrip("/") == page.url.rstrip("/"):
            score = 0
        if score > best_score:
            best_url, best_score = url, score
    return best_url if best_score >= 2 else None


def is_plausible_job(title: str, url: str) -> bool:
    t, u = title.lower(), url.lower()
    if any(h in u for h in JOB_URL_HINTS):
        return True
    if any(k in t for k in JOB_TITLE_KEYWORDS):
        return True
    return False


def capture_plausible(page, employer, emp_url, ats, term) -> list[dict]:
    rows = []
    now = datetime.now(timezone.utc).isoformat()
    for r in extract_links(page):
        if is_plausible_job(r["title"], r["url"]):
            rows.append({
                "employer": employer,
                "employer_url": emp_url,
                "ats": ats,
                "search_term": term,
                "job_title": r["title"],
                "job_url": r["url"],
                "captured_at": now,
            })
    return rows


def process_employer(context, emp, idx) -> tuple[list[dict], dict]:
    employer = emp.get("employer", "UNKNOWN")
    url = emp.get("url", "")
    ats = emp.get("ats", "")
    info = {
        "idx": idx,
        "employer": employer,
        "url": url,
        "ats": ats,
        "nav_error": None,
        "search_box": False,
        "search_selector": None,
        "followed_portal": None,
        "final_url": "",
        "terms": [],
        "plausible_total": 0,
        "note": "",
    }
    rows: list[dict] = []
    page = context.new_page()
    try:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except Exception as exc:
            info["nav_error"] = repr(exc)
        try:
            page.wait_for_load_state("networkidle", timeout=12000)
        except Exception:
            pass
        page.wait_for_timeout(1500)
        dismiss_consent(page)

        box, sel = find_search_box(page)

        # Follow obvious jobs-portal links if no search box on the landing page.
        hops = 0
        while box is None and hops < MAX_PORTAL_HOPS:
            portal = find_jobs_portal_link(page)
            if not portal:
                break
            try:
                page.goto(portal, wait_until="domcontentloaded", timeout=45000)
                try:
                    page.wait_for_load_state("networkidle", timeout=10000)
                except Exception:
                    pass
                page.wait_for_timeout(1500)
                dismiss_consent(page)
                info["followed_portal"] = portal
                box, sel = find_search_box(page)
            except Exception as exc:
                info["note"] = f"portal_nav_error: {exc!r}"
                break
            hops += 1

        info["final_url"] = page.url
        info["search_box"] = box is not None
        info["search_selector"] = sel

        if box is not None:
            for term in SEARCH_TERMS:
                term_rec = {"term": term, "submitted": False, "plausible": 0,
                            "links": 0, "text_len": 0, "error": None}
                try:
                    box2, _ = find_search_box(page)
                    if box2 is not None:
                        box2.click(timeout=5000)
                        box2.fill("")
                        box2.fill(term)
                        box2.press("Enter")
                        term_rec["submitted"] = True
                    page.wait_for_timeout(WAIT_AFTER_SEARCH_SEC * 1000)
                    try:
                        page.wait_for_load_state("networkidle", timeout=8000)
                    except Exception:
                        pass
                    try:
                        term_rec["text_len"] = len(
                            page.locator("body").inner_text(timeout=5000))
                    except Exception:
                        pass
                    links = extract_links(page)
                    term_rec["links"] = len(links)
                    term_rows = capture_plausible(page, employer, url, ats, term)
                    term_rec["plausible"] = len(term_rows)
                    rows.extend(term_rows)
                except Exception as exc:
                    term_rec["error"] = repr(exc)
                info["terms"].append(term_rec)
        else:
            # No search box anywhere: capture the reachable page once.
            label = "(no search box)"
            try:
                text_len = len(page.locator("body").inner_text(timeout=5000))
            except Exception:
                text_len = 0
            page_rows = capture_plausible(page, employer, url, ats, label)
            rows.extend(page_rows)
            info["terms"].append({
                "term": label, "submitted": False, "plausible": len(page_rows),
                "links": 0, "text_len": text_len, "error": None,
            })
            if not info["note"]:
                info["note"] = "no search box found (landing + followed portal)"
    except Exception as exc:
        info["note"] = f"employer_error: {exc!r}"
    finally:
        try:
            page.close()
        except Exception:
            pass

    # Dedupe within this employer by (title, url); keep first surfacing term.
    deduped = []
    seen = set()
    for r in rows:
        key = (r["job_title"].lower(), r["job_url"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    info["plausible_total"] = len(deduped)
    return deduped, info


def write_outputs(out_csv: Path, out_audit: Path, all_rows, audits,
                  meta) -> None:
    fields = ["employer", "employer_url", "ats", "search_term",
              "job_title", "job_url", "captured_at"]
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)

    lines = [
        "# Phase 3C Browser Batch Audit",
        "",
        f"- **Queue:** {QUEUE_REL}",
        f"- **Employer range (1-indexed, inclusive):** {meta['start']}-{meta['end']}",
        f"- **Employers processed so far:** {len(audits)} / {meta['count']}",
        f"- **Browser:** Chromium {meta['browser_version']} (Playwright, headless={meta['headless']})",
        f"- **Started (UTC):** {meta['started']}",
        f"- **Last updated (UTC):** {datetime.now(timezone.utc).isoformat()}",
        f"- **Search terms (one at a time, no Boolean OR):** {', '.join(SEARCH_TERMS)}",
        f"- **computerUse manual clicking used:** no",
        f"- **Total plausible rows:** {len(all_rows)}",
        "",
        "## Per-employer summary",
        "",
        "| # | Employer | Search box | Followed portal | Plausible | Final URL | Note |",
        "|--:|----------|-----------|-----------------|----------:|-----------|------|",
    ]
    for a in audits:
        portal = a["followed_portal"] or "-"
        note = a["note"] or ("nav_error: " + a["nav_error"] if a["nav_error"] else "-")
        lines.append(
            f"| {a['idx']} | {a['employer']} | "
            f"{'yes' if a['search_box'] else 'no'} | {portal} | "
            f"{a['plausible_total']} | {a['final_url'] or '-'} | {note} |"
        )
    lines.append("")
    lines.append("## Per-employer term detail")
    lines.append("")
    for a in audits:
        lines.append(f"### {a['idx']}. {a['employer']}")
        lines.append("")
        lines.append(f"- Career URL: {a['url']}")
        lines.append(f"- ATS: {a['ats']}")
        lines.append(f"- Final URL: {a['final_url'] or '-'}")
        if a["followed_portal"]:
            lines.append(f"- Followed jobs portal: {a['followed_portal']}")
        lines.append(
            f"- Search box: {'yes (' + str(a['search_selector']) + ')' if a['search_box'] else 'no'}")
        if a["nav_error"]:
            lines.append(f"- Navigation error: {a['nav_error']}")
        lines.append("")
        lines.append("| Term | Submitted | Visible links | Plausible | Text len | Error |")
        lines.append("|------|-----------|--------------:|----------:|---------:|-------|")
        for t in a["terms"]:
            lines.append(
                f"| {t['term']} | {'yes' if t['submitted'] else 'no'} | "
                f"{t['links']} | {t['plausible']} | {t['text_len']} | {t['error'] or '-'} |")
        lines.append("")
    out_audit.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Phase 3C deterministic browser batch")
    ap.add_argument("--start", type=int, default=26, help="1-indexed start (inclusive)")
    ap.add_argument("--end", type=int, default=50, help="1-indexed end (inclusive)")
    ap.add_argument("--out-prefix", default="browser_batch02",
                    help="output filename prefix (relative to repo root if not a path)")
    ap.add_argument("--headed", action="store_true", help="run with a visible browser")
    args = ap.parse_args()

    prefix = Path(args.out_prefix)
    if not prefix.is_absolute() and prefix.parent == Path("."):
        prefix = REPO_ROOT / args.out_prefix
    out_csv = Path(str(prefix) + "_results.csv")
    out_audit = Path(str(prefix) + "_audit.md")

    queue = load_queue()
    start_i = max(args.start - 1, 0)
    end_i = min(args.end, len(queue))
    targets = list(enumerate(queue[start_i:end_i], start=args.start))
    if not targets:
        print("No employers in the requested range.", file=sys.stderr)
        return 1
    print(f"Processing employers {args.start}-{end_i} ({len(targets)} total)")

    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print("BROWSER LAUNCH FAILED (playwright import):", repr(exc), file=sys.stderr)
        return 2

    started = datetime.now(timezone.utc).isoformat()
    all_rows: list[dict] = []
    audits: list[dict] = []

    pw = None
    browser = None
    try:
        pw = sync_playwright().start()
        try:
            browser = pw.chromium.launch(headless=not args.headed)
        except Exception as exc:
            print("BROWSER LAUNCH FAILED:", file=sys.stderr)
            traceback.print_exc()
            print(f"\nExact error: {exc!r}", file=sys.stderr)
            return 2
        browser_version = browser.version
        print(f"Browser: Chromium {browser_version}")
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1366, "height": 900},
        )
        context.set_default_timeout(20000)

        meta = {
            "start": args.start, "end": end_i, "count": len(targets),
            "browser_version": browser_version, "headless": not args.headed,
            "started": started,
        }

        for idx, emp in targets:
            print(f"[{idx}] {emp.get('employer','?')} -> {emp.get('url','')}")
            try:
                rows, info = process_employer(context, emp, idx)
            except Exception as exc:
                rows, info = [], {
                    "idx": idx, "employer": emp.get("employer", "?"),
                    "url": emp.get("url", ""), "ats": emp.get("ats", ""),
                    "nav_error": None, "search_box": False,
                    "search_selector": None, "followed_portal": None,
                    "final_url": "", "terms": [], "plausible_total": 0,
                    "note": f"fatal: {exc!r}",
                }
            all_rows.extend(rows)
            audits.append(info)
            # Save progress after EVERY employer.
            write_outputs(out_csv, out_audit, all_rows, audits, meta)
            print(f"    box={'y' if info['search_box'] else 'n'} "
                  f"portal={'y' if info['followed_portal'] else 'n'} "
                  f"plausible={info['plausible_total']} (saved)")

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

    print("-" * 60)
    print(f"Done. {len(all_rows)} plausible rows across {len(audits)} employers.")
    print(f"Wrote {out_csv.name} and {out_audit.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
