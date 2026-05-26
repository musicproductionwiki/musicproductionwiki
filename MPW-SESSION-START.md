# MPW SESSION START CARD
*Last updated: May 26, 2026 — Session 73*

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
1. Session 75: Build MPW-NEVER-RULES.md — canonical never rules document (NEXT)
2. Execute mpw_writer.py 4 pending updates — blocks next article batch
3. Execute mpw_bible_writer.py updates (650wpm + nav + v5.3) — blocks next T1 Bible batch

---

## NEVER RULES — HARD (zero exceptions, enforced by mpw_precommit_check.py)

| Rule | Added |
|------|-------|
| Never embed Python in HTML/JS — write JS as pure `cat > file.js << 'JSEOF'` heredoc, run `node --check` before embedding | S67 |
| Never load `style.css` or `../css/style.css` in tool pages — causes 600px black radial blob shapes | S68 |
| Never use `.hero` or `.container` class names in tool pages — conflicts with global CSS pseudo-elements | S68 |
| Never commit without running `mpw_precommit_check.py` first | S68 |
| Never invent slugs — verify against GitHub tree API before writing any links | S65 |
| Never enable Netlify Pretty URLs — breaks the site | S65 |
| Never truncate handoff documents | S65 |
| Never touch existing CSS style blocks — append only, new `<style>` block before `</head>` | S65 |
| Never use assistant prefill in API calls — returns empty response body | S67 |
| Never call Netlify functions via custom domain — always use `classy-haupia-be8e43.netlify.app` | S67 |
| Never use model `claude-sonnet-4-5` or `claude-sonnet-4-20250514` — correct model is `claude-sonnet-4-6` | S68 |
| Never extract nav block with naive find() — use div-depth tracking to guarantee balance | S68 |
| Never start tool rebuild without reading MPW-TOOL-BUILD-SPEC.md first | S68 |
| Never insert HTML cards without verifying position is INSIDE the target div | S67 |
| Never upload any file to GitHub without scanning for raw tokens first | S69 |
| Never use class-only nav selectors on mpw-nav-homepage-v1 pages | S65 |
| Never load style.css on tool pages — use main.js only | S68 |
| Never create AudioContext before a user gesture in Browser Apps | S65b |
| Never call direct api.anthropic.com from tool pages — always use Netlify proxy | S67 |
| Never use `innerHTML` in any tool JS — Netlify CSP blocks it | S57/58 |
| Never commit a tool without all 5 files in same Trees API commit | S67 |
| Never run `mpw_bible_writer.py` before updating read time to 650 wpm | S63 |
| Never run `mpw_writer.py` before applying all 4 pending nav/drawer updates | S63 |
| Never present files for approval and then commit without waiting — present ALL files, wait for explicit go | S71 |

---

## PENDING OWNER ACTIONS
| Action | Priority | Notes |
|--------|----------|-------|
| Submit sitemap to GSC | P0 | 780 URLs (36 tool URLs added S71) |
| Update MPW-HANDOFF-BIBLE.md in Claude project | P0 | Replace with S73 merged version |
| Update MPW-SESSION-START.md in Claude project | P0 | Replace with S74 version (this file) |
| Update MPW-HANDOFF-MERGE-PLAN.md in Claude project | P0 | Mark BIBLE ✅ |
| Update SESSION-START in Claude project | P0 | This file |
| Request indexing — /bible/reverb | P1 | GSC URL Inspection |
| Request indexing — suno-prompt-optimizer | P1 | GSC URL Inspection |
| Request indexing — ai-music-rights-navigator | P1 | GSC URL Inspection |
| OG images for both AI tools | P1 | 1200×630px |
| Affiliate applications | P2 REVENUE BLOCKER | Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox |
| Google Workspace domain dispute | P3 | Case #70817574 still open |

---

## LAST SESSION HANDOVER NOTE
Session 73 completed BIBLE merge. No session appends targeted this file — merge was a GitHub audit + corrections pass. Bible entry count corrected to 223 (GitHub confirmed — S61 claimed 231, S72 start card said 225, both wrong). Gold standard reference updated to reverb.html v1.6. S61 entry count corrected in file. S73 audit section appended. Merge cycle (S69–S73) is now COMPLETE. Post-merge rules take effect S74+: no more append files, masters updated directly each session. Next: Session 75 — build MPW-NEVER-RULES.md (canonical never rules file, 7th master doc). Sources: CORE, TECH, SCRIPTS, BIBLE, SESSION-START, CONTINUITY-MASTER-PLAN + chat history search for any rules discussed but never documented. After that: mpw_writer.py 4 pending updates, mpw_bible_writer.py v5.3 build.

---

## SESSION START RITUAL
Steve says: "Read the start card and tell me the current state."
Claude responds with: article count, Bible entry count, tool count, last SHA, top 3 priorities, relevant never rules for today's work.
If anything is wrong, correct before proceeding.
