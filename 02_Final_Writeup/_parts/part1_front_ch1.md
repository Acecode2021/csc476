<!--TITLEPAGE-->
# AUTOMATION OF HELP DESK, PROJECT TRACKING AND FIELD REPORT OF MAINTENANCE DEPARTMENT (UI)

**BY**

**Ogundele, Tobiloba James — E054654
Aderinto, Kunle Abraham — E055233
Olusola, Ayomide Emmanuel — E055067
Alonge, Ayobami Blessing — E054861**

**SUBMITTED**
**TO**
**THE DEPARTMENT OF COMPUTER SCIENCE,**
**FACULTY OF SCIENCE,**
**UNIVERSITY OF IBADAN, IBADAN, NIGERIA**

**IN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE AWARD OF THE DEGREE OF BACHELOR OF SCIENCE (B.Sc.) IN COMPUTER SCIENCE.**

**October 2026**
<!--/TITLEPAGE-->

\newpage

## CERTIFICATION

This is to certify that this project, **Automation of Help Desk, Project Tracking and Field Report of Maintenance Department (UI)**, was carried out by **[Student Name(s)]** (Matriculation Number(s): **[Matric Number(s)]**) and duly supervised by **[Supervisor Name]**.


..................................................... &nbsp; ..............................
**[Supervisor Name]** &nbsp;&nbsp;&nbsp; Date
(Supervisor)


..................................................... &nbsp;&nbsp; ..............................
**[HOD Name]** &nbsp;&nbsp;&nbsp; Date
(Head of Department)

\newpage

## DEDICATION

This project work is dedicated to the giver of life and wisdom: the Almighty God, and to my family — **[family names]** — for their prayers, patience and unwavering support throughout this programme. *(For a group project: replace "my family" with "our families".)*

\newpage

## ACKNOWLEDGEMENT

I will like to acknowledge the sustaining power of the Almighty God for wisdom, understanding and the grace to complete this project.

My sincere gratitude goes to my project supervisor, **[Supervisor Name]**, for taking the pains to guide, correct and encourage me at every stage of this work. I also acknowledge the Head of Department, **[HOD Name]**, and all the academic and non-academic staff of the Department of Computer Science, University of Ibadan, for making my stay in the department a worthwhile one. God bless you all.

Finally, I appreciate my family, friends and course mates — **[names]** — who supported me directly or indirectly. *(For a group project: use "we" instead of "I" and list all members.)*

\newpage

## TEAM MEMBERS' PARTICIPATION INPUT

*(To be prepared and submitted by the Team Leader only. If this is a solo project, delete this section. If your lecturer requires this section elsewhere, move it to the position specified.)*

| S/N | Full Name | Matriculation Number | Assigned Task / Responsibility | Work Completed |
|-----|-----------|----------------------|--------------------------------|----------------|
| 1 | [Full Name] | [Matric No.] | [e.g., Team Leader; requirements analysis; documentation; coordination] | [Describe actual contribution] |
| 2 | [Full Name] | [Matric No.] | [e.g., System analysis and design; UML diagrams; database design] | [Describe actual contribution] |
| 3 | [Full Name] | [Matric No.] | [e.g., Implementation; testing; user manual] | [Describe actual contribution] |

*Note: contributions must reflect the actual work performed by each member. Do not invent participation.*

\newpage

## ABSTRACT

Maintenance departments are responsible for keeping the facilities, equipment and infrastructure of an organisation in safe and serviceable condition. In many organisations, including university maintenance units, the three core information processes that support this work — help desk fault reporting, project tracking and field reporting — are still carried out manually through paper forms, logbooks, telephone calls and informal messaging. This manual approach leads to lost requests, duplicated effort, poor accountability and delayed management information. This project therefore addresses the automation of the help desk, project tracking and field report functions of a maintenance department through a single, integrated web-based information system with a user-friendly interface (UI).

The project was carried out using an iterative (agile-style) software development methodology. The existing manual processes were analysed through observation and informal interviews with maintenance staff; the proposed system was modelled with Unified Modeling Language (UML) use-case, data-flow, class and entity-relationship diagrams; and the system was implemented as a web application using Python, the Flask web framework, SQLite and HTML/CSS/JavaScript, with role-based authentication and authorisation for four user roles: Administrator, Supervisor, Technician and Staff. The system comprises three integrated modules — a help desk ticketing module, a project tracking module and a field report module — supported by a dashboard and a reporting facility.

The implemented system enables staff to log and track faults as tickets with unique identifiers, priorities and statuses; supervisors to create maintenance projects, allocate tasks and monitor progress; technicians to file structured field reports from completed jobs; and management to obtain real-time summaries and reports from a dashboard. The system was evaluated through unit, functional and usability testing, and the results, presented in Chapter Four, show that the stated objectives were met. The project demonstrates that an integrated, low-cost, web-based solution can effectively replace manual processes in a maintenance department.

\newpage

## TABLE OF CONTENTS

*(Page numbers are indicative — update them after final formatting in Microsoft Word.)*

- Title Page (unnumbered)
- Certification ... i
- Dedication ... ii
- Acknowledgement ... iii
- Team Members' Participation Input ... iv
- Abstract ... v
- Table of Contents ... vi
- List of Figures ... vii
- List of Tables ... viii
- CHAPTER ONE: INTRODUCTION ... 1
  - 1.1 Preamble ... 1
  - 1.2 Statement of Problems ... 2
  - 1.3 Aim and Objectives ... 3
  - 1.4 Justification ... 4
  - 1.5 Scope of Study ... 4
  - 1.6 Methodology ... 5
- CHAPTER TWO: REVIEW OF RELEVANT LITERATURES ... 7
- CHAPTER THREE: METHODOLOGY ... 14
- CHAPTER FOUR: SYSTEM IMPLEMENTATION AND TESTING / RESULTS AND DISCUSSION ... 24
- CHAPTER FIVE: SUMMARY, CONCLUSION AND RECOMMENDATION ... 32
- REFERENCES ... 34
- APPENDIX ... 36

\newpage

## LIST OF FIGURES

- Figure 3.1: Three-tier architecture of the proposed system ... 15
- Figure 3.2: Use-case diagram of the proposed system ... 17
- Figure 3.3: Level-0 data-flow diagram of the proposed system ... 18
- Figure 3.4: Entity-relationship diagram of the database ... 19
- Figure 3.5: Class diagram of the proposed system ... 20
- Figure 3.6: Wireframe of the login page ... 21
- Figure 3.7: Wireframe of the dashboard page ... 21
- Figure 4.1: Login page ... 25
- Figure 4.2: Dashboard ... 25
- Figure 4.3: Ticket list page ... 26
- Figure 4.4: New ticket form ... 26
- Figure 4.5: Ticket detail / status update page ... 27
- Figure 4.6: Projects list page ... 27
- Figure 4.7: Field report form ... 28
- Figure 4.8: Reports page ... 28

\newpage

## LIST OF TABLES

- Table 2.1: Comparison of existing systems and studies with the proposed system ... 12
- Table 3.1: Functional requirements of the proposed system ... 15
- Table 3.2: Non-functional requirements of the proposed system ... 16
- Table 3.3: Technologies and tools used ... 22
- Table 3.4: Database tables and their descriptions ... 19
- Table 4.1: Test cases and results ... 29
- Table 4.2: Summary of test results ... 30
- Table 5.1: Achievement of project objectives ... 33

\newpage

# CHAPTER ONE: INTRODUCTION

## 1.1 Preamble

Every organisation depends on the effective functioning of its physical facilities — buildings, equipment, power, water and other infrastructure. The unit charged with keeping these facilities in serviceable condition is the maintenance department. Maintenance may be defined as the combination of all technical and administrative actions intended to retain an item, equipment or facility in, or restore it to, a state in which it can perform its required function (Korka, Oloufa and Thomas, 1997; U.S. Department of Energy, 2010).

The work of a maintenance department generates three broad streams of information. First, faults and service requests from staff and occupants must be received, recorded and resolved — the function of a help desk. Second, planned maintenance works and improvement works must be organised as projects, broken into tasks, assigned and monitored to completion — the function of project tracking. Third, technicians who carry out work in the field must document what they found and what they did — the function of field reporting. Together, these three functions determine how quickly faults are resolved, how well projects are delivered and how reliable the department's records are.

In many organisations, including university maintenance units in Nigeria, these three functions are still performed manually: faults are reported by telephone call, WhatsApp message or a handwritten note; the help desk officer writes entries into a paper logbook; supervisors assign jobs verbally; projects are tracked in spreadsheets or in the memory of officers; and technicians submit paper field reports that are easily misplaced. Such processes are slow, error-prone and difficult to audit.

Information and communication technology has changed this picture. A computerized maintenance management system (CMMS) is now widely regarded as a centralised database that connects maintenance teams, assets and operational data, allowing work orders to be generated, assigned and monitored and maintenance history to be analysed (Swanson, 1997; Pandarkar, 2025). Similarly, web-based help desk ticketing systems have been shown to improve the management of client issues by giving every complaint a unique ticket, a status, a priority and a history (Wonohardjo, Putra and Yossy, 2022; Cahyadi and Ramayanti, 2025), while web-based project management information systems enable managers to allocate tasks, monitor progress and control costs (Fachrizal, Wibawa and Afifah, 2020; Hambali, Anisyah and Arianti, 2024). A web-based information system is a software application that users access through a web browser, with data stored in a central database, and it offers advantages of accessibility from any device, reduced software installation costs and easier maintenance (Sommerville, 2016).

This project, carried out in fulfilment of the requirements of CSC 476 (Semester Project), designs and implements a web-based information system that automates the three core functions of a maintenance department — help desk, project tracking and field reporting — within a single application, with emphasis on a clean and user-friendly user interface (UI). The system is intended for a typical university maintenance department, where staff report faults, supervisors coordinate maintenance projects and technicians execute jobs and file reports.

## 1.2 Statement of Problems

The maintenance department studied relies on manual processes for its help desk, project tracking and field reporting functions. This gives rise to the following problems:

1. Fault reports made by telephone, WhatsApp or on paper are easily forgotten, duplicated or lost, because there is no central register of requests.
2. There are no unique ticket numbers, priorities or statuses, so neither the reporter nor management can track the progress of a request.
3. Supervisors assign jobs verbally or by note, so technicians are unclear about their workload and management cannot measure performance.
4. Maintenance projects are planned and tracked in spreadsheets or memory, so delays, cost overruns and incomplete tasks are noticed late, if at all.
5. Field reports are written on paper; sheets are misplaced or damaged, entries are illegible, and reports reach the office days after the work is done.
6. Management has no reliable, timely reports on tickets, projects and field activities, which weakens planning and decision-making.

These problems create delays, loss of records, poor accountability and low productivity. There is therefore a need for a single, integrated, web-based system that automates help desk ticketing, project tracking and field reporting for the maintenance department.

## 1.3 Aim and Objectives

**Aim:** To design and implement a web-based information system for the automation of help desk, project tracking and field reporting in a maintenance department, with a user-friendly interface.

**Objectives:**

1. To analyse the existing manual processes of help desk, project tracking and field reporting in the maintenance department.
2. To elicit and document the functional and non-functional requirements of the proposed system.
3. To design the system using UML models, including use-case, data-flow, class and entity-relationship diagrams, and to design the user interface.
4. To implement the system as a web application with three integrated modules — help desk ticketing, project tracking and field reporting — plus a dashboard and reporting facility.
5. To implement role-based authentication and authorisation for four roles: Administrator, Supervisor, Technician and Staff.
6. To implement a ticket lifecycle (Open, In Progress, Resolved, Closed) with priorities, assignment and status updates.
7. To implement project tracking with tasks, assignees, deadlines and progress monitoring.
8. To implement structured field reporting by technicians, including location, equipment, findings and action taken.
9. To test the system through unit, functional and usability testing and to evaluate it against the stated requirements.

## 1.4 Justification

This project is justified for the following reasons:

1. **Efficiency.** Automating ticketing, tracking and reporting removes repetitive manual work and shortens the time between fault report and resolution. Structured incident logging, prioritisation and assignment are core service desk practices recommended by the ITIL framework (Axelos, 2019).
2. **Accountability.** Every ticket, task and field report has an owner, a status and timestamps, so responsibility can always be traced and performance can be measured.
3. **Reliable records.** A central database preserves maintenance history, which is the basis for planning, budgeting and analysis (Korka, Oloufa and Thomas, 1997; U.S. Department of Energy, 2010).
4. **Better decisions.** Dashboards and summary reports give management timely information on workload, progress and backlogs.
5. **Low cost.** The system is built with free, open-source technologies (Python, Flask, SQLite), so it avoids licence fees and vendor lock-in, a problem noted by Wonohardjo, Putra and Yossy (2022) in systems that depend on a platform provider.
6. **Accessibility.** Being web-based, the system can be used from any computer or mobile browser on the organisation's network, which suits technicians who are mostly in the field.
7. **Digital transformation.** The project supports the university's broader goal of moving service delivery from paper to digital platforms.

## 1.5 Scope of Study

**Scope.** The system covers a single maintenance department (used as a case study: a university maintenance unit) and three functional areas:

1. **Help desk ticketing** — staff submit fault/service tickets; tickets carry a unique ID, category, priority and status; supervisors assign tickets to technicians; technicians update status and add comments; tickets are resolved and closed; staff can view the status of their own tickets.
2. **Project tracking** — supervisors create maintenance projects, define tasks, assign tasks to technicians, set deadlines and monitor progress and status until completion.
3. **Field reporting** — technicians file structured field reports for jobs carried out (location, equipment, findings, action taken, date), which supervisors and management can review.
4. **Dashboard and reports** — summary counts and listings of tickets, projects, tasks and field reports, filterable by status, priority, date and personnel.
5. **User management** — role-based accounts (Administrator, Supervisor, Technician, Staff) with secure login.

**Limitations (delimitations).** The system does not include spare-parts inventory management, contractor billing or invoicing, a native mobile application, SMS/e-mail gateway integration, or IoT sensor integration. It is deployed on a local web server and is intended for a single department. These are deliberate boundaries that keep the project achievable within the semester; they are listed as future work in Chapter Five.

## 1.6 Methodology

The project was carried out using an iterative (agile-style) software development methodology, described in detail in Chapter Three. In summary: (i) the existing manual processes were analysed through observation and informal interviews; (ii) the requirements of the proposed system were documented; (iii) the system was designed with UML diagrams (use-case, data-flow, class and entity-relationship diagrams) and wireframes for the user interface; (iv) the system was implemented as a web application using Python 3, the Flask framework, SQLite, Jinja2 templates and HTML/CSS/JavaScript; (v) the system was tested at unit, integration (functional) and system level, including usability checks; and (vi) the source code was organised into a Git repository with installation documentation. The choice of an iterative approach allows feedback and corrections at each cycle (Pressman and Maxim, 2020; Sommerville, 2016).
