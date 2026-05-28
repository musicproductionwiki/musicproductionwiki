# MPW SESSION START CARD
*Last updated: May 27, 2026 — Session 78*

---

## CURRENT STATE
| Item | Value |
|------|-------|
| Articles live | 526 |
| Bible entries live | 223+ |
| Tools live | 41 |
| Last commit SHA | `9de422e2` — S78: compression.html share bars, genre table CSS grid, mpw-share-btns global |
| Model string | `claude-sonnet-4-6` |
| Proxy URL | `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy` |
| GitHub token | `[GITHUB_TOKEN — regenerate at github.com/settings/tokens if expired]` |
| Local path | `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\` |
| Site | `musicproductionwiki.com` |
| Repo | `github.com/musicproductionwiki/musicproductionwiki` |

---

## TOP 3 PRIORITIES
1. **Build `mpw_flagship_writer.py` — P0** — Automated Tier 1 flagship entry writer. 3-pass architecture: Pass 1 (discovery JSON ~2K tokens), Pass 2 (prose only ~8K tokens), Pass 3 (Python assembly — no API call). Target: 40 flagship entries published in one week via parallel sessions (4 sessions × 10 entries). Full spec in BIBLE and SCRIPTS handoffs. Build and test on 3 entries before full run.
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

---

## COMPRESSION.HTML — GOLD STANDARD (LOCKED S78)

**URL:** `musicproductionwiki.com/bible/compression`
**File:** `bible/compression.html`
**Last SHA:** `9de422e2`
**Version:** v1.2 (May 27, 2026)
**Size:** ~278KB

**Structure (25 sections):**
definition → how-it-works → new-producers → parameters → quick-reference → tools (GR Calculator) → signal-chain → fix-it → history → how-to-use → genre-table → topology → hardware-plugin → before-after → in-the-wild → producer-dna → signatures → types → verdict → plugin-recs → mistakes → mix-translation → flags → progression → faq → related

**SEO — confirmed perfect:**
- canonical: `https://musicproductionwiki.com/bible/compression`
- 5 JSON-LD schema blocks: Article, FAQPage, BreadcrumbList, HowTo, Speakable
- OG/Twitter: all 6 required tags present
- Title: `Compression: Complete Guide to Ratio, Attack, Release & Gain Reduction | The Producer's Bible`

**Share bars (8 strategic locations):**
1. After New Producers — "Share with a producer who needs this"
2. After Quick Reference table — "Share"
3. After GR Calculator tool — "Share this tool" + **embed code snippet**
4. After Genre table — "Share"
5. After In The Wild/comparison showcase — "Share this breakdown"
6. After Verdict — "Share the verdict / Copy Verdict"
7. Sidebar — "Share This Entry" (stacked column)
8. Footer — X and Reddit

**Share bar CSS pattern (mandatory for all flagship entries):**
```css
.mpw-share-bar { display:flex; flex-direction:column; gap:8px; margin-top:14px; padding-top:14px; border-top:1px solid #2a2a4a; }
.mpw-share-label { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#666; display:block; }
.mpw-share-btns { display:flex; gap:6px; width:100%; }
.mpw-share-btn { flex:1; height:36px; ... }
.share-x { background:#000; color:#fff!important; }
.share-reddit { background:#ff4500; color:#fff; }
.share-copy { background:#f5a623; color:#000; }
```

**Fix-It accordion:** 8 symptoms, result drops directly under selected symptom, no page jump
**Entry nav:** IntersectionObserver + scrollIntoView({inline:'center'}) for active pill auto-centering
**Citation block:** APA, MLA, Chicago, Harvard — one-click copy — Institutional Licensing footer
**Version changelog:** amber dot timeline — v1.0 and v1.2
**What to Read Next:** 6 learning path cards
**Embed code:** iframe snippet with one-click copy in "Embed This Tool" block
**Genre table:** CSS grid — desktop 6-column, mobile card layout (no HTML table)
**Producer quotes:** 3 formal blocks (Dave Pensado, Bob Katz, Tchad Blake) + 3 DNA quotes (Dre, CLA, Tchad)

---

## 40 FLAGSHIP ENTRIES — STATUS

Steve is hand-writing all 40. compression.html is entry #1, LIVE.

**Wave 1 — Universal 10 (write first):**
compression ✅ LIVE | eq | gain-staging | reverb ✅ LIVE | delay | limiting | saturation | sidechain-compression | lufs | mastering

**Wave 2 — Intermediate 15:**
parallel-compression | bus-compression | stereo-imaging | mid-side-processing | automation | high-pass-filter | parametric-eq | multiband-compression | noise-gate | dynamic-range | headroom | subtractive-synthesis | lfo | adsr | mix-translation

**Wave 3 — Advanced 15:**
transient-shaping | fm-synthesis | wavetable-synthesis | oscillator | true-peak-limiting | loudness-normalization | send-return | harmonic-distortion | resonance | sidechain-ducking | modulation | chorus | low-pass-filter | arrangement | reference-mixing

**Writing standard:** Phenomenal prose, philosophical depth, three-level reader:
1. Mid-session fix — producer has a problem right now, needs the answer immediately
2. Deep learning — understands the full picture, wants the theory
3. Institutional licensing — Berklee, Full Sail, Icon Collective reading for curriculum

---

## PENDING OWNER ACTIONS
| Action | Priority | Notes |
|--------|----------|-------|
| Affiliate applications | P0 REVENUE BLOCKER | Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox |
| GSC indexing requests | P0 | All 42 tools + reverb + compression |
| Replace quotes.json with quotes_merged_v2.json | P1 | Save to mpw-scripts\ |
| Save mpw_bible_writer_06.py to mpw-scripts\ | P1 | Updated writer |
| Add 1 more resonance quote to quotes file | P1 | |
| Google Workspace domain dispute | P3 | Case #70817574 |

---

## SESSION START RITUAL
Steve says: "Read the start card and tell me the current state."
Claude responds with: article count, tool count, last SHA, top 3 priorities, relevant never rules for today's work.
If anything is wrong, correct before proceeding.

## LAST SESSION HANDOVER NOTE
Session 78: compression.html flagship build complete (SHA `9de422e2`). All handoffs updated. Session 78b (this session): flagship writer architecture designed. Key decisions locked:

- **Writer name:** `mpw_flagship_writer.py`
- **Architecture:** 3-pass — Pass 1 discovery JSON, Pass 2 prose only, Pass 3 Python assembly
- **Quality gate:** Pass 1 must find the non-obvious central insight per term before Pass 2 runs. Generic insight = abort and retry.
- **Parallel execution:** 4 sessions × 10 entries = 40 flagships in one run
- **Tools:** Writer uses existing mpw_tools_v3.py for tool injection. Tool suite expansion is a separate parallel track — build after flagships are live.
- **Uniqueness mechanism:** The central insight drives every section. EQ is spatial, not corrective. Limiting is decision-making, not safety. Each term has a real insight that the obvious angle misses.
- **Full spec:** BIBLE handoff Section "FLAGSHIP WRITER SPEC" + SCRIPTS handoff Section "mpw_flagship_writer.py Build Brief"

Next session opens with: read BIBLE flagship writer spec → read SCRIPTS build brief → build the writer → test on eq, gain-staging, delay → run all 40.
