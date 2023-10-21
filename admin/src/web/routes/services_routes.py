"""Routes for the services pages."""
from flask import Blueprint
from src.core.controllers import services_controller
from src.core.common.decorators import LoginWrap, MaintenanceWrap
from src.core.common.decorators import PermissionWrap


services_bp = Blueprint('services', __name__,
                        url_prefix="/institution/services")


@services_bp.route("/", methods=["GET"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_index", "service_show"])
@LoginWrap.wrap
def services():
    """Route for the services page."""
    return services_controller.services()


@services_bp.route("/delete", methods=["POST"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_destroy"])
@LoginWrap.wrap
def delete_service():
    """Route for the service delete page."""
    return services_controller.delete_service()


@services_bp.route("/add", methods=["POST"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_create"])
@LoginWrap.wrap
def add_service():
    """Route for the service add page."""
    return services_controller.add_service()


@services_bp.route("/edit/<int:service_id>", methods=["POST"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_update"])
@LoginWrap.wrap
def edit_service(service_id):
    """Route for the service edit page."""
    return services_controller.edit_service(service_id)


@services_bp.route("<int:service_id>/requests", methods=["GET"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["service_index"])
@LoginWrap.wrap
def service_requests(service_id):
    """Route for the service requests page."""
    return services_controller.service_requests(service_id)
