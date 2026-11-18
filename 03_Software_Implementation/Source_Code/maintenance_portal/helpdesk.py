from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from extensions import db
from auth import CATEGORIES, PRIORITIES, TICKET_STATUSES, role_required
from models import Ticket, TicketUpdate, User

helpdesk_bp = Blueprint("helpdesk", __name__)


@helpdesk_bp.route("/tickets")
@login_required
def list_tickets():
    q = Ticket.query
    if current_user.role == "Staff":
        q = q.filter_by(reporter_id=current_user.user_id)
    elif current_user.role == "Technician":
        q = q.filter_by(technician_id=current_user.user_id)
    tickets = q.order_by(Ticket.created_at.desc()).all()
    return render_template("tickets.html", tickets=tickets)


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
    return render_template("new_ticket.html", categories=CATEGORIES, priorities=PRIORITIES)


@helpdesk_bp.route("/tickets/<int:ticket_id>", methods=["GET", "POST"])
@login_required
def ticket_detail(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if current_user.role == "Staff" and ticket.reporter_id != current_user.user_id:
        flash("You can only view your own tickets.", "error")
        return redirect(url_for("helpdesk.list_tickets"))
    if request.method == "POST":
        action = request.form.get("action")
        if action == "assign" and current_user.role in ("Supervisor", "Administrator"):
            tech_id = request.form.get("technician_id")
            technician = User.query.get(tech_id) if tech_id else None
            if technician and technician.role == "Technician":
                ticket.technician_id = technician.user_id
                db.session.add(TicketUpdate(ticket_id=ticket.ticket_id,
                                            author_id=current_user.user_id,
                                            note="Ticket assigned to %s" % technician.name))
                if ticket.status == "Open":
                    ticket.status = "In Progress"
                db.session.commit()
                flash("Ticket assigned.", "success")
            else:
                flash("Please select a valid technician.", "error")
        elif action == "comment" and current_user.role in ("Technician", "Supervisor", "Administrator"):
            note = request.form.get("note", "").strip()
            if note:
                db.session.add(TicketUpdate(ticket_id=ticket.ticket_id,
                                            author_id=current_user.user_id, note=note))
                db.session.commit()
                flash("Comment added.", "success")
        elif action == "status" and current_user.role in ("Technician", "Supervisor", "Administrator"):
            new_status = request.form.get("status")
            if new_status in TICKET_STATUSES:
                ticket.update_status(new_status, current_user)
                flash("Status updated to %s." % new_status, "success")
        return redirect(url_for("helpdesk.ticket_detail", ticket_id=ticket.ticket_id))
    updates = TicketUpdate.query.filter_by(ticket_id=ticket.ticket_id) \
        .order_by(TicketUpdate.created_at).all()
    technicians = User.query.filter_by(role="Technician").all()
    return render_template("ticket_detail.html", ticket=ticket, updates=updates,
                           technicians=technicians, statuses=TICKET_STATUSES,
                           priorities=PRIORITIES, categories=CATEGORIES)
