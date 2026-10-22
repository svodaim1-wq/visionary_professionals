# UI/UX Design Specification & Visual Guide

## 1. Design Overview & Regional Context
Blends **Route One Dispatch** patterns for the **US freight market**.

*   **Primary Audience:** US fleet owners, owner-operators (Dry Van, Reefer, Flatbed, Step Deck), freight brokers.
*   **Core Visual Goal:** Build trust, clarity, and rapid conversion for mobile-first US users.

---

## 2. Color Palette & Typography

### Color Palette
*   **Primary (Logistics Blue):** `#0F2C59` — Trust, professional freight management.
*   **Secondary (Highway Gold):** `#F89B29` — CTAs, badges, alert banners.
*   **Neutral Dark (Asphalt):** `#1E2022` — Text, dark header backgrounds.
*   **Neutral Light (Slate):** `#F4F6F9` — Section background contrasts.
*   **Success Green (Chat Green):** `#28A745` — Form completion, verification badges, call/text CTA.

### Typography
*   **Headings:** `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
*   **Body:** Inter / System UI sans-serif for mobile legibility.

---

## 3. Page Layouts & Component Design

### A. Global Header & Navigation (`base.html`)
*   **Top Announcement Bar:** Dark banner with US phone (`(413) 423-1495`) + active lane status.
*   **Navbar:** Logo left, links center, "Carrier Intake" CTA right (Amber `#F89B29`).
*   **Footer:** Multi-column (Services | Explore | Resources | Support) + social icons + contact.

### B. Home Page (`pages/home.html`)
*   **Hero:** High-contrast background, US truck imagery, overlay headline.
*   **CTA Group:** Primary "Get Dispatched Today" + Call/Text button.
*   **Stats Bar:** 4 badges (e.g., "$8K+ Weekly Gross", "500+ Loads", "20% Better Rates", "24/7 Dispatch").
*   **Services Section:** Numbered list with bold titles (from Route One pattern).
*   **Route Assistance Section:** Icon grid (Optimize routes, Minimize delays, Maximize cost-effectiveness, Support drivers).
*   **Beyond Dispatch Section:** Billing, Document Management, Safety, After-Hours, Driver Statements.
*   **Equipment Section:** Card grid with border-left accent, equipment type, per-mile benchmarks.
*   **Testimonials Section:** (planned)
*   **FAQ Section:** (planned)
*   **Newsletter Subscribe:** Email input + button.

### C. Services Page (`pages/services.html`)
Adapted from Route One structure:
*   Dispatch for Owner-Operators
*   Dispatch for Small Fleets
*   Dispatch by Equipment Type

### D. Equipment Page (`pages/equipment.html`)
Card grid with US equipment types: 53' Dry Van, Power Only, Reefer, Flatbed, Step Deck, Box Truck.

### E. Pricing Page (`pages/pricing.html`)
*   Two pricing cards (8-10% Per Load / $350-$500 Weekly Rate in USD).
*   Lane Rate Calculator widget.
*   "Talk to a Dispatch Specialist" CTA form (equipment type, # trucks, time in business, name, email, phone, MC, DOT).

### F. Onboarding Page (`onboarding/carrier_form.html`)
*   Step tracker: Fleet & Owner → Equipment & Capacity → US Compliance (W-9, COI, MC Authority).
*   2-column form grid, file upload section for compliance docs.

### G. About Page (`pages/about.html`)
*   Company story, mission, team values.
*   "Why Choose Us" differentiators.

---

## 4. Mobile & Performance Optimization
*   **Data Efficiency:** Compressed WebP imagery, no heavy video assets.
*   **Responsive Grid:** All card grids collapse to single-column on mobile.
*   **One-Tap Call & Text:** Floating button, bottom-right corner.
*   **Touch Targets:** Minimum 44px tap targets for mobile form elements.

---

## 5. Reference: Route One Dispatch Patterns to Adapt
| Element | Route One (US) | Our Site (US) |
| :--- | :--- | :--- |
| Phone CTA | (224) 407-2559 | (413) 423-1495 |
| Stats | $8K+ weekly, 20K+ loads | $8K+ weekly, 500+ loads/month |
| Equipment | Dry van, Flatbed, Reefer | Dry Van, Reefer, Flatbed, Step Deck, Box Truck, Power Only |
| Payment | % invoiced weekly | % invoiced weekly (USD) |
| Agreement | Dispatch-Carrier agreement | Carrier-Dispatch agreement |
| Compliance | W9, COI, MC/DOT | W-9, COI, MC/DOT |
| Contact form | Equipment, trucks, time in business | Same + equipment type |
