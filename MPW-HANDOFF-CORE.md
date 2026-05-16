# MusicProductionWiki.com — CORE Handoff
*Updated: May 15, 2026 (SESSION 30) · 526 articles + 202 Bible entries live*
*Modular format — 6 GitHub files replace single monolithic handoff*

---

# ⛔ RULE 1 — DOCUMENT INTEGRITY

All 6 handoff modules must be reproduced in full when updated. Never truncate. Article count must match GitHub API. Warn Steve at 75% context.

Module files (all in repo root):
- MPW-HANDOFF-CORE.md — this file
- MPW-HANDOFF-SCRIPTS.md — all script documentation
- MPW-HANDOFF-CONTENT.md — article standards, word counts, batch pipeline
- MPW-HANDOFF-BIBLE.md — Producer's Bible architecture + v5.0 spec
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
| NEVER use GitHub web editor for CSS or JS | Silent corruption — always fetch via API → edit → commit via API PUT |
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
| NEVER run batches 09-13 before new category pages exist | breakdowns.html LIVE ✅ — recreations.html + vocal-autopsies.html must exist first |
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
| NEVER run mpw_count.py using old GitHub contents API pagination | Replaced with Trees API version ✅ |
| ALWAYS use mpw_slugs.py after every batch commit | Refreshes slugs.txt from live repo |
| NEVER trust local slugs.txt as article count source | Only accurate immediately after mpw_slugs.py |
| NEVER fix title capitalisation in mpw_search_index.py as patch | Correct fix is in article <title> tags |
| NEVER include main.js on /bible/ pages | Conflicts with Bible page nav JS — crashes silently |
| NEVER write Bible page JS via Python heredoc with single-quote escaping | Use raw string r"""...""" |
| NEVER commit bible-index.json before /bible/index.html exists | Index page must exist first — RESOLVED ✅ |
| NEVER use position:absolute for dropdowns inside section with overflow:hidden | Use position:fixed with getBoundingClientRect() |
| NEVER use bible-compression.html as Bible entry gold standard | bible/eq.html is the v3.0 gold standard |
| NEVER run mpw_bible_writer.py without --test first and visual confirmation | Mandatory — always test before batch |
| NEVER guess Bible entry layout CSS | Always derive from live gold standard via DevTools |
| ANTHROPIC_KEY env var is ANTHROPIC_API_KEY in setenv.ps1 | Script reads ANTHROPIC_API_KEY — also ANTHROPIC_KEY as fallback |
| PASS1_TOKENS must be 20000 for Bible entries | Lower values truncate JSON |
| NEVER run sitewide fix script with parallel blob creation | Always sequential with exponential backoff on 403s |
| ALWAYS run mpw_dead_slug_audit.py after every batch commit | Dead slugs accumulate silently |
| ALWAYS run mpw_slugs.py before every batch write AND after every batch commit | Stale slugs cause dead related-article links |
| NEVER use parallel thread fetching for GitHub Contents API in fix scripts | 15-20 threads triggers secondary rate limit — use 10 max |
| NEVER paste Python code directly into PowerShell | Save as .py file and run python script.py |
| NEVER strip entire <style> blocks when looking for CSS fingerprints | Nukes all page CSS — use append-only with !important |
| NEVER write Bible page mobile fixes that touch desktop CSS | ALL Bible mobile fixes are @media(max-width:768px) only |
| ALWAYS append mobile CSS as new <style> block — never strip-and-replace | Append-only approach is correct |
| NEVER guess live HTML structure of Bible page before writing patch | Always fetch live HTML first |
| NEVER run parallel blob creation for GitHub API | Always sequential with 403 backoff |
| NEVER assume GitHub API is reachable from Claude's environment | api.github.com blocked — all GitHub ops from Steve's PowerShell |
| NEVER give Steve browser console commands to paste in PowerShell | Console commands go in Chrome F12 → Console only |
| NEVER deliver fix script without verifying target string exists in live file | Multiple scripts failed due to mismatched patterns |
| NEVER build Bible writer without running verification suite first | v5.0 = 54-check suite — all must pass before delivery |
| ALWAYS verify mpw_bible_writer.py with python3 check script before delivering | Syntax check + content checks — fix any MISSING before delivery |
| NEVER include Spotify iframes in Bible entries | Always use YouTube search link buttons |
| Bible batch format is slug:Term:Category (colon-separated, 3 parts) | Pipe-separated format fails — colons required |
| NEVER patch Bible template incrementally across multiple iterations | One complete rewrite — audit fully — then test once |
| NEVER remove Sound Better from desktop nav | Desktop keeps it — mobile only removal via @media(max-width:1024px) |
| NEVER use direct Spotify track URIs in Bible entries | AI hallucinates fake IDs — use YouTube search links instead |
| NEVER allow producer quote to render with literal asterisks | Strip asterisks in post-processing — wrap in <blockquote class="producer-quote"> |
| NEVER allow emotional_hook to render with literal asterisks | Strip asterisks via .strip().strip('*').strip() in masthead |
| NEVER allow AI to output related_terms or further_reading slugs not in CONFIRMED_LIVE_SLUGS | Validate at build time — omit invalid ones — sidechain-compression and transient-shaping CONFIRMED 404 |
| NEVER run Tier 1 batch before Bible template passes full desktop AND mobile visual QA | Template is v5.0 — test --slug compression first |
| NEVER use position:sticky with overflow:hidden on parent | Use overflow:clip instead — hidden creates stacking context that breaks sticky |
| NEVER hardcode Bible category anchor links (/bible/#frequency etc) | Bible index has no anchor sections — link to /bible/categories/{slug} instead |
| NEVER link track examples to MPW article pages | YouTube search links only |
| NEVER include track_examples spotify_uri in Pass 1 JSON | AI hallucinates URIs — removed from schema entirely |
| NEVER use open.spotify.com/search/ URLs | Requires login — SSL error on click |
| History API pushState MUST be used when opening mobile drawer | Prevents back button navigating away from current page |
| NEVER set $env:GITHUB_TOKEN or $env:ANTHROPIC_API_KEY inline in a .py file committed to GitHub | GitHub secret scanning blocks the commit — always use env vars |
| ALWAYS set both env vars at start of every PowerShell session | $env:GITHUB_TOKEN and $env:ANTHROPIC_API_KEY — both required |

---

# ⛔ RULE 3B — 75% CONTEXT WARNING — MANDATORY

At 75% context, Claude must stop all work immediately and tell Steve:

***"⚠️ I am at approximately 75% context. I will complete the current task only, then update the handoff and stop. A new session is required after this."***

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

# 2. PRIORITY TABLE (Updated Session 30)

| Priority | Task | Status | Detail |
|---|---|---|---|
| **P0** | Run --test on compression | ❌ NOT YET RUN | python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing" |
| **P0.1** | Desktop + mobile visual QA | ❌ NOT YET DONE | Must pass all checks before any batch |
| **P0.2** | Run mpw_bible_cat_pages.py --run | ❌ NOT YET RUN | Generates 8 Bible category pages at /bible/categories/{slug} |
| **P1** | Tier 1 batch — 50 Bible rewrites | After P0 confirmed | bible-upgrade-tier1.txt ready in mpw-scripts\ |
| **P1.1** | Sitemap regeneration + GSC resubmission | After Tier 1 batch | 202 Bible entries not yet in sitemap |
| **P1.2** | Air Bible entry retry | After template confirmed | --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency" |
| **P1.3** | netlify.toml redirect /dictionary/* → /bible/:splat | Pending | 301 redirect for old URLs |
| **P2** | Batch 09 — 100 track breakdowns | After Tier 1 | python mpw_writer.py --batch batch09.txt --start-date 2026-03-01 |
| **P3** | Fix 5 articles missing og:image | mpw_fix_meta.py | Rate limited Session 27 — retry |
| **P4** | Affiliate applications | REVENUE BLOCKER | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — Steve must do |
| **P5** | Google Workspace email | Steve action | Case 70817574 — domain-in-use conflict |
| **P6** | recreations.html category page | Before Batch 11 | Must exist before Batch 11 runs |
| **P7** | vocal-autopsies.html category page | Before Batch 12 | Must exist before Batch 12 runs |
| **P8** | Bible index page redesign | Future session | Current index doesn't match v5.0 entry design language |
| **P9** | Dreaming integration | After Tier 1 batch | Request Managed Agents access — implement after real session history exists |

---

# 16. NEXT SESSION START PROMPT (Session 31)

"Session 30 completed mpw_bible_writer.py v5.0 and ran out of context before testing. Steve has both files: mpw_bible_writer.py and mpw_bible_cat_pages.py in mpw-scripts. P0 is: run . .\setenv.ps1, then python mpw_bible_writer.py --validate (must show 54/54), then python mpw_bible_writer.py --test --slug compression --term 'Compression' --category 'Signal Processing'. Confirm live page on desktop AND mobile. Then run python mpw_bible_cat_pages.py --run to commit 8 Bible category pages. Then run Tier 1 batch. Do NOT patch mpw_bible_writer.py further before testing — it has been patched 30+ times this session."

---

# 21. SESSION LOG (3 Most Recent)

## May 15, 2026 — SESSION 30 — BIBLE WRITER v5.0 COMPLETE + CATEGORY PAGES

### What Was Completed
Full rewrite of build_html() in mpw_bible_writer.py — v5.0. 54/54 validation checks pass. Two new scripts delivered.

### Scripts Delivered This Session
| Script | Status | Location |
|---|---|---|
| mpw_bible_writer.py v5.0 | ✅ 54/54 checks — ready to test | mpw-scripts\ |
| mpw_bible_cat_pages.py | ✅ Syntax OK — ready to run | mpw-scripts\ |

### mpw_bible_writer.py v5.0 — What Changed from v4.0

**HEAD block:**
- Title: `{term} — The Producer's Bible | MusicProductionWiki.com`
- og:image: hardcoded to og-default.jpg fallback
- Added: og:image:width/height, article:published/modified/section, og:locale
- Added: robots meta
- Added: twitter:image, twitter:site @mpwikiofficial
- Added: GA4 (G-79VB543KCT)
- 4 separate schema script blocks: Article, FAQPage, BreadcrumbList, Speakable
- sameAs on Article schema from Pass 1 schema_about_same_as field
- dateModified always uses today's date (not pub_date) — signals rewrites to Google

**Sticky chain fixed (overflow:clip not overflow:hidden):**
- Bible identity bar: position:sticky top:0 z:600 height:32px — desktop only
- Main nav: position:sticky top:32px z:500 height:60px
- Entry nav: position:sticky top:92px z:400 (desktop) / top:96px (mobile)
- Dropdowns: z:99999 — above everything
- Mobile: identity bar hidden, nav resets to top:0, bible bar top:60px z:300, entry nav top:96px

**Nav:**
- "The Producer's Bible" is now a dropdown with all 8 Bible categories
- Sound Better restored on desktop, hidden at ≤1024px
- Hamburger at ≤1024px
- Mobile drawer: 2-column grid for Bible categories, Articles, and Gear sections
- History API pushState on drawer open — back button closes drawer, not navigates away

**Content fixes:**
- emotional_hook: asterisks stripped via .strip().strip('*').strip()
- producer_quote: asterisks stripped, wraps in blockquote.producer-quote
- signal_chain_position: extracted before f-string (was TypeError: unhashable type)
- Related terms: validated against CONFIRMED_LIVE_SLUGS at build time
- Further reading: validated against CONFIRMED_LIVE_SLUGS at build time
- sidechain-compression and transient-shaping REMOVED from confirmed slug list (confirmed 404 live)

**Track examples — root cause fixed:**
- track_examples now in Pass 1 JSON schema (was missing — caused "Unknown" titles)
- spotify_uri removed from schema entirely (AI hallucinates fake IDs)
- Pass 2 receives locked track list extracted from Pass 1 — cannot invent new tracks
- Reference links use YouTube search: google.com/search is gone, youtube.com/results?search_query= is live
- Section heading: "Listen on YouTube"

**Social share:**
- Removed from content body
- Added to sidebar (visible while reading)
- Added to footer (X and Reddit links)

**Newsletter:**
- Full-width breakout strip (margin:-24px, border-top/bottom amber)

**Sidebar:**
- align-self:start added — required for position:sticky to work
- top:120px
- "Browse The Bible" hardcoded list replaced with dynamic Related Terms from entry
- Related Terms also shown in sidebar with validation

**Bible identity bar:**
- "◆ The Producer's Bible" dominant (large amber bold)
- "A MusicProductionWiki Publication" secondary (dimmed)

**Signal chain SVG:**
- Fixed-width 140px boxes, labels truncated at 18 chars with ellipsis
- dominant-baseline:middle for text centering
- width:100% SVG scales to container

**Mobile:**
- Search button added to mobile drawer
- Back-to-top: bottom:32px right:20px (clears iOS home indicator)
- Entry nav: "Sections ›" label at left, 11px font, pill-shaped links
- overflow:clip on html/body (not overflow:hidden — hidden breaks sticky)

### mpw_bible_cat_pages.py — New Script

Generates 8 Bible category pages at /bible/categories/{slug}/index.html:
- dynamics, frequency, time-based, signal-processing, mixing, mastering, synthesis, music-theory
- Each page: identity bar, nav with Bible dropdown, hero, category siblings strip, client-side search/filter, entry card grid from bible-index.json
- Run: `python mpw_bible_cat_pages.py --test` then `python mpw_bible_cat_pages.py --run`

### What Was NOT Done This Session
- --test not run (session ran out of context)
- Desktop/mobile visual QA not done
- Tier 1 batch not run
- Category pages not committed
- Handoff not committed to GitHub (Steve must run commit_handoff.py)

### Issues Identified and Fixed This Session
| Issue | Root Cause | Fix |
|---|---|---|
| Progress bar + nav not sticky | overflow:hidden on body creates stacking context | Replaced with overflow:clip |
| "Unknown" track titles | track_examples missing from Pass 1 JSON schema | Added to schema — Pass 2 receives locked list |
| Spotify links 404 | AI hallucinates fake track IDs | Removed URI entirely — YouTube search URLs |
| Spotify search SSL error | open.spotify.com/search requires login | Replaced with YouTube search |
| Related terms 404 | sidechain-compression + transient-shaping in slug list but not live | Removed from CONFIRMED_LIVE_SLUGS |
| Asterisks on emotional_hook | No stripping in masthead render | .strip().strip('*') added |
| Identity bar wrong hierarchy | Publication credit was dominant | "The Producer's Bible" now dominant |
| Sidebar hardcoded entries | Shows Compression link on Compression page | Dynamic related terms from entry |
| Bible categories flat list | Not 2-column in drawer | All drawer sections now 2-column grid |
| Back button navigates away | Drawer open not in browser history | History API pushState on drawer open |
| signal_chain_position TypeError | Dict access inside f-string | Extracted to variable before f-string |

---

## May 15, 2026 — SESSION 29B — BIBLE TEMPLATE QA + BUG LIST

### What Was Tested
Live visual QA of musicproductionwiki.com/bible/compression on desktop (Chrome) and mobile (iPhone).

### What Works
| Item | Status |
|---|---|
| Two-pass streaming generation | ✅ Pass 1: 36 fields, Pass 2: 11 fields |
| Word count | ✅ 13,885 words |
| Nav dropdowns desktop | ✅ Articles + Gear working |
| TOC sidebar active highlighting | ✅ Amber highlight on scroll |
| Progress bar | ✅ Percentage-based |
| Back to top button | ✅ Amber, bottom right |
| Further reading links | ✅ /bible/ paths |
| Search overlay opens | ✅ ESC closes |
| Content quality | ✅ Institutional grade |
| mpw_fix_spotify.py | ✅ eq.html + compression.html patched |

### What Was Broken (all fixed in Session 30)
All 25 SEO items, nav stickiness, mobile bible bar, hamburger, asterisks, track examples, social share placement, sidebar, signal chain SVG.

---

## May 15, 2026 — SESSION 29 — HANDOFF RESTRUCTURE + BIBLE WRITER V4.0

| Task | Result |
|---|---|
| Handoff restructure (6 modular files) | ✅ Committed — b0f1fbb |
| mpw_bible_writer.py v4.0 | ✅ Built — streaming, 55-check suite |
| mpw_fix_spotify.py | ✅ Built — patched eq.html + compression.html |
| mpw_session_start.py | ✅ Built — fetches live state |
| commit_handoff.py | ✅ Built — Trees API commit script |

---

# 30. SESSION 30 — BIBLE TEMPLATE v5.0 SPEC (COMPLETED)

See session log above for full list of changes. The v5.0 template is complete. The compression test entry must be run and visually confirmed before any batch.

## CONFIRMED_LIVE_SLUGS (Python constant in mpw_bible_writer.py)

compression, eq, limiting, saturation, distortion, reverb, delay, parallel-compression, multiband-compression, noise-gate, gain-staging, headroom, stereo-imaging, mid-side-processing, bus-compression, mix-bus, send-return, automation, mastering, lufs, dynamic-range, true-peak-limiting, loudness-normalization, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, resonance, harmonic-distortion, chorus, flanger, phaser, tremolo, vibrato, plate-reverb, room-reverb, convolution-reverb, clip-gain, air-frequency-eq, air

NOTE: sidechain-compression and transient-shaping REMOVED — confirmed 404 on live site.

## Desktop Visual QA Checklist (must pass before batch)
- [ ] Progress bar at top, 3px, amber — sticky
- [ ] Identity bar "◆ The Producer's Bible | A MusicProductionWiki Publication" — sticky
- [ ] Nav sticky below identity bar — doesn't move on scroll
- [ ] "The Producer's Bible" nav item opens dropdown with 8 categories
- [ ] Articles and Gear dropdowns work, appear above entry nav
- [ ] Sound Better button present in nav
- [ ] Entry section nav sticky below main nav, active item highlights amber
- [ ] TOC sidebar sticky on right, highlights current section
- [ ] Back to top visible after scrolling
- [ ] Search opens with Ctrl+K, finds Bible + Article results with badges
- [ ] Social share buttons in sidebar and footer
- [ ] Breadcrumb visible above masthead
- [ ] Further Reading links all go to /bible/ (not 404)
- [ ] Related terms all go to /bible/ (not 404)
- [ ] Producer quote styled as blockquote, no asterisks
- [ ] Emotional hook — no asterisks
- [ ] YouTube reference track links open YouTube search
- [ ] Signal chain SVG readable, not overflowing

## Mobile Visual QA Checklist (must pass before batch)
- [ ] No horizontal scroll
- [ ] Identity bar hidden on mobile
- [ ] Bible bar visible as second sticky bar below nav
- [ ] Hamburger shows, tapping opens drawer
- [ ] Drawer: Bible categories in 2-column grid
- [ ] Drawer: Articles in 2-column grid
- [ ] Drawer: Gear in 2-column grid
- [ ] Back button closes drawer (not navigates away)
- [ ] Entry nav "Sections ›" label visible, scrolls horizontally
- [ ] All content full width — nothing cut off right
- [ ] Sidebar hidden
- [ ] Back to top visible after scroll

## Infrastructure Reference

- **Repo:** github.com/musicproductionwiki/musicproductionwiki
- **GitHub Token:** YOUR_GITHUB_TOKEN_HERE (expires Aug 2, 2026)
- **Anthropic API Key:** Set via $env:ANTHROPIC_API_KEY in PowerShell
- **Netlify:** Project ID classy-haupia-be8e43 — auto-deploys on GitHub push
- **Scripts dir:** C:\Users\swarn\OneDrive\Desktop\mpw-scripts\
- **GA4 ID:** G-79VB543KCT
- **Newsletter:** Beehiiv — "The Producer's Briefing"
- **Contact:** mpwikiofficial@gmail.com
- **Twitter/X:** @mpwikiofficial
- **Gold standard article:** articles/suno-vs-udio.html — LOCKED
- **Gold standard Bible entry:** bible/compression.html (v5.0) — after test confirmed
- **OG default image:** /images/og-default.jpg
- **Bible URL structure:** /bible/{slug} — never /dictionary/
- **Bible category pages:** /bible/categories/{slug} — generated by mpw_bible_cat_pages.py

## Pending Owner Actions (Steve must do — not Claude)
1. Affiliate applications: Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — REVENUE BLOCKER
2. Google Workspace email: Case 70817574 — domain-in-use conflict
3. Beehiiv newsletter: confirm embed code for Bible page newsletter widget
4. Twitter/X account: confirm @mpwikiofficial handle is live for share buttons
5. Request Managed Agents access for Dreaming feature (future session)

## Batch Files Ready to Run (after template confirmed)
- `bible-upgrade-tier1.txt` — 50 Tier 1 Bible rewrites — in mpw-scripts\
- `batch09.txt` — 100 track breakdowns — location TBC
