from flask import Blueprint, request
from src.core.controllers import register_controller

register_bp = Blueprint("register", __name__, url_prefix="/register")


@register_bp.route("/", methods=["GET"])
def first_registration():
    return register_controller.first_registration()


@register_bp.route("/first_form", methods=["POST"])
def first_form():
    return register_controller.first_form(request)


@register_bp.route('/confirmation/<string:hashed_email>', methods=['GET'])
def confirmation(hashed_email):
    return register_controller.confirmation(hashed_email)
