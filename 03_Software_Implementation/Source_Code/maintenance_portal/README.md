# Automation of Help Desk, Project Tracking and Field Report of Maintenance Department (UI)

A web-based information system that automates the three core functions of a
maintenance department — **help desk ticketing**, **project tracking** and
**field reporting** — within a single application with a user-friendly,
responsive interface.

Developed as a CSC 476 (Semester Project), Department of Computer Science,
Faculty of Science, University of Ibadan, Nigeria.

## Problem being solved

Maintenance departments often run their help desk, project tracking and field
reporting on paper logbooks, phone calls and spreadsheets. This causes lost
requests, no ticket tracking, verbal (untraceable) task assignment, delayed
paper reports and no timely management information. This system replaces those
manual processes with a central database, unique tickets, defined statuses and
real-time dashboards.

## Objectives

1. Automate help desk ticketing (submit, assign, update, close tickets with priorities and full history).
2. Provide project tracking (projects, tasks, assignees, deadlines, progress monitoring).
3. Provide structured field reporting by technicians (location, equipment, findings, action taken).
4. Provide role-based access (Administrator, Supervisor, Technician, Staff) and a reporting dashboard.

## Main features

- **Role-based authentication** — four roles with different access rights; passwords stored as salted hashes.
- **Help desk module** — staff submit tickets (title, category, priority, description); every ticket gets a unique ID; supervisors assign tickets to technicians; technicians update status (Open, In Progress, Resolved, Closed) and add comments; every change is logged with author and time; staff track their own tickets.
- **Project tracking module** — supervisors create maintenance projects and tasks, assign tasks to technicians, set deadlines; technicians update progress; overall project progress is computed automatically.
- **Field report module** — technicians file structured field reports (location, equipment, findings, action taken, date), optionally linked to a ticket; supervisors review them.
- **Dashboard and reports** — counts of tickets/projects/tasks/reports by status, a tickets-by-status chart, and filterable summary listings (status, priority, date range).
- **User management** — administrators create accounts and assign roles.
- **Responsive UI** — works on desktop and mobile browsers.

## Technologies used

| Technology | Purpose |
|---|---|
| Python 3.13 | Application language |
| Flask | Web framework (routing, templating integration) |
| Flask-SQLAlchemy | Database ORM |
| Flask-Login | Session authentication |
| Werkzeug | Password hashing, security utilities |
| SQLite | Database |
| Jinja2 | Server-side HTML templates |
| HTML5 / CSS3 | User interface |
| pytest | Automated testing |

## System requirements

- Python 3.10 or later
- Any modern web browser (Chrome, Firefox, Edge)
- No other system dependencies (SQLite is built into Python)

## Installation

```bash
# 1. Copy or clone this folder to your computer
# 2. Open a terminal inside the project folder
# 3. Create a virtual environment
python -m venv venv

# 4. Activate it
#    Windows:
venv\Scripts\activate
#    Linux / macOS:
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and edit the values (optional — sensible defaults
are built in):

```
SECRET_KEY=change-me-to-a-long-random-string
DATABASE_URL=sqlite:///maintenance.db
```

## Database setup

Tables are created automatically on first run. To load demonstration data
(users, tickets, projects, tasks and field reports), run:

```bash
python seed.py
```

Default accounts (change the admin password after first login):

| Role | Email | Password |
|---|---|---|
| Administrator | admin@maintenance.local | admin123 |
| Supervisor | supervisor@maintenance.local | supervisor123 |
| Technician | tech@maintenance.local | tech123 |
| Staff | staff@maintenance.local | staff123 |

## How to run

```bash
python app.py
```

Then open <http://127.0.0.1:5000> in your browser and sign in.

## How to test

```bash
python -m pytest tests/ -v
```

The suite covers authentication, role-based access control, ticket lifecycle
(create, assign, comment, close), ticket visibility per role, project and task
management, task progress updates, field reports, dashboard counts and report
filters.

## Project structure

```
maintenance_portal/
├── app.py                  # application entry point (create_app factory)
├── config.py               # configuration (secret key, database URI)
├── extensions.py           # shared SQLAlchemy and LoginManager objects
├── models.py               # User, Ticket, TicketUpdate, Project, Task, FieldReport
├── auth.py                 # login, logout, role-based access, user management
├── helpdesk.py             # ticket routes
├── projects.py             # project and task routes
├── reports.py              # field report routes
├── dashboard.py            # dashboard and summary report routes
├── seed.py                 # demo data loader
├── requirements.txt        # dependencies
├── templates/              # Jinja2 HTML templates
├── static/                 # CSS
└── tests/                  # pytest test suite
```

## Screenshots

See the `figures/` folder of the project documentation (Chapter Four of the
final report) for screenshots of the login page, dashboard, tickets, ticket
detail, projects, field report form and reports pages.

## Known limitations

- Runs on the Flask development server (for demonstration); deploy to a
  production WSGI server for live use.
- Single department; no spare-parts inventory, billing, SMS/e-mail gateway or
  native mobile app (see future work in the final report).

## Team members' roles

*(To be completed by the Team Leader — see the Team Members' Participation
Input section in the front matter of the final report.)*

## Acknowledgements

Developed at the Department of Computer Science, University of Ibadan, in
partial fulfilment of the requirements for the B.Sc. in Computer Science.
Thanks to our project supervisor and the department's staff.

## References

See the References section of the final project report. Key sources include
ITIL 4 (Axelos, 2019), the U.S. DOE O&M Best Practices Guide (2010), Korka,
Oloufa and Thomas (1997), Swanson (1997), Pandarkar (2025), Wonohardjo, Putra
and Yossy (2022), Fachrizal, Wibawa and Afifah (2020), Hambali, Anisyah and
Arianti (2024), and the official Flask documentation (The Pallets Projects, 2024).
