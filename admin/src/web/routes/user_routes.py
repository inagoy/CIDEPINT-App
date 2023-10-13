from flask import Blueprint
from src.core.common.decorators import PermissionWrap
from src.core.common.decorators import LoginWrap, MaintenanceWrap


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/<int:user_id>', methods=['GET'])
@MaintenanceWrap.wrap
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_show"])
def view_user(user_id):
    return "Mirando perfil..."
