\newpage

# CHAPTER FIVE: SUMMARY, CONCLUSION AND RECOMMENDATION

## 5.1 Summary

This project set out to automate the help desk, project tracking and field reporting functions of a maintenance department. Chapter One introduced the problem: manual, paper-based processes cause lost records, poor accountability and delayed information. Chapter Two reviewed the concepts of help desk ticketing, CMMS, project tracking and web-based information systems, the ITIL and ISO/IEC 25010 frameworks, commercial systems and ten related academic studies, and identified the gap of an integrated, low-cost system combining all three functions. Chapter Three described the methodology: analysis of the existing system, UML design (use-case, data-flow, class and entity-relationship diagrams), interface design and an iterative development approach. Chapter Four described the implementation of the web application using Python, Flask and SQLite, and the testing strategy and results.

## 5.2 Achievement of Project Objectives

Table 5.1: Achievement of project objectives

| Objective | Status |
|-----------|--------|
| 1. Analyse the existing manual processes | Achieved (Section 3.1) |
| 2. Elicit and document the requirements | Achieved (Sections 3.4, 3.5) |
| 3. Design the system (UML and UI) | Achieved (Sections 3.6–3.11) |
| 4. Implement the web application with three modules | Achieved (Sections 4.3–4.5) |
| 5. Implement role-based authentication | Achieved (Section 4.5) |
| 6. Implement the ticket lifecycle | Achieved (Section 4.5) |
| 7. Implement project tracking | Achieved (Section 4.5) |
| 8. Implement field reporting | Achieved (Section 4.5) |
| 9. Test and evaluate the system | Addressed in Chapter Four; to be concluded after final testing |

## 5.3 Conclusion

The project has produced a working, web-based information system that automates help desk ticketing, project tracking and field reporting for a maintenance department within a single application, with role-based access and a reporting dashboard. The system replaces paper logbooks, verbal assignment and delayed paper reports with a central database, unique tickets, defined statuses and real-time summaries. It demonstrates that a small, integrated, open-source web application can meet the operational needs of a maintenance department at low cost, filling the gap identified in Chapter Two.

## 5.4 Recommendations

1. The maintenance department should adopt the system for daily help desk, project and field-report operations.
2. Staff should receive basic training on logging tickets, tracking status and filing reports.
3. The database should be backed up regularly (the SQLite file can simply be copied).
4. Roles should be assigned carefully: only supervisors should assign tickets and create projects.
5. The system should be reviewed after one semester of use and improved based on user feedback.

## 5.5 Suggestions for Future Work

1. A native mobile application for technicians (offline-capable field reporting).
2. Spare-parts inventory management integrated with work orders.
3. E-mail/SMS notifications for ticket assignment and status changes.
4. Integration with IoT sensors for automatic fault detection.
5. Advanced analytics (e.g., frequently failing equipment, mean time to resolve).
6. Deployment on a production web server with HTTPS.

\newpage

## REFERENCES

*(In-text citations follow the Harvard author–date style: (Author, Year); (Author and Author, Year); (Author et al., Year). The reference list follows the APA-style format adopted by the department, using "and" instead of "&". Every entry below is cited in the text, and every in-text citation appears below.)*

- Axelos. (2019). *ITIL foundation: ITIL 4 edition*. TSO.
- Bellah, J., Chen, L., and Zimmer, C. (2018). Design and implementation of a web-based project management information system. *International Journal of Designs for Learning, 9*(1), 158–170. https://doi.org/10.14434/ijdl.v9i1.23344
- Cahyadi, R., and Ramayanti, D. (2025). Transformasi digital layanan internal melalui aplikasi helpdesk ticketing berbasis web di PT Centrepark Citra Corpora [Digital transformation of internal services through a web-based helpdesk ticketing application at PT Centrepark Citra Corpora]. *Jurnal RJTI, 4*(2), 173–179.
- Fachrizal, M. R., Wibawa, J. C., and Afifah, Z. (2020). Web-based project management information system in construction projects. *IOP Conference Series: Materials Science and Engineering, 879*(1), 012064. https://doi.org/10.1088/1757-899X/879/1/012064
- FlowPath. (n.d.). *Facility management software for higher education*. Retrieved October 9, 2026, from https://www.getflowpath.com/facility-management-software-for-higher-education
- Hambali, Y. A., Anisyah, A., and Arianti, A. S. (2024). Analysis and design of web-based project management system. *Journal of Engineering Science and Technology, 19*(3), 996–1009.
- Hariyanto, F., Budiman, T., Yulianto, A. B., and Yasin, V. (2025). Designing a web-based information system for monitoring final projects. *International Journal of Engineering, Science and Information Technology, 5*(2), 142–153. https://doi.org/10.52088/ijesty.v5i2.799
- International Organization for Standardization. (2011). *Systems and software engineering — Systems and software quality models (ISO/IEC 25010:2011)*. ISO.
- Korka, J. W., Oloufa, A. A., and Thomas, H. R. (1997). Facilities computerized maintenance management systems. *Journal of Architectural Engineering, 3*(3), 118–123. https://doi.org/10.1061/(ASCE)1076-0431(1997)3:3(118)
- ManageEngine. (n.d.). *What is IT incident management?* Retrieved October 9, 2026, from https://www.manageengine.com/products/service-desk/it-incident-management/what-is-it-incident-management.html
- Nielsen, J. (1994). *Usability engineering*. Morgan Kaufmann.
- Oxmaint. (n.d.). *Mobile CMMS app for offline field maintenance teams*. Retrieved October 9, 2026, from https://oxmaint.com/article/mobile-cmms-app-offline-field-maintenance-teams
- Pandarkar, R. E. (2025). A comprehensive review of computerized maintenance management systems (CMMS). *International Journal of Advanced Research in Science, Communication and Technology, 5*(2). https://doi.org/10.48175/IJARSCT-29271
- The Pallets Projects. (2024). *Flask documentation (3.x)*. Retrieved October 9, 2026, from https://flask.palletsprojects.com/
- Pressman, R. S., and Maxim, B. R. (2020). *Software engineering: A practitioner's approach* (9th ed.). McGraw-Hill Education.
- Sommerville, I. (2016). *Software engineering* (10th ed.). Pearson.
- Swanson, L. (1997). Computerized maintenance management systems: A study of system design and use. *Production and Inventory Management Journal, 38*(2), 11–15.
- U.S. Department of Energy. (2010). *Operations and maintenance best practices guide: A guide to achieving operational efficiency* (Release 3.0, Chapter 4: Computerized maintenance management systems). Federal Energy Management Program. https://www1.eere.energy.gov/femp/pdfs/OM_4.pdf
- Wicaksono, F., and Baswara, O. S. (2020). Design and implementation of web-based helpdesk information systems using extreme programming methods. *Information Technology Engineering Journals, 5*(2), 88–96.
- Wonohardjo, E. P., Putra, A. H., and Yossy, E. H. (2022). Design of web-based helpdesk ticketing system at PT DENSO Indonesia. *PIKSEL: Penelitian Ilmu Komputer Sistem Embedded and Logic, 10*(1), 1–18. https://doi.org/10.33558/piksel.v10i1.3183
- WorkTrek. (n.d.). *Facility management software*. Retrieved October 9, 2026, from https://worktrek.com/facility-management/

\newpage

## APPENDIX

### APPENDIX A: USER MANUAL

**A.1 Logging in.** Open the application URL in a web browser (e.g., http://127.0.0.1:5000). Enter your email address and password and click **Log in**. The pages you can access depend on your role.

**A.2 Staff (reporter).** Click **Tickets**, then **New Ticket**. Fill in the title, category, priority and description, and submit. To check progress, open **Tickets** and select your ticket; the current status and any technician comments are shown.

**A.3 Technician.** Open **Tickets** to see tickets assigned to you. Open a ticket, add comments and change the status (In Progress, Resolved, Closed). Open **Projects** to see your assigned tasks and update their progress. After completing a job, open **Field Reports**, click **New Report**, and fill in the location, equipment, findings and action taken.

**A.4 Supervisor.** Open **Tickets** to view all tickets and assign them to technicians. Open **Projects** to create maintenance projects, add tasks, assign them and monitor progress. Open **Field Reports** to review reports filed by technicians. Open **Dashboard** and **Reports** for summaries.

**A.5 Administrator.** Open **Users** to create, edit and deactivate accounts and to assign roles (Administrator, Supervisor, Technician, Staff). Administrators can also manage ticket categories.

### APPENDIX B: INSTALLATION GUIDE

**Prerequisites.** A computer with Python 3.10 or later installed (download from https://www.python.org) and a modern web browser.

**Steps.**

1. Copy or unzip the project folder (`maintenance_portal/`) to your computer.
2. Open a terminal/command prompt inside the project folder.
3. Create a virtual environment: `python -m venv venv`
4. Activate it: on Windows, `venv\Scripts\activate`; on Linux/Mac, `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Start the application: `python app.py`
7. Open a browser and go to `http://127.0.0.1:5000`
8. Log in with the seeded administrator account: `admin@maintenance.local` / `admin123` — **change this password after the first login.**

### APPENDIX C: SELECTED SOURCE CODE

The complete source code is in the project repository (`03_Software_Implementation/Source_Code`). Two short excerpts are shown here for illustration.

**C.1 Database models (excerpt from `models.py`).**

```python
class Ticket(db.Model):
    __tablename__ = "tickets"
    ticket_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(20), default="Medium")
    status = db.Column(db.String(20), default="Open")
    reporter_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    technician_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    resolved_at = db.Column(db.DateTime, nullable=True)

    def update_status(self, new_status, author):
        old = self.status
        self.status = new_status
        if new_status == "Closed":
            self.resolved_at = datetime.utcnow
        db.session.add(TicketUpdate(ticket_id=self.ticket_id,
                                    author_id=author.user_id,
                                    old_status=old, new_status=new_status))
        db.session.commit()
```

**C.2 A route example (excerpt from `helpdesk.py`).**

```python
@helpdesk_bp.route("/tickets/new", methods=["GET", "POST"])
@login_required
@role_required("Staff", "Supervisor", "Administrator")
def new_ticket():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            flash("Title is required.", "error")
            return redirect(url_for("helpdesk.new_ticket"))
        ticket = Ticket(title=title,
                        description=request.form.get("description", ""),
                        category=request.form.get("category", "General"),
                        priority=request.form.get("priority", "Medium"),
                        reporter_id=current_user.user_id)
        db.session.add(ticket)
        db.session.commit()
        flash("Ticket submitted.", "success")
        return redirect(url_for("helpdesk.list_tickets"))
    return render_template("new_ticket.html")
```

### APPENDIX D: TEST DOCUMENTATION

- **Unit tests:** located in `tests/`; run with `pytest -v` from the project folder. Tests cover model methods (e.g., `Ticket.update_status()` records history and sets `resolved_at`) and route behaviour.
- **Functional tests:** the fourteen cases in Table 4.1 (TC-01 to TC-14), executed manually through the web interface; results are recorded in Table 4.1 and summarised in Table 4.2.
- **How to reproduce:** follow Appendix B to install and run the application, then perform each test case in Table 4.1 and record the actual result.
