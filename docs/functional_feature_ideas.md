# Functional Ideas & Feature Roadmap

## 1. Core Platform Capabilities
Inspired by **Route One Dispatch**, **Logity Dispatch**, and **EchoDrive** — adapted for the **American dispatch ecosystem**.

---

## 2. Dynamic Carrier Onboarding Engine

### A. US-Specific Field Validation
*   **Active MC Authority:** Checkbox confirmation and authority letter upload.
*   **MC & DOT Numbers:** Form validation for FMCSA operating authority.
*   **Cargo Insurance Coverage:** Structured input ($100k / $250k / higher).
*   **Equipment Type Selector:** 53' Dry Van, Reefer, Flatbed, Step Deck, Box Truck, Power Only.
*   **Number of Trucks:** 1, 2-3, 4-6, 7-8, 9-14, 15+.
*   **Time in Business:** 0-11 months, 12+ months.

### B. Dynamic Document Uploads
*   Signed W-9 (EIN / Tax ID)
*   Certificate of Insurance (COI) — cargo & liability
*   Voided Check / Direct Deposit Form
*   Copy of CDL & MC Authority Letter

---

## 3. US Freight Lane & Rates Engine

### A. Lane Rate Calculator
Interactive widget on Pricing page:
*   Origin/Destination city selectors (Chicago, Omaha, Dallas, Atlanta, Los Angeles, Phoenix)
*   Equipment type selector
*   Distance in miles
*   Output: Estimated USD rate range ($/mile) + dispatch fee breakdown

### B. Live Lane Status Board
Dynamic homepage banner showing high-demand lanes.

### C. Rate Lock Guarantee
Adapted from Route One: guarantee dispatch rate for set period (e.g., 12 months US).

---

## 4. Operational Dispatch & Communication Tools

### A. SMS / Click-to-Text Communication
*   Click-to-call/text links: "Call or text (413) 423-1495".
*   Auto-notification to dispatch managers on new carrier registration.

### B. Dispatch Service Tiers (from Route One pattern)
*   **For Owner-Operators:** Daily loads, dedicated dispatcher.
*   **For Small Fleets:** Multi-truck coordination, volume rates.
*   **For Growing Fleets:** Full back-office, compliance, driver statements.

### C. Proof of Delivery (POD) & Invoicing Workflow (Future)
*   POD Submission Portal for drivers (mobile web upload).
*   Quick-Pay Status Tracking: Submitted → Verified → Payment Dispatched.

### D. Beyond-Dispatch Services (from Route One pattern)
*   Billing & Invoicing
*   Document Management
*   Safety Assistance / Compliance
*   After-Hours Dispatch
*   Driver Statements
*   Data Entry & Monitoring

---

## 5. Trust & Social Proof Elements (from Route One)

### A. Stats Bar
*   Weekly gross potential (e.g., "R80,000+")
*   Loads booked count
*   Better-than-average rates badge

### B. Testimonials Section
Carousel/grid of carrier testimonials.

### C. FAQ Section
*   Why choose us?
*   How to get started?
*   Dispatch-Carrier agreement info
*   Privacy & confidentiality
*   Rate permanence guarantee
*   Payment terms (% invoiced weekly)
*   In-house vs outsourced dispatch comparison
*   New carrier support

---

## 6. Navigation Structure (from Route One)

```
Home | About Us | Services (dropdown) | Solutions | Rates/Pricing | Blog | Contacts
Services dropdown:
  - Dispatch for Owner-Operators
  - Dispatch for Small Fleets
  - Dispatch by Trailer/Equipment Type
Footer columns:
  - Dispatch Services | Explore | Resources | Support
```

---

## 7. Technical Implementation Roadmap

| Feature Module | Priority | Target App | Status |
| :--- | :--- | :--- | :--- |
| Mobile-Responsive Carrier Form | High | `apps/onboarding/` | Done |
| W-9, COI & MC Authority Field Additions | High | `apps/onboarding/` | Done |
| SMS Instant Dispatch Button | Medium | `templates/includes/` | Done |
| Lane Rate Calculator (USD, $/mile) | Medium | `apps/services/` | Done |
| Carrier Document File Uploads | Low | `apps/onboarding/` | Done |
| Service Tiers (Owner/ Fleet) | Medium | `apps/pages/` | Planned |
| FAQ Section | Medium | `apps/pages/` | Planned |
| Testimonials | Medium | `apps/pages/` | Planned |
| Stats/Trust Bar | Medium | `apps/pages/` | Planned |
| POD Submission Portal | Low | `apps/dispatch/` | Phase 3 |
| Rate Lock Guarantee | Low | `apps/onboarding/` | Phase 3 |
| Blog | Low | `apps/blog/` | Future |
