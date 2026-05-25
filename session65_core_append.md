---

# SESSION 65 UPDATE — CORE — May 24, 2026

## Confirmed State at Session Start
- Articles: **526** live
- Bible entries: **223** live
- Tool pages: **36** live (`/tools/[slug].html`)
- Tools hub: **LIVE** at `musicproductionwiki.com/tools/`

---

## Session 65 — What Was Completed

### P0 — 526 Article Pages — Nav Batch ✅ COMPLETE

All 526 article pages patched in one Trees API commit. Four changes applied simultaneously:

**Change 1 — Desktop nav: Tools → added**
- `Tools →` li inserted before Bible li in all 526 articles
- Uses `.nav-tools-link` class (already defined in `mpw-nav-homepage-v1` style block on every article — no CSS changes needed)

**Change 2 — Mobile drawer: grid style replacing vertical list**
- Old `mobile-drawer` vertical list replaced with new grid-style drawer
- Inline styles used for grid items (not bmn-drawer-cat class) — article pages lack bmn-drawer CSS, inline avoids adding new CSS to 526 files
- Tools teal pill at top, Bible amber pill second

**Change 3 — replaceState → pushState/popstate back-button fix**
- Mobile drawer open now calls `history.pushState({drawerOpen:true})` to add a fake history entry
- `window.addEventListener('popstate')` catches the back button press and closes the drawer instead of navigating away
- This is the correct fix for article pages — `replaceState` (used on category pages) was wrong here and was confirmed not working

**Change 4 — CSS specificity fix: nav-bible-link and nav-tools-link**
- Old selectors: `.nav-bible-link{color:#f5a623}` and `.nav-bible-link:hover` — beaten by `nav.mpw-site-nav .nav-item>a` child combinator
- New selectors: `nav.mpw-site-nav .nav-item>a.nav-bible-link{...}` and `nav.mpw-site-nav .nav-item>a.nav-tools-link{...}`
- Tools link confirmed teal, Bible link confirmed amber on all article pages

**Commit history:**
| SHA | Change |
|-----|--------|
| `613a5f4d` | Test article (ableton-live-12-review) — first pass (Tools li + grid drawer) |
| `ece7bcf4` | Test article — replaceState JS fix attempt (confirmed not working) |
| `8087205e` | Test article — CSS specificity fix + replaceState |
| `f6979227` | Test article — pushState/popstate fix (confirmed working) |
| `c308817a` | **Full 525 articles — all 4 changes — one Trees API commit — one Netlify deploy** |

**Dry-run approach used (reference for future batches):**
1. Fetched 3 diverse live articles — confirmed exact target strings match (smart quote U+2019, arrow U+2192)
2. Confirmed exact mobile drawer HTML including `\u00a0` non-breaking space after bullet in `mob-bible` link
3. Ran Python dry-run — all 3 confirmed all 4 replacements valid before any commit
4. Committed 1 test article — verified visually (Tools teal ✅, Bible amber ✅, grid drawer ✅)
5. Discovered back button issue — debugged and fixed pushState/popstate approach
6. Discovered CSS specificity issue — fixed nav-item>a.classname selectors
7. Re-confirmed test article had all 4 fixes working
8. Committed remaining 525 via Trees API — spot-checked 3 after

---

## Strategic Session — 98 Tools Master Spec

This session included a full strategic review of the tools roadmap. Two complete rounds of 20 viral tool concepts were developed and researched, then integrated with the existing 64-tool spec to produce the final prioritized master spec.

**File delivered:** `mpw_tools_master_spec.md`
- Saved to Steve's project files
- 98 tools total (6 original tools cut, 40 new tools added)
- Priority-ranked 1–98 with editorial rationale
- Category: 6 cuts documented with reasons

**Six tools cut from original 64:**
- Send/Return FX Architecture — reference chart, not a tool
- Clip Gain vs Fader Reference — static signal flow, no calculation
- True Peak vs Sample Peak Reference — answer never changes
- Dither Type Selector — answer is almost always the same
- Dynamic EQ vs Multiband — recommendation logic too binary
- Intro Length Optimizer — output is a single number, low stickiness

**New tools added (highlights):**
- Priority 1 (viral) tools: "Why Does My Mix Sound Amateur" Diagnostic, Should I Sample This Decision Tree, Spotify Skip Probability Map, Comparison Trap Calculator, Sound Like Reverse Engineer, 808 Relationship Analyzer, Track Finisher, Drum Tuning Reference, Streaming Income Reality Check, J Dilla Drunk Beat Decoder, Is This Plagiarism Checker, Why Is My Vocal Sitting Wrong Fixer, Loudness War Visualizer, Chord Progression Emotion Mapper, Beat Selling Price Calculator
- Priority 2 tools: Frequency Masking Visualizer, Headphone Compensation Reference, and 18 others
- Human/psychology category added: Track Finisher, Comparison Trap Calculator, Producer Style DNA Mapper, Artist Development Readiness Score, Track Energy Arc Grader

**Paywall strategy confirmed:**
- Free forever: all session-critical calculation tools
- Email gate: tools that generate exportable documents (Royalty Split Calculator, Collaboration Agreement Builder, Release Readiness Scorer, Should I Sample This detailed report)
- Never paywall: business/legal tools that feed TruClarify leads — free access, email-gate the detailed output only

---

## Updated Priority Queue — Session 66 Onwards

| Priority | Task | Status |
|----------|------|--------|
| **P0** | **Build `mpw_tools_v6_writer.py`** — batch Python writer for 98 new tools — same architecture as Bible writer — two-pass JSON spec then HTML/JS generation | NEXT SESSION — CRITICAL |
| **P1** | **Update `mpw_writer.py`** — new grid-style mobile drawer must be in writer so all future articles get correct drawer automatically | BLOCKS FUTURE ARTICLES |
| **P2** | **Update `mpw_bible_writer.py`** — read time 500→650 wpm + new Bible mobile drawer categories + slim-bar Tools → + all 11 bible-bar categories | BLOCKS BIBLE BATCH |
| **P3** | **Bible entry pages (222)** — bmn-drawer replacement (Production, Recording, Tools missing from category grid) — requires exact dry-run approach from Session 65 | PENDING |
| **P4** | **Bible Tier 1 remaining 33 entries** — blocked on P2 | BLOCKED |
| **P5 (Steve)** | **Affiliate applications** — Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox | **REVENUE BLOCKER** |
| P6 | GSC: Request Indexing for /bible/reverb + /bible/chorus + /tools/ | Steve action |
| P7 | Sitemap: add /tools/ + all 36 /tools/[slug].html — priority 0.9/0.8 | After tools confirmed indexed |
| P8 | Tools hub UX review at 50+ tools — collapsible category accordion or category landing pages | Flag when approaching 50 |

---

## Tools Writer Architecture — Confirmed Plan

When building `mpw_tools_v6_writer.py`, the architecture is:

**Pass 1 (JSON spec):** Generates structured data per tool — inputs, canvas type, preset values, warning thresholds, genre data arrays, plugin tier recommendations, famous settings — as a validated JSON object.

**Pass 2 (HTML/JS):** Generates full self-contained HTML/JS from the validated spec. Canvas drawing code, createElement chains, click-to-copy chips, genre selector logic — all generated from the spec, not improvised.

**Key constraints:**
- No innerHTML anywhere — all canvas and DOM manipulation via createElement/appendChild (Netlify CSP on /tools/ pages)
- Canvas: CSS width:100%;height:Xpx — no inline width/height attributes
- Plugin tier cards: Free/Mid/Pro/Key insight tiers from mpw_affiliates.py registry
- Famous presets: named presets with specific parameter values and the engineering rationale behind each
- Live warning logic: red/amber/green states on outputs — not just numbers
- Genre intelligence: every tool knows genre-appropriate defaults
- SC constant: `SC = '</' + 'script>'` — never literal `</script>` in Python strings
- ThreadPoolExecutor — 8 workers — 98 tools in roughly 2–3 hours

**Quality standard:** Tool #98 must be as good as tool #1. The frozen template in Python sets the quality ceiling — the model improvises nothing structural.

---

## NEVER Rules Added — Session 65 — Core

| Rule | Detail |
|------|--------|
| NEVER use `replaceState` to fix back-button on article pages | `replaceState` is correct for category pages (Netlify redirect creates double history entry). Article pages need `pushState`+`popstate` — the drawer open adds a fake history entry that the back button consumes to close the drawer instead of navigating away |
| NEVER use class-only selector for nav color overrides on mpw-nav-homepage-v1 pages | `nav.mpw-site-nav .nav-item>a` child combinator with `!important` beats any class-only selector regardless of `!important`. Always use `nav.mpw-site-nav .nav-item>a.classname` pattern |
| NEVER build mpw_tools_v6_writer.py without reading mpw_tools_master_spec.md first | The spec is the frozen input — 98 tools, priority-ranked, with unique differentiators and paywall assignments documented |
| NEVER run article nav batches by fetching one article and assuming all match | The `\u00a0` non-breaking space after the bullet in `mob-bible` was only discovered by printing the exact repr() of the live file — always confirm exact bytes |
| NEVER commit the full batch before the test article has all issues resolved | Session 65 iterated 4 times on the test article before the full batch ran — this is correct procedure, not inefficiency |
| NEVER paywall session-critical calculation tools | Free forever. Email gate is for exportable documents only. Never on calculators. |

