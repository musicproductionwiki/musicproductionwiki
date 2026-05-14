# MPW — Content Standards & Batch Pipeline
*Fetch via: `python mpw_session_start.py --fetch content`*

---

# 10. Article Standards — LOCKED

| Category | Floor | Target | Ceiling |
| --- | --- | --- | --- |
| Review | 2,800w | 3,150w | 3,500w |
| Comparison | 3,900w | 4,300w | 5,000w |
| Technique | 5,400w | 6,500w | 7,700w |
| Roundup | 4,700w | 5,500w | 6,500w |
| Music Business | 3,200w | 3,550w | 4,000w |
| Wiki/Reference | 4,200w | 4,500w | 5,000w |
| AI Music | 4,200w | 4,800w | 5,800w |
| Breakdown | 3,500w | 4,000w | 4,500w |
| Studio Story | 4,000w | 4,800w | 5,500w |
| Recreation | 3,800w | 4,200w | 5,000w |
| Vocal Autopsy | 3,800w | 4,200w | 5,000w |
| Budget Recreation | 2,800w | 3,000w | 3,200w |
| Bible — anchor tier (top 50) | 2,800w | 3,000w | 3,200w |
| Bible — standard | 1,000w | 1,100w | 1,200w |
| Bible — short-form | 600w | 700w | 800w |

Read time calculated at 325 wpm.

---

# Writing Rules — NON-NEGOTIABLE

- **Dates:** Always "May 2026" — NEVER "May 2025"
- **Canonical tags:** Always `/articles/filename.html` format — no trailing slash
- **Asset paths:** `../css/` and `../js/` (articles live in /articles/ subdirectory)
- **Affiliate links:** Use `href=#affiliate` as placeholder until approvals confirmed
- **Categories:** Always confirm [CATEGORY] line in mpw_writer.py output matches expected
- **Duplicate check:** Always check MPW-HANDOFF-ARTICLES.md before proposing topics
- **Zip size:** Keep under 200KB — Cloudflare intercepts larger downloads
- **Batch workflow:** All articles written first, then one commit via mpw_commit_articles.py

---

# Content Pillars (9)

1. **Wiki/Reference** — authoritative definitions and technique guides
2. **Reviews** — honest gear, plugin, DAW reviews with scores
3. **Comparisons** — head-to-head with decision framework
4. **Techniques/Tutorials** — how-to production guides
5. **Trending/News** — industry developments
6. **AI Music** — AI tools, workflows, generators
7. **Producer Profiles** — artist case studies
8. **Music Business** — licensing, distribution, contracts, royalties
9. **History/Context** — genre origin stories, equipment history

---

# Category Definitions

**Review** — Hardware or software product with star/score rating. Must extract existing score on rewrites — NEVER change a score between runs.
**Comparison** — Two or more products head-to-head. Includes decision framework and verdict.
**Technique** — How-to guide for a specific production method. Exercises section (Beginner/Intermediate/Advanced) required.
**Roundup** — Best-of list with 5-10 items. ItemList schema required.
**Music Business** — Licensing, distribution, contracts, royalties, rights. TruClarify cross-link where relevant.
**Wiki/Reference** — Authoritative definition + how it works + examples. Evergreen content.
**AI Music** — AI tools, AI workflows, AI-generated music. Fast-changing — verify current info.
**Breakdown** — Beat or track breakdown. Instrument-by-instrument production analysis.
**Studio Story** — Narrative account of how a hit record was made. Deep historical detail.
**Recreation** — How to recreate a specific sound or track section. Step-by-step technical.
**Vocal Autopsy** — Analysis of a vocalist's technique on a specific track.
**Budget Recreation** — How to recreate expensive sounds with budget gear/plugins.

---

# 5. Content Batch Pipeline — Full Roadmap

## Completed Batches

| Batch | Content | Status |
| --- | --- | --- |
| 01-07 | Original rewrites + early new articles — 406 articles | LIVE |
| 08 | DAWs, interfaces, mics, headphones, monitors, synths, plugins, techniques, music-business — 120 articles | LIVE — May 10, 2026 |

## Queued Batches

| Batch | Articles | Status / Dependencies |
| --- | --- | --- |
| 09 — breakdown | 100 | breakdowns.html LIVE ✅ — mpw_writer.py v3.0 READY ✅ — GO |
| 10 — studio-story | 50 | After Batch 09 committed |
| 11 — recreation | 60 | recreations.html must exist first |
| 12 — vocal-autopsy | 35 | vocal-autopsies.html must exist first |
| 13 — budget-recreation | 60 | After Batch 11 committed |
| 14 — Bible | 200 first → 1,500 total | Batch B (20) = P0. Batch C (179) after B confirmed. |

---

# Audience Ownership & Revenue Strategy

**Newsletter:** The Producer's Briefing — Beehiiv — "Sound better by Friday" CTA — LIVE
**Lead magnet:** MPW Cheat Sheet Pack — NEEDS TO BE BUILT — P2
**Affiliate programs:** Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — ALL PENDING EMAIL — HIGH PRIORITY REVENUE BLOCKER
**Cross-promotion:** TruClarify — every music business article should funnel there — underutilized
**Institutional licensing:** "The Producer's Bible contains over 2 million words" — pitch to schools, platforms

**Acquisition stack (priority order):** Newsletter + lead magnet → YouTube → Free tool → Reddit → Discord → TikTok → Backlinks

---

# Gold Standard Article Structure — Required Elements

Every article must contain ALL of these (verified by mpw_full_audit.py):
1. `class="quick-answer"` — quick answer box
2. `class="faq-accordion"` — FAQ section with FAQPage JSON-LD schema
3. `class="article-layout"` — grid wrapper
4. `class="article-body"` — body div
5. `id="main-content"` — main content anchor
6. `class="site-footer"` — footer
7. Canonical tag: `/articles/filename.html` (no trailing slash)
8. OG tags: og:title, og:description, og:image
9. robots meta: `max-snippet:-1, max-image-preview:large, max-video-preview:-1`
10. At least one inline SVG diagram
11. BreadcrumbList JSON-LD schema
12. Article JSON-LD schema
13. Nav fingerprint: `mpw-nav-v4-final-r7`
14. Date: "May 2026" — never 2025
15. Word count above floor for category
