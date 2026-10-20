# Milestone Checklist

Review this after EVERY AI-assisted change.

## Phase 1: Foundation
- [x] Project directory structure created
- [x] Django project + apps configured
- [x] Base template + navbar/footer
- [x] Home page hero section styled
- [x] About/Why Choose Us page content
- [x] CSS styling complete

## Phase 2: Functionality
- [x] Carrier onboarding form (model + view + template)
- [x] Contact form (model + view + template)
- [x] Services page dynamic content
- [x] Equipment page dynamic content
- [x] Pricing page content complete

## Phase 3: Production
- [x] PostgreSQL config (via DB_* env vars)
- [x] .env properly configured (copy .env.example to .env)
- [ ] Static files collectstatic
- [x] Tests passing (8/8)
- [ ] Deploy ready

## Phase 4: SA Localization (from user docs)
- [x] Color palette updated per ui_design_blueprint.md
- [x] Typography updated (system-ui stack)
- [x] Announcement bar with SA phone + corridor status
- [x] WhatsApp floating button added
- [x] Home page: SA hero copy, trust metrics, corridor banner
- [x] Equipment page: SA fleet types with card grid layout
- [x] Pricing page: ZAR rates, corridor rate preview
- [x] Onboarding: CIPC, PrDP, GIT insurance, SA fleet type fields
- [x] Multi-step form tracker UI
- [x] Corridor rate calculator (interactive widget)
- [x] Document upload for SA compliance files
- [x] POD submission portal (stub page at /portal/)

## Phase 5: Route One Dispatch Patterns (from reference site)
- [x] Stats bar on home page (R80K+ weekly gross, loads count, etc.)
- [x] Testimonials section
- [x] FAQ section (Why choose us, How to start, Agreement, Privacy, Payment terms)
- [x] Services page with tiers (Owner-Operators, Small Fleets, By Equipment)
- [x] Footer with multi-column links (Services | Explore | Resources | Support)
- [x] Newsletter subscribe section
- [x] "Talk to a Dispatch Specialist" CTA form on pricing page

## Phase 6: Route One Patterns — Additional Pages
- [x] Solutions page (beyond-dispatch services)
- [x] Enhanced About page with Route One-style content
- [x] Dispatch Specialist CTA form wired to backend
- [x] Form success/error messages
- [x] Carrier portal stub page at /portal/

## Phase 7: Final Polish
- [x] Added missing nav links (About, Solutions, Portal)
- [x] Blog stub page at /blog/
- [x] Carrier packet page at /carrier-packet/
- [x] Custom 404 page
- [x] Security middleware + CSRF settings for production
- [x] README with full setup instructions

## Phase 8: Portal & Production
- [x] Carrier login page at /portal/login/
- [x] Schedule-a-call booking page at /schedule-call/
- [x] Blog + carrier-packet added to navbar
- [x] Gunicorn + Procfile for production deployment
- [x] All 12 tests passing

## Phase 9: API & Calculator Backend
- [x] REST API endpoint for corridor rate calculator at /services/api/corridor-rate/
- [x] Frontend calculator now fetches from API
- [x] API tests for valid, missing params, and invalid corridor cases

## Phase 10: Portal Dashboard & Settings
- [x] Carrier dashboard at /portal/dashboard/
- [x] Account settings page at /portal/settings/
- [x] Carrier login with Django messages
- [x] Carrier logout functionality
- [x] Custom 404 test route
- [x] All 12 tests passing

## Phase 12: Remaining Doc Features
- [x] POD Submission Portal at /onboarding/pod/
- [x] Rate Lock Guarantee (12-month rate lock added to onboarding)
- [x] Live Corridor Status Board on home page
- [x] WhatsApp auto-notification placeholder (messages framework)
- [x] All 12 tests passing

---

## Phase 13: Professional Visual & UX Overhaul — IMPLEMENTED
Goal: Transform the site to match the polish of professional dispatch sites (Route One, Logity, EchoDrive).
Status: Core overhaul implemented. Pending items are noted with (PENDING).

### 13.1 Global Design System
- [x] CSS variables for complete palette (blue/amber/charcoal/slate/green)
- [x] Typography scale (H1-H6, body, small) with responsive clamps
- [x] Spacing system (consistent section padding/margins)
- [x] Border-radius + shadow system
- [x] Animated gradient hero background
- [x] Smooth scroll + reveal-on-scroll animations (IntersectionObserver)
- [x] Hover lift + glow effects on cards/buttons
- [x] Custom button system (primary/secondary/outline/ghost/whatsapp)

### 13.2 Header / Navbar
- [x] Sticky glassmorphism navbar with blur
- [x] Logo placeholder (VP monogram)
- [x] Mobile hamburger menu with slide-in drawer
- [x] Dropdown menus for Services
- [x] Search bar in header (searches pages/services)
- [x] Phone + WhatsApp CTA buttons in header
- [x] Scroll progress bar at top

### 13.3 Home Page
- [x] Full-height hero with overlay
- [x] Animated headline (fade-in)
- [x] Dual CTA buttons
- [x] Trust metrics bar with count-up animation
- [x] Services preview grid (cards with icons)
- [x] Corridor status board (animated demand badges)
- [x] Testimonials carousel (auto-rotating)
- [x] FAQ accordion with smooth animation
- [x] Newsletter section with styled form
- [ ] Logo strip / trusted by section (PENDING)

### 13.4 About Page
- [x] Company story section with image
- [x] Team image placeholder
- [x] Values cards with icons
- [ ] Mission + vision cards (PENDING)
- [ ] Timeline / milestones section (PENDING)
- [ ] Stats with count-up animation (PENDING)

### 13.5 Services Page
- [x] Service tier cards with full detail
- [x] Feature comparison table
- [x] Individual service detail sections
- [x] CTA banners between sections

### 13.6 Equipment Page
- [x] Filterable equipment grid (category buttons)
- [x] Equipment cards with placeholder images
- [x] Tonnage + rate-per-km specs
- [ ] Request-this-vehicle CTA per card (PENDING)

### 13.7 Pricing Page
- [x] Interactive ZAR calculator (API-backed)
- [x] Feature list with checkmarks
- [x] Dispatch Specialist CTA form
- [ ] Pricing cards with toggle (monthly/load) (PENDING)
- [ ] Comparison table (PENDING)

### 13.8 Blog
- [x] Blog listing page with featured post
- [x] Author + date + reading time
- [ ] Category filters (PENDING)
- [ ] Search functionality (PENDING)
- [ ] Individual post template (PENDING)
- [ ] Related posts (PENDING)
- [ ] Blog model + admin integration (PENDING)

### 13.9 Help / Guide Page (NEW)
- [x] Getting started guide
- [x] FAQ searchable index
- [x] Glossary of dispatch terms
- [x] Document checklist
- [x] Contact support CTA
- [ ] Video/resource placeholders (PENDING)

### 13.10 Contact Page
- [x] Contact form with validation
- [x] WhatsApp / phone / email cards
- [ ] Map placeholder (PENDING)
- [ ] Office details + hours (PENDING)

### 13.11 Footer
- [x] Multi-column link layout
- [x] Logo + tagline
- [x] Social icons
- [x] Contact info
- [x] Legal links (Terms, Privacy, Cookies)
- [x] Back-to-top button
- [ ] Newsletter signup in footer (PENDING)

### 13.12 Animations & Motion
- [x] Reveal on scroll (fade/slide)
- [x] Hover micro-interactions
- [x] Button glow effects
- [x] Count-up stats animation
- [x] Back-to-top button
- [ ] Smooth page transitions (PENDING)
- [ ] Loading spinners for forms (PENDING)

### 13.13 Responsive & Accessibility
- [x] Mobile-first breakpoints (768/1024)
- [x] Alt text on images
- [x] ARIA labels on interactive elements
- [x] Reduced motion media query
- [ ] Touch-friendly tap targets (44px+) (PENDING)
- [ ] Keyboard navigation support (PENDING)

### 13.14 Placeholder Media
- [x] Logo (SVG)
- [x] Hero banner image (SVG)
- [x] Equipment type images (5 SVG)
- [x] About page image (SVG)
- [x] Favicon (SVG)
- [ ] Team avatars (PENDING)
- [ ] Testimonial avatars (PENDING)
- [ ] Social media icons (SVG) (PENDING)

---

## Phase 14: Advanced Features (FUTURE)
- [ ] User authentication system (register/login/logout)
- [ ] Carrier dashboard with real load data
- [ ] Live load board integration
- [ ] WhatsApp Business API integration
- [ ] Email notifications (SendGrid / AWS SES)
- [ ] SMS notifications
- [ ] Admin panel customization
- [ ] Analytics dashboard
- [ ] Multi-language support (i18n)
- [ ] SEO optimization (meta tags, sitemap, robots.txt)
- [ ] Performance optimization (caching, CDN)
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Dark mode toggle

## Phase 15: Testing & Quality (FUTURE)
- [ ] Full test coverage (90%+)
- [ ] E2E tests (Playwright/Cypress)
- [ ] Visual regression tests
- [ ] Load testing
- [ ] Security audit
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] Performance audit (Lighthouse 90+)
