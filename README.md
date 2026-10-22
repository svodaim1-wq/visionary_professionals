Visionary Professionals — US Freight Dispatch Website

A Django-based website for an American freight dispatching company serving owner-operators and small fleets across major US freight lanes.

Tech Stack
Backend: Django 5 and Python 3.12
Frontend: HTML5, CSS3, Vanilla JavaScript
Database: SQLite for development, PostgreSQL for production (via environment variables)
Quick Start
1. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

2. Install dependencies
pip install -r requirements.txt

3. Configure environment variables
Copy-Item .env.example .env


Update .env with your local configuration and secret values.

4. Run database migrations
python manage.py migrate

5. Create an administrator account
python manage.py createsuperuser

6. Start the development server
python manage.py runserver


Visit http://127.0.0.1:8000/ in your browser.

Pages
Route	Description
/	Home page with hero, statistics, services, testimonials, and FAQ
/about/	About us
/services/	Dispatch service tiers
/solutions/	Additional services
/equipment/	Fleet and equipment types
/pricing/	Rates in USD and lane rate calculator
/onboarding/carrier/	Carrier onboarding form
/contact/	Contact form
/portal/	Carrier portal
/blog/	Blog
/carrier-packet/	Required compliance documents
/admin/	Django administration
Documentation

Project documentation is available in the docs/ directory:

TERMINAL_COMMANDS.md — VS Code terminal commands
AI_RULES_GUIDELINES.md — Guidelines for AI assistants
MILESTONE_CHECKLIST.md — Project progress tracker
DIRECTORY_STRUCTURE.md — File and folder purposes
functional_feature_ideas.md — Feature roadmap
ui_design_blueprint.md — UI/UX specification
Environment Variables

See .env.example for the available configuration options. Never commit your actual .env file or expose secret keys, passwords, or other credentials.

Development Notes
Apply database migrations before running the application.
Keep dependencies documented in requirements.txt.
Configure production settings, environment variables, and a production-ready database before deployment.