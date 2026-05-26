# MPW SESSION START CARD
*Last updated: May 26, 2026 — Session 75*

---

## CURRENT STATE
| Item | Value |
|------|-------|
| Articles live | 526 |
| Bible entries live | 223 |
| Tools live | 41 |
| Last commit SHA | 806ac1bd — Session 71 SCRIPTS merge complete |
| Model string | `claude-sonnet-4-6` |
| Proxy URL | `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy` |
| GitHub token | `[GITHUB_TOKEN — regenerate at github.com/settings/tokens if expired]` |
| Local path | `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\` |
| Site | `musicproductionwiki.com` |
| Repo | `github.com/musicproductionwiki/musicproductionwiki` |

---

## TOP 3 PRIORITIES
1. Execute mpw_writer.py 4 pending updates — blocks next article batch
2. Execute mpw_bible_writer.py updates (650wpm + nav + v5.3) — blocks next T1 Bible batch
3. Sitemap submitted S75 ✅ — next: request indexing for /bible/reverb, suno-prompt-optimizer, ai-music-rights-navigator

---

## NEVER RULES — TOP 20 (Full canonical list: MPW-NEVER-RULES.md — read every session)

| Rule | Added | Enforcement |
|------|-------|-------------|
| Never touch existing CSS style blocks — append only, new `<style>` block before `</head>` | S26/S65 | SCRIPT |
| Never load `style.css` or `../css/style.css` in tool pages — causes 600px black blob shapes | S68 | SCRIPT |
| Never use `.hero` or `.container` class names in tool pages — conflicts with global CSS | S68 | SCRIPT |
| Never embed Python in HTML/JS — write JS as pure heredoc, run `node --check` before embedding | S67 | SCRIPT |
| Never use `innerHTML` in any tool JS or Bible JS — Netlify CSP blocks it | S57/S58 | SCRIPT |
| Never commit without running `mpw_precommit_check.py` first | S68 | SCRIPT |
| Never use any model except `claude-sonnet-4-6` — never claude-sonnet-4-5 or claude-sonnet-4-20250514 | S68 | SCRIPT |
| Never call Netlify functions via custom domain — always use `classy-haupia-be8e43.netlify.app` | S67 | SCRIPT |
| Never upload any file to GitHub without scanning for raw tokens first (`grep -rn 'ghp_\|sk-ant'`) | S69 | SCRIPT |
| Never set read time below 650 wpm for Bible entries | S63/S64 | SCRIPT |
| Never invent slugs — verify against GitHub tree API before writing any links | S26/S65 | MANUAL |
| Never enable Netlify Pretty URLs — breaks the site | S26 | MANUAL |
| Never truncate handoff documents | S26 | MANUAL |
| Never present files for approval and then commit without waiting for explicit "go" | S71 | MANUAL |
| Never commit a tool without all 5 files in same Trees API commit | S67 | MANUAL |
| Never start a tool build without reading MPW-TOOL-BUILD-SPEC.md first | S66/S68 | MANUAL |
| Never use assistant prefill in API calls — returns empty response body | S67 | MANUAL |
| Never extract nav block with naive find() — use div-depth tracking | S68 | MANUAL |
| Never create AudioContext before a user gesture in Browser Apps | S65b | MANUAL |
| Never run `mpw_bible_writer.py` before updating read time to 650 wpm | S63 | MANUAL |

---

## PENDING OWNER ACTIONS
| Action | Priority | Notes |
|--------|----------|-------|
| Submit sitemap to GSC | ✅ DONE S75 | 780 URLs |
| Update MPW-NEVER-RULES.md in Claude project | P0 | New file — add to project S75 |
| Update MPW-SESSION-START.md in Claude project | P0 | Replace with S75 version (this file) |
| Update MPW-HANDOFF-MERGE-PLAN.md in Claude project | P0 | Mark NEVER-RULES ✅ |
| Commit MPW-NEVER-RULES.md to GitHub | P0 | New master doc — must be in repo |
| Request indexing — /bible/reverb | P1 | GSC URL Inspection |
| Request indexing — suno-prompt-optimizer | P1 | GSC URL Inspection |
| Request indexing — ai-music-rights-navigator | P1 | GSC URL Inspection |
| OG images for both AI tools | P1 | 1200×630px |
| Affiliate applications | P2 REVENUE BLOCKER | Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox |
| Google Workspace domain dispute | P3 | Case #70817574 still open |

---

## LAST SESSION HANDOVER NOTE
Session 75 built MPW-NEVER-RULES.md — 7th master document — 95 rules across 7 categories — sourced from CORE, TECH, SCRIPTS, BIBLE, SESSION-START, CONTINUITY-MASTER-PLAN, and chat history search. SESSION-START updated to top 20 summary linking to canonical file. Merge cycle complete. Post-merge rules fully in effect. Next: mpw_writer.py 4 pending updates (blocks article batch), then mpw_bible_writer.py v5.3 (blocks T1 Bible batch).

---

## SESSION START RITUAL
Steve says: "Read the start card and tell me the current state."
Claude responds with: article count, Bible entry count, tool count, last SHA, top 3 priorities, relevant never rules for today's work.
Read MPW-NEVER-RULES.md every session — non-negotiable.
If anything is wrong, correct before proceeding.
