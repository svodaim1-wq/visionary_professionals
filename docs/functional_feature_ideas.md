# Functional Ideas & Feature Roadmap

## 1. Core Platform Capabilities
Inspired by **Route One Dispatch**, **Logity Dispatch**, and **EchoDrive** — adapted for the **South African dispatch ecosystem**.

---

## 2. Dynamic Carrier Onboarding Engine

### A. South Africa-Specific Field Validation
*   **CIPC Registration Number:** Form validation for SA company registration.
*   **Driver PrDP (Professional Driving Permit):** Checkbox confirmation and document upload field.
*   **GIT (Goods In Transit) Insurance Amount:** Structured input (R350k / R500k / R1M cover).
*   **Fleet Type Selector:** Superlink (34T), Tri-Axle (28T), 10-Ton Rigid, 8-Ton Flatbed, 1-Ton Bakkie.
*   **Number of Trucks:** 1, 2-3, 4-6, 7-8, 9-14, 15+.
*   **Time in Business:** 0-11 months, 12+ months.

### B. Dynamic Document Uploads
*   CIPC Certificate / Tax Clearance
*   GIT Insurance Policy Document
*   Banking Details (Proof of Bank Account)
*   Copy of Driver's License & PrDP

---

## 3. SA Freight Corridor & Rates Engine

### A. Corridor Rate Calculator
Interactive widget on Pricing page:
*   Origin/Destination city selectors (JHB, Durban, CPT, Polokwane, Nelspruit)
*   Vehicle type selector
*   Output: Estimated ZAR rate range + dispatch fee breakdown

### B. Live Corridor Status Board
Dynamic homepage banner showing high-demand corridors.

### C. Rate Lock Guarantee
Adapted from Route One: guarantee dispatch rate for set period (e.g., 12 months SA).

---

## 4. Operational Dispatch & Communication Tools

### A. WhatsApp Business API / Click-to-Chat
*   Pre-filled WhatsApp links: "Hi, I have a 34T Superlink available in JHB..."
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
| GIT & CIPC Field Additions | High | `apps/onboarding/` | Done |
| WhatsApp Instant Dispatch Button | Medium | `templates/includes/` | Done |
| Corridor Rate Calculator | Medium | `apps/services/` | Done |
| Carrier Document File Uploads | Low | `apps/onboarding/` | Done |
| Service Tiers (Owner/ Fleet) | Medium | `apps/pages/` | Planned |
| FAQ Section | Medium | `apps/pages/` | Planned |
| Testimonials | Medium | `apps/pages/` | Planned |
| Stats/Trust Bar | Medium | `apps/pages/` | Planned |
| POD Submission Portal | Low | `apps/dispatch/` | Phase 3 |
| Rate Lock Guarantee | Low | `apps/onboarding/` | Phase 3 |
| Blog | Low | `apps/blog/` | Future |
