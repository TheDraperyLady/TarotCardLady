# Tarot Card Lady - GitHub Pages Deployment

This repository contains a static website for Tarot Card Lady that has been optimized for GitHub Pages deployment.

## Files Structure
- `index.html` - Main website file
- `wp-content/` - Contains all CSS, JavaScript, images, and fonts
- `wp-includes/` - Contains jQuery and other dependencies
- `.nojekyll` - Ensures GitHub Pages serves all files

## Custom Fonts
The site uses custom fonts:
- **Britannic Bold** - For headings
- **Gilroy** - For body text (multiple weights: Light, Regular, Medium, Bold)

All font files are included in `wp-content/uploads/2025/05/`.

## Contact Form
The contact form uses Formspree.io for handling submissions. No additional setup required.

## Notes
- All file paths have been converted to relative paths for GitHub Pages compatibility
- The `.nojekyll` file ensures GitHub Pages serves all files including those starting with underscore
- CSS and JavaScript files are optimized and minified
