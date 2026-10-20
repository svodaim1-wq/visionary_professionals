# Visionary Professionals — SA Freight Dispatch Website

A Django-based website for a South African freight dispatching company serving owner-operators and small fleets across major SA corridors.

## Tech Stack
- **Backend:** Django 5 + Python 3.12
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** SQLite (dev), PostgreSQL (prod via env vars)

## Quick Start

```powershell
# 1. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment
Copy-Item .env.example .env

# 4. Run migrations
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Start dev server
python manage.py runserver
```

## Pages
| Route | Description |
|-------|-------------|
| `/` | Home — hero, stats, services, testimonials, FAQ |
| `/about/` | About us |
| `/services/` | Dispatch service tiers |
| `/solutions/` | Beyond-dispatch services |
| `/equipment/` | Fleet & equipment types |
| `/pricing/` | Rates (ZAR) + corridor calculator |
| `/onboarding/carrier/` | Carrier onboarding form |
| `/contact/` | Contact form |
| `/portal/` | Carrier portal (stub) |
| `/blog/` | Blog (stub) |
| `/carrier-packet/` | Required compliance documents |
| `/admin/` | Django admin |

## Documentation
All project docs are in the `docs/` folder:
- `TERMINAL_COMMANDS.md` — VSCode terminal commands
- `AI_RULES_GUIDELINES.md` — Rules for AI assistants
- `MILESTONE_CHECKLIST.md` — Progress tracker
- `DIRECTORY_STRUCTURE.md` — File/folder purposes
- `functional_feature_ideas.md` — Feature roadmap
- `ui_design_blueprint.md` — UI/UX specification

## Environment Variables
See `.env.example` for all available settings.
