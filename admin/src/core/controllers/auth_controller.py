"""Authentication controllers."""
from flask import flash, redirect, url_for, render_template
from flask import session
from src.core.common.decorators import LoginWrap
from src.web.helpers.auth import check_user, log_user
from src.core.oauth import oauth
from src.core.models.user import User, AuthEnum


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

    user = User.find_user_by(field='email', value=params["inputEmail"])

    if user and user.auth_method == AuthEnum.APP and check_user(
            user.email, params["inputPassword"]
    ):
        return log_user(user)

    flash("Contraseña inválida. Intente nuevamente", "danger")
    return redirect(url_for("auth.login"))


def logout():
    """
    Logout the user from the session.

    This function clears the session and displays a flash message indicating
    the successful logout. If there is no session started, it displays a
    flash message indicating that there is no session to logout from.
    the successful logout. If there is no session started, it displays a
    flash message indicating that there is no session to logout from.

    Returns:
        redirect: A redirect response to the login page.

    """
    if LoginWrap.evaluate_condition():
        session.clear()
        flash("Sesión cerrada correctamente", "info")
    else:
        flash("No hay sesión iniciada", "info")

    return redirect(url_for("home.home"))


def google_login():
    """
    Login function that renders the google authorization endpoint.
    """
    redirect_uri = url_for('auth.google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


def google_auth():
    """
    Authenticate by google

    Checks that the user authenticated by google had been
    registered using Google.

    Returns:
        redirect: A redirection to the login page if the authentication fails,
            or a redirection to the home page if the authentication succeeds.
    """

    token = oauth.google.authorize_access_token()

    email = token['userinfo'].get("email")
    user = User.find_user_by(field='email', value=email)

    if user and user.auth_method == AuthEnum.GOOGLE:
        return log_user(user)

    flash("Contraseña inválida. Intente nuevamente", "danger")
    return redirect(url_for("auth.login"))
