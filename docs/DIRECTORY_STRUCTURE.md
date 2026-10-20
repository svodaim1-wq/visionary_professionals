# Directory Structure

```
Dispatcher/
├── manage.py                  # Django CLI entry point
├── requirements.txt           # Python dependencies
├── .env.example               # Template for environment variables
├── config/                    # Django project settings
│   ├── settings.py            # Main settings (DB, apps, static, etc.)
│   ├── urls.py                # Root URL routing
│   ├── wsgi.py                # WSGI server entry
│   └── asgi.py                # ASGI server entry
├── apps/
│   ├── core/                  # Health check, site-wide utilities
│   ├── pages/                 # Static pages (home, about, equipment, pricing)
│   ├── onboarding/            # Carrier/driver intake form
│   ├── services/              # Services listing logic
│   └── contact/               # Contact form handling
├── templates/
│   ├── base.html              # Master layout (head, nav, footer)
│   ├── includes/              # Reusable partials
│   ├── pages/                 # One template per page
│   └── onboarding/            # Onboarding form template
├── static/
│   ├── css/main.css           # Global styles
│   ├── js/main.js             # Global scripts
│   └── images/                # Logos, hero images, etc.
├── docs/                      # All project documentation
├── tests/                     # Project-level test files
└── media/                     # User-uploaded files (future)
```

## File Purpose
Each Django app follows the standard layout: `models.py` (database), `views.py` (logic), `urls.py` (routing), `admin.py` (admin panel), `forms.py` (form definitions), `tests.py` (test cases).

Placeholder files with commented code are marked with `# TODO:` — implement when ready per AI_RULES_GUIDELINES.md.
