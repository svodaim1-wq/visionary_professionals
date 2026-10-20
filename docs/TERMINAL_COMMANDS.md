# Terminal Commands Guide

## Initial Setup (run once)
```powershell
# Create virtual environment
python -m venv venv

# Activate it (PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create environment file
Copy-Item .env.example .env
```

## Daily Development
```powershell
# Activate venv (each new terminal session)
.\venv\Scripts\Activate.ps1

# Run migrations (after model changes)
python manage.py makemigrations
python manage.py migrate

# Start dev server
python manage.py runserver

# Run tests
python manage.py test
```

## Admin Setup
```powershell
# Create superuser for /admin
python manage.py createsuperuser
```

## After Pulling Changes
```powershell
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
```
