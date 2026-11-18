from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="Staff")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        return str(self.user_id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Ticket(db.Model):
    __tablename__ = "tickets"
    ticket_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False, default="General")
    priority = db.Column(db.String(20), nullable=False, default="Medium")
    status = db.Column(db.String(20), nullable=False, default="Open")
    reporter_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    technician_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = db.Column(db.DateTime, nullable=True)

    reporter = db.relationship("User", foreign_keys=[reporter_id])
    technician = db.relationship("User", foreign_keys=[technician_id])

    def update_status(self, new_status, author):
        old = self.status
        self.status = new_status
        self.updated_at = datetime.utcnow()
        if new_status == "Closed":
            self.resolved_at = datetime.utcnow()
        db.session.add(TicketUpdate(ticket_id=self.ticket_id,
                                    author_id=author.user_id,
                                    note="Status changed from %s to %s" % (old, new_status),
                                    old_status=old, new_status=new_status))
        db.session.commit()


class TicketUpdate(db.Model):
    __tablename__ = "ticket_updates"
    update_id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("tickets.ticket_id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    note = db.Column(db.Text, nullable=False)
    old_status = db.Column(db.String(20), nullable=True)
    new_status = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship("User")


class Project(db.Model):
    __tablename__ = "projects"
    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Active")
    created_by = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)

    tasks = db.relationship("Task", backref="project", lazy=True)

    def add_task(self, title, assignee_id=None, deadline=None, description=""):
        task = Task(project_id=self.project_id, title=title, description=description,
                    assignee_id=assignee_id, deadline=deadline)
        db.session.add(task)
        db.session.commit()
        return task

    def progress(self):
        if not self.tasks:
            return 0
        return int(round(sum(t.progress for t in self.tasks) / len(self.tasks)))


class Task(db.Model):
    __tablename__ = "tasks"
    task_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    assignee_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    deadline = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Pending")
    progress = db.Column(db.Integer, nullable=False, default=0)

    assignee = db.relationship("User")

    def update_progress(self, value):
        value = max(0, min(100, int(value)))
        self.progress = value
        self.status = "Completed" if value >= 100 else ("In Progress" if value > 0 else "Pending")
        db.session.commit()


class FieldReport(db.Model):
    __tablename__ = "field_reports"
    report_id = db.Column(db.Integer, primary_key=True)
    technician_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey("tickets.ticket_id"), nullable=True)
    location = db.Column(db.String(200), nullable=False)
    equipment = db.Column(db.String(200), nullable=True)
    findings = db.Column(db.Text, nullable=False)
    action_taken = db.Column(db.Text, nullable=False)
    report_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default="Submitted")

    technician = db.relationship("User")
    ticket = db.relationship("Ticket")

    def submit(self):
        self.status = "Submitted"
        db.session.commit()
