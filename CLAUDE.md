# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo-based static site for an accounting services business using TailwindCSS for styling. The site features:
- Professional accounting services landing page
- Custom TailwindCSS theme with brand colors
- SEO optimization with structured data
- Google Tag Manager integration

## Common Commands

### Development
- `npm run dev` - Start development with CSS watching
- `npm run watch:css` - Watch and compile TailwindCSS files

### Building
- `npm run build:css` - Compile CSS for production
- `npm run build` - Full production build (CSS + Hugo with minification)
- `hugo` - Build site (requires Hugo CLI)
- `hugo server` - Serve locally with live reload

### Image Optimization
- `npm run optimize:images` - Optimize all images (resize + compress)
- `npm run optimize:images:preview` - Preview what would be optimized (dry-run)
- `npm run optimize:images:restore` - Restore original images from backup
- `npm run optimize:images:verbose` - Run with detailed logging

**Image Optimization Details:**
- Uses `sharp` library for high-quality image processing
- Hero images: resized to max 1920x1080, compressed to 85% quality
- Service images: resized to max 1920x1080, compressed to 85% quality
- Badges/icons: resized to max 800x800
- Automatically creates backups in `static/images/originals/`
- Typical savings: 85-95% file size reduction with minimal quality loss
- See `optimize-images.js` for full configuration

### Public Sharing via Localtunnel
For sharing the site publicly (useful when on restricted networks like coffee shop WiFi with client isolation):

**Setup:**
1. `hugo server --bind 0.0.0.0 --baseURL http://localhost:1313 --port 1313` - Start Hugo server
2. `node start-tunnel.js` - Start localtunnel (creates public URL)

**How it works:**
- The `start-tunnel.js` script creates a public HTTPS URL (e.g., `https://xyz.loca.lt`)
- Writes the URL to `tunnel-url.txt` for easy reference
- Tunnel stays active as long as the script is running
- First-time visitors will see a localtunnel landing page with an IP confirmation - they just click "Continue"

**Requirements:**
- `localtunnel` package (already in devDependencies)
- Both Hugo server and tunnel script must be running simultaneously

**Files:**
- `start-tunnel.js` - Node script that establishes tunnel connection
- `tunnel-url.txt` - Generated file containing the current public URL (git-ignored)

## Architecture

### Hugo Structure
- **Layouts**: Hugo templates in `layouts/` directory
  - `_default/baseof.html` - Base template with head, body structure
  - `_default/single.html` and `list.html` - Content templates
  - `partials/` - Reusable components (header, footer, hero, cta, SEO partials)
  - `shortcodes/` - Custom Hugo shortcodes for content

### Styling Strategy
- **Semantic CSS Architecture**: All components use semantic class names for single-source-of-truth maintenance
- **TailwindCSS with @apply**: Utility classes abstracted into semantic components using `@layer components`
- **No Inline Utilities**: HTML templates use only semantic class names (`.hero-title`, `.service-card`, etc.)
- **Custom theme** defined in `tailwind.config.js`:
  - Primary color: `#0B1F3B` (dark blue)
  - Accent color: `#2AA198` (teal)
  - Neutral color: `#F5F7FA` (light gray)
  - Custom fonts: Spectral (headings), Inter (body)
  - Custom border radius and shadow utilities

### Asset Pipeline
- **CSS**: Single consolidated `assets/css/tailwind.css` compiled to `assets/css/bundle.css`
- **PostCSS**: Configured with autoprefixer
- **Unified Architecture**: All styles (base, components, utilities) in one file using Tailwind's @layer system
- **Production**: Assets are minified and fingerprinted via Hugo's asset pipeline
- **JavaScript**: Single `assets/js/main.js` file

### Image Organization
- **Structured Directory System**: All images are organized into purpose-specific subdirectories for scalability and maintainability
- **Directory Structure**:
  - `static/images/heroes/` - Hero banner images for page headers and backgrounds
  - `static/images/icons/` - SVG icons for UI elements and feature highlights
  - `static/images/badges/` - Certification badges and achievement displays
  - `static/images/logos/` - Company logos and branding assets
  - `static/images/services/bookkeeping/` - Bookkeeping service-specific images
  - `static/images/services/automation/` - Business process automation service images
  - `static/images/services/strategy/` - Operations and growth strategy consulting images
  - `static/images/pages/` - Page-specific content images (about, pricing, contact subdirectories)
  - `static/images/shared/` - Shared/common images used across multiple pages
  - `static/images/references/` - Reference materials and documentation images

**Naming Conventions**:
- Service images: `service-name-variant.jpg` (e.g., `account-setup-natural.jpg`, `payroll-realistic.jpg`)
- Hero images: `hero-pagename-style.jpg` (e.g., `hero-homepage-main.jpg`, `hero-accounting-natural.jpg`)
- Icons: `descriptive-name-icon.svg` (e.g., `availability-icon.svg`, `proadvisor-trophy-icon.svg`)

**Guidelines for Adding New Images**:
- Always place images in appropriate subdirectories - never leave in root `/images/` directory
- Create new service subdirectories as features are added (e.g., `/services/consulting/`)
- Create page-specific subdirectories under `/pages/` for dedicated page content
- Maintain consistent naming patterns for easy identification and maintenance
- Use descriptive filenames that indicate purpose and content

### Content Structure
- `content/_index.md` - Homepage content with frontmatter
- Static assets in `static/` directory including images and robots.txt
- SEO and analytics partials for Google Tag Manager

### Key Files
- `tailwind.config.js` - TailwindCSS configuration with custom theme
- `postcss.config.js` - PostCSS configuration
- `image_generator.py` - Python script for image generation
- `start-tunnel.js` - Localtunnel script for public site sharing
- `theme-preview.html` - Theme preview/testing page

## Development Notes

- Hugo CLI must be installed for building (`hugo` command available)
- CSS compilation uses PostCSS with TailwindCSS
- Production builds include minification and asset fingerprinting
- No test framework configured (test command returns error)

## Styling Architecture Guidelines

### Core Principles
1. **Single Source of Truth**: All styling changes happen in `assets/css/tailwind.css` 
2. **Semantic Class Names**: HTML uses descriptive class names (`.hero-title`, not `.text-5xl`)
3. **Component-Based**: Each UI component has its own semantic class hierarchy
4. **Maintainable**: Changing a style affects all instances across the site
5. **Unified Architecture**: CSS custom properties, base styles, components, and utilities all in one consolidated file

### CSS Class Structure
```css
/* Section-level classes */
.hero-section, .services-section, .cta-section

/* Container classes */
.hero-container, .services-container, .cta-container

/* Content classes */
.hero-title, .services-title, .service-card, .service-title

/* Interactive elements */
.btn-hero-primary, .btn-hero-secondary, .btn-cta
```

### Making Style Changes
- **Typography**: Edit `.hero-title`, `.services-title`, `.service-title` classes
- **Spacing**: Edit `.hero-section`, `.services-section` padding/margins
- **Colors**: Edit button classes or add CSS custom properties
- **Hover Effects**: Edit `:hover` states in semantic classes
- **Responsive**: Use Tailwind responsive prefixes in `@apply` directives

## Recent Work Completed

### Semantic CSS Architecture Implementation
- **Complete Semantic System**: All components now use semantic classes
- **Hero Section**: `.hero-section`, `.hero-title`, `.hero-subtitle`, `.hero-buttons`
- **Services Section**: `.services-section`, `.service-card`, `.service-title`, etc.
- **Button System**: `.btn-hero-primary`, `.btn-hero-secondary`, `.btn-cta`
- **Template Updates**: All HTML templates use semantic classes only
- **Single Source of Truth**: All styling changes happen in one CSS file

### Pricing System Restructure (Latest)
- **Three-Card Layout**: Restructured pricing from 5 packages to 3 (Foundation, Restoration, Automation)
- **Vertical Layout**: Changed from 2-across grid to single-column vertical stacking
- **Unified Styling**: All pricing cards use consistent light teal gradient headers
- **Inline Links**: Replaced separate CTA buttons with inline hyperlinks in card descriptions
- **Enhanced Hugo Templates**: Updated pricing-cards.html shortcode to use safeHTML for link rendering
- **Removed Pricing Duplicates**: Centralized all pricing on dedicated page, removed from service pages

### Enhanced Hyperlink System
- **Global Link Styling**: Implemented site-wide enhanced hyperlink styles in @layer base
- **Hover/Click Effects**: Added smooth transitions and improved visual feedback
- **Consistent Branding**: All links use accent color with proper weight and underline styling
- **Performance**: Moved from component-specific to base layer for efficiency

### Content Optimization
- **Streamlined Navigation**: Removed "Related Services" sections from About and Contact pages
- **Centralized Pricing**: All pricing information now directs to dedicated pricing page
- **Improved UX**: Better text wrapping and alignment for bullet points in pricing cards

### Current Status
- Complete semantic CSS architecture implemented and **conflicts resolved**
- All styling consolidated into single `assets/css/tailwind.css` file
- Unified @layer system: base styles, CSS custom properties, semantic components, and utilities
- No inline Tailwind utilities in templates
- Clean asset pipeline with single CSS file processed by Hugo
- Easy maintenance with true single-source-of-truth approach
- Ready to extend this pattern to new pages and components

### Recent Fixes Completed
- **Resolved CSS Conflicts**: Eliminated duplicate styles between theme.css and tailwind.css
- **Consolidated Architecture**: Merged all styles into single tailwind.css with proper @layer structure  
- **Clean Asset Pipeline**: Removed static/css/bundle.css, using only Hugo-processed assets
- **Template Optimization**: Updated baseof.html to load single consolidated CSS bundle
- **Preserved Functionality**: Maintained all original semantic classes and design intent

## CSS Change Verification Process

To ensure CSS changes are immediately visible and prevent repeated requests:

### Mandatory Steps After Every CSS Change:

1. **Force CSS Rebuild**:
   ```bash
   npm run build:css
   ```

2. **Verify Change in Compiled CSS**:
   ```bash
   grep -n "your-change" assets/css/bundle.css
   ```

3. **Check Hugo Server Response**:
   - Monitor hugo server output for "Asset changed /css/bundle.css"
   - Ensure Hugo detects and rebuilds the site

4. **Browser Cache Management**:
   **CRITICAL FOR USER**: Always use these steps to see changes:
   - **Hard Refresh**: `Ctrl+Shift+F5` (Windows) or `Cmd+Shift+R` (Mac)
   - **Or use Dev Tools**: F12 → Network tab → Check "Disable cache"
   - **Or Incognito Mode**: Open site in private/incognito window

### Troubleshooting:
- If changes don't appear: Kill hugo server, run `npm run build:css`, restart server
- If still not visible: Clear all browser cache or try different browser
- Changes ARE in the code if they pass the grep verification step