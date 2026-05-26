---

# SESSION 67 UPDATE — SCRIPTS — May 25, 2026

## Tool Commit Pattern — Trees API (Required for Every Tool)

```python
import requests, base64, json

TOKEN = "[GITHUB_TOKEN]"
HEADERS = {"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
BASE = "https://api.github.com/repos/musicproductionwiki/musicproductionwiki"

def get_file(path):
    r = requests.get(f"{BASE}/contents/{path}", headers=HEADERS).json()
    return base64.b64decode(r['content']).decode('utf-8')

def commit_files(files_dict, message):
    main_sha = requests.get(f"{BASE}/git/refs/heads/main", headers=HEADERS).json()['object']['sha']
    new_tree = []
    for path, content in files_dict.items():
        blob = requests.post(f"{BASE}/git/blobs", headers=HEADERS, json={
            "content": base64.b64encode(content.encode('utf-8')).decode('ascii'),
            "encoding": "base64"
        }).json()['sha']
        new_tree.append({"path": path, "mode": "100644", "type": "blob", "sha": blob})
    tree_sha = requests.post(f"{BASE}/git/trees", headers=HEADERS, json={
        "base_tree": main_sha, "tree": new_tree
    }).json()['sha']
    commit_sha = requests.post(f"{BASE}/git/commits", headers=HEADERS, json={
        "message": message, "tree": tree_sha, "parents": [main_sha]
    }).json()['sha']
    r = requests.patch(f"{BASE}/git/refs/heads/main", headers=HEADERS, json={"sha": commit_sha})
    print(f"✅ {r.status_code} — {commit_sha}")
    return commit_sha
```

---

## Full Tool Deployment Sequence

For every new tool, in order:

### Step 1 — Build the HTML
- Follow MPW-TOOL-BUILD-SPEC.md design system
- Use `claude-sonnet-4-5` model
- Call `https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy`
- Include favicon, MPW nav, site footer, embed mode, all SEO

### Step 2 — Update tools/index.html
```python
idx = get_file('tools/index.html')
new_card = '''
    <a class="tool-card" href="/tools/[slug].html" data-cat="ai-music" data-name="[searchable terms]">
      <div class="tool-card-body">
        <span class="tool-card-name">[Tool Name]</span>
        <span class="tool-card-desc">[One sentence, 12 words max]</span>
        <span class="tool-card-cat">AI Music</span>
      </div>
      <span class="tool-card-arrow">&rarr;</span>
    </a>'''
# Insert before <!-- no-results placeholder --> or at end of grid
# Update count: '38 free music production tools' → '39 free...'
```

### Step 3 — Update bible/categories/tools/index.html
```python
btools = get_file('bible/categories/tools/index.html')
new_card = '<a class="bcat-card" href="/tools/[slug].html"><div class="bcat-card-inner"><span class="bcat-card-term">[Tool Name]</span><span class="bcat-card-cat">AI Music</span></div><span class="bcat-card-arrow">→</span></a>'

# CRITICAL: Insert INSIDE #catGrid, BEFORE closing </div>
close_pattern = '→</span></a>\n  </div>\n  <div class="bcat-empty"'
insert_point = btools.rfind(close_pattern) + len('→</span></a>')
btools = btools[:insert_point] + '\n' + new_card + btools[insert_point:]

# Verify: grid_open < new_card_pos < catEmpty_pos
grid_open = btools.find('id="catGrid">')
card_pos = btools.find('/tools/[slug].html')
empty_pos = btools.find('id="catEmpty"')
assert grid_open < card_pos < empty_pos, "Card not inside grid!"
```

### Step 4 — Update sitemap.xml
```python
import re
from datetime import date
sitemap = get_file('sitemap.xml')
new_url = f'  <url><loc>https://www.musicproductionwiki.com/tools/[slug].html</loc><lastmod>{date.today().isoformat()}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
sitemap = sitemap.replace('</urlset>', new_url + '\n</urlset>')
```

### Step 5 — Update search-index.json
```python
si = json.loads(get_file('search-index.json'))
si.append({
    "slug": "tools/[slug]",
    "title": "[Tool Name]",
    "category": "Tools",
    "description": "[One sentence description for search results]"
})
```

### Step 6 — Commit all 5 files in one Trees API commit
```python
commit_files({
    'tools/[slug].html': tool_html,
    'tools/index.html': idx,
    'bible/categories/tools/index.html': btools,
    'sitemap.xml': sitemap,
    'search-index.json': json.dumps(si, ensure_ascii=False),
}, "tools: add [Tool Name] — fully mapped to hub, bible, sitemap, search")
```

---

## Sitemap Pending
Two URLs added this session — Steve to submit in GSC:
- `https://www.musicproductionwiki.com/tools/suno-prompt-optimizer.html`
- `https://www.musicproductionwiki.com/tools/ai-music-rights-navigator.html`

---

## NEVER Rules — Session 67 — Scripts

| Rule | Detail |
|------|--------|
| NEVER commit a tool without all 5 files in same commit | Tool + tools/index.html + bible/categories/tools + sitemap.xml + search-index.json |
| NEVER insert into catGrid without assertion check | grid_open < card_pos < empty_pos — assert it |
| NEVER skip sitemap after tool build | Tools are not indexable without sitemap entry |
| NEVER forget search-index.json | Site search won't find the tool without it |

