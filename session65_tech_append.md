---

# SESSION 65 UPDATE — TECH — May 24, 2026

## Article Nav — Final Confirmed State (All 526 Articles)

### Desktop Nav — Confirmed
```html
<li class="nav-item"><a href="/tools/" class="nav-tools-link">Tools →</a></li>
<li class="nav-item"><a href="/bible/" class="nav-bible-link">The Producer's Bible →</a></li>
```

### CSS Specificity — Confirmed Fix
Old (broken — beaten by child combinator rule):
```css
nav.mpw-site-nav .nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-bible-link:hover{background:rgba(245,166,35,.1)!important;color:#f5a623!important}
```

New (correct — matches specificity of the overriding rule):
```css
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-bible-link:hover{background:rgba(245,166,35,.1)!important;color:#f5a623!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link{color:#00e8a2!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link:hover{background:rgba(0,232,162,.08)!important;color:#00e8a2!important}
```

**Lesson:** On `mpw-nav-homepage-v1` pages, the general rule `nav.mpw-site-nav .nav-item>a{color:#a0a0b4!important}` uses a child combinator and beats any class-only selector. Child combinator (`>`) increases specificity beyond a simple class. Always use `nav-item>a.classname` pattern for nav color overrides.

### Mobile Drawer — Confirmed Final HTML (All 526 Articles)
```html
<div class="mobile-drawer" id="mobileDrawer">
  <a href="/tools/" style="display:flex;align-items:center;gap:8px;padding:12px 16px;border-radius:9px;background:rgba(0,232,162,0.07);border:1px solid rgba(0,232,162,0.22);color:#00e8a2;font-size:14px;font-weight:600;text-decoration:none;margin:4px 0 8px">✦ The Producer's Tools</a>
  <a href="/bible/" class="mob-bible">●&nbsp;The Producer's Bible — Explore Free</a>
  <div class="mob-section-label">Articles</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:4px">
    <a href="/categories/techniques.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Techniques</a>
    <a href="/categories/reviews.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Reviews</a>
    <a href="/categories/comparisons.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Comparisons</a>
    <a href="/categories/breakdowns.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Breakdowns</a>
    <a href="/categories/recreations.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Recreations</a>
    <a href="/genres.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Genres</a>
    <a href="/categories/ai-music.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">AI Music</a>
    <a href="/categories/music-business.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Music Business</a>
  </div>
  <div class="mob-section-label">Gear</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:4px">
    <a href="/categories/daws.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">DAWs</a>
    <a href="/categories/plugins.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Plugins</a>
    <a href="/categories/gear.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Hardware</a>
  </div>
  <a href="https://theproducersbriefing.beehiiv.com" class="mob-cta">Sound Better →</a>
</div>
```

**Important:** `mob-bible` link contains `\u00a0` (non-breaking space U+00A0) after the bullet character — NOT a regular space. Any future patch script targeting this string must use the exact bytes. Confirmed by fetching live file and printing `repr()`.

### Drawer JS — pushState/popstate Pattern (All 526 Articles)
```javascript
var mob=document.getElementById('navMob');
var drawer=document.getElementById('mobileDrawer');
if(mob&&drawer){
  mob.addEventListener('click',function(){
    var opening=!drawer.classList.contains('open');
    drawer.classList.toggle('open');
    if(opening&&window.history&&window.history.pushState){history.pushState({drawerOpen:true},'',location.href);}
  });
  drawer.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){drawer.classList.remove('open');});});
  window.addEventListener('popstate',function(e){if(drawer.classList.contains('open')){drawer.classList.remove('open');}});
}
```

**Why pushState not replaceState on article pages:**
- Category pages use `replaceState` because Netlify's redirect creates a double history entry on page load — collapsing it prevents needing an extra back-press
- Article pages have no redirect — they load cleanly. `replaceState` on article pages does nothing useful for the back button
- Article pages need `pushState` when the drawer OPENS — this adds a fake history entry. When user presses back, the browser fires `popstate` which the JS catches and closes the drawer instead of navigating away

---

## File Structure — Updated

```
repo root/
├── bible/
│   ├── index.html           ← REBUILT S63 — reverb.html nav, Reverb featured, 25min, Beehiiv ✅
│   ├── reverb.html          ← gold standard — 25min read time ✅
│   ├── [222 entries]        ← mobile-drawer STILL in place — bmn-drawer PENDING (next Bible session)
│   └── categories/
│       ├── dynamics/        ← bmn-drawer ✅, replaceState ✅ (S61)
│       ├── frequency/       ← bmn-drawer ✅, replaceState ✅
│       ├── time-based/      ← bmn-drawer ✅, replaceState ✅
│       ├── signal-processing/ ← bmn-drawer ✅, replaceState ✅
│       ├── mixing/          ← bmn-drawer ✅, replaceState ✅
│       ├── mastering/       ← bmn-drawer ✅, replaceState ✅
│       ├── synthesis/       ← bmn-drawer ✅, replaceState ✅
│       ├── music-theory/    ← bmn-drawer ✅, replaceState ✅
│       ├── production/      ← bmn-drawer ✅, replaceState ✅
│       ├── recording/       ← bmn-drawer ✅, replaceState ✅
│       └── tools/           ← bmn-drawer ✅, replaceState ✅, "The Producer's Tools" ✅
├── tools/
│   ├── index.html           ← LIVE — final SHA 8c7269d2 (amber cards + nav fix) ✅
│   └── [36 slug].html       ← all 36 tool pages LIVE ✅
├── articles/
│   └── [526 slug].html      ← ALL UPDATED S65 — Tools → in nav, grid drawer, pushState JS, CSS fix ✅
├── index.html               ← Tools → added to nav SHA fe168acb ✅
├── css/style.css
├── js/main.js
└── [handoff files]
```

---

## CSS Specificity Reference — mpw-nav-homepage-v1 Pages

This rule governs all article pages and tools/index.html:

```css
/* THE OVERRIDING RULE (already in mpw-nav-homepage-v1 block): */
nav.mpw-site-nav .nav-item>a{color:#a0a0b4!important}
/* Child combinator (>) means: specificity = (0,2,1) — beats class-only selectors */

/* WRONG — beaten even with !important: */
nav.mpw-site-nav .nav-bible-link{color:#f5a623!important}
/* specificity = (0,2,0) — loses to (0,2,1) despite !important */

/* CORRECT — matches the specificity pattern: */
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important}
/* specificity = (0,3,1) — wins */
```

**This is a gotcha that has burned us twice** (tools/index.html in S63/64, all 526 articles in S65). Document it clearly: on any page using `mpw-nav-homepage-v1`, all nav link color overrides MUST use the `nav.mpw-site-nav .nav-item>a.classname` pattern.

---

## NEVER Rules Added — Session 65 — Tech

| Rule | Detail |
|------|--------|
| NEVER use `replaceState` to fix the drawer back-button on article pages | `replaceState` is for Netlify-redirect double-history-entry (category pages). Article pages need `pushState` on open + `popstate` listener to close — confirmed working, commit f6979227 |
| NEVER patch mobile drawer HTML without printing exact `repr()` of the live target string | `\u00a0` non-breaking space in `mob-bible` link was only found by inspecting exact bytes — not visible in normal output |
| NEVER add nav color overrides with class-only selectors on mpw-nav-homepage-v1 pages | Child combinator specificity beats `!important` class-only — must use `nav.mpw-site-nav .nav-item>a.classname` — burned twice, now documented |
| NEVER run a 500+ file batch without at least 4 iterative fixes confirmed on the test article first | Session 65 ran 4 commits on test article before the full batch — this is correct and prevents corrupting all 526 |
| NEVER use bmn-drawer-cat CSS class on article pages | Article pages lack bmn-drawer CSS — use inline styles for grid card items only |

