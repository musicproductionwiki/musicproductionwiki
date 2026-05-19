# MPW-HANDOFF-SCRIPTS.md
*Updated: May 18, 2026 (SESSION 39)*

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

# mpw_bible_writer.py — v5.1 — SESSION 39 FINAL — READY FOR BATCH

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_writer.py`

**CRITICAL: The v5.1 writer is NOT in the GitHub repo. The repo contains an old v4.0 version. ALWAYS use the local mpw-scripts\ copy. NEVER restore from GitHub.**

**STATUS: 16 Tier 1 entries committed with correct tools. 33 remaining — READY TO RUN.**

**CONFIRMED STATE of delivered writer (Session 39):**
- Syntax: CLEAN
- Imports build_tools_section_v3 from mpw_tools_v3 ✅
- TOOL_OVERRIDES: DEFINED (all 12 tools, 49 slugs)
- build_html_t1, PASS2_SYSTEM_T1, build_tools_section_v3: PRESENT
- --workers flag: PRESENT (ThreadPoolExecutor, default 4, max 8)
- SC = '</' + 'script>': DEFINED
- _delay function: COMPLETE (html= and return lines present)
- Tools nav pill: AFTER Quick Ref (position 5)
- Tools sidebar TOC: AFTER Quick Ref (position 5)
- Validation: 80/80
- Tool init functions: direct calls only — NO setTimeout anywhere

## Run Commands

```powershell
. .\setenv.ps1
python mpw_bible_writer.py --validate
python mpw_bible_writer.py --test --slug delay --term "Delay" --category "Time-Based" --tier 1
python mpw_bible_writer.py --batch-file bible-tier1-remaining34.txt --start-date 2026-05-19 --workers 8
```

## Architecture

**Three-tier routing:**
```
slug:Term:Category:Tier  (4 parts, colon-separated)
Tier 1 → build_html_t1()  — 7,000–8,000 words — full gold standard template
Tier 2 → build_html_t2()  — 3,800–5,000 words — standard template
Tier 3 → build_html_t3()  — 1,500–2,500 words — reference template
```

**Pass Architecture:**
- Pass 1 (20,000 tokens) — Structured JSON data
- Pass 1.5 (no API call) — quotes.json filter by tag
- Pass 2 (22,000 tokens Tier 1 / 14,000 Tier 2 / 8,000 Tier 3) — Prose HTML

**Key constants (Session 39 final):**
- Model: claude-sonnet-4-6 ✅
- PASS1_TOKENS: 20000
- PASS2_TOKENS_T1: 22000
- PASS2_TOKENS_T2: 14000
- PASS2_TOKENS_T3: 8000
- API timeout: 600 seconds ✅
- WORD_FLOOR_T1: 6800 / WORD_CEIL_T1: 7800
- WORD_FLOOR_T2: 3800 / WORD_CEIL_T2: 5000
- WORD_FLOOR_T3: 1500 / WORD_CEIL_T3: 2500

## TOOL_OVERRIDES Map (Session 39 — via mpw_tools_v3.py)

```python
TOOL_OVERRIDES = {
    'compression':           'gr',
    'saturation':            'gr',
    'distortion':            'gr',
    'parallel-compression':  'gr',
    'multiband-compression': 'gr',
    'noise-gate':            'gr',
    'bus-compression':       'gr',
    'dynamic-range':         'gr',
    'delay':                 'delay',
    'plate-reverb':          'delay',
    'automation':            'delay',
    'limiting':              'lufs',
    'lufs':                  'lufs',
    'mastering':             'lufs',
    'loudness-normalization':'lufs',
    'true-peak-limiting':    'lufs',
    'eq':                    'freq',
    'parametric-eq':         'freq',
    'high-pass-filter':      'freq',
    'low-pass-filter':       'freq',
    'shelving-eq':           'freq',
    'air-frequency-eq':      'freq',
    'resonance':             'freq',
    'harmonic-distortion':   'freq',
    'air':                   'freq',
    'reverb':                'rt60',
    'convolution-reverb':    'rt60',
    'room-reverb':           'rt60',
    'oscillator':            'note',
    'fm-synthesis':          'note',
    'wavetable-synthesis':   'note',
    'additive-synthesis':    'note',
    'vocoder':               'note',
    'subtractive-synthesis': 'note',
    'adsr':                  'adsr',
    'envelope':              'adsr',
    'gain-staging':          'gs',
    'send-return':           'gs',
    'clip-gain':             'gs',
    'headroom':              'hc',
    'mix-bus':               'hc',
    'stereo-imaging':        'sw',
    'mid-side-processing':   'sw',
    'lfo':                   'lfo',
    'chorus':                'lfo',
    'flanger':               'lfo',
    'phaser':                'lfo',
    'tremolo':               'lfo',
    'vibrato':               'lfo',
}
```

**IMPORTANT: tool_type from Pass 1 is unreliable. TOOL_OVERRIDES is the authoritative routing map.**
**IMPORTANT: writer calls build_tools_section_v3(slug, term) from mpw_tools_v3.py — NOT the old build_tools_section.**

## SC — Safe Script Closing Tag

```python
SC = '</' + 'script>'
```

This constant is defined before all tool functions. NEVER write `</script>` as a literal string inside Python string literals — it closes the browser's script parser early and breaks all JS on the page. Always use SC for the closing tag in tool HTML strings.

## _delay function — Session 39 Status

The _delay function is present and working. Delay Time Calculator renders correctly on delay.html and plate-reverb.html — confirmed visually by Steve in Session 39.

## Session 39 Changes to mpw_bible_writer.py

- patch_writer_v3.py patched writer to import build_tools_section_v3 from mpw_tools_v3
- build_tools_section_v3 replaces old build_tools_section
- 80/80 validation confirmed after patch

## Session 37 Changes to mpw_bible_writer.py

### System Prompt (PASS2_SYSTEM_T1) — Complete Rewrite

1. **Identity reframe** — "senior editor of The Producer's Bible" — most comprehensive treatment on the internet
2. **NON-NEGOTIABLE LAWS (LAW 1–7)** — structural mandates moved from user prompt to system prompt as identity constraints
3. **Failure description** — 7 explicit failure signatures Pass 2 self-checks before outputting
4. **Voice — 3 BAD/GOOD pairs** — parameters (attack ms), history (1176 all-buttons), mistakes (bypass test)
5. **Word count** — prose 4,800–5,500w, explains builder adds 1,500–2,500w to reach 7,000–8,000w total
6. **Section-level hard limits** — SUBSTANTIVE vs STRUCTURAL classification with specific word ranges

### User Prompt (build_pass2_prompt_t1) — Key Additions

- CONFIRMED_LIVE_SLUGS injected directly into prompt body
- Internal link format specified: `color:#f5a623;text-decoration:none;border-bottom:1px solid rgba(245,166,35,0.3)`
- History template: 4 cards × 1 paragraph × 120–150w (500–600w total)
- Verdict template: MPW editorial opinion mandate with example voice
- Final Checks: 8 checklist items including internal links count

### SEO Improvements

- Meta description: search-intent driven pattern, 155-char enforced, uses types from Pass 1
- Keywords: intent-phrase front-loading (how to use, tutorial, explained)
- HowTo schema: 5 universal workflow steps (was 2 DAW-specific)
- Article schema: `timeRequired`, `inLanguage: en-US`, ISO 8601 datetime

### Builder Changes

- **Tools position**: injected after `id="quick-reference"` via string replacement — confirmed by Steve as correct
- **Tools nav pill**: position 5 in entry nav (after Quick Ref) — confirmed by Steve
- **Tools sidebar TOC**: position 5 (after Quick Ref) — confirmed by Steve
- **Tools share bars**: Copy Link + Share on X + Reddit added to calculator section
- **Producer spotlight**: parses `<cite>` tags from rendered HTML — called after html is fully built
- **Verdict in sidebar TOC**: `('verdict', 'Verdict')` added between Types and Plugins
- **FAQ filter**: `build_faq_html()` skips items with empty `a` field
- **History template**: 4 cards × 1 paragraph × 120–150w

### Bug Fixes (Session 38)

- SyntaxError in _freq, _gs, _hr, _chord: bare unescaped single quotes at innerHTML= inside single-quoted Python strings — fixed by escaping 56 single quotes across 4 lines
- TOOL_OVERRIDES not defined: referenced but never assigned — fixed by inserting full dict after SC = line
- _delay missing html= and return lines: truncated function — fixed by inserting html and return after js= block
- Validation suite: gc-input and calcGR checks removed — replaced with tool-agnostic check matching any tool's DOM elements

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

## Validation Suite — v5.1 (80 checks)

See HANDOFF-BIBLE Section 47 for full updated check list.

Critical checks updated Session 38:
- gc-input check REMOVED — was GR calculator specific
- calcGR check REMOVED — was GR calculator specific
- Replaced with: 'tool present': any(x in c for x in ['gc-input','dt-bpm','lc-cur','rt-vol','freq-bands','nf-note','adsr-c','gs-s','hr-pk','sw-cv','lfo-b','ck-r'])

**VALIDATION SCORE ≠ CONTENT QUALITY. 80/80 structural checks do not guarantee content matches gold standard. Always visual QA.**

## Bible Entry Economics

Tier 1: ~50,000 tokens = ~$0.25/entry
Tier 2: ~32,000 tokens = ~$0.16/entry
Tier 3: ~15,000 tokens = ~$0.075/entry
For 1,500 entries (300 T1 + 700 T2 + 500 T3): ~$300 total

---

# mpw_tools_v3.py — SESSION 39 — NEW — CONFIRMED WORKING

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_tools_v3.py`

**PURPOSE:** Fully self-contained Python file with all 12 interactive tools and 49 slug mappings. No external imports. Public API: `build_tools_section_v3(slug, term)` returns complete HTML string for injection into Bible entries.

**CRITICAL RULES:**
- NEVER import build_preview.py or any external script — mpw_tools_v3.py must be self-contained
- NEVER use setTimeout for any init function call — call all init functions directly
- Tool init functions called at end of each tool's `<script>` block — no deferred execution

**Tool CSS class architecture:**
```
.t3          — outer container (black bg, amber border 1.5px, 10px radius)
.t3 .tb      — tool body (padding 16px 20px 18px)
.t3 .tr      — input row grid
.t3 .c2/c3/c4 — column counts
.t3 .rb      — result box (dark bg, amber number)
.t3 .rn      — result number (26px, weight 800, amber)
.t3 .co      — contextual comment (left border amber)
.t3 .sh      — section header (amber, uppercase)
.t3 .tc      — table/preset card (clickable, hover amber)
.t3 .btn     — amber button
```

**Brand header on every tool:**
- Green teal logomark (same SVG as site nav)
- MusicProductionWiki.com in white
- ◆ The Producer's Bible in amber
- "Interactive Tool" badge in amber
- Tool name right-aligned
- Dark amber header background (#0d0800)

**Footer on every tool:**
- ◆ The Producer's Bible — MusicProductionWiki.com
- Copy Link button
- X Share button
- Reddit button

```powershell
# Test import:
python -c "from mpw_tools_v3 import build_tools_section_v3; print(build_tools_section_v3('reverb','Reverb')[:200])"
```

---

# patch_writer_v3.py — SESSION 39

Patched mpw_bible_writer.py to import build_tools_section_v3 from mpw_tools_v3 instead of using old inline build_tools_section. Validated 80/80 after patch.

```powershell
python patch_writer_v3.py
python mpw_bible_writer.py --validate
```

---

# patch_live_tools_v6.py — SESSION 39 — PENDING RUN

**PURPOSE:** Surgical removal of duplicate bare `.t3` tool blocks that sit after `</section>` of the tools section on the 15 patched entries. The correct section-wrapped tool stays. The dead bare block (showing dashes, no working JS) is removed.

**HOW IT WORKS:**
- Fetches each of the 15 entries from GitHub
- Detects if a bare `.t3` block exists after the tools `</section>` close
- Removes only the bare block — leaves `<section id="tools">` untouched
- Reports `.t3` div count and tools section count before and after
- Skips entries where no duplicate detected
- Single Trees API commit for all changed files

```powershell
. .\setenv.ps1
python patch_live_tools_v6.py
```

**Run this FIRST at the start of next session before anything else.**

---

# patch_live_tools_v1 through v5 — ALL SUPERSEDED — DO NOT USE

- patch_live_tools.py — SUPERSEDED — imported old green-wrapper build_tools_section
- patch_live_tools_fix.py — SUPERSEDED — wrong insertion position
- patch_live_tools_v2.py — SUPERSEDED — searched for missing section wrapper
- patch_live_tools_v3.py — SUPERSEDED — inserted before helpful block
- patch_live_tools_v4.py — SUPERSEDED — still had setTimeout in tool scripts
- patch_live_tools_v5.py — SUPERSEDED — missed bare .t3 duplicate

---

# add_workers.py — SESSION 38

Patches mpw_bible_writer.py to add --workers flag via concurrent.futures.ThreadPoolExecutor.

```powershell
python add_workers.py
```

Output: [OK] Added concurrent.futures import / [OK] Added --workers argparse argument / [OK] Replaced sequential loop with ThreadPoolExecutor

**NOTE: Workers are now baked into the delivered writer. Only run add_workers.py if starting from the project knowledge base file (which does not have workers).**

---

# fix_writer.py — SESSION 38

Fixes two bugs in a broken mpw_bible_writer.py:
- BUG 1: SyntaxError in _freq/_gs/_hr/_chord js= strings (bare unescaped single quotes)
- BUG 2: TOOL_OVERRIDES not defined

```powershell
python fix_writer.py
```

Reads and writes `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_writer.py` in-place.
Creates backup at mpw_bible_writer.py.pre_fix.bak before modifying.

---

# mpw_handoff_runner.py — NEW SESSION 37

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_handoff_runner.py`

**PURPOSE:** Automates end-of-session handoff commits. Replaces manual 30-min handoff process.

```powershell
# At end of each session:
python session_patch_sNN.py --dry-run   # verify first
python session_patch_sNN.py             # commit
```

**Architecture:**
- Fetches live handoff files from GitHub (current SHA for each)
- Inserts session updates at append zone tags (never floating string search)
- Scrubs secrets: ghp_ and sk-ant- patterns removed automatically
- Validates sentinels + line count floors before committing
- Single Trees API commit (one Netlify deploy)
- Saves SHA state to handoff_state.json (local only, never committed)

**Zone tags** (added to all 6 handoff files by add_zones.py, committed SHA: 6afa90d5):
```
<!-- SESSION_APPEND_ZONE -->  (in .md files: # SESSION_APPEND_ZONE)
```

**Session patch template (session_patch_sNN.py):**
```python
patch = {
    'MPW-HANDOFF-CORE.md': "## Session NN Update\n...",
    'MPW-HANDOFF-BIBLE.md': "## Session NN Bible Update\n...",
    # ... other files as needed
}
run_patch(patch, dry_run=False)
```

Session 37 handoff committed — SHA: 7c321e33
Session 38 handoff: DELIVERED AS FILES — committed via GitHub API
Session 39 handoff: DELIVERED AS FILES — commit via GitHub API (see upload command in this handoff)

---

# add_zones.py — ONE-TIME (already run)

Added 11 append zone tags across 6 handoff files.
All 10 anchors verified against actual live files before run.
Committed SHA: 6afa90d5.
Do NOT run again.

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

Legacy — superseded by mpw_handoff_runner.py + session_patch_sNN.py workflow.
Still functional as fallback if handoff runner fails.

```powershell
python commit_handoff.py
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

# gen_sitemap.py (Session 35)

Generates sitemap.xml from live GitHub article list.

```powershell
python gen_sitemap.py
```

Output: 739 URLs (526 articles + 210 Bible entries + 3 static pages). Commits to repo root.
Future: add `<lastmod>{today_str}</lastmod>` for Bible entries — improves crawl budget.

---

# fix_gsc_issues.py (Session 36 — one-time use)

Fixed 2 Google Search Console issues:
1. 301 redirect: /ssl-2-plus-review/ → /articles/ssl-2-plus-review.html (netlify.toml)
2. Canonical fix: best-studio-monitors-under-300.html (self-closing slash removed)
Committed via Trees API — SHA: d6f787db46f8dc4bbbe5b7d4f1fd2ba0b45e0505

---

# Bible Batch Files

Location: C:\Users\swarn\OneDrive\Desktop\mpw-scripts\

- bible-upgrade-tier1.txt — 50 Tier 1 rewrites — 16 DONE, 33 REMAINING
  Format: compression:Compression:Signal Processing:1 (4 parts, tier=1)
- bible-index.json — 210 entries (v3.0/v4.0) — in repo root — NOT updated for v5.1 entries yet
- bible-tier1-remaining34.txt — CREATE before running remaining batch (see CORE for command)

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
