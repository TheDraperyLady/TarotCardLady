# WordPress Static Site - GitHub Pages Ready

This is a WordPress site that has been exported to static HTML/CSS/JS files and is now ready for deployment on GitHub Pages.

## What Was Fixed

The original WordPress export used absolute paths (starting with `/`) for all CSS, JavaScript, and image files. While these work fine when serving from the root directory (like with `python -m http.server`), they fail on GitHub Pages because it serves your site from a subdirectory (your repository name).

### Changes Made

All absolute paths have been converted to relative paths:

- `href="/wp-content/themes/..."` → `href="wp-content/themes/..."`
- `src="/wp-includes/js/..."` → `src="wp-includes/js/..."`
- `href="/wp-content/uploads/..."` → `href="wp-content/uploads/..."`
- `href="/"` → `href="./"`

## Deployment

1. Upload all files to a GitHub repository
2. Go to repository Settings → Pages
3. Select "Deploy from a branch" and choose your main branch

## File Structure

```
├── index.html                    # Main page
├── wp-content/                   # WordPress content
│   ├── themes/                   # Theme files
│   ├── plugins/                  # Plugin files (Elementor, etc.)
│   └── uploads/                  # Uploaded media
├── wp-includes/                  # WordPress core files
└── README.md                     # This file
```

## Testing Locally

You can test the site locally using:

```bash
python -m http.server
```

Then visit `http://localhost:8000` in your browser.

## Notes

- WordPress API endpoints (`/wp-json/`, `/xmlrpc.php`) have been converted to relative paths but won't function on a static site
- All styles and JavaScript should now load correctly on GitHub Pages
- The site is fully static and doesn't require a web server or database 