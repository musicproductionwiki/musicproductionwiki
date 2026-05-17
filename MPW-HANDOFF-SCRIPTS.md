# MPW-HANDOFF-SCRIPTS.md
*Updated: May 17, 2026 (SESSION 34)*

All scripts at: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\`
GitHub API blocked from Claude's environment — all GitHub operations run from Steve's PowerShell.

---

# mpw_session_start.py

```powershell
. .\setenv.ps1
python mpw_session_start.py
```

Fetches MPW-HANDOFF-CORE.md from GitHub, counts articles + Bible entries via Trees API, prints 3 recent commits, lists module files. Run at the start of every session.

---

# mpw_count.py — Trees API version

```powershell
python mpw_count.py
```

Trees API version — runs in under 10 seconds. No hanging.

---

# mpw_slugs.py

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
- Auto-updates MPW-CATALOG.md in same commit

---

# mpw_commit_articles.py — UPDATED SESSION 27 + SESSION 29

Automatically runs mpw_dead_slug_audit.py after every successful commit.
SESSION 29 UPDATE: Also regenerates MPW-CATALOG.md from live slug list and includes in same Trees API commit.

---

# mpw_bible_writer.py — v5.1 — SESSION 33 UPDATE REQUIRED

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_writer.py`

**STATUS: Writer needs update to Session 33 to generate v5.1 template matching gold standard.**
**The gold standard compression.html is the literal reference — read it before writing.**

## Run Commands

```powershell
. .\setenv.ps1
python mpw_bible_writer.py --validate
python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing"
python mpw_bible_writer.py --test --slug eq --term "EQ" --category "Frequency" --tier 1
python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-16
```

## Architecture

**Three-tier routing (NEW in v5.1):**
```
slug:Term:Category:Tier  (4 parts, colon-separated)
Tier 1 → build_html_t1()  — 6,800-7,800 words — full gold standard template
Tier 2 → build_html_t2()  — 3,800-5,000 words — standard template
Tier 3 → build_html_t3()  — 1,500-2,500 words — reference template
```

**Pass Architecture:**
- Pass 1 (20,000 tokens) — Structured JSON data
- Pass 1.5 (no API call) — quotes.json filter by tag
- Pass 2 (22,000 tokens Tier 1 / 14,000 Tier 2 / 8,000 Tier 3) — Prose HTML

**Key constants:**
- Model: claude-sonnet-4-6
- PASS1_TOKENS: 20000
- PASS2_TOKENS_T1: 22000
- PASS2_TOKENS_T2: 14000
- PASS2_TOKENS_T3: 8000
- WORD_FLOOR_T1: 6800 / WORD_CEIL_T1: 7800
- WORD_FLOOR_T2: 3800 / WORD_CEIL_T2: 5000
- WORD_FLOOR_T3: 1500 / WORD_CEIL_T3: 2500

## Pass 1 JSON Schema — All Required Fields

v5.0 fields (unchanged):
term, slug, category, tags, definition, emotional_hook, signal_chain_position, section_summaries, track_examples (list of {artist, track, year, album, produced_by, timestamp, listening_guide}), producers_verdict, progression_path, red_flags, green_flags, interaction_warnings, faq (list of {q, a}), further_reading_slugs, related_terms (list of {term, slug, preview}), hardware_vs_plugin_rows, genre_application_rows, types, section_mistakes, producer_quote, producer_quote_tags, wikipedia_slug, wikidata_id

NEW v5.1 fields:
```json
{
  "difficulty": "Beginner|Intermediate|Advanced",
  "prerequisites": ["slug1", "slug2", "slug3"],
  "misconception": {"myth": "...", "truth": "..."},
  "before_after_text": {"before": "...", "after": "..."},
  "the_number": "4:1",
  "the_number_label": "typical compression ratio for drums",
  "the_number_context": "1-2 sentences",
  "daw_implementations": {
    "ableton": "...", "logic": "...", "fl_studio": "...", "pro_tools": "..."
  },
  "plugin_recommendations": {
    "free": [{"name": "...", "manufacturer": "..."}],
    "mid": [{"name": "...", "manufacturer": "..."}],
    "pro": [{"name": "...", "manufacturer": "..."}]
  },
  "genre_settings_rows": [
    {"genre": "Trap", "ratio": "8:1-20:1", "attack": "...", "release": "...", "threshold": "...", "notes": "..."}
  ],
  "next_steps": {
    "beginner_slug": "gain-staging",
    "deeper_slug": "parallel-compression",
    "problem_slug": "bus-compression"
  },
  "tool_type": "calculator",
  "comparison_terms": [
    {"term": "Limiting", "slug": "limiting"},
    {"term": "Saturation", "slug": "saturation"}
  ]
}
```

All slug fields validated against CONFIRMED_LIVE_SLUGS at build time. Invalid slugs → null.

## Pass 1.5 — Quotes Filter

```python
def load_quotes(path='quotes.json'):
    # load from same dir as script
def filter_quotes(quotes, tags, max_results=10):
    # score by tag overlap, return top max_results
def build_quotes_context(quotes, tags):
    # format top 10 as string for Pass 2 prompt
```

## Pass 2 Prompt — Key Rules

- Target ~5,800-6,500 prose words for Tier 1
- Return HTML sections ONLY — no markdown, no fences, no explanations
- Every section tag must have exact ID shown in prompt
- Leave PLACEHOLDERS for dynamic content: TRACK_PLACEHOLDER, GENRE_PLACEHOLDER, PLUGIN_PLACEHOLDER, DAW_PLACEHOLDER, COMPARISON_PLACEHOLDER
- Pass 2 picks 1-2 quotes from quotes_context and formats as blockquote.producer-quote with cite
- NEVER fabricate quotes — only use quotes from quotes_context
- Track list is LOCKED — cannot swap, invent, or reorder tracks
- Never output </body></html>

## build_html_t1() — Required Outputs

All sections listed in HANDOFF-BIBLE Section 47 table.
Signal chain SVG: viewBox 0 0 1440 160, 8 boxes, full labels, mobile stack.
Email gate: openGateFor('full'|'quickref'|'genre'), unified modal.
Tools section: always present. Injects GR calculator if tool_type == 'calculator'.
Comparison callouts: built from p1.comparison_terms (up to 2).
History cards: 3-4 sub-sections in left-border cards (built by Pass 2 but CSS class added in post-processing).
Sidebar: TOC (20 links) + producer spotlight + share (mpw-share-bar) + newsletter.

Share bars in generated entries: must use .mpw-share-bar class with buttons in order Copy Link → Share on X → Reddit.

## CONFIRMED_LIVE_SLUGS

```python
CONFIRMED_LIVE_SLUGS = {
    'compression', 'eq', 'limiting', 'saturation', 'distortion', 'reverb', 'delay',
    'parallel-compression', 'multiband-compression', 'noise-gate', 'gain-staging',
    'headroom', 'stereo-imaging', 'mid-side-processing', 'bus-compression', 'mix-bus',
    'send-return', 'automation', 'mastering', 'lufs', 'dynamic-range',
    'true-peak-limiting', 'loudness-normalization', 'subtractive-synthesis',
    'fm-synthesis', 'wavetable-synthesis', 'additive-synthesis', 'lfo', 'envelope',
    'oscillator', 'adsr', 'vocoder', 'high-pass-filter', 'low-pass-filter',
    'parametric-eq', 'shelving-eq', 'resonance', 'harmonic-distortion', 'chorus',
    'flanger', 'phaser', 'tremolo', 'vibrato', 'plate-reverb', 'room-reverb',
    'convolution-reverb', 'clip-gain', 'air-frequency-eq', 'air'
}
# EXCLUDED (confirmed 404): sidechain-compression, transient-shaping
```

## Validation Suite — v5.1 (75+ checks)

See HANDOFF-BIBLE Section 47 for full check list.
Critical new checks that must pass:
- mpw-slim-bar, bible-bar, bb-cats present
- no identity bar, no Sections label, no audio toggle HTML ('Coming Soon' not in content)
- no youtube.com, no spotify.com
- signal chain viewBox 1440 160
- signal-chain-mobile present
- openGateFor, downloadQuickRef, downloadGenreTable present
- setTocActive (sidebar TOC tracking)
- calcGR (calculator JS)
- comparison-callouts class
- Also in The Bible (not Further Reading)
- word count floor/ceiling per tier

## Bible Entry Economics

Tier 1: ~50,000 tokens = ~$0.25/entry
Tier 2: ~32,000 tokens = ~$0.16/entry
Tier 3: ~15,000 tokens = ~$0.075/entry
For 1,500 entries (300 T1 + 700 T2 + 500 T3): ~$300 total

---

# mpw_bible_cat_pages.py

Generates 8 Bible category pages at /bible/categories/{slug}/index.html.
Run after Bible writer --test confirmed.

```powershell
python mpw_bible_cat_pages.py --run
```

Each page reads live bible-index.json from GitHub, groups entries by category, client-side search/filter, category siblings strip, entry card grid.

Future: add tools category page (/bible/categories/tools/) after /tools/ hub exists.

---

# mpw_dead_slug_audit.py

Run after every batch commit. Finds dead related-article links across all articles.

```powershell
python mpw_dead_slug_audit.py
```

Automatically called by mpw_commit_articles.py after every successful commit.

---

# commit_handoff.py

Commits all 6 handoff modules + MPW-CATALOG.md to GitHub in one Trees API commit.

```powershell
python commit_handoff.py
```

Run at end of every session after all handoff files are updated.

---

# commit_handoff_s34.py (Session 34)

Updated version of commit_handoff.py for Session 34. Reads MPW-HANDOFF-CORE-S34.md from mpw-scripts\, fetches other 5 modules from GitHub, commits all 6 in one Trees API commit.

```powershell
python commit_handoff_s34.py
```

---

# setenv.ps1

Sets environment variables for the PowerShell session. Must run at start of every session.

```powershell
. .\setenv.ps1
```

Sets: $env:GITHUB_TOKEN and $env:ANTHROPIC_API_KEY
Keys clear on window close — must re-run after reopening PowerShell.

---

# Session 34 Patch Scripts (in mpw-scripts\ after download)

These scripts were written during Session 34 to diagnose and fix compression.html. Keep them for reference — they document the debugging process.

| Script | Purpose |
|---|---|
| check_wrap.py | Found bible-entry-wrap tag in body (first attempt — found CSS not HTML) |
| check_wrap2.py | Found all occurrences of bible-entry-wrap string — revealed CSS positions |
| check_wrap3.py | Printed exact wrap div tag from body section |
| check_body.py | Found main tag and aside element ancestor context |
| check_main.py | Confirmed main tag is `<main id="main-content">` with no container class |
| check_children.py | **KEY DIAGNOSTIC** — walked DOM tree, found only 1 direct child of bible-entry-wrap (should be 2) |
| find_unclosed.py | Counted div opens vs closes in entry-main segment — found balance of 2 (should be 1) |
| find_unclosed2.py | **ROOT CAUSE FOUND** — iterated with stack, identified gain-calculator div at position 18781 as unclosed |
| fix_calculator_div.py | **ROOT FIX** — added </div><!-- /gain-calculator --> before Signal Chain comment — SHA da97338e |
| debug_aside.py | Added red border to aside to confirm it renders — confirmed sidebar appeared after fix |
| remove_debug.py | Removed red border — SHA de721781 |
| fix_combined.py | Combined: aside display fix + share bars rebuilt Copy Link → X → Reddit order |
| fix_all_final.py | Rebuilt ALL mpw-share-bar divs in one pass from section context |
| fix_footer_only.py | Footer: removed Copy Link, X and Reddit only, centered |
| fix_footer_v2.py | Footer: inline-flex container attempt — still stretched |
| fix_footer_v3.py | Footer: fixed 120px width on both — X still appeared wider due to text length |
| fix_footer_v4.py | Footer: shortened X label to just "X", auto padding — buttons sized by content |
| fix_footer_v5.py | Footer: added .footer-share-btn class (flex:0 0 auto !important) — PENDING VISUAL CONFIRM |
| check_footer.py | Printed footer HTML from live file |
| audit_share.py | Audited all share bars in file — found wrong order in bars 6,7,8 |
| get_share_css.py | Printed exact share CSS from live style block |

## Div Balance Check Pattern (reusable)

```python
import re

def check_entry_main_balance(html):
    body_start = html.find('<body')
    body = html[body_start:]
    em_open = body.find('<div class="entry-main">')
    em_close = body.find('</div><!-- /entry-main -->')
    segment = body[em_open:em_close]
    opens = len(re.findall(r'<div[^>]*>', segment))
    closes = len(re.findall(r'</div>', segment))
    balance = opens - closes
    # balance should be 1 — entry-main itself
    return balance, opens, closes

def find_unclosed_divs(html):
    body_start = html.find('<body')
    body = html[body_start:]
    em_open = body.find('<div class="entry-main">')
    em_close = body.find('</div><!-- /entry-main -->')
    segment = body[em_open:em_close]
    stack = []
    for m in re.finditer(r'<(/?)div[^>]*>', segment):
        if m.group(1) == '/':
            if stack: stack.pop()
        else:
            stack.append((m.start(), m.group()[:80]))
    return stack  # each item = (position, opening_tag) of unclosed div
```

---

# Bible Batch Files

Location: C:\Users\swarn\OneDrive\Desktop\mpw-scripts\

- bible-upgrade-tier1.txt — 50 Tier 1 rewrites — READY after writer v5.1 confirmed
  Format: slug:Term:Category:1 (4 parts, tier=1)
  Example line: compression:Compression:Signal Processing:1
- bible-index.json — 202 entries — in repo root

Run Tier 1 batch:
```powershell
. .\setenv.ps1
python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-16
```

---

# mpw_fix_meta.py

Fix 5 articles missing og:image. Rate limited Session 27 — retry when ready.

```powershell
python mpw_fix_meta.py
```

---

# mpw_fix_sitewide_r7.py

NEVER run without --test on 3 articles first.
NEVER run after homepage updated to newer nav without updating r7 first.
Full run touches 614 files.

```powershell
python mpw_fix_sitewide_r7.py --test
python mpw_fix_sitewide_r7.py --run
```

---

# mpw_audit.py

Run before any article rewrite. Output is CSV showing what needs fixing vs full rewrite.

```powershell
python mpw_audit.py --dry-run
```

NEVER run article quality audit blind. NEVER rewrite without checking audit output first.

---

# GitHub API Notes

- api.github.com is BLOCKED from Claude's environment
- All GitHub operations must run from Steve's PowerShell
- Never use GitHub web editor for CSS or JS — silent corruption
- Multi-file commits MUST use Trees API (gh_trees_commit function)
- Single file commit: individual PUT acceptable
- Rate limit: sequential blob creation with exponential backoff on 403s — never parallel
- Max threads for Contents API: 10 (15-20 triggers secondary rate limit)
- NEVER use Set-Content in PowerShell for Python scripts with CSS values — use create_file tool
