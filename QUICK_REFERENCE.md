# Quick Reference: WordPress to GitHub Pages

## 🚀 Quick Start

1. **Run the script**: `python fix_paths_for_github_pages.py [directory]`
2. **Test locally**: Open `index.html` in browser
3. **Upload to GitHub**: Push files to repository
4. **Enable Pages**: Settings → Pages → Deploy from branch

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