# Appli_Ticketing

A professional Django-based IT ticketing system for teams and organizations.

## Features
- User authentication (unique email, strong password policy)
- Ticket creation, editing, deletion, assignment
- Ticket grouping by project/team (admin approval)
- Dashboard and reporting
- Responsive, modern UI (Bootstrap, Google Fonts)
- Secure coding practices
- Session management (5 min inactivity, expires on browser close)
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

## Fixes
- Migration errors (model mismatch, recursive URL includes)
- NoReverseMatch errors (namespaced URLs)
- Blank/unstyled pages (Bootstrap, tables, separators)
- Restrict group creation and ticket inclusion to admins
- Show assigned user and group info in ticket views

## To Do
- Group management dashboard (view, edit, delete groups)
- Ticket filtering by group/project
- Bulk ticket assignment to groups
- Email notifications for ticket updates
- Advanced reporting and analytics
- REST API for integration
- Docker support for deployment

---

For more details, see the code and templates in the `appli_ticketing` and `tickets` folders.
