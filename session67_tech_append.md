---

# SESSION 67 UPDATE — TECH — May 25, 2026

## Netlify Function — Final Working Implementation

### `netlify/functions/claude-proxy.js`
```javascript
const https = require('https');

exports.handler = async (event) => {
  const cors = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Content-Type': 'application/json'
  };
  if (event.httpMethod === 'OPTIONS') return { statusCode: 204, headers: cors, body: '' };
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return { statusCode: 500, headers: cors, body: JSON.stringify({ error: 'ANTHROPIC_API_KEY not set' }) };
  return new Promise((resolve) => {
    const data = Buffer.from(event.body || '{}');
    const req = https.request({
      hostname: 'api.anthropic.com', port: 443, path: '/v1/messages', method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': data.length, 'x-api-key': key, 'anthropic-version': '2023-06-01' }
    }, (res) => {
      let body = '';
      res.on('data', c => body += c);
      res.on('end', () => resolve({ statusCode: res.statusCode, headers: cors, body: body }));
    });
    req.on('error', e => resolve({ statusCode: 502, headers: cors, body: JSON.stringify({ error: e.message }) }));
    req.write(data); req.end();
  });
};
```

### `netlify.toml` — Current State
```toml
[build]
  publish = "."
  command = "echo 'build complete'"

[functions]
  directory = "netlify/functions"

[[redirects]]
  from = "/api/claude"
  to = "/.netlify/functions/claude-proxy"
  status = 200
  force = true

[[redirects]]
  from = "/dictionary/*"
  to = "/bible/:splat"
  status = 301

[[redirects]]
  from   = "/ssl-2-plus-review/"
  to     = "/articles/ssl-2-plus-review.html"
  status = 301

[[redirects]]
  from   = "/ssl-2-plus-review"
  to     = "/articles/ssl-2-plus-review.html"
  status = 301
```

**CRITICAL:** `[build] command` is required. Without it Netlify skips function bundling on static sites.

---

## Claude API Call Pattern — Correct for All Future Tools

```javascript
var res = await fetch('https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    model: 'claude-sonnet-4-5',
    max_tokens: 800,
    system: systemPrompt,
    messages: [{ role: 'user', content: userMessage }]
  })
});
var data = await res.json();
var raw = data.content && data.content[0] ? data.content[0].text : '';
console.log('RAW:', raw.substring(0, 300)); // always log for debugging
```

---

## Favicon
```html
<!-- In every tool <head> -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="alternate icon" href="/favicon.ico">
```

```svg
<!-- /favicon.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="#00e8a2"/>
  <rect x="3" y="13" width="4" height="15" rx="2" fill="#06061a"/>
  <rect x="10" y="8" width="4" height="20" rx="2" fill="#06061a"/>
  <rect x="17" y="3" width="4" height="26" rx="2" fill="#06061a"/>
  <rect x="25" y="10" width="4" height="15" rx="2" fill="#06061a"/>
</svg>
```

---

## Tool Design System — Session 67 Confirmed Actual Values

These override anything in MPW-TOOL-BUILD-SPEC.md where they conflict:

| Property | Value |
|----------|-------|
| Background | `#06061a` |
| Body text | `#e8e8ff` |
| Chip text unselected | `#c0c0e8` |
| Chip border unselected | `rgba(255,255,255,0.18)` |
| Section label | `#00e8a2` teal, DM Mono bold, 9-10px |
| Group labels | `#8080b8` DM Mono bold |
| Waveform speed — main | `0.00125` |
| Waveform speed — blue | `0.0019` |
| Waveform speed — amber | `0.0008` |
| Output text | DM Sans 16-18px — NEVER monospace |
| Monospace | DM Mono — labels/counts/hints ONLY |

---

## Tool Mapping Checklist — Required After Every Build

Run this check before closing any tool build session:

```
[ ] tools/[slug].html — committed to GitHub
[ ] tools/index.html — card added, count updated, same commit
[ ] bible/categories/tools/index.html — bcat-card added INSIDE #catGrid div
[ ] sitemap.xml — URL added with priority 0.8
[ ] search-index.json — entry added with category "Tools"
[ ] GSC — URL inspection + request indexing (Steve)
[ ] OG image — /images/[slug]-og.jpg referenced but needs to be created (Steve)
```

---

## Robust Response Parsing Pattern

```javascript
function extract(pattern, text, fallback) {
  var m = text.match(pattern);
  return m ? m[1].trim() : fallback;
}
var optimized = extract(/OPTIMIZED:\s*([^\n]+)/i, raw, '') || input;
var analysis  = extract(/ANALYSIS:\s*([\s\S]+?)(?=\nNEXT:|\n\d+\.|$)/i, raw, '');
var next      = extract(/NEXT:\s*([\s\S]+?)$/i, raw, '');

// Fallback if parsing fails completely
if (!analysis && !next && raw.length > 50) {
  var lines = raw.split('\n').filter(l => l.trim());
  analysis = lines.filter(l => !/^(SCORE|OPTIMIZED|ANALYSIS|NEXT|\d+[\.\)])/i.test(l.trim()) && l.length > 20).join(' ');
  next = lines.filter(l => /^\d+[\.\)]\s/.test(l.trim())).join('\n');
}
```

---

## NEVER Rules Added — Session 67 — Tech

| Rule | Detail |
|------|--------|
| NEVER call functions via custom domain | `musicproductionwiki.com/.netlify/functions/*` = 404. Use `classy-haupia-be8e43.netlify.app` |
| NEVER use `fetch()` inside Netlify Functions | Use `https.request()` + `Buffer.from()` |
| NEVER omit `[build] command` from netlify.toml | Required for function bundling on static sites |
| NEVER use `claude-sonnet-4-20250514` | Model is `claude-sonnet-4-5` |
| NEVER use assistant prefill | Returns empty content |
| NEVER put output text in monospace | DM Sans everywhere readable |
| NEVER insert catGrid cards without position verification | Confirm: grid_open < insert_pos < catEmpty_pos |

