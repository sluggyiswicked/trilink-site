# Product Requirements Document
## Trilink Accounting Services Website

### 1. Project Overview

**Objective**: Build a professional Hugo-based static website for an accounting services company, deployed on AWS Amplify with full analytics and lead tracking.

**Timeline**: 8-step implementation plan
**Status**: ~30% Complete (Steps 1-2 done, Step 3 next)

### 2. Technical Requirements

#### Core Stack
- **Frontend Framework**: Hugo (extended)
- **Styling**: TailwindCSS via PostCSS pipeline
- **Hosting**: AWS Amplify
- **Analytics**: Google Tag Manager + GA4 with Consent Mode v2
- **Repository**: Single repo workflow (no git commands from agent)

#### Configuration Variables
```
COMPANY_NAME="Your Accounting Co."
PRIMARY_DOMAIN="yourdomain.com"
PRIMARY_HOSTNAME="www.yourdomain.com"
STAGING_HOSTNAME="staging.yourdomain.com"
GA4_MEASUREMENT_ID="G-XXXXXXX"
GTM_CONTAINER_ID="GTM-YYYYYYY"
```

### 3. Design System

#### Theme Variables
```
THEME_FONT_HEADINGS="Spectral"
THEME_FONT_BODY="Inter"
THEME_COLOR_PRIMARY="#0B1F3B" (deep navy)
THEME_COLOR_ACCENT="#2AA198" (teal)
THEME_COLOR_NEUTRAL="#F5F7FA" (light background)
THEME_RADIUS="1rem"
THEME_SHADOW="0 10px 20px rgba(0,0,0,0.06)"
```

#### Design Principles
- Clean, professional aesthetic for financial services
- Mobile-first responsive design
- Accessibility compliance (WCAG AA+)
- Performance-optimized (LCP < 2.5s, CLS < 0.1)

### 4. Functional Requirements

#### 4.1 Page Structure & Information Architecture

##### **Core Pages** (5 pages)
- **Homepage** (`/`): Value prop, services overview, outcomes, proof, CTA to consultation
- **Services Overview** (`/services/`): H1: "Accounting + Automation that scales" 
- **Pricing** (`/pricing/`): Foundation, Operate, Automate, Strategy packages
- **About** (`/about/`): Team, certifications, approach, values
- **Contact** (`/contact/`): "Book a consultation" form and contact info
- **Resources** (`/resources/`): Case studies, FAQ, guides

##### **Accounting Services** (6 detailed pages)
- **Account Setup & Consulting** (`/services/accounting/account-setup-consulting/`)
- **Account Cleanup (Catch-Up)** (`/services/accounting/account-cleanup/`)
- **Software Training** (`/services/accounting/software-training/`)
- **Payroll Setup & Processing** (`/services/accounting/payroll/`)
- **Ongoing Bookkeeping & Monthly Close** (`/services/accounting/bookkeeping-monthly-close/`)
- **Year-End Adjustments** (`/services/accounting/year-end-adjustments/`)

##### **Business Process Automation** (4 detailed pages)
- **Custom Interfaces & Internal Tools** (`/services/automation/custom-interfaces/`)
- **Integrations** (`/services/automation/integrations/`)
- **Cost Allocation Automations** (`/services/automation/cost-allocation/`)
- **Dashboards & Reporting** (`/services/automation/dashboards-reporting/`)

##### **Operations & Growth Strategy** (1 detailed page)
- **Operations & Growth Strategy** (`/services/operations-strategy/`)

##### **Legal Pages** (2 pages)
- **Privacy Policy** (`/legal/privacy/`)
- **Terms of Service** (`/legal/terms/`)

**Total Site Pages**: 19 pages

#### 4.2 SEO Requirements
- **Meta Tags**: Proper title, description, canonical on all pages
- **Structured Data**: JSON-LD `AccountingService` schema
- **Social Media**: Open Graph and Twitter Card meta tags
- **Technical SEO**: XML sitemap, robots.txt, proper heading hierarchy
- **Performance**: Lighthouse scores ≥95 across all categories

#### 4.3 Analytics & Tracking
- **Google Tag Manager**: Container with Consent Mode v2
- **GA4 Integration**: Page views, scroll depth, form submissions
- **Lead Tracking**: `generate_lead` events for contact form submissions
- **Cookie Consent**: Accessible banner with granular consent options
- **Privacy Compliance**: GDPR/CCPA compliant data collection

#### 4.4 Lead Generation
- **Contact Forms**: Accessible forms with proper validation
- **CTA Placement**: Strategic call-to-action buttons throughout site
- **Event Tracking**: Form submissions tracked via dataLayer
- **Conversion Optimization**: A/B testable components

### 5. Implementation Plan

#### STEP 1: Scaffold Core ✅ COMPLETE
- Hugo project initialization
- TailwindCSS via PostCSS setup
- Base layouts and partials
- Build pipeline configuration

#### STEP 2: Preview & Theme QA ✅ COMPLETE
- Development server setup
- Theme validation checklist
- Visual approval gate
- Design system implementation

#### STEP 3: Company Branding & Identity ✅ COMPLETE
- ✅ Company name finalization and implementation ("Trilink Collaborative LLC")
- ✅ Logo design and integration (header with company name)
- ✅ Brand asset creation and optimization
- ✅ Updated hero messaging and service positioning
- ✅ Semantic CSS classes for branding consistency

#### STEP 4: Pages & IA 🔄 IN PROGRESS (Expanded Scope)
**Phase 1: Foundation** 
- ✅ Homepage with updated hero and services cards
- ✅ Services cards transformed to new offerings
- ✅ Semantic CSS architecture with Tailwind @apply
- ❌ Services overview page (`/services/`)
- ❌ Pricing page with 4 packages
- ❌ Contact/consultation booking page

**Phase 2: Accounting Services Detail Pages (6 pages)**
- ❌ Account Setup & Consulting page
- ❌ Account Cleanup (Catch-Up) page  
- ❌ Software Training page
- ❌ Payroll Setup & Processing page
- ❌ Ongoing Bookkeeping & Monthly Close page
- ❌ Year-End Adjustments page

**Phase 3: Automation Services Detail Pages (4 pages)**
- ❌ Custom Interfaces & Internal Tools page
- ❌ Integrations page
- ❌ Cost Allocation Automations page
- ❌ Dashboards & Reporting page

**Phase 4: Strategy & Supporting Pages (4 pages)**
- ❌ Operations & Growth Strategy page
- ❌ About page
- ❌ Resources page (case studies, FAQ)
- ❌ Legal pages (privacy, terms)

**Progress**: 3 of 19 pages complete (16%)

#### STEP 5: SEO & Analytics 🔄 PARTIALLY COMPLETE
- ✅ SEO partials structure
- ❌ Complete meta tag implementation
- ❌ JSON-LD structured data
- ❌ GTM with Consent Mode v2
- ❌ Cookie banner

#### STEP 6: Lead Tracking ❌ NOT STARTED
- Contact form with dataLayer integration
- Analytics event implementation
- Lead tracking validation

#### STEP 7: Amplify Deployment ❌ NOT STARTED
- `amplify.yml` configuration
- Environment variables setup
- Staging/production branches

#### STEP 8: Acceptance Testing ❌ NOT STARTED
- Performance validation
- Lighthouse audits
- Analytics verification
- Accessibility testing

### 6. Success Metrics

#### Performance Targets
- **LCP (Largest Contentful Paint)**: < 2.5 seconds
- **CLS (Cumulative Layout Shift)**: < 0.1
- **INP (Interaction to Next Paint)**: < 200ms
- **Lighthouse Performance**: ≥95

#### SEO Targets
- **Lighthouse SEO Score**: ≥95
- **Rich Results**: Valid AccountingService schema
- **Core Web Vitals**: Pass all metrics
- **Mobile Usability**: 100% mobile-friendly

#### Analytics Targets
- **GA4 Implementation**: 100% event tracking coverage
- **Consent Rate**: >70% analytics consent
- **Lead Events**: Accurate form submission tracking
- **Data Quality**: Clean, structured analytics data

### 7. Technical Specifications

#### Required Files Structure
```
/
├── assets/
│   ├── css/
│   │   ├── tailwind.css
│   │   ├── theme.css
│   │   └── bundle.css (generated)
│   └── js/
│       └── main.js
├── content/
│   ├── _index.md
│   ├── services/
│   ├── industries/
│   ├── about/
│   ├── contact/
│   ├── pricing/
│   ├── resources/
│   └── legal/
├── layouts/
│   ├── _default/
│   ├── partials/
│   └── shortcodes/
├── static/
│   ├── robots.txt
│   ├── 404.html
│   └── images/
├── config/_default/
├── amplify.yml
├── package.json
├── tailwind.config.js
└── postcss.config.js
```

#### Build Requirements
- **Node.js**: Latest LTS version
- **Hugo Extended**: Required for SCSS/PostCSS processing
- **NPM Scripts**:
  - `dev`: Development server with CSS watching
  - `build`: Production build with minification
  - `build:css`: CSS compilation only

### 8. Deployment Requirements

#### AWS Amplify Configuration
- **Staging Branch**: Connected to `staging` branch → `staging.yourdomain.com`
- **Production Branch**: Connected to `main` branch → `www.yourdomain.com`
- **Environment Variables**: GTM_CONTAINER_ID, GA4_MEASUREMENT_ID
- **Build Settings**: Custom `amplify.yml` with Hugo build process

#### Performance Optimization
- **Asset Optimization**: Minification and fingerprinting in production
- **Image Optimization**: Proper sizing and lazy loading
- **Font Loading**: Preload critical fonts, swap for non-critical
- **Cache Headers**: Proper browser caching configuration

### 9. Quality Assurance

#### Pre-Launch Checklist
- [ ] All pages load without errors
- [ ] Forms submit and track properly
- [ ] Mobile navigation works correctly
- [ ] Analytics events fire correctly
- [ ] SEO meta tags present on all pages
- [ ] Structured data validates
- [ ] Cookie banner functions properly
- [ ] Lighthouse scores ≥95 all categories
- [ ] Cross-browser compatibility tested
- [ ] Accessibility audit passed

### 10. Detailed Implementation Checklist

#### **Phase 1: Foundation Pages (Priority 1)**
- [ ] **Services Overview** (`/services/`)
  - [ ] Create Hugo content file with frontmatter
  - [ ] H1: "Accounting + Automation that scales with your business"
  - [ ] Service category sections with overview content
  - [ ] Primary/secondary CTAs and trust elements
  - [ ] SEO meta tags and structured data

- [ ] **Pricing Page** (`/pricing/`) 
  - [ ] 4 pricing packages: Foundation, Operate, Automate, Strategy
  - [ ] Package descriptions, "starting at" pricing, quote CTAs
  - [ ] Trust elements and value propositions

- [ ] **Contact Page** (`/contact/`)
  - [ ] "Book a consultation" form with proper fields
  - [ ] Contact information and office details
  - [ ] Form submission handling and validation

#### **Phase 2: Accounting Services Detail Pages (Priority 2)**
- [ ] **Account Setup & Consulting** (`/services/accounting/account-setup-consulting/`)
- [ ] **Account Cleanup** (`/services/accounting/account-cleanup/`)
- [ ] **Software Training** (`/services/accounting/software-training/`)
- [ ] **Payroll Setup & Processing** (`/services/accounting/payroll/`)
- [ ] **Ongoing Bookkeeping** (`/services/accounting/bookkeeping-monthly-close/`)
- [ ] **Year-End Adjustments** (`/services/accounting/year-end-adjustments/`)

*Each accounting page includes: Ideal for, Outcomes, Deliverables, SEO optimization*

#### **Phase 3: Automation Services Detail Pages (Priority 2)**
- [ ] **Custom Interfaces** (`/services/automation/custom-interfaces/`)
- [ ] **Integrations** (`/services/automation/integrations/`)
- [ ] **Cost Allocation** (`/services/automation/cost-allocation/`)
- [ ] **Dashboards & Reporting** (`/services/automation/dashboards-reporting/`)

*Each automation page includes: Technical specs, integration examples, ROI benefits*

#### **Phase 4: Strategy & Supporting Pages (Priority 3)**
- [ ] **Operations & Growth Strategy** (`/services/operations-strategy/`)
- [ ] **About Page** (`/about/`) - Team, certifications, approach
- [ ] **Resources Page** (`/resources/`) - Case studies, FAQ, guides
- [ ] **Legal Pages** (`/legal/privacy/`, `/legal/terms/`)

#### **Navigation & SEO (Ongoing)**
- [ ] Update main navigation menu structure
- [ ] Implement breadcrumbs for deep pages
- [ ] Create XML sitemap with all pages
- [ ] Add internal linking strategy
- [ ] Implement canonical URLs
- [ ] Add Open Graph meta tags

#### **Content & Copy Requirements**
- [ ] Expand TLAs (QBO, GAAP, BPA, etc.) once per page
- [ ] Add 3-5 FAQs per service page
- [ ] Include trust elements (certifications, client quotes)
- [ ] Optimize for search intent keywords
- [ ] Create consistent CTA messaging

#### **Technical Implementation**
- [ ] Create Hugo layouts for service detail pages
- [ ] Add semantic CSS classes for new page types
- [ ] Implement form handling for consultation booking
- [ ] Add analytics tracking for new pages
- [ ] Test mobile responsiveness on all pages
- [ ] Optimize images and assets

**Current Status**: Phase 1 Foundation - 16% complete (3/19 pages)

### 11. Future Enhancements (Post-Launch)
- Blog/resources content management
- Client portal integration
- Online appointment booking
- Live chat integration
- Advanced lead scoring
- Marketing automation integration