from src.core.controllers import services_controller
from flask import Blueprint
from src.core.common.decorators import LoginWrap, MaintenanceWrap
# from src.core.common.decorators import PermissionWrap, PermissionWrap

services_bp = Blueprint('services', __name__, url_prefix="/services")


@services_bp.route("/", methods=["GET"])
@MaintenanceWrap.wrap
@LoginWrap.wrap
def services():
    return services_controller.services()


@services_bp.route("/delete", methods=["POST"])
@MaintenanceWrap.wrap
@LoginWrap.wrap
def delete_service():
    return services_controller.delete_service()
