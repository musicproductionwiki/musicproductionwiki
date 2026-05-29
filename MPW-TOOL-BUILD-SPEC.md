# MPW-TOOL-BUILD-SPEC.md
## Frozen Tool Build Specification — Session 66 — May 25, 2026
## MusicProductionWiki.com — The Producer's Bible

---

# ⛔ MANDATORY FIRST READ
# Every parallel session building tools must load this document first.
# Do not build a single line of code until you have read and confirmed
# the frozen CSS system, component library, and quality checklist below.
# This document is the source of truth. Your session output must match it.

---

# PART 1 — THE 25 PRIORITY TOOLS

## Build Queue — Confirmed Order

All 25 tools are pure Anthropic API or pure JS.
Zero RunPod. Zero backend. Deploys to Netlify as-is.

### TIER 1 — AI Music / Suno (build first)

| # | Tool | Slug | Build Type |
|---|------|------|-----------|
| 1 | Suno Prompt Optimizer | `/tools/suno-prompt-optimizer` | Claude API |
| 2 | AI Music Rights Navigator | `/tools/ai-music-rights-navigator` | Claude API |
| 3 | AI Music DDEX Disclosure Checker | `/tools/ai-music-ddex-checker` | Claude API |
| 4 | AI Track Copyright Strength Calculator | `/tools/ai-copyright-strength` | Claude API |
| 5 | Suno Credits Calculator | `/tools/suno-credits-calculator` | Pure JS |
| 6 | AI Music Income Calculator | `/tools/ai-music-income-calculator` | Pure JS |
| 7 | AI Platform Comparison Tool | `/tools/ai-music-platform-comparison` | Claude API |
| 8 | AI Lyrics Optimizer for Suno | `/tools/ai-lyrics-optimizer` | Claude API |
| 9 | AI Music Distribution Roadmap | `/tools/ai-music-distribution-roadmap` | Claude API |
| 10 | AI Music Niche Finder | `/tools/ai-music-niche-finder` | Claude API |
| 11 | AI vs Human Monetization Comparison | `/tools/ai-vs-human-monetization` | Pure JS |
| 12 | Suno vs Human Quiz | `/tools/suno-vs-human-quiz` | Pure JS |
| 13 | AI + Human Hybrid Workflow Builder | `/tools/ai-hybrid-workflow-builder` | Claude API |
| 14 | AI Music Genre Accuracy Tester | `/tools/ai-genre-accuracy-tester` | Pure JS |

### TIER 2 — Production Viral

| # | Tool | Slug | Build Type |
|---|------|------|-----------|
| 15 | "Why Does My Mix Sound Amateur?" Diagnostic | `/tools/mix-sounds-amateur-diagnostic` | Claude API |
| 16 | "Why Is My Vocal Sitting Wrong?" Fixer | `/tools/vocal-sitting-wrong-fixer` | Claude API |
| 17 | 808 Relationship Analyzer | `/tools/808-relationship-analyzer` | Pure JS + Canvas |
| 18 | Drum Tuning Reference | `/tools/drum-tuning-reference` | Pure JS + Canvas |
| 19 | Spotify Skip Probability Map | `/tools/spotify-skip-probability-map` | Pure JS + Canvas |
| 20 | Streaming Income Reality Check | `/tools/streaming-income-reality-check` | Pure JS |
| 21 | Frequency Masking Visualizer | `/tools/frequency-masking-visualizer` | Pure JS + Canvas |
| 22 | BPM Tap Tempo Pro | `/tools/tap-tempo-pro` | Pure JS + Web Audio |
| 23 | Beat Selling Price Calculator | `/tools/beat-selling-price-calculator` | Claude API |
| 24 | Chord Progression Emotion Mapper | `/tools/chord-progression-emotion-mapper` | Claude API + Canvas |
| 25 | AI Music Playlist Placement Scorer | `/tools/ai-playlist-placement-scorer` | Claude API |

---

# PART 2 — FROZEN VISUAL DESIGN SYSTEM

## The Quality Standard

Every tool must match or exceed the Frequency Conflict Detector:
`https://www.musicproductionwiki.com/tools/frequency-conflict-detector`

That tool is the MPW design gold standard for tools pages.

## Brand Colors — CSS Variables (copy verbatim)

```css
:root {
  --bg:     #0d0d1a;
  --bg2:    #111120;
  --bg3:    #16162a;
  --bg4:    #1c1c32;
  --border: rgba(255,255,255,0.07);
  --border2:rgba(255,255,255,0.12);
  --border3:rgba(255,255,255,0.18);
  --amber:  #f5a623;
  --amber2: rgba(245,166,35,0.12);
  --amber3: rgba(245,166,35,0.06);
  --teal:   #00e8a2;
  --teal2:  rgba(0,232,162,0.1);
  --red:    #ff3d5a;
  --text:   #f0f0f4;
  --text2:  #a0a0b8;
  --text3:  #5a5a7a;
  --mono:   'DM Mono', monospace;
  --sans:   'DM Sans', sans-serif;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  line-height: 1.6;
}
```

## Font Import (required in every tool <head>)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## Body Layout

```css
.tool-page { max-width: 860px; margin: 0 auto; padding: 40px 20px 80px; }
@media(max-width:600px){ .tool-page { padding: 24px 16px 60px; } }
```

## Page Title Block

```html
<div class="tool-page-title">
  <h1>[Tool Name]</h1>
  <p class="tool-page-desc">[One or two sentence description of what this tool does and who it's for.]</p>
</div>
```

```css
.tool-page-title { margin-bottom: 28px; }
.tool-page-title h1 {
  font-size: clamp(26px,5vw,36px); font-weight: 900;
  letter-spacing: -0.03em; color: var(--text); margin-bottom: 10px;
}
.tool-page-desc { font-size: 16px; color: var(--text2); line-height: 1.65; }
```

## Branded Tool Header Card (required on every tool)

```html
<div class="thc">
  <div class="thc-brand">
    <div class="thc-mark">
      <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
        <rect x="1.5" y="7" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
        <rect x="6" y="4" width="2.5" height="12" rx="1.2" fill="#0a0a0b"/>
        <rect x="10.5" y="1" width="2.5" height="16" rx="1.2" fill="#0a0a0b"/>
        <rect x="15" y="5" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
      </svg>
    </div>
    <div>
      <div class="thc-name">MusicProductionWiki.com</div>
      <div class="thc-sub">◆ The Producer's Tools</div>
    </div>
  </div>
  <div class="thc-right">
    <span class="thc-badge">INTERACTIVE TOOL</span>
    <a href="/tools/[related-slug].html" class="thc-related">[Related Tool]</a>
  </div>
</div>
```

```css
.thc {
  background: var(--bg2); border: 1px solid var(--border2);
  border-radius: 12px; padding: 16px 20px;
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 24px; flex-wrap: wrap; gap: 12px;
}
.thc-brand { display: flex; align-items: center; gap: 12px; }
.thc-mark {
  width: 32px; height: 32px; border-radius: 8px;
  background: var(--teal); display: flex; align-items: center; justify-content: center;
}
.thc-name { font-size: 14px; font-weight: 600; color: var(--text); }
.thc-sub { font-size: 11px; color: var(--amber); font-family: var(--mono); letter-spacing:.04em; }
.thc-right { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
.thc-badge {
  font-size: 10px; font-family: var(--mono); font-weight: 700; color: var(--amber);
  border: 1px solid rgba(245,166,35,0.4); border-radius: 4px;
  padding: 4px 10px; letter-spacing: 0.1em;
}
.thc-related { font-size: 13px; color: var(--text2); text-decoration: none; transition: color .15s; }
.thc-related:hover { color: var(--teal); }
```

## Section Card

```html
<div class="tsec">
  <div class="tsec-label">SECTION TITLE</div>
  <!-- content -->
</div>
```

```css
.tsec {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: 10px; padding: 20px; margin-bottom: 16px;
}
.tsec-label {
  font-size: 9px; font-family: var(--mono); font-weight: 700;
  color: var(--amber); letter-spacing: 0.18em;
  text-transform: uppercase; margin-bottom: 16px;
}
```

## Insight Callout (amber left border — primary output)

```html
<div class="tinsight" id="output">Your result will appear here.</div>
```

```css
.tinsight {
  border-left: 3px solid var(--amber);
  background: var(--amber3);
  border-radius: 0 8px 8px 0;
  padding: 16px 18px;
  font-size: 15px; color: var(--text); line-height: 1.7;
  margin-top: 16px;
}
.tinsight.teal {
  border-left-color: var(--teal);
  background: var(--teal2);
}
```

## Field Label

```css
.tfield { margin-bottom: 18px; }
.tlabel {
  font-size: 9px; font-family: var(--mono); color: var(--text3);
  letter-spacing: 0.12em; text-transform: uppercase;
  display: block; margin-bottom: 8px;
}
```

## Slider

```html
<div class="tfield">
  <label class="tlabel" for="mySlider">LABEL</label>
  <div class="tslider-row">
    <input type="range" class="tslider" id="mySlider" min="0" max="100" value="50">
    <span class="tslider-val" id="myVal">50</span>
  </div>
</div>
```

```css
.tslider-row { display: flex; align-items: center; gap: 12px; }
.tslider {
  flex: 1; -webkit-appearance: none; appearance: none;
  height: 4px; background: var(--border2); outline: none;
  border-radius: 2px; cursor: pointer;
}
.tslider::-webkit-slider-thumb {
  -webkit-appearance: none; width: 16px; height: 16px;
  border-radius: 50%; background: var(--amber); cursor: pointer;
  box-shadow: 0 0 6px rgba(245,166,35,0.35);
}
.tslider-val {
  font-size: 13px; font-family: var(--mono); color: var(--amber);
  min-width: 40px; text-align: right; font-weight: 600;
}
```

## Select / Dropdown

```html
<div class="tfield">
  <label class="tlabel" for="mySelect">LABEL</label>
  <select class="tselect" id="mySelect">
    <option value="a">Option A</option>
  </select>
</div>
```

```css
.tselect {
  width: 100%; background: var(--bg3); border: 1px solid var(--border2);
  color: var(--text); font-family: var(--sans); font-size: 14px;
  padding: 10px 14px; border-radius: 8px; cursor: pointer; outline: none;
  appearance: none;
}
.tselect:focus { border-color: var(--amber); }
```

## Textarea (for lyrics optimizer, text inputs)

```html
<textarea class="ttextarea" id="myText" rows="5" placeholder="Paste your text here..."></textarea>
```

```css
.ttextarea {
  width: 100%; background: var(--bg3); border: 1px solid var(--border2);
  color: var(--text); font-family: var(--sans); font-size: 14px;
  padding: 12px 14px; border-radius: 8px; outline: none; resize: vertical;
  line-height: 1.6;
}
.ttextarea:focus { border-color: var(--amber); }
```

## Primary Button

```html
<button class="tbtn" id="calcBtn">Calculate →</button>
```

```css
.tbtn {
  background: linear-gradient(135deg, var(--amber), #e08000);
  color: #000; font-family: var(--sans); font-size: 14px; font-weight: 700;
  border: none; cursor: pointer; border-radius: 8px;
  padding: 12px 28px; letter-spacing: -0.01em;
  transition: transform 0.12s, box-shadow 0.12s;
  box-shadow: 0 0 20px rgba(245,166,35,0.2);
}
.tbtn:hover { transform: translateY(-1px); box-shadow: 0 0 30px rgba(245,166,35,0.35); }
.tbtn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
```

## Loading State (for Claude API calls)

```html
<div class="tloading" id="loading" style="display:none">
  <div class="tloading-dot"></div>
  <span>Analyzing...</span>
</div>
```

```css
.tloading {
  display: flex; align-items: center; gap: 10px;
  font-size: 13px; font-family: var(--mono); color: var(--text3);
  margin-top: 16px;
}
.tloading-dot {
  width: 8px; height: 8px; border-radius: 50%; background: var(--amber);
  animation: tpulse 1s ease-in-out infinite;
}
@keyframes tpulse { 0%,100%{opacity:1} 50%{opacity:0.2} }
```

## Click-to-Copy Chip

```html
<span class="tchip" data-val="VALUE" onclick="tcopy(this)">
  VALUE <span style="opacity:.5;font-size:11px">⊕</span>
</span>
```

```css
.tchip {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--bg3); border: 1px solid var(--border2);
  border-radius: 6px; padding: 6px 12px;
  font-family: var(--mono); font-size: 13px; font-weight: 600;
  color: var(--amber); cursor: pointer; transition: all 0.12s;
}
.tchip:hover { border-color: var(--amber); background: var(--amber2); }
```

```javascript
function tcopy(el) {
  var val = el.dataset.val || el.textContent.replace('⊕','').trim();
  navigator.clipboard.writeText(val).then(function() {
    var orig = el.innerHTML;
    el.innerHTML = 'Copied ✓';
    el.style.color = 'var(--teal)';
    el.style.borderColor = 'var(--teal)';
    setTimeout(function() {
      el.innerHTML = orig;
      el.style.color = '';
      el.style.borderColor = '';
    }, 1500);
  });
}
```

## Canvas Container

```html
<canvas id="myCanvas" style="width:100%;height:220px;display:block;border-radius:8px;background:var(--bg3);"></canvas>
```

```javascript
// Always set canvas dimensions in JS:
var canvas = document.getElementById('myCanvas');
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;
// Redraw on resize:
window.addEventListener('resize', function() {
  canvas.width = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;
  draw(); // re-render
});
```

## Score/Results Card Grid

```html
<div class="tscore-grid">
  <div class="tscore-card">
    <div class="tscore-label">METRIC NAME</div>
    <div class="tscore-val">87</div>
    <div class="tscore-sub">out of 100</div>
  </div>
</div>
```

```css
.tscore-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 12px; margin-top: 16px;
}
.tscore-card {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 8px; padding: 16px; text-align: center;
}
.tscore-label {
  font-size: 9px; font-family: var(--mono); color: var(--text3);
  letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 8px;
}
.tscore-val {
  font-size: 36px; font-weight: 900; color: var(--amber);
  letter-spacing: -0.04em; line-height: 1;
}
.tscore-sub { font-size: 11px; color: var(--text3); margin-top: 4px; }
```

## Risk Badge (for legal/rights tools)

```html
<span class="trisk trisk-low">LOW RISK</span>
<span class="trisk trisk-med">MEDIUM RISK</span>
<span class="trisk trisk-high">HIGH RISK</span>
<span class="trisk trisk-no">DO NOT USE</span>
```

```css
.trisk {
  display: inline-block; font-size: 10px; font-family: var(--mono);
  font-weight: 700; letter-spacing: 0.1em; border-radius: 4px;
  padding: 4px 10px;
}
.trisk-low  { background: rgba(0,232,162,0.12); color: var(--teal); border: 1px solid rgba(0,232,162,0.3); }
.trisk-med  { background: rgba(245,166,35,0.12); color: var(--amber); border: 1px solid rgba(245,166,35,0.3); }
.trisk-high { background: rgba(255,61,90,0.12); color: var(--red); border: 1px solid rgba(255,61,90,0.3); }
.trisk-no   { background: rgba(255,61,90,0.2); color: var(--red); border: 1px solid var(--red); }
```

## Related Tools Section (required at bottom of every tool)

```html
<div class="trelated">
  <div class="trelated-label">RELATED TOOLS</div>
  <div class="trelated-grid">
    <a href="/tools/[slug].html" class="trelated-card">
      <span class="trelated-name">[Tool Name]</span>
      <span class="trelated-desc">[Short desc]</span>
    </a>
    <a href="/tools/[slug].html" class="trelated-card">...</a>
    <a href="/tools/[slug].html" class="trelated-card">...</a>
  </div>
</div>
```

```css
.trelated { margin-top: 48px; padding-top: 32px; border-top: 1px solid var(--border); }
.trelated-label {
  font-size: 9px; font-family: var(--mono); font-weight: 700;
  color: var(--text3); letter-spacing: 0.15em; margin-bottom: 16px;
}
.trelated-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(200px,1fr)); gap: 10px; }
.trelated-card {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: 8px; padding: 14px 16px; text-decoration: none;
  transition: border-color 0.15s;
}
.trelated-card:hover { border-color: var(--border2); }
.trelated-name { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
.trelated-desc { display: block; font-size: 12px; color: var(--text3); }
```

---

# PART 3 — FULL PAGE TEMPLATE

Copy this skeleton for every tool. Replace ALL [PLACEHOLDER] values.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[Tool Name] — Free [Keyword] Tool | MusicProductionWiki</title>
<meta name="description" content="[150-160 char description with primary keyword. Ends with period.]">
<meta property="og:title" content="[Tool Name] — MusicProductionWiki">
<meta property="og:description" content="[OG description — 120 chars max]">
<meta property="og:url" content="https://www.musicproductionwiki.com/tools/[slug].html">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.musicproductionwiki.com/tools/[slug].html">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-79VB543KCT"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-79VB543KCT');</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question 1]",
      "acceptedAnswer": {"@type": "Answer", "text": "[Answer 1]"}
    },
    {
      "@type": "Question",
      "name": "[Question 2]",
      "acceptedAnswer": {"@type": "Answer", "text": "[Answer 2]"}
    },
    {
      "@type": "Question",
      "name": "[Question 3]",
      "acceptedAnswer": {"@type": "Answer", "text": "[Answer 3]"}
    }
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Home","item":"https://www.musicproductionwiki.com"},
    {"@type":"ListItem","position":2,"name":"Tools","item":"https://www.musicproductionwiki.com/tools/"},
    {"@type":"ListItem","position":3,"name":"[Tool Name]","item":"https://www.musicproductionwiki.com/tools/[slug].html"}
  ]
}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
<style>
/* === TOOL CSS — paste frozen variables + components here === */
:root {
  --bg:#0d0d1a;--bg2:#111120;--bg3:#16162a;--bg4:#1c1c32;
  --border:rgba(255,255,255,0.07);--border2:rgba(255,255,255,0.12);
  --amber:#f5a623;--amber2:rgba(245,166,35,0.12);--amber3:rgba(245,166,35,0.06);
  --teal:#00e8a2;--teal2:rgba(0,232,162,0.1);--red:#ff3d5a;
  --text:#f0f0f4;--text2:#a0a0b8;--text3:#5a5a7a;
  --mono:'DM Mono',monospace;--sans:'DM Sans',sans-serif;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:var(--sans);line-height:1.6}
.tool-page{max-width:860px;margin:0 auto;padding:40px 20px 80px}
/* [paste all component CSS here] */

/* NAV CSS SPECIFICITY — REQUIRED */
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-bible-link:hover{background:rgba(245,166,35,.1)!important;color:#f5a623!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link{color:#00e8a2!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link:hover{background:rgba(0,232,162,.08)!important;color:#00e8a2!important}
</style>
</head>
<body>

<!-- NAV — paste full mpw-nav-homepage-v1 here -->

<div class="tool-page">
  <div class="tool-page-title">
    <h1>[Tool Name]</h1>
    <p class="tool-page-desc">[Description]</p>
  </div>

  <!-- BRANDED HEADER CARD -->
  <div class="thc">
    <div class="thc-brand">
      <div class="thc-mark">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
          <rect x="1.5" y="7" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
          <rect x="6" y="4" width="2.5" height="12" rx="1.2" fill="#0a0a0b"/>
          <rect x="10.5" y="1" width="2.5" height="16" rx="1.2" fill="#0a0a0b"/>
          <rect x="15" y="5" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
        </svg>
      </div>
      <div>
        <div class="thc-name">MusicProductionWiki.com</div>
        <div class="thc-sub">◆ The Producer's Tools</div>
      </div>
    </div>
    <div class="thc-right">
      <span class="thc-badge">INTERACTIVE TOOL</span>
      <a href="/tools/" class="thc-related">All Tools →</a>
    </div>
  </div>

  <!-- TOOL INTERACTIVE BODY -->
  <!-- [build tool here] -->

  <!-- RELATED TOOLS -->
  <div class="trelated">
    <div class="trelated-label">RELATED TOOLS</div>
    <div class="trelated-grid">
      <a href="/tools/[slug1].html" class="trelated-card">
        <span class="trelated-name">[Name 1]</span>
        <span class="trelated-desc">[Desc 1]</span>
      </a>
      <a href="/tools/[slug2].html" class="trelated-card">
        <span class="trelated-name">[Name 2]</span>
        <span class="trelated-desc">[Desc 2]</span>
      </a>
      <a href="/tools/[slug3].html" class="trelated-card">
        <span class="trelated-name">[Name 3]</span>
        <span class="trelated-desc">[Desc 3]</span>
      </a>
    </div>
  </div>
</div>

<!-- FOOTER -->
<footer style="border-top:1px solid var(--border);padding:24px 20px;text-align:center;">
  <p style="font-size:12px;color:var(--text3)">
    © 2026 <a href="https://www.musicproductionwiki.com" style="color:var(--amber);text-decoration:none">MusicProductionWiki.com</a>
    &nbsp;·&nbsp; <a href="/tools/" style="color:var(--text2);text-decoration:none">All Tools</a>
    &nbsp;·&nbsp; <a href="/bible/" style="color:var(--text2);text-decoration:none">Producer's Bible</a>
    &nbsp;·&nbsp; <a href="https://theproducersbriefing.beehiiv.com" style="color:var(--text2);text-decoration:none">Newsletter</a>
  </p>
</footer>

<script src="../js/main.js"></script>
<script>
// TOOL JAVASCRIPT HERE
</script>
</body>
</html>
```

---

# PART 4 — CLAUDE API INTEGRATION

```javascript
async function callClaude(userMessage, systemPrompt) {
  var loadEl = document.getElementById('loading');
  var outputEl = document.getElementById('output');
  var btn = document.getElementById('calcBtn');
  if (loadEl) loadEl.style.display = 'flex';
  if (outputEl) outputEl.style.display = 'none';
  if (btn) btn.disabled = true;
  try {
    var res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system: systemPrompt,
        messages: [{role: 'user', content: userMessage}]
      })
    });
    var data = await res.json();
    var text = data.content && data.content[0] ? data.content[0].text : 'No response received.';
    if (outputEl) {
      outputEl.innerHTML = text.replace(/\n/g, '<br>');
      outputEl.style.display = 'block';
    }
    return text;
  } catch (err) {
    if (outputEl) {
      outputEl.textContent = 'Connection error. Please try again.';
      outputEl.style.display = 'block';
    }
    return null;
  } finally {
    if (loadEl) loadEl.style.display = 'none';
    if (btn) btn.disabled = false;
  }
}
```

---

# PART 5 — TOOL CARD FOR /tools/index.html

Every tool card goes in the appropriate section of `/tools/index.html`.
Add the AI Music category pill to the filter bar at the same time as the first AI music tool.

```html
<!-- AI Music category pill — add ONCE when first AI music tool goes live -->
<button class="tools-cat-btn" data-cat="ai-music">AI Music</button>

<!-- Tool card — add for every new tool -->
<a class="tool-card" href="/tools/[slug].html" data-cat="[category]" data-name="[searchable keywords]">
  <div class="tool-card-body">
    <span class="tool-card-name">[Tool Name]</span>
    <span class="tool-card-desc">[One sentence. Max 15 words. What it does.]</span>
    <span class="tool-card-cat">[Category Label]</span>
  </div>
  <span class="tool-card-arrow">→</span>
</a>
```

Category labels for the 25 tools:
- Tools 1–14: `AI Music`
- Tools 15–16: `Mixing & Signal Flow`
- Tools 17–18: `Beat Making & Rhythm`
- Tool 19: `Arrangement & Structure`
- Tool 20: `Business & Legal`
- Tool 21: `Frequency & EQ`
- Tool 22: `Time & Modulation`
- Tool 23: `Business & Legal`
- Tool 24: `Music Theory & Composition`
- Tool 25: `AI Music`

---

# PART 6 — QUALITY CHECKLIST

Before every commit, confirm ALL of the following:

**Head:**
- [ ] Correct canonical URL
- [ ] Meta description 150–160 chars with keyword
- [ ] FAQPage JSON-LD (min 3 pairs)
- [ ] BreadcrumbList JSON-LD
- [ ] GA4 tracking script
- [ ] DM Sans + DM Mono fonts imported
- [ ] ../css/style.css linked

**Visual:**
- [ ] Body background is #0d0d1a
- [ ] Branded tool header card present with teal logo mark
- [ ] Tool name in H1
- [ ] At least one section card using .tsec
- [ ] Insight callout .tinsight for primary output
- [ ] Related tools section at bottom
- [ ] Footer with copyright + links

**Functional:**
- [ ] Primary button works and triggers output
- [ ] Loading state shown during Claude API calls
- [ ] Error handled gracefully if API call fails
- [ ] Mobile responsive (test at 375px width mentally)
- [ ] All copy chips work

**Nav:**
- [ ] Full MPW nav present
- [ ] CSS specificity fix applied (nav.mpw-site-nav .nav-item>a.nav-bible-link)
- [ ] Tools → in desktop nav (nav-tools-link)
- [ ] Grid mobile drawer
- [ ] pushState + popstate back-button fix

**Commit:**
- [ ] File committed to tools/[slug].html
- [ ] Tool card added to tools/index.html in SAME commit
- [ ] AI Music pill added (first AI music tool only)

---

# PART 7 — GITHUB CREDENTIALS

```
Token: [GITHUB_TOKEN_FROM_SETENV]
Repo: github.com/musicproductionwiki/musicproductionwiki
Base URL: https://api.github.com/repos/musicproductionwiki/musicproductionwiki
GA4: G-79VB543KCT
Site: https://www.musicproductionwiki.com
```

---

# PART 8 — PARALLEL SESSION START PROMPT

Copy this verbatim when opening a new parallel Claude session for tool building:

```
You are building tools for MusicProductionWiki.com (MPW), a music production
reference site. You are acting as Co-CEO and production partner.

STEP 1: Fetch and read MPW-TOOL-BUILD-SPEC.md from GitHub:
https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/MPW-TOOL-BUILD-SPEC.md
Token: [GITHUB_TOKEN_FROM_SETENV]

STEP 2: Build [TOOL NAME] — slug: [TOOL SLUG]
Use the frozen CSS variables, component library, and page template from the spec.
The tool must match the quality of: musicproductionwiki.com/tools/frequency-conflict-detector
Build type: [Claude API / Pure JS / Pure JS + Canvas]

STEP 3: Commit to GitHub:
- tools/[slug].html (the tool)
- tools/index.html (add tool card — same commit via Trees API)

STEP 4: Report back with live URL and commit SHA.

NEVER rules from this project:
- NEVER use class-only nav selectors — child combinator required
- NEVER commit tool without updating tools/index.html in same commit
- NEVER skip the quality checklist
- NEVER invent tool slugs — use only the slug assigned in the spec
- NEVER set canvas dimensions via HTML attributes — use JS
```

---

# SESSION 80 ADDENDUM — TOOL BUILD SPEC
# Destination Tool Standards + Full Flagship Queue
*Appended to MPW-TOOL-BUILD-SPEC.md — May 29, 2026*

---

## GOLD STANDARDS — CORRECT REFERENCES

| Reference | Purpose | File |
|-----------|---------|------|
| **Frequency Conflict Detector** | Design + UX gold standard for ALL destination tools | `/tools/frequency-conflict-detector.html` |
| **Mix Fingerprint Analyzer** | Gold standard for Web Audio + D3 destination tools specifically | `/tools/mix-fingerprint.html` |
| **attack-release-calculator.html** | Nav extraction source ONLY — copy nav CSS block 2 + nav HTML from here | `/tools/attack-release-calculator.html` |
| **compression.html** | Share bar pattern, embed code pattern, schema structure | `bible/compression.html` |

**Never confuse these roles.** The attack-release calculator is a calculator-tier tool. It is not a design reference. It is only used as a source for the nav HTML + CSS injection pattern because its nav CSS block is confirmed working and self-contained.

---

## What Makes a Destination Tool vs a Calculator

A **calculator** answers one question. Returns immediately. One input → one output.

A **destination tool** is a product people return to, share, and reference in sessions. Visual output that communicates more than text. Curated data that took real research. A recommendation engine that tells the producer what to do next. These go in the flagship section and are Product Hunt submission material.

---

## Visual Standard — Destination Tools

| Element | Requirement |
|---------|-------------|
| Design gold standard | Frequency Conflict Detector — match or exceed |
| Background | `#0d0d1a` (--bg) with ambient orb glows via radial-gradient |
| Cards | Glassmorphism — `backdrop-filter:blur(20px)`, `rgba(255,255,255,0.04)` backgrounds |
| Charts | D3.js or Canvas — never static SVG for live data visualization |
| Animation | Elements draw themselves in — `d3.easeCubicOut`, 700–900ms |
| Color system | Each metric has its own color, consistent across chart + cards + diagnosis |
| Typography | DM Sans (UI) + DM Mono (numbers/labels) — Google Fonts, preconnected |
| Design variables | `--bg:#0d0d1a; --bg2:#111120; --bg3:#16162a; --bg4:#1c1c32; --amber:#f5a623; --teal:#00e8a2; --red:#ff3d5a; --text:#f0f0f4; --text2:#a0a0b8; --text3:#5a5a7a; --mono:'DM Mono',monospace; --sans:'DM Sans',sans-serif;` |

---

## UX Standard — Destination Tools

| Element | Requirement |
|---------|-------------|
| Layout | Input left / visualization right on desktop; single column on mobile |
| Flow | Numbered steps — user always knows where they are |
| Auto-measurement | Measure everything measurable automatically from uploaded file |
| Manual input | Only for what genuinely cannot be measured |
| How-to | 3-step plain English explanation BELOW the hero headline — never above it |
| Presets | Named producer/track presets — one-click load. Minimum 4 presets per tool |
| Click-to-copy | On every value a producer would enter in a DAW |
| Recommendation | Tool tells producer what to do next — not just what the number is |
| Diagnosis | Written verdict + body + specific fix per divergent axis/output |
| Related tools | At very bottom above footer only — never mid-page |

---

## Technical Standard — Destination Tools

| Requirement | Detail |
|-------------|--------|
| Nav | Full `mpw-site-nav` — HTML + CSS extracted from `attack-release-calculator.html` block 2. Never rebuild from scratch. |
| main.js | `<script src="../js/main.js" defer></script>` in `<head>` |
| No style.css | Tool pages never load `../css/style.css` |
| OG image | `<meta property="og:image" content="https://musicproductionwiki.com/og-image.png">` |
| Canonical | Non-www: `https://musicproductionwiki.com/tools/[slug].html` |
| Schema | FAQPage + BreadcrumbList minimum |
| Share bar | Copy Link + Share on X + Reddit — flex row, flex:1 each, no wrap |
| Embed code | Every tool embeddable — one-click iframe snippet below share bar |
| Email gate | On export/report output — never on the tool itself |
| Embed mode | `?embed=true` hides nav and footer |
| Mobile | Single column ≤920px. Visualization full width. Score cards 2-col. |
| Monetization | Built in from day one — not retrofitted |

---

## Full Flagship Destination Tool Queue — All 12

| # | Tool | Slug | Group | Status | Priority |
|---|------|------|-------|--------|----------|
| 1 | Loudness Penalty Calculator | `/tools/loudness-penalty` | A — Pure JS | ⚠️ Live but thin — needs file upload revamp | S81 revamp |
| 2 | 808 Relationship Analyzer | `/tools/808-relationship-analyzer` | B — Web Audio | 🔜 Not built | S81+ |
| 3 | Arrangement Blueprint Generator | `/tools/arrangement-blueprint` | C — Canvas/SVG | 🔜 Not built | S81+ |
| 4 | Mix Fingerprint Analyzer | `/tools/mix-fingerprint` | C — D3.js | ✅ LIVE | Done |
| 5 | Vocal Chain Builder | `/tools/vocal-chain-builder` | D — Claude API | 🔜 Not built | S82+ |
| 6 | ClearCheck — Sample Risk Assessor | `/tools/clearcheck` | D — Claude API | 🔜 Not built | S82+ |
| 7 | Mix Translation System Simulator | `/tools/mix-translation` | C — SVG multi-panel | 🔜 Not built | S82+ |
| 8 | Plugin Chain Signal Flow Visualizer | `/tools/signal-flow-visualizer` | C — Drag-drop SVG | 🔜 Not built | S82+ |
| 9 | Reference Track Decoder | `/tools/reference-decoder` | D — Claude API | 🔜 Not built | S82+ |
| 10 | Producer BPM DNA | `/tools/bpm-dna` | C — D3 bell curve | 🔜 Not built | S81+ |
| 11 | Stem Quality Tester | `/tools/stem-quality-tester` | D — Claude API + Web Audio | 🔜 Not built | S82+ |
| 12 | Frequency Conflict Detector v2 | `/tools/frequency-conflict-detector` | A — Pure JS upgrade | 🔜 Not built | S81+ |

---

## Flagship Section on Hub — Current State

| Card | Status |
|------|--------|
| Mix Fingerprint Analyzer | ✅ LIVE — first card |
| Frequency Conflict Detector | ✅ LIVE — second card |
| Arrangement Blueprint Generator | Coming Soon card |
| Mix Translation Stress Tester | Coming Soon card |
| Dynamic Range Analyzer | Coming Soon card |
| ClearCheck | Coming Soon card |

Loudness Penalty is NOT in the flagship section until full revamp with file upload is complete.

---

## Hub Architecture Note

Zone 1 (live tool as hero) was NOT built in S80 — too complex and broke the page. The hub currently uses the original hero (headline + desc) with the flagship cards section (Zone 2) between hero and grid. Zone 1 remains a future enhancement after the destination tool queue matures.
