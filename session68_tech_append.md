---

# SESSION 68 UPDATE — TECH — May 26, 2026

## Critical Technical Lessons

### 1. Python-in-JS Causes Silent Syntax Errors

**Root cause:** Writing JS via Python string interpolation in heredocs.

**Example of what broke:**
```python
# This looks fine in Python but writes broken JS
sys_prompt = f"SCORE: [1-10]\nGENRE_SCORE: [0-10]"
# Writes literal newline into JS string → SyntaxError
```

**Correct pattern — always:**
```bash
# Write JS as pure heredoc
cat > /home/claude/tool_js.js << 'JSEOF'
var sys = 'SCORE: [1-10]\nGENRE_SCORE: [0-10]';  // \n is a real escape here
JSEOF
# Verify syntax
node --check /home/claude/tool_js.js && echo "OK"
# Read into HTML as raw bytes — never as Python string
```

**The rule:** Python never touches JS content. Write JS → check JS → read as bytes → embed.

---

### 2. Nav Div Balance — Use Depth Tracking

**Root cause:** Extracting nav block with `find('</div>', mob_end)` truncated mid-drawer.

**Broken pattern:**
```python
nav_end = html.find('</div>', mob_drawer_end)
nav_block = html[nav_start:nav_end + 6]  # Wrong — grabs first </div> after drawer
```

**Correct pattern:**
```python
# Track div depth to get perfectly balanced block
depth = 0
pos = nav_start
while pos < len(html):
    open_m = html.find('<div', pos)
    close_m = html.find('</div>', pos)
    if open_m == -1: open_m = len(html)
    if close_m == -1: close_m = len(html)
    if open_m < close_m:
        depth += 1; pos = open_m + 4
    else:
        depth -= 1; pos = close_m + 6
        if depth == 0: break
nav_block = html[nav_start:pos]
# Verify: nav_block.count('<div') == nav_block.count('</div>')
```

---

### 3. style.css Cannot Be Loaded on Tool Pages

**Why:** `style.css` defines `.hero::before` (600px circle) and `.hero::after` (400px circle) as massive black radial-gradient blobs. These render as giant black shapes that push tool content hundreds of pixels down.

**What the working tools do:** They load `main.js` only. The nav renders because `main.js` provides JS behavior (dropdown toggle, mobile drawer), and the nav's visual CSS is provided via the browser's cached `style.css` from other site pages OR the 4 nav specificity lines in the tool's own `<style>` block are sufficient for the nav's layout (since nav layout CSS is in `main.js`'s injected styles).

**Rule:** Never add `<link rel="stylesheet" href="/css/style.css">` or `<link rel="stylesheet" href="../css/style.css">` to tool pages.

---

### 4. Class Name Conflicts With Global CSS

Classes to NEVER use in tool pages (defined in `style.css` with conflicting rules):
- `.hero` — has `::before`/`::after` 600px/400px blobs, `padding: 5rem 0 4rem`
- `.container` — has `max-width: var(--max-w)`, `overflow-x: hidden`
- `.newsletter-section` — has 700px blob
- `.category-header` — has 400px blob
- `.hero-lines` — has full-viewport background-image

**Safe alternatives:** `.tool-hero`, `.tool-container`, or any unique prefixed class.

---

### 5. File Assembly for Large HTML Tools

**Working pattern (no Python interpolation touching JS):**

```python
# 1. Write JS as pure heredoc — node --check it
# 2. Write HTML sections as Python writes (ok for HTML strings)
# 3. Assemble by reading files as raw bytes

with open('/home/claude/final_tool.html', 'wb') as out:
    for section in ['head.html', 'css.html', 'body.html']:
        with open(f'/home/claude/{section}', 'rb') as f:
            out.write(f.read())
    # JS file — read as raw bytes, never as Python string
    with open('/home/claude/tool.js', 'rb') as f:
        out.write(b'\n<script>\n')
        out.write(f.read())
        out.write(b'\n</script>\n</body>\n</html>')
```

---

### 6. Pre-Commit Verification Checklist for Tool Pages

Run before every commit:

```python
import re, subprocess

with open('tool.html') as f: html = f.read()

# Div balance
assert html.count('<div') == html.count('</div>'), "Unbalanced divs"

# No style.css
assert 'style.css' not in html, "style.css must not be loaded"

# No bare .hero or .container (use .tool-hero, .tool-container)
# (only if using global class workaround)

# JS syntax check — extract each <script> block and node --check it
scripts = re.findall(r'<script(?![\s\S]{0,10}(?:async|ld\+json|src=))[^>]*>([\s\S]+?)</script>', html)
for i, s in enumerate(scripts):
    with open(f'/tmp/check_{i}.js','w') as f: f.write(s)
    r = subprocess.run(['node','--check',f'/tmp/check_{i}.js'], capture_output=True, text=True)
    assert r.returncode == 0, f"Script {i} syntax error: {r.stderr}"

# Model string
assert 'claude-sonnet-4-6' in html, "Wrong model"

# Proxy URL
assert 'classy-haupia-be8e43' in html, "Wrong proxy"

print("ALL CHECKS PASSED")
```

