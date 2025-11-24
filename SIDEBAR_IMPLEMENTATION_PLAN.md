# Sidebar Consistency Implementation Plan

**Created:** 2025-10-28
**Status:** Ready for Implementation
**Estimated Time:** Phase 1 (30 min), Phase 2 (1-2 hours), Phase 3 (Future)

---

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Current State Analysis](#current-state-analysis)
3. [Phase 1: Critical Fixes](#phase-1-critical-fixes-30-minutes)
4. [Phase 2: Context-Aware Content](#phase-2-context-aware-content-1-2-hours)
5. [Phase 3: Future Enhancements](#phase-3-future-enhancements)
6. [Testing Guide](#testing-guide)
7. [Reference Information](#reference-information)
8. [Rollback Instructions](#rollback-instructions)

---

## Executive Summary

### The Problem
The current `page-sidebar` component is **identical across all 15+ pages**, causing:
- ❌ Redundant CTAs (shows "Book Consultation" on Contact page)
- ❌ Self-referential links (Pricing page links to Pricing)
- ❌ Dead links (Downloads page doesn't exist)
- ❌ Generic, non-contextual content
- ❌ Doesn't leverage rich frontmatter data already on pages

### The Solution
**Smart Conditional Sections with Frontmatter-Driven Content**
- ✅ Same 3-section structure (consistency)
- ✅ Content adapts based on page type (context-awareness)
- ✅ Uses existing frontmatter data (no new content needed)
- ✅ No content restructuring required (works with flat file structure)
- ✅ Incremental implementation (ship improvements progressively)

### Expected Outcomes

**After Phase 1:**
- Professional, polished sidebar with no redundancies
- Removed dead links and self-references
- Context-aware CTA titles

**After Phase 2:**
- Service pages show relevant related services
- Trust indicators match the service being viewed
- Navigation adapts intelligently to page type
- Each page has contextual, engaging sidebar content

**After Phase 3:**
- Resource downloads drive engagement
- Testimonials build trust
- Clear next-step guidance throughout user journey

---

## Current State Analysis

### Current Sidebar Location
**File:** `layouts/_default/single.html`
**Lines:** 96-129

### Current Sidebar Structure
```html
<!-- Sidebar -->
<aside class="page-sidebar">
  <!-- Section 1: Quick Navigation (Conditional) -->
  {{ if .Parent }}
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">{{ .Parent.Title }}</h3>
    <nav class="page-sidebar-nav">
      {{ range .Parent.Pages }}
        <a href="{{ .RelPermalink }}" class="page-sidebar-nav-item{{ if eq .RelPermalink $.RelPermalink }} active{{ end }}">
          {{ .Title }}
        </a>
      {{ end }}
    </nav>
  </div>
  {{ end }}

  <!-- Section 2: Contact CTA (Always Displayed) -->
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">Ready to Get Started?</h3>
    <p class="text-gray-600 text-sm mb-4">Schedule a free consultation to discuss your specific needs.</p>
    <a href="/contact/" class="btn-primary w-full text-center block">Book Consultation</a>
  </div>

  <!-- Section 3: Quick Links (Always Displayed) -->
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">Quick Links</h3>
    <nav class="page-sidebar-nav">
      <a href="/pricing/" class="page-sidebar-nav-item">Pricing</a>
      <a href="/resources/case-studies/" class="page-sidebar-nav-item">Case Studies</a>
      <a href="/resources/downloads/" class="page-sidebar-nav-item">Downloads</a>
      <a href="/about/" class="page-sidebar-nav-item">About Us</a>
    </nav>
  </div>
</aside>
```

### Pages Affected
All pages using `single.html` template:
- **Service Pages:** Bookkeeping, Business Process Automation, Operations & Growth Strategy, and all service sub-pages
- **Other Pages:** Contact, About, Pricing, QuickBooks ProAdvisor, Case Studies

### Critical Issues Identified
1. **Section 1 (Quick Navigation):** Rarely displays because pages don't have `.Parent` relationships in flat structure
2. **Section 2 (Contact CTA):** Shows on Contact page (redundant), uses generic text everywhere
3. **Section 3 (Quick Links):** Contains dead links, shows self-referential links, identical everywhere

---

## Phase 1: Critical Fixes (30 Minutes)

### Goals
- Remove redundant CTAs
- Remove self-referential Quick Links
- Remove dead links
- Make CTA titles context-aware

### Implementation Steps

#### Step 1: Open the Template
```bash
# File to edit:
layouts/_default/single.html
# Lines: 96-129
```

#### Step 2: Replace Entire Sidebar Section

**Find this code (lines 96-129):**
```html
<!-- Sidebar -->
<aside class="page-sidebar">
  <!-- Quick Navigation -->
  {{ if .Parent }}
  ...entire sidebar...
  {{ end }}
</aside>
```

**Replace with this:**
```html
<!-- Sidebar -->
<aside class="page-sidebar">
  <!-- Section 1: Quick Navigation -->
  {{ if .Parent }}
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">{{ .Parent.Title }}</h3>
    <nav class="page-sidebar-nav">
      {{ range .Parent.Pages }}
        <a href="{{ .RelPermalink }}" class="page-sidebar-nav-item{{ if eq .RelPermalink $.RelPermalink }} active{{ end }}">
          {{ .Title }}
        </a>
      {{ end }}
    </nav>
  </div>
  {{ end }}

  <!-- Section 2: Contact CTA -->
  {{ if not (eq .RelPermalink "/contact/") }}
  <div class="page-sidebar-section">
    {{ $ctaTitle := "Ready to Get Started?" }}
    {{ if .Params.cta.title }}
      {{ $ctaTitle = .Params.cta.title }}
    {{ end }}
    <h3 class="page-sidebar-title">{{ $ctaTitle }}</h3>
    <p class="text-gray-600 text-sm mb-4">Schedule a free consultation to discuss your specific needs.</p>
    <a href="/contact/" class="btn-primary w-full text-center block">Book Consultation</a>
  </div>
  {{ end }}

  <!-- Section 3: Quick Links -->
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">Quick Links</h3>
    <nav class="page-sidebar-nav">
      {{ if not (eq .RelPermalink "/pricing/") }}
      <a href="/pricing/" class="page-sidebar-nav-item">Pricing</a>
      {{ end }}
      {{ if not (eq .RelPermalink "/resources/case-studies/") }}
      <a href="/resources/case-studies/" class="page-sidebar-nav-item">Case Studies</a>
      {{ end }}
      {{ if not (eq .RelPermalink "/about/") }}
      <a href="/about/" class="page-sidebar-nav-item">About Us</a>
      {{ end }}
    </nav>
  </div>
</aside>
```

#### Step 3: Save and Test

**Rebuild CSS (if Hugo server not running):**
```bash
npm run build:css
```

**Start Hugo server (if not running):**
```bash
hugo server --bind 0.0.0.0 --baseURL http://localhost:1313 --port 1313
```

**Test these pages:**
1. `/contact/` - Should NOT show "Book Consultation" CTA section
2. `/pricing/` - Quick Links should NOT have "Pricing" link
3. `/about/` - Quick Links should NOT have "About Us" link
4. `/services/bookkeeping/` - CTA title should show custom title from frontmatter if available

### Phase 1 Changes Summary
✅ Added conditional: `{{ if not (eq .RelPermalink "/contact/") }}` around CTA section
✅ CTA title now uses `{{ .Params.cta.title }}` from frontmatter with fallback
✅ Quick Links now exclude current page using conditionals
✅ Removed "Downloads" link (doesn't exist)

---

## Phase 2: Context-Aware Content (1-2 Hours)

### Goals
- Make Section 1 navigation intelligent with multiple fallback strategies
- Add new Trust/Value section showing service-specific indicators
- Enhance CTA with better context-awareness
- Update service page frontmatter to support new features

### Implementation Steps

#### Step 1: Update Service Page Frontmatter

**Add to ALL service pages** (bookkeeping.md, business-process-automation.md, etc.):

```yaml
---
title: "Your Service Title"
# ... existing frontmatter ...

# NEW: Sidebar configuration
sidebar:
  related_services:
    - title: "Account Setup & Consulting"
      url: "/services/account-setup-consulting/"
      description: "Get your QuickBooks set up right from the start"
    - title: "Ongoing Bookkeeping"
      url: "/services/ongoing-bookkeeping-monthly-close/"
      description: "Monthly accounting and financial close services"
    - title: "Account Cleanup"
      url: "/services/account-cleanup-catch-up/"
      description: "Catch up on past-due bookkeeping and reconciliations"

# Existing trust indicators (make sure these exist)
trust_indicators:
  - text: "GAAP Compliant Accounting"
    icon: "check"
  - text: "QuickBooks ProAdvisor Certified"
    icon: "badge"
  - text: "Audit-Ready Records"
    icon: "shield"

# Existing CTA (make sure this exists)
cta:
  title: "Ready to Get Your Books in Order?"
  description: "Clean, organized, audit-ready books. Let's get started."
---
```

**Example for business-process-automation.md:**
```yaml
sidebar:
  related_services:
    - title: "Bookkeeping Services"
      url: "/services/bookkeeping/"
      description: "Traditional bookkeeping and accounting"
    - title: "Operations Strategy"
      url: "/services/operations-growth-strategy/"
      description: "Strategic consulting for growth"

trust_indicators:
  - text: "70-80% Time Savings on Routine Tasks"
    icon: "clock"
  - text: "Custom Workflow Automation"
    icon: "automation"
  - text: "QuickBooks Integration Expertise"
    icon: "integration"
```

#### Step 2: Replace Sidebar with Phase 2 Version

**Replace entire sidebar section in `layouts/_default/single.html`:**

```html
<!-- Sidebar -->
<aside class="page-sidebar">

  <!-- Section 1: Smart Navigation -->
  {{ if .Parent }}
    <!-- If page has parent, show sibling navigation -->
    <div class="page-sidebar-section">
      <h3 class="page-sidebar-title">{{ .Parent.Title }}</h3>
      <nav class="page-sidebar-nav">
        {{ range .Parent.Pages }}
          <a href="{{ .RelPermalink }}" class="page-sidebar-nav-item{{ if eq .RelPermalink $.RelPermalink }} active{{ end }}">
            {{ .Title }}
          </a>
        {{ end }}
      </nav>
    </div>

  {{ else if .Params.sidebar.related_services }}
    <!-- If page has related services in frontmatter, show those -->
    <div class="page-sidebar-section">
      <h3 class="page-sidebar-title">Related Services</h3>
      <nav class="page-sidebar-nav">
        {{ range .Params.sidebar.related_services }}
          <a href="{{ .url }}" class="page-sidebar-nav-item">
            <strong>{{ .title }}</strong>
            {{ if .description }}
              <span class="block text-xs text-gray-500 mt-1">{{ .description }}</span>
            {{ end }}
          </a>
        {{ end }}
      </nav>
    </div>

  {{ else if eq .Section "services" }}
    <!-- If it's a service page without related_services, show main service categories -->
    <div class="page-sidebar-section">
      <h3 class="page-sidebar-title">Our Services</h3>
      <nav class="page-sidebar-nav">
        <a href="/services/bookkeeping/" class="page-sidebar-nav-item">Bookkeeping Services</a>
        <a href="/services/business-process-automation/" class="page-sidebar-nav-item">Business Process Automation</a>
        <a href="/services/operations-growth-strategy/" class="page-sidebar-nav-item">Operations & Growth Strategy</a>
      </nav>
    </div>

  {{ else }}
    <!-- Default: Show Quick Links for non-service pages -->
    <div class="page-sidebar-section">
      <h3 class="page-sidebar-title">Quick Links</h3>
      <nav class="page-sidebar-nav">
        {{ if not (eq .RelPermalink "/pricing/") }}
        <a href="/pricing/" class="page-sidebar-nav-item">Pricing</a>
        {{ end }}
        {{ if not (eq .RelPermalink "/resources/case-studies/") }}
        <a href="/resources/case-studies/" class="page-sidebar-nav-item">Case Studies</a>
        {{ end }}
        {{ if not (eq .RelPermalink "/about/") }}
        <a href="/about/" class="page-sidebar-nav-item">About Us</a>
        {{ end }}
      </nav>
    </div>
  {{ end }}

  <!-- Section 2: Trust & Value Indicators -->
  {{ if .Params.trust_indicators }}
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">Why Choose Us</h3>
    <ul class="space-y-2">
      {{ range .Params.trust_indicators }}
      <li class="flex items-start text-sm text-gray-700">
        <svg class="w-5 h-5 text-accent mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
        </svg>
        <span>{{ .text }}</span>
      </li>
      {{ end }}
    </ul>
  </div>
  {{ else if or (eq .Section "about") (eq .RelPermalink "/about/") (eq .RelPermalink "/contact/") }}
  <!-- Default trust indicators for About/Contact pages -->
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">Why Trilink</h3>
    <ul class="space-y-2">
      <li class="flex items-start text-sm text-gray-700">
        <svg class="w-5 h-5 text-accent mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
        </svg>
        <span>QuickBooks ProAdvisor Certified</span>
      </li>
      <li class="flex items-start text-sm text-gray-700">
        <svg class="w-5 h-5 text-accent mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
        </svg>
        <span>GAAP Compliant Practices</span>
      </li>
      <li class="flex items-start text-sm text-gray-700">
        <svg class="w-5 h-5 text-accent mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
        </svg>
        <span>Personalized Service</span>
      </li>
    </ul>
  </div>
  {{ end }}

  <!-- Section 3: Context-Aware CTA -->
  {{ $isContact := eq .RelPermalink "/contact/" }}
  {{ if not $isContact }}
  <div class="page-sidebar-section">
    {{ $ctaTitle := "Ready to Get Started?" }}
    {{ $ctaDesc := "Schedule a free consultation to discuss your specific needs." }}

    {{ if .Params.cta.title }}
      {{ $ctaTitle = .Params.cta.title }}
    {{ end }}

    {{ if .Params.cta.description }}
      {{ $ctaDesc = .Params.cta.description }}
    {{ end }}

    <h3 class="page-sidebar-title">{{ $ctaTitle }}</h3>
    <p class="text-gray-600 text-sm mb-4">{{ $ctaDesc }}</p>
    <a href="/contact/" class="btn-primary w-full text-center block">Book Consultation</a>
  </div>
  {{ end }}

</aside>
```

#### Step 3: Update CSS (if needed)

The existing CSS classes should work, but if you want to enhance the trust indicators list:

**Add to `assets/css/tailwind.css` in the `.page-sidebar` section:**

```css
.page-sidebar-section ul {
  @apply list-none p-0 m-0;
}

.page-sidebar-section ul.space-y-2 > li {
  @apply mb-2;
}

.page-sidebar-section ul.space-y-2 > li:last-child {
  @apply mb-0;
}
```

#### Step 4: Test Phase 2

**Test Navigation Section on different page types:**
1. Service page with `sidebar.related_services` → Should show those
2. Service page without frontmatter → Should show main 3 services
3. Non-service page (About, Contact) → Should show Quick Links

**Test Trust Indicators:**
1. Service pages → Should show frontmatter trust_indicators
2. About/Contact pages → Should show default trust elements
3. Other pages → May not show (that's okay)

**Test CTA:**
1. All pages except Contact → Should show with custom title/description from frontmatter
2. Contact page → Should NOT show at all

### Phase 2 Changes Summary
✅ Section 1 has intelligent fallback logic: .Parent → related_services → main services → Quick Links
✅ Section 2 is NEW: Shows service-specific trust indicators or default credentials
✅ Section 3 uses both cta.title AND cta.description from frontmatter
✅ All changes use existing frontmatter data where available

---

## Phase 3: Future Enhancements

### Not Implemented Yet - Ideas for Future

#### 3.1: Resource Downloads Section
```html
{{ if .Params.sidebar.resources }}
<div class="page-sidebar-section">
  <h3 class="page-sidebar-title">Free Resources</h3>
  <nav class="page-sidebar-nav">
    {{ range .Params.sidebar.resources }}
      <a href="{{ .url }}" class="page-sidebar-nav-item" download>
        <strong>{{ .title }}</strong>
        <span class="block text-xs text-gray-500 mt-1">{{ .type }}</span>
      </a>
    {{ end }}
  </nav>
</div>
{{ end }}
```

**Frontmatter example:**
```yaml
sidebar:
  resources:
    - title: "Setup Checklist"
      url: "/downloads/setup-checklist.pdf"
      type: "PDF Guide"
    - title: "Pre-Consultation Form"
      url: "/downloads/consultation-form.pdf"
      type: "Fillable PDF"
```

#### 3.2: Testimonial Snippets
```html
{{ if .Params.sidebar.testimonial }}
<div class="page-sidebar-section">
  <h3 class="page-sidebar-title">Client Success</h3>
  <blockquote class="text-sm text-gray-600 italic">
    "{{ .Params.sidebar.testimonial.quote }}"
  </blockquote>
  <p class="text-xs text-gray-500 mt-2">
    — {{ .Params.sidebar.testimonial.author }}, {{ .Params.sidebar.testimonial.company }}
  </p>
</div>
{{ end }}
```

#### 3.3: Popular Services (for non-service pages)
```html
{{ if not (eq .Section "services") }}
<div class="page-sidebar-section">
  <h3 class="page-sidebar-title">Popular Services</h3>
  <nav class="page-sidebar-nav">
    <a href="/services/bookkeeping/" class="page-sidebar-nav-item">
      <strong>Bookkeeping</strong>
      <span class="block text-xs text-gray-500 mt-1">Most popular</span>
    </a>
    <a href="/services/business-process-automation/" class="page-sidebar-nav-item">
      <strong>Automation</strong>
      <span class="block text-xs text-gray-500 mt-1">Save 70-80% time</span>
    </a>
  </nav>
</div>
{{ end }}
```

---

## Testing Guide

### Phase 1 Testing Checklist

**Contact Page (`/contact/`):**
- [ ] Sidebar does NOT show "Book Consultation" CTA section
- [ ] Quick Links section shows (Pricing, Case Studies)
- [ ] Quick Links does NOT include "About Us" (self-reference)

**Pricing Page (`/pricing/`):**
- [ ] Sidebar shows CTA section
- [ ] Quick Links does NOT include "Pricing" (self-reference)
- [ ] Quick Links includes Case Studies, About Us

**About Page (`/about/`):**
- [ ] Sidebar shows CTA section
- [ ] Quick Links does NOT include "About Us" (self-reference)
- [ ] Quick Links includes Pricing, Case Studies

**Service Pages (e.g., `/services/bookkeeping/`):**
- [ ] Sidebar shows CTA section with custom title from frontmatter (if available)
- [ ] Quick Links includes Pricing, Case Studies, About Us
- [ ] No "Downloads" link appears

### Phase 2 Testing Checklist

**Service Page WITH sidebar.related_services in frontmatter:**
- [ ] Section 1 shows "Related Services" with items from frontmatter
- [ ] Each related service shows title and description
- [ ] Section 2 shows trust indicators from frontmatter with checkmarks
- [ ] Section 3 shows custom CTA title AND description from frontmatter

**Service Page WITHOUT sidebar.related_services:**
- [ ] Section 1 shows "Our Services" with main 3 service categories
- [ ] Section 2 shows trust indicators from frontmatter (if available)
- [ ] Section 3 shows CTA with custom text

**About Page:**
- [ ] Section 1 shows Quick Links (no self-reference to About)
- [ ] Section 2 shows default trust elements (ProAdvisor, GAAP, etc.)
- [ ] Section 3 shows CTA

**Contact Page:**
- [ ] Section 1 shows Quick Links
- [ ] Section 2 shows default trust elements
- [ ] Section 3 does NOT show (no CTA on contact page)

**Pricing Page:**
- [ ] Navigation section shows appropriately
- [ ] Trust section shows (if applicable)
- [ ] CTA section shows with pricing-appropriate text

### Browser Cache Testing

**IMPORTANT:** After making changes, always test with a hard refresh to avoid browser cache issues.

**Hard Refresh Methods:**
- **Windows:** `Ctrl+Shift+F5` or `Ctrl+F5`
- **Mac:** `Cmd+Shift+R`
- **Chrome DevTools:** F12 → Network tab → Check "Disable cache"
- **Incognito/Private:** Open site in private browsing mode

### Visual Testing Checklist

- [ ] Sidebar sections have consistent spacing
- [ ] Text is readable and properly sized
- [ ] Links have proper hover states
- [ ] Icons (checkmarks) display correctly in trust section
- [ ] Mobile responsive (sidebar stacks properly on mobile)
- [ ] No layout shifts or overlapping content

---

## Reference Information

### Hugo Conditional Patterns Used

#### Check Current Page
```go
{{ if eq .RelPermalink "/contact/" }}
  <!-- Code for contact page only -->
{{ end }}
```

#### Check Page Section
```go
{{ if eq .Section "services" }}
  <!-- Code for all service pages -->
{{ end }}
```

#### Check if Frontmatter Field Exists
```go
{{ if .Params.sidebar.related_services }}
  <!-- Code if field exists -->
{{ end }}
```

#### Multiple Conditions (OR)
```go
{{ if or (eq .Section "about") (eq .RelPermalink "/about/") }}
  <!-- Code if either condition is true -->
{{ end }}
```

#### Multiple Conditions (AND)
```go
{{ if and (eq .Section "services") .Params.trust_indicators }}
  <!-- Code if both conditions are true -->
{{ end }}
```

#### Variable Assignment
```go
{{ $ctaTitle := "Default Title" }}
{{ if .Params.cta.title }}
  {{ $ctaTitle = .Params.cta.title }}
{{ end }}
<h3>{{ $ctaTitle }}</h3>
```

### Frontmatter Structure Reference

**Complete service page frontmatter example:**

```yaml
---
title: "Bookkeeping Services"
description: "Professional bookkeeping and accounting services"

# Sidebar Configuration (NEW for Phase 2)
sidebar:
  related_services:
    - title: "Account Setup & Consulting"
      url: "/services/account-setup-consulting/"
      description: "Get your QuickBooks set up right"
    - title: "Ongoing Bookkeeping"
      url: "/services/ongoing-bookkeeping-monthly-close/"
      description: "Monthly accounting services"
    - title: "Account Cleanup"
      url: "/services/account-cleanup-catch-up/"
      description: "Catch up on past-due bookkeeping"

# Trust Indicators (should already exist, verify format)
trust_indicators:
  - text: "GAAP Compliant Accounting"
    icon: "check"
  - text: "QuickBooks ProAdvisor Certified"
    icon: "badge"
  - text: "Audit-Ready Records"
    icon: "shield"

# CTA Configuration (should already exist, verify format)
cta:
  title: "Ready to Get Your Books in Order?"
  description: "Clean, organized, audit-ready books. Let's get started."
  button_text: "Book Consultation"  # Not used in sidebar, but good to have

# Other existing frontmatter...
---
```

### CSS Classes Reference

**All classes are defined in `assets/css/tailwind.css`:**

```css
.page-sidebar              /* Main sidebar container */
.page-sidebar-section      /* Individual sidebar section (card) */
.page-sidebar-title        /* Section heading */
.page-sidebar-nav          /* Navigation container */
.page-sidebar-nav-item     /* Individual navigation link */
.page-sidebar-nav-item.active  /* Active navigation state */
```

**Standard Tailwind classes used:**
- `text-gray-600`, `text-gray-500`, `text-gray-700` - Text colors
- `text-sm`, `text-xs` - Text sizes
- `mb-4`, `mt-1`, `mt-2` - Margins
- `space-y-2` - Vertical spacing between list items
- `flex`, `items-start` - Flexbox layout
- `w-5`, `h-5` - Icon sizes
- `block` - Display property

### File Locations Quick Reference

```
layouts/
  _default/
    single.html          # Sidebar code here (lines 96-129)

content/
  services/
    bookkeeping.md       # Update frontmatter
    business-process-automation.md
    operations-growth-strategy.md
    account-setup-consulting.md
    # ... all other service pages

assets/
  css/
    tailwind.css         # Sidebar CSS classes (lines 1371-1407)
```

---

## Rollback Instructions

### If Phase 1 Causes Issues

**Revert to original sidebar code:**

```html
<!-- Sidebar -->
<aside class="page-sidebar">
  <!-- Quick Navigation -->
  {{ if .Parent }}
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">{{ .Parent.Title }}</h3>
    <nav class="page-sidebar-nav">
      {{ range .Parent.Pages }}
        <a href="{{ .RelPermalink }}" class="page-sidebar-nav-item{{ if eq .RelPermalink $.RelPermalink }} active{{ end }}">
          {{ .Title }}
        </a>
      {{ end }}
    </nav>
  </div>
  {{ end }}

  <!-- Contact CTA -->
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">Ready to Get Started?</h3>
    <p class="text-gray-600 text-sm mb-4">Schedule a free consultation to discuss your specific needs.</p>
    <a href="/contact/" class="btn-primary w-full text-center block">Book Consultation</a>
  </div>

  <!-- Quick Links -->
  <div class="page-sidebar-section">
    <h3 class="page-sidebar-title">Quick Links</h3>
    <nav class="page-sidebar-nav">
      <a href="/pricing/" class="page-sidebar-nav-item">Pricing</a>
      <a href="/resources/case-studies/" class="page-sidebar-nav-item">Case Studies</a>
      <a href="/resources/downloads/" class="page-sidebar-nav-item">Downloads</a>
      <a href="/about/" class="page-sidebar-nav-item">About Us</a>
    </nav>
  </div>
</aside>
```

### If Phase 2 Causes Issues

**Option 1:** Revert to Phase 1 version (see Phase 1 code above)
**Option 2:** Debug specific issue:
- If navigation not showing: Check frontmatter format
- If trust indicators not showing: Verify frontmatter field names
- If styling looks off: Check CSS compilation with `npm run build:css`

### Git Rollback

```bash
# View recent changes
git diff layouts/_default/single.html

# Rollback just the sidebar file
git checkout HEAD -- layouts/_default/single.html

# Rollback all changes since last commit
git reset --hard HEAD
```

---

## Quick Start for Tomorrow

### Step-by-Step Launch

1. **Open project in your editor**
   ```bash
   cd C:\projects\node\trilink-site
   code .
   ```

2. **Start Hugo server**
   ```bash
   hugo server --bind 0.0.0.0 --baseURL http://localhost:1313 --port 1313
   ```

3. **Open sidebar template**
   ```
   File: layouts/_default/single.html
   Lines: 96-129
   ```

4. **Choose your phase:**
   - **Phase 1** (30 min) → Go to [Phase 1 Implementation](#phase-1-critical-fixes-30-minutes)
   - **Phase 2** (1-2 hours) → Go to [Phase 2 Implementation](#phase-2-context-aware-content-1-2-hours)

5. **Make changes and test**
   - Hugo will auto-reload on save
   - Hard refresh browser: `Ctrl+Shift+F5`
   - Test pages listed in [Testing Guide](#testing-guide)

6. **Commit when satisfied**
   ```bash
   git add layouts/_default/single.html
   git commit -m "Improve sidebar context-awareness and consistency"
   ```

---

## Implementation Tips

### Tip 1: Work Incrementally
Don't try to do everything at once. Implement Phase 1, test thoroughly, commit, then move to Phase 2.

### Tip 2: Test on Multiple Page Types
After each change, test on:
- A service page (e.g., `/services/bookkeeping/`)
- Contact page (`/contact/`)
- Pricing page (`/pricing/`)
- About page (`/about/`)

### Tip 3: Use Hugo Server Watch
Hugo will automatically rebuild when you save files. Watch the terminal output for errors.

### Tip 4: Browser DevTools
Keep DevTools open (F12) to:
- Disable cache (Network tab → "Disable cache")
- Inspect element styles
- Check console for errors

### Tip 5: Frontmatter Validation
Before testing Phase 2, verify that at least ONE service page has proper frontmatter:
- `sidebar.related_services` array
- `trust_indicators` array
- `cta.title` and `cta.description`

### Tip 6: Start with Easy Wins
If you're short on time, just do Phase 1. It provides immediate visible improvements with minimal risk.

---

## Success Metrics

### Phase 1 Success
- ✅ No redundant CTAs on Contact page
- ✅ No self-referential links in Quick Links
- ✅ No broken/dead links
- ✅ CTA titles vary by page (when frontmatter exists)

### Phase 2 Success
- ✅ Service pages show relevant related services
- ✅ Trust indicators are service-specific
- ✅ Navigation adapts intelligently to page type
- ✅ Each page feels contextual, not generic
- ✅ CTA descriptions are compelling and specific

### Overall Success
- ✅ Sidebar enhances user journey instead of being repetitive
- ✅ Content drives engagement with relevant CTAs
- ✅ Professional, polished appearance across all pages
- ✅ Easy to maintain (just update frontmatter for new pages)

---

## Questions or Issues?

### Common Issues

**Issue:** Changes don't appear in browser
**Solution:** Hard refresh (`Ctrl+Shift+F5`) or clear browser cache

**Issue:** Hugo build errors
**Solution:** Check terminal for syntax errors, ensure all `{{ }}` blocks are closed

**Issue:** Frontmatter not working
**Solution:** Check YAML syntax, ensure proper indentation, restart Hugo server

**Issue:** Sidebar looks broken
**Solution:** Rebuild CSS with `npm run build:css`, check for CSS conflicts

### Need Help?

This document should be comprehensive enough for implementation. If you encounter issues:

1. Check the [Rollback Instructions](#rollback-instructions)
2. Review the [Testing Guide](#testing-guide)
3. Verify frontmatter format matches [Reference Information](#reference-information)
4. Check Hugo terminal output for errors

---

**Document Version:** 1.0
**Last Updated:** 2025-10-28
**Status:** Ready for Implementation

Good luck with the implementation! Start with Phase 1 for quick wins, then move to Phase 2 when ready. 🚀
