# MPW-HANDOFF-SCRIPTS.md
*Last merged: May 26, 2026 (Session 71 — merged S55 master + S65/S65b/S66/S67/S68 appends)*
*Previous update: May 22, 2026 (SESSION 55)*

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

---

# SESSION 41 UPDATE — SCRIPT STATE

## Patch Scripts Status After Session 41

| Script | Status | Notes |
|---|---|---|
| patch_mobile_fix.py | ✅ COMPLETED | SHA: a0553356 — 70 entries — wrap + aside + JS |
| patch_nav_mobile.py | ❌ FAILED — DO NOT USE | justify-content:flex-start has no effect |
| patch_nav_and_btt.py | ⏳ NEEDED | Read compression.html first — copy exact code |
| patch_writer_inline_style.py | ✅ COMPLETED | Removed inline style from local writer |
| patch_writer_spotlight.py | ❓ RUN STATUS UNKNOWN | Verify with --validate |
| patch_writer_tools_position.py | ❓ RUN STATUS UNKNOWN | Verify with --test chorus --no-commit |
| patch_live_tools_v6.py | ✅ COMPLETED | Confirmed by Steve — Session 40 P0 |
| mpw_diagnose.py | ✅ NEW | Delivered and run Session 41 — 223 entries confirmed |

## Entry Nav — BROKEN ON ALL 70 v5.1 ENTRIES ❌

Confirmed by Steve on mobile — reported multiple times — screenshots provided.
Symptom: Pills freeze at Quick Ref. Scrolling content does NOT advance the nav.
Tools, Signal Chain, History, etc. never highlight in the nav pill bar.
Affects ALL 70 v5.1 entries — original 16 AND the 54 Session 40 entries.
Root cause: margin:0 auto on .entry-nav-inner — pills center, cannot overflow, scroll never activates.
The h2 inside the tools section is irrelevant to this bug.
Fix: patch_nav_and_btt.py — append .entry-nav-inner{margin:0!important} before </head>.
READ compression.html before writing. Copy exact code. Never write from memory.

## patch_nav_and_btt.py — What It Must Do

1. Append `<style>.entry-nav-inner{margin:0!important}</style>` before `</head>`
2. Inject exact btt-btn button HTML before `</body>` — copy from compression.html
3. Inject exact btt scroll listener JS before `</body>` — copy from compression.html
4. Sentinel check — skip entries already patched
5. Single Trees API commit — all 70 v5.1 entries

BEFORE WRITING: fetch bible/compression.html from GitHub. Read it. Copy exact strings.

## mpw_bible_writer.py v5.2 — Build Next Session

Current local writer has bugs. Full v5.2 spec in HANDOFF-BIBLE.md.
Pre-build checklist:
1. Read compression.html in full
2. Read HANDOFF-BIBLE.md v5.2 spec completely
3. Make all 12 fixes in one pass
4. Run --validate → 80/80
5. Run --test chorus --no-commit
6. Steve visual QA
7. THEN regenerate 54 entries

---

# SESSION 46 — Fix Scripts

## fix_v3_permanent.py — NEW

Idempotent fix for mpw_tools_v3.py. Fixes:
1. "" leak after </script> in all 11 tool body strings
2. Converts LTIPS values from single-quoted to double-quoted JS strings

```powershell
python fix_v3_permanent.py
```
Safe to run even if already applied — idempotent. Run after any reinstall of mpw_tools_v3.py.

## fix_writer_permanent.py — NEW

Idempotent fix for mpw_bible_writer.py. Fixes:
1. Removes duplicate {tools_html} from final HTML assembly f-string

```powershell
python fix_writer_permanent.py
```
Safe to run even if already applied — idempotent. Run after any reinstall of mpw_bible_writer.py.

## verify_fixes.py — NEW

Confirms all 3 Session 46 fixes are correctly applied to both files.

```powershell
python verify_fixes.py
```

Run after any reinstall of either file. All checks must be green before running --test.

## ⚠️ STALE Scripts — Do NOT Run

| Script | Issue |
|---|---|
| install_bible_writer_v52_part1.ps1 | Writes UNFIXED writer — overwrites working version |
| install_bible_writer_v52_part2.ps1 | Same — DO NOT RUN |
| install_bible_writer_v52_part3.ps1 | Same — DO NOT RUN |

P0b next session: read fixed writer from disk, encode as new 3-part PS1 scripts.

## Run Order After Any Reinstall

```powershell
# If mpw_tools_v3.py reinstalled:
python fix_v3_permanent.py
python verify_fixes.py

# If mpw_bible_writer.py reinstalled:
python fix_writer_permanent.py
python verify_fixes.py

# Then test:
. .\setenv.ps1; python mpw_bible_writer.py --test --slug chorus --term "Chorus" --category "Time-Based" --tier 1 --no-commit
```

---

# SESSION 47 — Writer Install Scripts + New Fix Scripts

## mpw_bible_writer.py — v5.2 s47d — CURRENT STATE

**Size:** 214,478 bytes
**Syntax:** CLEAN
**Validation:** 90/90 when chorus.html generated fresh

**CRITICAL: The v5.2 s47d writer is NOT in the GitHub repo. The repo contains an old v4.0 version. ALWAYS use the local mpw-scripts\ copy. NEVER restore from GitHub.**

## Current Install Scripts

```powershell
Unblock-File .\install_writer_v52_s47d_part1.ps1
Unblock-File .\install_writer_v52_s47d_part2.ps1
Unblock-File .\install_writer_v52_s47d_part3.ps1
.\install_writer_v52_s47d_part1.ps1
.\install_writer_v52_s47d_part2.ps1
.\install_writer_v52_s47d_part3.ps1
python verify_fixes.py
```

**Always Unblock-File before running.**

## ⚠️ STALE Scripts — Updated List

| Script | Issue |
|---|---|
| install_bible_writer_v52_part1/2/3.ps1 | Writes UNFIXED writer — DO NOT RUN |
| install_writer_v52_s46_part1/2/3.ps1 | Session 46 — superseded by s47d |
| install_writer_v52_s47_part1/2/3.ps1 | PS1 syntax error — DO NOT RUN |
| install_writer_v52_s47b_part1/2/3.ps1 | Session 47b — missing fixes — DO NOT RUN |

**CURRENT:** install_writer_v52_s47d_part1/2/3.ps1

## fix_settimeout.py — NEW Session 47 (Other Context)

Removes setTimeout(lfoCalc, 0) from mpw_tools_v3.py LFO tool init. Restores direct lfoCalc() call.

```powershell
python fix_settimeout.py
```

**NOTE:** This fix is already baked into the s47d writer install scripts. Only needed if mpw_tools_v3.py is reinstalled from an old source.

## Run Order After Any Reinstall — Updated Session 47

```powershell
# If mpw_tools_v3.py reinstalled from old source:
python fix_v3_permanent.py
python fix_settimeout.py
python verify_fixes.py

# If mpw_bible_writer.py reinstalled (use s47d scripts instead):
python fix_writer_permanent.py
python verify_fixes.py

# Then test:
. .\setenv.ps1; python mpw_bible_writer.py --test --slug chorus --term "Chorus" --category "Time-Based" --tier 1 --no-commit
```

## Key Function Changes — v5.2 s47d

### filter_quotes(quotes, tags, max_results=10, spotlight_names=None)
Spotlight producer quotes always returned first (regardless of tag match), then remaining slots filled by tag overlap score. Guarantees Pass 2 always has quote text for spotlight producers.

### build_pass2_prompt_t1(..., quotes_filtered=None)
Injects ACTUAL QUOTE TEXT verbatim for each spotlight producer into the prompt body, including exact HTML markup. Pass 2 cannot fabricate or substitute.

### build_plugin_recs_html(plugin_recs)
Returns "MusicProductionWiki Recommends" amber intro block + Free/Mid/Pro card grid. Never says "MPW."

### build_session_breakdown_html(session_breakdown)
Strips "Step N —" prefix from Pass 1 step text before rendering. Number circles handle numbering.

### count_words_html(html)
Strips script, style, table, tool section (.t3), DAW tabs, signal chain diagram, and nav blocks before counting words. Returns prose-only word count for accurate read time.

## Pass Architecture — v5.2 Final

- Pass 1 (20,000 tokens) — Structured JSON — receives available_quote_authors list from quotes.json
- Pass 1.5 (no API call) — quotes.json filter by tag + spotlight producer priority
- Pass 2 (22,000 tokens T1 / 14,000 T2 / 8,000 T3) — Prose HTML

**Key constants (Session 47 final):**
- Model: claude-sonnet-4-6
- PASS1_TOKENS: 20000
- PASS2_TOKENS_T1: 22000
- PASS2_TOKENS_T2: 14000
- PASS2_TOKENS_T3: 8000
- API timeout: 600 seconds
- WORD_FLOOR_T1: 6800 / WORD_CEIL_T1: 7800
- Read time: 500 wpm (updated Session 47)

---

# SESSION 51 UPDATE — May 21, 2026

## No New Scripts Built in S51

Session 51 focused entirely on manually building reverb.html. No new Python scripts were written.

## Key Technical Lesson — JS String Apostrophe Safety

The same apostrophe bug that hit LTIPS in Session 46 (single-quoted JS strings with contractions) recurred in reverb.html's DT_N array. Now a NEVER rule. When building v5.3 writer, ALL JS string literals containing natural language text must use either escaped apostrophes or double quotes.

Affected patterns to check in v5.3 writer JS output:
- DT_N array (Decision Tree node text)
- ED_F object (Error Diagnostic fix text)
- Any inline JS string with English prose

## reverb.html Commit Command (Steve — run after mobile QA)

```powershell
. .\setenv.ps1

$filePath = "C:\Users\swarn\OneDrive\Desktop\mpw-scripts\reverb.html"
$content = [System.IO.File]::ReadAllBytes($filePath)
$base64 = [System.Convert]::ToBase64String($content)

# Get current SHA (if file exists in repo):
$sha_resp = Invoke-RestMethod `
    -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" `
    -Headers @{Authorization="token $env:GITHUB_TOKEN"} `
    -ErrorAction SilentlyContinue

$body = @{
    message = "feat: Reverb Bible entry S51 — 28 sections, RT60 calculator, radar chart, decision tree, mono check, recall sheet"
    content  = $base64
    branch   = "main"
}
if ($sha_resp.sha) { $body.sha = $sha_resp.sha }

Invoke-RestMethod `
    -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" `
    -Method PUT `
    -Headers @{Authorization="token $env:GITHUB_TOKEN"; "Content-Type"="application/json"} `
    -Body ($body | ConvertTo-Json -Depth 5)
```

After commit: verify live at musicproductionwiki.com/bible/reverb
Check: radar chart draws polygons, decision tree shows questions, nav pills highlight on scroll, works on real iPhone.

## Session 52 First Steps

```powershell
. .\setenv.ps1
python verify_fixes.py
python mpw_session_start.py
```

Then: open musicproductionwiki.com/bible/reverb on real device and report any remaining issues.

---

# SESSION 52 UPDATE — May 22, 2026

## mpw_bible_writer.py — Status Change

v5.2 writer (s47d) is SUPERSEDED. To be replaced by v5.3 in Session 53.
v5.3 will be back-engineered from reverb_v11.html. See MPW-HANDOFF-BIBLE.md for full spec.
Do NOT use v5.2 writer for new T1 entries — it does not contain S52 additions.

## reverb.html Commit Command (Single File PUT — No 200KB Limit)

```powershell
. .\setenv.ps1
$content = [System.IO.File]::ReadAllBytes("C:\Users\swarn\OneDrive\Desktop\mpw-scripts\reverb.html")
$base64 = [System.Convert]::ToBase64String($content)
$sha_resp = Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" -Headers @{Authorization="token $env:GITHUB_TOKEN"} -ErrorAction SilentlyContinue
$body = @{message="feat: reverb.html S52 — world-class gold standard — 10 additions — 23 sections";content=$base64;branch="main"}
if ($sha_resp.sha) { $body.sha = $sha_resp.sha }
Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" -Method PUT -Headers @{Authorization="token $env:GITHUB_TOKEN";"Content-Type"="application/json"} -Body ($body | ConvertTo-Json)
```

NOTE: reverb.html is 299.7KB — this is fine for single-file API PUT. The 200KB limit only applies to ZIP batches via Notepad → Save As.

## Generic Single Bible Entry Commit Template

```powershell
. .\setenv.ps1
$SLUG = "reverb"
$COMMIT_MSG = "feat: $SLUG Bible entry S52"
$LOCAL_PATH = "C:\Users\swarn\OneDrive\Desktop\mpw-scripts\$SLUG.html"
$GITHUB_PATH = "bible/$SLUG.html"

$content = [System.IO.File]::ReadAllBytes($LOCAL_PATH)
$base64 = [System.Convert]::ToBase64String($content)
$sha_resp = Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/$GITHUB_PATH" -Headers @{Authorization="token $env:GITHUB_TOKEN"} -ErrorAction SilentlyContinue
$body = @{message=$COMMIT_MSG;content=$base64;branch="main"}
if ($sha_resp.sha) { $body.sha = $sha_resp.sha }
Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/$GITHUB_PATH" -Method PUT -Headers @{Authorization="token $env:GITHUB_TOKEN";"Content-Type"="application/json"} -Body ($body | ConvertTo-Json)
```

## JS Triple-Check Script (Run Before Every Bible Entry Output)

```python
import re, subprocess, tempfile, os

def js_triple_check(html):
    errors = []
    scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
    for i, content in enumerate(scripts):
        apos = re.findall(r"(?<!\\)\b\w+'\w+\b", content)
        if apos:
            errors.append(f"Block {i} APOSTROPHE: {apos[:5]}")
        non_ascii = re.findall(r'[^\x00-\x7F]', content)
        if non_ascii:
            errors.append(f"Block {i} UNICODE: {[hex(ord(c)) for c in set(non_ascii)][:5]}")
        with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(content)
            tmpfile = f.name
        result = subprocess.run(['node', '--check', tmpfile], capture_output=True, text=True)
        os.unlink(tmpfile)
        if result.returncode != 0:
            errors.append(f"Block {i} SYNTAX: {result.stderr.strip()[:100]}")
    return errors
```

## Session 52 Diagnostic Commands

```powershell
# Standard session start:
. .\setenv.ps1
python mpw_session_start.py
python verify_fixes.py

# Commit reverb.html (copy command from above)

# After commit — verify live:
# Open musicproductionwiki.com/bible/reverb
# Check all 10 additions, nav highlighting, spectrograms, tools
# Test on real iPhone
```

---

# SESSION 53 UPDATE — May 22, 2026

## reverb.html — S53 Commit Command

reverb.html is now 324KB. Fine for single-file API PUT (no size limit). Steve saves from outputs download, renames to reverb.html, then either:

**Option A — Claude commits from bash (preferred):**
Steve uploads reverb.html to Claude session and says "commit reverb.html". Claude executes directly via GitHub API PUT.

**Option B — Steve commits via PowerShell:**
```powershell
. .\setenv.ps1
$content = [System.IO.File]::ReadAllBytes("C:\Users\swarn\OneDrive\Desktop\mpw-scripts\reverb.html")
$base64 = [System.Convert]::ToBase64String($content)
$sha_resp = Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" -Headers @{Authorization="token $env:GITHUB_TOKEN"} -ErrorAction SilentlyContinue
$body = @{message="feat: reverb.html S53 — content overhaul — 25 sections — affiliate-ready plugins — 324KB";content=$base64;branch="main"}
if ($sha_resp.sha) { $body.sha = $sha_resp.sha }
Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" -Method PUT -Headers @{Authorization="token $env:GITHUB_TOKEN";"Content-Type"="application/json"} -Body ($body | ConvertTo-Json)
```

## Session 53 — No New Python Scripts Built

Session 53 focused on reverb.html content overhaul and handoff updates. No new Python scripts were written.

v5.3 writer build is P1 for Session 54. It will be back-engineered from reverb_v11.html S53 version. The gold standard is now confirmed and content-complete.

## v5.3 Writer — Build Spec Summary (Full spec in HANDOFF-BIBLE.md)

1-pass template fill from reverb_v11.html S53. All structure frozen. Claude fills variables only.

Key requirements:
- Section order: 25 sections per S53 canonical order (beginner-trap at position 3)
- Sidebar: TOC + Newsletter + Share only — NO Producer Spotlight
- Plugins: editorial card layout (three-column auto-fill, Free/Mid/Pro cards with descriptions)
- JS triple-check mandatory before output
- node --check on all script blocks
- Model: claude-sonnet-4-6
- Target: 95/95 validation checks

## Session 54 First Steps

```powershell
. .\setenv.ps1
python mpw_session_start.py
python verify_fixes.py
```

Then: confirm reverb.html mobile QA complete → commit → begin v5.3 writer build.

## ⚠️ Stale Scripts — Updated List

| Script | Issue |
|---|---|
| install_bible_writer_v52_part1/2/3.ps1 | Writes UNFIXED writer — DO NOT RUN |
| install_writer_v52_s46_part1/2/3.ps1 | Session 46 — superseded by s47d |
| install_writer_v52_s47_part1/2/3.ps1 | PS1 syntax error — DO NOT RUN |
| install_writer_v52_s47b_part1/2/3.ps1 | Session 47b — missing fixes — DO NOT RUN |

**CURRENT (v5.2):** install_writer_v52_s47d_part1/2/3.ps1 — but v5.2 is SUPERSEDED by v5.3 (to be built S54). Do not run new v5.2 batches.

---

# SESSION 54 UPDATE — May 22, 2026

## reverb.html — S54 Commit Command

**Option A — Claude commits from bash (preferred):**
Steve uploads reverb_v16b.html to Claude session renamed as reverb.html and says "commit reverb.html". Claude executes directly.

**Option B — Steve commits via PowerShell:**
```powershell
. .\setenv.ps1
$content = [System.IO.File]::ReadAllBytes("C:\Users\swarn\OneDrive\Desktop\mpw-scripts\reverb.html")
$base64 = [System.Convert]::ToBase64String($content)
$sha_resp = Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" -Headers @{Authorization="token $env:GITHUB_TOKEN"} -ErrorAction SilentlyContinue
$body = @{message="feat: reverb.html S54 — definitive reverb reference — v1.6 — 383KB — SEO + revenue pass";content=$base64;branch="main"}
if ($sha_resp.sha) { $body.sha = $sha_resp.sha }
Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" -Method PUT -Headers @{Authorization="token $env:GITHUB_TOKEN";"Content-Type"="application/json"} -Body ($body | ConvertTo-Json)
```

NOTE: reverb.html is 383.5KB — fine for single-file API PUT. 200KB limit applies only to ZIP/Notepad method.

## Zenodo DOI Workflow (NEW S54 — implement after reverb.html commits)

```
1. Create account: zenodo.org
2. New upload → Upload Type: Publication → Publication Type: Technical Note
3. Fill metadata:
   - Title: Reverb — The Producer's Bible
   - Authors: MusicProductionWiki Editorial Team
   - Description: [entry meta description]
   - License: Creative Commons Attribution-NonCommercial 4.0
   - Related URL: https://musicproductionwiki.com/bible/reverb
   - Version: 1.6
4. Upload PDF export of reverb_v16b.html (print to PDF from browser)
5. Publish → DOI issued: 10.5281/zenodo.XXXXXXX
6. Update citation block in reverb.html: replace "Pending" with actual DOI
7. Commit updated file
```

## Crossref Membership Application (NEW S54)

Apply at: crossref.org/membership
Cost: $275/year
Process: 1–2 week approval
After approval: register MPW as publisher, get custom DOI prefix (10.XXXXX)
Future entries: use Crossref DOI prefix instead of Zenodo
Zenodo entries: add "superseded by" pointer to Crossref DOI

## JS Triple-Check Script (UPDATED S54)

The standard JS triple-check now accounts for 5 script blocks (4 internal + external Beehiiv scripts). Only run node --check on internal `<script>` blocks — skip external src= scripts.

```python
import re, subprocess, tempfile, os

def js_triple_check(html):
    errors = []
    # Only check inline scripts (no src attribute)
    scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', html, re.DOTALL)
    for i, content in enumerate(scripts):
        # Skip JSON-LD blocks
        if '@context' in content or 'application/ld' in content:
            continue
        apos = re.findall(r"(?<!\\)\b\w+'\w+\b", content)
        if apos:
            errors.append(f"Block {i} APOSTROPHE: {apos[:5]}")
        non_ascii = re.findall(r'[^\x00-\x7F]', content)
        if non_ascii:
            errors.append(f"Block {i} UNICODE: {[hex(ord(c)) for c in set(non_ascii)][:5]}")
        with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(content)
            tmpfile = f.name
        result = subprocess.run(['node', '--check', tmpfile], capture_output=True, text=True)
        os.unlink(tmpfile)
        if result.returncode != 0:
            errors.append(f"Block {i} SYNTAX: {result.stderr.strip()[:100]}")
    return errors
```

## Stale Scripts — Updated List (S54)

| Script | Issue |
|---|---|
| install_bible_writer_v52_part1/2/3.ps1 | Writes UNFIXED writer — DO NOT RUN |
| install_writer_v52_s46_part1/2/3.ps1 | Session 46 — superseded |
| install_writer_v52_s47_part1/2/3.ps1 | PS1 syntax error — DO NOT RUN |
| install_writer_v52_s47b_part1/2/3.ps1 | Session 47b — missing fixes — DO NOT RUN |
| install_writer_v52_s47d_part1/2/3.ps1 | v5.2 — SUPERSEDED by v5.3 (to be built S55) |

**CURRENT:** v5.3 writer to be built in Session 55 from reverb_v16b.html gold standard.

## Session 55 First Steps

```powershell
. .\setenv.ps1
python mpw_session_start.py
python verify_fixes.py
```

Then: confirm reverb.html mobile QA complete → upload to session → "commit reverb.html" → Claude commits → begin v5.3 writer build.

---

# SESSION 54 ADDENDUM — WRITER BUILD SEQUENCE FOR NEW CONTENT TYPES — May 22, 2026

## Writer Build Roadmap (Sessions 55–64)

| Session | Writer | Content Type | Target Count |
|---|---|---|---|
| 55 | v5.3 (T1/T2/T3) | Flagship/Standard/Reference | Run 33 remaining T1 |
| 57 | Genre Bible writer | Type 7 | 20 Genre entries |
| 59 | Producer DNA writer | Type 4 | 100 Producer entries |
| 61 | Gear/Plugin Reference writer | Type 6 | 150 Gear entries |
| 63 | Track Anatomy writer | Type 5 | 200 Track entries (incl. Batch 09) |

Each writer follows the same delivery standard as v5.3:
- 3-part base64 PS1 scripts if file exceeds 200KB
- JS triple-check on all output
- node --check subprocess on all script blocks
- Model: claude-sonnet-4-6
- --validate flag with type-specific validation suite
- --workers flag (default 4, max 8)

## Genre Bible Writer Spec (Session 57 — Type 7)

Batch file format: `slug:Genre Name:7`
Example: `trap:Trap:7`

Key writer requirements:
- Genre settings table: BPM range, key preferences, typical compression, typical reverb, loudness target
- Essential plugins table: 10 tools with genre-specific use case per tool
- Essential sample packs table: 5 curated packs with affiliate links
- Reference tracks: 10 essential tracks with timestamps and what to listen for
- Internal Bible links: minimum 20 links to relevant T1/T2 entries
- HowTo schema: genre production workflow steps
- MusicGenre schema type
- FAQPage: 8 questions specific to making the genre
- No invented production claims — all technique specs must be verifiable

## Producer DNA Writer Spec (Session 59 — Type 4)

Batch file format: `slug:Producer Name:4`
Example: `metro-boomin:Metro Boomin:4`

Key writer requirements:
- All signal chain specs sourced only from verified interviews, confirmed gear lists, direct attribution
- NEVER invent equipment or settings — leave placeholder if unconfirmed
- Producer quotes: minimum 2, maximum 4, all with source and date
- Reference tracks: minimum 3, all with timestamps
- Internal Bible links: minimum 8 to T1/T2 entries the producer's techniques relate to
- Person schema type with sameAs Wikipedia link
- PDF Blueprint variable: `{{BLUEPRINT_URL}}` — filled at Gumroad upload time
- Validation must check: quote citations present, no invented equipment claims

## Gear/Plugin Reference Writer Spec (Session 61 — Type 6)

Batch file format: `slug:Product Name:Manufacturer:6`
Example: `valhalla-room:Valhalla Room:Valhalla DSP:6`

Key writer requirements:
- Product schema type with price and manufacturer
- Every parameter documented: min/max range, musical interpretation, interaction effects
- Genre settings table: 6–8 genres with typical settings for this specific plugin
- Comparison section: where it sits vs 2–3 alternatives
- Affiliate link: rel="noopener sponsored" — URL filled when affiliate program approved
- Review schema: editorial rating (Sound Quality, Value, Ease of Use, Versatility)
- Partner disclosure block if editorial partnership exists
- Validation must check: price accuracy, manufacturer name accuracy, no invented specs

## Track Anatomy Writer Spec (Session 63 — Type 5)

Batch file format: `slug:Track Title:Artist:Year:5`
Example: `billie-jean:Billie Jean:Michael Jackson:1983:5`

Key writer requirements:
- MusicRecording schema with producer, artist, year
- All production claims must be verifiable — studio documentation or widely confirmed
- Timestamp guide: minimum 5 specific timestamps with what to listen for
- Inline SVG spectrogram: characteristic frequency/dynamic signature of the track
- DAW exercise: 3 specific exercises recreating key elements
- Internal Bible links: minimum 10 to T1/T2 entries the track's techniques demonstrate
- Validation must check: track credits accurate, no invented production claims

## Digital Product Generation Script (Future — Session 59+)

```python
# mpw_blueprint_generator.py
# Extracts Producer DNA entry data and generates $9 Blueprint PDF
# Requires: reportlab or weasyprint, Producer DNA entry HTML

def generate_blueprint(slug, entry_html):
    # Extract: producer name, signal chains, top plugins, reference tracks
    # Populate PDF template
    # Save to /outputs/blueprints/{slug}-blueprint.pdf
    # Upload to Gumroad via API
    # Return Gumroad product URL
    pass
```

Build after Type 4 Producer DNA writer confirmed working.

## Gumroad Setup Checklist (When Ready)

```
1. Create Gumroad account: gumroad.com
2. Connect Stripe or PayPal for payouts
3. Upload first PDF product (Producer Blueprint — test with one entry)
4. Set price: $9.00
5. Enable "Pay what you want" minimum $9 (optional — captures more revenue)
6. Get product URL: gumroad.com/l/[product-id]
7. Add URL to Bible entry as {{BLUEPRINT_URL}} variable
8. Test purchase end-to-end before running full batch
```

## Viral Distribution Scripts (Reusable Templates)

### Twitter/X Thread Template — Three Questions Framework
```
Tweet 1: "Most producers think reverb is about how much space you add. It's not. It's about answering three questions, in order, before touching a single parameter. 🧵"

Tweet 2: "Question 1: What is the emotional role of this element in THIS moment? Not throughout the track. Right here. HUMBLE. demands proximity. That single answer eliminates every large hall, every long decay. The question answered itself before the DAW opened."

Tweet 3: "Question 2: What acoustic environment serves that emotional role? Not a reverb type — an environment. A room. A cathedral. An open field. Think in spaces, not plugins. Holocene inhabits a geological space. That answer points directly to shimmer. The space defined the tool."

Tweet 4: "Question 3: What is the minimum amount of reverb that achieves it? This is the question that separates professional reverb use from amateur reverb use. Finneas found it by muting the return until the vocal felt wrong without it. The level defined by its absence."

Tweet 5: "We built the full framework into a free reference entry — with the Clearmountain, Everett, and Finneas signal chains, a live RT60 calculator, and every common mistake fixed with exact parameters. [link to entry]"
```

### Reddit Post Template — r/WeAreTheMusicMakers
```
Title: "I spent months building what I think is the most comprehensive free reverb reference on the internet. Here's the most important thing I learned."

Body: [Beginner Trap section content — 3 mistakes, 3 fixes]

"The full entry has the Three Questions framework, Clearmountain/Everett/Finneas signal chains with exact dB values, a live RT60 calculator, 7 reverb types including a full shimmer deep-dive, and a mix translation test across 5 playback systems. All free. [link]"
```

---

# SESSION 55 ADDENDUM — SCRIPTS — May 22, 2026

## mpw_tools_v3.py — Updated (Session 55)

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_tools_v3.py`
Version: Session 55 branding-corrected build
Lines: 1,227 — Size: 80.0KB — Syntax: CLEAN — Tools: 12 — Slugs: 49

**6 branding gaps fixed this session** (see HANDOFF-TECH for full detail).

Install: drop updated file into mpw-scripts\ — no other changes required.

Verify after install:
```powershell
python -c "from mpw_tools_v3 import build_tools_section_v3; html=build_tools_section_v3('compression','Compression'); print('MusicProductionWiki.com' in html, 'Embed This Tool' in html, 'letter-spacing:.04em' in html)"
```
Should print: `True True True`

## reverb.html — GitHub API Commit (Reference)

Session 55 used direct Python urllib.request commit (no curl — file too large for shell arg limit):

```python
import json, urllib.request, base64

TOKEN = "ghp_..."
REPO  = "musicproductionwiki/musicproductionwiki"
FILE  = "bible/reverb.html"

with open('/path/to/reverb_v16b.html', 'rb') as f:
    content = base64.b64encode(f.read()).decode('ascii')

# Get SHA
url = f"https://api.github.com/repos/{REPO}/contents/{FILE}"
req = urllib.request.Request(url)
req.add_header('Authorization', f'token {TOKEN}')
with urllib.request.urlopen(req) as r:
    sha = json.loads(r.read())['sha']

# Commit
payload = json.dumps({"message": "commit message", "content": content, "sha": sha}).encode()
req2 = urllib.request.Request(url, data=payload, method='PUT')
req2.add_header('Authorization', f'token {TOKEN}')
req2.add_header('Content-Type', 'application/json')
with urllib.request.urlopen(req2) as r:
    result = json.loads(r.read())
    print(result['commit']['sha'])
```

**NEVER use curl for large files** — shell argument list too long error above ~400KB base64.

## mpw_bible_writer.py — Status (Session 55)

The v5.3 writer was NOT built this session — architecture was confirmed and S56 is the build session.

**Architecture confirmed:**
- TRUE 1-pass: one API call, structure frozen, Claude fills content slots only
- Tools: injected from mpw_tools_v3.py — Claude never generates tool HTML
- Gold standard: reverb.html (v1.6) — 25 sections — replaces compression.html as reference

**v5.3 writer build checklist for Session 56:**
1. Read reverb.html gold standard in full before writing a single function
2. Build frozen template with {{SLOT}} markers for all 25 sections + JS data blocks
3. One API call (claude-sonnet-4-6, 28,000 tokens) fills all slots
4. Python substitutes slots, injects tools via `build_tools_section_v3(slug, term)`
5. Python calculates word count, builds 5 JSON-LD schema blocks, assembles final HTML
6. node --check on all inline JS blocks before output
7. Deliver via base64 PS1 script (NEVER .py download direct)

**v5.3 validation targets:** 95/95 checks

## Zenodo DOI Setup — Workflow (P3 for Steve)

Step-by-step:
1. Go to zenodo.org → Sign up (free) → Verify email
2. Click "New Upload" → Upload type: "Publication" → Subtype: "Technical note"
3. Title: "Reverb — The Producer's Bible | MusicProductionWiki.com"
4. Authors: MusicProductionWiki (organization)
5. Description: Paste entry abstract (first 3 sentences of definition section)
6. License: CC BY-NC
7. Related identifiers: URL → https://musicproductionwiki.com/bible/reverb → IsIdenticalTo
8. Submit → Zenodo issues DOI immediately (format: 10.5281/zenodo.XXXXXXX)
9. Add DOI to reverb.html citation block: replace {{DOI}} with full DOI string
10. Commit updated reverb.html (single file PUT — no SHA needed if editing locally)

Subsequent entries: repeat steps 2–10 per entry. Zenodo allows unlimited free uploads for open-access content.

## Crossref Membership — Workflow (P3 for Steve — $275/year)

Required for academic DOI issuance (Zenodo DOIs are free but Crossref DOIs have higher academic credibility):
1. crossref.org/membership → Apply for membership
2. Organization type: Publisher
3. Annual fee: $275 (base) — pay annually
4. After approval: assign DOIs in format 10.XXXXX/mpw-[slug]
5. Register each entry DOI via Crossref metadata deposit API
Build this workflow after Zenodo is running smoothly.


---

# SESSION 56 ADDENDUM — SCRIPTS — May 22, 2026

## mpw_tools_v4.py — Built, Delivered, Rejected

**Location:** C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_tools_v4.py
**Status:** DELIVERED but REJECTED — do not integrate into writer
**Size:** 84.4KB — 1,310 lines — 47 slugs — syntax clean — smoke test 47/47 PASS

The file was successfully written to disk via deliver_v4.ps1 (base64 PowerShell WriteAllBytes).
Steve confirmed import works. But after reviewing via tool_preview.html, Steve rejected the tools on quality grounds. See CORE-S56 for full explanation and rebuild spec.

**DO NOT** import mpw_tools_v4.py into mpw_bible_writer.py until the world-class rebuild is complete.

## tool_preview.html — How to Generate

After mpw_tools_v4.py is rebuilt (Session 57), generate the preview with a .py file (not python -c):

```python
# make_preview.py — save to mpw-scripts\ and run: python make_preview.py
from mpw_tools_v4 import build_tools_section_v4

slugs = [
    ('compression', 'Compression'),
    ('eq', 'EQ'),
    ('reverb', 'Reverb'),
    ('music-theory', 'Music Theory'),
    ('saturation', 'Saturation'),
    ('stereo-imaging', 'Stereo Imaging'),
    ('mastering', 'Mastering'),
    ('gain-staging', 'Gain Staging'),
    ('subtractive-synthesis', 'Subtractive Synthesis'),
    ('mix-bus', 'Mix Bus'),
]

html = '<html><body style="background:#0d0d0d;padding:20px;font-family:system-ui">'
for slug, term in slugs:
    html += '<h3 style="color:#f5a623;margin:24px 0 8px;font-size:11px;letter-spacing:.1em;text-transform:uppercase">%s</h3>' % slug
    html += build_tools_section_v4(slug, term)
    html += '<br>'
html += '</body></html>'

with open('tool_preview.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done — open tool_preview.html in your browser')
```

**CRITICAL:** Use make_preview.py (a file), NEVER python -c for multi-line scripts. PowerShell mangles backslash-quote sequences.

## NEVER Rules — Scripts (Session 56)

| Rule | Detail |
|---|---|
| NEVER use print() at module level in mpw_tools_v*.py | Executes on every import — confirmed annoying — all print statements must be inside if __name__ == '__main__' |
| NEVER build tool chunks in separate files and concatenate | Causes scoping issues, import pollution, and assembly errors — write the full file as a single coherent script |
| NEVER test tools on file:// protocol | Clipboard API and CSP restrictions differ from Netlify — always test on live Netlify or via make_preview.py opened from a local server |
| NEVER run python -c with multi-line scripts in PowerShell | Use a .py file — PowerShell mangles quotes and backslashes in multi-line -c strings |

## v4 Tool Build Approach — Session 57 (Correct Method)

The correct build method for complex Python files:

1. Read ALL of mpw_tools_v3.py from disk before writing a single line of v4
2. Read every single tool body in v3 — not just _brand_header() and _share() — every build_gr(), build_delay(), build_adsr() etc.
3. Write a design spec for each v4 tool FIRST — what inputs, what visual output, what presets, what the computed result is
4. Build one tool at a time in a temp .py file, test it with make_preview.py, approve it visually before moving to next
5. Assemble all 12 into one file only after each tool is individually confirmed
6. NEVER use chunk files (tools_1_4.py, tools_5_8.py etc.) — write the full file directly
7. Deliver via base64 PS1 (WriteAllBytes) — same method as v3


---

# SESSION 57/58 UPDATE — May 22, 2026

## mpw_tools_v4.py — REBUILT (World-Class Version)

**Location:** C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_tools_v4.py
**Status:** REBUILT — 195,294 bytes — 6 tools — 33 slug mappings — 6/6 JS PASS
**CSS class prefix:** `.t4` (v3 uses `.t3`) — no conflicts

The Session 56 rejected version was discarded. This is a clean rebuild at v5 quality standard.

### Install via Two-Part PS1

```powershell
# Save both files via Notepad -> Save As -> All Files (bypass Cloudflare)
Unblock-File .\deliver_v4_part1.ps1
Unblock-File .\deliver_v4_part2.ps1
. .\deliver_v4_part1.ps1   # writes temp base64 chunk to %TEMP%
. .\deliver_v4_part2.ps1   # assembles mpw_tools_v4.py + runs smoke test
```

Expected smoke test output:
```
Written: C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_tools_v4.py (195294 bytes)
PASS 31291 chars
```

### Verify Install

```powershell
python -c "from mpw_tools_v4 import build_tools_section_v4; r=build_tools_section_v4('compression','Compression'); print('PASS', len(r), 'chars') if r else print('FAIL')"
# Expected: PASS 31291 chars

python mpw_tools_v4.py
# Smoke test — all 6 tools + dispatcher verified
```

### Integration into mpw_bible_writer.py (Session 59 P0)

Add to writer:
```python
from mpw_tools_v4 import build_tools_section_v4, TOOL_OVERRIDES_V4

def build_tools_section(slug, term):
    # Try v4 first (6 new world-class tools)
    result = build_tools_section_v4(slug, term)
    if result is not None:
        return result
    # Fall through to v3 (12 existing tools)
    return build_tools_section_v3(slug, term)
```

The v4 dispatcher returns `None` for slugs not in its map — safe to fall through to v3.

### Tool Map — v4 (33 slugs)

| Tool | Slugs |
|---|---|
| T1 Attack/Release Calculator | compression, limiting, parallel-compression, multiband-compression, bus-compression, noise-gate, adsr, envelope |
| T2 Vocal Chain Builder | delay, reverb, send-return, automation, gain-staging |
| T3 EQ Problem Solver | eq, parametric-eq, shelving-eq, hpf, lpf, air-frequency-eq, resonance |
| T4 Frequency Conflict Detector | stereo-imaging, mid-side-processing, dynamic-range |
| T5 Saturation & Harmonic Character | saturation, distortion, harmonic-distortion, clip-gain |
| T6 Mix Bus Headroom & Summing | mix-bus, headroom, mastering, lufs, loudness-normalization, true-peak-limiting |

### Plugin Format — Unified (Session 58)

All 6 tools now use the same tier-colored plugin renderer: `Free | Mid | Pro | Key insight` format with color-coded labels. T2 and T3 plugin strings were reformatted from `Stage: names` pattern to tier format. Renderer uses createElement/appendChild — no innerHTML.

## Tool Preview — How to Generate (Session 58 Method)

```python
# make_v4_preview.py — save to mpw-scripts\ and run: python make_v4_preview.py
import sys
sys.path.insert(0, r'C:\Users\swarn\OneDrive\Desktop\mpw-scripts')
from mpw_tools_v4 import build_tools_section_v4

tests = [
    ('compression', 'Compression'),
    ('eq', 'EQ'),
    ('saturation', 'Saturation'),
    ('stereo-imaging', 'Stereo Imaging'),
    ('mix-bus', 'Mix Bus'),
    ('mastering', 'Mastering'),
]

html = '<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>*{box-sizing:border-box;margin:0;padding:0}body{background:#080808;color:#e0ddd8;font-family:system-ui;padding:20px}</style></head><body>'
for slug, term in tests:
    html += f'<div style="max-width:700px;margin:0 auto 40px"><h3 style="color:#f5a623;font-size:10px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:10px">{slug}</h3>'
    html += build_tools_section_v4(slug, term) or f'<p style="color:#555">No v4 tool for {slug}</p>'
    html += '</div>'
html += '</body></html>'

with open('tool_v4_preview.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done — open tool_v4_preview.html')
```

## JS Triple-Check for Tool Development (S57/58 Pattern)

This is the validated check function used in Session 57/58 for every tool:

```python
import re, subprocess, tempfile, os, sys

def js_check(html, label):
    errors = []
    scripts = re.findall(r'<script>(.*?)<\/script>', html, re.DOTALL)
    for i, content in enumerate(scripts):
        apos = re.findall(r"(?<!\\)\b\w+'\w+\b", content)
        if apos: errors.append(f"[{label}] APOSTROPHE: {apos[:5]}")
        non_ascii = re.findall(r'[^\x00-\x7F]', content)
        if non_ascii: errors.append(f"[{label}] UNICODE: {[hex(ord(c)) for c in set(non_ascii)][:5]}")
        with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(content); tmp = f.name
        r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode != 0: errors.append(f"[{label}] SYNTAX: {r.stderr.strip()[:300]}")
    return errors
```

## NEVER Rules Added Session 57/58 — Scripts

| Rule | Detail |
|---|---|
| NEVER use unicode chars directly in JS strings | Run `re.sub(r'[^\x00-\x7F]', lambda m: '\\u{:04x}'.format(ord(m.group())), js)` before output |
| NEVER use innerHTML anywhere in tool JS | CSP blocks it on /bible/* — always createElement/appendChild |
| NEVER deliver tools with escape sequences as \\uXXXX that Python renders to actual unicode | Python f-strings render \\u25b2 as actual triangle char — use ASCII alternatives (^ v) for expand/collapse |
| NEVER embed </script> as literal string in Python tool heredocs | Use SC = '</' + 'script>' — always |
| NEVER use print() at module level | All diagnostic prints inside if __name__ == '__main__' block |

---

# SESSION 60 UPDATE — SCRIPTS — May 23, 2026

## New Scripts Delivered

### fix_v3_mobile.py — CONFIRMED PASS

**Purpose:** Patches `mpw_tools_v3.py` — fixes canvas mobile rendering on ADSR and Stereo Width tools.

**Run:**
```powershell
cd C:\Users\swarn\OneDrive\Desktop\mpw-scripts
python fix_v3_mobile.py
```

**Confirmed output (Steve's machine):**
```
Syntax: CLEAN
[OK] ADSR canvas element (remove hardcoded width)
[OK] aDraw() -- use offsetWidth at draw time
[OK] aDraw() -- add ResizeObserver
[OK] Stereo Width canvas element (remove hardcoded width)
[OK] swCalc() -- use offsetWidth at draw time
[OK] swCalc() -- add ResizeObserver
All checks PASS. Fix complete.
```

**Status:** ✅ Run and confirmed on Steve's machine. `mpw_tools_v3.py` now has correct canvas standard for ADSR and Stereo Width.

---

### patch_canvas_mobile.py — READY TO RUN

**Purpose:** Surgically patches 3 live Bible entries (adsr.html, envelope.html, stereo-imaging.html) with the same canvas mobile fix. Uses Trees API — single Netlify deploy.

**Run (after mobile previews confirmed OK on real iPhone):**
```powershell
. .\setenv.ps1
python patch_canvas_mobile.py
```

**All 6 patch targets confirmed against live GitHub files before delivery.**

**Verify after run:**
- https://musicproductionwiki.com/bible/adsr
- https://musicproductionwiki.com/bible/envelope
- https://musicproductionwiki.com/bible/stereo-imaging

---

### mpw_tools_v5a.py — DELIVERED — PASS 8/8

**Purpose:** Tools 1–8 (v3 rebuilds with v5 standard). 119KB, 1,479 lines.

**Smoke test:**
```powershell
python mpw_tools_v5a.py
```
Expected: `Syntax: CLEAN` + `All tests PASS`

**Import:**
```python
from mpw_tools_v5a import build_tools_section_v5a, TOOL_OVERRIDES_V5A
```

---

### mpw_tools_v5b.py — DELIVERED — PASS 8/8

**Purpose:** Tools 9–16 (v3 rebuilds + 4 new tools). 99KB, 1,675 lines.

**Smoke test:**
```powershell
python mpw_tools_v5b.py
```
Expected: `Syntax: CLEAN` + `All tests PASS`

---

### mpw_tools_v5c.py — DELIVERED — PASS 8/8

**Purpose:** Tools 17–24 (8 new tools). 87KB, 953 lines.

**Smoke test:**
```powershell
python mpw_tools_v5c.py
```
Expected: `Syntax: CLEAN` + `All tests PASS`

---

### mpw_tools_v5_dispatch.py — DELIVERED — PASS

**Purpose:** Unified dispatcher for all 24 v5 tools. Routes 145 slugs (v5 only — v4 tools have separate dispatcher) to the correct batch file.

**Run smoke test:**
```powershell
python mpw_tools_v5_dispatch.py
```
Expected: `Syntax OK` for all 3 files + `Total slugs: 145` + `Dispatcher smoke test: PASS`

**Integration with mpw_bible_writer.py (one-line swap):**
```python
# OLD:
from mpw_tools_v3 import build_tools_section_v3, TOOL_OVERRIDES

# NEW:
from mpw_tools_v5_dispatch import build_tools_section_v5 as build_tools_section_v3, TOOL_OVERRIDES_V5 as TOOL_OVERRIDES
```

---

## Scripts to Build — Session 61

### mpw_affiliates.py — BUILD FIRST

**Purpose:** Affiliate link registry. All plugin recommendations across all 36 tools reference this file. One approval → one file update → all tools update.

**Structure:**
```python
AFFILIATE = {
    'plugin_boutique': 'https://www.pluginboutique.com/?a_aid=PLACEHOLDER',
    'sweetwater': 'https://sweetwater.sjv.io/PLACEHOLDER',
    'amazon': 'https://amzn.to/PLACEHOLDER',
    'loopmasters': 'https://www.loopmasters.com/?a_aid=PLACEHOLDER',
    'pluginfox': 'https://www.pluginfox.com/?ref=PLACEHOLDER',
}

# Plugin → affiliate program mapping
PLUGIN_AFFILIATES = {
    'Valhalla Room': ('plugin_boutique', 'valhalla-room'),
    'FabFilter Pro-Q 3': ('plugin_boutique', 'fabfilter-pro-q-3'),
    'Waves CLA-76': ('plugin_boutique', 'waves-cla-76'),
    # ... all plugins from all 36 tools (v4 T1-T12 + v5 tools 1-24)
}

def aff_link(plugin_name, display_text=None):
    """Returns affiliate href for a plugin name."""
    ...
```

---

### mpw_tool_manifest.py — BUILD SECOND

**Purpose:** Single source of truth for all 36 tools. All generators (tool pages, hub page, sitemap) read from this manifest.

**Structure per tool:**
```python
TOOLS = [
    {
        'slug': 'adsr-visualizer',
        'name': 'ADSR Envelope Visualizer',
        'category': 'Time & Modulation',
        'bible_slug': 'adsr',  # links to /bible/adsr
        'description': 'Visualize ADSR envelope shapes with Web Audio preview. 15 presets.',
        'meta_description': 'Free ADSR visualizer with audio preview. Set attack, decay, sustain, release and hear the result. 15 producer presets for trap, R&B, EDM and more.',
        'long_tail_keywords': ['adsr calculator online', 'adsr envelope visualizer', 'adsr settings trap'],
        'related_tools': ['delay-time-calculator', 'lfo-sync-calculator'],
        'faq': [
            {'q': 'What is ADSR?', 'a': '...'},
            ...
        ],
    },
    # ... all 36 tools
]
```

---

### generate_tool_pages.py — BUILD THIRD

**Purpose:** Generates all 24 standalone `/tools/[slug].html` pages from the manifest. Each page includes: tool HTML (from v5 dispatch), SEO meta, keyword content, FAQPage schema, SoftwareApplication schema, related tools section, embed code.

**Run:**
```powershell
python generate_tool_pages.py
```

Output: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\tools\` (24 HTML files)

Then commit all to `tools/` directory via Trees API.

---

### generate_tools_hub.py — BUILD FOURTH

**Purpose:** Generates `/tools/index.html` — the category hub page with 8 categories, search/filter, and all 36 tool cards.

**Run:**
```powershell
python generate_tools_hub.py
```

Output: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\tools\index.html`

Then commit to `tools/index.html` via Trees API.

---

## Parallel Build Sessions — Session 60 Record

Session 60 used 3 simultaneous Claude sessions to build 24 tools in parallel. Each session received a self-contained prompt (session_A_tools_1_8.md, session_B_tools_9_16.md, session_C_tools_17_24.md) with complete boilerplate, canvas standard, tool specs, slug mapping, and smoke test.

Results:
- Session A: 8 tools — PASS 8/8 — 119KB — 1,479 lines
- Session B: 8 tools — PASS 8/8 — 99KB — 1,675 lines
- Session C: 8 tools — PASS 8/8 — 87KB — 953 lines

**This parallel approach is reusable** for future tool batches. Session prompt files are stored in mpw-scripts\ as templates.



---

# SESSION 62 UPDATE — SCRIPTS — May 24, 2026

## mpw_bible_cat_pages.py — FINAL SESSION 62

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_cat_pages.py`

Generates all 11 Bible category pages at `bible/categories/[slug]/index.html` via Trees API.

```powershell
python mpw_bible_cat_pages.py --test   # preview Dynamics page only
python mpw_bible_cat_pages.py --run    # commit all 11 pages
```

**Architecture:**
- Fetches live `bible-index.json` from GitHub (222 entries)
- Builds exact reverb.html nav (slim bar 36px, bible bar with 11 categories, bmn-drawer grid)
- A-Z letter index: only rendered when category has ≥ 50 entries — JS hides empty letter headers after filter
- Subcat filter pills: Tools page only (content pages have no subcategory tags on entries)
- Tools page uses TOOL_MANIFEST (36 tools from mpw_tool_manifest.py) — links to `/tools/[slug]`
- Hero max-width 1100px, main max-width 1100px
- Mobile: single column grid at 768px, fluid H1

**TOOL_MANIFEST:** Exact slugs from `mpw_tool_manifest.py` — verified against live GitHub tree before each run.

**Run after:** Any bible-index.json update, any Bible entry batch, any copy/layout change.

---

## generate_tool_pages_v2.py — FINAL SESSION 62

Location: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\generate_tool_pages_v2.py`

Generates all 36 standalone tool pages at `tools/[slug].html` via Trees API.

```powershell
python generate_tool_pages_v2.py              # generates + commits all 36
python generate_tool_pages_v2.py --dry-run    # generates locally only
```

**Architecture:**
- Reads tool list from `mpw_tool_manifest.py` (ALL_TOOLS — 36 tools)
- Dispatches real tool HTML from `mpw_tools_v5_dispatch.py` via `build_tools_section_v5(bible_key, name)`
- Strips `<h2>Tools for This Entry</h2>` from dispatch output (redundant on standalone pages)
- TOOL_PAGE_CSS contains full inline nav CSS (slim bar, bible bar, bmn-drawer, search overlay) — no dependency on style.css for nav
- CSS path: `/css/style.css` (absolute)
- Footer: inline-styled via `make_footer()` — `.site-footer` CSS in TOOL_PAGE_CSS
- Slug override: `transient-shaping` → `transient-shaper` in dispatch

**Dispatch coverage:** 35/36 tools covered directly. `transient-shaper-reference` uses `_overrides = {"transient-shaping": "transient-shaper"}`.

**Run after:** Any tool content update, any nav change, any copy change.

---

## NEVER Rules Added — Session 62 — Scripts

| Rule | Detail |
|------|--------|
| NEVER commit tool pages without confirming dispatch returns real content (not empty/placeholder) | Check `len(tool_html) > 100` is not sufficient — open the live page |
| NEVER modify `make_footer()` or any major function without verifying TOOL_PAGE_CSS still exists in file after edit | Accidentally deleted during refactor — caused 36/36 FAIL |
| NEVER use placeholder tool content as a "Phase 2" deferral without flagging it clearly to Steve | Placeholder was committed and called "working" — it was not |
| NEVER generate tool pages without TOOL_PAGE_CSS containing all nav class definitions | Classes must be inline — style.css definitions are unreliable at /tools/ depth |
| NEVER ask Steve to run PowerShell to fetch GitHub files Claude can fetch directly with the token | Token ghp_[REDACTED - stored in setenv.ps1] is always in memory — use it |

---

# SESSION 63 UPDATE — SCRIPTS — May 24, 2026

## mpw_bible_cat_pages.py — S63f — CURRENT VERSION

**Location:** `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_cat_pages.py`
**Delivered as:** `mpw_bible_cat_pages_s63f.py` — Steve saves as `mpw_bible_cat_pages.py`
**Size:** ~55KB — 944 lines — SYNTAX CLEAN
**Status:** ✅ CURRENT — zero-mismatch SUBCAT_MAP — hero centered — pro card design

### Run Commands

```powershell
. .\setenv.ps1
python mpw_bible_cat_pages.py --test    # prints first generated page, no commit
python mpw_bible_cat_pages.py --run     # regenerates + commits all 11 category pages
```

### What Changed From Session 62 Version

1. **SUBCAT_MAP** — complete rebuild — 232 slug entries — zero mismatches against all 222 live bible-index.json entries. Previous version had 62 mismatches causing subcategory filters to show wrong entries.

2. **`build_cards()`** — letter headers entirely removed from HTML output. Each card has `data-subcat` attribute. Card label shows subcategory name via `subcat.title() if subcat else ecat`.

3. **JS filter** — reads `c.dataset.subcat` with exact equality (`subcat === _sub`). No longer reads textContent. `filterSub()` lowercases the filter value. Letter header JS code block removed.

4. **Card design** — professional rebrand: amber left border always visible at 20% opacity, full amber on hover, box-shadow lift, `→` arrow, `:active` state, `az-entry-body` wrapper, min-height 56px.

5. **Hero centering** — ALL hero elements centered: breadcrumb, eyebrow, h1, desc, count, pills, tools-why, tools-request. `bcat-hero-inner` has `text-align:center`. Tools request block converted from flex (with dot) to block (centered text, no dot).

6. **Tools page duplicate tagline removed** — `bcat-tools-tagline` paragraph removed from `tools_hero_extra`. Hero desc already covers "Built for the session. Not the syllabus."

7. **Responsive grid** — 4-col desktop → 3 at 1200px → 3 at 1024px → 2 at 768px → 1 at 480px. Tools grid: 3-col desktop → 2 at 1024px → 1 at 768px.

8. **Mobile card overrides** — permanent faint amber border on mobile (not just hover), min-height 60px for tap targets, arrow hidden on mobile, `:active` state for touch feedback.

### Session 63 Iteration History — CRITICAL LESSONS

**8 wasted commits before reaching s63f.** Every iteration was a full `--run` regenerating all 11 pages and one Netlify deploy. Full history documented in CORE append.

**Root causes of wasted commits:**

1. **CSS inject approach was wrong** — the S63 early inject (`cat-layout-s63`) committed to live pages was overwritten the moment Steve ran `--run` from the script. All fixes must be in the generator.

2. **SUBCAT_MAP built without live verification** — first version had 62 mismatches discovered only after Steve reported wrong filter counts. Always cross-check against live `bible-index.json`.

3. **Centering misunderstood as a width problem** — attempted to fix "looks left-aligned" by increasing max-width to 1400px. This made cards wider, not content more centered. The real fix was `text-align:center` on the container and each child element.

4. **Each delivery fixed some elements but missed others** — breadcrumb, eyebrow, h1, desc, count, pills, tools-why, tools-request all needed explicit centering. Each iteration caught one or two missed elements. Should have listed every single child element before writing any CSS.

5. **Script version confusion** — multiple file names (s63.py, s63b.py, s63c.py, s63d.py, s63e.py, s63f.py) delivered across session. Steve ran the wrong version at least once. Solution: always give the script a clearly incremented name and confirm Steve saves it over the correct path before running.

**How to avoid in future:**
- Before writing any centering CSS, list every HTML element inside the container that needs centering
- Run `--test` before `--run` to preview one page
- Use sequential naming (s63f is current) — never deliver unnamed or ambiguously-named files
- Run SUBCAT_MAP zero-mismatch check BEFORE delivering the script, not after

### SUBCAT_MAP Zero-Mismatch Verification Script

Run this before delivering any new version of `mpw_bible_cat_pages.py`:

```python
import urllib.request, json, base64

TOKEN = "ghp_[REDACTED — stored in setenv.ps1]"
# Fetch bible-index.json
req = urllib.request.Request(
    "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible-index.json",
    headers={"Authorization": f"token {TOKEN}"}
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
entries = json.loads(base64.b64decode(data['content']).decode('utf-8'))

# Import SUBCAT_MAP from the script
exec(open('mpw_bible_cat_pages.py').read().split('def fetch_bible_index')[0])

CATEGORIES_SUBCATS = {
    'Dynamics':          ['compression','limiting','gating','transient shaping','expansion','sidechain'],
    'Frequency':         ['eq','filters','high-pass','low-pass','shelving','air frequencies'],
    'Time-Based':        ['reverb','delay','chorus','modulation','pitch shifting'],
    'Signal Processing': ['saturation','distortion','clipping','harmonic enhancement','bit crushing'],
    'Mixing':            ['gain staging','stereo imaging','bus processing','routing','mid-side'],
    'Mastering':         ['loudness','lufs','true peak','limiting','delivery'],
    'Synthesis':         ['subtractive','fm','wavetable','additive','lfo','envelopes'],
    'Music Theory':      ['scales & modes','chords','rhythm','harmony','arrangement'],
    'Production':        ['beat making','midi','sampling','daw workflow','sound design'],
    'Recording':         ['microphones','preamps','interfaces','acoustics','vocal production','recording settings'],
}

total_missing = 0
for cat_name, valid_subcats in CATEGORIES_SUBCATS.items():
    cat_entries = [e for e in entries if e.get('category','') == cat_name]
    for e in cat_entries:
        slug = e.get('slug','')
        subcat = SUBCAT_MAP.get(slug,'')
        if not subcat:
            print(f"MISSING: {cat_name}/{slug}")
            total_missing += 1
        elif subcat not in valid_subcats:
            print(f"WRONG: {cat_name}/{slug} → '{subcat}'")
            total_missing += 1

if total_missing == 0:
    print(f"PERFECT — all {len(entries)} slugs correctly mapped")
else:
    print(f"{total_missing} mismatches — fix before delivering")
```

## mpw_bible_writer.py — Read Time Update PENDING

The writer currently calculates read time at 500 wpm (per v5.2 spec). Steve confirmed 650 wpm is the standard going forward in Session 63. The `count_words_html()` function word count is correct — only the wpm divisor needs updating.

**Required change:**
```python
# CURRENT (wrong):
read_time = max(1, round(word_count / 500))

# CORRECT (650 wpm standard):
read_time = max(1, round(word_count / 650))
```

This must be applied before running any new T1 batch. Run `--validate` after the change.

## Scripts to Build — Session 64

The tools hub build is the P0 for Session 64. Rather than separate generator scripts (mpw_affiliates.py + mpw_tool_manifest.py + generate_tool_pages.py + generate_tools_hub.py as originally planned), Session 64 will build `/tools/index.html` directly as a hand-crafted HTML page — same approach as reverb.html and bible/index.html. This gives full design control without generator overhead.

See the tools hub build prompt delivered at end of Session 63 for the complete specification.

## NEVER Rules Added — Session 63 — Scripts

| Rule | Detail |
|------|--------|
| NEVER deliver mpw_bible_cat_pages.py without running zero-mismatch SUBCAT_MAP verification | 62 mismatches in first S63 version — always cross-check against live bible-index.json before delivery |
| NEVER commit a new category page generator version without running --test first | `--test` flag prints first generated page without committing — catches template errors cheaply |
| NEVER fix generator-managed pages with CSS injection | `--run` overwrites all pages from scratch — inject-only patches are lost on every run |
| NEVER deliver a script with ambiguous naming when multiple versions are in flight | S63 had 6 versions (s63 through s63f) — always use clearly incremented names and confirm Steve is saving to the right path |
| NEVER use read time below 650 wpm for Bible entries | 500 wpm is confirmed wrong — 650 wpm is the standard — update mpw_bible_writer.py before next T1 batch |
| NEVER commit all 11 category pages without verifying at least one on the live site first | --run commits all 11 in one Trees API call — if CSS or template is wrong, all 11 are broken at once |

---

# SESSION 63/64 UPDATE — SCRIPTS — May 24, 2026

## mpw_bible_cat_pages.py — S63f — CURRENT VERSION

See session63_scripts_append.md for full documentation. Summary:
- 232-slug SUBCAT_MAP — zero mismatches confirmed
- Hero centered — all child elements explicitly centered
- Professional amber card design
- Working dataset.subcat filter
- Letter headers removed

**Run commands:**
```powershell
. .\setenv.ps1
python mpw_bible_cat_pages.py --test
python mpw_bible_cat_pages.py --run
```

---

## mpw_bible_writer.py — TWO PENDING UPDATES (BLOCKS NEXT T1 BATCH)

Both changes must be applied before running any new Bible entries:

**1. Read time — change 500 wpm → 650 wpm:**
```python
# CURRENT (wrong):
read_time = max(1, round(word_count / 500))

# CORRECT:
read_time = max(1, round(word_count / 650))
```

**2. Nav updates — bible writer will be fully rewritten based on reverb.html gold standard in a future session.** Until then, do not run new T1 batches — the current writer nav is stale.

---

## mpw_writer.py — PENDING UPDATE (BLOCKS NEXT ARTICLE BATCH)

The mobile drawer in `mpw_writer.py` currently outputs the old vertical list `mobile-drawer` style. Before the next article batch, the writer must output the new grid-style drawer. The target HTML is documented in full in the CORE append (P0 batch scope section). Update the NAV_HTML or drawer template in the writer to match.

**Do NOT run mpw_writer.py for new article batches until this is updated.**

---

## Scripts to Build — Session 65 (Updated)

The following scripts are still needed (unchanged from Session 61/62 plan):

1. `mpw_affiliates.py` — affiliate link registry
2. `mpw_tool_manifest.py` — all 36 tools master record

Note: `generate_tools_hub.py` and `generate_tool_pages.py` are no longer needed — the hub was built as hand-crafted HTML (tools/index.html, SHA 8c7269d2) and the 36 tool pages are already live.

---

## NEVER Rules Added — Session 63/64 — Scripts

| Rule | Detail |
|------|--------|
| NEVER run mpw_bible_writer.py for new T1 entries before updating read time to 650 wpm | 500 wpm is confirmed wrong — produces inflated read times |
| NEVER run mpw_writer.py for new article batches before updating mobile drawer HTML | Current writer outputs old vertical list drawer — new grid style must be in writer before next batch |
| NEVER build generate_tools_hub.py | tools/index.html was hand-crafted — generator not needed and would add unnecessary complexity |


---

## ⚠️ BLOCKS — Must Fix Before Next Batches

| Blocker | What It Blocks | Status |
|---------|----------------|--------|
| `mpw_writer.py` — 4 pending updates (drawer, Tools nav, CSS specificity, pushState) | Next article batch | ⛔ PENDING since S63 |
| `mpw_bible_writer.py` — read time 650 wpm + nav rewrite | Next T1 Bible batch | ⛔ PENDING since S63 |
| `mpw_bible_writer.py` — v5.3 build (from reverb.html gold standard) | Full Bible tier quality | ⛔ NOT YET BUILT |
| Tool page/Bible card nav sync | Consistent UX — /tools/ and /bible/ both broken | ⛔ OPEN ACTION |
| `mpw_tools_v6_writer.py` | New tool batch generation | ⛔ NOT YET BUILT |
| `mpw_affiliates.py` | Affiliate link management | ⛔ NOT YET BUILT — pending affiliate approvals |

---

## ⚠️ NEVER Rules — Scripts (Consolidated S71)

| Rule | Added |
|------|-------|
| Never embed Python in HTML/JS — write JS as pure heredoc, run `node --check` before embedding | S67 |
| Never use `innerHTML` in any tool JS — Netlify CSP blocks it on `/tools/` and `/bible/` | S57/58 |
| Never hardcode plugin names or affiliate links in tool HTML — reference `mpw_affiliates.py` | S65 |
| Never load `style.css` in tool pages | S68 |
| Never start a parallel tool session without loading `MPW-TOOL-BUILD-SPEC.md` first | S66 |
| Never use `replaceState` in mobile drawer JS — use `pushState` + `popstate` | S66 |
| Never commit a tool without all 5 files in one Trees API commit | S67 |
| Never insert into catGrid without assertion check (`grid_open < card_pos < empty_pos`) | S67 |
| Never skip sitemap or search-index.json after tool build | S67 |
| Never run `mpw_bible_writer.py` for new T1 entries before updating read time to 650 wpm | S63 |
| Never run `mpw_writer.py` for new article batches before applying all 4 pending updates | S63 |
| Never use `print()` at module level in `mpw_tools_v*.py` | S56 |
| Never build tool chunks in separate files and concatenate | S56 |
| Never test tools on `file://` protocol — test via Netlify or local server | S56 |
| Never run `python -c` with multi-line scripts in PowerShell — use a .py file | S56 |
| Never use unicode chars directly in JS strings — use `\uXXXX` escapes | S57/58 |
| Never use `</script>` as literal string in Python — use `SC = '</' + 'script>'` | S57/58 |
| Never build `mpw_tools_v6_writer.py` without reading `mpw_tools_master_spec.md` first | S65 |
| Never autoplay audio on page load in Browser Apps — `await Tone.start()` in click handler only | S65b |
| Never import Tone.js from unconfirmed version — only cdnjs.cloudflare.com 14.8.49 | S65b |
| Never add a Browser App to `/tools/index.html` before confirmed live on GitHub | S65b |
| Never run `mpw_bible_cat_pages.py` without SUBCAT_MAP zero-mismatch verification first | S63 |
| Never upload any file to GitHub without running token redaction scan first | S68/S69 |
| Never use model `claude-sonnet-4-5` — correct model is `claude-sonnet-4-6` | S68 |
| Never use `curl` for files > ~400KB — use Python `urllib.request` | S55 |

---

# SESSION 65 UPDATE — SCRIPTS — May 24, 2026

## Session 65 — No New Scripts Delivered

All work this session was direct GitHub API operations from Claude's bash environment (individual PUTs and Trees API commits). No new Python scripts were written for Steve to run locally.

---

## mpw_writer.py — PENDING UPDATE (STILL BLOCKS NEXT ARTICLE BATCH)

The mobile drawer in `mpw_writer.py` currently outputs the old vertical list `mobile-drawer` style. Before the next article batch, the writer must output the new grid-style drawer confirmed and live on all 526 articles in Session 65.

**Target drawer HTML to freeze into writer:** See SESSION 65 UPDATE — TECH — "Mobile Drawer — Confirmed Final HTML" section. That is the exact HTML the writer must output.

**Also required in writer update:**
- Desktop nav must include `Tools →` li before Bible li
- CSS must use `nav.mpw-site-nav .nav-item>a.nav-bible-link` and `nav.mpw-site-nav .nav-item>a.nav-tools-link` specificity pattern (not class-only selectors)
- Drawer JS must use `pushState`+`popstate` pattern (not `replaceState`)

**Do NOT run mpw_writer.py for new article batches until all four items above are updated.**

---

## mpw_bible_writer.py — PENDING UPDATES (STILL BLOCKS NEXT T1 BATCH)

Two pending updates remain from prior sessions — unchanged:

**1. Read time — change 500 wpm → 650 wpm:**
```python
# CURRENT (wrong):
read_time = max(1, round(word_count / 500))

# CORRECT:
read_time = max(1, round(word_count / 650))
```

**2. Nav full rewrite based on reverb.html gold standard** — planned for a future session. Until done, do not run new T1 batches.

---

## mpw_tools_v6_writer.py — NEW — TOP PRIORITY NEXT SESSION

**This is the primary build target for Session 66.**

A batch Python writer for the 98 new tools specified in `mpw_tools_master_spec.md`. Same two-pass architecture as `mpw_bible_writer.py` but optimized for JS-heavy tool output instead of prose.

### Architecture

**Pass 1 — Tool Spec JSON (per tool):**
Prompt generates a structured JSON object containing:
- All input fields with types and default values
- Canvas type and drawing logic specification
- Genre data arrays (genre → recommended values)
- Preset definitions (name, values, engineering rationale)
- Warning threshold logic (what triggers red/amber/green states)
- Plugin tier recommendations (Free/Mid/Pro/Key — references mpw_affiliates.py)
- Famous settings (named producers/tracks, exact parameter values, why those values)
- SEO meta description and FAQ pairs

**Pass 2 — Full HTML/JS (from validated spec):**
Prompt generates self-contained HTML/JS from the Pass 1 JSON. The system prompt freezes the structural template — the model fills the tool-specific content only.

### Quality Constraints (must be in system prompt)
- No `innerHTML` anywhere — Netlify CSP blocks it on `/tools/` pages — use `createElement`/`appendChild` only
- Canvas: `width:100%;height:Xpx` CSS — no inline `width`/`height` attributes on canvas elements
- `SC = '</' + 'script>'` — never literal `</script>` in Python string literals
- All plugin recommendations via `mpw_affiliates.py` — never hardcoded strings
- Live warning logic: red/amber/green states on every output — not just numbers
- Famous presets: specific parameter values + the engineering rationale behind each value

### Key Constants (to be confirmed when building)
- Model: `claude-sonnet-4-6`
- PASS1_TOKENS: 8000 (spec JSON is smaller than Bible prose)
- PASS2_TOKENS: 16000 (tools are JS-heavy but shorter than T1 Bible entries)
- API timeout: 600 seconds
- ThreadPoolExecutor: 8 workers
- Save path: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\tools\`

### Build Order
1. Write `mpw_tools_v6_writer.py` with frozen HTML/JS template
2. Test on Priority 1 tools first (#1–3 from master spec)
3. Visual QA on test tools — confirm canvas, presets, warnings, plugin cards all work
4. Run Priority 1–2 batch (tools #1–35) — 35 tools
5. Commit via Trees API — single deploy
6. Update `/tools/index.html` to add new tool cards (hand-edit or build a manifest updater)

### Input Format (batch file)
```
slug:Tool Name:Category:Priority
mix-sounds-amateur-diagnostic:Why Does My Mix Sound Amateur? Diagnostic:Mixing & Signal Flow:1
should-i-sample-this:Should I Sample This? Decision Tree:Business & Legal:1
spotify-skip-probability-map:Spotify Skip Probability Map:Arrangement & Structure:1
...
```

---

## mpw_tools_master_spec.md — DELIVERED

**Location:** Steve's project files (downloaded this session)
**Content:** 98 tools, priority-ranked 1–98, categories, slugs, unique differentiators, paywall assignments
**Purpose:** Frozen input for `mpw_tools_v6_writer.py` — the writer reads from this spec, it does not improvise

**Paywall assignments:**
- Email gate: Royalty Split Calculator, Collaboration Agreement Builder, Release Readiness Scorer, Should I Sample This detailed report
- Never paywall: calculation tools, session-critical tools, business/legal tools that feed TruClarify leads

---

## Scripts to Build — Session 66

Priority order:

1. **`mpw_tools_v6_writer.py`** — batch tool generator (primary build — see architecture above)
2. **`mpw_writer.py` update** — freeze new drawer HTML + Tools nav + CSS specificity fix + pushState JS into writer
3. **`mpw_bible_writer.py` update** — 650 wpm read time + nav rewrite

---

## NEVER Rules Added — Session 65 — Scripts

| Rule | Detail |
|------|--------|
| NEVER build mpw_tools_v6_writer.py without reading mpw_tools_master_spec.md first | The spec is the frozen input — slugs, priorities, unique differentiators, paywall assignments all documented |
| NEVER use innerHTML in any tool generated by mpw_tools_v6_writer.py | Netlify CSP blocks innerHTML on /tools/ pages — all DOM manipulation must use createElement/appendChild |
| NEVER hardcode plugin names or affiliate links in tool HTML | All plugin recommendations must reference mpw_affiliates.py — one approval, one file update, all tools update |
| NEVER run mpw_writer.py for new article batches before updating drawer HTML | Current writer outputs old vertical list — new grid-style drawer confirmed on all 526 articles must be frozen into writer first |
| NEVER run mpw_bible_writer.py for new T1 entries before updating read time | 500 wpm confirmed wrong — 650 wpm is the standard — must be updated before next batch |


---

# SESSION 65 UPDATE — SCRIPTS (Part 2) — May 24, 2026

## mpw_tools_v6_writer.py — Architecture Update

Full architecture confirmed in session65_scripts_append.md. Additional detail from this session:

### New Tool Categories Requiring Writer Updates

The v6 writer must handle three distinct tool types that were not in the original spec:

**Type A — Standard Calculator Tools (majority of 148 tools)**
Same architecture as existing v5 tools: two-pass JSON spec then HTML/JS. Canvas drawing, createElement chains, genre selectors, plugin tier cards, famous presets, live warning logic.

**Type B — AI-Powered Tools (AI Music category and Mix Diagnostic)**
These tools call the Anthropic API on the client side. The writer generates the tool HTML/JS with the API call baked in. The system prompt for each tool is frozen in the writer. These tools reason, not just calculate.

Key pattern:
```javascript
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    messages: [{role: "user", content: userInput}]
  })
});
```

Note: API key is handled by the artifact infrastructure — writer does NOT hardcode API keys.

**Type C — Decision Tree / Rights Tools (AI Music legal tools, Should I Sample This)**
These are logic-tree tools, not calculators. Input flows through a structured decision tree and outputs a risk level, recommendation, and next steps. Writer generates the JS decision tree from a structured data spec.

### Browser App Scripts — NOT Python Writer

Browser Apps (Priority 0) are built directly in Claude sessions, not via the Python writer. They are:
- Committed directly to `/tools/[slug].html` via GitHub API
- Not batch-generated
- Built interactively with Steve reviewing design in real time
- Each gets a dedicated session or half-session

**Browser App build checklist (apply to every app):**
- [ ] No innerHTML anywhere (Netlify CSP)
- [ ] SC constant for closing script tags if Python is involved (N/A for direct builds)
- [ ] Mobile-responsive (test at 375px width)
- [ ] Web Audio API: audio context created on user gesture (not on page load — browsers block autoplay)
- [ ] getUserMedia: graceful fallback if user denies microphone
- [ ] Tone.js imported via CDN: `https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js`
- [ ] Canvas: CSS `width:100%;height:Xpx` not inline width/height attributes
- [ ] Works on mobile (touch events, not just mouse events)
- [ ] Verified in Chrome, Firefox, Safari before commit
- [ ] Added to `/tools/index.html` tool card grid after commit

### Tone.js CDN — Confirmed Available

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

This is the version available via cdnjs.cloudflare.com and confirmed importable in Claude's artifact environment. All Browser App builds use this version.

### MIDI Writer JS — For Chord Progression Builder

```html
<script src="https://cdn.jsdelivr.net/npm/midi-writer-js@2.1.4/build/midi-writer-browser.js"></script>
```

Enables MIDI file export from the Chord Progression Builder app. Produces standard MIDI files the user can drag directly into any DAW.

---

## Browser DAW — Session 66 Build Plan

### Goal
A fully functional, playable browser DAW. Opens on page load, no setup, works on mobile. Producers can make actual music immediately.

### Tech Stack
- **Tone.js** — drum synthesis, melodic synth, transport/scheduling
- **Canvas API** — step grid visualization, VU meter, waveform display
- **Web Audio API** — effects chain (reverb, delay)
- **Pure vanilla JS** — all UI interaction (no frameworks)

### Session 66 Build Order
1. Start with drum sequencer only — 16 steps, 4 tracks (kick, snare, hi-hat, clap), working playback
2. Add melodic synth + piano roll (16 steps, 2 octaves)
3. Add effects (reverb send, delay send) per track
4. Add preset patterns (trap, house, boom-bap, techno, afrobeats)
5. Add tempo control + tap tempo
6. Polish: animations, VU meter, visual pulse on beat 1
7. Steve visual review → design feedback → final adjustments
8. Commit to `/tools/browser-daw.html` via GitHub API
9. Add tool card to `/tools/index.html`
10. Update sitemap

### What NOT to Build in Session 66
- Sample/audio file upload (Tier 2 — $2k–$5k developer)
- MIDI keyboard input (Tier 2)
- WAV export (Tier 2)
- Saved projects (Tier 2)
- More than 8 tracks (keep MVP clean)

### Audio Context Warning
```javascript
// CORRECT — create AudioContext on user gesture
document.getElementById('playBtn').addEventListener('click', async () => {
  await Tone.start(); // requires user gesture — browsers block autoplay
  // now safe to play audio
});
```

This is the most common mistake in Web Audio API development. The AudioContext must be started (or resumed) in response to a user gesture — click, tap, keypress. Never auto-play on page load. Claude must always include this pattern.

---

## AI Music Tools — Writer Notes

When `mpw_tools_v6_writer.py` generates AI Music tools, the system prompt for each tool's Anthropic API call must be frozen in the Python writer, not improvised at generation time.

**Example for AI #1 — Rights Navigator:**
```python
AI_RIGHTS_NAVIGATOR_SYSTEM = """You are the definitive authority on AI music commercial rights in 2026. 
You know the current terms of service for Suno (free vs Pro vs Premier), Udio, Stable Audio, AIVA, and ElevenLabs.
You know the DDEX AI disclosure requirements now enforced by Spotify and Apple Music.
You know the US Copyright Office's position on AI-generated music (Thaler v. Perlmutter).
You know which distributors accept AI music (DistroKid yes, some others no).
You know that fully AI-generated audio is not eligible for Content ID as of 2026.
Given the user's platform, tier, and intended use, output a clear yes/no/risk assessment 
with the specific reason for each use case. Be specific, not generic. Cite the platform's 
current terms where relevant. Flag the DDEX disclosure requirement when it applies."""
```

Every AI music tool that calls the Anthropic API must have its system prompt frozen in the writer at spec time. The system prompt defines the quality ceiling.

---

## Scripts to Build — Session 66 and Beyond

**Session 66 — Browser DAW (direct build, no Python writer):**
- Build `/tools/browser-daw.html` directly in session with Claude
- Update `/tools/index.html` to add Browser DAW card
- Update sitemap.xml

**Session 67 — Browser Apps batch:**
- Build APP #2–5 (Spectrum Analyzer, Chord Explorer, Ear Trainer, Tuner)
- Each committed individually as `/tools/[slug].html`
- `/tools/index.html` updated after each confirmed live

**Session 68 — Writer build:**
- Build `mpw_tools_v6_writer.py`
- First batch: Priority 1 tools #1–7 (viral tier)
- Also update `mpw_writer.py` with new drawer HTML (blocks article batches)

**Session 69+ — Continued writer batches:**
- AI Music tools AI #1–10 (rights and prompt tools first)
- Priority 1 completion #8–15
- Priority 2 batch

---

## NEVER Rules Added — Session 65 Part 2 — Scripts

| Rule | Detail |
|------|--------|
| NEVER autoplay audio on page load in Browser Apps | AudioContext must be started in response to a user gesture — `await Tone.start()` inside click/tap handler — browsers block autoplay globally |
| NEVER hardcode system prompts for AI-powered tools in the generated HTML | System prompts must be frozen in the Python writer at spec time, not generated by the tool's Anthropic API call itself |
| NEVER build Browser App tools via the Python writer batch system | Browser Apps require interactive design review with Steve — they are direct Claude-in-session builds, not batch output |
| NEVER import Tone.js from a version not confirmed available on cdnjs.cloudflare.com | Only use `https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js` — other versions or sources may not be available from Netlify |
| NEVER add a Browser App to /tools/index.html before it is confirmed live on GitHub | Check the live URL before updating the hub page card grid |


---

# SESSION 66 UPDATE — SCRIPTS — May 25, 2026

## MPW-TOOL-BUILD-SPEC.md — Parallel Session Protocol

The most important new "script" from Session 66 is not Python — it is the frozen spec
document that coordinates parallel Claude sessions. Every session building tools loads
this file first and treats it as ground truth.

### How to Start a Parallel Tool-Build Session

Every parallel session begins with these exact steps:

1. Load `MPW-TOOL-BUILD-SPEC.md` from GitHub
2. Confirm the tool slug is in the 25-tool queue and not already built
3. Check `/tools/index.html` to confirm the slug does not already exist as a card
4. Build the tool using the frozen CSS/component system from the spec
5. Commit to GitHub via direct PUT API (single file — individual PUT is OK for one file)
6. In the SAME commit, add the tool card to `/tools/index.html` using Trees API
7. Report back to Steve: live URL, SHA, tool name confirmed

### GitHub Commit Pattern — Single Tool

For a single tool file commit (use individual PUT, not Trees API):

```python
import requests, base64

TOKEN = "[GITHUB_TOKEN_FROM_SETENV]"
HEADERS = {"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
BASE = "https://api.github.com/repos/musicproductionwiki/musicproductionwiki"

with open('/home/claude/[tool-slug].html', 'r') as f:
    content = f.read()

# Check if file exists (to get SHA for update)
r = requests.get(f"{BASE}/contents/tools/[tool-slug].html", headers=HEADERS)
sha = r.json().get('sha') if r.status_code == 200 else None

payload = {
    "message": "tools: add [Tool Name] — [brief description]",
    "content": base64.b64encode(content.encode('utf-8')).decode('ascii'),
}
if sha:
    payload["sha"] = sha

r2 = requests.put(f"{BASE}/contents/tools/[tool-slug].html", headers=HEADERS, json=payload)
result = r2.json()
print(f"SHA: {result['commit']['sha']}")
print(f"URL: https://www.musicproductionwiki.com/tools/[tool-slug].html")
```

### GitHub Commit Pattern — Tool + Index Update (Trees API)

When updating `/tools/index.html` at the same time (required for every tool):

```python
import requests, base64

TOKEN = "[GITHUB_TOKEN_FROM_SETENV]"
HEADERS = {"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
BASE = "https://api.github.com/repos/musicproductionwiki/musicproductionwiki"

# Read both files
with open('/home/claude/[tool-slug].html', 'r') as f:
    tool_content = f.read()
with open('/home/claude/tools-index-updated.html', 'r') as f:
    index_content = f.read()

# Get current main SHA
main_sha = requests.get(f"{BASE}/git/refs/heads/main", headers=HEADERS).json()['object']['sha']

# Create blobs
files = {
    f"tools/[tool-slug].html": tool_content,
    "tools/index.html": index_content,
}
new_tree = []
for path, content in files.items():
    blob = requests.post(f"{BASE}/git/blobs", headers=HEADERS, json={
        "content": base64.b64encode(content.encode('utf-8')).decode('ascii'),
        "encoding": "base64"
    }).json()['sha']
    new_tree.append({"path": path, "mode": "100644", "type": "blob", "sha": blob})

# Create tree, commit, update ref
tree_sha = requests.post(f"{BASE}/git/trees", headers=HEADERS, json={
    "base_tree": main_sha, "tree": new_tree
}).json()['sha']

commit_sha = requests.post(f"{BASE}/git/commits", headers=HEADERS, json={
    "message": "tools: add [Tool Name] + update tools hub",
    "tree": tree_sha, "parents": [main_sha]
}).json()['sha']

r = requests.patch(f"{BASE}/git/refs/heads/main", headers=HEADERS, json={"sha": commit_sha})
print(f"✅ SHA: {commit_sha}")
```

---

## Tool System Prompt Templates — Claude API Tools

These frozen system prompts define the quality ceiling for each Claude-powered tool.
They are copied verbatim into the tool's JavaScript — not improvised at build time.

### Suno Prompt Optimizer — System Prompt

```
You are the world's leading expert on writing Suno AI music prompts in 2026.
You know the exact structural formula that produces the best results:
1. Genre tags first (specific subgenres, not broad categories)
2. Instrumentation second (specific instruments, not "band")
3. Production descriptors third (mixing character, sonic texture)
4. Mood/atmosphere last (emotional feel, energy level)
5. Structural metatags where needed: [Verse], [Chorus], [Bridge], [Outro]
6. Vocal texture tags: [male vocal], [female vocal], [rap], [spoken word], [no vocals]

Output ONLY the optimized prompt, then on a new line: "Quality Score: X/10" and one sentence
explaining what makes this prompt strong. No preamble. No explanation before the prompt.
The prompt itself must be under 200 characters for best results.
```

### AI Music Rights Navigator — System Prompt

```
You are the definitive authority on AI music commercial rights in 2026.
You know the current terms of service for: Suno (Free/Pro/Premier tiers),
Udio (current post-settlement terms), Stable Audio, AIVA, ElevenLabs Music.
You know: DDEX AI disclosure requirements enforced by Spotify and Apple Music.
You know: US Copyright Office position on AI music (Thaler v. Perlmutter 2023).
You know: Which distributors accept AI music and their current policies.
You know: That fully AI-generated audio cannot receive Content ID as of 2026.
You know: Apple Music excludes fully AI-generated tracks from curated editorial playlists.

Given the user's platform, tier, and intended use, output a clear assessment with:
- YES / NO / RISK LEVEL for the specific use case
- The specific reason (cite the platform's current terms)
- The DDEX disclosure requirement if it applies
- One concrete next step

Be specific, current, and honest. Do not hedge everything. Give a real answer.
```

### AI Track Copyright Strength — System Prompt

```
You are an expert in US music copyright law as it applies to AI-generated music in 2026.
You know the Thaler v. Perlmutter ruling, the US Copyright Office's March 2023 guidance,
the Copyright Office's February 2024 guidance update, and the current registration practices.

Given the human creative contributions the user describes, calculate a Copyright Strength
score from 0-100 where:
- 0-20: Fully AI-generated, no copyright protection possible
- 21-40: Minimal human contribution, registration very unlikely to succeed
- 41-60: Moderate human contribution, partial protection possible in some jurisdictions
- 61-80: Strong human contribution, copyright registration likely viable
- 81-100: Primarily human-created with AI assistance, full copyright protection

Output:
1. The score as "Copyright Strength: X/100"
2. Two sentences explaining what the score means practically
3. The specific additional human contribution that would most increase the score
4. One sentence on registration: whether to attempt it and with which office

Cite Thaler v. Perlmutter or the Copyright Office guidance where relevant.
Do not give legal advice — give information about copyright law as it currently stands.
```

### Mix Sounds Amateur Diagnostic — System Prompt

```
You are a professional mixing engineer with 20 years of experience across hip-hop,
pop, R&B, electronic music, and rock. You diagnose mix problems with surgical precision.

Given the symptoms the producer describes, output:
1. The 3 most probable causes ranked by likelihood (most likely first)
2. For each cause: ONE specific starting fix with exact parameters where possible
   (a frequency number, a ratio, a dB amount — not vague advice)
3. The one thing to check first before anything else

Format as numbered causes with their fixes. Be direct. No preamble.
Examples of good fixes: "HPF the room mics at 120Hz" not "EQ the low end"
"Cut 3dB at 350Hz on the guitar" not "reduce the muddy frequencies"
"Set attack to 30ms to let the transient through" not "adjust the attack"
```

### Vocal Sitting Wrong Fixer — System Prompt

```
You are a specialist vocal mixing engineer. You have mixed vocals for major label releases
across hip-hop, pop, R&B, and singer-songwriter genres.

Given the specific symptom the producer describes about their vocal, diagnose the root cause
and provide exact fixes. Distinguish clearly between:
- EQ problems (frequency issues)
- Dynamics problems (compression, limiting, de-essing)
- Space problems (reverb, delay, pre-delay)
- Level problems (volume, automation)
- Arrangement problems (other elements clashing with the vocal)

Output the 3 most likely causes ranked by probability, with a specific fix for each.
Include exact parameter values where possible. No vague advice.
```

---

## mpw_writer.py — Pending Updates

The following changes are REQUIRED in mpw_writer.py before the next article batch.
These have been pending since Session 65 and are blocking article production.

### Update 1 — Mobile drawer: replace vertical list with grid style

The current writer produces the old vertical mobile drawer. It must produce the new
grid-style drawer that matches the Session 65 patch applied to all 526 article pages.

Grid drawer HTML to use in writer (inline styles for article compatibility):
```html
<div class="mobile-drawer" id="mobileDrawer">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:16px">
    <a href="/tools/" style="background:#0d2d2d;border:1px solid rgba(0,232,162,.25);border-radius:8px;padding:12px;text-decoration:none;display:block">
      <div style="font-size:11px;font-weight:700;color:#00e8a2;letter-spacing:.08em">TOOLS →</div>
      <div style="font-size:10px;color:#5a5a7a;margin-top:2px">Free production tools</div>
    </a>
    <a href="/bible/" style="background:#2d1f00;border:1px solid rgba(245,166,35,.25);border-radius:8px;padding:12px;text-decoration:none;display:block">
      <div style="font-size:11px;font-weight:700;color:#f5a623;letter-spacing:.08em">BIBLE →</div>
      <div style="font-size:10px;color:#5a5a7a;margin-top:2px">The Producer's Bible</div>
    </a>
  </div>
  <!-- existing nav links below -->
</div>
```

### Update 2 — Desktop nav: Tools → link

Add Tools → before Bible → in the desktop nav list:
```html
<li class="nav-item"><a href="/tools/" class="nav-tools-link">Tools →</a></li>
```

### Update 3 — CSS specificity fix

Replace any `.nav-bible-link` and `.nav-tools-link` class selectors with:
```css
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-bible-link:hover{background:rgba(245,166,35,.1)!important;color:#f5a623!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link{color:#00e8a2!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link:hover{background:rgba(0,232,162,.08)!important;color:#00e8a2!important}
```

### Update 4 — pushState/popstate back-button fix

Replace replaceState with pushState in the drawer JS:
```javascript
// CORRECT
hamburger.addEventListener('click', function() {
  drawer.classList.toggle('open');
  if (drawer.classList.contains('open')) {
    history.pushState({drawerOpen: true}, '');
  }
});
window.addEventListener('popstate', function(e) {
  if (drawer.classList.contains('open')) {
    drawer.classList.remove('open');
  }
});
// WRONG — do not use replaceState here
```

---

## mpw_bible_writer.py — Pending Updates

### Update 1 — Read time calculation

Change from 500 wpm to 650 wpm for read time calculation.
Bible entries average 5,000+ words — at 500wpm this shows unrealistically high read times.
650wpm is the correct rate for scanning/reference reading.

### Update 2 — Nav rewrite

Same four changes as mpw_writer.py above. The Bible writer's nav must match:
- Grid mobile drawer
- Tools → in desktop nav
- CSS specificity fix
- pushState/popstate

### Update 3 — Bible entry bmn-drawer

The 222 Bible entry pages also need their mobile drawers updated (the bmn-drawer).
This is a separate batch injection script — NOT the bible writer. Pending after writer fix.
The bmn-drawer currently lacks the Production, Recording, and Tools categories.

---

## Session Assignment for Parallel Tool Builds

When Steve opens parallel sessions, each session receives this instruction:

```
You are building MPW tools for MusicProductionWiki.com.

STEP 1: Load the frozen spec by reading MPW-TOOL-BUILD-SPEC.md from:
https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/MPW-TOOL-BUILD-SPEC.md
Use the GitHub token: [GITHUB_TOKEN_FROM_SETENV]

STEP 2: Build [TOOL NAME] at slug [TOOL SLUG] using the frozen CSS and component system
from the spec. The tool must match the quality of the live Frequency Conflict Detector
at musicproductionwiki.com/tools/frequency-conflict-detector.

STEP 3: Commit the tool to GitHub at tools/[slug].html and update tools/index.html
with the new tool card in the same commit.

STEP 4: Report back: live URL, commit SHA, and confirm it renders correctly.

The 25 tools are listed in MPW-TOOL-BUILD-SPEC.md. Your assigned tools are:
[Session A: tools 1-3] [Session B: tools 4-7] [Session C: tools 8-11] [Session D: tools 12-14]
[Session E: tools 15-18] [Session F: tools 19-22] [Session G: tools 23-25]
```

---

## NEVER Rules Added — Session 66 — Scripts

| Rule | Detail |
|------|--------|
| NEVER start a parallel tool session without loading MPW-TOOL-BUILD-SPEC.md first | The spec is what keeps output consistent across sessions |
| NEVER use replaceState in mobile drawer JS on tool pages | Use pushState + popstate — replaceState was confirmed non-functional for back-button fix |
| NEVER commit a tool without also updating /tools/index.html | Always Trees API for 2+ files — single Netlify deploy |
| NEVER run mpw_writer.py for new article batches until the 4 pending updates are applied | Grid drawer + Tools nav + CSS specificity + pushState — all 4 required |
| NEVER run mpw_bible_writer.py until read time is updated to 650wpm and nav is fixed | Both changes required before next Bible batch |


---

# SESSION 67 UPDATE — SCRIPTS — May 25, 2026

## Tool Commit Pattern — Trees API (Required for Every Tool)

```python
import requests, base64, json

TOKEN = "[GITHUB_TOKEN]"
HEADERS = {"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
BASE = "https://api.github.com/repos/musicproductionwiki/musicproductionwiki"

def get_file(path):
    r = requests.get(f"{BASE}/contents/{path}", headers=HEADERS).json()
    return base64.b64decode(r['content']).decode('utf-8')

def commit_files(files_dict, message):
    main_sha = requests.get(f"{BASE}/git/refs/heads/main", headers=HEADERS).json()['object']['sha']
    new_tree = []
    for path, content in files_dict.items():
        blob = requests.post(f"{BASE}/git/blobs", headers=HEADERS, json={
            "content": base64.b64encode(content.encode('utf-8')).decode('ascii'),
            "encoding": "base64"
        }).json()['sha']
        new_tree.append({"path": path, "mode": "100644", "type": "blob", "sha": blob})
    tree_sha = requests.post(f"{BASE}/git/trees", headers=HEADERS, json={
        "base_tree": main_sha, "tree": new_tree
    }).json()['sha']
    commit_sha = requests.post(f"{BASE}/git/commits", headers=HEADERS, json={
        "message": message, "tree": tree_sha, "parents": [main_sha]
    }).json()['sha']
    r = requests.patch(f"{BASE}/git/refs/heads/main", headers=HEADERS, json={"sha": commit_sha})
    print(f"✅ {r.status_code} — {commit_sha}")
    return commit_sha
```

---

## Full Tool Deployment Sequence

For every new tool, in order:

### Step 1 — Build the HTML
- Follow MPW-TOOL-BUILD-SPEC.md design system
- Use `claude-sonnet-4-6` model  *(S67 had wrong string — corrected S71)*
- Call `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy`
- Include favicon, MPW nav, site footer, embed mode, all SEO

### Step 2 — Update tools/index.html
```python
idx = get_file('tools/index.html')
new_card = '''
    <a class="tool-card" href="/tools/[slug].html" data-cat="ai-music" data-name="[searchable terms]">
      <div class="tool-card-body">
        <span class="tool-card-name">[Tool Name]</span>
        <span class="tool-card-desc">[One sentence, 12 words max]</span>
        <span class="tool-card-cat">AI Music</span>
      </div>
      <span class="tool-card-arrow">&rarr;</span>
    </a>'''
# Insert before <!-- no-results placeholder --> or at end of grid
# Update count: '38 free music production tools' → '39 free...'
```

### Step 3 — Update bible/categories/tools/index.html
```python
btools = get_file('bible/categories/tools/index.html')
new_card = '<a class="bcat-card" href="/tools/[slug].html"><div class="bcat-card-inner"><span class="bcat-card-term">[Tool Name]</span><span class="bcat-card-cat">AI Music</span></div><span class="bcat-card-arrow">→</span></a>'

# CRITICAL: Insert INSIDE #catGrid, BEFORE closing </div>
close_pattern = '→</span></a>\n  </div>\n  <div class="bcat-empty"'
insert_point = btools.rfind(close_pattern) + len('→</span></a>')
btools = btools[:insert_point] + '\n' + new_card + btools[insert_point:]

# Verify: grid_open < new_card_pos < catEmpty_pos
grid_open = btools.find('id="catGrid">')
card_pos = btools.find('/tools/[slug].html')
empty_pos = btools.find('id="catEmpty"')
assert grid_open < card_pos < empty_pos, "Card not inside grid!"
```

### Step 4 — Update sitemap.xml
```python
import re
from datetime import date
sitemap = get_file('sitemap.xml')
new_url = f'  <url><loc>https://www.musicproductionwiki.com/tools/[slug].html</loc><lastmod>{date.today().isoformat()}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
sitemap = sitemap.replace('</urlset>', new_url + '\n</urlset>')
```

### Step 5 — Update search-index.json
```python
si = json.loads(get_file('search-index.json'))
si.append({
    "slug": "tools/[slug]",
    "title": "[Tool Name]",
    "category": "Tools",
    "description": "[One sentence description for search results]"
})
```

### Step 6 — Commit all 5 files in one Trees API commit
```python
commit_files({
    'tools/[slug].html': tool_html,
    'tools/index.html': idx,
    'bible/categories/tools/index.html': btools,
    'sitemap.xml': sitemap,
    'search-index.json': json.dumps(si, ensure_ascii=False),
}, "tools: add [Tool Name] — fully mapped to hub, bible, sitemap, search")
```

---

## Sitemap Pending
Two URLs added this session — Steve to submit in GSC:
- `https://www.musicproductionwiki.com/tools/suno-prompt-optimizer.html`
- `https://www.musicproductionwiki.com/tools/ai-music-rights-navigator.html`

---

## NEVER Rules — Session 67 — Scripts

| Rule | Detail |
|------|--------|
| NEVER commit a tool without all 5 files in same commit | Tool + tools/index.html + bible/categories/tools + sitemap.xml + search-index.json |
| NEVER insert into catGrid without assertion check | grid_open < card_pos < empty_pos — assert it |
| NEVER skip sitemap after tool build | Tools are not indexable without sitemap entry |
| NEVER forget search-index.json | Site search won't find the tool without it |


---

# SESSION 68 UPDATE — SCRIPTS — May 26, 2026

## Nav Block Extractor (Div-Depth Balanced)

Use this every time you need the nav block from a reference tool. Never use naive `find()`.

```python
import urllib.request, json, base64

def get_nav_block(slug='ai-music-rights-navigator.html'):
    TOKEN = '[GITHUB_TOKEN — stored in Netlify env vars, regenerate at github.com/settings/tokens if expired]'
    headers = {'Authorization':f'token {TOKEN}','User-Agent':'MPW'}
    req = urllib.request.Request(
        f'https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/tools/{slug}',
        headers=headers
    )
    with urllib.request.urlopen(req) as r: data = json.loads(r.read())
    html = base64.b64decode(data['content']).decode('utf-8', errors='replace')

    nav_start = html.find('<div class="mpw-nav-wrap">')
    if nav_start == -1:
        raise ValueError("mpw-nav-wrap not found")

    # Div-depth tracking — guaranteed balanced
    depth = 0
    pos = nav_start
    end = nav_start
    while pos < len(html):
        open_m = html.find('<div', pos)
        close_m = html.find('</div>', pos)
        if open_m == -1: open_m = len(html)
        if close_m == -1: close_m = len(html)
        if open_m < close_m:
            depth += 1; pos = open_m + 4
        else:
            depth -= 1; pos = close_m + 6; end = pos
            if depth == 0: break

    nav_block = html[nav_start:end]

    # Validate balance
    opens = nav_block.count('<div')
    closes = nav_block.count('</div>')
    assert opens == closes, f"Nav unbalanced: {opens} opens, {closes} closes"
    print(f"Nav block: {len(nav_block)} chars, {opens} divs balanced")
    return nav_block
```

---

## JS Syntax Checker

Run before embedding any JS in HTML.

```python
import subprocess

def check_js(filepath):
    r = subprocess.run(['node', '--check', filepath], capture_output=True, text=True)
    if r.returncode == 0:
        print(f"✓ {filepath}: syntax OK")
        return True
    else:
        print(f"✗ {filepath}: SYNTAX ERROR")
        print(r.stderr[:500])
        return False
```

---

## GitHub Restore Script

Restore any file to a previous commit SHA.

```python
import urllib.request, json, base64

def restore_file(filepath, restore_sha, token):
    headers = {'Authorization':f'token {token}','User-Agent':'MPW'}

    # Get content at historical commit
    req = urllib.request.Request(
        f'https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/{filepath}?ref={restore_sha}',
        headers=headers
    )
    with urllib.request.urlopen(req) as r: data = json.loads(r.read())
    content = data['content']  # already base64

    # Get current SHA
    req2 = urllib.request.Request(
        f'https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/{filepath}',
        headers=headers
    )
    with urllib.request.urlopen(req2) as r: cur = json.loads(r.read())
    current_sha = cur['sha']

    # Commit restore
    body = json.dumps({
        'message': f'revert: restore {filepath} to {restore_sha}',
        'content': content,
        'sha': current_sha
    }).encode()
    req3 = urllib.request.Request(
        f'https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/{filepath}',
        data=body,
        headers={**headers, 'Content-Type':'application/json'},
        method='PUT'
    )
    with urllib.request.urlopen(req3) as r: result = json.loads(r.read())
    print(f"Restored: {result['content']['sha']}")
```

---

## Tool Build Pre-Commit Checklist Script

```python
import re, subprocess

def verify_tool(filepath):
    with open(filepath) as f: html = f.read()
    errors = []

    # Div balance
    if html.count('<div') != html.count('</div>'):
        errors.append(f"Unbalanced divs: {html.count('<div')} opens, {html.count('</div>')} closes")

    # No style.css
    if 'style.css' in html:
        errors.append("style.css must NOT be loaded in tool pages")

    # Model string
    if 'claude-sonnet-4-6' not in html:
        errors.append("Wrong or missing model string — must be claude-sonnet-4-6")

    # Proxy URL
    if 'classy-haupia-be8e43' not in html:
        errors.append("Missing proxy URL")

    # GA4
    if 'G-79VB543KCT' not in html:
        errors.append("Missing GA4 tag")

    # JS syntax
    scripts = re.findall(
        r'<script(?![\s\S]{0,10}(?:async|ld\+json|src=))[^>]*>([\s\S]+?)</script>',
        html
    )
    for i, s in enumerate(scripts):
        with open(f'/tmp/verify_{i}.js','w') as f2: f2.write(s)
        r = subprocess.run(['node','--check',f'/tmp/verify_{i}.js'], capture_output=True, text=True)
        if r.returncode != 0:
            errors.append(f"Script block {i} syntax error: {r.stderr[:200]}")

    # File size
    size = len(html.encode())
    if size > 200000:
        errors.append(f"File too large: {size:,} bytes (Cloudflare limit: 200KB)")

    if errors:
        print(f"FAILED — {len(errors)} errors:")
        for e in errors: print(f"  ✗ {e}")
        return False
    else:
        print(f"ALL CHECKS PASSED — {size:,} bytes ({size/1024:.1f}KB)")
        return True
```


---

## Pre-Upload Token Redaction Scan

**Run this before uploading ANY file to GitHub — handoffs, scripts, HTML, everything.**

```python
import re, sys

SENSITIVE_PATTERNS = [
    r'ghp_[A-Za-z0-9]{36}',           # GitHub personal access token
    r'sk-ant-[A-Za-z0-9\-]{90,}',     # Anthropic API key
    r'AKIA[A-Z0-9]{16}',               # AWS access key
]

def scan_for_secrets(filepath):
    with open(filepath) as f: content = f.read()
    found = []
    for pattern in SENSITIVE_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            found.extend(matches)
    if found:
        print(f"SECRETS FOUND in {filepath} — DO NOT UPLOAD:")
        for m in found: print(f"  {m[:12]}... [REDACT BEFORE UPLOADING]")
        return False
    print(f"✓ {filepath}: no secrets found")
    return True
```

**NEVER rule:** Always run this scan before `gh_put()`. If it finds anything, redact to `[GITHUB_TOKEN]` or `[ANTHROPIC_API_KEY]` first.



---

# ⛔ SESSION 78 UPDATE — May 27, 2026

## State at End of Session 78
- No new Python scripts written this session
- All session work was direct HTML/CSS/JS editing of bible/compression.html via GitHub Trees API

## New Canonical Script Patterns (S78)

### Trees API Single-File Bible Entry Commit Pattern
Used every time a Bible entry is updated:
```python
import json, base64, urllib.request

TOKEN = '[GITHUB_TOKEN]'
OWNER = 'musicproductionwiki'
REPO  = 'musicproductionwiki'
BRANCH = 'main'

with open('local_file.html', 'r', encoding='utf-8') as f:
    content = f.read()

def gh(path, method='GET', body=None):
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/{path}'
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json',
        'User-Agent': 'mpw-fix',
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

ref    = gh(f'git/ref/heads/{BRANCH}')
head   = ref['object']['sha']
base_t = gh(f'git/commits/{head}')['tree']['sha']

b64  = base64.b64encode(content.encode('utf-8')).decode('ascii')
blob = gh('git/blobs', 'POST', {'content': b64, 'encoding': 'base64'})
tree = gh('git/trees', 'POST', {
    'base_tree': base_t,
    'tree': [{'path': 'bible/compression.html', 'mode': '100644', 'type': 'blob', 'sha': blob['sha']}]
})
commit = gh('git/commits', 'POST', {
    'message': 'commit message here',
    'tree': tree['sha'],
    'parents': [head]
})
gh(f'git/refs/heads/{BRANCH}', 'PATCH', {'sha': commit['sha']})
print(f'Done — SHA: {commit["sha"]}')
```

### Share Bar Python Builder Pattern
Used when injecting share bars into Bible HTML via Python:
```python
X_SVG = '<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.26 5.632 5.905-5.632zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'
R_SVG = '<svg width="12" height="12" viewBox="0 0 20 20" fill="currentColor">...</svg>'

def make_share(anchor, label, tweet, copy_label='Copy Link'):
    url = f'https://musicproductionwiki.com/bible/compression#{anchor}'
    ue = url.replace(':', '%3A').replace('/', '%2F').replace('#', '%23')
    te = tweet.replace(' ', '+').replace("'", '%27').replace('—', '%E2%80%94')
    cjs = f"(function(b){{navigator.clipboard.writeText('{url}').then(function(){{b.textContent='Copied!';setTimeout(function(){{b.textContent='{copy_label}'}},2000);}})}})(this)"
    return (f'<div class="mpw-share-bar" style="margin-top:20px">'
            f'<span class="mpw-share-label">{label}</span>'
            f'<div class="mpw-share-btns">'
            f'<button class="mpw-share-btn share-copy" onclick="{cjs}">{copy_label}</button>'
            f'<a href="https://x.com/intent/tweet?text={te}&url={ue}" target="_blank" rel="noopener" class="mpw-share-btn share-x">{X_SVG}Share on X</a>'
            f'<a href="https://www.reddit.com/submit?url={ue}&title={te}" target="_blank" rel="noopener" class="mpw-share-btn share-reddit">{R_SVG}Reddit</a>'
            f'</div>'
            f'</div>')
```

### div-depth Share Bar Finder Pattern
Used to find and replace existing share bars by anchor URL:
```python
def replace_share_bar_by_anchor(content, find_anchor, new_bar):
    idx = content.find(f'compression{find_anchor}')
    if idx == -1:
        return content, False
    bar_start = content.rfind('<div class="mpw-share-bar', 0, idx)
    if bar_start == -1:
        return content, False
    depth = 0
    i = bar_start
    while i < len(content):
        if content[i:i+4] == '<div':
            depth += 1
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                bar_end = i + 6
                break
        i += 1
    return content[:bar_start] + new_bar + content[bar_end:], True
```

## S78 Scripts Used
All S78 work was done via inline Python in Claude's bash environment — no standalone .py scripts delivered. Patterns above are the canonical reference for future sessions.

## Script File State — End of Session 78
All scripts on Steve's machine unchanged from end of Session 77. No new PS1 scripts delivered this session.

---

# `mpw_flagship_writer.py` — Build Brief

## What This Script Does

Generates all 40 Tier 1 flagship Bible entries at compression.html quality via 3-pass architecture. Each entry is generated in ~3 minutes. Parallel sessions produce 40 entries in one week.

## Input

```powershell
. .\setenv.ps1
python mpw_flagship_writer.py --batch-file flagships_wave1.txt --workers 4
```

Batch file format (one per line):
```
eq:EQ:Frequency:1
gain-staging:Gain Staging:Signal Processing:1
delay:Delay:Time-Based:1
limiting:Limiting:Dynamics:1
saturation:Saturation:Signal Processing:1
```

## Script Structure

```python
mpw_flagship_writer.py
├── LOCKED_TEMPLATES{}         # All verbatim blocks from compression.html
│   ├── SHARE_CSS              # 742 chars — exact from live file
│   ├── GENRE_CSS              # 1,342 chars — exact from live file  
│   ├── NAV_JS                 # 939 chars — exact IIFE
│   ├── FIXIT_JS               # 670 chars — exact function
│   ├── CITATION_TEMPLATE      # 7,320 chars — slug/title/date vars only
│   ├── CHANGELOG_TEMPLATE     # 4,239 chars — slug/title/date/version vars only
│   ├── FOOTER_TEMPLATE        # 2,248 chars — slug/title vars only
│   ├── EMBED_TEMPLATE         # 1,777 chars — slug/tool-name vars only
│   ├── WTRN_TEMPLATE          # Per-entry — 6 cards hardcoded per slug
│   └── SIDEBAR_SHARE_TEMPLATE # 2,062 chars — slug vars only
│
├── WTRN_CARDS{}               # Per-slug What to Read Next cards
│   ├── 'eq': [6 card dicts]
│   ├── 'gain-staging': [6 card dicts]
│   └── ... (all 40 slugs)
│
├── GENRE_COLUMNS{}            # Per-slug genre table column headers
│   ├── 'eq': ['Genre','Key Frequencies','Move','Q','Character','Notes']
│   ├── 'compression': ['Genre','Ratio','Attack','Release','GR Target','Character']
│   └── ... (all 40 slugs)
│
├── pass1_discovery(slug, term, category)  # API call → JSON
├── pass2_prose(slug, term, p1_json)       # API call → JSON
├── pass3_assemble(slug, term, p1, p2)     # Python → full HTML
├── validate(html, slug)                   # 90-point checklist → bool
├── commit(slug, html)                     # Trees API → SHA
└── run_batch(batch_file, workers)         # Parallel execution
```

## Pass 1 System Prompt (exact)

```
You are the editorial director of The Producer's Bible at MusicProductionWiki.com.

Your job is to find the non-obvious central insight about {term} — the one thing every producer thinks they understand about this topic but fundamentally doesn't.

CRITICAL: The central insight must be:
- Specific to {term} only — it cannot apply to any other entry
- Non-obvious — not the definition, not the Wikipedia answer
- Reframing — it makes the reader pause and think differently
- Actionable — a producer can immediately apply it in a DAW session

REJECT these as central insights:
- Anything that uses "balance," "tone," or "control" without specifics
- Anything that could appear in the Wikipedia article on {term} unchanged
- Anything that applies to more than one term in music production

EXAMPLES OF ACCEPTED CENTRAL INSIGHTS:
- Compression: "Compression is a time tool, not a level tool — it controls when energy arrives, not how much."
- EQ: "EQ is a spatial tool masquerading as a corrective one — every cut creates distance, every boost creates presence."
- Limiting: "A limiter is not a safety net — it is a decision about what information you are willing to destroy."
- Reverb: "Reverb is not an effect — it is the room the listener believes they are standing in."

Return ONLY valid JSON. No preamble. No markdown. No explanation.
```

## Pass 1 User Prompt (exact)

```
Term: {term}
Slug: {slug}
Category: {category}
Available producer quote authors for this entry: {available_authors_for_slug}

Return the discovery JSON for this entry. Central insight first — if it is generic, the entire entry fails.
```

## Pass 1 Central Insight Validation

```python
def validate_central_insight(insight, term, slug):
    """Returns (pass, reason)"""
    generic_words = ['balance', 'control', 'tone', 'adjust', 'affect', 'impact']
    if any(w in insight.lower() for w in generic_words):
        return False, f"Generic word found: {[w for w in generic_words if w in insight.lower()]}"
    if len(insight) < 60:
        return False, "Too short — not specific enough"
    if term.lower() not in insight.lower() and slug not in insight.lower():
        return False, "Insight doesn't reference the term — probably generic"
    return True, "PASS"
```

Max 2 retries on fail. On 3rd fail: write to `flagships_review_needed.txt` and skip to next entry.

## Pass 2 System Prompt (exact)

```
You are the senior editor of The Producer's Bible at MusicProductionWiki.com.

The central insight for this entry is: {central_insight}

Every section you write must serve this insight. A producer who reads only the definition should understand the insight. A producer who reads the verdict should feel it confirmed and deepened.

You are writing for three simultaneous readers:
1. Producer with a problem RIGHT NOW — needs the answer in 30 seconds
2. Producer who wants the full picture — theory, history, philosophy
3. Berklee professor who will cite this entry as curriculum material

WRITING LAWS — no exceptions:
1. No hedging. Never "it depends," "generally," "in some cases," "typically."
2. Specific numbers always. Not "boost the highs" — "boost 12kHz by 2dB, Q 0.7, on the vocal bus."
3. Named producers with named gear and named records. Not "some engineers prefer" — "Michael Brauer uses a Neve 8078 to..."
4. The best sentence in every section must be the kind of sentence a producer screenshots and sends to their session partner.
5. The verdict is MPW's authoritative opinion — not a summary. It should be the most opinionated paragraph on the page.
6. The opening hook is the first sentence of the definition. It must be one sentence a producer cannot put down.

Return ONLY valid JSON. No HTML tags anywhere. No markdown. No preamble.
```

## Pass 3 Assembly — Key Functions

```python
def build_share_bar(anchor, label, tweet, slug, copy_label='Copy Link'):
    """Returns complete share bar HTML with mpw-share-btns wrapper"""
    url = f'https://musicproductionwiki.com/bible/{slug}#{anchor}'
    # ... builds full bar from LOCKED_TEMPLATES['SHARE_CSS'] pattern

def build_fixit_accordion(symptoms):
    """Builds complete fix-it section from Pass 1 fixit_symptoms list"""
    # Returns full HTML with 8 .fixit-item blocks

def build_genre_table(rows, columns, slug):
    """Builds CSS grid genre table from Pass 1 genre_rows"""
    # Uses GENRE_COLUMNS[slug] for column headers
    # Returns full .genre-grid-wrap HTML

def build_producer_dna(producers):
    """Builds 3 collapsible DNA cards from Pass 1 producer_dna"""
    # Includes signal chain, signature technique, dnaToggle JS

def build_citation(slug, term, date):
    """Returns citation block with APA/MLA/Chicago/Harvard"""
    # Substitutes into LOCKED_TEMPLATES['CITATION_TEMPLATE']

def build_changelog(slug, term, date, version='1.0', changes=None):
    """Returns version changelog HTML"""
    # v1.0 only at launch — substitutes into LOCKED_TEMPLATES['CHANGELOG_TEMPLATE']

def build_wtrn(slug):
    """Returns What to Read Next block from WTRN_CARDS[slug]"""
    # 6 cards hardcoded per slug — no API call

def build_seo_head(slug, term, category, read_min, pub_date):
    """Returns complete <head> with all SEO tags and 5 JSON-LD blocks"""
    # All 5 schema blocks: Article, FAQPage, BreadcrumbList, HowTo, Speakable
    # Title pattern: f'{term}: [tagline] | The Producer\'s Bible'
    # Canonical: non-www always
```

## Validation Checklist (90 points)

```python
CHECKS = {
    # Structure (25)
    'all_25_sections': all(f'id="{s}"' in html for s in SECTION_IDS),
    'section_h2_present': all(f'id="{s}"' in html and '<h2>' in get_section(html,s) for s in SECTION_IDS),
    # Share bars (8)
    'share_new_producers': 'new-producers' in html and 'mpw-share-btns' in get_after(html,'new-producers'),
    'share_quick_ref': 'quick-reference' in html and 'mpw-share-btns' in get_after(html,'quick-reference'),
    'share_tools': 'tools' in html and 'mpw-share-btns' in get_after(html,'tools'),
    'share_genre': 'genre-table' in html and 'mpw-share-btns' in get_after(html,'genre-table'),
    'share_in_wild': 'in-the-wild' in html and 'mpw-share-btns' in get_after(html,'in-the-wild'),
    'share_verdict': 'verdict' in html and 'mpw-share-btns' in get_after(html,'verdict'),
    'share_sidebar': 'Share This Entry' in html,
    'share_footer': 'share-x' in html and 'share-reddit' in html,
    # Content (15)
    '3_producer_quotes': html.count('producer-quote-block') >= 3,
    '8_fixit_symptoms': html.count('fixit-symptom') == 8,
    '8_fixit_results': html.count('fixit-result') == 8,
    'genre_grid': 'genre-grid-wrap' in html,
    'producer_dna_3': html.count('dna-card') >= 3,
    'embed_code': 'Embed This Tool' in html,
    'citation_block': 'Cite This Entry' in html,
    'changelog': 'Version History' in html,
    'wtrn': 'What to Read Next' in html,
    'tool_present': mpw_tools_v3.build_tools_section_v3(slug, term) is not None,
    # SEO (15)
    'canonical': f'bible/{slug}' in html and 'rel="canonical"' in html,
    'og_title': 'og:title' in html,
    'og_description': 'og:description' in html,
    'og_image': 'og:image' in html,
    'og_url': 'og:url' in html,
    'twitter_card': 'twitter:card' in html,
    'article_schema': '"@type": "Article"' in html,
    'faqpage_schema': '"@type": "FAQPage"' in html,
    'breadcrumb_schema': '"@type": "BreadcrumbList"' in html,
    'howto_schema': '"@type": "HowTo"' in html,
    'speakable_schema': '"@type": "SpeakableSpecification"' in html,
    'no_www_canonical': 'https://www.' not in html.split('canonical')[1][:100],
    'ga4': 'G-79VB543KCT' in html,
    'beehiiv': 'beehiiv' in html,
    'no_placeholder': '{{' not in html and 'PLACEHOLDER' not in html,
    # JS (10)
    'nav_js': 'entry-nav-inner' in html and 'scrollIntoView' in html,
    'fixit_js': 'window.fixitSelect' in html,
    'dna_toggle': 'dnaToggle' in html,
    'no_settimeout': 'setTimeout' not in html.split('<script')[1],
    'no_innerhtml': 'innerHTML' not in html,
    'js_syntax': check_js_syntax(html),  # node --check
    # Quality (17)
    'word_count_floor': count_words(html) >= 6500,
    'no_hedging': not any(p in html for p in ['it depends', 'generally speaking', 'in some cases', 'typically,', 'usually,']),
    'no_2025_dates': '2025' not in html,
    'no_generic_links': 'href="/bible/sidechain-compression"' not in html,  # excluded slug
    ...
}
```

## Delivery Format

Delivered as 3-part PS1 install scripts (same pattern as mpw_bible_writer.py delivery):
- `install_flagship_writer_part1.ps1`
- `install_flagship_writer_part2.ps1`
- `install_flagship_writer_part3.ps1`

Each part under 200KB. Run in order. Final part runs smoke test: generates `eq.html` locally, prints word count, validation score, and first paragraph for review.

## Wave Batch Files

Create these before running:

```
flagships_wave1a.txt  → eq, gain-staging, delay, limiting, saturation
flagships_wave1b.txt  → sidechain-compression, lufs, mastering (reverb+chorus already live)
flagships_wave2a.txt  → parallel-compression, bus-compression, stereo-imaging, mid-side-processing, automation
flagships_wave2b.txt  → high-pass-filter, parametric-eq, multiband-compression, noise-gate, dynamic-range
flagships_wave2c.txt  → headroom, subtractive-synthesis, lfo, adsr, mix-translation
flagships_wave3a.txt  → transient-shaping, fm-synthesis, wavetable-synthesis, oscillator, true-peak-limiting
flagships_wave3b.txt  → loudness-normalization, send-return, harmonic-distortion, resonance, sidechain-ducking
flagships_wave3c.txt  → modulation, chorus (regen?), low-pass-filter, arrangement, reference-mixing
```

Run wave1a + wave1b + wave2a + wave2b simultaneously (4 parallel sessions) for first 20 entries. Review output. Then run wave2c + wave3a + wave3b + wave3c for remaining 20.
