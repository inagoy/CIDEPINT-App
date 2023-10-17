from src.core.controllers import services_controller
from flask import Blueprint
from src.core.common.decorators import LoginWrap, MaintenanceWrap
from src.core.common.decorators import PermissionWrap

services_bp = Blueprint('services', __name__, url_prefix="/services")


@services_bp.route("/", methods=["GET"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_index", "service_show"])
@LoginWrap.wrap
def services():
    return services_controller.services()


@services_bp.route("/delete", methods=["POST"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_destroy"])
@LoginWrap.wrap
def delete_service():
    return services_controller.delete_service()


@services_bp.route("/add", methods=["POST"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_create"])
@LoginWrap.wrap
def add_service():
    return services_controller.add_service()


@services_bp.route("/edit", methods=["POST"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_update"])
@LoginWrap.wrap
def edit_service():
    return services_controller.edit_service()
