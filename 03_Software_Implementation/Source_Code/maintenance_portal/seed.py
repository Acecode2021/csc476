from datetime import date, datetime, timedelta

from app import create_app
from extensions import db
from models import FieldReport, Project, Task, Ticket, User

app = create_app()


def seed():
    with app.app_context():
        if User.query.first():
            print("Database already seeded.")
            return
        admin = User(name="System Administrator", email="admin@maintenance.local",
                     role="Administrator")
        admin.set_password("admin123")
        supervisor = User(name="Maintenance Supervisor", email="supervisor@maintenance.local",
                          role="Supervisor")
        supervisor.set_password("supervisor123")
        tech1 = User(name="John Technician", email="tech@maintenance.local", role="Technician")
        tech1.set_password("tech123")
        tech2 = User(name="Mary Field", email="tech2@maintenance.local", role="Technician")
        tech2.set_password("tech123")
        staff = User(name="Staff User", email="staff@maintenance.local", role="Staff")
        staff.set_password("staff123")
        db.session.add_all([admin, supervisor, tech1, tech2, staff])
        db.session.commit()

        t1 = Ticket(title="Faulty air conditioner in Block C",
                    description="The AC in room 204 is not cooling.",
                    category="HVAC", priority="High", status="In Progress",
                    reporter_id=staff.user_id, technician_id=tech1.user_id)
        t2 = Ticket(title="Broken pipe in toilet corridor",
                    description="Water leaking near the ground-floor toilet.",
                    category="Plumbing", priority="Critical", status="Open",
                    reporter_id=staff.user_id)
        t3 = Ticket(title="Replace corridor lights, Block A",
                    description="Three tube lights are not working.",
                    category="Electrical", priority="Medium", status="Open",
                    reporter_id=staff.user_id)
        t4 = Ticket(title="Network switch down in ICT lab",
                    description="No internet in the ICT lab since morning.",
                    category="IT Equipment", priority="High", status="Resolved",
                    reporter_id=staff.user_id, technician_id=tech2.user_id,
                    resolved_at=datetime.utcnow())
        t5 = Ticket(title="Repaint Block B facade",
                    description="Walls need repainting.",
                    category="General", priority="Low", status="Closed",
                    reporter_id=staff.user_id, technician_id=tech1.user_id,
                    resolved_at=datetime.utcnow() - timedelta(days=2))
        t6 = Ticket(title="Generator servicing request",
                    description="Quarterly servicing due.",
                    category="Electrical", priority="Medium", status="Open",
                    reporter_id=staff.user_id)
        db.session.add_all([t1, t2, t3, t4, t5, t6])
        db.session.commit()

        p1 = Project(name="Repainting of Block B",
                     description="Repaint the whole of Block B building.",
                     start_date=date.today(), end_date=date.today() + timedelta(days=30),
                     created_by=supervisor.user_id)
        p2 = Project(name="Quarterly Generator Servicing",
                     description="Service all generators on campus.",
                     start_date=date.today(), end_date=date.today() + timedelta(days=14),
                     created_by=supervisor.user_id)
        db.session.add_all([p1, p2])
        db.session.commit()

        tasks = [
            Task(project_id=p1.project_id, title="Scrape and prime walls",
                 assignee_id=tech1.user_id, deadline=date.today() + timedelta(days=7),
                 status="In Progress", progress=60),
            Task(project_id=p1.project_id, title="First coat of paint",
                 assignee_id=tech1.user_id, deadline=date.today() + timedelta(days=14),
                 status="Pending", progress=0),
            Task(project_id=p1.project_id, title="Second coat and finishing",
                 assignee_id=tech2.user_id, deadline=date.today() + timedelta(days=21),
                 status="Pending", progress=0),
            Task(project_id=p2.project_id, title="Drain old oil and replace filters",
                 assignee_id=tech2.user_id, deadline=date.today() + timedelta(days=5),
                 status="Completed", progress=100),
            Task(project_id=p2.project_id, title="Test run and log readings",
                 assignee_id=tech1.user_id, deadline=date.today() + timedelta(days=7),
                 status="In Progress", progress=40),
        ]
        db.session.add_all(tasks)
        db.session.commit()

        r1 = FieldReport(technician_id=tech2.user_id, ticket_id=t4.ticket_id,
                         location="ICT Lab, Block A", equipment="Network switch",
                         findings="Switch port 4 was faulty; uplink cable damaged.",
                         action_taken="Replaced the uplink cable and tested all ports. Internet restored.",
                         report_date=date.today() - timedelta(days=1))
        r2 = FieldReport(technician_id=tech1.user_id, ticket_id=t1.ticket_id,
                         location="Block C, Room 204", equipment="Air conditioner",
                         findings="Compressor not starting; relay faulty.",
                         action_taken="Replaced the relay; AC now cooling normally.",
                         report_date=date.today())
        db.session.add_all([r1, r2])
        db.session.commit()
        print("Seeded: 5 users, 6 tickets, 2 projects, 5 tasks, 2 field reports.")


if __name__ == "__main__":
    seed()
