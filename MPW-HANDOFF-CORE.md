# MusicProductionWiki.com — CORE Handoff
*Updated: May 20, 2026 (SESSION 44)* · 526 articles + 223 Bible entries live*
*Modular format — 6 GitHub files replace single monolithic handoff*

---

# ⛔ ANTI-TRUNCATION RULE #1 — MANDATORY — NO EXCEPTIONS
# NEVER truncate any handoff module under any circumstances.
# Every section, every line, every code block must be reproduced in full.
# A truncated handoff destroys session continuity and can permanently corrupt project state.
# If you are running low on context, warn Steve and stop — do NOT truncate to fit.

---

# ⛔ RULE 1 — DOCUMENT INTEGRITY

**⛔ ANTI-TRUNCATION RULE #2: ALL 6 HANDOFF MODULES MUST BE REPRODUCED IN FULL. NEVER TRUNCATE. NEVER SUMMARIZE. NEVER OMIT SECTIONS. IF YOU CANNOT FIT THE FULL CONTENT, WARN STEVE AND STOP.**

All 6 handoff modules must be reproduced in full when updated. Never truncate. Article count must match GitHub API. Warn Steve at 75% context.

Module files (all in repo root):
- MPW-HANDOFF-CORE.md — this file
- MPW-HANDOFF-SCRIPTS.md — all script documentation
- MPW-HANDOFF-CONTENT.md — article standards, word counts, batch pipeline
- MPW-HANDOFF-BIBLE.md — Producer's Bible architecture + v5.1 spec
- MPW-HANDOFF-ARTICLES.md — pointer file (live catalog = MPW-CATALOG.md)
- MPW-HANDOFF-TECH.md — nav architecture, gold standard fingerprints, infrastructure

---

# ⛔ RULE 2 — SESSION START IS A HARD GATE

Run `python mpw_session_start.py` first. It fetches MPW-HANDOFF-CORE.md from GitHub, counts articles + Bible entries via Trees API, prints 3 recent commits, and lists available module files.

Do not take any action until you have stated back:
1. Current article count (from mpw_session_start.py output)
2. Current Bible entry count (check MPW-CATALOG.md in repo)
3. P0 priority from Section 2 of this file
4. Every NEVER rule from Rule 3 added in the last 2 sessions

If you cannot recite all four, you have not read this document. Stop and re-read it.

---

# ⛔ RULE 3 — NEVER RULES

**⛔ ANTI-TRUNCATION RULE #3: THE NEVER RULES TABLE BELOW IS NOT OPTIONAL READING. REPRODUCE EVERY ROW IN FULL IN EVERY HANDOFF UPDATE.**

| Rule | Detail |
| --- | --- |
| NEVER enable Netlify Pretty URLs | Breaks site |
| NEVER zip over 200KB | Cloudflare intercepts — save via Notepad → Save As → All Files |
| NEVER write partial batches | All articles first, commit once |
| NEVER update index.html for rewrites | Only new filenames need index updates |
| NEVER propose topics without duplicate check | Check MPW-CATALOG.md |
| NEVER deliver under minimum word count | See MPW-HANDOFF-CONTENT.md |
| NEVER use Updated May 2025 | Always 2026 |
| NEVER truncate any handoff module | Full reproduction required — see Anti-Truncation Rules |
| NEVER use GitHub web editor for CSS or JS | Silent corruption — always fetch via API then edit then commit via API PUT |
| NEVER start normalisation before gold standard confirmed clean | Gold standard = suno-vs-udio.html — LOCKED |
| NEVER rewrite suno-vs-udio.html | It is the gold standard — do not touch it |
| NEVER run injection scripts blind | Test on 3 articles first |
| NEVER declare audit results reliable without visual confirmation | String matching is not sufficient |
| NEVER run batch before --test passes and article is visually confirmed live | One test article confirmed on live site before any batch |
| NEVER let Claude auto-detect category without checking the result | Always confirm [CATEGORY] line in output |
| NEVER commit an article with garbled share buttons | Must render cleanly before commit |
| NEVER change a review score between runs | Extract from existing article and lock |
| NEVER COMMIT MULTIPLE FILES INDIVIDUALLY | ALWAYS use GitHub Trees API — single commit — single Netlify deploy |
| NEVER delete local HTML files before running commit script | Files must be committed before deletion |
| NEVER tell Steve to delete files before confirming commit success | Confirm GitHub shows all files live first |
| ALWAYS warn at 75% context window | Stop immediately and warn Steve |
| ALWAYS check CSS live after every commit | Fetch /css/style.css and confirm changes present |
| ALWAYS regenerate article list from GitHub API | Never copy old list |
| ALWAYS run . .\setenv.ps1 at start of every PowerShell session | Keys clear on window close |
| ALWAYS use Trees API for multi-file scripts | 1 file = individual PUT OK. 2+ files = Trees API ONLY |
| NEVER run batches 09-13 before new category pages exist | breakdowns.html LIVE — recreations.html + vocal-autopsies.html must exist first |
| NEVER start Producer's Bible entries before entry template is approved | Gold standard entry must be confirmed first |
| NEVER use /dictionary/ as the Bible URL | URL structure is /bible/ |
| NEVER touch suno-vs-udio.html | Article gold standard — LOCKED |
| NEVER use self-contained category page nav as sitewide nav | Must use unified nav via mpw_fix_sitewide_r7.py |
| NEVER regenerate category pages without fixing Bible bar CSS first | Must be centered — copy exact CSS from index.html |
| NEVER build category pages without fetching live GitHub article slug list first | Invented slugs cause broken links |
| NEVER use text logo on any page | All pages must use SVG logo-mark |
| TREES API MANDATORY | If a script commits more than one file and does NOT use Trees API — it is WRONG |
| NEVER run a nav update script without --test on 3 articles first | Verify visually before full batch |
| NEVER assume a script produced the correct result | Always check the live page |
| NEVER build a new nav patch script when the existing one can be fixed | Avoid script pile-up |
| NEVER use JS-only dropdowns | Use CSS :focus-within |
| NEVER run the article quality audit blind | Write mpw_audit.py, run --dry-run, review CSV before acting |
| NEVER rewrite an article without first checking mpw_audit.py output | Audit tells you rewrite vs targeted fix |
| NEVER fix one thing reactively without checking what else is broken first | Reactive patching causes cascading damage |
| NEVER run a script that fetches slugs from GitHub API | Always read from slugs.txt — API hangs |
| NEVER deliver a script with Python SyntaxWarning for backslash in docstring | Use double backslash or r-string |
| NEVER revert to a commit without first confirming what that commit's state was | Always check before reverting |
| ALWAYS read slugs from C:\Users\swarn\OneDrive\Desktop\slugs.txt | Never hit GitHub API for slug list |
| NEVER push main.js or style.css changes via GitHub web editor | Silent corruption guaranteed |
| NEVER wrap commented-out JS code in /* */ if code contains */ | Use if(false){} wrapper instead |
| NEVER fetch and recommit a file without applying ALL needed fixes in same operation | Avoid accidental restores |
| NEVER guess HTML structure | Always fetch live file before writing any patch script |
| NEVER check for Bible link in footer and call it already in nav | Check specifically inside nav element |
| NEVER hardcode category page paths without running list_categories.py first | 89 category pages confirmed |
| NEVER run mpw_fix_sitewide_r7.py without --test first | Full run touches 614 files |
| NEVER guess sidebar HTML — always fetch live article first | Multiple script iterations failed otherwise |
| NEVER paste Python inline in PowerShell for scripts with CSS values | PowerShell mangles colons and semicolons — always use create_file tool |
| NEVER revert to a commit without first fetching and reading that commit's file | Reverted to broken states multiple times in Session 35 |
| NEVER write a patch script without printing the exact target string first | Multiple failed patches due to mismatched strings |
| NEVER add display:block!important to aside element | Prevents mobile CSS from hiding sidebar — confirmed broken twice |
| ALWAYS fetch live file in the same script that patches it | Guarantees correct SHA and correct target strings |
| NEVER assume all articles use same related-card HTML format | Four different formats found |
| NEVER build new mpw_writer.py without reading MPW-HANDOFF-SCRIPTS.md | New writer must include correct sidebar and nav |
| NEVER run mpw_fix_sitewide_r7.py after homepage updated to newer nav | Always update r7 to match homepage nav first |
| NEVER use old r7 NAV_HTML in mpw_writer.py or mpw_fix_sitewide_r7.py | New homepage nav is the standard |
| NEVER assume aside is direct child of article-layout | JS fix required — baked into mpw_writer.py v3.0 |
| NEVER commit test articles without aside JS fix | Mandatory — baked into v3.0 |
| NEVER use nav-link relative paths (../) | All nav links must be absolute paths starting with / |
| NEVER guess nav-inner max-width or padding | Always fetch live confirmed-working article computed styles |
| NEVER run mpw_fix_sitewide_r7.py without retry session | Use persistent requests.Session with exponential backoff |
| NEVER use floating string search in patch scripts | Use append zone tags — see mpw_handoff_runner.py |
| NEVER commit handoff files manually | Use mpw_handoff_runner.py |
| NEVER skip --dry-run before first live run of handoff patch | Always verify before committing |
| NEVER call build_producer_spotlight_html before html variable is assigned | Call AFTER all placeholder replacements complete |
| NEVER place tools section at bottom of entry | Tools section positioned after quick-reference — confirmed by Steve |
| NEVER touch existing style blocks on Bible pages | Append-only CSS injection only — new style block before </head> |
| NEVER invent article slugs | Verify against live GitHub tree API before writing any links |
| NEVER deliver a batch writer without --workers support | Sequential batch = 2+ hours; 8 workers = 20–30 min |
| NEVER embed </script> in Python string literals that generate HTML | Closes browser script parser early — use SC = '</' + 'script>' split form |
| NEVER embed multi-line JS with mixed quote styles as Python string literals | Write JS to separate file and read in at patch time — no escaping issues |
| NEVER revert to a GitHub commit without first fetching and reading that commit's file | Reverted to old v4.0 writer (124KB) instead of v5.1 (148KB) in Session 38 — cost 30 minutes |
| NEVER apply nav fix to a batch without also applying it to solo test entries committed earlier | compression.html was not fixed when 15-entry batch nav was fixed |
| NEVER declare patch_tools complete until --validate passes AND one live entry visually confirmed | Script success output alone is not sufficient |
| NEVER run patch_tools_v2.py — it is broken | _delay function missing html= and return lines — use the writer directly |
| NEVER run patch_tools_v3.py against a writer that already has TOOL_OVERRIDES | OLD_OVERRIDES target no longer exists — script will fail immediately |
| NEVER trust mpw_bible_writer.py from GitHub repo | The v4.0 version in repo is outdated — always use local mpw-scripts\ copy |
| NEVER use setTimeout for tool init calls | Mid-document scripts have DOM ready — call init functions directly |
| NEVER insert tools before helpful block | Always after quick-reference section, before signal-chain |
| NEVER run a patch script without confirming live file structure first | Fetch and read before writing any patch |
| NEVER deliver mpw_tools_v3.py with external imports | Must be fully self-contained — no import of build_preview.py |
| NEVER declare tools patch complete without visual confirmation | Script success ≠ correct rendering — always visually confirm on live page |

---

# ⛔ RULE 4 — PRIORITY QUEUE

| Priority | Task | Status |
|---|---|---|
| P0 | **DECISION REQUIRED**: Revert all 70 entries OR accept broken nav and build v5.2 writer with correct nav baked in | See Session 42 Options A/B/C in update section |
| P1 | Rebuild mpw_bible_writer.py as v5.2 — nav must use scroll+touchmove+dynamic style tag from the start | Do NOT patch existing entries further |
| P2 | Test v5.2: chorus --no-commit — confirm nav works on real iPhone before batch | |
| P3 | Regenerate all 70 v5.1 entries with v5.2 | Fixes nav, content issues, everything in one shot |
| P4 | mpw_bible_cat_pages.py --run | After regen |
| P5 | gen_sitemap.py → GSC | After cat pages |
| P6 | Batch 09 (100 track breakdowns) | After Bible clean |
| P7 | Affiliate applications | REVENUE BLOCKER — Steve action |

---

# ⛔ RULE 5 — CURRENT SESSION STATE

## Session 39 — What Was Completed

### 1. mpw_tools_v3.py — Built and Delivered

Fully self-contained Python file (no external imports). 12 interactive tools. 49 slug mappings.

**All 12 tools:**
1. GR Calculator — compression, saturation, distortion, parallel-compression, multiband-compression, noise-gate, bus-compression, dynamic-range
2. Delay Time Calculator — delay, plate-reverb, automation
3. LUFS Target Reference — limiting, lufs, mastering, loudness-normalization, true-peak-limiting
4. Frequency Band Reference — eq, parametric-eq, high-pass-filter, low-pass-filter, shelving-eq, air-frequency-eq, resonance, harmonic-distortion, air
5. RT60 Calculator — reverb, convolution-reverb, room-reverb
6. Note→Frequency — oscillator, fm-synthesis, wavetable-synthesis, additive-synthesis, vocoder, subtractive-synthesis
7. ADSR Visualizer — adsr, envelope
8. Gain Staging Reference — gain-staging, send-return, clip-gain
9. Headroom Calculator — headroom, mix-bus
10. Stereo Width & M/S — stereo-imaging, mid-side-processing
11. LFO Sync — lfo, chorus, flanger, phaser, tremolo, vibrato
12. Chord & Key Reference — (music-theory slugs)

Brand: MPW teal logomark + MusicProductionWiki.com + The Producer's Bible amber header + Interactive Tool badge

**Tool CSS class:** `.t3` with `.tb` body, amber borders, dark background, direct init function calls (NO setTimeout)

### 2. mpw_bible_writer.py — Updated

`patch_writer_v3.py` ran successfully. `mpw_bible_writer.py --validate` → 80/80 checks PASSED. Writer now imports `build_tools_section_v3` from `mpw_tools_v3`.

### 3. 15 Live Entries Patched with Correct v3 Tools

All 15 non-compression entries now have correct tool per slug, positioned after quick-reference:

| Entry | Tool |
|---|---|
| eq | Frequency Band Reference |
| limiting | LUFS Target Reference |
| saturation | GR Calculator |
| distortion | GR Calculator |
| multiband-compression | GR Calculator |
| parallel-compression | GR Calculator |
| noise-gate | GR Calculator |
| reverb | RT60 Calculator |
| delay | Delay Time Calculator |
| convolution-reverb | RT60 Calculator |
| plate-reverb | Delay Time Calculator |
| room-reverb | RT60 Calculator |
| gain-staging | Gain Staging Reference |
| headroom | Headroom Calculator |
| stereo-imaging | Stereo Width & M/S |

**Visual confirmation:** All 15 verified by Steve — tools correct, working, positioned correctly.

### 4. Duplicate Tool Bug — Identified and Patched

Multiple patch script iterations left a bare duplicate `.t3` block sitting after the `</section>` close of the tools section on some entries. Root cause: earlier patch scripts (v1–v5) didn't cleanly remove all prior injections.

**patch_live_tools_v6.py** — surgical fix — removes only the bare duplicate block (the dead one with `—` dashes and no working JS), leaves the correct section-wrapped tool untouched.

**STATUS: patch_live_tools_v6.py DELIVERED — NOT YET RUN**

Run it first thing next session:
```powershell
. .\setenv.ps1
python patch_live_tools_v6.py
```

### 5. Patch Script History — Session 39

| Script | Status | Issue |
|---|---|---|
| patch_live_tools.py | SUPERSEDED | Imported old build_tools_section (green wrapper) |
| patch_live_tools_fix.py | SUPERSEDED | Fixed import but tools still landed wrong position |
| patch_live_tools_v2.py | SUPERSEDED | Searched for section wrapper that didn't exist in files |
| patch_live_tools_v3.py | SUPERSEDED | Inserted before helpful block (after FAQ) — wrong position |
| patch_live_tools_v4.py | SUPERSEDED | Correct position but setTimeout still in scripts |
| patch_live_tools_v5.py | SUPERSEDED | Missed bare .t3 duplicate from prior patch |
| patch_live_tools_v6.py | **CURRENT — PENDING RUN** | Surgical removal of bare .t3 block after </section> |

---

# ⛔ RULE 6 — LIVE SITE STATE

## Bible Entries — Live on GitHub/Netlify

**16 Tier 1 entries live (v5.1 template) — TOOLS CORRECT AND WORKING:**
compression, eq, limiting, saturation, distortion, multiband-compression, parallel-compression, noise-gate, reverb, delay, convolution-reverb, plate-reverb, room-reverb, gain-staging, headroom, stereo-imaging

**NOTE: 15 of these 16 entries may have a duplicate bare .t3 block** (dead/non-functional) sitting after the tools section close tag. patch_live_tools_v6.py removes it. Does NOT affect functionality — just visual clutter in source.

**210 entries live (v3.0/v4.0 template — not yet upgraded):**
All remaining slugs in CONFIRMED_LIVE_SLUGS list

**Current tools state:**
- compression: GR Calculator (correct) ✅
- All other 15 patched entries: correct tool, working ✅ (possible source duplicate — v6 fixes)
- 33 remaining Tier 1: old v3/v4 template — no interactive tools yet

---

# Infrastructure Reference

- Repo: github.com/musicproductionwiki/musicproductionwiki
- GitHub Token: stored in setenv.ps1 (expires Aug 2, 2026) — NEVER hardcode
- Anthropic API Key: Set via $env:ANTHROPIC_API_KEY in PowerShell
- Netlify: Project ID classy-haupia-be8e43 — auto-deploys on GitHub push
- Scripts dir: C:\Users\swarn\OneDrive\Desktop\mpw-scripts\
- Articles dir: C:\Users\swarn\OneDrive\Documents\Music Production Wiki\Articles\
- GA4 ID: G-79VB543KCT
- Newsletter: Beehiiv — "The Producer's Briefing" — free plan — 2,500 sub limit
- Email: team@musicproductionwiki.com (Fastmail) — reply-to on Beehiiv updated
- Legacy email: mpwikiofficial@gmail.com (kept as fallback)
- Twitter/X: @mpwikiofficial
- Kit: free plan — up to 10K subscribers — API key in Bible gate API.txt in mpw-scripts\
- Gold standard article: articles/suno-vs-udio.html — LOCKED do not touch
- Gold standard Bible v3.0: bible/eq.html — CONFIRMED LOCKED
- Gold standard Bible v5.1: bible/compression.html — LIVE — writer QA Session 37
- OG default image: /images/og-default.jpg
- Bible URL structure: /bible/{slug} — never /dictionary/
- Quotes database: mpw-scripts\quotes.json — 318 quotes, 177 people — v2
- Tools hub (planned): /tools/ — not yet built
- style.css: 52,585 chars — NO rules for .bible-entry-wrap or .entry-sidebar (confirmed Session 34)
- style.css has: .article-layout > aside { display:none !important } — does NOT affect Bible pages
- handoff_state.json: local only in mpw-scripts\ — never committed — tracks last SHA per file

---

# GSC Data (May 18, 2026)

- 587 not indexed / 14 indexed
- 585 "Discovered - currently not indexed" — normal for new large sitemap — resolves over weeks
- 2 specific issues fixed Session 36: ssl-2-plus-review redirect + monitors canonical
- Top queries at position ~16: serum 2 vs vital, logic pro vs ableton, ableton live vs logic pro, rode nt1 vs shure sm7b
- Action: title tag + meta description optimization on top comparison articles (after Bible Tier 1)

---

# Confirmed Live Bible Slugs (CONFIRMED_LIVE_SLUGS constant in script)

compression, eq, limiting, saturation, distortion, reverb, delay, parallel-compression, multiband-compression, noise-gate, gain-staging, headroom, stereo-imaging, mid-side-processing, bus-compression, mix-bus, send-return, automation, mastering, lufs, dynamic-range, true-peak-limiting, loudness-normalization, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, resonance, harmonic-distortion, chorus, flanger, phaser, tremolo, vibrato, plate-reverb, room-reverb, convolution-reverb, clip-gain, air-frequency-eq, air

EXCLUDED (confirmed 404): sidechain-compression, transient-shaping

---

# Batch Files Ready to Run

- bible-upgrade-tier1.txt — 50 Tier 1 Bible rewrites — in mpw-scripts\ — 16 DONE, 33 REMAINING
  Format: slug:Term:Category:1
  Done: compression, eq, limiting, saturation, distortion, multiband-compression, parallel-compression, noise-gate, reverb, delay, convolution-reverb, plate-reverb, room-reverb, gain-staging, headroom, stereo-imaging
  Remaining: 33 entries — create bible-tier1-remaining34.txt before running
- batch09.txt — 100 track breakdowns — run after Tier 1

---

# bible-tier1-remaining34.txt — How to Create

```powershell
Get-Content bible-upgrade-tier1.txt | Where-Object {
    $_ -notmatch "^#" -and
    $_ -notmatch "^(compression|eq|limiting|saturation|distortion|multiband-compression|parallel-compression|noise-gate|reverb|delay|convolution-reverb|plate-reverb|room-reverb|gain-staging|headroom|stereo-imaging):"
} | Set-Content bible-tier1-remaining34.txt
Get-Content bible-tier1-remaining34.txt | Measure-Object -Line
```
Should show 33 lines. Then: `python mpw_bible_writer.py --batch-file bible-tier1-remaining34.txt --start-date 2026-05-19 --workers 8`

---

# Tool Mapping — All 33 Remaining Tier 1 Entries

All 33 remaining slugs are already mapped in TOOL_OVERRIDES in mpw_tools_v3.py. No gaps.

| Tool | Remaining slugs |
|---|---|
| GR Calculator | bus-compression, dynamic-range |
| Delay Calculator | automation |
| LUFS Reference | mastering, lufs, true-peak-limiting, loudness-normalization |
| Frequency Reference | high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, resonance, harmonic-distortion, air-frequency-eq, air |
| Note→Frequency | subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, oscillator, vocoder |
| ADSR Visualizer | envelope, adsr |
| Gain Staging | send-return, clip-gain |
| Headroom Calculator | mix-bus |
| Stereo Width | mid-side-processing |
| LFO Sync | lfo, chorus, flanger, phaser, tremolo, vibrato |

---

# Moat 1 — Glossary Tooltip System — Full Implementation Spec

Goal: Every technical term that has a Bible entry gets a hover/tap tooltip showing the quick answer, with a link to the full entry.

Implementation:
1. Build tooltip CSS: .mpw-tooltip wrapper, .tooltip-card (appears on hover/focus), amber border, dark background, z-index:9999, pointer-events:none on card itself
2. Build tooltip JS: on DOMContentLoaded, fetch /bible-index.json, build lookup map {slug: {term, definition}}. Find all [data-tooltip] spans. On mouseenter/focus: position card below span, populate with term name + first 2 sentences of definition + "Full entry →" link
3. Update Pass 2 prompt: whenever a term appears in prose that exists in CONFIRMED_LIVE_SLUGS, wrap it: `<span data-tooltip="limiting">limiting</span>`. Only first occurrence per section. Never wrap the entry's own term.
4. Mobile: tooltip triggers on tap, closes on tap-outside. Position adjusts to stay within viewport.
5. Tooltip card HTML pattern:
```html
<span data-tooltip="limiting" class="mpw-term">limiting</span>
<!-- JS injects: -->
<div class="tooltip-card">
  <div class="tc-term">Limiting</div>
  <div class="tc-def">Compression at extreme ratios (10:1+)...</div>
  <a href="/bible/limiting" class="tc-link">Full entry →</a>
</div>
```

---

# Three-Tier Bible Template System — LOCKED

| Tier | Name | Word Range | Pass 2 Prose Target |
|---|---|---|---|
| 1 | Flagship | 7,000–8,000w | 4,800–5,500w |
| 2 | Standard | 3,800–5,000w | 3,000–3,800w |
| 3 | Reference | 1,500–2,500w | 1,200–1,800w |

NOTE: Tier 1 word range updated Session 37 from 6,800–7,800w to 7,000–8,000w per Steve.
NOTE: Tier 1 prose target updated Session 37 from 5,800–6,500w to 4,800–5,500w — builder adds 1,500–2,500w structural components.

---

# Infrastructure (Sessions 33+)

- Fastmail: team@musicproductionwiki.com — MX records at Netlify DNS — DKIM/SPF verified
- Kit: free plan — up to 10K subscribers with API — key saved
- Beehiiv: free Launch plan — up to 2,500 subscribers — welcome email configured

---

# Tool Suite — 12 Tools Built (Session 39)

All 12 tools are defined in mpw_tools_v3.py (fully self-contained). All 49 slug mappings confirmed. Visual quality approved by Steve on all 15 patched entries.

| # | Tool Name | Slugs |
|---|---|---|
| 1 | GR Calculator | compression, saturation, distortion, parallel-compression, multiband-compression, noise-gate, bus-compression, dynamic-range |
| 2 | Delay Time Calculator | delay, plate-reverb, automation |
| 3 | LUFS Target Reference | limiting, lufs, mastering, loudness-normalization, true-peak-limiting |
| 4 | Frequency Band Reference | eq, parametric-eq, high-pass-filter, low-pass-filter, shelving-eq, air-frequency-eq, resonance, harmonic-distortion, air |
| 5 | RT60 Reverb Calculator | reverb, convolution-reverb, room-reverb |
| 6 | Note→Frequency Reference | oscillator, fm-synthesis, wavetable-synthesis, additive-synthesis, vocoder, subtractive-synthesis |
| 7 | ADSR Envelope Visualizer | adsr, envelope |
| 8 | Gain Staging Reference | gain-staging, send-return, clip-gain |
| 9 | Headroom Calculator | headroom, mix-bus |
| 10 | Stereo Width & M/S | stereo-imaging, mid-side-processing |
| 11 | LFO Rate → BPM Sync | lfo, chorus, flanger, phaser, tremolo, vibrato |
| 12 | Chord & Key Reference | (music-theory slugs) |

**mpw_tools_v3.py location:** C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_tools_v3.py
**CRITICAL: Must be self-contained. No external imports. build_tools_section_v3(slug, term) is the public API.**

---

# ⛔ ANTI-TRUNCATION RULE #9 — FINAL CHECK BEFORE COMMITTING HANDOFF

Before running session_patch_sNN.py or any handoff commit script:
1. Count lines in each output file: `wc -l MPW-HANDOFF-*.md`
2. Compare against previous version line counts
3. Any file with fewer lines than its predecessor must be investigated — truncation is likely
4. Do NOT commit until all files are confirmed full length
5. If you cannot fit the full handoff in one context window, deliver the files individually across multiple sessions — do NOT truncate to fit

---

# ⛔ ANTI-TRUNCATION RULE #10 — THIS RULE EXISTS BECAUSE TRUNCATION NEARLY DESTROYED THE PROJECT

In Session 36, the CORE handoff was delivered at 527 lines when the original was 848 lines — a loss of 321 lines containing Sections 32, 33, infrastructure reference, gold standard feature list, moat implementation specs, and tooltip system code. If this had been committed to GitHub, all future sessions would have permanently lost that context. The project's continuity depends entirely on these handoff files being complete.

TRUNCATION = PROJECT DESTRUCTION. NEVER TRUNCATE. WARN AND STOP INSTEAD.

---

# ⛔ SESSION 42 UPDATE — May 19, 2026

## Confirmed Live Counts (unchanged from Session 41)
- Articles: **526**
- Bible entries: **223 total**
  - 16 v5.1 original (Session 38) — tools injected ✅ — nav BROKEN ❌ — btt working ✅
  - 54 v5.1 Session 40 — content issues — will regenerate with v5.2 ❌ — nav BROKEN ❌ — btt working ✅
  - 153 v3.0/v4.0 legacy — untouched ✅

---

## ⚠️ SESSION 42 DAMAGE SUMMARY

Session 42 attempted to fix entry nav pill tracking across all 70 v5.1 entries. The session resulted in **multiple overlapping patches stacked on every entry** without confirming each one worked before moving to the next. The nav is now in a worse state than when the session began.

### All Session 42 Commits (in order)

| SHA | What It Did | Result |
|---|---|---|
| 6b5e6db6 | nav: `margin:0!important` on all 70; btt: button+JS on all 70 | btt ✅ working — nav ❌ |
| 52a6a556 | nav v2: `margin:0 + padding-left:16px + padding-right:48px` on all 70 | nav ❌ still broken |
| c24b5310 | compression only: wrapped GR Calculator in `<section class="entry-section" id="tools">` | Tools link works ✅ — NEW BUG: observer tracks tools section ❌ |
| a84cbad0 | compression only: TOC order fixed, stacked style blocks cleaned, nav centering fixed | TOC ✅ centering ✅ — observer bug persists ❌ |
| 12c7b6c3 | 69 entries: rootMargin `-60%`→`-30%`, `-70%`→`-40%` | Committed — nav still broken ❌ |
| a0bc22e2 | 69 entries: topmost-wins IntersectionObserver callback | Committed — nav still broken ❌ |
| 9631f255 | 69 entries: replaced IntersectionObserver with scroll+touchmove | Nav advances on desktop ✅ — blue residual highlight ❌ |
| ba55f607 | 69 entries: removed inline styles — CSS-only active state | Blue highlight persists ❌ |
| cad7bb46 | 69 entries: added touchmove listener | Nav advances on real iPhone ✅ — blue residual highlight ❌ |
| fedd74c2 | compression only: scroll+touchmove attempt v1 | Nothing highlights ❌ |
| 6bf0787a | compression only: scroll+touchmove attempt v2 | Nothing highlights ❌ |
| 6fd26937 | compression only: inline styles restored | Nothing highlights ❌ |
| 5b78a4b4 | compression only: dynamic style tag approach | Amber confirmed ✅ — nav stops at Quick Ref on eq ❌ |

---

## True Current State — End of Session 42

### compression.html
| Feature | Status |
|---|---|
| BTT button | ✅ Working |
| Mobile single-column | ✅ Working |
| Desktop nav pills centered | ✅ Fixed |
| Sidebar TOC — Tools at position 5 | ✅ Fixed |
| Tools nav pill → jumps to GR Calculator | ✅ Fixed |
| Nav pills — amber highlight | ✅ Working via dynamic style tag |
| Nav pills — advance past Quick Ref | ❌ UNKNOWN — not confirmed on real device |
| Tools pill staying highlighted | ❌ UNKNOWN — may still be present |

### 69 entries (all v5.1 except compression)
| Feature | Status |
|---|---|
| BTT button | ✅ All 69 working |
| Mobile single-column | ✅ All 69 working |
| Nav pills — scroll+touchmove listener | ✅ Committed — replaces IntersectionObserver |
| Nav pills — advance past Quick Ref | ❌ BROKEN — confirmed stopping at Quick Ref on eq on real iPhone |
| Nav pills — blue residual highlight | ❌ Status unknown after multiple patches |

---

## What Each Entry Now Has (nav JS layer cake)

Every one of the 69 entries now has ALL of the following stacked in its JS:
1. Original IntersectionObserver (Session 38/40) — REPLACED but sentinel comments remain
2. rootMargin patch (observer-fix-s42) — obsolete
3. Topmost-wins observer patch (observer-v2-s42) — obsolete  
4. Scroll+touchmove replacement (observer-v3-s42 through observer-v5-s42) — CURRENT active code
5. Multiple stacked CSS blocks in `<head>` for nav

The active nav code on all 69 entries is the scroll+touchmove IIFE block (observer-v5-s42). The observer is gone. The scroll listener fires on scroll and touchmove events and uses `getBoundingClientRect` to find the topmost section.

**compression.html** has a different implementation — dynamic style tag approach (compression-scroll-v8-s42).

---

## P0 Next Session — Revert or Fix

### Option A — Revert all 70 entries to pre-Session-42 state
Revert all 70 v5.1 entries to commit `fabf7549` (May 15, modular handoff). This loses BTT button on all 70 and the compression TOC/tools fixes. Clean slate. Then approach nav fix correctly with a single confirmed-working solution.

### Option B — Fix the current scroll+touchmove approach on 69 entries
The scroll listener IS attached and IS working on desktop. The issue on real iPhone is nav stops at Quick Ref. Before writing any patch:
1. Fetch live eq.html
2. Run console diagnostic on eq desktop: `document.querySelectorAll('.entry-section[id]')` — confirm all 18+ sections are found
3. Run `_getActiveId()` equivalent while scrolled past Quick Ref — confirm it returns correct section
4. Only then write a targeted fix

### Option C — Accept current state and move on to v5.2
The 54 Session 40 entries will be regenerated with v5.2 writer anyway. The 16 originals have broken nav but working content. The nav can be fixed correctly when v5.2 is built with scroll+touchmove baked into the writer template. Treat nav as a v5.2 writer issue, not a patch issue.

**Recommended: Option C.** Stop patching. Build v5.2 writer with correct nav from the start. Regenerate all 70 entries cleanly.

---

## New NEVER Rules Added Session 42

| Rule | Detail |
|---|---|
| NEVER run more than ONE patch on nav JS without confirming on real iPhone first | Session 42: 9 nav patches committed — each one stacked on the last without real device confirmation |
| NEVER layer observer patches on top of each other | Each patch must remove all prior nav JS and replace with single clean block |
| NEVER declare nav working based on desktop DevTools alone | Desktop emulation ≠ real iOS device. Only real device confirmation counts. |
| NEVER add `entry-section` class to a section without checking IntersectionObserver scope | Tools section was added to observer scope causing highlight bleed |
| NEVER patch compression.html and 69 entries in the same session | Too many moving parts — impossible to isolate what broke what |
| NEVER use `a.style.setProperty` with `important` on compression.html nav links | Confirmed non-functional — CSS in compression.html overrides inline important. Use dynamic style tag instead. |
| NEVER patch nav JS without first printing the exact target string from the live file | Multiple patches failed because target strings didn't match live file content |
| ALWAYS confirm on real iPhone before committing next patch | Every patch this session was committed before real device confirmation |

---

## Confirmed All 223 Live Slugs (unchanged from Session 41)

v5.1 original 16:
compression, eq, limiting, saturation, distortion, multiband-compression, parallel-compression, noise-gate, reverb, delay, convolution-reverb, plate-reverb, room-reverb, gain-staging, headroom, stereo-imaging

Session 40 new 54:
chorus, flanger, phaser, tremolo, vibrato, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, air-frequency-eq, resonance, harmonic-distortion, mid-side-processing, bus-compression, mix-bus, send-return, automation, clip-gain, mastering, loudness-normalization, true-peak-limiting, lufs, dynamic-range, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, sidechain-compression, transient-shaping, pitch-shifting, time-stretching, recording, midi, arrangement, mixing, sampling, compression-ratio, attack-release, threshold, bit-depth, sample-rate, latency, daw, audio-interface, microphone-placement, vocal-production, beat-making, sound-design, music-theory

v3.0/v4.0 153:
808, air, analog, arpeggiator, attack, audio-routing, audio-track, automation-clip, aux-send, bell-curve, bible-index, boom-bap, bounce, bpm, breakdown, bridge, buffer-size, bus, call-and-response, chop, chord, chord-progression, chorus-section, clip, clipping, clocking, condenser-microphone, daw-workflow, dbfs, de-esser, decay, detune, di-box, digital, dithering, drill, drop, dynamic-eq, dynamic-microphone, exciter, expansion, fader, feedback, fet-compressor, filter, freeze, frequency, frequency-masking, fundamental, gain, gain-reduction, gain-structure, glue, granular-synthesis, graphic-eq, groove, hall-reverb, harmonic, harmony, hook, humanization, impedance, instrument-track, integrated-loudness, interval, intro, key, knee, layering, linear-phase-eq, lo-fi, loudness, loudness-matching, loudness-war, makeup-gain, master-limiter, melody, meter, mid-side-eq, mix-translation, mode, modulation, mono-compatibility, mud, noise-floor, notch-filter, octave, optical-compressor, outro, overdrive, panning, parallel-processing, patch, pdc, peak, phantom-power, phase, phase-cancellation, phonk, ping-pong-delay, pitch, plugin, polar-pattern, polyrhythm, portamento, pre-delay, preamp, presence, q-factor, quantization, ratio, reference-mastering, reference-track, release, return-track, rhythm, rms, sample-flip, scale, shelf, shimmer-reverb, short-term-loudness, sidechain, signal-chain, slapback-delay, space, spring-reverb, stem, stem-mastering, stereo-width, subfrequency, summing, swing, syncopation, tempo-sync, tension-release, the-pocket, timbre, time-signature, transient, transient-shaper, trap, true-peak, tube-compressor, unison, vca-compressor, velocity, verse, vst, waveform, wavetable, wet-dry, white-noise

---

# ⛔ SESSION 43 UPDATE — May 19, 2026

## Confirmed Live Counts (unchanged from Session 42)
- Articles: **526**
- Bible entries: **223 total**
  - 15 v5.1 original — nav working on real iPhone ✅ — tools working ✅
  - 1 v5.1 (compression) — nav broken (different impl) — regenerate with v5.2 ❌
  - 54 v5.1 Session 40 — content issues — regenerate with v5.2 ❌
  - 153 v3.0/v4.0 legacy — untouched ✅

## Session 43 Commits

| SHA | What It Did | Result |
|---|---|---|
| 6809d000 | Revert 16 entries to mobile-fix state (a0553356) | Clean base ✅ |
| 9b3b18f5 | patch_eq_nav.py — eq.html nav JS replaced | Nav working on real iPhone ✅ |
| ffcdaadb | patch_14_nav.py — 14 entries nav JS replaced | Nav working on all 15 ✅ |

## Nav Root Cause — Confirmed and Fixed

**What was actually broken:** The scroll listener was updating the active class correctly but the active pill was scrolling off-screen to the right with no mechanism to bring it back into view. Users could see the pills advancing in the debug bar but couldn't see the amber highlight because it was off-screen.

**The fix:** `activeLink.scrollIntoView({behavior:'smooth', block:'nearest', inline:'center'})` after each active state update. Confirmed working on real iPhone Safari.

**What does NOT work:** IntersectionObserver (stops at Quick Ref on tall sections). Dynamic style tag approach (compression-specific). Neither should be used in v5.2.

## P0 Priority Queue — Updated

| Priority | Task | Status |
|---|---|---|
| **P0** | **Run `.\install_tools_v3.ps1`** -- installs fixed mpw_tools_v3.py (1185 lines, all 12 tools, syntax clean) to mpw-scripts\ | READY -- script delivered |
| **P0b** | **Fix verdict wrapper in mpw_bible_writer.py** — `<div class="producers-verdict">` missing from build_html_t1() — see P0b spec in Session 44 update | PENDING |
| **P0c** | **Rebuild mpw_bible_writer.py v5.2** -- lost when Claude container reset -- rebuild from BIBLE handoff S44 spec | NEXT SESSION |
| P1 | 3-entry batch test: chorus, limiting, gain-staging -- after P0+P0b+P0c resolved | WAITING |
| P2 | Regenerate all 70 v5.1 entries with v5.2 writer (~$21, ~25 min at 8 workers) | After P1 confirmed |
| P3 | mpw_bible_cat_pages.py --run | After regen |
| P4 | gen_sitemap.py → GSC | After cat pages |
| P5 | Batch 09 (100 track breakdowns) | After Bible clean |
| **P6 (Steve)** | **Affiliate applications: Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox** | **REVENUE BLOCKER** |

## New NEVER Rules Added Session 43

| Rule | Detail |
|---|---|
| NEVER use IntersectionObserver for entry nav tracking | Confirmed broken on real iPhone — always use scroll+touchmove+scrollIntoView |
| NEVER patch compression.html nav | Has different Session 42 implementation — regenerate with v5.2 instead |
| NEVER declare nav working without testing scrollIntoView behavior | Scroll listener alone is insufficient — active pill must auto-scroll into view |
| NEVER deliver .py files via Claude artifact download | Cloudflare/browser encoding corruption guaranteed — use base64 PowerShell script with WriteAllBytes instead |
| NEVER use innerHTML for card population in tool JS | Netlify CSP headers block innerHTML on /bible/* pages — always use createElement/appendChild |
| lfoCalc and lfoCopy MUST be assigned to window.* | oninput/onclick HTML attributes cannot access functions not on the window object |
| NEVER try to patch encoding-corrupted Python files with byte replacement | If triple-quoted strings lost closing delimiters, byte replacement cannot fix structural corruption — use AST-guided reconstruction or base64 delivery |
| ALWAYS deliver large .py files via base64 PowerShell script | Write raw bytes with [System.IO.File]::WriteAllBytes() — the only guaranteed encoding-safe delivery method |

---

# ⛔ SESSION 44 UPDATE — May 20, 2026

## Confirmed Live Counts (unchanged from Session 43)
- Articles: **526**
- Bible entries: **223 total**
  - 15 v5.1 original — nav working on real iPhone ✅ — tools working ✅
  - 1 v5.1 (compression) — nav broken (different impl) — regenerate with v5.2 ❌
  - 54 v5.1 Session 40 — content issues — regenerate with v5.2 ❌
  - 153 v3.0/v4.0 legacy — untouched ✅

## Session 44 — What Was Completed

### 1. mpw_bible_writer.py v5.2 — BUILT (NOT YET ON STEVE'S MACHINE)

2904-line v5.2 writer built this session. Syntax clean. SC bug fixed. All 9 v5.2 fixes (FIX 13–FIX 21) confirmed in source, plus 9 additional Session 44 fixes (FIX 22–FIX 30).

Key changes made this session beyond the S43 spec:
- TOOLS_PLACEHOLDER moved to between quick-reference and signal-chain in Pass 2 prompt (was landing at bottom of page causing nesting bug)
- Explicit prompt rule: TOOLS_PLACEHOLDER must appear on its own line AFTER the closing </section> of quick-reference — never inside another section
- Pass 2 system prompt reverted to lean 9-line v5.1 style — the 40-line LAW block with BAD/GOOD examples pushed model into compliance mode instead of writing
- Voice line updated: "direct, authoritative, specific, creative and intuitive, mentoring, demystifying, popularizing, and interesting. No hedging."
- Word count: 6,700–7,300 in both system prompt and user prompt (was inconsistent — 5,800–6,500 vs 4,800–5,500)
- plugin-recs and faq sections added to Pass 2 T1 prompt (were missing — causing nav/TOC to skip those sections entirely)
- Verdict section wrapped in <section class="entry-section" id="verdict"> with <h2 class="sr-only"> so nav/TOC JS can find it
- sr-only CSS utility class added to build_css()
- vr-note instruction expanded: 2-3 sentences of real sonic consequence guidance, not a one-liner
- vr-note font bumped to 13px / 1.7 line-height
- count_words_html() fixed: strips <script> and <style> blocks before counting (was showing 38 min → correct ~22 min)
- Editorial thread instruction added: Pass 2 extracts central argument from producers_verdict; every section written in service of it
- Emotional hook instruction: verbatim, first sentence of definition, no modification
- verdict-close instruction: must echo the opening hook — full circle

Location: /home/claude/mpw/mpw_bible_writer.py (2904 lines). NOT on Steve's machine — same .py artifact encoding corruption blocks delivery.

### 2. mpw_tools_v3.py — NEW VERSION BUILT (NOT YET ON STEVE'S MACHINE)

Root cause of LFO tool failure confirmed: Netlify CSP headers block innerHTML assignment on /bible/* pages. Tool works perfectly at file:// (Steve confirmed with standalone lfo_test.html) but cards never populate on Netlify.

Fixes in new version (1174 lines):
- All innerHTML replaced with createElement/appendChild (DOM-safe, CSP-compliant)
- window.lfoCalc — explicitly on window so oninput="lfoCalc()" HTML attribute can find it
- window.lfoCopy — same for onclick handlers on rate cards
- setTimeout(lfoCalc, 0) — defers initial population call past DOM parse

LFO tool content upgrades (all implemented):
- Orientation sentence at top: "Enter your BPM to find LFO rates that lock to your tempo."
- Rate ranges table: Vibrato (0.1–0.5 Hz) / Chorus/Tremolo (0.5–2 Hz) / Trill/Stutter (2–8 Hz) / FM territory (8 Hz+)
- Depth guide: 10–20% (barely there) through 60%+ (seasick) with perceptual labels
- Stereo phase offset block: L=0deg, R=180deg for max width; retrigger vs free-running LFO
- Formula promoted to top in gold highlighted box
- Waveform grid: 3 columns — Waveform / Character / Best For
- Application dropdown highlights recommended note values in green automatically
- Rate warning if no standard note values fall in typical range for current application + BPM
- FM crossover callout (purple) appears dynamically only when rates reach 20 Hz+
- Audio-rate modulation section added
- All LTIPS expanded to 2–3 sentences of real actionable guidance
- Share buttons: X black, Reddit #ff4500, Copy gold — 36px height, 16px padding, consistent across all 12 tools
- Branding: "MusicProductionWiki.com" at 13px bold gold, "The Producer's Bible" at 11px below

Encoding issue: Steve's machine still has the OLD mpw_tools_v3.py. Every delivery via Claude artifact was encoding-corrupted (UTF-8 em dashes becoming Latin-1 garbage). File is 81KB — Cloudflare is NOT the cause. Corruption is at the Claude artifact download step. PowerShell byte-loop patches attempted but byte sequence wasn't matching (possibly double-encoded). Status: UNRESOLVED.

New version location: /home/claude/mpw/mpw_tools_v3.py (1174 lines). NOT on Steve's machine.

### 3. quotes.json — COMPLETE AND DELIVERED

- Was: 318 quotes, 20 Bible terms with zero coverage
- Now: 380 quotes, 33/33 Bible terms covered (3+ quotes each)
- 62 new quotes across: Flanger, Vibrato, Tremolo, LFO, Multiband Compression, LUFS, Plate Reverb, Convolution Reverb, Room Reverb, Transient Shaping, Parametric EQ, High-Pass Filter, Low-Pass Filter, Clip Gain, Air Frequency EQ, Oscillator, ADSR, Vocoder, Wavetable Synthesis, Additive Synthesis
- All new quotes: real person, real role, real source URL
- Delivered: /mnt/user-data/outputs/quotes.json
- Steve action required: drop into C:\Users\swarn\OneDrive\Desktop\mpw-scripts\

### 4. _headers — Netlify CSP File — DELIVERED

- Allows unsafe-inline scripts on /bible/* pages
- Steve action required: commit _headers to GitHub repo root (same level as articles/ and bible/)

### 5. chorus.html — Regenerated Twice This Session

- Tool still non-functional on Netlify (old tools file on Steve's machine)
- Word count shows 36 min — word counter fix deployed but this HTML predates it; next regen shows ~22 min
- Verdict wrapper: div.producers-verdict still missing (P0b fix not yet applied to writer)
- Misconception block placement: appears before definition prose — should be after Parameters — PENDING

## P0 — mpw_tools_v3.py Delivery Options for Session 45

Option A — Python patch script (RECOMMENDED): Write a script that reads Steve's existing mpw_tools_v3.py and applies ONLY the LFO fixes. Smallest delta, no full file delivery. If encoding issues, escalate to Option C.

Option B — PowerShell here-string: Write entire file as @'...'@ | Set-Content -Encoding UTF8. Bypasses artifact download. Risk: PowerShell here-string escaping issues.

Option C — Base64 decode (most reliable):
  [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('...')) | Set-Content -Path "...\mpw_tools_v3.py" -Encoding UTF8
  Guaranteed encoding-safe delivery.

## P0b — Verdict Wrapper Fix Required in mpw_bible_writer.py

Pass 2 writes verdict-header/lead/grid WITHOUT the div.producers-verdict wrapper. All verdict CSS fails.

Required structure:
  <section class="entry-section" id="verdict">
    <h2 class="sr-only">The Producer's Verdict</h2>
    <div class="producers-verdict">   <- THIS WRAPPER IS MISSING
      <div class="verdict-header">...</div>
      <p class="verdict-lead">...</p>
      <div class="verdict-grid">...</div>
      <div class="mpw-share-bar"></div>
      <p class="verdict-close">...</p>
    </div>
  </section>

Fix in build_html_t1(): inject wrapper programmatically after Pass 2 returns content, or add explicit instruction to Pass 2 prompt.

## Key File State End of Session 44

| File | Location | Status |
|---|---|---|
| mpw_bible_writer.py v5.2 | Claude container (2904 lines) — NOT persistent | NOT on Steve's machine — rebuild next session |
| mpw_tools_v3.py FIXED | install_tools_v3.ps1 delivered — run to install | **Run .\install_tools_v3.ps1 to write to mpw-scripts\** |
| mpw_tools_v3.py.bak | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ | Encoding-corrupted — leave as .bak |
| quotes.json (380 quotes) | Delivered earlier this session | Needs drop into mpw-scripts\ |
| _headers (Netlify CSP) | Delivered earlier this session | Needs commit to GitHub repo root |

## mpw_tools_v3.py — Delivery Resolution (End of Session 44)

The tools file went through multiple failed delivery attempts this session. Root cause chain:

1. Claude artifact download → Cloudflare saves as wrong encoding (UTF-8 bytes as cp1252/Latin-1)
2. The uploaded `mpw_tools_v3_py.bak` was the correct 1174-line self-contained new version BUT double-encoded — AND the triple-quoted Python strings had their closing `"""` stripped by the corruption, making the file structurally broken (not just a character replacement fix)
3. PowerShell byte-loop patches failed because the byte sequences were cp1252-encoded, not raw UTF-8 E2 80 94
4. The old `mpw_tools_v3.py` in mpw-scripts\ imports from `build_preview.py` (which doesn't exist) — it was never self-contained

**Final fix applied this session:**
- Decoded bak file: strip BOM → decode UTF-8 → encode cp1252 → decode UTF-8 (recovers original chars)
- Replaced all non-ASCII with ASCII/HTML entity equivalents (em dashes → `--`, degree → `&deg;`, etc.)
- Found and re-inserted missing `"""` closing quotes in all 11 affected tool functions using AST-guided insertion before each `_wrap(` call
- Verified all 12 tools render correctly (tested: compression, delay, limiting, eq, reverb, oscillator, adsr, gain-staging, headroom, stereo-imaging, chorus, lfo — all OK)
- Delivered as `install_tools_v3.ps1` — base64-encoded PowerShell script that writes raw bytes directly, bypassing all encoding issues

**To install:**
```powershell
.\install_tools_v3.ps1
```
Writes `mpw_tools_v3.py` (1185 lines, all ASCII, syntax clean, all 12 tools working) to mpw-scripts\.

**Then test:**
```powershell
python mpw_bible_writer.py --test --slug chorus --term "Chorus" --category "Time-Based" --tier 1 --no-commit
```

## New NEVER Rules Added Session 44

| Rule | Detail |
|---|---|
| NEVER deliver .py files via Claude artifact download | Cloudflare/browser encoding corruption guaranteed — use PowerShell here-string or base64 PS script instead |
| NEVER use innerHTML for card population in tool JS | Netlify CSP headers block innerHTML on /bible/* pages — always use createElement/appendChild |
| lfoCalc and lfoCopy MUST be assigned to window.* | oninput/onclick HTML attributes cannot access functions not on the window object |
| NEVER try to patch encoding-corrupted Python files with byte replacement | If triple-quoted strings have lost their closing delimiters, byte replacement cannot fix structural corruption — must use AST-guided reconstruction or base64 delivery |
| ALWAYS deliver large .py files via base64 PowerShell script | Write raw bytes with [System.IO.File]::WriteAllBytes() — the only guaranteed encoding-safe delivery method |

## Confirmed All 223 Live Slugs (unchanged from Session 41)

v5.1 original 16:
compression, eq, limiting, saturation, distortion, multiband-compression, parallel-compression, noise-gate, reverb, delay, convolution-reverb, plate-reverb, room-reverb, gain-staging, headroom, stereo-imaging

Session 40 new 54:
chorus, flanger, phaser, tremolo, vibrato, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, air-frequency-eq, resonance, harmonic-distortion, mid-side-processing, bus-compression, mix-bus, send-return, automation, clip-gain, mastering, loudness-normalization, true-peak-limiting, lufs, dynamic-range, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, sidechain-compression, transient-shaping, pitch-shifting, time-stretching, recording, midi, arrangement, mixing, sampling, compression-ratio, attack-release, threshold, bit-depth, sample-rate, latency, daw, audio-interface, microphone-placement, vocal-production, beat-making, sound-design, music-theory

v3.0/v4.0 153:
808, air, analog, arpeggiator, attack, audio-routing, audio-track, automation-clip, aux-send, bell-curve, bible-index, boom-bap, bounce, bpm, breakdown, bridge, buffer-size, bus, call-and-response, chop, chord, chord-progression, chorus-section, clip, clipping, clocking, condenser-microphone, daw-workflow, dbfs, de-esser, decay, detune, di-box, digital, dithering, drill, drop, dynamic-eq, dynamic-microphone, exciter, expansion, fader, feedback, fet-compressor, filter, freeze, frequency, frequency-masking, fundamental, gain, gain-reduction, gain-structure, glue, granular-synthesis, graphic-eq, groove, hall-reverb, harmonic, harmony, hook, humanization, impedance, instrument-track, integrated-loudness, interval, intro, key, knee, layering, linear-phase-eq, lo-fi, loudness, loudness-matching, loudness-war, makeup-gain, master-limiter, melody, meter, mid-side-eq, mix-translation, mode, modulation, mono-compatibility, mud, noise-floor, notch-filter, octave, optical-compressor, outro, overdrive, panning, parallel-processing, patch, pdc, peak, phantom-power, phase, phase-cancellation, phonk, ping-pong-delay, pitch, plugin, polar-pattern, polyrhythm, portamento, pre-delay, preamp, presence, q-factor, quantization, ratio, reference-mastering, reference-track, release, return-track, rhythm, rms, sample-flip, scale, shelf, shimmer-reverb, short-term-loudness, sidechain, signal-chain, slapback-delay, space, spring-reverb, stem, stem-mastering, stereo-width, subfrequency, summing, swing, syncopation, tempo-sync, tension-release, the-pocket, timbre, time-signature, transient, transient-shaper, trap, true-peak, tube-compressor, unison, vca-compressor, velocity, verse, vst, waveform, wavetable, wet-dry, white-noise

# SESSION_APPEND_ZONE

---

# ⛔ SESSION 45 UPDATE — May 20, 2026

## Session 45 Confirmed State at Start
- Articles: **526** live (unchanged)
- Bible entries: **223 total** (unchanged)
  - 15 v5.1 original — nav working on real iPhone ✅ — tools working ✅
  - 1 v5.1 (compression) — nav broken (different impl) — regenerate with v5.2 ❌
  - 54 v5.1 Session 40 — content issues — regenerate with v5.2 ❌
  - 153 v3.0/v4.0 legacy — untouched ✅

## Session 45 — What Was Completed

### P0 — mpw_tools_v3.py CONFIRMED INSTALLED
- install_tools_v3.ps1 ran successfully (delivered Session 44)
- mpw_tools_v3.py confirmed installed: 1185 lines, all ASCII, syntax clean
- `python -c "import mpw_tools_v3; print('OK')"` → OK ✅
- `mpw_tools_v3.build_tools_section_v3('chorus','Chorus')` → returns 20,729 chars with LNOTES, lfoCalc, BPM-Synced content ✅
- `mpw_tools_v3.TOOL_OVERRIDES.get('chorus')` → `'lfo'` ✅

### P0b — mpw_bible_writer.py v5.2 REBUILT AND INSTALLED
Full v5.2 writer rebuilt from scratch in container applying ALL FIX 13–FIX 30 plus Session 44 additions. Delivered via 3-part base64 PS1 scripts (132KB each, under Cloudflare 200KB limit).

**Delivery scripts used (these work — Unblock-File first):**
- install_bible_writer_v52_part1.ps1
- install_bible_writer_v52_part2.ps1  
- install_bible_writer_v52_part3.ps1

**Install command:**
```powershell
Unblock-File .\install_bible_writer_v52_part1.ps1; Unblock-File .\install_bible_writer_v52_part2.ps1; Unblock-File .\install_bible_writer_v52_part3.ps1; .\install_bible_writer_v52_part1.ps1; .\install_bible_writer_v52_part2.ps1; .\install_bible_writer_v52_part3.ps1
```

**CONFIRMED on Steve's machine:**
- Written: 202,024 bytes (varies slightly by build)
- Syntax: CLEAN (confirmed via `python -c "import ast; ast.parse(open(r'path', encoding='utf-8').read()); print('SYNTAX CLEAN')"`)
- Note: The part3 script uses `open(r'$dest')` without encoding — this fails on Windows (cp1252 error). Harmless — the file IS written correctly. Use explicit encoding check separately.

**Writer state in Claude container (END OF SESSION 45):**
- File: /home/claude/mpw_bible_writer.py
- Lines: 2,967
- Bytes: 203,027 (UTF-8)
- Syntax: CLEAN
- All 24/24 feature checks PASS (see BIBLE handoff Session 45 update)

### Chorus Test Run Results
chorus --test --no-commit ran successfully. chorus.html generated (187KB). The v3 LFO tool IS rendering in the page (formula box, rate ranges, depth guide, stereo phase block, waveform grid all visible). HOWEVER the BPM-Synced rate cards (lcards div) are empty and non-functional.

### Tool Rendering — Root Cause FULLY DIAGNOSED

**The chain:**
1. Pass 2 ignores TOOLS_PLACEHOLDER and writes its own LFO tool (the simple 2-input version with lfo-b, lfo-d IDs) inside `<section class="entry-section" id="tools">` — this appears TWICE in the output (once after Quick Ref where it injected its tool, and again near the bottom of the page)
2. FIX 22b regex `_tools_pat = _re2.compile(r'<section[^>]+id=.{0,3}tools.{0,3}[^>]*>.*?</section>', _re2.DOTALL)` with `count=1` correctly replaces the FIRST occurrence with the v3 tool
3. The SECOND occurrence (at the bottom of the page) remains — it still has the old simple tool with a `<script>` block that calls `calc()` using `lfo-b` and `lfo-d` element IDs
4. The v3 tool also uses `lfo-b` and `lfo-d` IDs (confirmed from mpw_tools_v3.py structure) — duplicate IDs in the DOM
5. The v3 tool's `lfoCalc()` calls `document.getElementById('lcards')` — but `lcards` ID may conflict or the second tool's script interferes with initialization
6. Result: v3 tool header/body renders correctly but `lcards` div stays empty

**THE FIX (P0 for Session 46 — CRITICAL):**
Change FIX 22b in build_html_t1() to use `count=0` (replace ALL occurrences) instead of `count=1`. This removes both Pass 2 tool sections and injects the v3 tool once in the correct position.

**Exact change needed in mpw_bible_writer.py:**

In the FIX 22b block, change:
```python
_replaced = _tools_pat.sub(tools_html, html, count=1)
```
To:
```python
# Replace ALL occurrences — Pass 2 sometimes writes tools section twice
_replaced = _tools_pat.sub('', html, count=0)  # remove all first
# Then inject v3 tool after quick-reference
_sig = '</section>\n<section class="entry-section" id="signal-chain">'
_hist = '</section>\n<section class="entry-section" id="history">'
if _sig in _replaced:
    _replaced = _replaced.replace(_sig, '</section>\n' + tools_html + '\n<section class="entry-section" id="signal-chain">', 1)
elif _hist in _replaced:
    _replaced = _replaced.replace(_hist, '</section>\n' + tools_html + '\n<section class="entry-section" id="history">', 1)
html = _replaced
```

This guarantees: (a) all Pass 2 tool sections are stripped, (b) v3 tool appears exactly once in correct position, (c) no duplicate IDs in DOM, (d) lfoCalc() finds exactly one lcards div.

**Secondary suspicion:** The v3 LFO tool in mpw_tools_v3.py on Steve's machine uses `setTimeout(lfoCalc, 0)` for init. The `lcards` div is populated by `lfoCalc()` via `createElement/appendChild`. If this is working for standalone lfo_test.html but not in chorus.html, the issue may be that the script block is executing before the lcards container div is in the DOM (because the tool appears mid-page). Adding `window.addEventListener('load', lfoCalc)` as a fallback would resolve this. But the duplicate ID / duplicate script issue is the primary root cause and must be fixed first.

## Key File State End of Session 45

| File | Location | Status |
|---|---|---|
| mpw_bible_writer.py v5.2 | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ | INSTALLED — 202,024 bytes — SYNTAX CLEAN — FIX 22b still has count=1 bug |
| mpw_tools_v3.py (1185 lines) | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ | INSTALLED — confirmed working — 20,729 char LFO tool |
| mpw_tools_v3.py.bak | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ | Leave as .bak — encoding-corrupted |
| quotes.json (380 quotes) | Delivered Session 44 | **Steve must drop into C:\Users\swarn\OneDrive\Desktop\mpw-scripts\** |
| _headers (Netlify CSP) | Delivered Session 44 | **Steve must commit to GitHub repo root** |
| chorus.html | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ | 187KB — v3 LFO tool rendering but lcards empty — DO NOT COMMIT |

## New NEVER Rules Added Session 45

| Rule | Detail |
|---|---|
| NEVER use $env:SRCDIR in delivery scripts | setenv.ps1 does NOT set SRCDIR — only sets ANTHROPIC_API_KEY and GITHUB_TOKEN — always hardcode path C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ |
| NEVER use Python -c for multi-line scripts with quotes in PowerShell | PowerShell mangles nested quotes — always use heredoc @"..."@ or write to a .py file |
| NEVER validate writer install with open() without encoding='utf-8' | Python 313 on Windows defaults to cp1252 — always specify encoding='utf-8' |
| NEVER use count=1 in FIX 22b regex substitution | Pass 2 writes tools section TWICE — must remove ALL occurrences then inject once |
| NEVER declare tool fix working without checking lcards population | The v3 LFO tool header can render while lcards stays empty — visual check of the cards grid is required |
| NEVER download PS1 files without Unblock-File before running | Windows security blocks unsigned scripts — always Unblock-File immediately after download |

## Priority Queue for Session 46

| Priority | Task | Detail |
|---|---|---|
| **P0** | Fix FIX 22b count=1 bug in writer | Change to remove ALL tool sections then inject once — see exact fix above |
| **P0b** | Deliver fixed writer via 3-part PS1 | Rebuild delivery scripts after fix |
| **P0c** | Run --test chorus --no-commit | Verify lcards populate AND only one id="tools" in output |
| **P0d** | Run diagnostic on output | `@" c=open('chorus.html',encoding='utf-8').read(); print('id_tools_count:', c.count('id="tools"')); print('lcards:', 'lcards' in c); print('lfoCalc:', 'lfoCalc' in c) "@ | python` |
| **P1** | Run --validate | Target: 89/89 (80 v5.1 + 9 new v5.2 checks) |
| **P2** | Open chorus.html locally and confirm | Nav advances on iPhone, LFO cards populate, read time ~22 min, Signatures section present, Producer Spotlight has ps-move |
| **P3** | 3-entry batch test | `python mpw_bible_writer.py --batch-file bible-v52-test3.txt --start-date 2026-05-20 --workers 4` |
| **P4** | Full regen 70 v5.1 entries | `python mpw_bible_writer.py --batch-file bible-tier1-remaining34.txt --start-date 2026-05-20 --workers 8` — ~$21, ~25 min |
| **P5** | `python mpw_bible_cat_pages.py --run` | After regen |
| **P6** | `gen_sitemap.py → GSC` | After cat pages |
| **P7 (Steve)** | **Affiliate applications** | Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox — **REVENUE BLOCKER** |

## Steve Pending Actions (MUST DO BEFORE NEXT SESSION)
1. Drop quotes.json into C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ (delivered Session 44)
2. Commit _headers to GitHub repo root — same level as articles/ and bible/ (delivered Session 44)
3. Affiliate applications (P7 above) — REVENUE BLOCKER

## Infrastructure Notes (Permanent Reference)
- setenv.ps1 sets ONLY: ANTHROPIC_API_KEY and GITHUB_TOKEN — no SRCDIR
- All delivery scripts must hardcode path: C:\Users\swarn\OneDrive\Desktop\mpw-scripts\
- Python 313 on Windows — always use encoding='utf-8' when opening .py files
- Files over 200KB intercepted by Cloudflare — split PS1 delivery into 2 parts (132KB each)
- Downloaded PS1 files must be Unblock-File'd before running
- mpw_bible_writer.py is NOT in GitHub repo — local copy only
- mpw_tools_v3.py IS installed locally but NOT in GitHub repo

