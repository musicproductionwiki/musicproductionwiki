# MusicProductionWiki.com — CORE Handoff
*Updated: May 17, 2026 (SESSION 33) · 526 articles + 202 Bible entries live*
*Modular format — 6 GitHub files replace single monolithic handoff*

---

# ⛔ RULE 1 — DOCUMENT INTEGRITY

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

| Rule | Detail |
| --- | --- |
| NEVER enable Netlify Pretty URLs | Breaks site |
| NEVER zip over 200KB | Cloudflare intercepts — save via Notepad → Save As → All Files |
| NEVER write partial batches | All articles first, commit once |
| NEVER update index.html for rewrites | Only new filenames need index updates |
| NEVER propose topics without duplicate check | Check MPW-CATALOG.md |
| NEVER deliver under minimum word count | See MPW-HANDOFF-CONTENT.md |
| NEVER use Updated May 2025 | Always 2026 |
| NEVER truncate any handoff module | Full reproduction required |
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
| NEVER deliver a script with Python SyntaxWarning for backslash in docstring | Use double backslash |
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
| NEVER assume all articles use same related-card HTML format | Four different formats found |
| NEVER build new mpw_writer.py without reading MPW-HANDOFF-SCRIPTS.md | New writer must include correct sidebar and nav |
| NEVER run mpw_fix_sitewide_r7.py after homepage updated to newer nav | Always update r7 to match homepage nav first |
| NEVER use old r7 NAV_HTML in mpw_writer.py or mpw_fix_sitewide_r7.py | New homepage nav is the standard |
| NEVER assume aside is direct child of article-layout | JS fix required — baked into mpw_writer.py v3.0 |
| NEVER commit test articles without aside JS fix | Mandatory — baked into v3.0 |
| NEVER use nav-link relative paths (../) | All nav links must be absolute paths starting with / |
| NEVER guess nav-inner max-width or padding | Always fetch live confirmed-working article computed styles |
| NEVER run mpw_fix_sitewide_r7.py without retry session | Use persistent requests.Session with exponential backoff |
| NEVER write new articles without running --test first and visually confirming | mpw_writer.py v3.0 test-first always |
| ALWAYS strip mpw-nav-js script from articles | Old mpw-nav-js in main.js conflicts with new dropdown JS |
| ALWAYS strip ALL search overlay duplicates | patch() runs 20-pass removal |
| ALWAYS use absolute paths in nav links | /about.html, /categories/techniques.html, /bible/, etc. |
| ALWAYS use claude-sonnet-4-6 for new article generation | Mandatory — upgraded Session 21 |
| NEVER run multiagent batch without --dry-run first | Always dry-run then test then full run |
| NEVER run mpw_count.py using old GitHub contents API pagination | Replaced with Trees API version |
| ALWAYS use mpw_slugs.py after every batch commit | Refreshes slugs.txt from live repo |
| NEVER trust local slugs.txt as article count source | Only accurate immediately after mpw_slugs.py |
| NEVER fix title capitalisation in mpw_search_index.py as patch | Correct fix is in article title tags |
| NEVER include main.js on /bible/ pages | Conflicts with Bible page nav JS — crashes silently |
| NEVER write Bible page JS via Python heredoc with single-quote escaping | Use raw string r triple-quote |
| NEVER commit bible-index.json before /bible/index.html exists | Index page must exist first — RESOLVED |
| NEVER use position:absolute for dropdowns inside section with overflow:hidden | Use position:fixed with getBoundingClientRect() |
| NEVER run mpw_bible_writer.py without --test first and visual confirmation | Mandatory — always test before batch |
| NEVER guess Bible entry layout CSS | Always derive from live gold standard via DevTools |
| ANTHROPIC_KEY env var is ANTHROPIC_API_KEY in setenv.ps1 | Script reads ANTHROPIC_API_KEY — also ANTHROPIC_KEY as fallback |
| PASS1_TOKENS must be 20000 for Bible entries | Lower values truncate JSON |
| NEVER run sitewide fix script with parallel blob creation | Always sequential with exponential backoff on 403s |
| ALWAYS run mpw_dead_slug_audit.py after every batch commit | Dead slugs accumulate silently |
| ALWAYS run mpw_slugs.py before every batch write AND after every batch commit | Stale slugs cause dead related-article links |
| NEVER use parallel thread fetching for GitHub Contents API in fix scripts | 15-20 threads triggers secondary rate limit — use 10 max |
| NEVER paste Python code directly into PowerShell | Save as .py file and run python script.py |
| NEVER strip entire style blocks when looking for CSS fingerprints | Nukes all page CSS — use append-only with !important |
| NEVER write Bible page mobile fixes that touch desktop CSS | ALL Bible mobile fixes are @media(max-width:768px) only |
| ALWAYS append mobile CSS as new style block — never strip-and-replace | Append-only approach is correct |
| NEVER guess live HTML structure of Bible page before writing patch | Always fetch live HTML first |
| NEVER run parallel blob creation for GitHub API | Always sequential with 403 backoff |
| NEVER assume GitHub API is reachable from Claude's environment | api.github.com blocked — all GitHub ops from Steve's PowerShell |
| NEVER give Steve browser console commands to paste in PowerShell | Console commands go in Chrome F12 Console only |
| NEVER deliver fix script without verifying target string exists in live file | Multiple scripts failed due to mismatched patterns |
| NEVER build Bible writer without running verification suite first | v5.1 = 75+ check suite — all must pass before delivery |
| ALWAYS verify mpw_bible_writer.py with python3 check script before delivering | Syntax check + content checks — fix any MISSING before delivery |
| NEVER include Spotify iframes or YouTube links in Bible entries | v5.1 uses text-only track citations — Option A confirmed Session 31 |
| Bible batch format is slug:Term:Category:Tier (colon-separated, 4 parts) | Tier field added Session 32 — 1=Flagship, 2=Standard, 3=Reference |
| NEVER patch Bible template incrementally across multiple iterations | One complete rewrite — audit fully — then test once |
| NEVER remove Sound Better from desktop nav | Desktop keeps it — mobile only removal via @media(max-width:768px) |
| NEVER link track examples to any external page | v5.1 uses text-only track citations — no links of any kind |
| NEVER allow producer quote to render with literal asterisks | Strip asterisks in post-processing — wrap in blockquote.producer-quote |
| NEVER allow AI to output related_terms slugs not in CONFIRMED_LIVE_SLUGS | Validate at build time — omit invalid ones silently |
| NEVER run Tier 1 batch before Bible template passes full desktop AND mobile visual QA | --test must pass and be visually confirmed first |
| NEVER commit Bible page with navs not sticky | overflow:clip on html/body — NOT overflow:hidden |
| NEVER commit Bible page with horizontal scroll on mobile | Verify in DevTools mobile emulation before batch |
| ALWAYS audit mpw_bible_writer.py output with python audit script before delivering | Run full 75+ check suite — all must pass |
| NEVER set env vars inline in .py files committed to GitHub | GitHub secret scanning blocks commit — always use env vars |
| ALWAYS set both env vars at start of every PowerShell session | $env:GITHUB_TOKEN and $env:ANTHROPIC_API_KEY — both required |
| NEVER use overflow:hidden on html/body in Bible pages | Use overflow:clip — hidden breaks position:sticky on all descendants |
| NEVER invent article slugs for related-article links | Always verify against CONFIRMED_LIVE_SLUGS |
| NEVER use a progress bar on Bible pages desktop | Replaced by Bible category nav bar — progress bar mobile only |
| NEVER fabricate quotes from real producers | All quotes must come from quotes.json with verified source URL |
| NEVER add quotes to entries without tag matching against quotes.json | Pass 1.5 filters by tag — never invent quotes inline |
| NEVER build Producer Profile pages before Batch 09 exists | Option C sidebar now — Option B full profiles after Batch 09 |
| NEVER build app before 1000 Bible entries + 25000 monthly visitors | Milestone trigger — revisit then |
| NEVER use identity bar on Bible pages | Removed Session 31 — MPW slim bar + Bible bar replace it |
| NEVER use Sections label in entry nav | Removed Session 31 — pill links only no label |
| ALWAYS set scroll-margin-top on all Bible section headings | 128px desktop / 110px mobile (updated Session 33) |
| NEVER use the old Bible nav stack (identity bar + main nav + entry nav) | New stack: MPW slim bar + Bible bar + entry nav — Session 31 locked |
| NEVER include a "Coming Soon" audio demo placeholder | Delete it — placeholder signals incompleteness — add only when asset is real |
| NEVER truncate SVG signal chain labels | Full text labels required — no ellipsis — redesign box width if needed |
| NEVER omit a section from the entry nav | All 20 sections must appear as nav pills — Verdict added Session 33 |
| NEVER gate the tool itself | Gate the download/save output only — free tool use is the moat |
| NEVER use Further Reading AND Related Terms as separate sections | Consolidate — Further Reading removed in v5.1 — use "Also in The Bible" only |
| ALWAYS add entry-section class to every section with an ID | Required for sidebar TOC tracking and entry nav tracking JS |
| NEVER build tools category pages before /tools/ hub page exists | Hub page first — category pages second |
| NEVER stack multiple appended CSS style blocks on Bible pages | Causes cascading conflicts — use ONE consolidated override block |
| NEVER hide .bible-bar on mobile | Bible bar must always show as product identity — hide only bb-cats/bb-all/bb-divider on mobile |
| NEVER use stacked append-only CSS when patches conflict | Consolidate all overrides into one style block before committing |
| Every shareable section must have Copy Link + Share on X + Reddit | Three buttons, uniform .mpw-share-btn styling, flex:1 equal width |
| NEVER make share buttons different sizes | Use flex:1 on .mpw-share-btn so all three are always equal width |
| Producer's Verdict must be in the entry nav | 20th pill — id="verdict" on .producers-verdict wrapper |
| Email API gate is bypassed — Kit/Brevo to be wired at P3.5 | openGateFor() fires downloads directly — no modal shown |
| NEVER wire Beehiiv API — use Kit free API at P3.5 | Kit account created, API key in Bible gate API.txt in mpw-scripts\ |

---

# ⛔ RULE 3B — 75% CONTEXT WARNING — MANDATORY

At 75% context, Claude must stop all work immediately and tell Steve:

"I am at approximately 75% context. I will complete the current task only, then update the handoff and stop. A new session is required after this."

This is not optional.

---

# ⛔ RULE 4 — CALL OUT SKIPPED STEPS IMMEDIATELY

If Claude skips a step in the session start checklist, delivers output without required deliverables, or takes action before completing the hard gate — Steve must call it out immediately.

---

# ⛔ RULE 5 — DELIVERABLES CHECKLIST

Every handoff update requires ALL of the following:
- [ ] All 6 MPW-HANDOFF-*.md modules updated in GitHub via Trees API
- [ ] MPW-CATALOG.md auto-regenerated and included in same commit
- [ ] Session log updated in MPW-HANDOFF-CORE.md (Section 21 — keep 3 most recent)
- [ ] Section 2 Priority table updated
- [ ] Section 16 Next Session Start Prompt updated
- [ ] mpw_session_start.py updated if session start logic changed

---

# 2. PRIORITY TABLE (Updated Session 33)

| Priority | Task | Status | Detail |
|---|---|---|---|
| P0 | compression.html v5.1 gold standard committed | COMPLETE Session 33 | Live at bible/compression.html — SHA d5427723 — 170KB — unified share bars — Producer's Verdict in nav — Bible bar always visible |
| P0.1 | mpw_bible_writer.py v5.1 built | COMPLETE Session 33 | 2,387 lines — syntax OK — 80/81 checks vs gold standard — in mpw-scripts\ |
| P0.2 | compression.html visual QA — mobile share bars uniform | IN PROGRESS Session 33 | Share bars have equal-width flex:1 buttons — DAW tab blank yellow box fix pending — sidebar confirmed on desktop — mobile buttons not fully uniform yet |
| P0.3 | Run --test compression on updated writer | NEXT SESSION P0 | Run after compression.html visual QA confirmed clean |
| P0.4 | Run mpw_bible_cat_pages.py --run | After --test confirmed | 8 Bible category pages committed |
| P1 | Build Moat 1 — Glossary Tooltip System | Session 34 after P0 confirmed | data-tooltip system, JS lookup against bible-index.json, CSS tooltip card |
| P1.1 | Build Moat 2 — "Was This Helpful?" feedback | Session 34 after Moat 1 | Level vote + text field + GA4 + Google Form/Sheets backend |
| P1.2 | Build Moat 3 — DAW preference localStorage | Session 34 after Moat 2 | 10 lines JS — localStorage key mpw_daw_pref |
| P2 | Tier 1 batch — 50 Bible rewrites | After P0.3 + P0.4 confirmed | python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-16 |
| P2.1 | Air entry retry | After Tier 1 | python mpw_bible_writer.py --test --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency" |
| P2.2 | Sitemap regeneration + GSC resubmission | After Tier 1 | 202+ Bible entries not yet in sitemap |
| P2.3 | netlify.toml redirect /dictionary/* to /bible/:splat | Pending | 301 redirect for old URLs |
| P3 | Build /tools/ hub page | After Moats 1-3 | Standalone destination — grid of all tools — submittable to Product Hunt |
| P3.1 | Build Delay Time Calculator | On Delay Bible entry | Highest search volume tool — BPM in → all note divisions in ms |
| P3.2 | Build Frequency Reference Tool | On EQ Bible entry | Click a band → instruments that live there + EQ context |
| P3.3 | Build LUFS Target Calculator | On Mastering/LUFS entries | Current LUFS + platform target → headroom needed |
| P3.5 | Wire Kit API to email gate | After affiliate revenue starts | Replace openGateFor() bypass with Kit free API — key in Bible gate API.txt |
| P4 | Batch 09 — 100 track breakdowns | After Tier 1 | python mpw_writer.py --batch batch09.txt --start-date 2026-03-01 |
| P4.1 | Run mpw_dead_slug_audit.py | After Tier 1 commits | Find all dead related-article links |
| P5 | Fix 5 articles missing og:image | mpw_fix_meta.py | Rate limited Session 27 — retry |
| P6 | Affiliate applications | REVENUE BLOCKER | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — Steve must do |
| P7 | Google Workspace email | RESOLVED Session 33 | Fastmail set up at team@musicproductionwiki.com — DNS configured via Netlify — MX/SPF/DKIM all verified |
| P8 | recreations.html category page | Before Batch 11 | Must exist before Batch 11 runs |
| P9 | vocal-autopsies.html category page | Before Batch 12 | Must exist before Batch 12 runs |
| P10 | Producer Profile pages /producers/ | After Batch 09 | Full content pillar — Option B — see Section 32 |
| P11 | Bible subcategory pages | After 500 entries | /bible/categories/dynamics/compression/ etc |
| P12 | Mobile app PWA first then React Native | After 1000 entries + 25K monthly visitors | Milestone trigger |

---

# 16. NEXT SESSION START PROMPT (Session 34)

"Run python mpw_session_start.py. State article count, Bible entry count, P0 priority, and last 5 NEVER rules added.

P0 is completing visual QA on compression.html. The file is live at musicproductionwiki.com/bible/compression. Check these specific issues on both desktop and mobile:
1. Share buttons — are all three (Copy Link / Share on X / Reddit) equal width on mobile AND desktop?
2. DAW tabs — is the first tab (Ableton) showing blank yellow? If yes fix the active state CSS.
3. Sidebar — is the TOC visible on desktop and scrollable?
4. Producer's Verdict — is VERDICT in the entry nav and does it jump to the section?

If any issues remain: fetch the live file, fix in one consolidated CSS block (NOT appended patches), commit. Do not add more than 2 style blocks total to any Bible page.

After visual QA passes: run P0.3 — python mpw_bible_writer.py --test --slug compression --term 'Compression' --category 'Signal Processing' --tier 1. Compare output to live gold standard. Fix discrepancies. Then run P0.4 — mpw_bible_cat_pages.py --run.

Then build Moat 1 (glossary tooltip system). Read HANDOFF-CORE Section 33 spec before building."

---

# 21. SESSION LOG (3 Most Recent)

## May 17, 2026 — SESSION 33 — COMPRESSION.HTML V5.1 GOLD STANDARD + INFRASTRUCTURE

### What Was Built / Completed

| Deliverable | Status |
|---|---|
| compression.html v5.1 committed to bible/compression.html | COMPLETE — SHA d5427723 — 170KB |
| mpw_bible_writer.py v5.1 built from scratch | COMPLETE — 2,387 lines — syntax OK — 80/81 checks |
| commit_compression_v51.py — auto-finds file, verifies before commit | COMPLETE — in mpw-scripts\ |
| Fastmail email set up at team@musicproductionwiki.com | COMPLETE — MX/SPF/DKIM verified via Netlify DNS |
| Kit account created for email gate API (free tier) | COMPLETE — API key in Bible gate API.txt |
| Beehiiv welcome email written and configured | COMPLETE — "You're in. Here's what happens next." |
| Beehiiv address/reply-to updated to team@musicproductionwiki.com | COMPLETE |

### compression.html v5.1 — Session 33 Features Added

**Nav:**
- MPW slim bar: search + hamburger always right-aligned on mobile (margin-right:auto on logo)
- Bible bar: ALWAYS visible on all screen sizes — never hidden — identity-only on mobile (bb-cats/bb-all/bb-divider hidden)
- Entry nav: 20 pills (added Verdict pill — was 19)
- Mobile stack: 40px slim bar + 44px bible bar = 84px — entry-nav top:84px

**Content fixes:**
- Producer's Verdict: amber header bar + 2-column grid of 6 rules + italic lead + closing statement + share bar
- Verdict section has id="verdict" and is in entry nav
- Mistake cards: warm #1f0800 bg + orange #ff6600 left border + readable #e0c090 text
- Newsletter card: full amber background + dark text + white input + dark button

**Share system (unified):**
- 4 shareable sections: Quick Ref, Genre Table, GR Calculator, Producer's Verdict
- All use .mpw-share-bar class with .mpw-share-btn flex:1 = equal width buttons
- Every share bar: Copy Link + Share on X + Reddit
- Verdict share copies all 6 rules as clean text to clipboard
- Tools section has its own Share this tool bar (X + Reddit + Copy Link)

**CSS architecture:**
- Reduced from 7 appended style blocks (conflicting) to 2 style blocks (main + consolidated override)
- Desktop sidebar restored: @media(min-width:769px) grid:1fr 280px with display:block on entry-sidebar
- All mobile overrides in single consolidated block

**Email gate:**
- openGateFor() bypassed — downloads fire directly
- TODO P3.5: wire Kit free API (key in Bible gate API.txt)
- Modal HTML kept in page but never shown

**Infrastructure (Session 33):**
- Fastmail: team@musicproductionwiki.com — MX records at Netlify DNS — DKIM/SPF verified
- Kit: free plan — up to 10K subscribers with API — key saved
- Beehiiv: free Launch plan — up to 2,500 subscribers — welcome email configured

### Outstanding Issues on compression.html (Session 34 P0)

1. **Share buttons mobile** — flex:1 applied but visual uniformity needs confirmation after latest commit
2. **DAW tab blank yellow** — first tab (Ableton) rendering as amber box — text may be white-on-amber — CSS fix needed
3. **Writer --test not yet run** — P0.3 not complete — do not run Tier 1 batch until --test passes visual QA

---

## May 16, 2026 — SESSION 32 FINAL — GOLD STANDARD BUILD + STRATEGIC PLANNING

### What Was Built
| Deliverable | Status |
|---|---|
| compression.html v5.1 gold standard | COMPLETE — 153KB — 38/38 checks — at /mnt/user-data/outputs/compression.html |
| All 6 handoff modules updated | Session 32 Final versions — this commit |

### Gold Standard compression.html — Full Feature List

**Nav Stack (v5.1 locked):**
- MPW slim bar (40px, z:700, #181818) — logo + Articles/Gear/About + "A MusicProductionWiki Publication" + search + Sound Better CTA
- Bible bar (50px, z:600, #0d0800) — diamond + title + 8 category pills (active highlighted amber) + All entries
- Entry nav (top:90px, z:400) — 19 pill links, no label, active tracking JS
- Mobile: SVG hidden → vertical .scm-box stack. bible-mobile-bar shown. Entry nav top:126px.
- 6 breakpoints: 380px, 400px, 480px, 600px, 768px, 1024px

**Content (19 sections):**
definition, how-it-works, parameters, quick-reference, signal-chain, diagram, history, how-to-use, genre-table, hardware-plugin, before-after, in-the-wild, types, mistakes, flags, progression, faq, tools, related

**Content Features:**
- Difficulty badge (Intermediate)
- Prereq chain (3 linked terms)
- Start Here learning path box
- Quick Answer block
- PDF export button (email gated)
- Unified smart gate modal (3 assets: full PDF, quickref, genre table)
- Common misconception block
- The Number box (amber stat card)
- Section summaries (amber left-border callouts)
- Signal chain SVG 1440×160px — full labels + sub-descriptions + "YOU ARE HERE"
- Mobile vertical signal chain (.scm-box stack)
- Interaction warnings (3)
- DAW tabs (Ableton/Logic/FL/Pro Tools) — localStorage preference next session
- Genre settings table (5 genres × 5 parameters) — with share + email-gated download
- Hardware vs plugin comparison table
- Plugin recs (Free/Mid/Pro tiers) in outer card
- Before/After block (outer card)
- 7 track examples (text-only, no links)
- 4 history sub-sections in left-bordered cards
- 2 producer quotes (Rick Rubin + Bob Clearmountain — from quotes.json, compression tag)
- Types grid (6 cards)
- Comparison callouts (Compression vs Limiting, Compression vs Saturation) — mobile 1-col
- Producers Verdict
- Common Mistakes (6)
- Red/Green Flags (cards)
- Progression Path (3 stages)
- FAQ accordion (8 questions)
- Also in The Bible (8 related term cards with previews)
- Tools section with GR Calculator

**Interactive Tools:**
- Gain Reduction Calculator (live JS — 4 inputs → GR, output level, excess above threshold, final after makeup)
- Save Settings as PDF button (email gated → downloadQuickRef)
- Copy Settings button (clipboard → tab-separated text)
- Quick Reference share on X + Download Card (email gated)
- By Genre share on X + Download Cheat Sheet (email gated)
- Smart gate modal (openGateFor — 3 asset types, email validation, loading state)

**SEO / Schema (5 blocks):**
- Article + sameAs (Wikidata + DBpedia)
- FAQPage (8 questions)
- BreadcrumbList
- Speakable (cssSelector: .qa-text, .entry-term, .entry-hook)
- HowTo (5 steps for parameter setting)
- lastReviewed in Article schema
- Internal links: /bible/bus-compression, /bible/gain-staging, /bible/limiting, /bible/saturation, /bible/parallel-compression

**Sidebar:**
- Full TOC (19 links) with IntersectionObserver tracking
- Producer spotlight (3 cards — Rubin, Clearmountain, Scheps)
- Share buttons
- Newsletter signup
- (No duplicate related terms — consolidated into in-page "Also in The Bible" section)

**Removed from v5.0:**
- Audio toggle placeholder ("Coming Soon") — deleted entirely
- Further Reading section — redundant with "Also in The Bible"
- Duplicate sidebar related terms
- YouTube track links — text-only citations only
- Identity bar

**Stats:**
- Words: 7,058 content words
- Read time: 22 min
- File: 153KB (under 200KB Cloudflare limit)
- Nav links: 19
- H2s: 21 / H3s: 10
- FAQs: 8 / Track items: 7 / Producer quotes: 2
- Schema blocks: 5
- Mobile checks: 38/38


### Key Strategic Decisions Made Session 32

**Three-Tier Bible Template System — LOCKED:**
| Tier | Name | Word Range | Pass 2 Prose Target | Use For |
|---|---|---|---|---|
| 1 | Flagship | 6,800–7,800w | 5,800–6,500w | Top 200-300 cornerstone terms |
| 2 | Standard | 3,800–5,000w | 3,000–3,800w | Mid-range terms |
| 3 | Reference | 1,500–2,500w | 1,200–1,800w | Narrow/technical terms |

Batch file format extended: `slug:Term:Category:Tier` (was 3 parts, now 4)
Tier determines which build_html function is called: build_html_t1(), build_html_t2(), build_html_t3()
Tier 3 non-negotiables: full nav stack, all SEO schema, canonical, OG/Twitter, newsletter, Also in The Bible, Bible colophon

**Tools as Moat — Architecture Decided:**

Three moats built/planned:

Moat 1 — Glossary Tooltip System (SESSION 33):
- data-tooltip="slug" attribute on technical terms in prose
- JS lookup against bible-index.json (already exists)
- CSS tooltip card appears on hover/tap
- Writer updated to wrap CONFIRMED_LIVE_SLUGS terms in spans
- 1,500 entries × avg 15 tooltips = 22,500 automatic internal links
- No other music production site has this

Moat 2 — "Was This Helpful?" Feedback (SESSION 33):
- Three buttons: Beginner / Intermediate / Advanced (level match vote)
- One text field: "What's missing?" (open)
- GA4 event on submission
- Google Form/Sheets backend (no database needed initially)
- Data calibrates tier classification and shapes future content decisions

Moat 3 — DAW Preference localStorage (SESSION 33):
- On first Bible visit: prompt "Which DAW?" — 4 buttons
- Stores to localStorage key mpw_daw_pref
- Every subsequent Bible entry auto-opens to preferred DAW tab
- 10 lines of JS — highest effort:impact ratio of any planned feature

**Tools Category Architecture — Decided:**

Two entry points:
1. `/tools/` — standalone hub page (grid of all tools, submittable to Product Hunt)
2. `/bible/categories/tools/` — 9th Bible category pill (filters entries with interactive tools)
3. Individual tool pages at `/tools/[slug]/` when a tool graduates beyond its Bible entry

Tool priority order:
1. GR Calculator — already live on compression entry ✅
2. Delay Time Calculator — highest search volume ("delay time calculator bpm") — next
3. Frequency Reference Tool — most linkable/shareable — on EQ entry
4. LUFS Target Calculator — mastering/loudness entries
5. Attack/Release Time Calculator — extends compression entry
6. BPM Tap Tempo — trivially simple, very high volume
7. ClearCheck Layer 1 — flagship, unique to MPW via TruClarify

Gate strategy: NEVER gate the tool itself. Gate the download/save output only. Free tool use is the moat. Email capture on "Save as PDF" / "Download Cheat Sheet" — not on calculator use.

**Section-Level Sharing System — Built:**
- Genre table: Share on X + Copy Link + Download Cheat Sheet (email gated)
- Quick Reference: Share on X + Copy Settings (clipboard) + Download Card (email gated)
- Calculator: Save Settings as PDF (email gated)
- Smart unified gate modal handles all 3 asset types

**Moat 4 (future) — "Where to Go Next" Smart Nav:**
- 3 opinionated next-steps per entry: Beginner path / Deeper dive / Solve a problem
- Pass 1 returns next_steps field: {beginner_slug, deeper_slug, problem_slug}
- Higher pages-per-session, turns Bible into a course not just a reference

**Moat 5 (future) — Verified Settings Badges:**
- Cross-reference genre settings with quotes.json documented settings
- "↗ Verified from [Source]" badge on settings backed by engineer interviews
- Citable claims that get linked to from forums and other sites

---

## May 16, 2026 — SESSION 31 FINAL — STRATEGIC PLANNING + HANDOFF

### What Was Decided
Nav architecture locked: MPW slim bar + Bible bar + entry nav. Identity bar removed. Progress bar desktop removed, mobile kept. Quotes system confirmed (quotes.json, Pass 1.5). 13 new v5.1 features confirmed. Three-tier word count system initiated.

### What Was Built
quotes.json v2 (318 quotes, 177 people). All 6 handoff modules Session 31 Final. Nav stack mockup approved. v5.1 spec written.

---

# 32. SESSION 32 — v5.1 GOLD STANDARD — COMPLETE SPEC

This section documents the gold standard compression.html built in Session 32 and refined in Session 33. Do not modify the committed file directly — modify the writer to match it.

## The Gold Standard File

Location: `bible/compression.html`
Built: May 16, 2026 — Session 32
Refined: May 17, 2026 — Session 33 (multiple commits)
Current SHA: d5427723fb9758420a8bbc03cf6d072f59f35f22
Size: 170KB (was 153KB — grew with share bars, verdict, CSS consolidation)
Style blocks: 2 (main + consolidated override)

## Nav Stack — FINAL v5.1 (Session 33 confirmed)

```
Desktop sticky chain:
  .mpw-slim-bar    position:sticky  top:0     z-index:700  height:40px  background:#181818
  .bible-bar       position:sticky  top:40px  z-index:600  height:50px  background:#0d0800
  .entry-nav       position:sticky  top:90px  z-index:400
  Dropdowns        z-index:99999
  #reading-progress display:none (desktop)

Mobile (≤1024px):
  .msb-logo margin-right:auto — pushes search+hamburger to right
  .bible-bar STAYS VISIBLE — identity only — bb-cats/bb-all/bb-divider hidden
  .bible-mobile-bar display:none (removed — bible-bar handles identity)

Mobile (≤768px):
  .entry-nav top:84px (40px slim + 44px bible)
  [id].entry-section scroll-margin-top:110px
  .entry-sidebar display:none
  .bible-entry-wrap display:block
  Signal chain SVG hidden → .signal-chain-mobile flex (vertical stack)
  #reading-progress display:block
```

## Entry Nav — 20 Links (Session 33 — Verdict added)

definition, how-it-works, parameters, quick-reference, signal-chain, history, how-to-use, genre-table, hardware-plugin, before-after, in-the-wild, types, **verdict**, plugin-recs, mistakes, flags, progression, faq, tools, related

## Unified Share Bar System (Session 33)

CSS class: `.mpw-share-bar` / `.mpw-share-btn`
All buttons use `flex:1` for equal width — no exceptions.
Button variants: `.share-copy` (amber) / `.share-x` (black) / `.share-reddit` (red #ff4500)
4 shareable sections: quick-reference, genre-table, gr-calculator, verdict
Label goes full-width on its own row (width:100%)

## Email Gate — Bypassed (Session 33)

openGateFor() fires downloads directly. No modal shown.
TODO P3.5: wire Kit free API — key saved in Bible gate API.txt in mpw-scripts\
Beehiiv API requires paid plan ($49+/month) — not used.

## Infrastructure Added Session 33

- Email: team@musicproductionwiki.com via Fastmail — DNS verified at Netlify
- Email list: Kit free plan (up to 10K subscribers, API included)
- Newsletter: Beehiiv free plan (up to 2,500 subscribers, unlimited sends)
- Welcome email live on Beehiiv: "You're in. Here's what happens next."

---

# 33. SESSION 33 — PRIORITIES + SPECS

## P0: compression.html Gold Standard — COMPLETE

Committed Session 33. Multiple fix commits during session refining:
- Share bars unified (4 sections, 3 buttons each, flex:1 equal width)
- Bible bar always visible as product identity
- Producer's Verdict redesigned (amber header + 2-col grid + share bar)
- CSS consolidated from 7 style blocks to 2

## P0.2: Remaining Visual QA Items (Session 34 P0)

1. Share buttons — confirm equal width on mobile after latest commit
2. DAW tab blank yellow — fix active state CSS (daw-tab-btn.active background must be dark, not amber)
3. Run --test on writer and compare to live gold standard

## P1: Moat 1 — Glossary Tooltip System

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

## P1.1: Moat 2 — "Was This Helpful?" Feedback

Goal: Structured feedback on level match + content gaps.

HTML block: insert before "Also in The Bible" section.
```html
<div class="helpful-block" id="helpful">
  <div class="helpful-q">What level did this entry match?</div>
  <div class="helpful-btns">
    <button onclick="helpfulVote('beginner',this)">Beginner</button>
    <button onclick="helpfulVote('intermediate',this)">Intermediate</button>
    <button onclick="helpfulVote('advanced',this)">Advanced</button>
  </div>
  <div id="helpful-missing" style="display:none">
    <label>What's missing? <span>(optional)</span></label>
    <input type="text" id="helpful-input" placeholder="e.g. more on sidechain, clearer ratio explanation...">
    <button onclick="helpfulSubmit()">Send</button>
  </div>
  <div id="helpful-thanks" style="display:none">Thanks — your feedback shapes future entries. ✓</div>
</div>
```

JS: helpfulVote(level, btn) → highlight selected button, show missing field, fire GA4 event('helpful_vote', {level, slug}). helpfulSubmit() → POST to Google Form endpoint with level + missing text + slug + URL, show thanks div, fire GA4 event('helpful_submit').

CSS: amber button on selection, green thanks message, subtle card with border.
Google Form: 3 fields — level (hidden), missing (text), slug (hidden). Responses to Google Sheets.

## P1.2: Moat 3 — DAW Preference localStorage

Goal: One-time DAW preference stored locally. Every Bible entry auto-opens to preferred DAW tab.

JS (10 lines, inject into all Bible entries):
```javascript
(function(){
  var DAW_KEY = 'mpw_daw_pref';
  var pref = localStorage.getItem(DAW_KEY);
  if (pref && typeof dawTab === 'function') {
    var btn = document.querySelector('.daw-tab-btn[data-daw="'+pref+'"]');
    if (btn) dawTab(btn, pref);
  }
  document.querySelectorAll('.daw-tab-btn').forEach(function(b){
    b.addEventListener('click', function(){
      localStorage.setItem(DAW_KEY, b.dataset.daw);
    });
  });
})();
```

Also: add data-daw attribute to each .daw-tab-btn.

---

# INFRASTRUCTURE REFERENCE

- Repo: github.com/musicproductionwiki/musicproductionwiki
- GitHub Token: YOUR_GITHUB_TOKEN_HERE (expires Aug 2, 2026)
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
- Gold standard Bible v5.1: bible/compression.html — LIVE Session 33 — SHA d5427723
- OG default image: /images/og-default.jpg
- Bible URL structure: /bible/{slug} — never /dictionary/
- Quotes database: mpw-scripts\quotes.json — 318 quotes, 177 people — v2
- Tools hub (planned): /tools/ — not yet built

## GSC Data (May 15, 2026 — 3 month view)
- 301 total impressions / 0 clicks / 0% CTR / 16.4 average position
- Top queries: serum 2 vs vital (10), logic pro vs ableton (9), ableton live vs logic pro (6), rode nt1 vs shure sm7b (5)
- Comparisons are the traffic beachhead — position 16 to 5 = clicks start
- Action: title tag + meta description optimization on top comparison articles

## Confirmed Live Bible Slugs (CONFIRMED_LIVE_SLUGS constant in script)
compression, eq, limiting, saturation, distortion, reverb, delay, parallel-compression, multiband-compression, noise-gate, gain-staging, headroom, stereo-imaging, mid-side-processing, bus-compression, mix-bus, send-return, automation, mastering, lufs, dynamic-range, true-peak-limiting, loudness-normalization, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, resonance, harmonic-distortion, chorus, flanger, phaser, tremolo, vibrato, plate-reverb, room-reverb, convolution-reverb, clip-gain, air-frequency-eq, air

EXCLUDED (confirmed 404): sidechain-compression, transient-shaping

## Pending Owner Actions
1. Affiliate applications: Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — REVENUE BLOCKER
2. Complete compression.html visual QA on mobile (share buttons, DAW tab) — Session 34 P0
3. Run Tier 1 batch after writer --test confirmed

## Batch Files Ready to Run (after v5.1 writer --test confirmed)
- bible-upgrade-tier1.txt — 50 Tier 1 Bible rewrites — in mpw-scripts\ — format now slug:Term:Category:1
- batch09.txt — 100 track breakdowns — run after Tier 1
