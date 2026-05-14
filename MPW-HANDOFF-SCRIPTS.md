# MPW — Script Reference
*Fetch via: `python mpw_session_start.py --fetch scripts`*
*All scripts live at: C:\Users\swarn\OneDrive\Desktop\mpw-scripts\*

---

## ENVIRONMENT SETUP (every session)
```powershell
cd C:\Users\swarn\OneDrive\Desktop\mpw-scripts
. .\setenv.ps1
```
setenv.ps1 loads: ANTHROPIC_API_KEY, GITHUB_TOKEN, REPO

---

## mpw_count.py — Article Count
```
python mpw_count.py
```
Counts .html files in /articles/ via Trees API. Runs in <10 seconds. Use ONLY this version — the old Contents API version hangs on Steve's network.

---

## mpw_slugs.py — Refresh Slug Catalog
```
python mpw_slugs.py
```
Pulls live slug list from GitHub Trees API → slugs.txt.
Run BEFORE every batch write AND AFTER every batch commit.

---

## mpw_writer.py v3.0 — New Article Writer
```
# Test single article:
python mpw_writer.py --test --slug ableton-live-12-review

# Write single article with explicit category:
python mpw_writer.py --articles "my-new-slug:review"

# Write batch from file:
python mpw_writer.py --batch-file Batches/batch09.txt --batch 09 --session A

# Skip slug catalog check (new topics not yet in catalog):
python mpw_writer.py --test --slug new-topic-slug --skip-catalog

# Dump shell only (diagnostic):
python mpw_writer.py --dump-shell

# With backdating:
python mpw_writer.py --batch-file Batches/batch09.txt --start-date 2026-05-01
```
Model: claude-sonnet-4-6 — Workers: 8 — Output: ./new-articles/

**After each batch:**
1. `python mpw_commit_articles.py --folder new-articles --dry-run`
2. `python mpw_commit_articles.py --folder new-articles`
3. `python mpw_fix_sitewide_r7.py --test` (safety check — r7 nav already baked in by writer)

---

## mpw_commit_articles.py — Commit Batch to GitHub
```
python mpw_commit_articles.py --folder new-articles --dry-run
python mpw_commit_articles.py --folder new-articles
```
Uses Trees API. Auto-runs mpw_dead_slug_audit.py after successful commit.

---

## mpw_bible_writer.py v2.0 — Bible Entry Writer
```
python mpw_bible_writer.py --test --slug eq --term "EQ" --category "Frequency"
python mpw_bible_writer.py --batch-file Bible-Batches/batch14-B.txt --start-date 2026-05-12
python mpw_bible_writer.py --batch-file Bible-Batches/batch14-C.txt
python mpw_bible_writer.py --dry-run --batch-file Bible-Batches/batch14-B.txt
```
Model: claude-sonnet-4-6 — Workers: 8 — PASS1_TOKENS: 20,000 (required — lower values truncate JSON)
Generation time: 4-5 minutes per entry. Cost: ~$25 for 200 entries.
NEVER load main.js on Bible pages — conflicts with Bible nav JS.

---

## mpw_fix_sitewide_r7.py — Canonical Sitewide Nav Script
```
python mpw_fix_sitewide_r7.py --test
python mpw_fix_sitewide_r7.py
```
ALWAYS run --test first. Full run touches 615 files. Uses Trees API.

---

## mpw_full_audit.py — 13-Check Comprehensive Audit
```
python mpw_full_audit.py
```
Checks: canonicals, meta, OG, dates, bible bars, nav fingerprint, structural elements, word count, orphans, duplicate titles, canonical format, robots meta, search index entry.
Last run: May 14, 2026 — 12 total issues (7 date-2025, 5 missing og:image). Run weekly.

---

## mpw_dead_slug_audit.py — Dead Slug Audit
```
python mpw_dead_slug_audit.py
```
7-check audit: related-cards, sidebar items, body links, category cards, search-index.json, sitemap.xml, root files. 20 parallel threads — outputs CSV.
Auto-runs after mpw_commit_articles.py.

---

## mpw_fix_dead_slugs.py — Fix Dead Slug References Sitewide
```
python mpw_fix_dead_slugs.py --dry-run
python mpw_fix_dead_slugs.py
```
Parallel fetch (10 threads max), sequential blob creation with rate limit backoff, chunked Trees API (100 files/chunk).

---

## mpw_fix_dates.py — Fix 2025 Date Strings
```
python mpw_fix_dates.py --dry-run
python mpw_fix_dates.py --test
python mpw_fix_dates.py --run
```

---

## mpw_fix_canonicals.py — Fix Missing/Wrong Canonical Tags
```
python mpw_fix_canonicals.py --dry-run
python mpw_fix_canonicals.py --test
python mpw_fix_canonicals.py --run
```

---

## mpw_fix_meta.py — Add Missing OG Tags + Meta Descriptions
```
python mpw_fix_meta.py
```
Derives from existing title + quick-answer box. 5 articles still missing og:image — rate limited Session 27 — retry with 15 min cooldown.

---

## mpw_fix_bible_bar_dupes.py — Fix Duplicate Bible Bars
```
python mpw_fix_bible_bar_dupes.py
```
Strips duplicate bible bars, reinjects exactly one clean v4 bar sitewide. Trees API.

---

## mpw_fix_titles.py — Fix Garbled Article Titles
```
python mpw_fix_titles.py
```
Fixes <title> tags via Trees API. Session 22 — 291 articles fixed — commit 40209fe3.

---

## mpw_rewrite_critical.py — Rewrite Critical Articles (Multiagent)
```
python mpw_rewrite_critical.py --dry-run
python mpw_rewrite_critical.py --test --slug [slug]
python mpw_rewrite_critical.py
```
8 workers. ALWAYS dry-run first. Session 21 — 18 CRITICAL articles — ALL LIVE.

---

## mpw_session_start.py — Session Start Gate (NEW Session 28)
```
python mpw_session_start.py
python mpw_session_start.py --fetch scripts
python mpw_session_start.py --fetch content
python mpw_session_start.py --fetch bible
python mpw_session_start.py --fetch articles
python mpw_session_start.py --fetch tech
```
Fetches MPW-HANDOFF-CORE.md from GitHub, prints it. Confirms article count via Trees API. Prints 3 most recent commits. Lists all 6 module files.

---

## mpw_commit_handoff.py — Commit All 6 Handoff Files (NEW Session 28)
```
python mpw_commit_handoff.py
```
Reads all 6 MPW-HANDOFF-*.md files from current directory. Commits to repo root via Trees API. Single commit — single Netlify deploy.

---

## about.html Bible Bar Patch One-Liner
```powershell
cd C:\Users\swarn\OneDrive\Desktop\mpw-scripts
. .\setenv.ps1
python -c "
import base64, requests
TOKEN = 'ghp_YOUR_TOKEN_HERE'
REPO = 'musicproductionwiki/musicproductionwiki'
headers = {'Authorization': f'token {TOKEN}', 'Accept': 'application/vnd.github.v3+json'}
r = requests.get(f'https://api.github.com/repos/{REPO}/contents/about.html', headers=headers)
sha = r.json()['sha']
html = base64.b64decode(r.json()['content']).decode('utf-8')
if 'bible-bar-v4' in html:
    print('Already patched')
else:
    from mpw_add_bible_bar import INJECT, NAV_MARKER, strip_old_bars
    html = strip_old_bars(html)
    html = html.replace(NAV_MARKER, INJECT + NAV_MARKER, 1)
    encoded = base64.b64encode(html.encode('utf-8')).decode()
    res = requests.put(f'https://api.github.com/repos/{REPO}/contents/about.html',
        headers=headers,
        json={'message': 'Add bible bar to about.html (bible-bar-v4)', 'content': encoded, 'sha': sha})
    print(res.status_code, res.json().get('commit', {}).get('sha', ''))
"
```
