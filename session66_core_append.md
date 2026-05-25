---

# SESSION 66 UPDATE — CORE — May 25, 2026

## Confirmed State at Session Start
- Articles: **526** live
- Bible entries: **223** live
- Tool pages: **36** live (`/tools/[slug].html`)
- Tools hub: **LIVE** at `musicproductionwiki.com/tools/`
- Browser DAW: **LIVE** at `/tools/browser-daw.html` (v3 — audio engine fixed)
- GSC: 1,270 impressions / 1 click / avg position 25.2 (under 1 month old)

---

## Session 66 — Strategic Decisions Made

### Tool Building Strategy — Confirmed

After a full competitive research session covering BandLab, Soundtrap, Amped Studio,
Stemulator, LALAL.AI, Moises, and the AI music market, the following was confirmed:

**P0 for next sessions: Build 25 quality tools in parallel sessions**

Steve will run multiple Claude conversations simultaneously (Max plan — $200/month).
All sessions pull from a single frozen spec document (`MPW-TOOL-BUILD-SPEC.md`) so
output is visually and functionally consistent regardless of which session builds which tool.

### The 25 Priority Tools — Final Selection

These 25 tools are the confirmed build queue. Ordered by traffic opportunity, build speed,
and zero infrastructure cost. All 25 are pure Claude API or pure JS — no RunPod, no backend.

**TIER 1 — AI Music / Suno (build first — lowest competition, fastest ranking):**
1. Suno Prompt Optimizer — `/tools/suno-prompt-optimizer`
2. AI Music Commercial Rights Navigator — `/tools/ai-music-rights-navigator`
3. AI Music DDEX Disclosure Checker — `/tools/ai-music-ddex-checker`
4. AI Track Copyright Strength Calculator — `/tools/ai-copyright-strength`
5. Suno Credits Calculator — `/tools/suno-credits-calculator`
6. AI Music Income Calculator — `/tools/ai-music-income-calculator`
7. AI Platform Comparison Tool — `/tools/ai-music-platform-comparison`
8. AI Lyrics Optimizer for Suno — `/tools/ai-lyrics-optimizer`
9. AI Music Distribution Roadmap — `/tools/ai-music-distribution-roadmap`
10. AI Music Niche Finder — `/tools/ai-music-niche-finder`
11. AI vs Human Monetization Comparison — `/tools/ai-vs-human-monetization`
12. Suno vs Human Quiz — `/tools/suno-vs-human-quiz`
13. AI + Human Hybrid Workflow Builder — `/tools/ai-hybrid-workflow-builder`
14. AI Music Genre Accuracy Tester — `/tools/ai-genre-accuracy-tester`

**TIER 2 — Production Viral (high search volume, broad audience):**
15. "Why Does My Mix Sound Amateur?" Diagnostic — `/tools/mix-sounds-amateur-diagnostic`
16. "Why Is My Vocal Sitting Wrong?" Fixer — `/tools/vocal-sitting-wrong-fixer`
17. 808 Relationship Analyzer — `/tools/808-relationship-analyzer`
18. Drum Tuning Reference — `/tools/drum-tuning-reference`
19. Spotify Skip Probability Map — `/tools/spotify-skip-probability-map`
20. Streaming Income Reality Check — `/tools/streaming-income-reality-check`
21. Frequency Masking Visualizer — `/tools/frequency-masking-visualizer`
22. BPM Tap Tempo Pro — `/tools/tap-tempo-pro`
23. Beat Selling Price Calculator — `/tools/beat-selling-price-calculator`
24. Chord Progression Emotion Mapper — `/tools/chord-progression-emotion-mapper`
25. AI Music Playlist Placement Scorer — `/tools/ai-playlist-placement-scorer`

### Why These 25 — Strategic Rationale

**AI Music tools rank fast:** "Suno prompt optimizer," "AI music DDEX disclosure,"
"can I sell Suno music" — thousands of monthly searches, near-zero tool-based competition.
A new site can rank page 1 for these queries in weeks, not months.

**No infrastructure required:** All 25 are pure Anthropic API or pure JS. Zero RunPod,
zero backend, zero additional hosting cost. Deploy to Netlify exactly like existing tools.

**Production tools capture existing search volume:** The Tier 2 tools target queries
that have been searched millions of times — "why does my mix sound bad," "how to tune 808"
— but have no interactive tool-based answers. MPW fills that gap.

**Browser DAW deferred from this batch:** The Browser DAW is a 2–3 session dedicated build.
It does not belong in a 25-tool parallel batch. Build it in a dedicated session after these
25 are live and driving traffic.

### Parallel Session Architecture — Confirmed

Steve runs multiple simultaneous Claude conversations on the Max plan. Each session:
1. Loads `MPW-TOOL-BUILD-SPEC.md` from GitHub at session start
2. Builds 2–3 tools from the assigned batch
3. Commits each tool directly to GitHub via GitHub API
4. Updates `/tools/index.html` in the same commit (add tool card)
5. Steve reviews each tool visually before approving next build

**Session assignment:**
- Session A: AI Music tools #1–7 (Suno/rights/income/platform)
- Session B: AI Music tools #8–14 (lyrics/distribution/quiz/workflow/genre)
- Session C: Production tools #15–21 (mix diagnostic/vocal/808/drum/skip/income/frequency)
- Session D: Production tools #22–25 + catch-up (tap tempo/beat selling/chord/AI playlist)

### Quality Standard — The Frequency Conflict Detector Standard

Every new tool must match or exceed the quality of the live Frequency Conflict Detector
at `musicproductionwiki.com/tools/frequency-conflict-detector`.

That tool demonstrates the correct MPW visual language:
- Dark `#0d0d1a` background
- Amber `#f5a623` primary accent
- Teal `#00e8a2` secondary accent
- DM Sans font family
- Branded header card with teal logo mark, site name, "Interactive Tool" badge
- Section cards with subtle borders `rgba(255,255,255,0.07)`
- Canvas visualizations with proper MPW styling
- Amber left-border on insight callouts

The `MPW-TOOL-BUILD-SPEC.md` freezes the exact CSS and HTML components so every
parallel session produces visually consistent output without re-designing.

### GSC / Traffic Assessment — May 25, 2026

Steve showed GSC data: 1,270 impressions, 1 click, avg position 25.2 over 3 months.
Site is under 1 month old. This is normal and expected.

**Assessment:** The impression spike in the last 3 days indicates Google is crawling at
volume. Position 25.2 means some pages are on page 2-3 — one authority signal or backlink
push could move several to page 1. The 25 tools being built now will rank faster than
articles because tool-specific queries (especially AI Music) have near-zero competition.

**Steve action items from GSC review:**
- Submit sitemap including all 36 tool pages + `/tools/browser-daw.html`
- Request indexing on top 20 articles individually in GSC
- Request indexing on `/tools/` hub and `/tools/browser-daw.html`
- Apply for affiliate programs (Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox)
  — this is a REVENUE BLOCKER and has been pending for multiple sessions

### Stem Splitter / RunPod Products — Future Queue

Extensive research was done on stem separation, RunPod infrastructure, and premium products.
These are confirmed for the future roadmap but NOT built now. Revenue from the 25 tools
and affiliate programs funds the infrastructure investment.

**Confirmed future products (after traffic and revenue established):**
- MPW Stem Splitter (ensemble HTDemucs + BS-RoFormer, RunPod, $7.99/$12.99)
- MPW AI Beat Generator (AudioCraft on RunPod)
- MPW Vocal Cleaner (DeepFilterNet3 on RunPod)

**Pricing confirmed for future Stem Splitter:**
- Free: 2 separations/day, MP3, 4-stem, no analysis
- Standard $7.99/mo: Unlimited, WAV, 10-stem, basic analysis, blend mode, BPM/key detection
- Premium $12.99/mo: 18-stem, Stem Repair, MIDI export, fingerprint analysis, sample pack gen

**Competitive moats confirmed:**
- Proprietary fine-tuning dataset from community stems
- Producer's Bible integration on every stem type
- Community stems library (network effects — year 2 product)
- Genre-calibrated quality score
- Reverse reconstruction from degraded sources

### TruClarify — Status

TruClarify is a future business concept — not a current focus. Steve confirmed he is not
actively developing TruClarify right now. It is a "trusted middleman network" business
model that requires relationship-building before it can generate revenue. The AI music
legal tools in the 25-tool batch serve the same audience but as free reference tools,
not as a business. TruClarify remains on the long-term roadmap.

### Browser DAW — Current State

Browser DAW v3 is LIVE at `/tools/browser-daw.html`. SHA `2a0e05c2`. Audio engine works.
The visual redesign work done in Session 65 revealed that competing with Amped Studio
requires a multi-session dedicated build. The Browser DAW is deferred to a dedicated
session after the 25 tools are live. The v3 version stays live as-is.

---

## Updated Priority Queue — Session 67 Onwards

| Priority | Task | Status |
|----------|------|--------|
| **P0** | **Build 25 quality tools — parallel sessions** | NEXT — dedicated sessions |
| **P0a** | **Build `MPW-TOOL-BUILD-SPEC.md`** — frozen design + component spec | Session 66 deliverable |
| **P1** | **Update `mpw_writer.py`** — new grid drawer, Tools nav, CSS fix, pushState | BLOCKS ARTICLE BATCHES |
| **P2** | **Update `mpw_bible_writer.py`** — 650 wpm read time + nav rewrite | BLOCKS BIBLE BATCHES |
| **P3** | **Bible nav fix** — 222 Bible entry pages bmn-drawer replacement | PENDING |
| **P4** | **Bible Tier 1 remaining 33 entries** — blocked on P2 | BLOCKED |
| **P5 (Steve)** | **Affiliate applications** — Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox | **REVENUE BLOCKER** |
| **P6 (Steve)** | **GSC: Submit sitemap + request indexing** | SEO priority |

---

## NEVER Rules Added — Session 66

| Rule | Detail |
|------|--------|
| NEVER build the Browser DAW as part of a multi-tool batch session | It requires 2–3 dedicated sessions — mixing it with tool batches kills quality on both |
| NEVER build a tool without loading MPW-TOOL-BUILD-SPEC.md first | The frozen spec is what keeps parallel sessions visually consistent |
| NEVER commit a tool without adding its card to /tools/index.html in the same commit | Orphaned tool pages with no hub entry are unfindable from the site |
| NEVER skip the quality checklist before committing any tool | FAQPage schema, canonical, OG tags, MPW nav, mobile responsive, pushState — all required |
| NEVER propose RunPod products until affiliate revenue is confirmed | Infrastructure cost must be funded by existing revenue streams first |
| NEVER underestimate the AI Music / Suno tool opportunity | These queries have near-zero tool competition — rank fast and establish MPW authority |

