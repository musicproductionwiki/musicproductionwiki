# MPW-HANDOFF-SCRIPTS.md
*Updated: May 22, 2026 (SESSION 55)*

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

**Purpose:** Unified dispatcher for all 24 v5 tools. Routes 145 slugs to the correct batch file.

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

**Purpose:** Affiliate link registry. All plugin recommendations in all 24 v5 tools reference this file. One approval → one file update → all 24 v5 tools update.

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
    # ... all plugins from all 24 v5 tool plugin recommendations
}

def aff_link(plugin_name, display_text=None):
    """Returns affiliate href for a plugin name."""
    ...
```

---

### mpw_tool_manifest.py — BUILD SECOND

**Purpose:** Single source of truth for all 24 v5 tools. All generators (tool pages, hub page, sitemap) read from this manifest.

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
    # ... all 24 v5 tools
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

**Purpose:** Generates `/tools/index.html` — the category hub page with 8 categories, search/filter, and all 24 tool cards.

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

