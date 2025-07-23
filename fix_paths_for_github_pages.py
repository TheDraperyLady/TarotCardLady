#!/usr/bin/env python3
"""
WordPress to GitHub Pages Path Fixer

This script converts absolute paths in a WordPress static export to relative paths
so the site can be deployed on GitHub Pages.

Usage:
    python fix_paths_for_github_pages.py [directory]

If no directory is specified, it will process the current directory.
"""

import os
import re
import sys
import glob
from pathlib import Path

def fix_paths_in_file(file_path):
    """Fix paths in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix CSS href paths
        content = re.sub(r'href="/wp-content/', 'href="wp-content/', content)
        
        # Fix JavaScript src paths
        content = re.sub(r'src="/wp-includes/', 'src="wp-includes/', content)
        
        # Fix image src paths
        content = re.sub(r'src="/wp-content/uploads/', 'src="wp-content/uploads/', content)
        
        # Fix favicon href paths
        content = re.sub(r'href="/wp-content/uploads/', 'href="wp-content/uploads/', content)
        
        # Fix meta content paths (for favicons, etc.)
        content = re.sub(r'content="/wp-content/uploads/', 'content="wp-content/uploads/', content)
        
        # Fix wp-json href paths
        content = re.sub(r'href="/wp-json/', 'href="wp-json/', content)
        
        # Fix homepage links
        content = re.sub(r'href="/"', 'href="./"', content)
        
        # Fix canonical and shortlink URLs
        content = re.sub(r'href="/"', 'href="./"', content)
        
        # Fix any remaining absolute paths that might be missed
        content = re.sub(r'href="/wp-content/', 'href="wp-content/', content)
        content = re.sub(r'src="/wp-content/', 'src="wp-content/', content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all HTML files."""
    # Get directory from command line or use current directory
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "."
    
    directory = Path(directory)
    
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)
    
    print(f"Processing directory: {directory.absolute()}")
    
    # Find all HTML files
    html_files = list(directory.rglob("*.html"))
    
    if not html_files:
        print("No HTML files found.")
        return
    
    print(f"Found {len(html_files)} HTML files to process.")
    
    modified_count = 0
    
    for html_file in html_files:
        print(f"Processing: {html_file}")
        if fix_paths_in_file(html_file):
            modified_count += 1
            print(f"  ✓ Modified")
        else:
            print(f"  - No changes needed")
    
    print(f"\nSummary:")
    print(f"  Total files processed: {len(html_files)}")
    print(f"  Files modified: {modified_count}")
    print(f"  Files unchanged: {len(html_files) - modified_count}")
    
    if modified_count > 0:
        print(f"\n✅ Successfully converted {modified_count} files for GitHub Pages deployment!")
        print(f"\nNext steps:")
        print(f"  1. Test your site locally by opening index.html in a browser")
        print(f"  2. Push your files to a GitHub repository")
        print(f"  3. Enable GitHub Pages in your repository settings")
        print(f"  4. Your site will be available at: https://[username].github.io/[repository-name]/")
    else:
        print(f"\nℹ️  No files needed modification. Your site may already be GitHub Pages ready.")

if __name__ == "__main__":
    main() 