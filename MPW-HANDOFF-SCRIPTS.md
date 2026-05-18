# MPW-HANDOFF-SCRIPTS.md
*Updated: May 18, 2026 (SESSION 36)*

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

# mpw_bible_writer.py — v5.1 — SESSION 36 UPDATE COMPLETE

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_writer.py`

**STATUS: Structural update complete (81/81 checks). Content quality ~55% of gold standard. Pass 2 prompt rewrite required Session 37 before any batch.**

## Run Commands

```powershell
. .\setenv.ps1
python mpw_bible_writer.py --validate
python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing" --tier 1
python mpw_bible_writer.py --validate --html-file compression.html
python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-16
```

## Architecture

**Three-tier routing:**
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

**Key constants (Session 36 final):**
- Model: claude-sonnet-4-6 ✅
- PASS1_TOKENS: 20000
- PASS2_TOKENS_T1: 22000
- PASS2_TOKENS_T2: 14000
- PASS2_TOKENS_T3: 8000
- API timeout: 600 seconds ✅
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

**IMPORTANT: tool_type from Pass 1 is unreliable — Compression returned null. Use hardcoded TOOL_OVERRIDES map in build_tools_section().**

## Pass 1.5 — Quotes Filter

```python
def load_quotes(path='quotes.json'):
    # load from same dir as script
def filter_quotes(quotes, tags, max_results=10):
    # score by tag overlap, return top max_results
def build_quotes_context(quotes, tags):
    # format top 10 as string for Pass 2 prompt
```

## Pass 2 Prompt — Required Fixes (Session 37)

The current pass 2 prompt in build_pass2_prompt_t1() is insufficient. Required fixes:

1. **Mandate h2 tags** — Every section must open with `<h2>ExactTitle</h2>`. Show exact h2 text for each section.
2. **Mandate 2 producer quotes** — "Tier 1 entries MUST include exactly 2 producer quotes from quotes_context. Place one in the definition section and one in the history or how-to-use section."
3. **Fix FAQ_PLACEHOLDER placement** — Show exact required line: `FAQ_PLACEHOLDER` alone on its own line inside the faq section.
4. **Fix PLUGIN_PLACEHOLDER placement** — Show exact required position after hardware-plugin table.
5. **Strengthen system prompt** — "Every sentence must contain a concrete, actionable, specific claim. No hedging. No generic explainer prose. You are writing the definitive professional reference that producers bookmark and return to."
6. **Mandate entry-section class + exact IDs** — "Every section element must have class=\"entry-section\" and the exact id shown. Never use a different id."

## Pass 2 Current Placeholder List (build_html_t1 replaces these)

```
THE_NUMBER_PLACEHOLDER     → build_the_number_html()
SIGNAL_CHAIN_PLACEHOLDER   → build_signal_chain_svg()
GENRE_PLACEHOLDER          → build_genre_table_html()
PLUGIN_PLACEHOLDER         → build_plugin_recs_html()
DAW_PLACEHOLDER            → build_daw_tabs_html()
COMPARISON_PLACEHOLDER     → build_comparison_callouts_html()
TRACK_PLACEHOLDER          → build_track_list_html()
FAQ_PLACEHOLDER            → build_faq_html()
FLAGS_PLACEHOLDER          → build_flags_html()
BEFORE_AFTER_PLACEHOLDER   → build_before_after_html()
QUICKREF_SHARE_PLACEHOLDER → mpw-share-bar for quick reference
```

## build_html_t1() — Required Outputs

All sections listed in HANDOFF-BIBLE Section 47 table.
Signal chain SVG: viewBox 0 0 1440 160, 8 boxes, full labels, mobile stack.
Email gate: openGateFor('full'|'quickref'|'genre'), unified modal.
Tools section: always present. Injects GR calculator if tool_type == 'calculator' OR slug is in TOOL_OVERRIDES.
Comparison callouts: built from p1.comparison_terms (up to 2).
History cards: 3-4 sub-sections in left-border cards (built by Pass 2).
Sidebar: TOC (20 links) + producer spotlight + share widget (mpw-share-bar vertical) + newsletter.
bible-entry-wrap: inline grid style MUST be present as inline style on the element.
aside: inline style MUST contain min-width:280px;width:280px;position:sticky;top:148px;align-self:start;overflow-y:auto;height:calc(100vh - 168px) — NO display property.

## Session 36 Bug Fixes Applied

1. **MODEL string** — was `claude-sonnet-4-20250514` → now `claude-sonnet-4-6`
2. **API timeout** — was 300s → now 600s
3. **css_block NameError** — build_head() referenced `{css_block}` in f-string without defining it. Fixed: `css_block = build_css()` added before return statement.
4. **Stale validation checks** — 5 checks updated:
   - scroll-margin mobile: 136px → 110px
   - no audio toggle: `'Coming Soon' not in c` → `'audio-toggle' not in c`
   - Download Cheat Sheet: → mpw-share-bar present check
   - Copy Settings: → calc-share-bar present check
   - entry-nav 126px: → entry-nav 84px mobile

<!-- SCRIPT_UPDATES_APPEND_HERE -->
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

## Validation Suite — v5.1 (81 checks)

See HANDOFF-BIBLE Section 47 for full updated check list (updated Session 36).

Critical updated checks:
- scroll-margin mobile now checks 110px (not 136px)
- no audio toggle now checks audio-toggle class (not 'Coming Soon' string)
- mpw-share-bar present replaces Download Cheat Sheet check
- calc-share-bar present replaces Copy Settings check
- entry-nav 84px mobile replaces 126px check

**VALIDATION SCORE ≠ CONTENT QUALITY. 81/81 structural checks do not guarantee content matches gold standard. Always visual QA.**

## Bible Entry Economics

Tier 1: ~50,000 tokens = ~$0.25/entry
Tier 2: ~32,000 tokens = ~$0.16/entry
Tier 3: ~15,000 tokens = ~$0.075/entry
For 1,500 entries (300 T1 + 700 T2 + 500 T3): ~$300 total

---

# mpw_bible_cat_pages.py

Generates 8 Bible category pages at /bible/categories/{slug}/index.html.
Run after Bible writer visual QA confirmed ≥90%.

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

# setenv.ps1

Sets environment variables for the PowerShell session. Must run at start of every session.

```powershell
. .\setenv.ps1
```

Sets: $env:GITHUB_TOKEN and $env:ANTHROPIC_API_KEY
Keys clear on window close — must re-run after reopening PowerShell.

---

# gen_sitemap.py (Session 35)

Generates sitemap.xml from live GitHub article list.

```powershell
python gen_sitemap.py
```

Output: 739 URLs (526 articles + 210 Bible entries + 3 static pages). Commits to repo root.

---

# fix_gsc_issues.py (Session 36 — one-time use)

Fixed 2 Google Search Console issues:
1. 301 redirect: /ssl-2-plus-review/ → /articles/ssl-2-plus-review.html (netlify.toml)
2. Canonical fix: best-studio-monitors-under-300.html (self-closing slash removed)
Committed via Trees API — SHA: d6f787db46f8dc4bbbe5b7d4f1fd2ba0b45e0505

---

# fix_share_bars_s36*.py (Session 36 — series)

Series of scripts that fixed share bars on compression.html:
- fix_share_bars_s36.py — removed outer wrapper div from calculator bar
- fix_share_bars_s36b.py — added calc-share-bar class to both bars
- fix_share_bars_s36c.py — injected CSS: calc-share-bar auto-width
- fix_share_bars_s36d.py — CSS: solid amber Copy Link
- fix_share_bars_s36e.py — CSS: 3-col equal grid on mobile
All committed. Final state: all share bars uniform on compression.html.

---

# Bible Batch Files

Location: C:\Users\swarn\OneDrive\Desktop\mpw-scripts\

- bible-upgrade-tier1.txt — 50 Tier 1 rewrites — READY after writer visual QA ≥90%
  Format: slug:Term:Category:1 (4 parts, tier=1)
  Example line: compression:Compression:Signal Processing:1
- bible-index.json — 210 entries — in repo root

Run Tier 1 batch (ONLY after Pass 2 prompt rewrite + visual QA confirmed):
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
