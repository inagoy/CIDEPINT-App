"""Routes for the registration pages."""
from flask import Blueprint, request
from src.core.controllers import register_controller
from src.core.common.decorators import MaintenanceWrap


register_bp = Blueprint("register", __name__, url_prefix="/register")


@register_bp.route("/", methods=["GET"])
@MaintenanceWrap.wrap
def first_registration():
    """Route for the first registration."""
    return register_controller.first_registration()


@register_bp.route("/first_form", methods=["POST"])
@MaintenanceWrap.wrap
def first_form():
    """Route for the first registration form."""
    return register_controller.first_form(request)


@register_bp.route('/confirmation/<string:hashed_email>', methods=['GET'])
@MaintenanceWrap.wrap
def confirmation(hashed_email):
    """Route for the confirmation page."""
    return register_controller.confirmation(hashed_email)


@register_bp.route("/second_form/<string:hashed_email>", methods=["POST"])
@MaintenanceWrap.wrap
def second_form(hashed_email):
    """Route for the second registration form."""
    return register_controller.second_form(request, hashed_email)


@register_bp.route("/confirm_password/<string:hashed_email>", methods=["POST"])
@MaintenanceWrap.wrap
def confirm_password(hashed_email):
    """Route for the password confirmation."""
    return register_controller.confirm_password(request, hashed_email)


@register_bp.route("/google-register", methods=["GET"])
@MaintenanceWrap.wrap
def google_register():
    """Route for google register."""
    return register_controller.google_register()


@register_bp.route("/signup-google", methods=["GET"])
@MaintenanceWrap.wrap
def google_callback():
    """Route for google register callback."""
    return register_controller.google_callback()


@register_bp.route("/second_form/google/<string:hashed_email>",
                   methods=["POST"])
@MaintenanceWrap.wrap
def google_second_form(hashed_email):
    """Route for google register form."""
    return register_controller.google_second_form(hashed_email)
