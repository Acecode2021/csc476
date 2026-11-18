from functools import wraps

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from extensions import db, login_manager
from models import User

auth_bp = Blueprint("auth", __name__)

CATEGORIES = ["General", "Electrical", "Plumbing", "HVAC", "Carpentry", "IT Equipment", "Other"]
PRIORITIES = ["Low", "Medium", "High", "Critical"]
ROLES = ["Administrator", "Supervisor", "Technician", "Staff"]
TICKET_STATUSES = ["Open", "In Progress", "Resolved", "Closed"]


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for("auth.login"))
            if current_user.role not in roles:
                flash("You do not have permission to access that page.", "error")
                return redirect(url_for("dashboard.index"))
            return f(*args, **kwargs)
        return wrapper
    return decorator


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            flash("Invalid email or password.", "error")
            return redirect(url_for("auth.login"))
        login_user(user)
        flash("Welcome back, %s." % user.name, "success")
        return redirect(url_for("dashboard.index"))
    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))


@auth_bp.route("/users")
@login_required
@role_required("Administrator")
def list_users():
    users = User.query.order_by(User.created_at).all()
    return render_template("users.html", users=users)


@auth_bp.route("/users/new", methods=["GET", "POST"])
@login_required
@role_required("Administrator")
def new_user():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        role = request.form.get("role", "Staff")
        password = request.form.get("password", "")
        if not name or not email or not password:
            flash("Name, email and password are required.", "error")
            return redirect(url_for("auth.new_user"))
        if User.query.filter_by(email=email).first():
            flash("A user with that email already exists.", "error")
            return redirect(url_for("auth.new_user"))
        user = User(name=name, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("User created.", "success")
        return redirect(url_for("auth.list_users"))
    return render_template("new_user.html", roles=ROLES)
