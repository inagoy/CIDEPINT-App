from flask import Blueprint, request
from src.core.controllers import users_config_controller
from src.core.controllers import institutions_config_controller
from src.core.controllers import site_config_controller as config
from src.core.common.decorators import PermissionWrap
from src.core.common.decorators import LoginWrap


super_bp = Blueprint('super', __name__, url_prefix='/admin')


# SITE CONFIG
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


# USERS
@super_bp.route("/users", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_index"])
def users():
    return users_config_controller.users()


@super_bp.route("/users/active", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_index"])
def active():
    return users_config_controller.active()


@super_bp.route("/users/inactive", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_index"])
def inactive():
    return users_config_controller.inactive()


@super_bp.route("/users/search", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_index"])
def search():
    return users_config_controller.search()


@super_bp.route("/users/delete-user", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_destroy"])
def delete_user():
    return users_config_controller.delete_user()


@super_bp.route("/users/add-user", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_create"])
def add_user():
    return users_config_controller.add_user()


@super_bp.route('/confirmation/<string:hashed_email>', methods=['GET'])
def confirmation(hashed_email):
    return users_config_controller.confirmation(hashed_email)


@super_bp.route("/users/edit-user/<int:user_id>", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_update"])
def edit_user(user_id):
    return users_config_controller.edit_user(user_id)


@super_bp.route("/users/user-roles/<int:user_id>", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_update"])
def roles(user_id):
    return users_config_controller.roles(user_id)


@super_bp.route("/users/user-roles/<int:user_id>/add-role", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_update"])
def add_role(user_id):
    return users_config_controller.add_role(user_id)


@super_bp.route("/users/user-roles/<int:user_id>/delete-role",
                methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_update"])
def delete_role(user_id):
    return users_config_controller.delete_role(user_id)


# INSTITUTIONS
@super_bp.route("/institutions", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_index",
                                       "institution_show"])
def institutions():
    return institutions_config_controller.institutions()


@super_bp.route("/institutions/add-institution", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_create",
                                       "institution_activate",
                                       "institution_deactivate"])
def add_institution():
    return institutions_config_controller.add_institution()


@super_bp.route("/institutions/edit-institution/<int:institution_id>",
                methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_update",
                                       "institution_activate",
                                       "institution_deactivate"])
def edit_institution(institution_id):
    return institutions_config_controller.edit_institution(institution_id)


@super_bp.route("/institutions/delete-institution",
                methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_destroy"])
def delete_institution():
    return institutions_config_controller.delete_institution()
