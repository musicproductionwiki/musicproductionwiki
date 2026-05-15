# MPW-HANDOFF-SCRIPTS.md
*Updated: May 15, 2026 (SESSION 29)*

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

# mpw_bible_writer.py — v4.0 — SESSION 29

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_writer.py`

**Two-pass architecture. 55-check validation suite.**

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

```powershell
. .\setenv.ps1
python mpw_bible_writer.py --validate
python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing"
python mpw_bible_writer.py --test --slug air --term "Air Frequency EQ" --category "Frequency" --start-date 2026-05-12
python mpw_bible_writer.py --batch-file Bible-Batches/batch15.txt --start-date 2026-05-15
```

## v4.0 — 55-Check Validation Suite

```python
python3 -c "
content = open('mpw_bible_writer.py').read()
checks = {
    # v3.0 checks (42)
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
    'system prompt': 'system_prompt' in content or 'SYSTEM_PROMPT' in content,
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
    'faq 8 questions': 'faq' in content,
    'track_examples 5': 'track_examples' in content,
    'listening_guide': 'listening_guide' in content,
    'section_summaries': 'section_summaries' in content,
    'before_after_text': 'before_after_text' in content,
    # v4.0 new checks (13)
    'misconception-block CSS': 'misconception-block' in content,
    'producers-verdict CSS': 'producers-verdict' in content,
    'progression-path CSS': 'progression-path' in content,
    'red-flag CSS': 'red-flag' in content,
    'green-flag CSS': 'green-flag' in content,
    'genre-table CSS': 'genre-table' in content,
    'hardware-plugin CSS': 'hardware-plugin' in content,
    'the-number-box CSS': 'the-number-box' in content,
    'producer-quote-block CSS': 'producer-quote-block' in content,
    'section-summary CSS': 'section-summary' in content,
    'signal-chain CSS': 'signal-chain' in content,
    'no iframes': \"'<iframe'\" in content or '\"<iframe\"' in content,
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

# mpw_fix_spotify.py — SESSION 29 NEW

Patches eq.html and compression.html only — replaces Spotify iframes with green link buttons.
All other 199 v3.0 entries never had iframes — no patch needed.

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

TOKEN = 'YOUR_GITHUB_TOKEN_HERE'  # expires Aug 2, 2026 — set via $env:GITHUB_TOKEN or replace inline
REPO = 'musicproductionwiki/musicproductionwiki'
HEADERS = {'Authorization': f'token {TOKEN}', 'Accept': 'application/vnd.github.v3+json'}

def gh_trees_commit(file_dict, message):
    """file_dict = {path: content_string}"""
    # 1. Get latest commit SHA
    ref = requests.get(f'https://api.github.com/repos/{REPO}/git/ref/heads/main', headers=HEADERS).json()
    base_sha = ref['object']['sha']
    tree_sha = requests.get(f'https://api.github.com/repos/{REPO}/git/commits/{base_sha}', headers=HEADERS).json()['tree']['sha']

    # 2. Create blobs sequentially (no parallel — rate limits)
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

    # 3. Create tree
    new_tree = requests.post(f'https://api.github.com/repos/{REPO}/git/trees', headers=HEADERS,
        json={'base_tree': tree_sha, 'tree': blobs}).json()

    # 4. Create commit
    new_commit = requests.post(f'https://api.github.com/repos/{REPO}/git/commits', headers=HEADERS,
        json={'message': message, 'tree': new_tree['sha'], 'parents': [base_sha]}).json()

    # 5. Update ref
    requests.patch(f'https://api.github.com/repos/{REPO}/git/refs/heads/main', headers=HEADERS,
        json={'sha': new_commit['sha']})

    return new_commit['sha']
```

---

# MPW-CATALOG.md — Auto-Generated

MPW-CATALOG.md in repo root is the living article + Bible entry catalog.
Generated automatically by mpw_commit_articles.py and mpw_bible_writer.py after every successful commit.
Never edit manually — always regenerate from live slug list.
