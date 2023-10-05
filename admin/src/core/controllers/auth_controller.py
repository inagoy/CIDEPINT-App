from src.core.models.user import User
from flask import flash, redirect, url_for, render_template
from flask import session
# from src.core.bcrypt import bcrypt
from src.core.common.decorators import LoginWrap


def check_user(email, password):

    user = User.find_user_by_email(email)

    # if user and bcrypt.check_password_hash(user.password,
    #                                       password.encode("utf-8")):
    if user and user.password == password:
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
    current_institution = User.get_user_institutions(user_id=user.id)[0]
    if current_institution:
        session["current_institution"] = current_institution.id

    flash("Sesión iniciada correctamente", "success")
    return redirect(url_for("home.home_user"))


def logout():
    if LoginWrap.evaluate_condition():
        del session["user"]
        session.clear
        flash("Sesión cerrada correctamente", "info")
    else:
        flash("No hay sesión iniciada", "info")

    return redirect(url_for("auth.login"))
