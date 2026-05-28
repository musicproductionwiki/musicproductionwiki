# MPW SESSION START CARD
*Last updated: May 28, 2026 — Session 79*

---

## CURRENT STATE
| Item | Value |
|------|-------|
| Articles live | 526 |
| Bible entries live | 223+ |
| Tools live | 41 |
| Last commit SHA | `23e74048` — S79: Tool session plan, flagship writer blueprint, all handoffs updated |
| Model string | `claude-sonnet-4-6` |
| Proxy URL | `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy` |
| GitHub token | `[GITHUB_TOKEN — regenerate at github.com/settings/tokens if expired]` |
| Local path | `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\` |
| Site | `musicproductionwiki.com` |
| Repo | `github.com/musicproductionwiki/musicproductionwiki` |

---

## TOP 3 PRIORITIES
1. **Session 80 — Tool Hub Redesign + Build** — Hub three-zone redesign, Loudness Penalty Calculator, session prompt files for all parallel tool builds. Full spec in `MPW-TOOL-SESSION-PLAN.md`.
2. **Affiliate applications** — Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox — REVENUE BLOCKER
3. **GSC indexing requests** — all 42 tools + reverb + compression

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
| Never upload any file to GitHub without scanning for raw tokens first | S69 |
| Never hardcode tool counts — use dynamic JS | S77 |
| Never use HTML `<table>` for Bible genre settings table — use CSS grid with mobile card layout | S78 |
| Never structure share bar buttons inline with label — label on own row, buttons in `.mpw-share-btns` full-width row below | S78 |
| Never commit a Bible flagship entry without auditing all share bar placements against reverb.html | S78 |
| Never build a Bible tool without an embed code block below the share bar | S78 |
| Never gate the tool itself — gate the download/export output only | S79 |
| Never build a tool without its monetization hook (email gate on download) coded from day one | S79 |
| Never build a parallel session tool without a complete self-contained session prompt file | S79 |
| Never commit a tool page without updating /tools/index.html hub card in same Trees API commit | S79 |
| Never reference TruClarify in ClearCheck architecture — ClearCheck is fully independent | S79 |
| Never target Pass 2 prose at 4,800 words — correct target is 12,000–14,000 words | S79 |
| Never run Pass 2 as a single API call — split into Pass 2A (foundation) and Pass 2B (evidence) | S79 |
| Never generate track lists in any Pass — use flagship_tracks.json (6 locked tracks per slug) | S79 |
| Never generate genre table numbers — use flagship_genre_data.json | S79 |
| Never generate producer signal chains — use flagship_producer_dna.json | S79 |
| Never run flagship writer before all 9 curation files are complete | S79 |

---

## COMPRESSION.HTML — GOLD STANDARD (LOCKED S78)

**URL:** `musicproductionwiki.com/bible/compression`
**Last SHA:** `9de422e2` | **Size:** ~288KB | **Version:** v1.2

**Also gold standard:** `bible/reverb.html` — prose depth and content architecture.
Both must be studied before writing any new flagship entry.

---

## KEY NEW DOCUMENTS — SESSION 79

| Document | Purpose |
|---|---|
| `MPW-TOOL-SESSION-PLAN.md` | Complete tool hub strategy, all 12 destination tool specs, parallel build architecture, Session 80 scope |
| `MPW-FLAGSHIP-WRITER-BLUEPRINT.md` | Complete Bible writer spec, all 40 pre-approved insights, 4-pass architecture, 3-gate system |

---

## 40 FLAGSHIP ENTRIES — STATUS

**Wave 1:** compression ✅ LIVE | eq | gain-staging | reverb ✅ LIVE | delay | limiting | saturation | sidechain-compression | lufs | mastering

**Wave 2:** parallel-compression | bus-compression | stereo-imaging | mid-side-processing | automation | high-pass-filter | parametric-eq | multiband-compression | noise-gate | dynamic-range | headroom | subtractive-synthesis | lfo | adsr | mix-translation

**Wave 3:** transient-shaping | fm-synthesis | wavetable-synthesis | oscillator | true-peak-limiting | loudness-normalization | send-return | harmonic-distortion | resonance | sidechain-ducking | modulation | chorus | low-pass-filter | arrangement | reference-mixing

---

## PENDING OWNER ACTIONS
| Action | Priority | Notes |
|--------|----------|-------|
| Affiliate applications | P0 REVENUE BLOCKER | Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox |
| GSC indexing requests | P0 | All 42 tools + reverb + compression |
| Replace quotes.json with quotes_merged_v2.json | P1 | Save to mpw-scripts\ |
| Save mpw_bible_writer_06.py to mpw-scripts\ | P1 | Updated writer |
| Add 1 resonance quote + fix 4 zero-coverage gaps | P1 | sidechain-compression, mix-translation, sidechain-ducking, reference-mixing |
| ClearCheck attorney listing fee pricing decision | P2 | US only, listing fee model |
| Google Workspace domain dispute | P3 | Case #70817574 |

---

## SESSION START RITUAL
Steve says: "Read the start card and tell me the current state."
Claude responds with: article count, tool count, last SHA, top 3 priorities, relevant never rules for today's work.
If anything is wrong, correct before proceeding.

## LAST SESSION HANDOVER NOTE
Session 79: Full planning and architecture session. Two master documents created and committed:

- **`MPW-TOOL-SESSION-PLAN.md`** — Complete tool hub strategy. One hub (`/tools/`), three-zone architecture, all 12 destination tool specs fully detailed, parallel build system (Groups A/B/C/D, simultaneous sessions), Session 80 scope locked (hub redesign + Loudness Penalty + session prompt files for all tools), ClearCheck updated to attorney listing fee model (US only, no TruClarify dependency).
- **`MPW-FLAGSHIP-WRITER-BLUEPRINT.md`** — Complete Bible writer master spec. 4-pass architecture (Pass 1 + Pass 1.5 + Pass 2A + Pass 2B + Pass 3). Word count corrected: Pass 2 target 12,000–14,000 words (not 4,800). Gate 3 assembled minimum 15,000 words. All 40 pre-approved central insights locked. 9 curation files documented. 3-gate quality system with per-section word floors. API cost ~$0.40–0.50/entry, ~$16–20 for all 40.

All 5 handoff files updated and committed. SHA log and session start updated.

**Session 80 opens with:** Read start card → Read `MPW-TOOL-SESSION-PLAN.md` → Read `MPW-TOOL-BUILD-SPEC.md` → Fetch live `/tools/index.html` and `/tools/frequency-conflict-detector.html` → Build hub redesign → Build Loudness Penalty Calculator → Write all session prompt files → Commit all.
