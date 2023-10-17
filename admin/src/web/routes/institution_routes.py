from src.core.controllers import institution_controller
from flask import Blueprint, request
from src.core.common.decorators import LoginWrap, MaintenanceWrap
from src.core.common.decorators import PermissionWrap

institution_bp = Blueprint('institution', __name__, url_prefix="/institution")


@institution_bp.route("/<int:institution_id>", methods=["GET"])
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["request_index"])
def institution(institution_id):
    return institution_controller.institution(request, institution_id)


@institution_bp.route("/roles", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_institution_index"])
def institution_roles():
    return institution_controller.institution_roles()


@institution_bp.route("/roles/update-role", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(
    permissions=[
        "user_institution_create",
        "user_institution_update",
        "user_institution_destroy"])
def update_role():
    return institution_controller.update_role()


@institution_bp.route("/roles/user-search", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_institution_index"])
def user_search():
    return institution_controller.user_search()
