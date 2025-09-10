# Tarot Card Lady - GitHub Pages Deployment

This repository contains a static website for Tarot Card Lady that has been optimized for GitHub Pages deployment.

## 🚀 Quick Start

1. **Run the script**: `python fix_paths_for_github_pages.py [directory]`
2. **Test locally**: Open `index.html` in browser
3. **Upload to GitHub**: Push files to repository
4. **Enable Pages**: Settings → Pages → Deploy from branch

## 📁 File Structure

```
your-site/
├── index.html
├── wp-content/
│   ├── themes/
│   ├── plugins/
│   └── uploads/
├── wp-includes/
│   └── js/
└── README.md
```

### Key Files
- `index.html` - Main website file
- `wp-content/` - Contains all CSS, JavaScript, images, and fonts
- `wp-includes/` - Contains jQuery and other dependencies
- `.nojekyll` - Ensures GitHub Pages serves all files

## 🔧 Path Conversions

| Find | Replace |
|------|---------|
| `href="/wp-content/` | `href="wp-content/` |
| `src="/wp-includes/` | `src="wp-includes/` |
| `src="/wp-content/uploads/` | `src="wp-content/uploads/` |
| `href="/wp-content/uploads/` | `href="wp-content/uploads/` |
| `content="/wp-content/uploads/` | `content="wp-content/uploads/` |
| `href="/wp-json/` | `href="wp-json/` |
| `href="/"` | `href="./"` |

## 🎨 Custom Fonts

The site uses custom fonts:
- **Britannic Bold** - For headings
- **Gilroy** - For body text (multiple weights: Light, Regular, Medium, Bold)

All font files are included in `wp-content/uploads/2025/05/`.

## 📝 Contact Form

The contact form uses Formkeep for handling submissions.

## ✅ Testing Checklist

- [ ] Homepage loads
- [ ] CSS styles work
- [ ] JavaScript functions
- [ ] Images display
- [ ] Navigation works
- [ ] Mobile responsive
- [ ] Favicon shows

## 🐛 Common Issues

**Images not loading**: Check `src` paths  
**CSS not working**: Check `href` paths  
**JS errors**: Check `src` paths  
**Links broken**: Check `href="/"` → `href="./"`

## 🔗 Your Site URL

`https://[username].github.io/[repository-name]/`

## 📋 Notes

- All file paths have been converted to relative paths for GitHub Pages compatibility
- The `.nojekyll` file ensures GitHub Pages serves all files including those starting with underscore
- CSS and JavaScript files are optimized and minified
