from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from extensions import db
from auth import role_required
from models import FieldReport, Ticket

reports_bp = Blueprint("reports", __name__)


@reports_bp.route("/field-reports")
@login_required
def list_reports():
    q = FieldReport.query
    if current_user.role == "Technician":
        q = q.filter_by(technician_id=current_user.user_id)
    reports = q.order_by(FieldReport.created_at.desc()).all()
    return render_template("field_reports.html", reports=reports)


@reports_bp.route("/field-reports/new", methods=["GET", "POST"])
@login_required
@role_required("Technician", "Supervisor", "Administrator")
def new_report():
    if request.method == "POST":
        location = request.form.get("location", "").strip()
        findings = request.form.get("findings", "").strip()
        action_taken = request.form.get("action_taken", "").strip()
        if not location or not findings or not action_taken:
            flash("Location, findings and action taken are required.", "error")
            return redirect(url_for("reports.new_report"))
        ticket_id = request.form.get("ticket_id") or None
        report = FieldReport(technician_id=current_user.user_id,
                             ticket_id=int(ticket_id) if ticket_id else None,
                             location=location,
                             equipment=request.form.get("equipment", ""),
                             findings=findings,
                             action_taken=action_taken)
        rd = request.form.get("report_date")
        if rd:
            report.report_date = datetime.strptime(rd, "%Y-%m-%d").date()
        db.session.add(report)
        db.session.commit()
        report.submit()
        flash("Field report submitted.", "success")
        return redirect(url_for("reports.list_reports"))
    tickets = Ticket.query.filter(Ticket.status != "Closed").all()
    return render_template("new_field_report.html", tickets=tickets)
