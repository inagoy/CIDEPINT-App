"""Routes for the institution pages."""
from flask import Blueprint
from src.core.controllers import institution_controller
from src.core.common.decorators import LoginWrap, MaintenanceWrap
from src.core.common.decorators import PermissionWrap

institution_bp = Blueprint('institution', __name__, url_prefix="/institution")


@institution_bp.route("/<int:institution_id>", methods=["GET"])
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["request_index"])
def institution(institution_id):
    """Route for a specific institution."""
    return institution_controller.institution(institution_id)


@institution_bp.route("/edit", methods=["GET", "POST"])
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_update"])
def edit_institution():
    """Route for the institution edit page."""
    return institution_controller.edit_institution()


@institution_bp.route("/roles", methods=["GET"])
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_institution_index"])
def institution_roles():
    """Route for the institution roles managment."""
    return institution_controller.institution_roles()


@institution_bp.route("/roles/update-role", methods=["POST"])
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(
    permissions=[
        "user_institution_create",
        "user_institution_update",
        "user_institution_destroy"])
def update_role():
    """Route for the institution roles update."""
    return institution_controller.update_role()


@institution_bp.route("/roles/user-search", methods=["POST"])
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_institution_index"])
def user_search():
    """Route for the institution roles search."""
    return institution_controller.user_search()
