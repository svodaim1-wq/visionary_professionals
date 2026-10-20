# AI Rules & Guidelines

## Always Follow
1. Work in `C:\Users\Administrator\Documents\Projects\Mom\Dispatcher` only
2. Never delete files without explicit user request
3. Keep placeholder comments (`# TODO:`) as-is until user asks to implement
4. After ANY change, update `docs/MILESTONE_CHECKLIST.md` status
5. Match existing code style (no comments in new code unless asked)
6. Test with `python manage.py runserver` before marking tasks complete

## When Implementing a Placeholder
- Remove the commented-out code block
- Replace with real implementation
- Keep the same file/location
- Run migrations if models change
- Update the checklist

## Tech Stack Conventions
- Backend: Django 5 + Python 3.11+
- Frontend: Plain HTML/CSS/JS (no framework)
- Database: SQLite (dev), PostgreSQL (prod future)
- Config: django-decouple + .env file
- Static files: served from /static/ dir

## File Naming
- Python: snake_case (e.g., `carrier_form.html`)
- Templates: snake_case
- CSS/JS: main.css / main.js (single file for now)

## Never Do
- Add npm/frontend build tools without asking
- Change settings.py SECRET_KEY without asking
- Add third-party Django packages without asking
- Commit to git without asking
