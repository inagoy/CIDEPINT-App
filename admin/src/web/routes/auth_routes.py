"""Routes for the login pages."""
from flask import Blueprint, request
from src.core.controllers import auth_controller


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/", methods=["GET"])
def login():
    """Route for login."""
    return auth_controller.login()


@auth_bp.route("/authenticate", methods=["POST"])
def authenticate():
    """Route for authentication."""
    return auth_controller.authenticate(request)


@auth_bp.route("/logout", methods=["GET"])
def logout():
    """Route for logout."""
    return auth_controller.logout()


@auth_bp.route("/google-login", methods=["GET"])
def google_login():
    """Route for google authentication."""
    return auth_controller.google_login()


@auth_bp.route("/signin-google")
def google_auth():
    """Route for google authentication."""
    return auth_controller.google_auth()
