# Service Pages Standardization Plan

## Goal
Standardize the remaining service pages to match the clean, content-focused design pattern used on the pricing page, while preserving the card-based grid layouts that work well on overview pages.

## Current State Analysis

### Pages We Like (Keep As-Is)
1. **Homepage** (`content/_index.md`) - Hero sections and service grid cards ✅
2. **Bookkeeping Overview** (`content/services/bookkeeping-overview.md`) - Card-based grid layout for services ✅
3. **Business Process Automation** (`content/services/business-process-automation.md`) - Already uses clean card pattern ✅
4. **Pricing Page** (`content/pricing.md`) - Clean content sections with inline links ✅ (MODEL)

### Pages to Standardize

#### 1. Operations & Growth Strategy (`content/services/operations-growth-strategy.md`)
**Current Pattern:**
- Uses `content-section-wrapper` and `content-section-card` divs ✅
- Alternating white/gray sections ✅
- **Issue:** Has large closing CTA section at bottom with separate button styling

**Changes Needed:**
- ✅ Already uses the right content-section pattern
- ✅ Already has good alternating white/gray sections
- ❌ Remove large closing CTA section (lines 408-415)
- ✅ Inline links already present in content

#### 2. Individual Bookkeeping Service Pages
All following pages need to be converted from long-form prose to clean content-section pattern:

- `content/services/account-setup-consulting.md`
- `content/services/account-cleanup-catch-up.md`
- `content/services/ongoing-bookkeeping-monthly-close.md`
- `content/services/year-end-adjustments.md`
- `content/services/payroll-setup-processing.md`
- `content/services/software-training.md`

**Current Pattern:**
- Heavy use of content-section divs ✅
- Alternating white/gray ✅
- **Issues:**
  - Some have pricing sections that should link to pricing page instead
  - Some have heavy "Ready to Get Started?" sections at bottom
  - Some have "Success Story" sections that could be streamlined

**Changes Needed:**
- Keep content-section pattern (already present)
- Remove pricing sections → replace with inline link to `/pricing/`
- Remove heavy bottom CTA sections
- Streamline success stories or move to case studies
- Ensure all CTAs are inline links within content

## Design Pattern: Pricing Page Model

### Key Characteristics
1. **Content Section Structure:**
   ```html
   <div class="content-section-wrapper">
     <div class="content-section-card content-section-white">
       <!-- Content with inline links -->
     </div>
     <div class="content-section-card content-section-gray">
       <!-- Content with inline links -->
     </div>
   </div>
   ```

2. **Inline Links Instead of Buttons:**
   - Example: `<a href="/contact/">Get started</a>` within paragraph text
   - Example: `<a href="/pricing/">Contact us for a custom quote</a>`
   - Links are styled with accent color, bold, underlined with enhanced hover states

3. **No Separate CTA Sections:**
   - No large closing sections with buttons
   - No "Ready to Get Started?" hero-style CTAs
   - All CTAs integrated naturally into content flow

4. **Alternating Backgrounds:**
   - White (`content-section-white`) and gray (`content-section-gray`) alternate
   - Creates visual rhythm without heavy section breaks

5. **FAQ Sections:**
   - Simple Q&A format within `content-section-card`
   - Bold questions, regular text answers
   - Clean and scannable

## Implementation Plan

### Phase 1: Operations & Growth Strategy
**File:** `content/services/operations-growth-strategy.md`

**Tasks:**
1. Remove closing CTA section (lines 408-415)
2. Add inline link to contact at end of last content section
3. Verify all pricing references link to `/pricing/` page

**Estimated Changes:** Minimal - mostly deletions

### Phase 2: Individual Bookkeeping Service Pages
**Files:** 6 service pages listed above

**For Each Page:**
1. **Review Pricing Sections:**
   - Remove detailed pricing breakdowns
   - Replace with: "For pricing information, see our [pricing page](/pricing/)."

2. **Simplify Bottom CTAs:**
   - Remove "Ready to Get Started?" sections
   - Add inline link in final paragraph instead

3. **Success Stories:**
   - Keep if brief and relevant (1-2 paragraphs max)
   - Or remove and link to `/resources/case-studies/`

4. **Ensure Content-Section Pattern:**
   - All content wrapped in `content-section-wrapper`
   - Sections alternate white/gray
   - No standalone markdown content outside cards

5. **FAQ Sections:**
   - Keep if valuable
   - Ensure simple Q&A format
   - Place in final content-section-card

### Phase 3: Verify Template Consistency
**File:** `layouts/_default/single.html`

**Tasks:**
1. Verify page-level CTA section (lines 241-256) respects `hide_cta` parameter
2. Ensure all service pages have `hide_cta: true` in frontmatter
3. Review sidebar CTAs to ensure they're appropriate for new pattern

## Content Guidelines

### ✅ DO:
- Use `content-section-wrapper` and `content-section-card` divs
- Alternate white and gray backgrounds
- Use inline links within paragraphs for CTAs
- Keep FAQ sections simple and scannable
- Link to pricing page for all pricing information
- Link to case studies page for detailed success stories

### ❌ DON'T:
- Create separate CTA sections at page bottom
- Include detailed pricing breakdowns on service pages
- Use button-style CTAs outside of hero sections
- Create heavy closing sections
- Duplicate content that exists on other pages

## Success Criteria

After implementation, all service pages should:
1. Use consistent `content-section` pattern
2. Have inline links for CTAs (no separate sections)
3. Link to pricing page (no embedded pricing)
4. Have clean, scannable layouts
5. Alternate white/gray backgrounds
6. Have minimal redundancy with other pages
7. Set `hide_cta: true` in frontmatter to disable template-level CTA

## Files to Modify

### Content Files (Markdown)
1. `content/services/operations-growth-strategy.md` - Remove closing CTA
2. `content/services/account-setup-consulting.md` - Remove pricing, streamline CTAs
3. `content/services/account-cleanup-catch-up.md` - Remove pricing, streamline CTAs
4. `content/services/ongoing-bookkeeping-monthly-close.md` - Remove pricing, streamline CTAs
5. `content/services/year-end-adjustments.md` - Remove pricing, streamline CTAs
6. `content/services/payroll-setup-processing.md` - Remove pricing, streamline CTAs
7. `content/services/software-training.md` - Remove pricing, streamline CTAs

### No Template Changes Needed
- Layout templates already support this pattern
- CSS already includes all necessary styles
- Shortcodes work correctly

## Timeline Estimate
- **Phase 1:** 15 minutes (Operations page)
- **Phase 2:** 1-2 hours (6 bookkeeping service pages)
- **Phase 3:** 15 minutes (Template verification)
- **Total:** ~2-2.5 hours

## Next Steps
1. Review and approve this plan
2. Start with Phase 1 (Operations page) as proof of concept
3. Proceed to Phase 2 (individual service pages)
4. Review results and adjust if needed
5. Complete Phase 3 verification
