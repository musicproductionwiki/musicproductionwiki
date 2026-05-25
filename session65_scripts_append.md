---

# SESSION 65 UPDATE — SCRIPTS — May 24, 2026

## Session 65 — No New Scripts Delivered

All work this session was direct GitHub API operations from Claude's bash environment (individual PUTs and Trees API commits). No new Python scripts were written for Steve to run locally.

---

## mpw_writer.py — PENDING UPDATE (STILL BLOCKS NEXT ARTICLE BATCH)

The mobile drawer in `mpw_writer.py` currently outputs the old vertical list `mobile-drawer` style. Before the next article batch, the writer must output the new grid-style drawer confirmed and live on all 526 articles in Session 65.

**Target drawer HTML to freeze into writer:** See SESSION 65 UPDATE — TECH — "Mobile Drawer — Confirmed Final HTML" section. That is the exact HTML the writer must output.

**Also required in writer update:**
- Desktop nav must include `Tools →` li before Bible li
- CSS must use `nav.mpw-site-nav .nav-item>a.nav-bible-link` and `nav.mpw-site-nav .nav-item>a.nav-tools-link` specificity pattern (not class-only selectors)
- Drawer JS must use `pushState`+`popstate` pattern (not `replaceState`)

**Do NOT run mpw_writer.py for new article batches until all four items above are updated.**

---

## mpw_bible_writer.py — PENDING UPDATES (STILL BLOCKS NEXT T1 BATCH)

Two pending updates remain from prior sessions — unchanged:

**1. Read time — change 500 wpm → 650 wpm:**
```python
# CURRENT (wrong):
read_time = max(1, round(word_count / 500))

# CORRECT:
read_time = max(1, round(word_count / 650))
```

**2. Nav full rewrite based on reverb.html gold standard** — planned for a future session. Until done, do not run new T1 batches.

---

## mpw_tools_v6_writer.py — NEW — TOP PRIORITY NEXT SESSION

**This is the primary build target for Session 66.**

A batch Python writer for the 98 new tools specified in `mpw_tools_master_spec.md`. Same two-pass architecture as `mpw_bible_writer.py` but optimized for JS-heavy tool output instead of prose.

### Architecture

**Pass 1 — Tool Spec JSON (per tool):**
Prompt generates a structured JSON object containing:
- All input fields with types and default values
- Canvas type and drawing logic specification
- Genre data arrays (genre → recommended values)
- Preset definitions (name, values, engineering rationale)
- Warning threshold logic (what triggers red/amber/green states)
- Plugin tier recommendations (Free/Mid/Pro/Key — references mpw_affiliates.py)
- Famous settings (named producers/tracks, exact parameter values, why those values)
- SEO meta description and FAQ pairs

**Pass 2 — Full HTML/JS (from validated spec):**
Prompt generates self-contained HTML/JS from the Pass 1 JSON. The system prompt freezes the structural template — the model fills the tool-specific content only.

### Quality Constraints (must be in system prompt)
- No `innerHTML` anywhere — Netlify CSP blocks it on `/tools/` pages — use `createElement`/`appendChild` only
- Canvas: `width:100%;height:Xpx` CSS — no inline `width`/`height` attributes on canvas elements
- `SC = '</' + 'script>'` — never literal `</script>` in Python string literals
- All plugin recommendations via `mpw_affiliates.py` — never hardcoded strings
- Live warning logic: red/amber/green states on every output — not just numbers
- Famous presets: specific parameter values + the engineering rationale behind each value

### Key Constants (to be confirmed when building)
- Model: `claude-sonnet-4-6`
- PASS1_TOKENS: 8000 (spec JSON is smaller than Bible prose)
- PASS2_TOKENS: 16000 (tools are JS-heavy but shorter than T1 Bible entries)
- API timeout: 600 seconds
- ThreadPoolExecutor: 8 workers
- Save path: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\tools\`

### Build Order
1. Write `mpw_tools_v6_writer.py` with frozen HTML/JS template
2. Test on Priority 1 tools first (#1–3 from master spec)
3. Visual QA on test tools — confirm canvas, presets, warnings, plugin cards all work
4. Run Priority 1–2 batch (tools #1–35) — 35 tools
5. Commit via Trees API — single deploy
6. Update `/tools/index.html` to add new tool cards (hand-edit or build a manifest updater)

### Input Format (batch file)
```
slug:Tool Name:Category:Priority
mix-sounds-amateur-diagnostic:Why Does My Mix Sound Amateur? Diagnostic:Mixing & Signal Flow:1
should-i-sample-this:Should I Sample This? Decision Tree:Business & Legal:1
spotify-skip-probability-map:Spotify Skip Probability Map:Arrangement & Structure:1
...
```

---

## mpw_tools_master_spec.md — DELIVERED

**Location:** Steve's project files (downloaded this session)
**Content:** 98 tools, priority-ranked 1–98, categories, slugs, unique differentiators, paywall assignments
**Purpose:** Frozen input for `mpw_tools_v6_writer.py` — the writer reads from this spec, it does not improvise

**Paywall assignments:**
- Email gate: Royalty Split Calculator, Collaboration Agreement Builder, Release Readiness Scorer, Should I Sample This detailed report
- Never paywall: calculation tools, session-critical tools, business/legal tools that feed TruClarify leads

---

## Scripts to Build — Session 66

Priority order:

1. **`mpw_tools_v6_writer.py`** — batch tool generator (primary build — see architecture above)
2. **`mpw_writer.py` update** — freeze new drawer HTML + Tools nav + CSS specificity fix + pushState JS into writer
3. **`mpw_bible_writer.py` update** — 650 wpm read time + nav rewrite

---

## NEVER Rules Added — Session 65 — Scripts

| Rule | Detail |
|------|--------|
| NEVER build mpw_tools_v6_writer.py without reading mpw_tools_master_spec.md first | The spec is the frozen input — slugs, priorities, unique differentiators, paywall assignments all documented |
| NEVER use innerHTML in any tool generated by mpw_tools_v6_writer.py | Netlify CSP blocks innerHTML on /tools/ pages — all DOM manipulation must use createElement/appendChild |
| NEVER hardcode plugin names or affiliate links in tool HTML | All plugin recommendations must reference mpw_affiliates.py — one approval, one file update, all tools update |
| NEVER run mpw_writer.py for new article batches before updating drawer HTML | Current writer outputs old vertical list — new grid-style drawer confirmed on all 526 articles must be frozen into writer first |
| NEVER run mpw_bible_writer.py for new T1 entries before updating read time | 500 wpm confirmed wrong — 650 wpm is the standard — must be updated before next batch |

