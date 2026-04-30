# MusicProductionWiki.com

A professional music production reference wiki — free, independent, and built for producers at every level.

## 📁 Project Structure

```
musicproductionwiki/
├── index.html                    ← Homepage
├── css/
│   └── style.css                 ← All styles (single file, no build step)
├── js/
│   └── main.js                   ← All interactivity (vanilla JS)
├── articles/
│   └── sidechain-compression-guide.html   ← Article template (duplicate to create new articles)
└── categories/
    ├── daws.html
    ├── plugins.html
    ├── gear.html
    ├── techniques.html
    ├── music-business.html
    └── glossary.html
```

## 🚀 Quick Deploy

### GitHub Pages
1. Push this repository to GitHub
2. Go to **Settings → Pages**
3. Set source to `main` branch, `/ (root)` folder
4. Your site will be live at `https://yourusername.github.io/musicproductionwiki/`

### Custom Domain (musicproductionwiki.com)
1. Add a `CNAME` file to the root with content: `musicproductionwiki.com`
2. Configure your domain's DNS:
   - Add an `A` record pointing to GitHub Pages IPs:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
   - Or add a `CNAME` record: `www` → `yourusername.github.io`
3. Enable "Enforce HTTPS" in GitHub Pages settings

### Netlify / Vercel
Simply drag and drop this folder into Netlify Drop, or connect your GitHub repository. No build step required.

## ✏️ Adding New Articles

1. Copy `articles/sidechain-compression-guide.html` to a new file
2. Update:
   - `<title>` and `<meta name="description">`
   - Breadcrumb text
   - Article header (tags, h1, date, read time)
   - Article body content
   - TOC sidebar links
   - Related articles section
3. Update relative paths if needed (`../css/style.css`, `../js/main.js`)

## ✏️ Adding New Category Pages

1. Copy any file in `categories/`
2. Update the category header, filter tags, and article list
3. Add a link to the new category in `index.html` and all nav menus

## 🎨 Design System

### Colors (CSS variables in `style.css`)
| Variable | Value | Use |
|---|---|---|
| `--ink` | `#0f0e0d` | Primary text, dark backgrounds |
| `--paper` | `#faf8f5` | Page background |
| `--accent` | `#c8401a` | Links, CTAs, active states |
| `--teal` | `#1a6b6b` | Secondary accent |
| `--gold` | `#b8860b` | Tertiary accent |

### Typography
- **Display**: DM Serif Display (headings, pull quotes)
- **Body**: DM Sans (all body text)
- **Mono**: DM Mono (code, terms)

All fonts loaded from Google Fonts.

### Key Components
- `.article-card` — Card-style article preview
- `.article-list-item` — Row-style article listing
- `.sidebar-widget` — Sidebar panel
- `.category-card` — Homepage category grid card
- `.newsletter-section` — Dark full-width newsletter CTA
- `.article-layout` — Two-column article + sidebar grid
- `.category-layout` — Two-column category + sidebar grid

## 📰 Newsletter

The newsletter signup is wired to a simple JavaScript handler in `main.js` that simulates subscription. To connect to a real email service:

1. Replace the `newsletter-form-js` submit handler in `js/main.js` with your actual API call
2. Popular options: Mailchimp, ConvertKit, Buttondown, Beehiiv

## 📱 Responsive Breakpoints

| Breakpoint | Layout changes |
|---|---|
| `< 1024px` | Category grid → 2 columns; sidebar moves below |
| `< 768px` | All grids → single column; mobile nav activates |
| `< 480px` | Hero actions stack; subscribe button hidden |

## 📄 License

Content © MusicProductionWiki.com. All rights reserved.

Design and code are free to adapt for your own projects.

---

**The Music Production Wiki Team**
