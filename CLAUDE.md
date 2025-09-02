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

## Architecture

### Hugo Structure
- **Layouts**: Hugo templates in `layouts/` directory
  - `_default/baseof.html` - Base template with head, body structure
  - `_default/single.html` and `list.html` - Content templates
  - `partials/` - Reusable components (header, footer, hero, cta, SEO partials)
  - `shortcodes/` - Custom Hugo shortcodes for content

### Styling
- **TailwindCSS**: Primary styling framework
- **Custom theme** defined in `tailwind.config.js`:
  - Primary color: `#0B1F3B` (dark blue)
  - Accent color: `#2AA198` (teal)
  - Neutral color: `#F5F7FA` (light gray)
  - Custom fonts: Spectral (headings), Inter (body)
  - Custom border radius and shadow utilities

### Asset Pipeline
- **CSS**: `assets/css/tailwind.css` compiled to `assets/css/bundle.css`
- **PostCSS**: Configured with autoprefixer
- **Semantic CSS**: Button classes defined in `@layer components` in tailwind.css
- **Production**: Assets are minified and fingerprinted
- **JavaScript**: Single `assets/js/main.js` file

### Content Structure
- `content/_index.md` - Homepage content with frontmatter
- Static assets in `static/` directory including images and robots.txt
- SEO and analytics partials for Google Tag Manager

### Key Files
- `tailwind.config.js` - TailwindCSS configuration with custom theme
- `postcss.config.js` - PostCSS configuration
- `image_generator.py` - Python script for image generation
- `theme-preview.html` - Theme preview/testing page

## Development Notes

- Hugo CLI must be installed for building (`hugo` command available)
- CSS compilation uses PostCSS with TailwindCSS
- Production builds include minification and asset fingerprinting
- No test framework configured (test command returns error)

## Recent Work Completed

### Theme Refinement (Step 3 Progress)
- **Button Styling System**: Implemented semantic CSS classes using Tailwind's `@apply`:
  - `.btn-hero-primary` - Primary hero buttons (white border)
  - `.btn-hero-secondary` - Secondary hero buttons (translucent border)
  - `.btn-cta` - Call-to-action buttons (brand colored background)
- **Service Card Interactions**: Added subtle hover effects with shadows and transforms
- **CSS Architecture**: Fixed compilation pipeline to use compiled bundle.css instead of raw tailwind.css
- **Template Structure**: Proper Hugo template separation (layouts vs content)
- **Responsive Design**: Maintained mobile-first approach with consistent typography

### Current Status
- Homepage is fully functional with proper styling and interactions
- Button styles are properly compiled and applied
- Service cards have professional hover effects
- Typography and spacing follow design system
- Ready to proceed with remaining content pages or SEO implementation