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
