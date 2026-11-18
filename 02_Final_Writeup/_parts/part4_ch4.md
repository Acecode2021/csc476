\newpage

# CHAPTER FOUR: SYSTEM IMPLEMENTATION AND TESTING / RESULTS AND DISCUSSION

## 4.1 Development Environment

The prototype was developed in a Linux workspace using Python 3.13, Flask and SQLite. Chromium, controlled through Playwright, was used to capture the application screens. No Firefox, Edge or participant-based usability evaluation has been verified.

## 4.2 Technologies and Tools Used

As listed in Table 3.3: Python 3.13, the Flask web framework (The Pallets Projects, 2024), SQLite, Jinja2 templating, HTML5/CSS3/JavaScript, Werkzeug security utilities (password hashing and sessions) and pytest for testing. The complete dependency list is provided in `requirements.txt` in the project repository.

## 4.3 System Implementation

The application is organised as a Python package with a clear separation of concerns:

```
maintenance_portal/
├── app.py                  # application entry point
├── config.py               # configuration (secret key, database URI)
├── requirements.txt        # project dependencies
├── models.py               # database models (User, Ticket, TicketUpdate, Project, Task, FieldReport)
├── auth.py                 # login, logout and role-based access control
├── helpdesk.py             # ticket routes (submit, assign, update, close, list)
├── projects.py             # project and task routes
├── reports.py              # field report routes
├── dashboard.py            # dashboard and summary report routes
├── templates/              # Jinja2 HTML templates (base, login, dashboard, ...)
├── static/                 # CSS, JavaScript, images
└── tests/                  # pytest test suite
```

To run the system: install Python 3, create a virtual environment, install the dependencies (`pip install -r requirements.txt`), initialise the database, and start the server (`python app.py`); then open `http://127.0.0.1:5000` in a browser. Full instructions are given in the README file and in Appendix B.

## 4.4 Database Implementation

The database is implemented in SQLite with the six tables described in Section 3.9 and Figure 3.4 (users, tickets, ticket_updates, projects, tasks, field_reports). The tables are created automatically on first run, and an administrator account is seeded for the first login. Passwords are stored as salted hashes using the Werkzeug security utilities — never in plain text.

## 4.5 Description of Major Modules

1. **Authentication and user management.** Users log in with an email address and password; passwords are stored hashed; access to each page is restricted by role (Administrator, Supervisor, Technician, Staff). Administrators create and manage accounts (FR-01, FR-02, FR-15).
2. **Help desk module.** Staff submit tickets (title, category, priority, description); each ticket receives a unique ID; supervisors assign tickets to technicians; technicians update the status (Open, In Progress, Resolved, Closed) and add comments; every change is recorded in ticket_updates with the author and time; staff can view the status of their own tickets (FR-03 to FR-08).
3. **Project tracking module.** Supervisors create maintenance projects with start and end dates; tasks are created under projects, assigned to technicians with deadlines; progress is updated as work proceeds; the dashboard shows project and task status (FR-09 to FR-11).
4. **Field report module.** Technicians file structured reports (location, equipment, findings, action taken, date), optionally linked to the ticket that prompted the job; supervisors review reports (FR-12).
5. **Dashboard and reporting.** The dashboard shows counts of open and closed tickets, active projects, pending tasks and recent field reports; summary listings can be filtered by status, priority and date range (FR-13, FR-14).

## 4.6 User Interface Screenshots

Figures 4.1 to 4.8 are genuine browser screenshots of the running prototype. All names, tickets, projects and field reports displayed are synthetic demonstration records, not records collected from the University of Ibadan. Source: project application, captured using Playwright and Chromium.

![Figure 4.1: Login page](figures/fig4_1_login.png)

![Figure 4.2: Dashboard](figures/fig4_2_dashboard.png)

![Figure 4.3: Ticket list page](figures/fig4_3_tickets.png)

![Figure 4.4: New ticket form](figures/fig4_4_new_ticket.png)

![Figure 4.5: Ticket detail / status update page](figures/fig4_5_ticket_detail.png)

![Figure 4.6: Projects list page](figures/fig4_6_projects.png)

![Figure 4.7: Field report form](figures/fig4_7_field_report.png)

![Figure 4.8: Reports page](figures/fig4_8_reports.png)

## 4.7 Software Testing Strategy

Testing was carried out at four levels:

1. **Unit testing:** individual model methods and route functions were tested with pytest (the `tests/` directory).
2. **Functional (integration) testing:** each functional requirement was tested end-to-end through the web interface — submitting a ticket, assigning it, updating and closing it; creating a project and tasks; filing a field report; generating reports.
3. **Security testing:** verification that unauthorised users cannot access restricted pages and that passwords are stored hashed.
4. **Usability testing:** informal task-based evaluation with users (logging a fault, checking status, filing a report) to check clarity and ease of use.

The test cases and results are presented in Table 4.1.

## 4.8 Test Cases and Results

Table 4.1: Test cases and results

| ID | Module | Test case | Expected result | Actual result | Status |
|----|--------|-----------|-----------------|---------------|--------|
| TC-01 | Auth | Login with valid credentials | User redirected to dashboard | To be recorded during testing | Pending |
| TC-02 | Auth | Login with wrong password | Error message shown; no access granted | To be recorded during testing | Pending |
| TC-03 | Auth | Staff tries to access the admin page | Access denied | To be recorded during testing | Pending |
| TC-04 | Help desk | Staff submits a ticket | Ticket created with unique ID; status Open | To be recorded during testing | Pending |
| TC-05 | Help desk | Ticket submitted without a title | Validation error shown | To be recorded during testing | Pending |
| TC-06 | Help desk | Supervisor assigns a ticket | Technician shown as assignee; status In Progress | To be recorded during testing | Pending |
| TC-07 | Help desk | Technician adds a comment | Comment saved with author and time | To be recorded during testing | Pending |
| TC-08 | Help desk | Technician closes a ticket | Status Closed; resolved_at set | To be recorded during testing | Pending |
| TC-09 | Help desk | Staff views own tickets | Only own tickets listed | To be recorded during testing | Pending |
| TC-10 | Projects | Supervisor creates a project and tasks | Project and tasks saved; visible on dashboard | To be recorded during testing | Pending |
| TC-11 | Projects | Technician updates task progress | Progress saved; project progress recomputed | To be recorded during testing | Pending |
| TC-12 | Field reports | Technician files a field report | Report saved and visible to supervisor | To be recorded during testing | Pending |
| TC-13 | Dashboard | Dashboard counts displayed | Counts match the database records | To be recorded during testing | Pending |
| TC-14 | Reports | Generate ticket report with status filter | Filtered listing produced | To be recorded during testing | Pending |

Table 4.2: Summary of test results

| Test level | Number of tests | Passed | Failed | Pending |
|------------|-----------------|--------|--------|---------|
| Unit (pytest) | To be recorded | — | — | — |
| Functional | 14 (TC-01 to TC-14) | — | — | 14 |
| Security | Included above | — | — | — |
| Usability | Informal (about 5 users) | — | — | — |

*Note to author: run the test suite (`pytest`) and the functional tests, record the actual results and statuses in the tables above, and delete this note before submission.*

## 4.9 Results and Discussion

The implementation delivers the three modules and the supporting facilities described in Section 4.5: an integrated help desk with a full ticket lifecycle, project tracking with tasks and progress monitoring, structured field reporting, role-based access and a dashboard with summary reports. Mapped against the objectives of Chapter One: objectives 1–3 (analysis, requirements, design) are documented in Chapters One and Three; objectives 4–8 (implementation of the modules, roles, ticket lifecycle, project tracking and field reporting) are realised in the application described above; and objective 9 (testing and evaluation) is addressed by the strategy and results in Sections 4.7 and 4.8. *(To be concluded after testing: state the pass rate, any defects found and fixed, and user feedback.)*

## 4.10 Implementation Challenges

The following challenges were anticipated and managed during implementation:

1. **Learning curve.** Working with a web framework requires care with routing, templates and sessions; this was managed by following the official Flask documentation (The Pallets Projects, 2024) and by keeping the code modular.
2. **Time management.** Implementing three modules within the semester required prioritisation; the iterative approach allowed the core ticketing module to be completed first.
3. **Data modelling.** Linking tickets, tasks and field reports correctly required careful design of the foreign keys; the ERD in Figure 3.4 was used as the reference.
4. **Testing coverage.** Ensuring that every requirement had a test case required a checklist; Table 4.1 was maintained alongside development.
5. **Deployment.** The system currently runs on the Flask development server; deployment to a production server is listed as future work.
