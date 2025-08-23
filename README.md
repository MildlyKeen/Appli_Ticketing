# Appli_Ticketing

Django-Based app for ticketing and reports with dashboards

## Features
- User authentication (unique email, strong password policy)
- Ticket creation, editing, deletion, assignment
- Ticket grouping by project/team (admin approval)
- Dashboard and reporting
- Responsive, modern UI (Bootstrap, Google Fonts)
- Secure coding practices
- Session management (10 min inactivity, expires on browser close)
- Admin-only group creation and ticket inclusion
- Error handling and validation feedback

## Setup
1. Clone the repo
2. Create and activate a Python virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```

## CI/CD
- Automated tests, linting, and migrations via GitHub Actions (`.github/workflows/django.yml`)

---

For more details, see the code and templates in the `appli_ticketing` and `tickets` folders.
