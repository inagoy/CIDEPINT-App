from src.core.bcrypt import bcrypt
from flask import session, redirect, url_for, flash
from src.web.helpers.session import superuser_session
from src.core.models.site_config import SiteConfig
from src.web.helpers.users import get_institutions_user
from src.core.models.user import AuthEnum, User


def check_user(email, password):
    """
    Check if a user exists with the given email and password.
     :param email: The email of the user.
     :type email: str
     :param password: The password of the user.
     :type password: str
     :return: The user object if the email and password match, None otherwise.
     :rtype: User or None
     """

    user = User.find_user_by(field='email', value=email)

    if user and bcrypt.check_password_hash(user.password,
                                           password.encode("utf-8")):
        return user
    else:
        return None


def check_google_user(email):
    user = User.find_user_by(field='email', value=email)
    if user and user.active and user.auth_method == AuthEnum.GOOGLE:
        return user
    else:
        return None


def log_user(user: object):

    if (user.active is False):
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
