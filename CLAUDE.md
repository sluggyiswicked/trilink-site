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

## Styling Architecture Guidelines

### Core Principles
1. **Single Source of Truth**: All styling changes happen in `assets/css/tailwind.css` 
2. **Semantic Class Names**: HTML uses descriptive class names (`.hero-title`, not `.text-5xl`)
3. **Component-Based**: Each UI component has its own semantic class hierarchy
4. **Maintainable**: Changing a style affects all instances across the site

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

### Current Status
- Complete semantic CSS architecture implemented
- All styling centralized in `assets/css/tailwind.css`
- No inline Tailwind utilities in templates
- Easy maintenance with single-source-of-truth approach
- Ready to extend this pattern to new pages and components