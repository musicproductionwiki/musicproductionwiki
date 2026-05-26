# MPW SESSION START CARD
*Last updated: May 26, 2026 — Session 72*

---

## CURRENT STATE
| Item | Value |
|------|-------|
| Articles live | 526 |
| Bible entries live | 225 |
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
1. Session 73: MPW-HANDOFF-BIBLE.md merge (NEXT)
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
| Update MPW-HANDOFF-CONTENT.md in Claude project | P0 | Replace with S72 merged version |
| Update MPW-HANDOFF-ARTICLES.md in Claude project | P0 | Replace with S72 merged version |
| Update MPW-HANDOFF-MERGE-PLAN.md in Claude project | P0 | Mark CONTENT + ARTICLES ✅ |
| Update SESSION-START in Claude project | P0 | This file |
| Request indexing — /bible/reverb | P1 | GSC URL Inspection |
| Request indexing — suno-prompt-optimizer | P1 | GSC URL Inspection |
| Request indexing — ai-music-rights-navigator | P1 | GSC URL Inspection |
| OG images for both AI tools | P1 | 1200×630px |
| Affiliate applications | P2 REVENUE BLOCKER | Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox |
| Google Workspace domain dispute | P3 | Case #70817574 still open |

---

## LAST SESSION HANDOVER NOTE
Session 72 completed CONTENT + ARTICLES merge. MPW-HANDOFF-CONTENT.md and MPW-HANDOFF-ARTICLES.md replaced with merged versions (S72). All appends from S39 through S60 integrated and resolved. Bible entry count corrected to 225 (reverb.html v1.6 + chorus.html v5.2 both confirmed LIVE). Key items: mpw_writer.py 4 pending updates and bible writer updates flagged URGENT as blocks; producer quotes gap (Kevin Parker et al.) flagged P2; Batch 09 through 13 all queued pending writer fixes. Next: Session 73 BIBLE merge (128KB — largest doc).

---

## SESSION START RITUAL
Steve says: "Read the start card and tell me the current state."
Claude responds with: article count, Bible entry count, tool count, last SHA, top 3 priorities, relevant never rules for today's work.
If anything is wrong, correct before proceeding.
