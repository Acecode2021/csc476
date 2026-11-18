from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from sqlalchemy import func

from extensions import db
from auth import PRIORITIES, TICKET_STATUSES
from models import FieldReport, Project, Task, Ticket

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
@dashboard_bp.route("/dashboard")
@login_required
def index():
    stats = {
        "open_tickets": Ticket.query.filter_by(status="Open").count(),
        "in_progress": Ticket.query.filter_by(status="In Progress").count(),
        "resolved": Ticket.query.filter_by(status="Resolved").count(),
        "closed": Ticket.query.filter_by(status="Closed").count(),
        "active_projects": Project.query.filter_by(status="Active").count(),
        "tasks_pending": Task.query.filter_by(status="Pending").count(),
        "tasks_in_progress": Task.query.filter_by(status="In Progress").count(),
        "tasks_completed": Task.query.filter_by(status="Completed").count(),
        "field_reports": FieldReport.query.count(),
    }
    by_status = db.session.query(Ticket.status, func.count(Ticket.ticket_id)) \
        .group_by(Ticket.status).all()
    max_count = max([c for _, c in by_status], default=1) or 1
    bars = [(status, count, int(100 * count / max_count)) for status, count in by_status]
    recent_tickets = Ticket.query.order_by(Ticket.created_at.desc()).limit(5).all()
    recent_reports = FieldReport.query.order_by(FieldReport.created_at.desc()).limit(5).all()
    return render_template("dashboard.html", stats=stats, bars=bars,
                           recent_tickets=recent_tickets, recent_reports=recent_reports)


@dashboard_bp.route("/summary")
@login_required
def summary():
    status = request.args.get("status", "")
    priority = request.args.get("priority", "")
    date_from = request.args.get("date_from", "")
    date_to = request.args.get("date_to", "")
    q = Ticket.query
    if status:
        q = q.filter_by(status=status)
    if priority:
        q = q.filter_by(priority=priority)
    if date_from:
        q = q.filter(Ticket.created_at >= date_from)
    if date_to:
        q = q.filter(Ticket.created_at <= date_to + " 23:59:59")
    tickets = q.order_by(Ticket.created_at.desc()).all()
    projects = Project.query.order_by(Project.project_id.desc()).all()
    reports = FieldReport.query.order_by(FieldReport.created_at.desc()).all()
    return render_template("summary.html", tickets=tickets, projects=projects,
                           reports=reports, status=status, priority=priority,
                           date_from=date_from, date_to=date_to,
                           statuses=TICKET_STATUSES, priorities=PRIORITIES)
