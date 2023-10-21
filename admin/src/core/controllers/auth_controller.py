"""Authentication controllers."""
from src.core.models.user import User
from flask import flash, redirect, url_for, render_template
from flask import session
from src.core.bcrypt import bcrypt
from src.core.common.decorators import LoginWrap
from src.core.models.site_config import SiteConfig
from src.web.helpers.session import superuser_session
from src.web.helpers.users import get_institutions_user


def check_user(email, password):
    """
    Check if the user with the given email and password exists.

    Parameters:
    - email (str): The email of the user.
    - password (str): The password of the user.

    Returns:
    - User or None: The user object if the email and password match,
        None otherwise.
    """
    user = User.find_user_by_email(email)

    if user and bcrypt.check_password_hash(user.password,
                                           password.encode("utf-8")):
        return user
    else:
        return None


def login():
    """
    Login function that renders the login template.

    Returns:
        The rendered login template.
    """
    return render_template("modules/auth/login.html")


def authenticate(request):
    """
    Authenticate a user based on the provided request.

    Args:
        request (Request): The request object containing the user's input data.

    Returns:
        redirect: A redirection to the login page if the authentication fails,
            or a redirection to the home page if the authentication succeeds.
    """
    params = request.form

    user = check_user(params["inputEmail"], params["inputPassword"])

    if not user or user.active is False:
        flash("Mail o contraseña inválidos. Intente nuevamente", "danger")
        return redirect(url_for("auth.login"))

    else:
        session["user"] = user.email
        if SiteConfig.in_maintenance_mode():
            if superuser_session():
                flash("Sesión iniciada correctamente", "success")
                return redirect(url_for("home.home_user"))
            else:
                session.clear()
                flash("Mail o contraseña inválidos. Intente nuevamente",
                      "danger")
                return redirect(url_for("auth.login"))
        else:
            institutions = get_institutions_user()
            if not (institutions.__len__() == 0 or
                    institutions[0] is None):
                session["current_institution"] = institutions[0].id

            flash("Sesión iniciada correctamente", "success")
            return redirect(url_for("home.home_user"))


def logout():
    """
    Logout the user from the session.

    This function clears the session and displays a flash message indicating
    the successful logout. If there is no session started, it displays a flash
    message indicating that there is no session to logout from.

    Returns:
        redirect: A redirect response to the login page.

    """
    if LoginWrap.evaluate_condition():
        session.clear()
        flash("Sesión cerrada correctamente", "info")
    else:
        flash("No hay sesión iniciada", "info")

    return redirect(url_for("home.home"))
