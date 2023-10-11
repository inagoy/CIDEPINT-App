from src.core.controllers import institution_controller
from flask import Blueprint, request
from src.core.common.decorators import LoginWrap

institution_bp = Blueprint('institution', __name__, url_prefix="/institution")


@institution_bp.route("/<int:institution_id>", methods=["GET"])
@LoginWrap.wrap
def institution(institution_id):
    return institution_controller.institution(request, institution_id)
