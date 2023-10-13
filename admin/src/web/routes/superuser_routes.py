from flask import Blueprint, request
from src.core.controllers import users_config_controller
from src.core.controllers import institutions_config_controller
from src.core.controllers import site_config_controller as config
from src.core.common.decorators import PermissionWrap
from src.core.common.decorators import LoginWrap


super_bp = Blueprint('super', __name__, url_prefix='/admin')


@super_bp.route("/site-config", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["config_show"])
def view_config():
    return config.view_config()


@super_bp.route('/edit-config', methods=['GET', 'POST'])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["config_update"])
def edit_config():
    return config.edit_config(request)


@super_bp.route("/users", methods=["GET"])
def users():
    return users_config_controller.users()


@super_bp.route("/institutions", methods=["GET"])
def institutions():
    return institutions_config_controller.institutions()
