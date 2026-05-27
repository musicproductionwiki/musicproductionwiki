# MPW SESSION START CARD
*Last updated: May 27, 2026 — Session 73*

---

## CURRENT STATE
| Item | Value |
|------|-------|
| Articles live | 526 |
| Bible entries live | **234** |
| Tools live | **41** |
| Last commit SHA | `0d30f23b` — Fix tool card names — 21 mismatches corrected to match H1 titles |
| Model string | `claude-sonnet-4-6` |
| Proxy URL | `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy` |
| GitHub token | `[GITHUB_TOKEN — from setenv.ps1, regenerate at github.com/settings/tokens if expired. Expires Aug 2, 2026]` |
| Local path | `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\` |
| Site | `musicproductionwiki.com` |
| Repo | `github.com/musicproductionwiki/musicproductionwiki` |
| Never rules count | 123 (15 SCRIPT-enforced, 108 MANUAL) |

---

## TOP 3 PRIORITIES
1. **Category page canonical www. fix** — 89 category pages still have www. in canonical URLs. Single Trees API commit. Full scope first — fetch all 89, read 3, verify pattern, then execute.
2. **Affiliate applications** — Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox. REVENUE BLOCKER. Owner action only.
3. **Favicon sitewide** — ~851 files. Articles have data URI emoji favicon — replace with /favicon.svg. Use incremental Trees API chunks of 100.

---

## NEVER RULES — TOP 20 (Full canonical list: MPW-NEVER-RULES.md — read every session)

| Rule | Added |
|------|-------|
| **Always fully scope before any batch — fetch live files, read them, spot-check 3 files. No assuming, no guessing.** | S73 |
| Never execute a batch based on audit data from a prior session without re-fetching live first | S73 |
| Never touch existing CSS style blocks — append only, new `<style>` block before `</head>` | S26/S65 |
| Never load `style.css` or `../css/style.css` in tool pages — causes 600px black blob shapes | S68 |
| Never embed Python in HTML/JS — write JS as pure heredoc, node --check first | S67 |
| Never commit without running `mpw_precommit_check.py` first | S68 |
| Never invent slugs — verify against GitHub tree API before writing any links | S65 |
| Never enable Netlify Pretty URLs — breaks the site | S26 |
| Never truncate any handoff document — full reproduction required | S26 |
| Never use any model except `claude-sonnet-4-6` | S68 |
| Never extract nav block with naive find() — use div-depth tracking | S68 |
| Never run a batch without spot-checking 3 live files first | S72 |
| Never assume a batch str.replace() match after multiple prior commits modified the file | S72 |
| Never inject mpw-search-js into a page with its own navMob handler | S72 |
| Never show nav-search-btn on mobile by adding to media query show list — breaks hamburger | S72 |
| Never deploy tool without og:image pointing to a live file | S72/S73 |
| Never deploy tool with www. canonical URL | S72 |
| Never deploy tool without embed mode support (?embed=true) | S72 |
| Never leave tool card header with wrong tool name — must match H1 | S73 |
| Never add og:image meta pointing to a non-existent file | S73 |
| Never hardcode GitHub token — store in setenv.ps1 only | S26 |
| 2+ files = Trees API always — one commit = one deploy | S39 |

---

## TOOL STATE — ALL GREEN (End of S73)

All 41 tools now have:
- ✅ Correct MPW nav + mobile eyeglass + hamburger + wireMobSearch
- ✅ og:image pointing to live og-image.png
- ✅ Non-www canonical URL
- ✅ overflow-x (clip or hidden) on html + body
- ✅ Embed mode (?embed=true)
- ✅ Standardized share row (Copy/X/Reddit, flex nowrap)
- ✅ Standard clean footer (© 2026 · All Tools · Producer's Bible · Newsletter)
- ✅ backToTop arrow hidden
- ✅ Correct tool name in card header matching H1

---

## PENDING OWNER ACTIONS

| Action | Priority | Notes |
|--------|----------|-------|
| Affiliate applications | P0 REVENUE BLOCKER | Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox |
| Submit sitemap to GSC | P1 | After category canonical fix |
| GSC indexing requests — all 41 tools | P1 | Use URL Inspection for each tool |
| Google Workspace domain dispute | P3 | Case #70817574 still open |

---

## SESSION START RITUAL

1. Run `. .\setenv.ps1` in PowerShell (loads GitHub token)
2. State back: article count (526), Bible count (234), tool count (41), last SHA (`0d30f23b`)
3. Load `MPW-NEVER-RULES.md` from GitHub
4. Load `MPW-AUDIT-ACTION-PLAN-S73.md` from GitHub
5. Proceed with P1 — category canonical www. fix

## LAST SESSION HANDOVER NOTE
Session 73 was a full sitewide tool quality audit and fix session. All 41 tools are now fully compliant — correct nav, og:image, canonical, overflow-x, embed mode, share row, footer, no arrow, correct card names. Key lesson: Batch C was a ghost (37 broken iframes expected, 0 found) — always re-audit live before executing. 11 new never rules added. Next session: category page canonical www. fix (89 pages, one Trees API commit) + affiliate applications (owner action).
