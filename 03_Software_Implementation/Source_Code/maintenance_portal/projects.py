from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from extensions import db
from auth import role_required
from models import Project, Task, User

projects_bp = Blueprint("projects", __name__)


@projects_bp.route("/projects")
@login_required
def list_projects():
    projects = Project.query.order_by(Project.project_id.desc()).all()
    return render_template("projects.html", projects=projects)


@projects_bp.route("/projects/new", methods=["GET", "POST"])
@login_required
@role_required("Supervisor", "Administrator")
def new_project():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            flash("Project name is required.", "error")
            return redirect(url_for("projects.new_project"))
        project = Project(name=name,
                          description=request.form.get("description", ""),
                          created_by=current_user.user_id)
        sd = request.form.get("start_date")
        ed = request.form.get("end_date")
        if sd:
            project.start_date = datetime.strptime(sd, "%Y-%m-%d").date()
        if ed:
            project.end_date = datetime.strptime(ed, "%Y-%m-%d").date()
        db.session.add(project)
        db.session.commit()
        flash("Project created.", "success")
        return redirect(url_for("projects.list_projects"))
    return render_template("new_project.html")


@projects_bp.route("/projects/<int:project_id>", methods=["GET", "POST"])
@login_required
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        action = request.form.get("action")
        if action == "add_task" and current_user.role in ("Supervisor", "Administrator"):
            title = request.form.get("title", "").strip()
            if title:
                assignee_id = request.form.get("assignee_id") or None
                deadline = request.form.get("deadline") or None
                if deadline:
                    deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
                project.add_task(title, assignee_id=assignee_id, deadline=deadline,
                                 description=request.form.get("description", ""))
                flash("Task added.", "success")
            else:
                flash("Task title is required.", "error")
        return redirect(url_for("projects.project_detail", project_id=project.project_id))
    tasks = Task.query.filter_by(project_id=project.project_id).all()
    technicians = User.query.filter_by(role="Technician").all()
    return render_template("project_detail.html", project=project, tasks=tasks,
                           technicians=technicians)


@projects_bp.route("/tasks/<int:task_id>/progress", methods=["POST"])
@login_required
def update_progress(task_id):
    task = Task.query.get_or_404(task_id)
    if current_user.role not in ("Technician", "Supervisor", "Administrator"):
        flash("You do not have permission to update tasks.", "error")
        return redirect(url_for("projects.list_projects"))
    if task.assignee_id not in (None, current_user.user_id) and current_user.role == "Technician":
        flash("You can only update your own tasks.", "error")
        return redirect(url_for("projects.project_detail", project_id=task.project_id))
    value = request.form.get("progress", "0")
    try:
        task.update_progress(int(value))
        flash("Progress updated.", "success")
    except ValueError:
        flash("Progress must be a number.", "error")
    return redirect(url_for("projects.project_detail", project_id=task.project_id))
