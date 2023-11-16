from flask import url_for, request
from flask import current_app as app


def url_to_public_login():
    URL = app.config["PUBLIC_LOGIN_URL"]
    return URL


def url_to_private_login():
    return url_for("auth.login")


def url_to_login(private: str = None):
    if not private:
        return url_to_private_login()
    else:
        return url_to_public_login()


def url_to_public_home():
    URL = app.config["PUBLIC_HOME_URL"]
    return URL


def url_to_private_home():
    return url_for("home.home")


def url_to_home(private: str = None):
    if not private:
        return url_to_private_home()
    else:
        return url_to_public_home()


def get_admin_app_param():
    return 'false' if request.args.get('admin_app') else None
