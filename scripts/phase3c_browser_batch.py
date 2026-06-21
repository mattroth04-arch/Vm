#!/usr/bin/env python3
"""Reusable deterministic Playwright browser search for a Phase 3C employer range.

Generalizes the single-employer pilot to process a *range* of employers from the
Phase 3C queue, deterministically (no computerUse / manual clicking), with
low-false-positive job extraction.

For each employer in the range it:
  1. Opens the career URL and waits for load (auto-dismisses consent banners).
  2. Detects whether a free-text search box exists (page + iframes).
  3. If no search box is found, follows an *obvious* link to the real jobs
     portal (known ATS domains or explicit "search jobs"-style links) and
     re-detects a search box there.
  4. If a search box exists, submits each search term one at a time
     (no Boolean OR), pressing Enter, waiting 3s, and extracting candidate jobs.
  5. Records blockers (timeout / dead URL / login wall / CAPTCHA / bot block)
     and continues to the next employer.
  6. Saves progress (results CSV + audit MD) after EVERY employer.

Job extraction is conservative to reduce false positives:
  - Prefers anchors inside job-card / result containers when such containers
    exist on the page ("when possible"); otherwise falls back to all visible
    anchors.
  - Excludes navigation / footer / login / privacy / category links.
  - Requires each candidate to match a plausible job-title pattern (a role noun
    in a title-shaped string), not just any link text.
  - Records an `extraction_reason` for every written row.

Authoritative inventory files (current_results.csv, applied_jobs.csv,
master_seen_jobs.csv) are never read or written.

If the browser fails to launch, the exact error is printed and the script exits
non-zero without writing partial results.

Usage:
  python3 scripts/phase3c_browser_batch.py [--start 51] [--end 150]
                                           [--out-prefix browser_batch03]
                                           [--headed]
Range is 1-indexed and inclusive.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
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

# URL substrings that indicate a job posting/listing (positive signal).
JOB_URL_HINTS = (
    "/job/", "/jobs/", "/job-", "jobid", "job_id", "requisition", "/req",
    "/posting", "/position", "/opening", "/vacanc", "gh_jid", "/jr",
    "myworkdayjobs", "lever.co/", "icims.com/jobs", "/careersection",
    "candidateexperience", "/job-boards", "/postings/",
)

# Role nouns (substring match) that make a multi-word title plausible.
ROLE_NOUNS = (
    "analyst", "scientist", "engineer", "manager", "specialist", "researcher",
    "epidemiolog", "associate", "director", "coordinator", "consultant",
    "writer", "statistician", "biostat", "economist", "fellow", "technician",
    "technologist", "developer", "advisor", "officer", "nurse", "physician",
    "clinician", "pharmacist", "professor", "faculty", "instructor",
    "lecturer", "administrator", "supervisor", "assistant", "practitioner",
    "therapist", "programmer", "architect", "strategist", "planner",
    "auditor", "investigator", "liaison", "educator", "counselor",
    "dietitian", "surgeon", "psychologist", "fellowship", "internship",
    "manager,", "lead ", "lead,", "analytics ", "research associate",
    "research scientist", "data analyst", "data scientist",
)
# Words that are valid job titles even as a single token.
STRONG_STANDALONE = {
    "epidemiologist", "biostatistician", "statistician", "researcher",
    "scientist", "analyst", "physician", "pharmacist", "economist",
    "technologist", "programmer", "psychologist", "epidemiology",
}

# Title substrings that mark a link as navigation/footer/category (excluded).
NAV_TITLE_TOKENS = (
    "login", "log in", "sign in", "signin", "sign up", "register",
    "create account", "create profile", "my account", "profile", "dashboard",
    "saved job", "saved search", "bookmark", "job cart", "job alert",
    "create alert", "privacy", "cookie", "terms of", "terms and",
    "accessibility", "contact", "about us", "about abbott", "our culture",
    "culture", "benefits", "blog", "newsroom", "news", "press", "media",
    "events", "faq", "help center", "support", "sitemap", "language",
    "skip to", "share", "equal opportunity", "eeo", "accommodation",
    "recruitment fraud", "diversity", "students", "early careers",
    "alumni", "veterans", "military", "locations", "our people",
    "leadership", "investor", "supplier", "overview", "our research",
    "therapeutic area", "pipeline", "resources", "resource center",
    "insights", "report", "stories", "story", "gallery", "video",
    "podcast", "webinar", "learn more", "read more", "explore ",
    "see all", "view all", "browse", "home", "search jobs", "search all",
    "find jobs", "job search", "all jobs", "all openings", "why work",
    "working at", "life at", "meet our", "our team", "our story",
    "frequently asked", "candidate", "talent community", "join our",
    "follow us", "social", "back to", "next", "previous", "load more",
    "show more", "filter", "sort", "menu", "cookies settings",
    "do not sell", "feedback", "newsletter", "subscribe",
)
NAV_URL_TOKENS = (
    "/login", "/signin", "/sign-in", "/sign_in", "/register", "/privacy",
    "/cookie", "/terms", "/accessibility", "/contact", "/about", "/benefit",
    "/blog", "/news", "/press", "/event", "/faq", "/help", "/sitemap",
    "/saved", "/alert", "/diversity", "/students", "/alumni", "/veterans",
    "/location", "/leadership", "/investor", "/culture", "/why-",
    "/life-at", "/talent-community", "/talentcommunity", "/our-people",
    "mailto:", "tel:", "javascript:", "/podcast", "/webinar", "/media",
    "/social", "/newsletter", "/subscribe",
)
NAV_URL_SUFFIXES = (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".zip")

# Page-text markers that indicate the page is blocked / behind a wall.
BLOCKER_MARKERS = (
    "captcha", "are you a robot", "verify you are human", "verify you're human",
    "access denied", "request blocked", "pardon our interruption",
    "unusual traffic", "attention required", "please enable javascript and",
    "incapsula", "bot detection", "403 forbidden", "forbidden",
    "this site can", "temporarily unavailable",
)

# JS that returns metadata for every anchor in a document/frame in one call.
_ANCHOR_JS = r"""
() => {
  const CARD = /(job|posting|opening|vacanc|result|career-card|position|req)/i;
  const out = [];
  const anchors = document.querySelectorAll('a[href]');
  anchors.forEach(a => {
    let text = (a.innerText || a.textContent || '').replace(/\s+/g, ' ').trim();
    const href = a.href || '';
    if (!href) return;
    let visible = true;
    try {
      const r = a.getBoundingClientRect();
      const s = window.getComputedStyle(a);
      visible = !!s && s.display !== 'none' && s.visibility !== 'hidden'
                && (r.width > 0 || r.height > 0);
    } catch (e) {}
    let inCard = false, cardLabel = '';
    let el = a;
    for (let d = 0; d < 5 && el; d++) {
      const cls = ((el.className && el.className.toString) ? el.className.toString() : '') + ' ' + (el.id || '');
      let da = '';
      try { da = el.getAttribute('data-automation-id') || ''; } catch (e) {}
      if (CARD.test(cls) || CARD.test(da)) {
        inCard = true; cardLabel = (cls + ' ' + da).trim().slice(0, 50);
        break;
      }
      el = el.parentElement;
    }
    let selfDa = '';
    try { selfDa = a.getAttribute('data-automation-id') || ''; } catch (e) {}
    out.push({ text, href, visible, inCard, cardLabel, da: selfDa });
  });
  return out;
}
"""


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
    for ctx in [page] + [f for f in page.frames]:
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


def anchor_meta(page) -> list[dict]:
    """All anchors (with metadata) across the main page + same-origin frames."""
    metas: list[dict] = []
    contexts = [page] + [f for f in page.frames]
    for ctx in contexts:
        try:
            rows = ctx.evaluate(_ANCHOR_JS)
        except Exception:
            continue
        if rows:
            metas.extend(rows)
    return metas


def body_text(page) -> str:
    try:
        return (page.evaluate(
            "() => document.body ? document.body.innerText : ''") or "")
    except Exception:
        return ""


def find_jobs_portal_link(page) -> str | None:
    best_url, best_score = None, 0
    current_host = urlparse(page.url).netloc.lower()
    for m in anchor_meta(page):
        if not m.get("visible") or not m.get("text"):
            continue
        url = m["href"]
        text = m["text"].lower()
        host = urlparse(url).netloc.lower()
        path = urlparse(url).path.lower()
        if not urlparse(url).scheme.startswith("http"):
            continue
        score = 0
        if any(d in host for d in JOBS_PORTAL_DOMAINS) and host != current_host:
            score += 3
        if any(t in text for t in PORTAL_LINK_TEXTS):
            score += 2
        if "search" in path and ("job" in path or "career" in path):
            score += 1
        if url.rstrip("/") == page.url.rstrip("/"):
            score = 0
        if score > best_score:
            best_url, best_score = url, score
    return best_url if best_score >= 2 else None


def is_nav_link(title: str, url: str) -> bool:
    low_t = title.lower()
    low_u = url.lower()
    if any(tok in low_t for tok in NAV_TITLE_TOKENS):
        return True
    if any(tok in low_u for tok in NAV_URL_TOKENS):
        return True
    if low_u.split("?")[0].endswith(NAV_URL_SUFFIXES):
        return True
    return False


def is_plausible_title(title: str) -> bool:
    t = title.strip()
    if not (3 <= len(t) <= 120):
        return False
    if not re.search(r"[A-Za-z]{3,}", t):
        return False
    words = [w for w in re.split(r"\s+", t) if w]
    if not (1 <= len(words) <= 12):
        return False
    low = t.lower()
    if len(words) == 1:
        token = re.sub(r"[^a-z]", "", words[0].lower()).rstrip("s")
        return token in STRONG_STANDALONE
    return any(rn in low for rn in ROLE_NOUNS)


def classify_anchor(m: dict, card_mode: bool):
    """Return (is_candidate, extraction_reason or None)."""
    title = (m.get("text") or "").strip()
    url = m.get("href") or ""
    if not m.get("visible") or not title:
        return False, None
    if not urlparse(url).scheme.startswith("http"):
        return False, None
    if is_nav_link(title, url):
        return False, None
    if not is_plausible_title(title):
        return False, None
    signals = []
    if m.get("inCard"):
        signals.append(f"card[{(m.get('cardLabel') or '').strip()}]")
    if m.get("da"):
        signals.append(f"data-automation-id={m['da']}")
    low_u = url.lower()
    hit = next((h for h in JOB_URL_HINTS if h in low_u), None)
    if hit:
        signals.append(f"url[{hit}]")
    if not card_mode:
        signals.append("fallback")
    signals.append("title_pattern")
    return True, "; ".join(signals)


def capture_into(page, term, acc, employer, emp_url, ats) -> None:
    """Extract candidate jobs for the current page state into `acc`.

    Updates acc['raw'] (set), acc['nav'] (set), acc['cands'] (dict).
    Prefers job-card anchors when any exist on the page.
    """
    metas = anchor_meta(page)
    visible = [m for m in metas if m.get("visible") and (m.get("text") or "").strip()]

    has_cards = any(
        m.get("inCard") or "jobtitle" in (m.get("da") or "").lower()
        for m in visible
    )
    pool = [m for m in visible
            if (m.get("inCard") or "jobtitle" in (m.get("da") or "").lower())] \
        if has_cards else visible

    now = datetime.now(timezone.utc).isoformat()
    for m in visible:
        title = (m["text"]).strip()
        url = m["href"]
        key = (title.lower(), url)
        acc["raw"].add(key)
        if is_nav_link(title, url):
            acc["nav"].add(key)

    for m in pool:
        is_cand, reason = classify_anchor(m, card_mode=has_cards)
        if not is_cand:
            continue
        title = m["text"].strip()
        url = m["href"]
        key = (title.lower(), url)
        if key in acc["cands"]:
            continue
        acc["cands"][key] = {
            "employer": employer,
            "employer_url": emp_url,
            "ats": ats,
            "search_term": term,
            "job_title": title,
            "job_url": url,
            "extraction_reason": reason,
            "captured_at": now,
        }


def process_employer(context, emp, idx) -> tuple[list[dict], dict]:
    employer = emp.get("employer", "UNKNOWN")
    url = emp.get("url", "")
    ats = emp.get("ats", "")
    info = {
        "idx": idx, "employer": employer, "url": url, "ats": ats,
        "search_box_found": False, "search_selector": None,
        "jobs_portal_followed": None, "final_url": "",
        "terms_searched": 0, "raw_links_seen": 0, "excluded_nav_links": 0,
        "candidate_job_links": 0, "blockers": [],
    }
    acc = {"raw": set(), "nav": set(), "cands": {}}
    page = context.new_page()
    try:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
        except Exception as exc:
            name = type(exc).__name__
            info["blockers"].append(
                "timeout" if "Timeout" in name else f"nav_error:{name}")
        try:
            page.wait_for_load_state("networkidle", timeout=10000)
        except Exception:
            pass
        page.wait_for_timeout(1200)
        dismiss_consent(page)

        # Blocker detection on landing page.
        if page.url.startswith("chrome-error"):
            info["blockers"].append("page_load_failed")
        txt = body_text(page).lower()
        marker = next((mk for mk in BLOCKER_MARKERS if mk in txt), None)
        if marker:
            info["blockers"].append(f"blocked:{marker}")

        box, sel = find_search_box(page)
        hops = 0
        while box is None and hops < MAX_PORTAL_HOPS:
            portal = find_jobs_portal_link(page)
            if not portal:
                break
            try:
                page.goto(portal, wait_until="domcontentloaded", timeout=40000)
                try:
                    page.wait_for_load_state("networkidle", timeout=10000)
                except Exception:
                    pass
                page.wait_for_timeout(1200)
                dismiss_consent(page)
                info["jobs_portal_followed"] = portal
                if "login" in page.url.lower() or "signin" in page.url.lower():
                    info["blockers"].append("login_wall")
                box, sel = find_search_box(page)
            except Exception as exc:
                info["blockers"].append(f"portal_nav_error:{type(exc).__name__}")
                break
            hops += 1

        info["final_url"] = page.url
        info["search_box_found"] = box is not None
        info["search_selector"] = sel

        if box is not None:
            for term in SEARCH_TERMS:
                try:
                    box2, _ = find_search_box(page)
                    if box2 is not None:
                        box2.click(timeout=5000)
                        box2.fill("")
                        box2.fill(term)
                        box2.press("Enter")
                        info["terms_searched"] += 1
                    page.wait_for_timeout(WAIT_AFTER_SEARCH_SEC * 1000)
                    try:
                        page.wait_for_load_state("networkidle", timeout=8000)
                    except Exception:
                        pass
                    capture_into(page, term, acc, employer, url, ats)
                except Exception as exc:
                    info["blockers"].append(f"term_error[{term}]:{type(exc).__name__}")
        else:
            capture_into(page, "(no search box)", acc, employer, url, ats)
            if not info["blockers"]:
                info["blockers"].append("no_search_box")
    except Exception as exc:
        info["blockers"].append(f"employer_error:{type(exc).__name__}")
    finally:
        try:
            page.close()
        except Exception:
            pass

    info["raw_links_seen"] = len(acc["raw"])
    info["excluded_nav_links"] = len(acc["nav"])
    rows = list(acc["cands"].values())
    info["candidate_job_links"] = len(rows)
    return rows, info


def write_outputs(out_csv: Path, out_audit: Path, all_rows, audits, meta) -> None:
    fields = ["employer", "employer_url", "ats", "search_term",
              "job_title", "job_url", "extraction_reason", "captured_at"]
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)

    tot_raw = sum(a["raw_links_seen"] for a in audits)
    tot_nav = sum(a["excluded_nav_links"] for a in audits)
    tot_cand = sum(a["candidate_job_links"] for a in audits)
    with_results = sum(1 for a in audits if a["candidate_job_links"] > 0)
    blocked = sum(1 for a in audits if a["blockers"])

    lines = [
        "# Phase 3C Browser Batch Audit",
        "",
        f"- **Queue:** {QUEUE_REL}",
        f"- **Employer range (1-indexed, inclusive):** {meta['start']}-{meta['end']}",
        f"- **Employers processed so far:** {len(audits)} / {meta['count']}",
        f"- **Employers with results:** {with_results}",
        f"- **Employers with blockers:** {blocked}",
        f"- **Browser:** Chromium {meta['browser_version']} (Playwright, headless={meta['headless']})",
        f"- **Started (UTC):** {meta['started']}",
        f"- **Last updated (UTC):** {datetime.now(timezone.utc).isoformat()}",
        f"- **Search terms (one at a time, no Boolean OR):** {', '.join(SEARCH_TERMS)}",
        f"- **computerUse manual clicking used:** no",
        f"- **Totals:** raw_links_seen={tot_raw}, excluded_nav_links={tot_nav}, candidate_job_links={tot_cand}",
        "",
        "## Per-employer summary",
        "",
        "| # | Employer | Box | Portal followed | Terms | Raw links | Excluded nav | Candidates | Blockers |",
        "|--:|----------|-----|-----------------|------:|----------:|-------------:|-----------:|----------|",
    ]
    for a in audits:
        portal = a["jobs_portal_followed"] or "-"
        blk = ", ".join(a["blockers"]) if a["blockers"] else "-"
        lines.append(
            f"| {a['idx']} | {a['employer']} | "
            f"{'yes' if a['search_box_found'] else 'no'} | {portal} | "
            f"{a['terms_searched']} | {a['raw_links_seen']} | "
            f"{a['excluded_nav_links']} | {a['candidate_job_links']} | {blk} |"
        )
    lines += ["", "## Sample candidates (first 3 per employer with results)", ""]
    by_emp: dict[str, list[dict]] = {}
    for r in all_rows:
        by_emp.setdefault(r["employer"], []).append(r)
    for a in audits:
        emp_rows = by_emp.get(a["employer"], [])
        if not emp_rows:
            continue
        lines.append(f"### {a['idx']}. {a['employer']}")
        for r in emp_rows[:3]:
            lines.append(
                f"- **{r['job_title']}** — {r['job_url']} "
                f"_(term: {r['search_term']}; {r['extraction_reason']})_")
        lines.append("")
    out_audit.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Phase 3C deterministic browser batch")
    ap.add_argument("--start", type=int, default=51, help="1-indexed start (inclusive)")
    ap.add_argument("--end", type=int, default=150, help="1-indexed end (inclusive)")
    ap.add_argument("--out-prefix", default="browser_batch03",
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
                    "search_box_found": False, "search_selector": None,
                    "jobs_portal_followed": None, "final_url": "",
                    "terms_searched": 0, "raw_links_seen": 0,
                    "excluded_nav_links": 0, "candidate_job_links": 0,
                    "blockers": [f"fatal:{type(exc).__name__}"],
                }
            all_rows.extend(rows)
            audits.append(info)
            write_outputs(out_csv, out_audit, all_rows, audits, meta)
            print(f"    box={'y' if info['search_box_found'] else 'n'} "
                  f"portal={'y' if info['jobs_portal_followed'] else 'n'} "
                  f"raw={info['raw_links_seen']} nav={info['excluded_nav_links']} "
                  f"cand={info['candidate_job_links']} "
                  f"blk={','.join(info['blockers']) or '-'} (saved)")

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
    print(f"Done. {len(all_rows)} candidate rows across {len(audits)} employers.")
    print(f"Wrote {out_csv.name} and {out_audit.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
