# MPW SESSION START CARD
*Last updated: May 27, 2026 — Session 74*

---

## CURRENT STATE
| Item | Value |
|------|-------|
| Articles live | 526 |
| Bible entries live | **235** |
| Tools live | **42** |
| Last commit SHA | `59350bd7` — reverb HOW TO USE share bar fix |
| Model string | `claude-sonnet-4-6` |
| Proxy URL | `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy` |
| GitHub token | `[GITHUB_TOKEN — from setenv.ps1, regenerate at github.com/settings/tokens if expired. Expires Aug 2, 2026]` |
| Local path | `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\` |
| Site | `musicproductionwiki.com` |
| Repo | `github.com/musicproductionwiki/musicproductionwiki` |
| Never rules count | 125 (15 SCRIPT-enforced, 110 MANUAL) |

---

## TOP 3 PRIORITIES
1. **Reverb share bars** — remaining inline tool card bars still need fixing (Tempo-Locked calculator bar + any others not yet confirmed). Scope all bars first, one Trees API commit.
2. **Affiliate applications** — Plugin Boutique, Amazon Associates, Lookmasters, Sweetwater, PluginFox. REVENUE BLOCKER. Owner action only.
3. **Bible writer v5.3** — save `mpw_bible_writer_06.py` to `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\`. Then run T1 batch.

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
| Never commit Bible fixes one file at a time — always Trees API, one commit | S74 |
| Never assume a share bar is fixed without auditing ALL share bars in the file first including inline tool card bars | S74 |
| Never hardcode GitHub token — store in setenv.ps1 only | S26 |
| 2+ files = Trees API always — one commit = one deploy | S39 |

---

## TOOL STATE — ALL GREEN (End of S73/S74)

All 42 tools now have:
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
| Save mpw_bible_writer_06.py to mpw-scripts\ | P1 | Delivered this session — save before next Bible batch |
| GSC indexing requests — all 42 tools | P1 | Use URL Inspection for each tool |
| Google Workspace domain dispute | P3 | Case #70817574 still open |

---

## SESSION START RITUAL

1. Run `. .\setenv.ps1` in PowerShell (loads GitHub token)
2. State back: article count (526), Bible count (235), tool count (42), last SHA (`59350bd7`)
3. Load `MPW-NEVER-RULES.md` from GitHub
4. Proceed with P1 — reverb remaining share bars (scope first, Trees API commit)

## LAST SESSION HANDOVER NOTE
Session 74 was a Bible quality pass. reverb.html patched: 11-pill bible bar (Production/Recording/Tools added), og:image fixed, meta desc trimmed, dates updated. mpw_bible_writer_06.py (v5.3) delivered: 650wpm, 11 bible bar pills, correct og:image, ImageObject schema. Interactive Tool badge removed from 66 Bible entries (Group A — inline style badge). 160 total entries audited — 94 use calc-eyebrow architecture (already correct, no fix needed). reverb.html share bars fixed: 4 main mpw-share-bar divs unified + RT60 tool card bar + HOW TO USE bar. Remaining: Tempo-Locked calculator bar needs fixing next session — scope all bars with Trees API commit. Sitemap submitted to GSC (804 pages). Category canonical www. fix confirmed done. Favicon confirmed done.
