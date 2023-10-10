from flask import Blueprint, request
from src.core.controllers import auth_controller

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/", methods=["GET"])
def login():
    return auth_controller.login()


@auth_bp.route("/authenticate", methods=["POST"])
def authenticate():
    return auth_controller.authenticate(request)


@auth_bp.route("/logout", methods=["GET"])
def logout():
    return auth_controller.logout()
