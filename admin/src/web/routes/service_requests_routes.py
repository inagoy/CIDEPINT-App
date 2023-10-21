"""Routes for the service request page."""
from src.core.common.decorators import LoginWrap, MaintenanceWrap
from src.core.common.decorators import PermissionWrap
from flask import Blueprint
from src.core.controllers import service_request_controller

service_requests_bp = Blueprint('service_requests', __name__,
                                url_prefix="/service-requests")


@service_requests_bp.route("/", methods=["GET"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["request_index"])
@LoginWrap.wrap
def service_requests():
    """Route for the service request page."""
    return service_request_controller.service_requests()


@service_requests_bp.route("/edit/<int:service_request_id>", methods=["POST"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["request_update"])
@LoginWrap.wrap
def edit_service_request(service_request_id):
    """Route for the service request edit page."""
    return service_request_controller.edit_service_request(
        service_request_id
    )


@service_requests_bp.route("/delete", methods=["POST"])
@MaintenanceWrap.wrap
@PermissionWrap.wrap_args(permissions=["request_destroy"])
@LoginWrap.wrap
def delete_service_request():
    """Route for the service request delete page."""
    return service_request_controller.delete_service_request()


@service_requests_bp.route("/service-request/<int:service_request_id>/notes",
                           methods=["GET"]
                           )
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["request_update"])
def notes(service_request_id):
    """Route for the service request notes page."""
    return service_request_controller.notes(service_request_id)


@service_requests_bp.route(
        "/service-request/<int:service_request_id>/new_note",
        methods=["POST"]
    )
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["request_update"])
def new_note(service_request_id):
    """Route for the service request new note page."""
    return service_request_controller.new_note(service_request_id)
