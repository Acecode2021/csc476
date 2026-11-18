import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app
from extensions import db
from models import FieldReport, Project, Task, Ticket, TicketUpdate, User


class TestConfig:
    SECRET_KEY = "test-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        admin = User(name="Admin", email="admin@test.local", role="Administrator")
        admin.set_password("adminpass")
        sup = User(name="Sup", email="sup@test.local", role="Supervisor")
        sup.set_password("suppass")
        tech = User(name="Tech", email="tech@test.local", role="Technician")
        tech.set_password("techpass")
        staff = User(name="Staff", email="staff@test.local", role="Staff")
        staff.set_password("staffpass")
        db.session.add_all([admin, sup, tech, staff])
        db.session.commit()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def login(client, email, password):
    client.get("/logout")  # ensure any previous session is ended first
    return client.post("/login", data={"email": email, "password": password},
                       follow_redirects=True)


# TC-01: login with valid credentials
def test_login_valid(client):
    resp = login(client, "staff@test.local", "staffpass")
    assert resp.status_code == 200
    assert b"Dashboard" in resp.data


# TC-02: login with wrong password
def test_login_invalid(client):
    resp = client.post("/login", data={"email": "staff@test.local", "password": "wrong"},
                       follow_redirects=True)
    assert b"Invalid email or password" in resp.data


# TC-03: Staff cannot access the admin users page
def test_role_access_denied(client):
    login(client, "staff@test.local", "staffpass")
    resp = client.get("/users")
    assert resp.status_code == 302  # redirected away
    assert "/dashboard" in resp.headers["Location"]


def test_unauthenticated_redirect(client):
    resp = client.get("/dashboard")
    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]


def test_password_stored_hashed(app):
    with app.app_context():
        user = User.query.filter_by(email="staff@test.local").first()
        assert user.password_hash != "staffpass"
        assert user.check_password("staffpass")


# TC-04: Staff submits a ticket
def test_create_ticket(client, app):
    login(client, "staff@test.local", "staffpass")
    resp = client.post("/tickets/new", data={
        "title": "Broken chair",
        "category": "General",
        "priority": "Low",
        "description": "Chair in room 12 is broken",
    }, follow_redirects=True)
    assert resp.status_code == 200
    with app.app_context():
        ticket = Ticket.query.filter_by(title="Broken chair").first()
        assert ticket is not None
        assert ticket.status == "Open"
        assert ticket.reporter.email == "staff@test.local"


# TC-05: ticket without a title is rejected
def test_ticket_validation(client, app):
    login(client, "staff@test.local", "staffpass")
    client.post("/tickets/new", data={"title": "", "description": "no title"},
                follow_redirects=True)
    with app.app_context():
        assert Ticket.query.count() == 0


# TC-06: Supervisor assigns a ticket
def test_assign_ticket(client, app):
    login(client, "staff@test.local", "staffpass")
    client.post("/tickets/new", data={"title": "Leak", "description": "Roof leak"},
                follow_redirects=True)
    login(client, "sup@test.local", "suppass")
    with app.app_context():
        ticket = Ticket.query.first()
        tech = User.query.filter_by(role="Technician").first()
        tid, tech_id = ticket.ticket_id, tech.user_id
    client.post("/tickets/%d" % tid, data={"action": "assign", "technician_id": tech_id},
                follow_redirects=True)
    with app.app_context():
        ticket = Ticket.query.get(tid)
        assert ticket.technician_id == tech_id
        assert ticket.status == "In Progress"
        assert TicketUpdate.query.filter_by(ticket_id=tid).count() == 1


# TC-07: Technician adds a comment
def test_add_comment(client, app):
    login(client, "staff@test.local", "staffpass")
    client.post("/tickets/new", data={"title": "Leak", "description": "Roof leak"},
                follow_redirects=True)
    login(client, "tech@test.local", "techpass")
    with app.app_context():
        tid = Ticket.query.first().ticket_id
    client.post("/tickets/%d" % tid, data={"action": "comment", "note": "On my way"},
                follow_redirects=True)
    with app.app_context():
        update = TicketUpdate.query.filter_by(ticket_id=tid).first()
        assert update is not None
        assert update.note == "On my way"
        assert update.author.email == "tech@test.local"


# TC-08: Technician closes a ticket
def test_close_ticket(client, app):
    login(client, "staff@test.local", "staffpass")
    client.post("/tickets/new", data={"title": "Leak", "description": "Roof leak"},
                follow_redirects=True)
    login(client, "tech@test.local", "techpass")
    with app.app_context():
        tid = Ticket.query.first().ticket_id
    client.post("/tickets/%d" % tid, data={"action": "status", "status": "Closed"},
                follow_redirects=True)
    with app.app_context():
        ticket = Ticket.query.get(tid)
        assert ticket.status == "Closed"
        assert ticket.resolved_at is not None


# TC-09: Staff sees only their own tickets
def test_staff_views_own_tickets(client, app):
    with app.app_context():
        other = User(name="Other", email="other@test.local", role="Staff")
        other.set_password("otherpass")
        db.session.add(other)
        db.session.commit()
        db.session.add(Ticket(title="Not yours", description="x",
                              reporter_id=other.user_id))
        db.session.commit()
    login(client, "staff@test.local", "staffpass")
    resp = client.get("/tickets")
    assert b"Not yours" not in resp.data


# TC-10: Supervisor creates a project and tasks
def test_create_project_and_tasks(client, app):
    login(client, "sup@test.local", "suppass")
    client.post("/projects/new", data={"name": "Repaint Block B",
                                       "description": "Repaint walls"},
                follow_redirects=True)
    with app.app_context():
        project = Project.query.filter_by(name="Repaint Block B").first()
        assert project is not None
        pid = project.project_id
        tech = User.query.filter_by(role="Technician").first()
        tech_id = tech.user_id
    client.post("/projects/%d" % pid, data={
        "action": "add_task", "title": "Prime walls", "assignee_id": tech_id,
    }, follow_redirects=True)
    with app.app_context():
        project = Project.query.get(pid)
        assert len(project.tasks) == 1
        assert project.tasks[0].title == "Prime walls"


# TC-11: Technician updates task progress
def test_update_task_progress(client, app):
    login(client, "sup@test.local", "suppass")
    client.post("/projects/new", data={"name": "Gen servicing"}, follow_redirects=True)
    with app.app_context():
        project = Project.query.first()
        tech = User.query.filter_by(role="Technician").first()
        task = project.add_task("Test run", assignee_id=tech.user_id)
        pid, task_id = project.project_id, task.task_id
    login(client, "tech@test.local", "techpass")
    client.post("/tasks/%d/progress" % task_id, data={"progress": "75"},
                follow_redirects=True)
    with app.app_context():
        task = Task.query.get(task_id)
        assert task.progress == 75
        assert task.status == "In Progress"
        assert Project.query.get(pid).progress() == 75


# TC-12: Technician files a field report
def test_field_report(client, app):
    login(client, "tech@test.local", "techpass")
    resp = client.post("/field-reports/new", data={
        "location": "Block A", "equipment": "Generator",
        "findings": "Oil dirty", "action_taken": "Oil changed",
    }, follow_redirects=True)
    assert resp.status_code == 200
    with app.app_context():
        report = FieldReport.query.first()
        assert report is not None
        assert report.location == "Block A"
        assert report.status == "Submitted"


# TC-13: dashboard counts match the database
def test_dashboard_counts(client, app):
    with app.app_context():
        staff = User.query.filter_by(email="staff@test.local").first()
        db.session.add(Ticket(title="T1", description="x", status="Open",
                              reporter_id=staff.user_id))
        db.session.add(Ticket(title="T2", description="x", status="Closed",
                              reporter_id=staff.user_id))
        db.session.commit()
    login(client, "sup@test.local", "suppass")
    resp = client.get("/dashboard")
    assert resp.status_code == 200
    assert b"Open tickets" in resp.data
    assert b"Closed" in resp.data


# TC-14: report page applies filters
def test_summary_filter(client, app):
    with app.app_context():
        staff = User.query.filter_by(email="staff@test.local").first()
        db.session.add(Ticket(title="OpenOne", description="x", status="Open",
                              reporter_id=staff.user_id))
        db.session.add(Ticket(title="ClosedOne", description="x", status="Closed",
                              reporter_id=staff.user_id))
        db.session.commit()
    login(client, "sup@test.local", "suppass")
    resp = client.get("/summary?status=Open")
    assert b"OpenOne" in resp.data
    assert b"ClosedOne" not in resp.data


def test_admin_creates_user(client, app):
    login(client, "admin@test.local", "adminpass")
    client.post("/users/new", data={"name": "New Tech", "email": "new@test.local",
                                    "role": "Technician", "password": "pass1234"},
                follow_redirects=True)
    with app.app_context():
        user = User.query.filter_by(email="new@test.local").first()
        assert user is not None
        assert user.role == "Technician"
        assert user.check_password("pass1234")
