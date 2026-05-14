# MPW — Producer's Bible Reference
*Fetch via: `python mpw_session_start.py --fetch bible`*
*ALWAYS read this file before any Bible session. Full strategic plan: MPW-PRODUCERS-BIBLE.md*

---

# 11. The Producer's Bible — Strategic Overview

**Goal:** 1,500 entries — the most comprehensive music production reference on the internet.
**Current:** 2 entries live (EQ + Compression) — both fully resolved Session 26 ✅
**Next:** Batch B (20 entries) — Signal Processing cluster — batch14-B.txt ready — P0
**Pitch:** "The Producer's Bible contains over 2 million words of authoritative music production reference content" — unanswerable competitive claim for institutional licensing.

---

# Bible Architecture

| Key | Value |
| --- | --- |
| URL structure | `/bible/[term]` — LOCKED Session 9 |
| Index page | `/bible/index.html` — LIVE — commit 29ee26a9 ✅ |
| Bible search | Fuse.js against /bible-index.json |
| bible-index.json | LIVE — 1 entry (EQ) — grows with each batch |
| 301 redirect needed | /dictionary/* → /bible/:splat 301 — add to netlify.toml |
| Schema | DefinedTerm + DefinedTermSet primary schema |
| Accent color | Amber throughout — category badge, edition marker, track borders, active nav state |

---

# 3B. Gold Standard Entry — LOCKED

**File:** `bible/eq.html`
**Canonical URL:** `https://musicproductionwiki.com/bible/eq`
**Status:** LIVE — layout AND mobile BOTH fixed Session 26 ✅
**NEVER TOUCH — it is the template for all new entries.**

Why EQ replaced compression as template:
- Full Tier 1 features: YouTube embed, Spotify embeds, interactive calculator (frequency chart), audio toggle shell
- Full visual components: param cards, SVG diagram, track example cards, type grid, DAW notes, mistake list
- Full SEO: SpeakableSpecification, wordCount, timeRequired, datePublished
- Uses mpw-nav-homepage-v1 nav with logo-mark SVG — identical to live site nav

**bible/compression.html:** LIVE — commit e387c341 — LOCKED — DO NOT use as template.

---

# Bible Word Count Spec

| Tier | Count | Floor | Target | Ceiling |
| --- | --- | --- | --- | --- |
| Anchor terms (top 50 by search vol.) | 50 | 2,800w | 3,000w | 3,200w |
| Standard terms | ~1,350 | 1,000w | 1,100w | 1,200w |
| Short-form terms (slang, abbreviations) | ~100 | 600w | 700w | 800w |

**Total Bible word count at launch (estimated):** 1.8–2.1 million words.

---

# Bible Entry Template — 15 Required Sections

Every entry must contain all 15:
1. Emotional hook pull quote (amber left border, italic)
2. Quick Answer (1-2 paragraphs, under 40 words, snippet-engineered)
3. Full definition (producer-voice, not academic, 3-4 paragraphs)
4. How It Works (with SVG diagram — role="img", aria-labelledby, title element)
5. Parameters (individual param cards where applicable)
6. Quick Reference Card (settings table — Copy Table button required)
7. History & Origin
8. How Producers Use It (DAW-specific notes: Ableton, FL, Logic, Pro Tools, Reaper)
9. In The Wild (3-5 real track examples with timestamps)
10. Types (where applicable — VCA/FET/Optical/Variable-Mu, etc.)
11. Common Mistakes (6 items, red ✕ icon list)
12. Related Terms (9-10 cross-links to /bible/[term])
13. Producers Also Look Up (4 adjacent term cards)
14. Further Reading (7 links to MPW technique articles)
15. FAQ (8 questions — full FAQPage schema)

---

# mpw_bible_writer.py v2.0

**Location:** `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_bible_writer.py`
**Layout bug:** RESOLVED Session 26 ✅ — READY FOR BATCH B

| Setting | Value |
| --- | --- |
| Model | claude-sonnet-4-6 |
| Workers | 8 (ThreadPoolExecutor) |
| PASS1_TOKENS | 20,000 (required — lower truncates JSON) |
| Generation time | 4-5 minutes per entry (not 45 seconds) |
| Cost | ~$25 for 200 entries (~$0.15/entry) |
| Env var | ANTHROPIC_API_KEY — also reads ANTHROPIC_KEY as fallback |

```
python mpw_bible_writer.py --test --slug eq --term "EQ" --category "Frequency"
python mpw_bible_writer.py --batch-file Bible-Batches/batch14-B.txt --start-date 2026-05-12
python mpw_bible_writer.py --batch-file Bible-Batches/batch14-C.txt
python mpw_bible_writer.py --dry-run --batch-file Bible-Batches/batch14-B.txt
```

---

# Bible Batch Files

| File | Entries | Status |
| --- | --- | --- |
| Bible-Batches/batch14-B.txt | 20 entries | READY — Signal Processing cluster — P0 |
| Bible-Batches/batch14-C.txt | 179 entries | READY — After Batch B confirmed |

**Batch B backdating:** `--start-date 2026-05-12`
**NEVER set datePublished before May 6, 2026** — site launched May 6-7, 2026.

---

# 3C. Bible Batch Staggering Strategy

Stagger in batches of 200 every 2-3 weeks:
- **Batch A (first 200):** Highest search volume terms across all categories — rank fastest
- **Batch B (next 300):** Complete Signal Processing category — topical authority compounds
- **Batch C onward:** First 200 indexed and ranking by now — trust established

Total sitemap build-out: 6-8 weeks. 1,500 indexed pages vs. 1,500 pages in Google sandbox.

---

# 34H. Copy Table Feature

Every Quick Reference Card includes a "Copy Table" button. Copies table content as formatted plain text with source attribution:
```
COMPRESSION QUICK REFERENCE — MusicProductionWiki.com / The Producer's Bible
Parameter | General | Drums | Vocals | Bass | Mix Bus
...
Source: musicproductionwiki.com/bible/compression
```
At 1,500 entries with 1,500 copy buttons — passive link seeding at scale. Compounds over time.

---

# Bible Session Rules

| Rule | Detail |
| --- | --- |
| Read this file before any Bible session | Strategic foundation — never skip |
| NEVER start writing before gold standard approved | bible/eq.html is approved and LIVE |
| NEVER load main.js on Bible pages | Conflicts silently with Bible nav JS |
| ALWAYS run --test on one entry first | Never run batch before test passes |
| ALWAYS run --dry-run first | Confirm entry list and categories |
| Batch B is P0 | Run before anything else Bible-related |
| Copy Table button required | Every Quick Reference Card needs it |
| NEVER delete existing glossary articles without 301 redirects | Every glossary URL must redirect to its Bible equivalent |
| 2026 Edition marker required | In header and footer of every entry |

---

# Bible Quality Control at Scale

**Before batch runs:**
- First 10 entries reviewed manually before batch continues
- One entry per category reviewed before that category's batch runs
- "In The Wild" sections spot-checked for accuracy (real tracks, real timestamps)

**After batch runs:**
- Word count: no entry under floor or over ceiling for its tier
- Cross-link validation: all /bible/[term] links resolve
- Schema: DefinedTerm schema present on every entry
- Amber accent color: category badge, edition marker confirmed

**Ongoing:**
- Monthly spot-check of 20 random entries for accuracy
- Community feedback mechanism — producers can flag errors
