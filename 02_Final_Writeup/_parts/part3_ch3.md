\newpage

# CHAPTER THREE: METHODOLOGY

## 3.1 Analysis of the Existing System

The maintenance department studied carries out its work through manual processes:

- **Help desk.** Staff report faults by telephone, WhatsApp or paper form. The help desk officer writes the report in a paper logbook. There is no ticket number, priority or status, and the reporter cannot track progress.
- **Project tracking.** Maintenance projects (e.g., repainting a building, servicing a generator) are planned verbally or in spreadsheets. Tasks are assigned by word of mouth; progress is known only informally.
- **Field reporting.** Technicians write reports on paper after jobs; reports are handed in days later, filed in cabinets or drawers, and are difficult to retrieve.

Data collection for this analysis was done through observation of the department's workflow and informal interviews with maintenance staff (a help desk officer, technicians and a supervisor), supplemented by a review of the department's logbook and report files.

## 3.2 Problems with the Existing System

1. **Loss of records:** paper forms and logbooks are misplaced, damaged or illegible.
2. **No tracking:** requests have no unique identifiers or statuses; nothing can be traced.
3. **Poor accountability:** verbal assignment means responsibility cannot be established.
4. **Delayed information:** field reports reach the office late; management reports are compiled manually, sometimes weeks later.
5. **Duplication and errors:** the same fault may be reported several times through different channels; manual entry introduces errors.
6. **No decision support:** management has no quick view of open tickets, ongoing projects or field activity.

## 3.3 Proposed System

The proposed system is a web-based information system named the **Maintenance Department Portal**. It integrates three modules — **Help Desk**, **Project Tracking** and **Field Reports** — plus a **Dashboard and Reports** facility and **user management**. Four roles are supported: **Administrator** (manages users and categories), **Supervisor** (assigns tickets, creates and monitors projects and tasks, reviews reports), **Technician** (works on assigned tickets and tasks, files field reports) and **Staff** (submits tickets and tracks their status). The system architecture is presented in Section 3.6.

## 3.4 Functional Requirements

Table 3.1 lists the functional requirements of the proposed system.

Table 3.1: Functional requirements of the proposed system

| ID | Requirement | Description |
|----|-------------|-------------|
| FR-01 | User authentication | Users log in with email and password; sessions are maintained securely. |
| FR-02 | Role-based authorisation | Administrator, Supervisor, Technician and Staff have different access rights. |
| FR-03 | Submit ticket | Staff create tickets with title, category, priority and description. |
| FR-04 | Ticket identification | Every ticket receives a unique ID and timestamps. |
| FR-05 | Ticket lifecycle | Ticket status moves Open, In Progress, Resolved, Closed. |
| FR-06 | Assign ticket | Supervisors (and Administrators) assign tickets to technicians. |
| FR-07 | Update ticket | Technicians update status and add comments; changes are recorded with author and time. |
| FR-08 | View tickets | Staff view their own tickets and current status; technicians view assigned tickets; supervisors view all tickets. |
| FR-09 | Create project | Supervisors create maintenance projects with description, start and end dates. |
| FR-10 | Manage tasks | Tasks are created under projects, assigned to technicians, given deadlines and progress values. |
| FR-11 | Monitor progress | Project and task status and progress are visible to supervisors; overall progress is computed. |
| FR-12 | File field report | Technicians file reports with location, equipment, findings, action taken and date, optionally linked to a ticket. |
| FR-13 | Dashboard | A dashboard shows counts of tickets, projects, tasks and reports by status. |
| FR-14 | Generate reports | The system produces listings and summaries of tickets, projects and field reports, filterable by status, priority and date range. |
| FR-15 | Manage users | Administrators create, edit and deactivate user accounts and assign roles. |

## 3.5 Non-Functional Requirements

The non-functional requirements are derived from the ISO/IEC 25010 software quality model (International Organization for Standardization, 2011) and are listed in Table 3.2.

Table 3.2: Non-functional requirements of the proposed system

| Category | Requirement |
|----------|-------------|
| Usability | Simple, consistent interface; responsive layout usable on desktop and mobile browsers; clear feedback messages. |
| Security | Passwords stored as hashes; session-based authentication; role-based authorisation; input validation to prevent common web attacks. |
| Reliability | The system should be available during working hours; data is stored transactionally in the database. |
| Performance | Pages respond within 3 seconds under normal load for a departmental user base. |
| Maintainability | Modular code structure (models, routes, templates); README and inline documentation. |
| Portability | Runs on any operating system with Python 3; usable from any modern web browser. |
| Integrity | Ticket and report records cannot be edited silently; updates are logged with author and time. |

## 3.6 System Architecture

The system follows a **three-tier architecture** (Figure 3.1). The **presentation layer** is the web browser, which renders HTML5 pages styled with CSS3 and enhanced with JavaScript; it is responsive, so it adapts to desktop and mobile screens. The **application layer** is a Flask web server written in Python; it contains the routes (controllers), the business logic and the authentication and authorisation checks. The **data layer** is an SQLite database that stores users, tickets, ticket updates, projects, tasks and field reports. Because the application and data layers sit on a server, any number of staff can use the system concurrently from any device on the network, and updates are deployed in one place.

![Figure 3.1: Three-tier architecture of the proposed system](figures/fig3_1_architecture.png)

## 3.7 Use-Case Diagram

Figure 3.2 shows the use-case diagram of the proposed system. The actors are Staff (reporter), Technician, Supervisor and Administrator.

![Figure 3.2: Use-case diagram of the proposed system](figures/fig3_2_usecase.png)

The key use cases are:

- **Authentication:** every actor logs in and logs out (FR-01, FR-02).
- **Help desk:** Staff submits a ticket and views its status (FR-03, FR-08); Supervisor assigns tickets (FR-06); Technician updates status, adds comments and closes tickets (FR-05, FR-07).
- **Project tracking:** Supervisor creates projects and tasks, assigns tasks and monitors progress (FR-09, FR-10, FR-11); Technician updates task progress (FR-10).
- **Field reporting:** Technician files field reports (FR-12); Supervisor views them.
- **Dashboard and reports:** Supervisor and Administrator view the dashboard and generate reports (FR-13, FR-14).
- **Administration:** Administrator manages users (FR-15).

## 3.8 Data-Flow Diagram

Figure 3.3 shows the Level-0 data-flow diagram (DFD). The system is decomposed into four processes: **1.0 Help Desk Ticketing**, **2.0 Project Tracking**, **3.0 Field Reporting** and **4.0 Dashboard and Reports**, which read from and write to a single data store, **D1 (Maintenance Database)**. Staff supply fault reports and receive ticket statuses; technicians supply status updates and field reports; supervisors supply project and task data and receive summary reports.

![Figure 3.3: Level-0 data-flow diagram of the proposed system](figures/fig3_3_dfd0.png)

## 3.9 Database Design

The database contains six tables (Figure 3.4): **users**, **tickets**, **ticket_updates**, **projects**, **tasks** and **field_reports**. The **users** table stores account details and roles; **tickets** stores help desk tickets with reporter and technician references; **ticket_updates** logs every status change and comment; **projects** and **tasks** store maintenance projects and their tasks; and **field_reports** stores the structured reports filed by technicians.

![Figure 3.4: Entity-relationship diagram of the database](figures/fig3_4_erd.png)

Table 3.4: Database tables and their descriptions

| Table | Description |
|-------|-------------|
| users | User accounts: user_id (PK), name, email (unique), password_hash, role, created_at. |
| tickets | Help desk tickets: ticket_id (PK), title, description, category, priority, status, reporter_id (FK to users), technician_id (FK to users), created_at, updated_at, resolved_at. |
| ticket_updates | Ticket history: update_id (PK), ticket_id (FK), author_id (FK), note, old_status, new_status, created_at. |
| projects | Maintenance projects: project_id (PK), name, description, start_date, end_date, status, created_by (FK to users). |
| tasks | Project tasks: task_id (PK), project_id (FK), title, description, assignee_id (FK to users), deadline, status, progress. |
| field_reports | Field reports: report_id (PK), technician_id (FK), ticket_id (FK, optional), location, equipment, findings, action_taken, report_date, created_at, status. |

## 3.10 UML Diagrams (Class Diagram)

Figure 3.5 shows the class diagram of the proposed system. Each class corresponds to a database table; the classes encapsulate the attributes and the operations that act on them (for example, Ticket.assign(), Ticket.update_status() and Ticket.close(); Project.add_task() and Project.progress(); FieldReport.submit()).

![Figure 3.5: Class diagram of the proposed system](figures/fig3_5_class.png)

## 3.11 Interface Design

The interface was designed with the principles of simplicity, consistency, visibility of status and feedback (Nielsen, 1994): every page shows the logged-in user and role and provides a logout link; forms validate input and show clear error messages; ticket, project and report statuses are shown as coloured labels; and the layout is responsive so that it adapts to desktop and mobile screens. Figures 3.6 and 3.7 show wireframes of the login page and the dashboard.

![Figure 3.6: Wireframe of the login page](figures/fig3_6_wireframe_login.png)

![Figure 3.7: Wireframe of the dashboard page](figures/fig3_7_wireframe_dashboard.png)

## 3.12 Development Methodology

The project used an **iterative (agile-style) life cycle** organised in short cycles: (1) requirements analysis; (2) design (UML and wireframes); (3) implementation of one module at a time; (4) testing of each increment; and (5) review and refinement. This approach was chosen because requirements were refined as prototypes were shown to users, and because it reduces the risk of discovering problems late (Sommerville, 2016; Pressman and Maxim, 2020). Table 3.3 lists the technologies and tools used.

Table 3.3: Technologies and tools used

| Technology / tool | Purpose |
|-------------------|---------|
| Python 3.13 | Programming language for the application layer. |
| Flask (The Pallets Projects, 2024) | Web framework: routing, request handling, templating integration. |
| SQLite | Lightweight relational database. |
| Jinja2 | Server-side HTML templating. |
| HTML5 / CSS3 / JavaScript | User interface structure, styling and client-side behaviour. |
| Werkzeug | Password hashing and session management (part of the Flask ecosystem). |
| pytest | Unit and functional testing. |
| Visual Studio Code | Development environment. |
| Git and GitHub | Version control and source-code repository. |
| Web browser (Chrome / Firefox / Edge) | Running and testing the application. |
