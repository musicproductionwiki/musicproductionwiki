# MPW Commit SHA Log
*Append-only. Never edit existing lines. One line per commit.*

| Date | SHA | File | Description |
|------|-----|------|-------------|
| 2026-05-26 | adf4c666 | tools/suno-prompt-optimizer.html | RESTORE — reverted to fd5123eb (pre-session-68 working version) |
| 2026-05-26 | ab9f7e47 | tools/suno-prompt-optimizer.html | fix: remove style.css, restore .hero/.container (still broken) |
| 2026-05-26 | 65b609ef | tools/suno-prompt-optimizer.html | fix: rename .hero to .tool-hero (still broken — style.css still loading) |
| 2026-05-26 | d76ec27e | tools/suno-prompt-optimizer.html | fix: add /css/style.css absolute path (caused 600px black shapes) |
| 2026-05-26 | 43756aa3 | tools/suno-prompt-optimizer.html | fix: remove ../css/style.css (still broken) |
| 2026-05-26 | fd0548cd | tools/suno-prompt-optimizer.html | fix: close mpw-nav-wrap div (still broken) |
| 2026-05-26 | 81439176 | tools/suno-prompt-optimizer.html | rebuild: Suno v4 — wrong design system, broken |
| 2026-05-26 | 25645183 | tools/suno-prompt-optimizer.html | fix: Suno v3d JS syntax (still broken) |
| 2026-05-26 | 9e57bb54 | tools/suno-prompt-optimizer.html | fix: Suno v3b (still broken) |
| 2026-05-26 | 1d0680b8 | tools/suno-prompt-optimizer.html | feat: Suno v3 glassmorphism (broken — Python-in-JS) |
| 2026-05-26 | 719a8376 | tools/suno-prompt-optimizer.html | feat: Suno v2 redesign (broken) |
| 2026-05-26 | fd5123eb | tools/suno-prompt-optimizer.html | GOOD — revert: restore to original working version (pre-session-68) |
| 2026-05-25 | 60848615 | tools/ai-music-rights-navigator.html | Tool #2 built and live |
| 2026-05-25 | 3672b6d4 | tools/suno-prompt-optimizer.html | fix: correct model name to claude-sonnet-4-5 |
| 2026-05-25 | de45ae2b | favicon.svg + all pages | add: MPW favicon SVG waveform bars |
| 2026-05-25 | 398e59345 | tools/suno-prompt-optimizer.html + tools/index.html + sitemap + search-index | Session 67: Suno tool + AI rights navigator + infrastructure |
| 2026-05-26 | 115f46e1 | MPW-HANDOFF-BIBLE.md | S73 BIBLE merge: entry count 226→223 (GitHub audit), gold standard updated to reverb.html v1.6, S61 count corrected |
| 2026-05-26 | 92b06d41 | MPW-SESSION-START.md | S74: S75 plan added, priorities updated |
| 2026-05-26 | 72aea370 | MPW-HANDOFF-MERGE-PLAN.md | S74: MPW-NEVER-RULES.md as 7th master doc, Session 75 section added |
| 2026-05-26 | e692daf9 | MPW-NEVER-RULES.md + MPW-SESSION-START.md + MPW-HANDOFF-MERGE-PLAN.md | S75: Add MPW-NEVER-RULES.md (7th master doc) — 95 rules — update SESSION-START top 20 + MERGE-PLAN ✅ |
| 2026-05-26 | a565a93f | js/main.js | S71: SEARCH_INDEX +222 Bible +41 Tool entries with correct URLs |
| 2026-05-26 | c45959b3 | js/main.js | S71: search URL fix attempt (window.location.origin) — superseded |
| 2026-05-26 | 17142bd9 | articles/*.html (526 files) | S71: fix renderItem() — bible/ and tools/ slugs route correctly — Trees API |
| 2026-05-27 | ba94b314 | index.html | S71: renderItem fix — bible/ and tools/ slugs route correctly |
| 2026-05-27 | a47608b0 | tools/index.html | S71: renderItem fix — tools/index search |
| 2026-05-27 | f162f141 | categories/*.html + about.html (90 files) | S71: renderItem fix — all category pages and about |
| 2026-05-27 | fb32b50e | tools/*.html (35 files) | S72: Full MPW nav injected on 35 NO_NAV tools |
| 2026-05-27 | 3831e5a1 | tools/ai-music-ddex-checker.html + ai-music-rights-navigator.html + suno-prompt-optimizer.html + tools/index.html | S72: Manual nav fixes — ddex stub replaced, navigator wired, suno-optimizer overlay added, index style.css removed |
| 2026-05-27 | a3ee22ff | tools/*.html + tools/index.html (42 files) | S72: MISTAKE — nav-search-btn added to media query show list — broke hamburger on all tools |
| 2026-05-27 | db467a8b | tools/*.html + tools/index.html (42 files) | S72: Revert — restored correct media query, hamburger working again |
| 2026-05-27 | f5cb1694 | tools/index.html | S72: Remove duplicate navMob handler, add overflow-x:hidden, restore dark background |
| 2026-05-27 | 5a615e07 | tools/*.html + tools/index.html (42 files) | S72: Mobile eyeglass override injected after nav CSS </style> close — correct DOM position |
| 2026-05-27 | adf7ff2e | tools/index.html | S72: Restore correct media query on index + remove stale eyeglass override blocks |
| 2026-05-27 | 967f1cf2 | og-image.png | S73: Add OG social preview image — 1200x630px glassmorphic brand card |
| 2026-05-27 | ab2faf98 | tools/*.html (41 files) | S73 Batch A: og:image + www. canonical fix + overflow-x on all 41 tools |
| 2026-05-27 | 5e54f584 | tools/*.html (41 files) | S73 Batch B: standardize share row — flex nowrap, Copy/X/Reddit on all 41 tools |
| 2026-05-27 | 67bc8334 | tools/*.html (36 files) | S73 Batch D: add embed mode (?embed=true) to 36 tools missing it |
| 2026-05-27 | e021c66c | tools/suno-prompt-optimizer.html + ai-copyright-strength.html + ai-music-ddex-checker.html + suno-credits-calculator.html | S73 Batch E: suno drawer 2-col grid, thc-right clip fix, footer www. fix |
| 2026-05-27 | 3d278d0d | tools/*.html (41 files) | S73: Hide backToTop arrow + standardize footer on all 41 tools |
| 2026-05-27 | 4d8530e9 | tools/*.html (39 files) | S73: Remove Interactive Tool badge from card headers — all 39 tools with a card |
| 2026-05-27 | 0d30f23b | tools/*.html (21 files) | S73: Fix tool card names — 21 mismatches corrected to match H1 titles |
| 2026-05-28 | 3c638d11 | bible/compression.html | S77: Bible tools count/URL fix — dynamic JS count, .html hrefs |
| 2026-05-28 | 4735c584 | bible/compression.html | S77: All 41 tool hrefs .html extension fix |
| 2026-05-28 | 4b9d1685 | bible/compression.html | S77: Genre table mobile row height (initial attempt) |
| 2026-05-28 | e251e703 | bible/compression.html | S77: Fix-It scroll removed (scrollIntoView) |
| 2026-05-28 | ba6aa61f | bible/compression.html | S77: GR calculator 4-column → 2×2 on mobile |
| 2026-05-28 | f0600018 | bible/compression.html | S77: compression.html v1.0 — full flagship entry — 25 sections — 241KB |
| 2026-05-28 | 7bcc86f7 | bible/compression.html | S78: 8 strategic share bars, Fix-It accordion, entry nav IntersectionObserver, citation block (APA/MLA/Chicago/Harvard), version changelog, What to Read Next, footer upgrade |
| 2026-05-28 | 991b5205 | bible/compression.html | S78: genre table mobile fix (min-width+table-layout), embedded calculator share, mix translation share, share button colors |
| 2026-05-28 | d1314123 | bible/compression.html | S78: Remove redundant calculator share, share-x white text !important, genre table fixed layout, embed code snippet |
| 2026-05-28 | 9de422e2 | bible/compression.html | S78: Share bars full-width row layout globally, genre table CSS grid (mobile card layout), all 6 share bars rebuilt with mpw-share-btns wrapper |
| 2026-05-28 | 23e74048 | MPW-HANDOFF-CORE-new.md + MPW-HANDOFF-BIBLE-new.md + MPW-HANDOFF-SCRIPTS-new.md + MPW-HANDOFF-CONTENT-new.md + MPW-NEVER-RULES-new.md + MPW-TOOL-SESSION-PLAN.md + MPW-FLAGSHIP-WRITER-BLUEPRINT.md | S79: Tool session plan, flagship writer blueprint, all handoffs updated — 7 files |

## Session 80 — May 29, 2026

| Date | SHA | Files | Description |
|------|-----|-------|-------------|
| 5-29 | `3e6b946` | tools/mix-fingerprint.html, tools/loudness-penalty.html, tools/index.html | S80: Mix Fingerprint Analyzer + Loudness Penalty Calculator + Hub Redesign (three-zone) — BROKEN Zone 1 |
| 5-29 | `7e4ae55` | tools/index.html | S80: Hub fixes — remove Zone 1 hero, flagship label, fix Mix Fingerprint card to live |
| 5-29 | `dec2923` | tools/index.html | S80: Restore original tools hub hero + flagship section + Mix Fingerprint live card |
| 5-29 | `f94b476` | tools/mix-fingerprint.html | S80: Mix Fingerprint full rebuild — contrast fix, written diagnosis, timeline analysis, playback predictions — LAST KNOWN GOOD MFP |
| 5-29 | `adf1e04` | tools/mix-fingerprint.html | S80: REVERT mix-fingerprint nav — restore slim tool nav, full site nav breaks page |
| 5-29 | `0211c60` | tools/index.html, tools/mix-fingerprint.html | S80: Hub restore + MFP full nav attempt + banner reorder + rethought timeline + related tools bottom |
| 5-29 | `fc8bf41` | tools/mix-fingerprint.html | S80: MFP banner below hero, related tools to bottom, full-track section-based timeline with unique flags |
| 5-29 | `ce91852` | tools/mix-fingerprint.html, tools/index.html | S80: Full nav on MFP (inline CSS + mobile drawer + search), glassmorphism cards, banner removed, hub nav sticky, LP removed from flagship, mobile fixes |
| 5-29 | `898fab4` | tools/index.html | S80: Hub sticky search + category pills bar below nav, glassmorphic backdrop — PILLS NOT WORKING |
| 5-29 | `602ac05` | tools/index.html | S80: Hub sticky bar fix — display:none/block instead of transform, remove overflow from body — STILL BROKEN |
| 5-29 | `a65ac06` | tools/index.html | S80: Hub always-visible fixed pills bar, html overflow-x:clip, mobile search fix — STILL BROKEN |
| 5-29 | `e958de9` | tools/index.html | S80: Hub z-index 8000 on pills bar, mobile search 80% centered — STILL BROKEN |
| 5-29 | `1c9fa54` | tools/index.html | S80: Hub pills bar position:sticky, no overflow on body, sections handle overflow — STILL BROKEN |
| 5-29 | `506ea69` | MPW-HANDOFF-CORE-new.md, MPW-NEVER-RULES-new.md, MPW-HANDOFF-TECH.md, MPW-HANDOFF-SCRIPTS-new.md, MPW-TOOL-BUILD-SPEC.md, MPW-SESSION-START.md | S80: Append S80 updates to all handoff masters |

### S80 Summary
- **Built:** Mix Fingerprint Analyzer (destination tool — Web Audio + D3 + glassmorphism + diagnosis + timeline + playback), Loudness Penalty Calculator (thin — needs revamp)
- **Hub:** Original hero restored, flagship section added (MFP first, FCD, 4 coming soon), nav sticky, 43 tool cards
- **Broken at session end:** Hub subcategory pills not sticky (5 failed attempts — root cause: overflow ancestor conflict not fully isolated), mobile search bar overflows right
- **HEAD:** `1c9fa54` (site) / `506ea69` (handoffs)
- **P0 for S81:** Fix hub sticky pills — fetch live, trace ancestry, find overflow, fix surgically

## Session 81 — May 29, 2026

| Date | SHA | Files | Description |
|------|-----|-------|-------------|
| 5-29 | `22240eb` | tools/index.html | S81: Hub sticky subcategory-pills fix (S80 P0) — completed the truncated `.hub-zone3-count` CSS rule that was the root cause; sticky bar + mobile search width + overflow resolved |
| 5-29 | `839a71a0` | tools/mix-fingerprint.html, sitemap.xml | S81: Mix Fingerprint v2 — validated BS.1770 engine (K-weighting, gated LUFS, 4x true-peak, EBU LRA, phase corr, Welch PSD), de-saturated genre-calibrated radar, honest distance-from-target fit score, platform LUFS verdicts, true-peak alert, measured reference-track upload (shared mpwAxisScores), full SEO/schema; sitemap -> 805 URLs |
| 5-29 | `68d071d1` | genres.html + 8 tool pages | S81: Canonical + og:url -> non-www (verified non-www is primary; www 301s). Only 9 files were www, not site-wide |
| 5-29 | `327bdb1b` | tools/index.html, tools/loudness-penalty.html | S81: Add og:image (ground truth: only 2 of 44 tools were missing it; S72 "35 missing" was already fixed) |
| 5-29 | `e7d5e71b` | 78 files | S81: GA4 double-tracking fix — single source via js/main.js; removed redundant inline gtag from 78 pages that also load main.js (incl. broken G-XXXXXXXXXX placeholder); 16 inline-only pages left as-is |

### S81 Summary
- **Built:** Mix Fingerprint Analyzer v2 (tools gold standard — validated DSP engine, honest scoring, reference A/B). New dev scripts: `mpw_mfp_calibrate.js`, `mfp_engine.js` (-> basis for shared DSP engine).
- **Fixed:** hub sticky pills (S80 P0); GA4 double-tracking (78 files); canonical/og:url -> non-www; og:image on 2 tools.
- **Strategy:** `MPW-MASTER-CHARTER.md` created (read-first doc) — mission, model policy, gold standards, traffic-first phased revenue (data collection = Phase 1, ClearCheck = Phase 3). NOT committed to repo (served root).
- **Ground truth (verified from GitHub):** 526 articles, 235 bible, 89 categories, 44 tools, ~900 HTML; sitemap 805.
- **New NEVER-RULES:** (1) never size a batch from a memory/audit count — grep the live repo first; (2) GA4 single source = js/main.js, never inline-gtag a main.js page; (3) canonical/og:url use non-www (www 301s); (4) live site serves repo files — never commit internal strategy docs to the served root.
- **HEAD:** `e7d5e71b`
- **P0 for S82:** Spec & build the data-collection pipe (Netlify event fn + GA4 custom events). Then: rebuild the handoff system (boot-sequence architecture).
