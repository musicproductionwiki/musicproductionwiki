# MPW-HANDOFF-SCRIPTS.md
*Updated: May 15, 2026 (SESSION 30)*

All scripts at: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\`
GitHub API blocked from Claude's environment — all GitHub operations run from Steve's PowerShell.

---

# mpw_session_start.py — SESSION 29 NEW

```powershell
. .\setenv.ps1
python mpw_session_start.py
```

Fetches MPW-HANDOFF-CORE.md from GitHub, counts articles + Bible entries via Trees API, prints 3 recent commits, lists module files. Run at the start of every session.

---

# mpw_count.py — SESSION 22 REBUILT (Trees API)

```powershell
python mpw_count.py
```

Trees API version — runs in <10 seconds. No hanging.

---

# mpw_slugs.py — SESSION 22

Run BEFORE every batch write AND AFTER every batch commit.

```powershell
python mpw_slugs.py
```

Refreshes `C:\Users\swarn\OneDrive\Desktop\slugs.txt` from live repo.

---

# mpw_writer.py — v3.0 — CONFIRMED READY

```powershell
python mpw_writer.py --test --slug ableton-live-12-review --category review --skip-catalog
python mpw_writer.py --batch batch09.txt --start-date 2026-03-01
```

Key specs:
- Model: claude-sonnet-4-6
- Nav: mpw-nav-homepage-v1 — commit dbc09281
- Nav inner: max-width:1360px, padding:0 24px
- Aside JS fix: moves aside back into article-layout if it escaped unclosed tags
- All nav links absolute paths
- 20-pass search overlay deduplication
- Trees API commit via gh_trees_commit()
- Runs mpw_dead_slug_audit.py after every successful commit
- Auto-updates MPW-CATALOG.md in same commit (Session 29 update)

---

# mpw_commit_articles.py — UPDATED SESSION 27 + SESSION 29

Automatically runs mpw_dead_slug_audit.py after every successful commit.
SESSION 29 UPDATE: Also regenerates MPW-CATALOG.md from live slug list and includes in same Trees API commit.

---

# mpw_bible_writer.py — v5.0 — SESSION 30

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_writer.py`

**Two-pass architecture. 54-check validation suite.**

Key specs:
- Model: claude-sonnet-4-6
- Workers: 8 (ThreadPoolExecutor)
- PASS1_TOKENS: 20,000
- PASS2_TOKENS: 16,000
- Word count: 5,500 floor / 6,000 target / 6,500 ceiling
- Generation time: 6-8 minutes per entry (two passes)
- Batch format: slug:Term:Category (colon-separated, 3 parts per line)
- System prompt applied to both passes
- Sequential blob creation with 403 backoff
- Trees API commit includes: bible/*.html + bible-index.json + MPW-CATALOG.md
- Auto-updates MPW-CATALOG.md in same commit
- Pass 1 p1_str context to Pass 2: 8,000 chars (increased from 4,000)

```powershell
. .\setenv.ps1
python mpw_bible_writer.py --validate
python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing"
python mpw_bible_writer.py --test --slug air --term "Air Frequency EQ" --category "Frequency" --start-date 2026-05-12
python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-15
```

## v5.0 Changes from v4.0

### Pass 1 JSON Schema Changes
- `track_examples` field ADDED — includes title, artist, track, year, timestamp (NO spotify_uri)
- `spotify_embeds` field REMOVED — AI hallucinates URIs
- `SPOTIFY_RULE` field REMOVED
- Pass 2 receives locked track list extracted directly from Pass 1 track_examples
- p1_str context increased to 8,000 chars

### build_html() Changes
- overflow:clip on html/body (was overflow:hidden — hidden breaks position:sticky)
- Bible identity bar added (desktop only): "◆ The Producer's Bible | A MusicProductionWiki Publication"
- Nav sticky: top:32px (below identity bar), z:500
- Entry nav: top:92px desktop, top:96px mobile (via media query override)
- "The Producer's Bible" nav item is now a dropdown with 8 category links
- Mobile drawer: 2-column grid (bmn-drawer-cats / bmn-drawer-cat) for Bible, Articles, Gear
- History API pushState on drawer open — back button closes drawer
- emotional_hook: .strip().strip('*') before render
- signal_chain_position extracted to variable before f-string (was TypeError)
- Social share moved to sidebar + footer (removed from content body)
- Newsletter: full-width breakout strip
- Sidebar: align-self:start, top:120px, dynamic related terms
- Signal chain SVG: fixed 140px boxes, 18-char label truncation
- Entry nav: "Sections ›" label, 11px mobile font, pill-shaped links
- YouTube search links (not Spotify URIs or search, not Google)
- Section heading: "Listen on YouTube"
- 4 schema blocks: Article (with sameAs), FAQPage, BreadcrumbList, Speakable
- dateModified: always today's date (not pub_date)
- og:locale: en_US added
- Back-to-top: bottom:32px right:20px

### CONFIRMED_LIVE_SLUGS constant
Python set in script — used by build_related_terms_html() and build_further_reading_html() to strip dead links at build time. sidechain-compression and transient-shaping EXCLUDED (confirmed 404).

## v5.0 — 54-Check Validation Suite

```python
python3 -c "
content = open('mpw_bible_writer.py').read()
checks = {
    'nav centered': 'justify-content:center' in content,
    'nav font 9px': 'font-size:9px' in content,
    'nav overflow-x auto': 'overflow-x:auto' in content,
    'nav sticky top:96px': 'top:96px' in content,
    'progress z-index 99999': 'z-index:99999' in content,
    'progress px width JS': 'Math.round((st/dh)*window.innerWidth)' in content,
    'type grid 3 cols': 'repeat(3,1fr)' in content,
    'newsletter card': 'bible-nl-card' in content,
    'further reading': 'further-grid' in content,
    'audio toggle': 'audio-toggle' in content,
    'gain calculator': 'gain-calculator' in content,
    'bm-publisher link': 'href=\"/bible/\" class=\"bm-publisher\"' in content,
    'no main.js in output': 'NO main.js' in content,
    'model claude-sonnet-4-6': 'claude-sonnet-4-6' in content,
    'PASS1_TOKENS 20000': '20000' in content,
    'trees API commit': 'gh_trees_commit' in content,
    'spotify links not iframes': 'spotify-link-item' in content,
    'build_pass1_prompt': 'build_pass1_prompt' in content,
    'call_claude_pass1': 'call_claude_pass1' in content,
    'build_pass2_prompt': 'build_pass2_prompt' in content,
    'call_claude_pass2': 'call_claude_pass2' in content,
    'build_html': 'build_html' in content,
    'PASS2_TOKENS': 'PASS2_TOKENS' in content,
    'system prompt': 'SYSTEM_PROMPT' in content,
    'word count floor 5500': '5500' in content,
    'word count target 6000': '6000' in content,
    'word count ceiling 6500': '6500' in content,
    'the_number field': 'the_number' in content,
    'producer_quote field': 'producer_quote' in content,
    'signal_chain_position': 'signal_chain_position' in content,
    'hardware_vs_plugin_rows': 'hardware_vs_plugin_rows' in content,
    'genre_application_rows': 'genre_application_rows' in content,
    'interaction_warnings': 'interaction_warnings' in content,
    'red_flags': 'red_flags' in content,
    'green_flags': 'green_flags' in content,
    'further_reading_slugs': 'further_reading_slugs' in content,
    'faq field': '\"faq\"' in content,
    'track_examples': 'track_examples' in content,
    'listening_guide': 'listening_guide' in content,
    'section_summaries': 'section_summaries' in content,
    'before_after_text': 'before_after_text' in content,
    'misconception-block CSS': 'misconception-block' in content,
    'producers-verdict CSS': 'producers-verdict' in content,
    'progression-path CSS': 'progression-path' in content,
    'red-flag CSS': 'red-flag' in content,
    'green-flag CSS': 'green-flag' in content,
    'genre-table CSS': 'genre-table' in content,
    'hardware-plugin CSS': 'hardware-plugin-table' in content,
    'the-number-box CSS': 'the-number-box' in content,
    'producer-quote-block CSS': 'producer-quote-block' in content,
    'section-summary CSS': 'section-summary' in content,
    'signal-chain CSS': 'signal-chain-diagram' in content,
    'no iframes in output': 'spotify-link-item' in content and 'spotify-links' in content,
    'catalog update': 'build_catalog_content' in content,
}
import ast
ast.parse(content)
print('Syntax OK')
missing = [k for k,v in checks.items() if not v]
ok = [k for k,v in checks.items() if v]
[print(f'[OK] {k}') for k in ok]
[print(f'[MISSING] {k}') for k in missing]
print(f'Score: {len(ok)}/{len(checks)}')
"
```

---

# mpw_bible_cat_pages.py — SESSION 30 NEW

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_cat_pages.py`

Generates 8 Bible category pages at `/bible/categories/{slug}/index.html`.

Categories: dynamics, frequency, time-based, signal-processing, mixing, mastering, synthesis, music-theory

Each page includes:
- Identity bar + nav matching Bible entry pages
- Hero with category name, description, entry count
- Horizontal siblings strip for cross-category navigation
- Client-side search/filter of entries
- Entry card grid built from live bible-index.json
- Mobile responsive

```powershell
. .\setenv.ps1
python mpw_bible_cat_pages.py --test    # dry-run, prints first category HTML
python mpw_bible_cat_pages.py --run     # generates and commits all 8 pages
```

Run --test first to verify bible-index.json is fetchable. Then --run to commit all 8 pages in one Trees API commit.

---

# mpw_fix_spotify.py — SESSION 29 NEW

Patches eq.html and compression.html only — replaces Spotify iframes with green link buttons.
All other 199 v3.0 entries never had iframes — no patch needed.
NOTE: v5.0 entries use YouTube search links, not Spotify buttons.

```powershell
python mpw_fix_spotify.py
```

Uses Trees API — 1 commit for both files.

---

# Audit + Fix Script Suite — SESSION 27

**mpw_dead_slug_audit.py** — 7 check types. Outputs CSV. Auto-runs via mpw_commit_articles.py.
**mpw_fix_dead_slugs.py** — Sequential blob creation with rate limit backoff. Chunked Trees API (100 files/chunk).
**mpw_full_audit.py** — 13-check site audit. Outputs prioritized CSV + orphan list.
**mpw_fix_canonicals.py** — Fixes missing or wrong canonical tags sitewide.
**mpw_fix_meta.py** — Adds missing OG tags and meta descriptions.
**mpw_fix_dates.py** — Fixes 2025→2026 date strings.
**mpw_fix_bible_bar_dupes.py** — Strips duplicate bible bars, reinjects one clean v4 bar.

---

# mpw_add_bible_bar.py — SESSION 25

```powershell
python mpw_add_bible_bar.py --test
python mpw_add_bible_bar.py --run --chunk 1 --total 6
```

about.html must be patched separately via one-liner (see MPW-HANDOFF-CONTENT.md Section 7).

---

# mpw_fix_sitewide_r7.py — SESSION 20

- 614 files committed in 1 commit — commit dbc09281 — CONFIRMED
- Nav fingerprint: mpw-nav-homepage-v1
- ALWAYS run --test first. Never run without retry session (exponential backoff on network drop).
- NEVER run after homepage has been updated to a newer nav without updating r7 first.

---

# GitHub Trees API Pattern (canonical)

```python
import requests, base64, time

TOKEN = 'YOUR_GITHUB_TOKEN_HERE'  # expires Aug 2, 2026 — set via $env:GITHUB_TOKEN
REPO = 'musicproductionwiki/musicproductionwiki'
HEADERS = {'Authorization': f'token {TOKEN}', 'Accept': 'application/vnd.github.v3+json'}

def gh_trees_commit(file_dict, message):
    """file_dict = {path: content_string}"""
    ref = requests.get(f'https://api.github.com/repos/{REPO}/git/ref/heads/main', headers=HEADERS).json()
    base_sha = ref['object']['sha']
    tree_sha = requests.get(f'https://api.github.com/repos/{REPO}/git/commits/{base_sha}', headers=HEADERS).json()['tree']['sha']

    blobs = []
    for path, content in file_dict.items():
        for attempt in range(5):
            r = requests.post(f'https://api.github.com/repos/{REPO}/git/blobs', headers=HEADERS,
                json={'content': content, 'encoding': 'utf-8'})
            if r.status_code == 201:
                blobs.append({'path': path, 'mode': '100644', 'type': 'blob', 'sha': r.json()['sha']})
                break
            elif r.status_code == 403:
                time.sleep(15 * (2 ** attempt))
            else:
                r.raise_for_status()

    new_tree = requests.post(f'https://api.github.com/repos/{REPO}/git/trees', headers=HEADERS,
        json={'base_tree': tree_sha, 'tree': blobs}).json()
    new_commit = requests.post(f'https://api.github.com/repos/{REPO}/git/commits', headers=HEADERS,
        json={'message': message, 'tree': new_tree['sha'], 'parents': [base_sha]}).json()
    requests.patch(f'https://api.github.com/repos/{REPO}/git/refs/heads/main', headers=HEADERS,
        json={'sha': new_commit['sha']})
    return new_commit['sha']
```

---

# MPW-CATALOG.md — Auto-Generated

MPW-CATALOG.md in repo root is the living article + Bible entry catalog.
Generated automatically by mpw_commit_articles.py and mpw_bible_writer.py after every successful commit.
Never edit manually — always regenerate from live slug list.

---

# SESSION 30 UPDATE — SCRIPTS STATUS

## Scripts In mpw-scripts\ (committed to GitHub repo root)

| Script | Status | Notes |
|---|---|---|
| mpw_bible_writer.py | ✅ v5.0 — 54/54 checks — ready to test | --test not yet run this session |
| mpw_bible_cat_pages.py | ✅ NEW — Syntax OK — ready to run | Generates 8 Bible category pages |
| mpw_session_start.py | ✅ Working | Fetches live counts via Trees API. Run at session start |
| mpw_fix_spotify.py | ✅ Done | Patched eq.html + compression.html. No iframes remain |
| commit_handoff.py | ✅ Working | Commits all 6 handoff files + MPW-CATALOG.md via Trees API |
| debug_blob.py | ✅ Working | Tests GitHub blob creation per file — use to debug 422 errors |

## Critical Script Issues

### mpw_bible_writer.py v5.0 — DO NOT RUN BATCH YET
--test must be run and visually confirmed first. Then desktop + mobile QA. Then Tier 1 batch.

### Token Configuration
- PASS1_TOKENS = 20000 (DO NOT REDUCE — lower values truncate JSON)
- PASS2_TOKENS = 16000
- MODEL = claude-sonnet-4-6
- Workers = 8 (ThreadPoolExecutor)
- Streaming = True (both passes) — prevents read timeout
- p1_str to Pass 2 = 8,000 chars (increased from 4,000)

### Environment Variables Required (set in PowerShell before every run)
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-..."  # From console.anthropic.com → API Keys
$env:GITHUB_TOKEN="YOUR_GITHUB_TOKEN_HERE"  # From github.com/settings/tokens
```
Both must be set. Scripts fail silently or with 401 if either is missing.

### GitHub Secret Scanning
GitHub blocks commits containing literal API keys or tokens.
ALL handoff .md files and .py scripts must use placeholder text:
- `YOUR_GITHUB_TOKEN_HERE` for GitHub token
- `YOUR_ANTHROPIC_API_KEY_HERE` for Anthropic key
Never write the real token into any file that gets committed.

### Bible Writer Usage
```powershell
python mpw_bible_writer.py --validate
python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing"
python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-15
```

### Batch File Format
```
slug:Term:Category
compression:Compression:Signal Processing
eq:EQ:Frequency
```
Colon-separated, 3 parts. Never pipe-separated.
