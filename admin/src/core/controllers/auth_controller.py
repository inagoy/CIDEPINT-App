from src.core.models.user import User
from flask import flash, redirect, url_for, render_template
from flask import session
from src.core.bcrypt import bcrypt
from src.web.helpers.auth import is_authenticated


def check_user(email, password):

    user = User.find_user_by_email(email)
    print(user.password, password.encode("utf-8"))
    if user and bcrypt.check_password_hash(user.password,
                                           password.encode("utf-8")):
        return user
    else:
        return None


def login():
    return render_template("auth/login.html")


def authenticate(request):
    params = request.form

    user = check_user(params["inputEmail"], params["inputPassword"])

    if not user:
        flash("Mail o contraseña inválidos. Intente nuevamente", "danger")
        return redirect(url_for("auth.login"))

    session["user"] = user.email
    flash("Sesión iniciada correctamente", "success")
    return redirect(url_for("home.home"))


def logout():
    if is_authenticated(session):
        del session["user"]
        session.clear
        flash("Sesión cerrada correctamente", "info")
    else:
        flash("No hay sesión iniciada", "info")

    return redirect(url_for("auth.login"))
