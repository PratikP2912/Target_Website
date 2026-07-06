from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models import db
from models.user import User

auth_bp = Blueprint("auth", __name__)


# ---------------- REGISTER ---------------- #

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        city = request.form.get("city")
        country = request.form.get("country")
        postal_code = request.form.get("postal_code")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:

            flash("Passwords do not match.", "danger")

            return redirect(url_for("auth.register"))

        existing = User.query.filter(
            (User.username == username) |
            (User.email == email)
        ).first()

        if existing:

            flash("Username or Email already exists.", "warning")

            return redirect(url_for("auth.register"))

        user = User(

            full_name=full_name,

            username=username,

            email=email,

            phone=phone,

            address=address,

            city=city,

            country=country,

            postal_code=postal_code,

            password=generate_password_hash(password)

        )

        db.session.add(user)

        db.session.commit()

        flash("Registration Successful!", "success")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


# ---------------- LOGIN ---------------- #

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
                user.password,
                password):

            login_user(user)

            flash("Welcome back!", "success")

            return redirect(
                url_for("profile.profile")
            )

        flash("Invalid email or password.", "danger")

    return render_template(
        "auth/login.html"
    )


# ---------------- LOGOUT ---------------- #

@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out successfully.", "info")

    return redirect(
        url_for("home.home")
    )