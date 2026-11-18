\newpage

# CHAPTER TWO: REVIEW OF RELEVANT LITERATURES

## 2.1 Conceptual Review

### 2.1.1 Help desk and ticketing systems

A help desk is the single point of contact between the users of a service and the unit that provides the service (Axelos, 2019). A ticketing system converts every reported fault or service request into a ticket that carries a unique identifier, a category, a priority, a status and a complete history of the actions taken (Wonohardjo, Putra and Yossy, 2022). The typical ticket lifecycle runs from logging, through categorisation, prioritisation and assignment, to resolution, verification and closure; at every stage the reporter can be kept informed (Axelos, 2019). Studies of web-based help desk systems report reduced response times, better tracking and improved user satisfaction when organisations move from telephone, e-mail and paper-based reporting to a centralised ticketing platform (Cahyadi and Ramayanti, 2025).

### 2.1.2 Maintenance management and computerized maintenance management systems

Maintenance is the combination of technical and administrative actions intended to retain or restore equipment to a state in which it can perform its required function (Korka, Oloufa and Thomas, 1997). A computerized maintenance management system (CMMS) is a software platform that supports the management and tracking of maintenance activities, typically providing work-order generation, prioritisation and tracking, historical records, preventive-maintenance scheduling and real-time reporting (U.S. Department of Energy, 2010). A CMMS gives organisations tighter control of resources, better cost management, improved scheduling, integration with other systems and reduced breakdowns (Swanson, 1997). Recent reviews describe CMMS as having evolved from simple record-keeping tools into data-driven platforms organised around work-order management, inventory, asset management and preventive/predictive maintenance (Pandarkar, 2025). Work-order management is considered the workflow backbone of a CMMS: it covers fault reporting, ticket generation, assignment and monitoring through to closure (Pandarkar, 2025).

### 2.1.3 Project tracking and project management information systems

A project management information system (PMIS) is a web-based or computerised system that supports the planning, execution, monitoring and control of projects (Fachrizal, Wibawa and Afifah, 2020). Core capabilities include creating projects, breaking them into tasks, allocating tasks to team members, setting deadlines and milestones, monitoring progress and expenditure, and generating reports for decision-making (Hambali, Anisyah and Arianti, 2024; Bellah, Chen and Zimmer, 2018). Web-based PMIS further allow documents to be uploaded and shared centrally, reducing document loss, improving financial control and making delays visible early (Fachrizal, Wibawa and Afifah, 2020).

### 2.1.4 Web-based information systems

A web-based information system is an application that users access through a web browser while the data is stored in a central database on a server (Sommerville, 2016). Compared with desktop and paper-based systems, web systems offer anytime, anywhere access, support for many users at once, easier updates (a single deployment point) and lower hardware requirements on the client side (Pressman and Maxim, 2020). These properties make them suitable for a maintenance department whose staff are distributed across offices and field locations.

## 2.2 Theoretical and Technical Framework

### 2.2.1 ITIL service management framework

The Information Technology Infrastructure Library (ITIL) is a widely adopted framework of best practices for IT service management (Axelos, 2019). Its service desk and incident management practices recommend a single point of contact for users, standardised logging and categorisation of incidents, prioritisation based on impact and urgency, defined escalation paths, resolution with verification, and continual measurement of performance. The proposed help desk module follows these practices: every fault is logged as a ticket with a category and priority, assigned to a technician, tracked through defined statuses and closed only after resolution.

### 2.2.2 CMMS functional framework

The CMMS framework described by the U.S. Department of Energy (2010) identifies the core functions of maintenance software: work-order generation, prioritisation and tracking; historical tracking of work orders; scheduling of preventive and corrective maintenance; storage of procedures and technical documentation; real-time reporting; and tracking of labour and parts. The proposed system adopts the work-order (ticket), tracking and reporting functions, adapted to a departmental scale.

### 2.2.3 Software quality model

The quality of the proposed system is assessed against the ISO/IEC 25010 software quality model, which defines characteristics including functional suitability, reliability, usability, security, performance efficiency, maintainability and portability (International Organization for Standardization, 2011). The non-functional requirements in Chapter Three are derived from this model.

### 2.2.4 Software development life cycle models

System development followed the iterative/incremental life cycle: requirements, design, implementation and testing are repeated in short cycles with feedback at each cycle (Sommerville, 2016; Pressman and Maxim, 2020). This was chosen over the waterfall model because requirements were expected to change as the system was demonstrated to users.

## 2.3 Review of Existing Systems

Several commercial systems provide one or two of the functions required by this project:

### 2.3.1 ManageEngine ServiceDesk Plus

A commercial IT service desk tool implementing ITIL processes such as incident management, with ticketing, automation and reporting (ManageEngine, n.d.). It is powerful but commercial, generic, and not tailored to a maintenance department's project tracking and field reporting needs.

### 2.3.2 WorkTrek

A cloud CMMS that manages work orders, assets and field activities, with a mobile app that allows technicians to receive, complete and close work orders in the field (WorkTrek, n.d.). It is commercial (subscription-priced) and offered as a hosted service.

### 2.3.3 Oxmaint

A mobile-first CMMS that gives field technicians work orders, asset history, photos, checklists and offline synchronisation (Oxmaint, n.d.). Its strength is field mobility; however, it is a commercial product and is not integrated with lightweight project tracking for departmental use.

### 2.3.4 FlowPath

A CMMS aimed at higher-education facilities, offering work-order management, mobile access for technicians, real-time reporting and analytics (FlowPath, n.d.). It shows that universities are an active market for such systems, but again it is commercial and modular rather than a single integrated departmental tool.

Common limitations of these commercial systems for this project: subscription cost, closed source code, dependence on the vendor's platform (a problem also reported by Wonohardjo, Putra and Yossy, 2022), and features that either exceed or miss the specific needs of a small maintenance department.

## 2.4 Review of Related Studies

**2.4.1 Korka, Oloufa and Thomas (1997)** studied the use of CMMS in three naval bases with about 1,200 facilities. They found that a CMMS supports maintenance reporting, planning, scheduling, material and work-order control, and — importantly — serves as a platform for analysing maintenance information to support decision-making. Their work underlines the value of a central maintenance database, which this project adopts.

**2.4.2 Swanson (1997)** examined the design and use of CMMS and identified benefits including tighter resource control, better cost management and auditability, the ability to schedule complex workloads, integration with other business systems and reduced breakdowns through improved asset reliability.

**2.4.3 Wonohardjo, Putra and Yossy (2022)** designed and implemented a web-based help desk ticketing system for PT DENSO Indonesia to replace an under-used IBM Lotus Notes system. Using Extreme Programming and UML, they produced a system independent of any platform provider, with a completion rate of 86% in a problem-reporting scenario tested with 15 participants. Their study confirms both the feasibility of web-based ticketing and the cost of vendor dependence.

**2.4.4 Wicaksono and Baswara (2020)** designed and implemented a web-based helpdesk information system using the Extreme Programming method, demonstrating that agile methods suit help desk development.

**2.4.5 Cahyadi and Ramayanti (2025)** developed a web-based helpdesk ticketing application for PT Centrepark Citra Corpora using an agile/RAD approach. The system provides role-based login, ticket management, technician reporting, status notifications and report generation, and it addressed the problems of a manual service process.

**2.4.6 Pandarkar (2025)**, in a comprehensive review of CMMS literature, identified four functional domains — work-order management, inventory, asset management and preventive/predictive maintenance — and noted that mobile-enabled CMMS features (technician apps, barcode scanning) reduce the latency between fault detection and work-order closure. The present project implements the work-order domain with web-based field reporting.

**2.4.7 Fachrizal, Wibawa and Afifah (2020)** designed a web-based project management information system for construction projects using the prototype method. The system manages project work and financial data, allows direct document upload (minimising document loss), and improves financial control and delay monitoring.

**2.4.8 Hambali, Anisyah and Arianti (2024)** analysed and designed a web-based project management system that helps a company manage programmer tasks and monitor project budgets from initiation to completion of the project scope.

**2.4.9 Hariyanto et al. (2025)** designed a web-based information system for monitoring final-year projects, replacing a manual process built on Google Classroom, Google Forms and WhatsApp. Using UML modelling, they achieved better efficiency, transparency, accuracy, tracking, security and communication — evidence that web-based monitoring systems outperform manual and semi-digital processes in academic units.

**2.4.10 Bellah, Chen and Zimmer (2018)** designed and implemented a web-based project management information system that supports project tracking and collaboration, confirming the feasibility of low-cost web technologies for project tracking.

## 2.5 Comparison of Existing Approaches

Table 2.1 compares the reviewed systems and studies against the three functions of this project.

Table 2.1: Comparison of existing systems and studies with the proposed system

| System / study | Help desk ticketing | Maintenance work orders | Project tracking | Field reporting | Role-based access | Reporting | Access model |
|----------------|---------------------|-------------------------|------------------|-----------------|-------------------|-----------|--------------|
| Wonohardjo, Putra and Yossy (2022) | Yes | No | No | No | Not stated | Efficiency metrics | Open (academic) |
| Cahyadi and Ramayanti (2025) | Yes | Partial (technician reporting) | No | No | Yes | Yes | Open (academic) |
| Wicaksono and Baswara (2020) | Yes | No | No | No | Not stated | Not stated | Open (academic) |
| Pandarkar (2025) — CMMS domain | Yes (work orders) | Yes | No | Partial | Varies | Yes | Mixed |
| Fachrizal, Wibawa and Afifah (2020) | No | Partial (works) | Yes | No | Not stated | Yes | Open (academic) |
| Hambali, Anisyah and Arianti (2024) | No | No | Yes | No | PM / programmer roles | Yes | Open (academic) |
| Hariyanto et al. (2025) | No | No | Yes (monitoring) | No | Yes | Yes | Open (academic) |
| Bellah, Chen and Zimmer (2018) | No | No | Yes | No | Yes | Yes | Open (academic) |
| ManageEngine ServiceDesk Plus | Yes | No | No | No | Yes | Yes | Commercial |
| WorkTrek / Oxmaint / FlowPath (CMMS) | Yes (work orders) | Yes | Partial | Yes (mobile field) | Yes | Yes | Commercial |
| **Proposed system** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Open-source, low-cost** |

## 2.6 Identified Research and Practical Gap

The review shows that existing solutions fall into two groups. Commercial CMMS and service-desk products are powerful but expensive, closed-source and dependent on the vendor's platform (Wonohardjo, Putra and Yossy, 2022; WorkTrek, n.d.; Oxmaint, n.d.; FlowPath, n.d.). Academic systems are low-cost and open, but each addresses only one function — help desk ticketing (Wonohardjo, Putra and Yossy, 2022; Wicaksono and Baswara, 2020; Cahyadi and Ramayanti, 2025) or project tracking (Fachrizal, Wibawa and Afifah, 2020; Hambali, Anisyah and Arianti, 2024; Hariyanto et al., 2025; Bellah, Chen and Zimmer, 2018) — and none integrates help desk, project tracking and field reporting in a single lightweight web application for a maintenance department. Field reporting by technicians, in particular, is treated as an attachment to work orders in commercial CMMS rather than as a first-class module.

The gap addressed by this project is therefore: **an integrated, low-cost, role-based web application that combines help desk ticketing, project tracking and structured field reporting for a maintenance department, with a simple user interface and a central database for reporting.** The proposed system fills this gap, as summarised in the last row of Table 2.1.

## 2.7 Chapter Summary

This chapter reviewed the concepts of help desk ticketing, maintenance management (CMMS), project tracking (PMIS) and web-based information systems; the ITIL, CMMS and ISO/IEC 25010 frameworks that inform the design; commercial systems that provide parts of the required functionality; and ten related academic studies. A comparison of existing approaches revealed the gap — the absence of an integrated, low-cost system combining all three functions — which this project addresses.
