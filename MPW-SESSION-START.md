# MPW SESSION START CARD
*Last updated: May 26, 2026 — Session 69*

---

## CURRENT STATE
| Item | Value |
|------|-------|
| Articles live | 526 |
| Bible entries live | 223 |
| Tools live | 40 |
| Last commit SHA | 4e9bb50a — Session 69 CORE merge complete |
| Model string | `claude-sonnet-4-6` |
| Proxy URL | `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy` |
| GitHub token | `[GITHUB_TOKEN — regenerate at github.com/settings/tokens if expired]` |
| Local path | `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\` |
| Site | `musicproductionwiki.com` |
| Repo | `github.com/musicproductionwiki/musicproductionwiki` |

---

## TOP 3 PRIORITIES
1. Session 70: MPW-HANDOFF-TECH.md merge (NEXT)
2. Suno Prompt Optimizer redesign — dedicated session, read MPW-TOOL-BUILD-SPEC.md first
3. Affiliate applications: Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox

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
| Never use model `claude-sonnet-4-5` — correct model is `claude-sonnet-4-6` | S68 |
| Never extract nav block with naive find() — use div-depth tracking to guarantee balance | S68 |
| Never start tool rebuild without reading MPW-TOOL-BUILD-SPEC.md first | S68 |
| Never insert HTML cards without verifying position is INSIDE the target div | S67 |
| Never upload files to GitHub without scanning for raw tokens first — `grep -rn 'ghp_K'` | S69 |

---

## PENDING OWNER ACTIONS
| Action | Priority | Notes |
|--------|----------|-------|
| Submit sitemap to GSC | P0 | 744 URLs |
| Request indexing — suno-prompt-optimizer | P0 | GSC URL Inspection |
| Request indexing — ai-music-rights-navigator | P0 | GSC URL Inspection |
| OG images for both AI tools | P1 | 1200x630px |
| Affiliate applications | P2 REVENUE BLOCKER | Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox |
| Google Workspace domain dispute | P3 | Case #70817574 still open |

---

## LAST SESSION HANDOVER NOTE
Session 69 completed CORE merge. MPW-HANDOFF-CORE.md replaced with merged version (238KB, live-verified). Tool count corrected 38→40 — 3 tools built in undocumented parallel sessions (ai-music-ddex-checker SHA 206e2a44, ai-copyright-strength SHA 7f113017, suno-credits-calculator SHA 4d827292). 5 core appends deleted from GitHub. Section 7 of CORE flagged for future restructure session. Next: Session 70 TECH merge — load MPW-HANDOFF-TECH.md + all tech appends.

---

## SESSION START RITUAL
Steve says: "Read the start card and tell me the current state."
Claude responds with: article count, tool count, last SHA, top 3 priorities, relevant never rules for today's work.
If anything is wrong, correct before proceeding.
