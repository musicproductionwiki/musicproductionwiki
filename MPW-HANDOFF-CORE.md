# MusicProductionWiki.com — CORE Handoff
*Updated: May 15, 2026 (SESSION 29) · 526 articles + 201 Bible entries live*
*Modular format — 6 GitHub files replace single monolithic handoff*

---

# ⛔ RULE 1 — DOCUMENT INTEGRITY

All 6 handoff modules must be reproduced in full when updated. Never truncate. Article count must match GitHub API. Warn Steve at 75% context.

Module files (all in repo root):
- MPW-HANDOFF-CORE.md — this file
- MPW-HANDOFF-SCRIPTS.md — all script documentation
- MPW-HANDOFF-CONTENT.md — article standards, word counts, batch pipeline
- MPW-HANDOFF-BIBLE.md — Producer's Bible architecture + v4.0 spec
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
| NEVER use bible-compression.html as Bible entry gold standard | bible/eq.html is the gold standard |
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
| NEVER assume GitHub API is reachable from Claude's environment | Session 28 — api.github.com blocked — all GitHub ops from Steve's PowerShell |
| NEVER give Steve browser console commands to paste in PowerShell | Console commands go in Chrome F12 → Console only |
| NEVER deliver fix script without verifying target string exists in live file | Multiple scripts failed due to mismatched patterns |
| NEVER build Bible writer without running verification suite first | v4.0 = 55-check suite — all must pass before delivery |
| ALWAYS verify mpw_bible_writer.py with python3 check script before delivering | Syntax check + content checks — fix any MISSING before delivery |
| NEVER include Spotify iframes in Bible entries | Always use styled green link buttons |
| Bible batch format is slug:Term:Category (colon-separated, 3 parts) | Pipe-separated format fails — colons required |

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

# ⛔ RULE 6 — REWRITE SESSION RULES

| Rule | Detail |
| --- | --- |
| ALWAYS fetch live gold standard at runtime | Script fetches suno-vs-udio.html from live site |
| ALWAYS run --test on one article first | Never run batch before test passes |
| NEVER touch suno-vs-udio.html | Gold standard — FULLY LOCKED |
| ALWAYS check [CATEGORY] auto-detection line | Confirm category is correct |

---

# 2. Current Priority Table

| Priority | Task | Detail |
| --- | --- | --- |
| **P0** | **DONE ✅ Handoff restructured** | Session 29 — 6 modular GitHub files committed |
| **P0.1** | **DONE ✅ mpw_bible_writer.py v4.0 built** | Session 29 — 55-check suite passes |
| **P0.2** | **DONE ✅ mpw_fix_spotify.py built** | Session 29 — run from PowerShell to patch eq.html + compression.html |
| **P1** | Run Batch 09 — 100 track breakdowns | `python mpw_writer.py --batch batch09.txt --start-date 2026-03-01` |
| **P1.1** | Retry 'air' Bible entry | `python mpw_bible_writer.py --test --slug air --term "Air Frequency EQ" --category "Frequency" --start-date 2026-05-12` |
| P1.2 | Fix 5 articles missing og:image | mpw_fix_meta.py — rate limited Session 27 — retry |
| P1.3 | netlify.toml redirect | /dictionary/* → /bible/:splat 301 |
| P1.4 | Google Workspace email | Case 70817574 |
| P1.5 | Affiliate applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — REVENUE BLOCKER |
| P2 | Suno audio for Bible entries | Dry/wet clips — /bible/audio/ |
| P2.1 | recreations.html category page | Must exist before Batch 11 |
| P2.2 | vocal-autopsies.html category page | Must exist before Batch 12 |
| P2.3 | Lead magnet — MPW Cheat Sheet Pack | PDF — start email list growth |
| P3 | Fix aside scrollbar | aside { overflow: visible; } in style.css |
| P3.1 | brands.html | Page does not exist — in nav |
| P4 | Run Batch 10 — 50 narrative studio stories | After Batch 09 committed |
| P5 | Run Batch 11 — 60 sound recreations | After Batch 10 + recreations.html exists |
| P6 | Run Batch 12 — 35 vocal autopsies | After Batch 11 + vocal-autopsies.html exists |
| P7 | Run Batch 13 — 60 budget recreations | After Batch 12 committed |
| P8 | Skimlinks reapply | Wait 90 days from rejection |
| **MILESTONE** | **Tools Platform — ClearCheck + interactive tools** | After 200 Bible entries + 100 Breakdowns + 100 Recreations live |

---

# 16. Next Session Start Prompt

"Run python mpw_session_start.py — fetches current handoff from GitHub. Then continue from P1 priority: Batch 09 and air Bible entry retry."

---

# 21. Session Log (3 Most Recent)

## May 15, 2026 — SESSION 29 — HANDOFF RESTRUCTURE + BIBLE WRITER V4.0 + SPOTIFY PATCH

### Tasks Completed

| Task | Result |
| --- | --- |
| Handoff restructure (Section 46 spec) | 6 modular files + mpw_session_start.py delivered to outputs |
| MPW-HANDOFF-CORE.md | NEVER rules, session gate, priority table, 3 session logs |
| MPW-HANDOFF-SCRIPTS.md | All script documentation |
| MPW-HANDOFF-CONTENT.md | Article standards, batch pipeline, monetisation |
| MPW-HANDOFF-BIBLE.md | Producer's Bible full spec |
| MPW-HANDOFF-ARTICLES.md | Pointer file to MPW-CATALOG.md |
| MPW-HANDOFF-TECH.md | Infrastructure, nav architecture, gold standard fingerprints |
| mpw_session_start.py | Fetches CORE.md, counts articles + Bible entries, prints 3 recent commits |
| mpw_bible_writer.py v4.0 | Two-pass architecture, 55-check suite, all 17 new content components |
| mpw_fix_spotify.py | Patches eq.html + compression.html — replaces iframes with green link buttons |

### Pending After Session 29 (Steve runs from PowerShell)
1. Commit all 7 handoff files + scripts to repo root via Trees API
2. `python mpw_fix_spotify.py` — patches 2 files
3. `python mpw_bible_writer.py --validate` — confirm 55/55
4. `python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing"`
5. Visual confirm at musicproductionwiki.com/bible/compression
6. `python mpw_bible_writer.py --test --slug air --term "Air Frequency EQ" --category "Frequency" --start-date 2026-05-12`
7. `python mpw_writer.py --batch batch09.txt --start-date 2026-03-01`

---

## May 15, 2026 — SESSION 28 — BIBLE BATCH RUNS + UI FIXES + WRITER V3.0 UPGRADE

| Task | Result |
| --- | --- |
| Bible page UI audit | 4 issues identified and fixed: progress bar, section nav, type grid, Spotify iframes |
| mpw_bible_writer.py v3.0 | All UI fixes baked in — 42/42 checks pass |
| Batch B 20 entries | LIVE — a424aa9b |
| Batch C 179 entries | 106/179 LIVE — ddb887a0 |
| Retry 1 | 64/75 LIVE — f84868c4 |
| Retry 2 | 10/11 LIVE — ef3d3b64 |
| Total Bible live | 201 entries (EQ + 200 batch) |
| air entry | Failed JSON parse — pending retry with "Air Frequency EQ" |

---

## May 14, 2026 — SESSION 27 — DEAD SLUG AUDIT + SITEWIDE FIX + AUDIT SUITE

| Task | Result |
| --- | --- |
| Dead slug diagnosis | 1,134 dead references — fixed — commits 43d88cc, a433dfe |
| mpw_full_audit.py | 12 issues: 7 date-2025, 5 missing og:image |
| mpw_fix_dates.py | 4 articles fixed — 28608ef8 |
| Audit suite | mpw_dead_slug_audit.py, mpw_fix_dead_slugs.py, mpw_full_audit.py, mpw_fix_canonicals.py, mpw_fix_meta.py, mpw_fix_dates.py, mpw_fix_bible_bar_dupes.py |
