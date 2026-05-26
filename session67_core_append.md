---

# SESSION 67 UPDATE — CORE — May 25, 2026

## Confirmed State at Session Start
- Articles: **526** live
- Bible entries: **223** live
- Tool pages: **36** live (before this session)
- Tool pages: **38** live (after this session — +2)
- Tools hub: LIVE at `musicproductionwiki.com/tools/`

---

## Session 67 — Tools Built

### Tool #1: Suno Prompt Optimizer ✅ LIVE
- **URL:** https://www.musicproductionwiki.com/tools/suno-prompt-optimizer.html
- **Final commit SHA:** `3672b6d4de5f48437cda48d9c875cacb45496469`
- **Type:** Claude API via Netlify Function proxy
- **Category:** AI Music (`data-cat="ai-music"`)

Features: 5-step tab flow (Genre→Sounds→Mood→Structure→Optimize), animated waveform hero (3 slow layers), drag-and-drop sequencer with touch support, consecutive duplicate blocks allowed, live prompt preview, score gauge 0-10, 4 meter bars, expert analysis streams live, before/after full prompt comparison, next steps, social share (Copy Link/X/Reddit), brand watermark, MPW nav, site footer, embed mode `?embed=1`, full SEO.

Selection limits: Genre max 4, Instruments max 6, Mood max 3, Vocal max 3

### Tool #2: AI Music Rights Navigator ✅ LIVE
- **URL:** https://www.musicproductionwiki.com/tools/ai-music-rights-navigator.html
- **Commit SHA:** `60848615b028233a1020b0b9b8675ba076748ea9`
- **Type:** Claude API via Netlify Function proxy
- **Category:** AI Music (`data-cat="ai-music"`)

Features: Platform selector (Suno/Udio/Stable Audio/AIVA/ElevenLabs/Other), Tier (Free/Pro/Premier), Use case (Streaming/YouTube/Sell/Sync/Content ID/Personal), verdict card YES/RISK/NO with badge, requirements list ✓/✗/⚠, DDEX disclosure section, legal context (Thaler v. Perlmutter, RIAA settlement), 3 action steps, social share, brand watermark, embed mode, full SEO.

---

## Netlify Function Proxy — CRITICAL INFRASTRUCTURE

**File:** `netlify/functions/claude-proxy.js`
**Environment variable:** `ANTHROPIC_API_KEY` — set in Netlify → Project configuration → Environment variables

**CRITICAL — Function URL:**
```
https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy
```
Use this absolute URL. `musicproductionwiki.com/.netlify/functions/*` returns 404. Never use relative paths.

**Model:** `claude-sonnet-4-5` — NOT `claude-sonnet-4-20250514`

---

## All Pages Updated This Session

| Page | What changed |
|------|-------------|
| `tools/suno-prompt-optimizer.html` | Built — Tool #1 |
| `tools/ai-music-rights-navigator.html` | Built — Tool #2 |
| `tools/index.html` | 2 new cards, AI Music pill, count 38 |
| `bible/categories/tools/index.html` | 2 new cards inside catGrid, count 38 |
| `sitemap.xml` | 2 new URLs added (741 total) |
| `search-index.json` | 2 new entries (528 total) |
| `favicon.svg` | Created — MPW waveform bars, teal bg |
| `netlify/functions/claude-proxy.js` | Created — Anthropic API proxy |
| `netlify.toml` | Updated — build command + functions dir |
| `tools/pre-delivery-checklist.html` | Fixed — Python code in JS was breaking tool |

---

## Pending Owner Actions

| Action | Priority | Notes |
|--------|----------|-------|
| Submit sitemap to GSC | P0 | 741 URLs — submit `sitemap.xml` |
| Request indexing — suno-prompt-optimizer | P0 | Use URL Inspection in GSC |
| Request indexing — ai-music-rights-navigator | P0 | Use URL Inspection in GSC |
| OG images | P1 | `/images/suno-prompt-optimizer-og.jpg` and `/images/ai-music-rights-navigator-og.jpg` — 1200×630px |
| Affiliate applications | P2 REVENUE BLOCKER | Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox |
| Google Workspace domain dispute | P3 | Case #70817574 still open |

---

## Priority Queue — Next Session

| # | Tool | Slug | Type |
|---|------|------|------|
| 3 | AI Music DDEX Disclosure Checker | `/tools/ai-music-ddex-checker.html` | Claude API |
| 4 | AI Track Copyright Strength Calculator | `/tools/ai-copyright-strength.html` | Claude API |
| 5 | Suno Credits Calculator | `/tools/suno-credits-calculator.html` | Pure JS |
| 6 | AI Music Income Calculator | `/tools/ai-music-income-calculator.html` | Pure JS |
| 7 | AI Platform Comparison Tool | `/tools/ai-music-platform-comparison.html` | Claude API |

---

## NEVER Rules Added — Session 67

| Rule | Detail |
|------|--------|
| NEVER call Netlify functions via custom domain | Always use `classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy` |
| NEVER use model `claude-sonnet-4-20250514` | Correct model is `claude-sonnet-4-5` |
| NEVER use assistant prefill | Returns empty response body |
| NEVER use `fetch()` inside Netlify Functions | Use Node's native `https.request()` with `Buffer.from()` |
| NEVER omit favicon link tags | `<link rel="icon" type="image/svg+xml" href="/favicon.svg">` in every tool head |
| NEVER insert HTML cards using rfind or string replace without verifying position | Always confirm insertion is INSIDE the target div — verify grid_open < insert_pos < grid_close |
| NEVER embed Python code or Python string concatenation in HTML/JS | This broke pre-delivery-checklist.html — one undetected Python artifact kills the whole tool |
| NEVER skip the full mapping checklist after building a tool | Every tool needs: tools/index.html card, bible/categories/tools card, sitemap.xml URL, search-index.json entry |

