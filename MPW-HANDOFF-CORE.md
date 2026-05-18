# MusicProductionWiki.com — CORE Handoff
*Updated: May 18, 2026 (SESSION 38) · 526 articles + 226 Bible entries live*
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

---

# ⛔ RULE 4 — PRIORITY QUEUE

| Priority | Task | Status |
|---|---|---|
| P0 | Tool suite research + rebuild (all 13 tools) | NEXT SESSION — research 12 remaining tool types before building |
| P0.1 | Run patch_live_tools.py to inject correct tools into 16 live entries | BLOCKED on tool rebuild — do tool research first |
| P1 | Run remaining 34 Tier 1 Bible entries | BLOCKED on tool rebuild + patch_live_tools |
| P2 | Run mpw_bible_cat_pages.py --run | After Tier 1 batch complete |
| P3 | gen_sitemap.py → resubmit to GSC | After cat pages |
| P4 | mpw_dead_slug_audit.py | After each batch commit |
| P5 | Batch 09 (100 track breakdowns) | After Tier 1 |
| P6 | Affiliate applications | REVENUE BLOCKER — Steve action required |
| P7 | Fix 5 missing og:image (mpw_fix_meta.py) | Low priority |
| P8 | Add netlify.toml redirect /dictionary/* → /bible/:splat | Pending owner action |

---

# ⛔ RULE 5 — CURRENT SESSION STATE

## Session 38 — What Was Completed

### 1. 16 Bible Entries Built and Committed (Tier 1 v5.1)

**SHA d0b0abbc** — 15 entries batch committed:
eq, limiting, saturation, distortion, multiband-compression, parallel-compression, noise-gate, reverb, delay, convolution-reverb, plate-reverb, room-reverb, gain-staging, headroom, stereo-imaging

**Earlier in session** — compression committed as solo test entry (SHA not separately recorded).

All 16: 12,000–13,500 words, 158–169KB, 80/80 validation checks. Full page renders, sidebar visible, nav tracking works on all 16.

### 2. mpw_bible_writer.py — Fixed and Delivered

The writer went through multiple patch failures this session. The confirmed-clean version was delivered to outputs and is the baseline for next session.

**Confirmed state of delivered writer:**
- Syntax: CLEAN (verified with ast.parse)
- TOOL_OVERRIDES: DEFINED (all 13 tools mapped)
- build_html_t1, PASS2_SYSTEM_T1, build_tools_section: ALL PRESENT
- --workers flag: PRESENT (ThreadPoolExecutor, default 4, max 8)
- SC = '</' + 'script>': DEFINED
- _delay function: html= and return lines PRESENT
- Tools nav pill: AFTER Quick Ref ✅
- Tools sidebar TOC: AFTER Quick Ref ✅
- Validation suite: 80/80

### 3. fix_writer.py — Delivered

Patch script that fixes two bugs in any broken mpw_bible_writer.py:
- BUG 1: SyntaxError in _freq, _gs, _hr, _chord js= strings (bare unescaped single quotes at innerHTML=)
- BUG 2: TOOL_OVERRIDES not defined (referenced but never assigned)

### 4. patch_live_tools.py — CONFIRMED CORRECT, NOT YET RUN

Script imports build_tools_section and TOOL_OVERRIDES from local mpw_bible_writer.py. Fetches all 15 non-compression entries from GitHub, replaces tools section with correct tool per slug, commits in one Trees API call. NOT RUN because tools visual quality was rejected — needs tool rebuild first.

### 5. Tools Visual Standard — Approved Direction

Delay Time Calculator preview built and approved by Steve as visual direction:
- Full MPW/Producer's Bible branding (amber border, diamond mark, Interactive Tool badge)
- Tap Tempo button
- Click any card to copy value to clipboard
- 13 note values (Whole through 32nd, straight/dotted/triplet)
- Hz displayed on every card
- Values in seconds when >1000ms
- Dotted 8th highlighted as "Most Used" (★)
- Contextual callouts that change per BPM (e.g. "120 BPM: The Edge's dotted 8th at 375ms")
- Share bar (Copy Link + X + Reddit) + ◆ The Producer's Bible mark

**All 13 tools must be rebuilt to this standard in next session.**

### 6. Competitor Research — Delay Tool Only

Researched: anotherproducer.com, nickfever.com, tools4music.com, soundplate.com, app store listings.
NOT yet researched: 12 remaining tool types (LUFS, frequency reference, RT60, note-to-freq, ADSR, gain staging, headroom, stereo width, LFO rate, chord/key, GR calculator upgrade).
**Next session must research all 12 before building.**

---

# ⛔ RULE 6 — LIVE SITE STATE

## Bible Entries — Live on GitHub/Netlify

**16 Tier 1 entries live (v5.1 template):**
compression, eq, limiting, saturation, distortion, multiband-compression, parallel-compression, noise-gate, reverb, delay, convolution-reverb, plate-reverb, room-reverb, gain-staging, headroom, stereo-imaging

**210 entries live (v3.0/v4.0 template — not yet upgraded):**
All remaining slugs in CONFIRMED_LIVE_SLUGS list

**Current tools state on live entries:**
- compression: GR Calculator (correct) ✅
- All other 15 entries: old GR Calculator (wrong tool for these slugs) ⚠️
- Tools section IS present and renders, just shows wrong tool
- Tools nav pill: after Quick Ref ✅ (correct position)
- Tools sidebar TOC: after Quick Ref ✅ (correct position)

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

- bible-upgrade-tier1.txt — 50 Tier 1 Bible rewrites — in mpw-scripts\ — 16 DONE, 34 REMAINING
  Format: slug:Term:Category:1
  Done: compression, eq, limiting, saturation, distortion, multiband-compression, parallel-compression, noise-gate, reverb, delay, convolution-reverb, plate-reverb, room-reverb, gain-staging, headroom, stereo-imaging
  Remaining: 34 entries — create bible-tier1-remaining34.txt before running
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
Should show 34 lines. Then: `python mpw_bible_writer.py --batch-file bible-tier1-remaining34.txt --start-date 2026-05-18 --workers 8`

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

# Tool Suite — 13 Tools Mapped (Session 38)

All 13 tools are defined in TOOL_OVERRIDES in mpw_bible_writer.py and routed in build_tools_section(). Visual quality approved direction (Delay Time Calculator preview). All 13 need full rebuild next session after competitor research.

| # | Tool Key | Tool Name | Slugs |
|---|---|---|---|
| 1 | gr_calculator | Gain Reduction Calculator | compression, saturation, distortion, parallel-compression, multiband-compression, noise-gate, bus-compression |
| 2 | delay_calculator | Delay Time Calculator | delay, plate-reverb, automation |
| 3 | lufs_calculator | LUFS Target Calculator | limiting, lufs, mastering, loudness-normalization, true-peak-limiting |
| 4 | frequency_reference | Frequency Band Reference | eq, parametric-eq, high-pass-filter, low-pass-filter, shelving-eq, air-frequency-eq, resonance, harmonic-distortion |
| 5 | rt60_calculator | RT60 Reverb Calculator | reverb, convolution-reverb, room-reverb |
| 6 | note_freq | Note → Frequency Reference | oscillator, fm-synthesis, wavetable-synthesis, additive-synthesis, vocoder, subtractive-synthesis |
| 7 | adsr_visualizer | ADSR Envelope Visualizer | adsr, envelope |
| 8 | gain_staging | Gain Staging Calculator | gain-staging, send-return, clip-gain |
| 9 | headroom_calc | Headroom Calculator | headroom, mix-bus |
| 10 | stereo_width | Stereo Width Visualizer | stereo-imaging, mid-side-processing |
| 11 | lfo_sync | LFO Rate → BPM Sync | lfo, chorus, flanger, phaser, tremolo, vibrato |
| 12 | chord_key | Chord & Key Reference | (music-theory slugs) |
| 13 | (GR Calculator is #1 — 12 unique tool types) | | |

Competitor research status:
- delay_calculator: RESEARCHED ✅ (anotherproducer, nickfever, tools4music, soundplate)
- All other 11 tool types: NOT YET RESEARCHED — must research before building

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
