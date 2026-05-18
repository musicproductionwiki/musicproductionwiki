# MusicProductionWiki.com — CORE Handoff
*Updated: May 18, 2026 (SESSION 36) · 526 articles + 210 Bible entries live*
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
| NEVER build Bible writer without running verification suite first | v5.1 = 81-check suite — all must pass before delivery |
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
| ALWAYS audit mpw_bible_writer.py output with python audit script before delivering | Run full 81-check suite — all must pass |
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
| Every shareable section must have Copy Link + Share on X + Reddit | Order: Copy Link → Share on X → Reddit — uniform .mpw-share-btn styling — equal height 34px |
| NEVER make share buttons different sizes | All .mpw-share-btn must have same height (34px), same border-radius (6px), same font-size |
| Producer's Verdict must be in the entry nav | 20th pill — id="verdict" on .producers-verdict wrapper |
| Email API gate is bypassed — Kit/Brevo to be wired at P3.5 | openGateFor() fires downloads directly — no modal shown |
| NEVER wire Beehiiv API — use Kit free API at P3.5 | Kit account created, API key in Bible gate API.txt in mpw-scripts\ |
| NEVER patch a Bible page without first fetching the live file from GitHub via PowerShell script | Claude cannot access GitHub or the live site — all patches must be Python scripts run by Steve |
| NEVER guess the target string in a patch script | Always fetch the live file in the same script and print the relevant section before replacing |
| NEVER run fix_combined.py or similar without pasting the full audit output before committing | Audit output must be verified in chat before commit proceeds |
| NEVER use display:block!important on the aside element | This prevents mobile CSS from hiding it — use CSS media queries only |
| The sidebar was hidden because gain-calculator div was unclosed | That div swallowed the aside as a nested child — balance check: entry-main should have exactly 1 unclosed div |
| NEVER commit Bible HTML without running balance check on entry-main | Opens=Closes+1 — any other value means broken DOM |
| Footer share buttons are X and Reddit only — no Copy Link | Centered, equal size, branded colors — not full-width stretched |
| .mpw-share-btn has flex:1 1 0 — footer buttons must use .footer-share-btn class to override | .footer-share-btn { flex:0 0 auto !important; width:auto !important; padding:0 18px !important; } |
| Share bar order is ALWAYS: Copy Link → Share on X → Reddit | No exceptions — this order confirmed Session 34 |
| NEVER use Set-Content in PowerShell for Python scripts with CSS values | Use create_file tool to output .py files — PowerShell mangles colons and semicolons |
| NEVER run mpw_bible_writer.py --test and call it passing if any content quality issue exists | 81/81 checks + visual QA both required — checks are structural only, not content quality |
| mpw_bible_writer.py Pass 2 prompt is critically deficient — do not run Tier 1 batch | Missing: h2 titles, FAQ, plugin recs, 2nd quote, working anchors, authoritative prose — rewrite first |
| NEVER declare writer ready for batch based on validation score alone | Visual QA against gold standard mandatory — must confirm all content elements present |
| NEVER use tool_type from Pass 1 to determine GR calculator rendering | Hardcode Compression to always get GR calculator — tool_type is unreliable |
| NEVER use MODEL = "claude-sonnet-4-20250514" | Model string is claude-sonnet-4-6 — always |
| NEVER set API timeout below 600 seconds for Pass 2 | 22,000 token Pass 2 requires up to 10 minutes — 300s is insufficient |
| NEVER truncate a handoff module to save context | If context is low, warn Steve and stop — do NOT deliver a partial handoff |

---

# ⛔ RULE 3B — 75% CONTEXT WARNING — MANDATORY

**⛔ ANTI-TRUNCATION RULE #4: AT 75% CONTEXT, STOP ALL WORK AND WARN STEVE. DO NOT ATTEMPT TO COMPRESS OR ABBREVIATE ANY HANDOFF MODULE TO FIT REMAINING CONTEXT. A PARTIAL HANDOFF IS WORSE THAN NO HANDOFF.**

At 75% context, Claude must stop all work immediately and tell Steve:

"I am at approximately 75% context. I will complete the current task only, then update the handoff and stop. A new session is required after this."

This is not optional.

---

# ⛔ RULE 4 — CALL OUT SKIPPED STEPS IMMEDIATELY

If Claude skips a step in the session start checklist, delivers output without required deliverables, or takes action before completing the hard gate — Steve must call it out immediately.

---

# ⛔ RULE 5 — DELIVERABLES CHECKLIST

**⛔ ANTI-TRUNCATION RULE #5: THE HANDOFF COMMIT IS NOT COMPLETE UNLESS ALL 6 FILES ARE FULL LENGTH. COMPARE LINE COUNTS AGAINST PREVIOUS VERSION BEFORE COMMITTING. ANY FILE SHORTER THAN ITS PREDECESSOR WITHOUT EXPLICIT REASON IS TRUNCATED — STOP AND FIX.**

Every handoff update requires ALL of the following:
- [ ] All 6 MPW-HANDOFF-*.md modules updated in GitHub via Trees API
- [ ] MPW-CATALOG.md auto-regenerated and included in same commit
- [ ] Session log updated in MPW-HANDOFF-CORE.md (Section 21 — keep 3 most recent)
- [ ] Section 2 Priority table updated
- [ ] Section 16 Next Session Start Prompt updated
- [ ] mpw_session_start.py updated if session start logic changed

---

# 2. PRIORITY TABLE (Updated Session 36)

| Priority | Task | Status | Detail |
|---|---|---|---|
| P0 | mpw_bible_writer.py Pass 2 prompt rewrite | CRITICAL — SESSION 37 | Pass 2 output is structurally valid but content quality is ~55% of gold standard. Missing: h2 section titles, FAQ, plugin recs, 2nd producer quote, working anchor nav, authoritative prose. Full Pass 2 prompt rewrite required before any Tier 1 batch. |
| P0.1 | Tool injection fix — GR calculator always on compression | SESSION 37 | Pass 1 returned tool_type: null for compression — GR calculator did not render. Hardcode compression to always get GR calculator regardless of Pass 1 output. |
| P0.2 | Producer Spotlight sidebar fix | SESSION 37 | Currently pulling producer names from track examples. Should pull from producer_quote_source or dedicated producer spotlight data. |
| P0.3 | Validate writer output visually against gold standard | SESSION 37 | After Pass 2 prompt rewrite, run --test compression, compare output side-by-side against live compression.html |
| P0.4 | Run mpw_bible_cat_pages.py --run | After P0.3 confirmed | 8 Bible category pages committed |
| P1 | Build Moat 1 — Glossary Tooltip System | After P0 confirmed | data-tooltip system, JS lookup against bible-index.json, CSS tooltip card |
| P1.1 | Build Moat 2 — "Was This Helpful?" feedback | After Moat 1 | Level vote + text field + GA4 + Google Form/Sheets backend |
| P1.2 | Build Moat 3 — DAW preference localStorage | After Moat 2 | 10 lines JS — localStorage key mpw_daw_pref |
| P2 | Tier 1 batch — 50 Bible rewrites | After P0.3 + P0.4 confirmed | python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-16 |
| P2.1 | Air entry retry | After Tier 1 | python mpw_bible_writer.py --test --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency" |
| P2.2 | Sitemap regeneration + GSC resubmission | After Tier 1 | Regenerate after Tier 1 batch |
| P2.3 | netlify.toml redirect /dictionary/* to /bible/:splat | Pending | 301 redirect for old URLs |
| P2.4 | Fix dead category card slugs | Pending | 448 references, 7 slugs — fix_dead_slugs.py needs href format investigation |
| P3 | Build /tools/ hub page | After Moats 1-3 | Standalone destination — grid of all tools — submittable to Product Hunt |
| P3.1 | Build Delay Time Calculator | On Delay Bible entry | Highest search volume tool |
| P3.2 | Build Frequency Reference Tool | On EQ Bible entry | Click a band → instruments that live there + EQ context |
| P3.3 | Build LUFS Target Calculator | On Mastering/LUFS entries | Current LUFS + platform target → headroom needed |
| P3.5 | Wire Kit API to email gate | After affiliate revenue starts | Replace openGateFor() bypass with Kit free API — key in Bible gate API.txt |
| P4 | Batch 09 — 100 track breakdowns | After Tier 1 | python mpw_writer.py --batch batch09.txt --start-date 2026-03-01 |
| P4.1 | Run mpw_dead_slug_audit.py | After Tier 1 commits | Find all dead related-article links |
| P5 | Fix 5 articles missing og:image | mpw_fix_meta.py | Rate limited Session 27 — retry |
| P6 | Affiliate applications | REVENUE BLOCKER | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — Steve must do |
| P7 | Google Workspace email | RESOLVED Session 33 | Fastmail set up at team@musicproductionwiki.com — DNS configured — MX/SPF/DKIM verified |
| P8 | recreations.html category page | Before Batch 11 | Must exist before Batch 11 runs |
| P9 | vocal-autopsies.html category page | Before Batch 12 | Must exist before Batch 12 runs |
| P10 | Producer Profile pages /producers/ | After Batch 09 | Full content pillar — Option B |
| P11 | Bible subcategory pages | After 500 entries | /bible/categories/dynamics/compression/ etc |
| P12 | Mobile app PWA first then React Native | After 1000 entries + 25K monthly visitors | Milestone trigger |
| P13 | GSC — 2 URL fixes committed | DONE Session 36 | ssl-2-plus-review/ redirect + monitors canonical fixed — commit d6f787db |

---

# 16. NEXT SESSION START PROMPT (Session 37)

**⛔ ANTI-TRUNCATION RULE #6: THE NEXT SESSION START PROMPT MUST BE REPRODUCED IN FULL. DO NOT SUMMARIZE.**

"Run python mpw_session_start.py. State article count, Bible entry count, P0 priority, and last 5 NEVER rules added.

P0 SESSION 37 is a complete rewrite of the mpw_bible_writer.py Pass 2 prompt. The current writer produces structurally valid HTML that passes 81/81 checks but fails visual QA at approximately 55% quality vs the gold standard compression.html. Specific failures:

1. Section h2 titles (Definition, How It Works, Parameters etc.) are missing from generated content
2. Only 1 producer quote — should be 2 minimum (built into Pass 2 prompt requirement)
3. FAQ section absent entirely — FAQ_PLACEHOLDER not placed correctly by Pass 2
4. Plugin recommendations absent — PLUGIN_PLACEHOLDER not placed correctly
5. Entry nav anchor links broken — clicking nav pills jumps to wrong content
6. Comparison callouts are one-liner stubs — no real content
7. Tools section shows 'Interactive Tool Coming Soon' for Compression — GR calculator not rendering because Pass 1 returned tool_type: null
8. Producer Spotlight sidebar is wrong — pulling from track produced_by field instead of real producer profiles
9. Content is generic and does not read as authoritative producer reference

The rewrite must fix ALL of these before the Tier 1 batch runs. After rewrite:
1. Run --test compression again
2. Visual QA the output against live gold standard
3. Confirm 81/81 checks still pass
4. Only then proceed to P0.4 (cat pages) and P2 (Tier 1 batch)

CRITICAL SESSION 37 RULES:
- Read the full current mpw_bible_writer.py before touching anything
- The Pass 2 prompt in build_pass2_prompt_t1() is the primary problem — fix it first
- The build_html_t1() placeholder replacement logic also needs auditing
- NEVER declare the writer ready based on validation score alone — visual QA is mandatory
- NEVER run the Tier 1 batch until the test output matches the gold standard at 90%+ quality
- NEVER truncate handoff modules — if context runs low, warn and stop"

---

# 21. SESSION LOG (3 Most Recent)

**⛔ ANTI-TRUNCATION RULE #7: THE SESSION LOG MUST INCLUDE THE FULL TEXT OF ALL 3 RECENT SESSIONS. DO NOT ABBREVIATE ANY SESSION ENTRY.**

## May 18, 2026 — SESSION 36 — WRITER UPDATE + SHARE BARS + GSC

### What Was Done

1. **Share bars — compression.html** — All share bars fixed:
   - Calculator share bar: outer display:flex wrapper removed, .mpw-share-bar promoted directly
   - Tools share bar: inline-styled links replaced with .mpw-share-bar (Copy Link → X → Reddit)
   - calc-share-bar CSS injected: auto-width buttons, solid amber Copy Link, 3-col equal grid on mobile
   - Footer kept as-is (Steve's decision)
   - Commits: fix_share_bars_s36.py through fix_share_bars_s36e.py — final commit bd601b91 + S36e

2. **mpw_bible_writer.py — major structural update** — Updated to match gold standard compression.html v5.1:
   - MODEL changed from claude-sonnet-4-20250514 to claude-sonnet-4-6
   - API timeout increased from 300s to 600s
   - css_block NameError fixed — added css_block = build_css() local var in build_head()
   - Consolidated overrides CSS block added (second style block matching gold standard)
   - bible-entry-wrap inline grid override added to build_html_t1()
   - aside inline style added to build_html_t1()
   - Genre share bar updated from old section-share-bar to mpw-share-bar
   - Quick Ref QUICKREF_SHARE_PLACEHOLDER updated to mpw-share-bar
   - build_footer() updated to amber bible-nl-card + correct footer structure
   - Verdict prompt updated: id="verdict" standalone div after types section
   - Sidebar share widget added (mpw-share-bar vertical column)
   - calc-share-bar CSS added to consolidated overrides block
   - 5 stale validation checks updated to match v5.1 gold standard
   - Final: 81/81 checks pass

3. **Writer visual QA — FAILED at ~55%** — Structural checks pass but content quality is far below gold standard:
   - Section h2 titles missing
   - Only 1 producer quote (need 2)
   - FAQ section absent
   - Plugin recs absent
   - Entry nav anchor links broken
   - Comparison callouts are stubs
   - GR calculator not rendering (tool_type returned null from Pass 1)
   - Producer Spotlight wrong data
   - Content generic — not authoritative producer-language
   - P0 for Session 37: complete Pass 2 prompt rewrite

4. **GSC issues fixed** — fix_gsc_issues.py written and run:
   - netlify.toml: redirect /ssl-2-plus-review/ → /articles/ssl-2-plus-review.html (301, both with and without trailing slash)
   - articles/best-studio-monitors-under-300.html: canonical tag corrected
   - Trees API commit — SHA: d6f787db46f8dc4bbbe5b7d4f1fd2ba0b45e0505

### Session 36 Key Findings

**Writer pass 2 root problem:** The Pass 2 prompt instructs Claude to output HTML sections but does not enforce h2 tags, does not enforce FAQ_PLACEHOLDER position, does not enforce PLUGIN_PLACEHOLDER position, does not mandate 2 producer quotes. A complete prompt rewrite is needed that mandates h2 tags for every section, mandates FAQ_PLACEHOLDER at exact position, mandates PLUGIN_PLACEHOLDER after hardware-plugin table, mandates exactly 2 producer quotes, enforces authoritative producer-language.

**tool_type reliability:** Pass 1 returned tool_type: null for Compression. Fix: hardcode Compression (and any other entries with known tools) in build_tools_section() via TOOL_OVERRIDES map regardless of Pass 1 output.

**anchor nav broken:** The entry nav pills link to section IDs but generated sections may not have the exact IDs or class="entry-section". Audit: check every section in Pass 2 output has both class="entry-section" and the exact id listed in ENTRY_NAV_LINKS.

**ANTI-TRUNCATION FAILURE THIS SESSION:** When writing handoff files, CORE.md was truncated from 848 lines to 527 lines — losing sections 32, 33, infrastructure reference, gold standard feature list, and moat specs. This would have permanently destroyed that context if committed. Never truncate. Always check output line count against source line count before committing.

### Session 36 Commit Log (key SHAs)

| SHA | What |
|---|---|
| fix_share_bars_s36.py run | Calculator outer wrapper removed |
| fix_share_bars_s36b.py run | calc-share-bar class added to both bars |
| fix_share_bars_s36c.py run | CSS inject: calc-share-bar auto-width |
| fix_share_bars_s36d.py run | CSS: solid amber Copy Link |
| fix_share_bars_s36e.py run | CSS: 3-col equal grid on mobile |
| d6f787db | GSC fixes: ssl redirect + monitors canonical |
| mpw_bible_writer.py | Multiple iterations — final 81/81 checks |

---

## May 17, 2026 — SESSION 35 — SHARE BARS + SITE MAINTENANCE

### What Was Done

1. **Sitemap regenerated** — gen_sitemap.py written and run. 526 articles + 210 Bible entries = 739 URLs. Committed to GitHub.
2. **Dead slug audit** — mpw_dead_slug_audit.py run. 448 dead references across 7 slugs in category cards. fix_dead_slugs.py written — did not patch (href format mismatch — needs re-investigation).
3. **compression.html QA** — Multiple patch attempts. Net result: aside debug border removed, bible-entry-wrap inline grid restored, share bars partially fixed.
4. **compression.html reverted** to stable state. Current SHA has: aside correct, grid inline style present, bottom share bar converted to mpw-share-bar, sidebar share converted to mpw-share-bar.

### Key Learnings Session 35

- NEVER paste Python inline in PowerShell — CSS values get mangled
- NEVER revert without first checking what that commit's state actually was
- NEVER add display:block!important to aside — breaks mobile hide via CSS media query
- ALWAYS fetch live file and print exact target strings before writing any patch script
- ALWAYS use create_file tool for Python scripts — never Set-Content or here-strings

### Session 35 Commit Log (key SHAs)

| SHA | What |
|---|---|
| 774794ce | Revert to a475be6 (pre-FAQ-fix) |
| 72502529 | Restore bible-entry-wrap inline grid override |
| f508bb5d | Fix sidebar grid + FAQ button color |
| 0be16550 | Restore sidebar inline style + fix FAQ buttons |
| 82e821cd | Fix FAQ buttons — reset global button style override |
| 3856107a | Fix footer share buttons — fully inline equal width |
| a475be68 | Fix footer share buttons — equal size X + Reddit |
| da97338e | ROOT FIX Session 34 — gain-calculator div closed |

---

## May 17, 2026 — SESSION 34 — COMPRESSION.HTML VISUAL QA + SHARE BARS

### What Was Done

This session was entirely dedicated to visual QA on compression.html — fixing the sidebar, share buttons, and footer. It took approximately 40 commits due to cascading HTML structure bugs and iterative CSS patching.

### Root Cause of Sidebar Failure — CRITICAL

The sidebar was swallowed inside .entry-main by the browser. Root cause: the gain-calculator div was NEVER CLOSED. This caused everything after the calculator — including the aside — to be nested inside entry-main. The grid had only 1 direct child so the second column never rendered.

Fix: Added `</div><!-- /gain-calculator -->` immediately before the Signal Chain section. SHA: da97338e

Lesson: ALWAYS run a div balance check on entry-main before committing any Bible page. Correct balance is opens = closes + 1.

### Sidebar CSS Fix

display:block!important on the aside inline style was preventing mobile @media CSS from hiding it. Fix: removed display:block!important. Left only: `min-width:280px;width:280px;position:sticky;top:148px;align-self:start;overflow-y:auto;height:calc(100vh - 168px)`

### Share Bar System — Final Architecture

All share bars rebuilt: **Copy Link → Share on X → Reddit**, same height (34px), same border-radius (6px), branded colors. See MPW-HANDOFF-TECH.md Section 13 for full CSS.

### Session 34 Commit Log (key SHAs)

| SHA | What |
|---|---|
| 4a1d115b | First sidebar CSS fix attempt |
| e5c6c614 | Aside height constraint removed |
| b92be506 | Debug red border added to aside |
| da97338e | ROOT FIX — gain-calculator div closed — sidebar appeared |
| de721781 | Debug red border removed |
| 82a7f552 | Share bar CSS replaced — all branded colors |
| 268a4949 | Tools share bar + footer share buttons fixed |
| 48bc8bf3 | All share bars rebuilt — Copy Link > X > Reddit order |
| 13a5351e | Unclosed span removed from calculator section |

---

# Strategic Context

**⛔ ANTI-TRUNCATION RULE #8: THE STRATEGIC CONTEXT SECTIONS BELOW ARE NOT OPTIONAL. THEY MUST BE REPRODUCED IN FULL IN EVERY HANDOFF UPDATE. DO NOT DROP MOAT SPECS, INFRASTRUCTURE REFERENCE, OR GOLD STANDARD FEATURE LIST.**

## Compression.html v5.1 Gold Standard — Full Feature List

**Nav Stack (v5.1 locked):**
- MPW slim bar (40px, z:700, #181818) — logo + Articles/Gear/About + "A MusicProductionWiki Publication" + search + Sound Better CTA
- Bible bar (50px, z:600, #0d0800) — diamond + title + 8 category pills (active highlighted amber) + All entries
- Entry nav (top:90px, z:400) — 20 pill links (Verdict added Session 33), no label, active tracking JS
- Mobile: SVG hidden → vertical .scm-box stack. Entry nav top:84px.
- 6 breakpoints: 380px, 400px, 480px, 600px, 768px, 1024px

**Content (20 sections):**
definition, how-it-works, parameters, quick-reference, signal-chain, diagram, history, how-to-use, genre-table, hardware-plugin, before-after, in-the-wild, types, verdict, mistakes, flags, progression, faq, tools, related

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
- DAW tabs (Ableton/Logic/FL/Pro Tools)
- Genre settings table (5 genres × 5 parameters) — with share + email-gated download
- Hardware vs plugin comparison table
- Plugin recs (Free/Mid/Pro tiers) in outer card
- Before/After block
- 7 track examples (text-only, no links)
- 4 history sub-sections in left-bordered cards
- 2 producer quotes (Rick Rubin + Bob Clearmountain — from quotes.json, compression tag)
- Types grid (6 cards)
- Comparison callouts (Compression vs Limiting, Compression vs Saturation)
- Producers Verdict (amber header + 2-col grid of 6 rules)
- Common Mistakes (6)
- Red/Green Flags (cards)
- Progression Path (3 stages)
- FAQ accordion (8 questions)
- Also in The Bible (8 related term cards with previews)
- Tools section with GR Calculator
- Helpful feedback block (Beginner/Intermediate/Advanced vote)

**Interactive Tools:**
- Gain Reduction Calculator (live JS — 4 inputs → GR, output level, excess above threshold, final after makeup)
- Save Settings as PDF button (email gated → downloadQuickRef)
- Quick Reference share on X + Download Card (email gated)
- By Genre share on X + Download Cheat Sheet (email gated)
- Smart gate modal (openGateFor — 3 asset types)

**Share bars (8 total — all unified Session 36):**
1. Quick Reference — mpw-share-bar — Copy Link → X → Reddit
2. GR Calculator — mpw-share-bar calc-share-bar — Copy Link → X → Reddit
3. Genre Table — mpw-share-bar — Copy Link → X → Reddit
4. Verdict — mpw-share-bar — Copy Link → X → Reddit (centered)
5. Tools — mpw-share-bar calc-share-bar — Copy Link → X → Reddit
6. Bottom page — mpw-share-bar — Copy Link → X → Reddit
7. Sidebar — mpw-share-bar vertical — Copy Link → X → Reddit
8. Footer — inline styled — X → Reddit only (Steve's decision — no Copy Link)

**CSS architecture:**
- 2 style blocks (main + consolidated override) + calc-share-bar block appended Session 36
- Desktop sidebar: @media(min-width:769px) grid:1fr 280px with display:block on entry-sidebar
- All mobile overrides in single consolidated block

**SEO / Schema (5 blocks):**
- Article + sameAs (Wikidata + DBpedia)
- FAQPage (8 questions)
- BreadcrumbList
- Speakable (cssSelector: .qa-text, .entry-term, .entry-hook)
- HowTo (5 steps for parameter setting)
- lastReviewed in Article schema

**Sidebar:**
- Full TOC (20 links) with IntersectionObserver tracking
- Producer spotlight (3 cards)
- Share buttons (mpw-share-bar — Copy Link → X → Reddit — vertical)
- Newsletter signup

**Stats:**
- Words: 7,058 content words / 22 min read
- File: ~175KB
- Nav links: 20 (Verdict added Session 33)
- H2s: 21 / H3s: 10
- FAQs: 8 / Track items: 7 / Producer quotes: 2
- Schema blocks: 5
- Mobile checks: 38/38

## Three-Tier Bible Template System — LOCKED

| Tier | Name | Word Range | Pass 2 Prose Target | Use For |
|---|---|---|---|---|
| 1 | Flagship | 6,800–7,800w | 5,800–6,500w | Top 200-300 cornerstone terms |
| 2 | Standard | 3,800–5,000w | 3,000–3,800w | Mid-range terms |
| 3 | Reference | 1,500–2,500w | 1,200–1,800w | Narrow/technical terms |

Batch file format: `slug:Term:Category:Tier` (4 parts, colon-separated)

## Tools as Moat — Architecture

Moat 1 — Glossary Tooltip System (SESSION 37+):
- data-tooltip="slug" attribute on technical terms in prose
- JS lookup against bible-index.json
- CSS tooltip card appears on hover/tap
- Writer updated to wrap CONFIRMED_LIVE_SLUGS terms in spans
- 1,500 entries × avg 15 tooltips = 22,500 automatic internal links

Moat 2 — "Was This Helpful?" Feedback (SESSION 37+):
- Three buttons: Beginner / Intermediate / Advanced (level match vote)
- One text field: "What's missing?" (open)
- GA4 event on submission
- Google Form/Sheets backend (no database needed initially)
- HTML block: insert before "Also in The Bible" section
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
    <input type="text" id="helpful-input" placeholder="e.g. more on sidechain...">
    <button onclick="helpfulSubmit()">Send</button>
  </div>
  <div id="helpful-thanks" style="display:none">Thanks — your feedback shapes future entries. ✓</div>
</div>
```

Moat 3 — DAW Preference localStorage (SESSION 37+):
- Stores to localStorage key mpw_daw_pref
- Every subsequent Bible entry auto-opens to preferred DAW tab
```javascript
(function(){
  var DAW_KEY = 'mpw_daw_pref';
  var pref = localStorage.getItem(DAW_KEY);
  if (pref && typeof dawTab === 'function') {
    var btn = document.querySelector('.daw-tab-btn[data-daw="'+pref+'"]');
    if (btn) dawTab(btn, pref);
  }
  document.querySelectorAll('.daw-tab-btn').forEach(function(b){
    b.addEventListener('click', function(){ localStorage.setItem(DAW_KEY, b.dataset.daw); });
  });
})();
```

Moat 4 (future) — "Where to Go Next" Smart Nav:
- 3 opinionated next-steps per entry: Beginner path / Deeper dive / Solve a problem
- Pass 1 returns next_steps field: {beginner_slug, deeper_slug, problem_slug}

Moat 5 (future) — Verified Settings Badges:
- Cross-reference genre settings with quotes.json documented settings
- "↗ Verified from [Source]" badge on settings backed by engineer interviews

## Section-Level Sharing System — Final (Sessions 34–36)

- Every shareable section: Copy Link → Share on X → Reddit (this order always)
- All buttons: same height (34px), same border-radius (6px), branded colors
- Copy Link: amber (#f5a623 bg, #000 text)
- Share on X: black (#000 bg, #fff text)
- Reddit: orange-red (#ff4500 bg, #fff text)
- Footer exception: X and Reddit only (no Copy Link), centered
- calc-share-bar: auto-width buttons (flex:0 0 auto), not full-stretch. Mobile: 3-col equal grid.

## Tools Category Architecture — Decided

Three entry points:
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

Gate strategy: NEVER gate the tool itself. Gate the download/save output only.

## Infrastructure Reference

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
- Gold standard Bible v5.1: bible/compression.html — LIVE — share bars fixed Session 36
- OG default image: /images/og-default.jpg
- Bible URL structure: /bible/{slug} — never /dictionary/
- Quotes database: mpw-scripts\quotes.json — 318 quotes, 177 people — v2
- Tools hub (planned): /tools/ — not yet built
- style.css: 52,585 chars — NO rules for .bible-entry-wrap or .entry-sidebar (confirmed Session 34)
- style.css has: .article-layout > aside { display:none !important } — does NOT affect Bible pages

## GSC Data (May 18, 2026)

- 587 not indexed / 14 indexed
- 585 "Discovered - currently not indexed" — normal for new large sitemap — resolves over weeks
- 2 specific issues fixed Session 36: ssl-2-plus-review redirect + monitors canonical
- Top queries at position ~16: serum 2 vs vital, logic pro vs ableton, ableton live vs logic pro, rode nt1 vs shure sm7b
- Action: title tag + meta description optimization on top comparison articles (after Bible Tier 1)

## Confirmed Live Bible Slugs (CONFIRMED_LIVE_SLUGS constant in script)

compression, eq, limiting, saturation, distortion, reverb, delay, parallel-compression, multiband-compression, noise-gate, gain-staging, headroom, stereo-imaging, mid-side-processing, bus-compression, mix-bus, send-return, automation, mastering, lufs, dynamic-range, true-peak-limiting, loudness-normalization, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, resonance, harmonic-distortion, chorus, flanger, phaser, tremolo, vibrato, plate-reverb, room-reverb, convolution-reverb, clip-gain, air-frequency-eq, air

EXCLUDED (confirmed 404): sidechain-compression, transient-shaping

## Batch Files Ready to Run (after writer visual QA confirmed ≥90%)

- bible-upgrade-tier1.txt — 50 Tier 1 Bible rewrites — in mpw-scripts\ — format: slug:Term:Category:1
- batch09.txt — 100 track breakdowns — run after Tier 1

## Moat 1 — Glossary Tooltip System — Full Implementation Spec

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

## May 16, 2026 — SESSION 32 FINAL — KEY DECISIONS

**Three-Tier Bible Template System — LOCKED:**
| Tier | Name | Word Range | Pass 2 Prose Target |
|---|---|---|---|
| 1 | Flagship | 6,800–7,800w | 5,800–6,500w |
| 2 | Standard | 3,800–5,000w | 3,000–3,800w |
| 3 | Reference | 1,500–2,500w | 1,200–1,800w |

**Infrastructure (Session 33):**
- Fastmail: team@musicproductionwiki.com — MX records at Netlify DNS — DKIM/SPF verified
- Kit: free plan — up to 10K subscribers with API — key saved
- Beehiiv: free Launch plan — up to 2,500 subscribers — welcome email configured

## May 16, 2026 — SESSION 31 FINAL — STRATEGIC PLANNING + HANDOFF

### What Was Decided
Nav architecture locked: MPW slim bar + Bible bar + entry nav. Identity bar removed. Progress bar desktop removed, mobile kept. Quotes system confirmed (quotes.json, Pass 1.5). 13 new v5.1 features confirmed. Three-tier word count system initiated.

### What Was Built
quotes.json v2 (318 quotes, 177 people). All 6 handoff modules Session 31 Final. Nav stack mockup approved. v5.1 spec written.

---

# ⛔ ANTI-TRUNCATION RULE #9 — FINAL CHECK BEFORE COMMITTING HANDOFF

Before running commit_handoff_s36.py or any handoff commit script:
1. Count lines in each output file: `wc -l MPW-HANDOFF-*.md`
2. Compare against previous version line counts
3. Any file with fewer lines than its predecessor must be investigated — truncation is likely
4. Do NOT commit until all files are confirmed full length
5. If you cannot fit the full handoff in one context window, deliver the files individually across multiple sessions — do NOT truncate to fit

---

# ⛔ ANTI-TRUNCATION RULE #10 — THIS RULE EXISTS BECAUSE TRUNCATION NEARLY DESTROYED THE PROJECT

In Session 36, the CORE handoff was delivered at 527 lines when the original was 848 lines — a loss of 321 lines containing Sections 32, 33, infrastructure reference, gold standard feature list, moat implementation specs, and tooltip system code. If this had been committed to GitHub, all future sessions would have permanently lost that context. The project's continuity depends entirely on these handoff files being complete.

TRUNCATION = PROJECT DESTRUCTION. NEVER TRUNCATE. WARN AND STOP INSTEAD.
