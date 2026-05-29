# MPW SESSION START CARD
Last updated: May 29, 2026 — Session 80
Next session: 81

---

## CURRENT STATE

| Item | Value |
|------|-------|
| Articles live | **526** |
| Bible entries live | **223** |
| Tools live | **43** |
| Last commit SHA | `1c9fa54` — Hub pills bar position:sticky attempt (pills STILL BROKEN) |
| Model | `claude-sonnet-4-6` |
| Proxy | `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy` |
| GitHub token | stored in `setenv.ps1` — regenerate at github.com/settings/tokens if expired |
| Scripts dir | `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\` |

---

## TOP 3 PRIORITIES — SESSION 81

1. **Fix hub sticky subcategory pills** — FETCH LIVE FILE FIRST. Read every CSS block. Trace every ancestor of `.tools-sticky-bar`. Find the overflow rule. Fix surgically. Do not write a single line until root cause is confirmed.
2. **Fix hub mobile search bar overflow** — same protocol. Fetch, grep competing rules, override correctly.
3. **Affiliate applications** — Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox — REVENUE BLOCKER.

---

## TOP 20 NEVER RULES

| # | Rule |
|---|------|
| 1 | **NEVER GUESS OR ASSUME. ALWAYS FETCH THE LIVE FILE AND READ IT BEFORE TOUCHING ANYTHING.** Every broken S80 deployment happened from writing code without reading what was live. |
| 2 | Never commit multiple files individually — always Trees API, one commit, all files together. |
| 3 | Never commit without running `mpw_precommit_check.py` first. |
| 4 | Never present files for commit without Steve's explicit approval — present, stop, wait. |
| 5 | Never load `style.css` or `../css/style.css` in tool pages — causes 600px black blob shapes. |
| 6 | Never inject the full site `mpw-site-nav` HTML without also injecting its full inline CSS block (extracted from `attack-release-calculator.html` block 2). |
| 7 | Never touch nav on any tool page without first fetching `attack-release-calculator.html` and reading it. |
| 8 | Never use `position:sticky` without first confirming NO ancestor has `overflow` set. |
| 9 | Never apply CSS fixes without checking specificity of all competing rules first. |
| 10 | Never use `overflow-x:hidden` on `body` when any descendant uses `position:sticky` — use `overflow-x:clip` on `html` instead. |
| 11 | Never embed Python in HTML/JS — write JS as pure heredoc, run `node --check` before embedding. |
| 12 | Never use `innerHTML` in tool JS — Netlify CSP blocks it on `/tools/*`. Use `createElement`/`appendChild`. |
| 13 | Never use `.hero` or `.container` class names in tool pages — conflict with global `style.css`. |
| 14 | Never invent slugs — verify against GitHub Trees API before writing any links. |
| 15 | Never truncate handoff documents — always complete, never summarize. |
| 16 | Never enable Netlify Pretty URLs — breaks the site. |
| 17 | Never use any model except `claude-sonnet-4-6`. |
| 18 | Never call Netlify functions via custom domain — always `classy-haupia-be8e43.netlify.app`. |
| 19 | Never put Loudness Penalty in the flagship section — too thin, needs full revamp first. |
| 20 | Never gate Mix Fingerprint timeline analysis before 20,000 visitors/month. |

---

## WHAT IS BROKEN — DO NOT IGNORE

| Item | Status | Fix Approach |
|------|--------|-------------|
| Hub: subcategory pills not sticky | ❌ | Fetch live, trace ancestry, find overflow conflict |
| Hub: mobile search bar overflows right | ❌ | Fetch live, grep competing CSS, override with !important |
| MFP: timeline flags only show last 40s | ❌ | Fetch live MFP JS, find slice/sort bug in flag display |

## WHAT IS WORKING — DO NOT BREAK

| Item | Status |
|------|--------|
| Hub: original hero — "Built for the session." | ✅ |
| Hub: mpw-site-nav sticky | ✅ |
| Hub: 10 category pills filter + search | ✅ |
| Hub: 43 tool cards in grid | ✅ |
| Hub: flagship section — MFP first, FCD, 4 coming soon | ✅ |
| MFP: full Web Audio analysis + D3 radar | ✅ |
| MFP: glassmorphism design | ✅ |
| MFP: written diagnosis, playback predictions, timeline | ✅ |
| MFP: full site nav | ✅ |
| Loudness Penalty: live in grid | ✅ |

---

## PENDING OWNER ACTIONS

- Replace `quotes.json` with `quotes_merged_v2.json` (save to `mpw-scripts\`)
- Save `mpw_bible_writer_06.py` to `mpw-scripts\`
- Affiliate applications (Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox)
- GSC indexing requests — all 43 tools + reverb + compression
- Google Workspace domain dispute Case #70817574
- ClearCheck attorney listing fee pricing decision (US only)

---

## LAST SESSION HANDOVER NOTE — S80

Built Mix Fingerprint Analyzer (destination tool — Web Audio, D3, glassmorphism, written diagnosis, timeline, playback predictions) and Loudness Penalty Calculator (thin — needs revamp). Hub redesigned with flagship section and original hero restored. Nav is sticky. Multiple failed attempts to make subcategory pills sticky — root cause is an overflow conflict somewhere in the ancestor chain that was never fully isolated because code was written before reading the live file. S81 must fix this properly: fetch live, read everything, confirm root cause, then patch.
