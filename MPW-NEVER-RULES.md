# MPW-NEVER-RULES.md
## The Canonical Never Rules — MusicProductionWiki.com
*Built: May 26, 2026 — Session 75*
*Author: Claude (Co-CEO, MPW)*

---

## LOAD ORDER
Read this file every session, after MPW-SESSION-START.md, before any other master document.
If a new never rule is added this session → update this file FIRST. SESSION-START summary updated second. Nowhere else.

---

## ENFORCEMENT KEY
- **SCRIPT** — enforced by `mpw_precommit_check.py` — mechanical, cannot be bypassed
- **MANUAL** — Claude's responsibility — not mechanically enforced

---

## CATEGORY 1: CSS / JS

| Rule | Session Added | Reason | Enforcement |
|------|--------------|--------|-------------|
| Never touch existing CSS style blocks — append only. Inject CSS as a new `<style>` block before `</head>`. Never modify existing style blocks — they contain fingerprint comments and the entire block will be destroyed by any regex targeting them. | S26/S65 | Session 26: two scripts nuked all CSS on both Bible pages by targeting fingerprint strings inside the style block. Every page that has ever had a CSS fix applied contains a giant single style block with fingerprint comments. Regex destroys the entire block. | SCRIPT |
| Never load `style.css` or `../css/style.css` in tool pages. | S68 | The global stylesheet has `.hero::before` and `.hero::after` pseudo-elements that are 600px and 400px radial-gradient circles. They render as massive black blob shapes on tool pages. No working tool in the repo loads `style.css`. Asset path in tools is `../js/main.js` ONLY. | SCRIPT |
| Never use `.hero` or `.container` class names in tool pages. | S68 | These classes are defined in `style.css` with conflicting rules (`padding: 5rem`, radial blob pseudo-elements). Use `.tool-hero` and `.tool-container` or exact CSS from the reference tool. | SCRIPT |
| Never embed Python in HTML/JS — write JS as pure `cat > file.js << 'JSEOF'` heredoc, run `node --check file.js` before embedding. | S67 | Python string operations that touch JS content corrupt it silently. Python `\n` escape sequences become literal newlines inside JS string literals and regex patterns. | SCRIPT |
| Never write JS via Python string interpolation. | S68 | Same root cause as above. Python f-string escaping is incompatible with JS string literals. | SCRIPT |
| Never use `innerHTML` in any tool JS or Bible JS. | S57/S58 | Netlify CSP blocks innerHTML on `/bible/*` and `/tools/*` pages. All DOM manipulation via `createElement`/`appendChild`. | SCRIPT |
| Never use `</script>` as a literal string inside Python tool heredocs. | S57/S58 | It closes the browser's script parser early and breaks all JS on the page. Always use `SC = '</' + 'script>'` and reference `SC` in the string. | MANUAL |
| Never use unicode characters directly in JS strings inside Python f-strings. | S57/S58 | Python f-strings render `\u25b2` as an actual triangle character — use ASCII alternatives (`^`, `v`) or HTML entities instead. Run `re.sub(r'[^\x00-\x7F]', ...)` before output. | MANUAL |
| Never use `setTimeout` for any tool init function call. | S44/S56 | Call all init functions directly at end of each tool's script block. Netlify CSP and DOM readiness require direct calls. | MANUAL |
| Never use CSS inject approach on generator-managed pages. | S63/S64 | `mpw_bible_cat_pages.py --run` regenerates from scratch — CSS injected into live pages is overwritten. All fixes must go in the generator. | MANUAL |
| Never use `Set-Content` or here-strings in PowerShell to create Python scripts that contain CSS values. | S65 | PowerShell mangles backslash-quote sequences in multi-line content. Use a .py file. | MANUAL |
| Never use `replaceState` to fix back-button on article pages. | S65 | `replaceState` is correct for category pages. Article pages need `pushState` + `popstate` — the drawer open adds a fake history entry that the back button consumes. | MANUAL |
| Never use class-only selector for nav color overrides on mpw-nav-homepage-v1 pages. | S65 | `nav.mpw-site-nav .nav-item>a` uses `!important` and beats class-only selectors. Always use `nav.mpw-site-nav .nav-item>a.classname` (child combinator + class). | MANUAL |
| Never use `obs2` / IntersectionObserver in Bible nav JS. | S44 | IntersectionObserver confirmed broken on iPhone for Bible nav. Use scrollIntoView + touchmove listeners only. | MANUAL |
| Never write `ba-cols` or `ba-param-row` grids as inline styles. | S55 | Inline styles override media queries — all grid layouts must use CSS classes or they break mobile. | MANUAL |
| Never declare hero centering complete without verifying every direct child element. | S63/S64 | `text-align:center` on parent does not center all children automatically. | MANUAL |
| Never iterate CSS changes across 8+ commits without a mental render walkthrough first. | S63/S64 | S63 had 8 wasted commits on centering alone. | MANUAL |
| Never use the GitHub web editor for CSS or JS. | S65 | Silent corruption — always fetch via API then edit then commit via API PUT. | MANUAL |
| Never increase category page max-width beyond 1100px. | S63/S64 | Cards become too wide at 1400px — 4-col grid looks blown out. | MANUAL |
| Never use `rel="sponsored"` on free plugin links. | S65 | Google policy violation. Only on paid affiliate links. | MANUAL |
| Never use `onmouseenter` or `onmouseover` alone on interactive elements. | S55 | Touch devices cannot hover — always pair with `ontouchstart`. | MANUAL |
| Never declare a tool mobile-ready without testing on a real iPhone. | S55 | DevTools emulation misses ResizeObserver timing, canvas scale, and iOS Safari clipboard bugs. | MANUAL |
| Never use `ResizeObserver` with `||document.body` fallback. | S65b | Causes "Script error" on mobile Safari before DOM settles. Always observe a named parent container. | MANUAL |
| Never call canvas draw when canvas is inside `display:none`. | S65b | `offsetWidth` returns 0. Draw functions must check active mode before executing. | MANUAL |
| Never hardcode canvas `width` attribute to a fixed pixel value. | S55 | Always read `cv.offsetWidth` at draw time. Fixed attribute width overrides CSS `width:100%`. | MANUAL |
| Never omit `devicePixelRatio` scaling on canvas elements. | S57/S58 | Retina displays show blurry canvas without DPR scaling — always scale by `window.devicePixelRatio||1`. | MANUAL |
| Never use `document.execCommand('copy')` as clipboard fallback. | S65 | Deprecated. The `&&` guard on clipboard API is sufficient. | MANUAL |
| Never inject `MPW_TOOLS_V4_CSS` more than once per page. | S65b | Multiple injections cause class conflicts. Inject once per page in the `<style>` block. | MANUAL |
| Never use bible-bar/slim-bar nav on `/tools/` pages. | S65 | `/tools/` uses mpw-site-nav system, not Bible nav. | MANUAL |
| Never include `<div class="bible-mobile-bar">` in any page template. | S68 | Renders as raw white text — remove from all generators. | MANUAL |
| Never load `style.css` on tool pages — use `main.js` only. | S68 | Duplicate of style.css blob rule. Belt and suspenders. | SCRIPT |

---

## CATEGORY 2: API / PROXY

| Rule | Session Added | Reason | Enforcement |
|------|--------------|--------|-------------|
| Never call Netlify functions via custom domain — always use `classy-haupia-be8e43.netlify.app`. | S67 | `musicproductionwiki.com/.netlify/functions/*` returns 404. The proxy must be called via the Netlify subdomain. | SCRIPT |
| Never use assistant prefill in API calls. | S67 | Returns empty response body. | MANUAL |
| Never use any model except `claude-sonnet-4-6`. | S68 | `claude-sonnet-4-5` and `claude-sonnet-4-20250514` are superseded and incorrect. Using the wrong model string causes API failures or wrong behavior. | SCRIPT |
| Never call direct `api.anthropic.com` from tool pages — always use the Netlify proxy. | S67 | CORS policy blocks direct browser calls to Anthropic API. | MANUAL |
| Never use `fetch()` inside Netlify Functions — use Node's native `https.request()` with `Buffer.from()`. | S67 | `fetch()` is unavailable in older Netlify Function runtimes. | MANUAL |
| Never create AudioContext before a user gesture in Browser Apps. | S65b | Every modern browser blocks AudioContext autoplay until a user gesture occurs. Always gate on click handler. `await Tone.start()` or `audioContext.resume()` inside the click handler only. | MANUAL |
| Never import Tone.js from an unconfirmed version — only `cdnjs.cloudflare.com` version 14.8.49. | S65b | Unconfirmed CDN versions may break the Browser DAW. | MANUAL |
| Never use `curl` for files over ~400KB. | S69 | Shell argument list too long error above ~400KB base64. Use Python `requests` or the GitHub API directly. | MANUAL |

---

## CATEGORY 3: COMMITS

| Rule | Session Added | Reason | Enforcement |
|------|--------------|--------|-------------|
| Never commit without running `mpw_precommit_check.py` first. | S68 | The script catches JS errors, div imbalance, wrong model, style.css loading, and more. It would have prevented every broken deployment in S68. | SCRIPT |
| Never commit multiple files individually — always use GitHub Trees API for a single commit, single Netlify deploy. | S39 | Individual file commits create one deploy per file — burns Netlify build minutes and creates broken intermediate states. | MANUAL |
| Never upload any file to GitHub without scanning for raw tokens first. | S69 | Run `grep -rn 'ghp_\|sk-ant'` on every file before committing. Redact to `[GITHUB_TOKEN]`. GitHub secret scanning blocks the push AND the token may be compromised. | SCRIPT |
| Never delete local HTML files before confirming commit success. | S39 | Files must be confirmed live on GitHub before deletion. | MANUAL |
| Never tell Steve to delete files before confirming commit success. | S39 | Confirm GitHub shows all files live first. | MANUAL |
| Never commit a tool without all 5 required files in the same Trees API commit. | S67 | Orphaned tool pages are unfindable and cause broken site state. The 5 files: tool HTML, tools/index.html card, bible/categories/tools card, sitemap.xml URL, search-index.json entry. | MANUAL |
| Never commit the full batch before the test article has all issues resolved. | S65 | S65 iterated 4 times on test article before batch ran — correct procedure. One test article confirmed on live site before any batch. | MANUAL |
| Never run article nav batches by fetching one article and assuming all match. | S65 | The `\u00a0` non-breaking space after the bullet in `mob-bible` was only discovered by printing exact repr() of live file. Always confirm exact bytes. | MANUAL |
| Never skip sitemap or search-index.json after a tool build. | S67 | Every tool needs sitemap URL and search-index.json entry — omitting them leaves tools unfindable. | MANUAL |
| Never commit an article with garbled share buttons. | S51 | Must render cleanly before commit. | MANUAL |
| Never commit a Bible entry that has not passed all 6 checks. | S52 | Six-check QA is mandatory before any Bible entry goes live. | MANUAL |
| Never commit a tool page without confirming dispatch returns real content. | S68 | `len(tool_html) > 100` is not sufficient — open the live page. Placeholder content was committed and called "working" in S68. | MANUAL |
| Never present files for approval and then commit without waiting for explicit "go" from Steve. | S71 | Present ALL files, write the approval block, stop completely — no commits, no tool calls, nothing until Steve responds. Committing without approval = session failure. | MANUAL |
| Never run a nav update script without `--test` on 3 articles first. | S51 | Verify visually before full batch. | MANUAL |

---

## CATEGORY 4: CONTENT / ARTICLES

| Rule | Session Added | Reason | Enforcement |
|------|--------------|--------|-------------|
| Never invent slugs — verify against GitHub tree API before writing any links. | S26/S65 | Invented slugs cause broken internal links. Always query `https://api.github.com/repos/musicproductionwiki/musicproductionwiki/git/trees/main?recursive=1` to confirm real slugs. | MANUAL |
| Never propose article topics without duplicate check against MPW-CATALOG.md. | S39 | Duplicate articles waste a session slot and create SEO cannibalization. | MANUAL |
| Never update index.html or sitemap for rewrites of existing filenames. | S51 | Only net new articles need sitemap/index updates — rewrites use the same URL. | MANUAL |
| Never deliver articles under minimum word count. | S39 | See MPW-HANDOFF-CONTENT.md for counts by category. Reviews 3,200–3,500w. Comparisons 3,300–3,500w. Techniques 4,000–4,200w. Roundups 3,500–3,800w. | MANUAL |
| Never use "Updated May 2025" or any 2025 date in articles. | S39 | Always current year (2026). | MANUAL |
| Never write partial article batches — all articles first, commit once. | S39 | Partial commits create broken intermediate states. | MANUAL |
| Never zip article batches over 200KB. | S26 | Cloudflare intercepts — save via Notepad → Save As → All Files to avoid interception. | MANUAL |
| Never change a review score between runs. | S39 | Extract from existing article and lock — score changes are editorial decisions requiring Steve approval. | MANUAL |
| Never regenerate category pages without fixing Bible bar CSS first. | S51 | Must be centered — copy exact CSS from index.html. | MANUAL |
| Never build category pages without fetching live GitHub article slug list first. | S51 | Invented slugs cause broken links. | MANUAL |
| Never use a text logo on any page. | S39 | All pages must use SVG logo-mark. | MANUAL |
| Never run the article quality audit blind. | S51 | Write `mpw_audit.py`, run `--dry-run`, review CSV before acting. | MANUAL |
| Never rewrite an article without first checking `mpw_audit.py` output. | S51 | Audit tells you rewrite vs targeted fix. | MANUAL |
| Never let Claude auto-detect article category without checking the result. | S51 | Always confirm `[CATEGORY]` line in output. | MANUAL |
| Never build new tools without studying every v3 tool body in full. | S60 | Quality gap between v3 and v4 was caused by not internalizing v3 tool depth before writing v4. | MANUAL |
| Never use tracking pixels or third-party JS until Mediavine milestone. | S55 | Infrastructure cost must be funded by existing revenue streams first. | MANUAL |
| Never paywall session-critical calculation tools. | S65 | Free forever. Email gate is for exportable documents only. Never on calculators. | MANUAL |
| Never propose RunPod products until affiliate revenue is confirmed. | S66 | Infrastructure cost must be funded by existing revenue streams first. | MANUAL |

---

## CATEGORY 5: BIBLE

| Rule | Session Added | Reason | Enforcement |
|------|--------------|--------|-------------|
| Never use `/dictionary/` as the Bible URL structure. | S26 | URL structure is `/bible/[term]`. `/dictionary/` was an early candidate — rejected. | MANUAL |
| Never fabricate producer quotes. | S32 | Exactly 3 producer quotes from `quotes.json` per entry. Never invent. | MANUAL |
| Never set read time below 650 wpm for Bible entries. | S63/S64 | 500 wpm confirmed wrong — 650 wpm is the standard. `read_time = round(word_count / 650)`. | SCRIPT |
| Never run `mpw_bible_writer.py` for new T1 entries before updating read time to 650 wpm. | S63 | Produces inflated read times on all new entries. Blocks T1 batch until fixed. | MANUAL |
| Never run old `install_bible_writer_v52_part*.ps1` scripts. | S60 | They write the unfixed writer — will break the tool. | MANUAL |
| Never use single-quoted JS strings in LTIPS. | S46 | Apostrophes in tip text break JS parser — always double-quoted. | MANUAL |
| Never append `{tools_html}` in f-string AND use `TOOLS_PLACEHOLDER` replacement. | S51 | Causes duplicate tool sections. Use `TOOLS_PLACEHOLDER` only. | MANUAL |
| Never emit stray `""` after `</script>` in Python tool heredocs. | S52 | Stray string between `</script>` and closing triple-quote leaks into HTML and kills all JS. | MANUAL |
| Never approach plugin companies as advertorial. | S60 | Editorial partnership is not advertising — picks remain independent, partnerships disclosed. | MANUAL |
| Never build Genre Bible entries without confirming BPM/key data against actual tracks. | S60 | Genre conventions must reflect real production data, not assumptions. | MANUAL |
| Never start a new content type writer before the current batch is confirmed running. | S60 | Build sequence is sequential: v5.3 T1/T2/T3 first, then Genre Bible, then Producer DNA. | MANUAL |
| Never invent producer signal chains or track production details. | S60 | All must be sourced from verified interviews, confirmed gear lists, or widely confirmed production lore. | MANUAL |
| Never count dropdown-plus-text-output as an "interactive tool." | S60 | A tool is interactive when output changes in real time with visual feedback. Every tool must do arithmetic. | MANUAL |
| Never deliver Bible tools that only look up, not compute. | S60 | Every tool must do arithmetic — BPM calculations, dB formulas, Hz conversions, room acoustics math. | MANUAL |
| Never fix generator-managed pages with CSS injection. | S63/S64 | `mpw_bible_cat_pages.py --run` regenerates from scratch — injected patches are lost on every run. | MANUAL |
| Never deliver `mpw_bible_cat_pages.py` without zero-mismatch SUBCAT_MAP verification. | S63/S64 | 62 mismatches in first S63 version caused wrong filter counts. | MANUAL |
| Never commit all 11 category pages without verifying at least one on the live site first. | S63 | `--run` commits all 11 in one Trees API call — if template is wrong, all 11 are broken at once. | MANUAL |
| Never close the `entry-main` div before the `aside` tag. | S51 | Causes layout collapse on Bible entry pages. | MANUAL |
| Never add `display:block!important` to the Bible `aside` inline style. | S51 | Mobile CSS cannot override inline `!important`. | MANUAL |
| Never use main.js on Bible pages. | S51 | Article pages use `main.js`. Bible pages do NOT. Never mix. | MANUAL |
| Never restore `mpw_bible_writer.py` from GitHub. | S51 | The repo contains an old v4.0 version. Always use the local `mpw-scripts\` copy. | MANUAL |

---

## CATEGORY 6: TOOLS

| Rule | Session Added | Reason | Enforcement |
|------|--------------|--------|-------------|
| Never start a tool build or rebuild without reading `MPW-TOOL-BUILD-SPEC.md` first. | S66/S68 | The frozen spec defines the correct design system, component classes, fonts, colors, and build checklist. Not reading it caused full wasted rebuilds with the wrong design system in S68. | MANUAL |
| Never commit a tool without adding its card to `/tools/index.html` in the same commit. | S66 | Orphaned tool pages with no hub entry are unfindable from the site. | MANUAL |
| Never skip the quality checklist before committing any tool. | S66 | FAQPage schema, canonical, OG tags, MPW nav, mobile responsive, pushState — all required. | MANUAL |
| Never build the Browser DAW as part of a multi-tool batch session. | S65b/S66 | Requires 2–3 dedicated sessions. Mixing it with tool batches kills quality on both. | MANUAL |
| Never build chunk files for tool Python modules. | S56 | Assembling `tools_1_4.py + tools_5_8.py` etc. is fragile — write the complete file as a single coherent script. | MANUAL |
| Never use `print()` at module level in any `mpw_tools_v*.py`. | S56 | `print("Tools 1-4 OK")` executes on every import. All print statements inside `if __name__ == '__main__'`. | MANUAL |
| Never test tools on `file://` protocol. | S56 | Clipboard API and CSP restrictions differ from Netlify. Always test on live Netlify or via `make_preview.py` on a local server. | MANUAL |
| Never run `python -c` with multi-line scripts in PowerShell. | S56 | PowerShell mangles quotes and backslashes in multi-line `-c` strings. Use a `.py` file. | MANUAL |
| Never declare a tool live without Steve visually confirming the live page. | S63/S64 | Multiple commits were declared done but wrong on live site. | MANUAL |
| Never hardcode plugin names or affiliate links in tool HTML — reference `mpw_affiliates.py`. | S65 | Affiliate links must be centrally managed for easy updates. | MANUAL |
| Never build `generate_tools_hub.py`. | S63 | `tools/index.html` was hand-crafted — a generator is not needed and would add unnecessary complexity. | MANUAL |
| Never omit favicon link tags in any tool head. | S67 | `<link rel="icon" type="image/svg+xml" href="/favicon.svg">` in every tool head. | SCRIPT |
| Never insert HTML cards without verifying position is INSIDE the target div. | S67/S68 | Confirm `grid_open < insert_pos < grid_close` before any card insertion. | MANUAL |
| Never build AI music tools without verifying current DDEX disclosure requirements. | S65b | Requirements enforced by Spotify/Apple are changing — verify current policies before tool goes live. | MANUAL |
| Never build tools that write literal `</script>` in Python strings — always use `SC = '</' + 'script>'`. | S57/S58 | Duplicate of JS rule — critical enough to list in Tools category too. | MANUAL |
| Never put tool preview HTML inside a zip for Cloudflare delivery. | S57/S58 | Cloudflare intercepts — use separate file opens or base64 PS1 delivery. | MANUAL |
| Never ask Steve to run PowerShell to fetch GitHub files Claude can fetch directly with the token. | S68 | Token is always available in session — use it. | MANUAL |
| Never declare tool pages live without visual confirmation of rendered content. | S68 | Placeholder block was committed and declared working in S68. It was not. | MANUAL |
| Never modify `make_footer()` or major tool functions without verifying `TOOL_PAGE_CSS` still exists in the file after edit. | S68 | Accidentally deleted during refactor — caused 36/36 FAIL. | MANUAL |
| Never build `mpw_tools_v6_writer.py` without reading `mpw_tools_master_spec.md` first. | S65 | Spec defines the full tool architecture. Starting without it causes full rebuilds. | MANUAL |
| Never use `replaceState` in mobile drawer JS. | S66 | Use `pushState` + `popstate` — `replaceState` breaks back-button behavior. | MANUAL |

---

## CATEGORY 7: GENERAL / SYSTEM

| Rule | Session Added | Reason | Enforcement |
|------|--------------|--------|-------------|
| Never enable Netlify Pretty URLs. | S26 | Breaks the site. | MANUAL |
| Never truncate any handoff document. | S26 | Truncation destroys session continuity and can permanently corrupt project state. If running low on context, warn Steve and stop. | MANUAL |
| Never rewrite suno-vs-udio.html. | S39 | It is the article gold standard — LOCKED. Do not touch it. | MANUAL |
| Never build a new nav patch script when the existing one can be fixed. | S51 | Avoid script pile-up. | MANUAL |
| Never declare audit results reliable without visual confirmation. | S51 | String matching is not sufficient. | MANUAL |
| Never run injection scripts blind — always `--test` on 3 articles first. | S39 | Confirm exact bytes before any batch commit. | MANUAL |
| Never assume a script produced the correct result. | S51 | Always check the live page. | MANUAL |
| Never run batches 09–13 before new category pages exist. | S60 | `breakdowns.html` LIVE. `recreations.html` + `vocal-autopsies.html` must exist first. | MANUAL |
| Never start Producer's Bible entries before the entry template is approved. | S32 | Gold standard entry must be confirmed first. | MANUAL |
| Never use JS-only dropdowns. | S39 | Use CSS `:focus-within`. | MANUAL |
| Never use `print()` at module level in any script. | S56 | Executes on every import — confirmed annoying. All diagnostic prints inside `if __name__ == '__main__'`. | MANUAL |
| Never use the Beehiiv iframe embed method. | S63/S64 | Use v3 loader script in head + `data-beehiiv-form` div in body. | MANUAL |
| Never use `replaceState` on article pages for back-button. | S65 | Correct for category pages only. Article pages require `pushState` + `popstate`. | MANUAL |
| Never deliver a script with ambiguous naming when multiple versions are in flight. | S63 | S63 had 6 versions (s63 through s63f) — always use clearly incremented names. | MANUAL |
| Never leave raw tokens in any file committed to GitHub. | S68 | Run `grep -rn 'ghp_\|sk-ant'` before every commit. GitHub secret scanning blocks the push AND may compromise the token. | SCRIPT |
| Never use `../css/style.css` on pages in `/tools/` — use absolute `/css/style.css`. | S68 | Relative path breaks at `/tools/` depth. | SCRIPT |
| Never build SITE_HEADER without confirming all CSS classes are defined inline. | S68 | Nav rendered as unstyled bullet text when classes existed in HTML but not in CSS. | MANUAL |
| Never use `mpw_writer.py` for new article batches before applying all 4 pending nav/drawer updates. | S63 | Current writer outputs old vertical list drawer — new grid style must be in writer before next batch. | MANUAL |
| Never run `mpw_bible_writer.py` before updating read time to 650 wpm + new nav. | S63/S65/S66 | Blocks Bible batch — update before next T1 batch. | MANUAL |
| Never hardcode GitHub token in any file — store in `setenv.ps1` only. | S26 | Token expires Aug 2, 2026. Hardcoded tokens get caught by GitHub secret scanning. | SCRIPT |
| Never extract nav block with naive `find()` — use div-depth tracking to guarantee balance. | S68 | Naive find breaks on nested divs — div-depth tracking guarantees balanced extraction. | MANUAL |

---

## MASTER COUNTS (Session 75)
Total rules documented: 95
SCRIPT-ENFORCED: 14
MANUAL: 81

---

## SESSION END PROTOCOL (Permanent from S75)
If a new never rule is identified this session:
1. Add it to this file in the correct category before presenting any files for approval
2. Update SESSION-START summary table (top 20) second
3. Nowhere else

