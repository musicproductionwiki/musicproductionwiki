# MusicProductionWiki.com — CORE HANDOFF
*Updated: May 14, 2026 — SESSION 28 — HANDOFF RESTRUCTURE*
*Single source of truth for session gates, NEVER rules, and current priorities.*
*This file MUST stay under 400 lines. Trim oldest session log when adding new one.*

---

# ⛔ RULE 1 — DOCUMENT INTEGRITY
Reproduce in full when updated. Never truncate. Article count must match GitHub API. Warn Steve at 75% context. A shorter handoff is a broken handoff.

---

# ⛔ RULE 2 — SESSION START IS A HARD GATE

**Run `python mpw_session_start.py` — it fetches the current handoff from GitHub. Never rely on a delivered .md file.**

Do not take any action until you have stated back to Steve:
1. The current article count (from Trees API)
2. The current P0 priority (from Section 2 below)
3. The three most recent commits
4. Every NEVER rule from Rule 3 that applies to this session

**Fetch any module on demand:**
```
python mpw_session_start.py --fetch scripts
python mpw_session_start.py --fetch content
python mpw_session_start.py --fetch bible
python mpw_session_start.py --fetch articles
python mpw_session_start.py --fetch tech
```

---

# ⛔ RULE 3 — NEVER RULES
These apply every session without exception. Recite the relevant ones at session start.

| Rule | Detail |
| --- | --- |
| NEVER enable Netlify Pretty URLs | Breaks site |
| NEVER zip over 200KB | Cloudflare intercepts — save via Notepad → Save As → All Files |
| NEVER write partial batches | All articles first, commit once |
| NEVER update index.html for rewrites | Only new filenames need index updates |
| NEVER propose topics without duplicate check | Fetch MPW-HANDOFF-ARTICLES.md via session_start |
| NEVER deliver under minimum word count | See MPW-HANDOFF-CONTENT.md |
| NEVER use Updated May 2025 | Always 2026 |
| NEVER truncate this handoff | Full reproduction required |
| NEVER use GitHub web editor for CSS or JS | Silent corruption — always fetch via API → edit → commit via API PUT |
| NEVER start normalisation before gold standard confirmed clean | Gold standard = suno-vs-udio.html — LOCKED |
| NEVER rewrite suno-vs-udio.html | It is the gold standard — do not touch it |
| NEVER run injection scripts blind | Test on 3 articles first — May 7 scripts caused site-wide damage |
| NEVER declare audit results reliable without visual confirmation | String matching is not sufficient |
| NEVER run batch before --test passes and article is visually confirmed live | One test article confirmed on live site before any batch |
| NEVER let Claude auto-detect category without checking the result | Always confirm [CATEGORY] line in output |
| NEVER commit an article with garbled share buttons | Share buttons must render cleanly before commit |
| NEVER change a review score between runs | Score must be extracted from existing article and locked |
| NEVER COMMIT MULTIPLE FILES INDIVIDUALLY | ALWAYS use GitHub Trees API — single commit — single Netlify deploy |
| NEVER run a sitewide fix script with parallel blob creation | Session 27: hits GitHub secondary rate limit — always sequential with exponential backoff on 403s |
| NEVER assume GitHub rate limit is cleared after first retry | Token needs 10-15 minute cooldown after heavy API usage |
| ALWAYS run mpw_dead_slug_audit.py after every batch commit | mpw_commit_articles.py now runs this automatically |
| ALWAYS run mpw_slugs.py before every batch write AND after every batch commit | Stale slugs.txt causes dead related-article links |
| NEVER use parallel thread fetching for GitHub Contents API in fix scripts | 15-20 thread parallel fetching triggers secondary rate limit — use 10 threads max |
| TREES API MANDATORY — all fix scripts | mpw_fix_dead_slugs.py, mpw_fix_canonicals.py, mpw_fix_meta.py, mpw_fix_dates.py, mpw_fix_bible_bar_dupes.py all use Trees API |
| NEVER run multiagent batch without --dry-run first | Always dry-run, then --test on one article, then full run |
| NEVER run mpw_count.py using old GitHub contents API | OLD version hangs — Trees API version only |
| NEVER trust local slugs.txt as article count source | Use mpw_count.py for authoritative count |
| NEVER include main.js on /bible/ pages | Conflicts with Bible nav JS — crashes silently |
| NEVER touch bible/eq.html | NEW Bible gold standard — LOCKED |
| NEVER touch bible/compression.html | LIVE — commit e387c341 — NOT the template |
| NEVER commit handoff updates as .docx only | Handoff updates committed to GitHub via Trees API. .docx is optional for human reading only. |

---

# ⛔ RULE 3B — 75% CONTEXT WARNING — MANDATORY
At 75% context, Claude must stop and say:
> **"⚠️ I am at approximately 75% context. I will complete the current task only, then update the handoff and stop. A new session is required after this."**

Signs: responses feel compressed; difficulty recalling early session details; temptation to summarise; instinct to skip a step. At any of these signs — stop and warn Steve immediately.

---

# ⛔ RULE 4 — CALL OUT SKIPPED STEPS IMMEDIATELY
If Claude skips a session start step, delivers output without required deliverables, or acts before the hard gate — Steve must call it out immediately.

---

# ⛔ RULE 5 — DELIVERABLES CHECKLIST
Every session end requires ALL of the following:
- [ ] Updated MPW-HANDOFF-CORE.md committed to GitHub via Trees API
- [ ] All 6 module files updated if content changed — committed in one Trees API commit
- [ ] Session log updated with full detail in CORE
- [ ] Section 2 Priority table updated
- [ ] mpw_session_start.py can fetch and print CORE cleanly
- [ ] .docx optional — for human reading only

---

# ⛔ RULE 6 — REWRITE SESSION RULES
| Rule | Detail |
| --- | --- |
| ALWAYS fetch live gold standard at runtime | Script fetches suno-vs-udio.html from live site |
| ALWAYS run --test on one article first | Never run batch before test passes |
| NEVER touch suno-vs-udio.html | Gold standard — FULLY LOCKED |
| NEVER deliver a zip over 200KB | Cloudflare blocks it |
| ALWAYS check [CATEGORY] auto-detection line | Confirm category is correct |
| ALWAYS check [SCORE] line on reviews | Must show extracted score |
| Glossary articles auto-detect as glossary | Token limit fixed to 20,000 in v6.4 |

---

# ⛔ RULE 8 — PRODUCER'S BIBLE SESSION RULES
| Rule | Detail |
| --- | --- |
| Read MPW-HANDOFF-BIBLE.md at start of every Bible session | Strategic foundation — never skip |
| NEVER start writing entries before gold standard entry approved | bible/eq.html is approved and LIVE |
| NEVER set datePublished before May 6, 2026 | Site launched May 6-7, 2026 |
| bible/eq.html is the NEW gold standard entry | Session 24 — LIVE — layout + mobile RESOLVED Session 26 ✅ |
| bible-compression.html is LOCKED but NOT the template | LIVE — commit e387c341 — DO NOT use as template |
| NEVER load main.js on Bible pages | Conflicts with Bible nav JS |
| Bible URL structure is /bible/ NOT /dictionary/ | LOCKED Session 9 |
| 301 redirect needed in netlify.toml | /dictionary/* → /bible/:splat 301 |
| bible-index.json must exist before Bible search works | Path: /bible-index.json in repo root |

---

# 2. Priority Table — Current

| Priority | Task | Status |
| --- | --- | --- |
| DONE | Restructure handoff into modular files on GitHub | SESSION 28 — COMPLETE |
| P0 | Run Bible Batch B — 20 entries | batch14-B.txt ready — --start-date 2026-05-12 |
| P0.2 | Patch about.html with bible bar | Run python one-liner — see MPW-HANDOFF-SCRIPTS.md |
| P0.3 | Run Bible Batch C — 179 entries | After Batch B confirmed |
| P1 | Run Batch 09 — 100 track breakdowns | mpw_writer.py v3.0 ready — breakdowns.html LIVE |
| P1.1 | Fix 5 articles missing og:image | python mpw_fix_meta.py — rate limited Session 27 |
| P1.2 | netlify.toml — 301 redirect | /dictionary/* → /bible/:splat 301 |
| P1.3 | Google Workspace email setup | Case 70817574 — dispute pending |
| P1.4 | Affiliate program applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox |
| P2 | Suno audio for Bible entries | After Batch B confirmed |
| P2.1 | recreations.html category page | Must exist before Batch 11 |
| P2.2 | vocal-autopsies.html category page | Must exist before Batch 12 |
| P2.3 | Lead magnet — MPW Cheat Sheet Pack | Start email list growth |
| P3 | Fix aside scrollbar | aside { overflow: visible; } in style.css |
| P3.1 | brands.html | Page does not exist — in nav |
| P4 | Run Batch 10 — 50 studio stories | After Batch 09 committed |
| P5 | Run Batch 11 — 60 recreations | After Batch 10 + recreations.html |
| P6 | Run Batch 12 — 35 vocal autopsies | After Batch 11 + vocal-autopsies.html |
| P7 | Run Batch 13 — 60 budget recreations | After Batch 12 |
| P8 | Skimlinks reapply | Wait 90 days from rejection |
| MILESTONE | Tools Platform — ClearCheck + interactive tools | After 200 Bible + 100 Breakdowns + 100 Recreations live |

---

# 1. Site Status

| Key | Value |
| --- | --- |
| Live URL | musicproductionwiki.com |
| GitHub repo | github.com/musicproductionwiki/musicproductionwiki |
| Netlify site ID | classy-haupia-be8e43 |
| Stack | Pure HTML / CSS / vanilla JS — no frameworks |
| Articles live | 526 (confirmed May 14, 2026 via Trees API) |
| Bible entries live | 2 (bible/compression.html + bible/eq.html — BOTH resolved ✅) |
| Sitemap | 598 URLs — commit b3770cb1 — RESUBMITTED TO GSC May 13, 2026 ✅ |
| Gold standard article | suno-vs-udio.html — FULLY LOCKED |
| Bible gold standard | bible/eq.html — LIVE — LOCKED |
| search-index.json | 526 entries — CLEAN — commit 925f3931 |
| GA4 | G-79VB543KCT |
| Scripts location | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ |
| Handoff modules | Repo root — 6 x MPW-HANDOFF-*.md |

---

# 21. Session Log — 3 Most Recent

## May 14, 2026 — SESSION 28 — HANDOFF RESTRUCTURE

| Task | Result |
| --- | --- |
| Split monolithic handoff into 6 modular files | CORE, SCRIPTS, CONTENT, BIBLE, ARTICLES, TECH |
| Committed all 6 files to GitHub repo root | Trees API — single commit via mpw_commit_handoff.py |
| Wrote mpw_session_start.py | Fetches CORE from GitHub, prints article count, recent commits, module list |
| Updated Rule 2 | Now requires mpw_session_start.py — no longer relies on delivered .md |
| Updated Rule 5 | Handoff updates committed to GitHub — .docx optional only |
| Article list in ARTICLES.md | Regenerated from live GitHub Trees API slug list |

## May 14, 2026 — SESSION 27 — DEAD SLUG AUDIT + SITEWIDE FIX + AUDIT SUITE

| Task | Result |
| --- | --- |
| Dead slug diagnosis | 290 unique dead slugs sitewide — 1,134 references |
| mpw_slugs.py delivered | Trees API slug list to slugs.txt |
| mpw_dead_slug_audit.py built | 7-check audit — CSV output |
| mpw_fix_dead_slugs.py built + run | Sequential blobs — 1,209 dead refs fixed — commits 43d88cc + a433dfe |
| mpw_full_audit.py built | 13-check audit — only 12 issues on 526-article site |
| mpw_fix_dates.py built + run | 4 articles fixed — commit 28608ef8 |
| mpw_commit_articles.py updated | Auto-runs dead slug audit after every commit |
| Key commits | 7201c51, 43d88cc, a433dfe, 28608ef8 |
| Key lessons | Parallel blob creation hits rate limit — always sequential. 15 min cooldown after heavy API usage. |

## May 14, 2026 — SESSION 26 — BIBLE MOBILE FIXES + TOOLS STRATEGY

| Task | Result |
| --- | --- |
| Bible mobile fix v1/v2 BROKEN | Both stripped style blocks — nuked CSS — reverted |
| Bible mobile fix v3 SUCCESS | Targeted only body/html overflow — LIVE ✅ |
| bible/compression.html mobile + footer | Fixed — LIVE ✅ |
| bible/eq.html declared new gold standard | Full Tier 1 features — LOCKED ✅ |
| Tools Platform spec written | ClearCheck + 9 interactive tools milestone |

---

# 16. Next Session Start Prompt

```powershell
cd C:\Users\swarn\OneDrive\Desktop\mpw-scripts
. .\setenv.ps1
python mpw_session_start.py
```

Say to Claude: **"Run the session start script output above and continue."**

Claude must then: (1) state article count, (2) state P0, (3) recite applicable NEVER rules, (4) state 3 most recent commits, (5) confirm Rule 5 deliverables before signing off.
