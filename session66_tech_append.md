---

# SESSION 66 UPDATE — TECH — May 25, 2026

## MPW-TOOL-BUILD-SPEC.md — The Frozen Tool Template

This is the most important technical deliverable of Session 66. Every parallel session
building tools loads this document first. It contains the frozen visual system, component
library, and quality checklist that ensures all 25 tools look and function identically.

### Frozen CSS Variables (copy verbatim into every tool)

```css
:root {
  --bg:        #0d0d1a;
  --bg2:       #111120;
  --bg3:       #16162a;
  --bg4:       #1c1c32;
  --border:    rgba(255,255,255,0.07);
  --border2:   rgba(255,255,255,0.12);
  --border3:   rgba(255,255,255,0.18);
  --amber:     #f5a623;
  --amber2:    rgba(245,166,35,0.12);
  --amber3:    rgba(245,166,35,0.06);
  --teal:      #00e8a2;
  --teal2:     rgba(0,232,162,0.1);
  --red:       #ff3d5a;
  --green:     #00e8a2;
  --text:      #f0f0f4;
  --text2:     #a0a0b8;
  --text3:     #5a5a7a;
  --mono:      'DM Mono', monospace;
  --sans:      'DM Sans', sans-serif;
}
```

### Frozen Font Import (copy verbatim into every tool <head>)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Frozen Tool Header Component (the branded card — required on every tool)

This is the MPW-branded header that appears at the top of every tool's interactive section.
Matches the Frequency Conflict Detector gold standard exactly.

```html
<div class="tool-header-card">
  <div class="tool-header-brand">
    <div class="tool-logo-mark">
      <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
        <rect x="1.5" y="7" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
        <rect x="6" y="4" width="2.5" height="12" rx="1.2" fill="#0a0a0b"/>
        <rect x="10.5" y="1" width="2.5" height="16" rx="1.2" fill="#0a0a0b"/>
        <rect x="15" y="5" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
      </svg>
    </div>
    <div class="tool-brand-text">
      <div class="tool-brand-name">MusicProductionWiki.com</div>
      <div class="tool-brand-sub">◆ The Producer's Bible</div>
    </div>
  </div>
  <div class="tool-header-right">
    <span class="tool-badge">INTERACTIVE TOOL</span>
    <a href="/tools/[RELATED-TOOL]" class="tool-related-link">[Related Tool Name]</a>
  </div>
</div>
```

### Frozen Tool Header CSS

```css
.tool-header-card {
  background: var(--bg2);
  border: 1px solid var(--border2);
  border-radius: 12px;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 12px;
}
.tool-header-brand { display: flex; align-items: center; gap: 12px; }
.tool-logo-mark {
  width: 32px; height: 32px; border-radius: 8px;
  background: var(--teal); display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.tool-brand-name { font-size: 14px; font-weight: 600; color: var(--text); }
.tool-brand-sub { font-size: 11px; color: var(--amber); font-family: var(--mono); }
.tool-header-right { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
.tool-badge {
  font-size: 10px; font-family: var(--mono); font-weight: 700;
  color: var(--amber); border: 1px solid rgba(245,166,35,0.4);
  border-radius: 4px; padding: 4px 10px; letter-spacing: 0.1em;
}
.tool-related-link {
  font-size: 13px; color: var(--text2); text-decoration: none;
  transition: color 0.15s;
}
.tool-related-link:hover { color: var(--teal); }
```

### Frozen Section Card Component

```html
<div class="tool-section">
  <div class="tool-section-label">SECTION TITLE</div>
  <!-- content -->
</div>
```

```css
.tool-section {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 16px;
}
.tool-section-label {
  font-size: 9px; font-family: var(--mono); font-weight: 700;
  color: var(--amber); letter-spacing: 0.18em;
  text-transform: uppercase; margin-bottom: 16px;
}
```

### Frozen Insight Callout (amber left-border — use for key outputs)

```html
<div class="tool-insight">
  <p id="insightText">Output appears here.</p>
</div>
```

```css
.tool-insight {
  border-left: 3px solid var(--amber);
  background: var(--amber3);
  border-radius: 0 8px 8px 0;
  padding: 14px 16px;
  font-size: 14px;
  color: var(--text);
  line-height: 1.6;
  margin-top: 16px;
}
```

### Frozen Slider Component

```html
<div class="tool-field">
  <label class="tool-label">LABEL</label>
  <div class="tool-slider-row">
    <input type="range" class="tool-slider" id="mySlider" min="0" max="100" value="50">
    <span class="tool-slider-val" id="myVal">50</span>
  </div>
</div>
```

```css
.tool-field { margin-bottom: 16px; }
.tool-label {
  font-size: 9px; font-family: var(--mono); color: var(--text3);
  letter-spacing: 0.12em; text-transform: uppercase; display: block; margin-bottom: 8px;
}
.tool-slider-row { display: flex; align-items: center; gap: 12px; }
.tool-slider {
  flex: 1; -webkit-appearance: none; appearance: none;
  height: 4px; background: var(--border2); outline: none;
  border-radius: 2px; cursor: pointer;
}
.tool-slider::-webkit-slider-thumb {
  -webkit-appearance: none; width: 16px; height: 16px;
  border-radius: 50%; background: var(--amber); cursor: pointer;
  box-shadow: 0 0 6px rgba(245,166,35,0.4);
}
.tool-slider-val {
  font-size: 13px; font-family: var(--mono); color: var(--amber);
  min-width: 36px; text-align: right; font-weight: 600;
}
```

### Frozen Select/Dropdown Component

```html
<div class="tool-field">
  <label class="tool-label">LABEL</label>
  <select class="tool-select" id="mySelect">
    <option value="a">Option A</option>
    <option value="b">Option B</option>
  </select>
</div>
```

```css
.tool-select {
  width: 100%; background: var(--bg3); border: 1px solid var(--border2);
  color: var(--text); font-family: var(--sans); font-size: 14px;
  padding: 10px 14px; border-radius: 8px; cursor: pointer; outline: none;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%235a5a7a' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
}
```

### Frozen Primary Button

```html
<button class="tool-btn" id="calcBtn">Calculate →</button>
```

```css
.tool-btn {
  background: linear-gradient(135deg, var(--amber), #e08000);
  color: #000; font-family: var(--sans); font-size: 14px; font-weight: 700;
  border: none; cursor: pointer; border-radius: 8px;
  padding: 12px 28px; letter-spacing: -0.01em;
  transition: transform 0.12s, box-shadow 0.12s;
  box-shadow: 0 0 20px rgba(245,166,35,0.25);
}
.tool-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 0 30px rgba(245,166,35,0.4);
}
```

### Frozen Click-to-Copy Chip

```html
<span class="copy-chip" onclick="copyVal(this, 'VALUE')">VALUE <span class="copy-icon">⊕</span></span>
```

```css
.copy-chip {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--bg3); border: 1px solid var(--border2);
  border-radius: 6px; padding: 6px 12px;
  font-family: var(--mono); font-size: 13px; font-weight: 600;
  color: var(--amber); cursor: pointer; transition: all 0.12s;
}
.copy-chip:hover { border-color: var(--amber); background: var(--amber2); }
.copy-chip.copied { background: rgba(0,232,162,0.1); border-color: var(--teal); color: var(--teal); }
.copy-icon { font-size: 11px; opacity: 0.6; }
```

```javascript
function copyVal(el, val) {
  navigator.clipboard.writeText(val).then(function() {
    el.classList.add('copied');
    var orig = el.innerHTML;
    el.innerHTML = 'Copied! ✓';
    setTimeout(function() { el.classList.remove('copied'); el.innerHTML = orig; }, 1500);
  });
}
```

### Frozen Canvas Container

```html
<canvas id="myCanvas" style="width:100%;height:240px;border-radius:8px;background:var(--bg3);display:block;"></canvas>
```

Note: Always set width/height via CSS, not HTML attributes. Set canvas.width and canvas.height
via JavaScript after checking offsetWidth/offsetHeight to handle high-DPI displays.

---

## Tool Page Structure — Required Elements Checklist

Every tool page MUST include all of the following before committing:

### Head Section
- [ ] `<meta charset="UTF-8">`
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- [ ] `<title>` — tool name + MPW brand + keyword
- [ ] `<meta name="description">` — 150–160 chars, keyword-rich
- [ ] `<link rel="canonical" href="https://www.musicproductionwiki.com/tools/[slug].html">`
- [ ] OG tags: og:title, og:description, og:url, og:type="website"
- [ ] Twitter card tags
- [ ] GA4 script (G-79VB543KCT)
- [ ] DM Sans + DM Mono font import
- [ ] `<link rel="stylesheet" href="../css/style.css">`
- [ ] FAQPage JSON-LD schema (minimum 3 FAQ pairs)
- [ ] BreadcrumbList JSON-LD schema
- [ ] WebPage JSON-LD schema

### Body — Required
- [ ] Full MPW site nav (mpw-nav-homepage-v1 style block + nav HTML)
- [ ] Nav CSS specificity fix: `nav.mpw-site-nav .nav-item>a.nav-bible-link` + `nav.mpw-site-nav .nav-item>a.nav-tools-link`
- [ ] Mobile drawer: grid style with Tools teal pill + Bible amber pill
- [ ] pushState/popstate back-button fix in drawer JS
- [ ] Tool title (H1) + description paragraph
- [ ] Tool header branded card (MPW logo + Interactive Tool badge)
- [ ] Interactive tool body
- [ ] Related tools section (link to 3 relevant other tools)
- [ ] Footer with copyright + links to /tools/, /bible/, newsletter
- [ ] `<script src="../js/main.js"></script>` at end of body

### Commit Checklist
- [ ] File committed to `/tools/[slug].html` via GitHub API
- [ ] Tool card added to `/tools/index.html` in the same commit
- [ ] Sitemap updated (or flagged for batch update)
- [ ] Steve visually confirms on live site before next tool

---

## Nav HTML — Required on Every Tool Page

The complete nav HTML and style block is documented in session65_tech_append.md.
The CSS specificity pattern is:

```css
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-bible-link:hover{background:rgba(245,166,35,.1)!important;color:#f5a623!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link{color:#00e8a2!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link:hover{background:rgba(0,232,162,.08)!important;color:#00e8a2!important}
```

**NEVER use class-only selectors for nav color overrides.** The child combinator pattern
`nav.mpw-site-nav .nav-item>a.classname` is required. This burned us twice (Session 63/64
and Session 65). It is now permanently documented.

---

## Tool Card HTML — Required for /tools/index.html Update

Every tool commit must add this card to `/tools/index.html` in the correct category section:

```html
<a class="tool-card" href="/tools/[slug].html" data-cat="[category]" data-name="[searchable name]">
  <div class="tool-card-body">
    <span class="tool-card-name">[Tool Name]</span>
    <span class="tool-card-desc">[One-sentence description. 12 words max.]</span>
    <span class="tool-card-cat">[Category Name]</span>
  </div>
  <span class="tool-card-arrow">→</span>
</a>
```

Category data-cat values for the 25 tools:
- AI Music tools: `data-cat="ai-music"`
- Mix/vocal tools: `data-cat="mixing"`
- Beat/drum tools: `data-cat="beat-making"`
- Business tools: `data-cat="business"`
- Frequency tools: `data-cat="frequency"`
- Music theory tools: `data-cat="arrangement"`

A new "AI Music" category pill must be added to the filter bar in `/tools/index.html`:
```html
<button class="tools-cat-btn" data-cat="ai-music">AI Music</button>
```

---

## Anthropic API — Tool Integration Pattern

For tools that use the Claude API (AI Music tools, mix diagnostics, vocal fixer):

```javascript
async function callClaude(userMessage, systemPrompt) {
  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system: systemPrompt,
        messages: [{role: 'user', content: userMessage}]
      })
    });
    const data = await response.json();
    return data.content[0].text;
  } catch (err) {
    return 'Unable to connect. Please try again.';
  }
}
```

**ALWAYS:**
- Show a loading state while Claude is thinking
- Handle errors gracefully (never show raw error to user)
- Keep system prompts focused and specific — they define the quality ceiling
- System prompts are frozen in the tool, not generated dynamically

---

## File Structure Update — Session 66

```
tools/
├── index.html               ← hub — updated with each new tool card + AI Music pill
├── browser-daw.html         ← v3 LIVE — SHA 2a0e05c2
├── [36 existing tools]      ← all live
├── suno-prompt-optimizer.html    ← PENDING
├── ai-music-rights-navigator.html ← PENDING
├── ai-music-ddex-checker.html    ← PENDING
├── ai-copyright-strength.html    ← PENDING
├── suno-credits-calculator.html  ← PENDING
├── ai-music-income-calculator.html ← PENDING
├── ai-music-platform-comparison.html ← PENDING
├── ai-lyrics-optimizer.html      ← PENDING
├── ai-music-distribution-roadmap.html ← PENDING
├── ai-music-niche-finder.html    ← PENDING
├── ai-vs-human-monetization.html ← PENDING
├── suno-vs-human-quiz.html       ← PENDING
├── ai-hybrid-workflow-builder.html ← PENDING
├── ai-genre-accuracy-tester.html ← PENDING
├── mix-sounds-amateur-diagnostic.html ← PENDING
├── vocal-sitting-wrong-fixer.html ← PENDING
├── 808-relationship-analyzer.html ← PENDING
├── drum-tuning-reference.html    ← PENDING
├── spotify-skip-probability-map.html ← PENDING
├── streaming-income-reality-check.html ← PENDING
├── frequency-masking-visualizer.html ← PENDING
├── tap-tempo-pro.html            ← PENDING
├── beat-selling-price-calculator.html ← PENDING
├── chord-progression-emotion-mapper.html ← PENDING
└── ai-playlist-placement-scorer.html ← PENDING
```

---

## NEVER Rules Added — Session 66 — Tech

| Rule | Detail |
|------|--------|
| NEVER use class-only nav selectors | Child combinator required: `nav.mpw-site-nav .nav-item>a.classname` — documented 3 times now |
| NEVER build a tool page without the frozen CSS variables block | Copy the exact block from MPW-TOOL-BUILD-SPEC.md — do not re-derive colors |
| NEVER set canvas width/height via HTML attributes | Use CSS width/height and set canvas.width/canvas.height via JS after offsetWidth check |
| NEVER commit a tool without adding its card to /tools/index.html | Same Trees API commit — never two separate deploys for one tool |
| NEVER launch AI Music tools without verifying current platform terms | Suno, Udio, DDEX terms change frequently — verify before publishing rights guidance |
| NEVER add new category pill to tools hub without at least one tool in that category live | Add the AI Music pill in the same commit as the first AI music tool |

