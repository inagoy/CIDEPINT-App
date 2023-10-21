"""Routes for the superuser pages."""
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
    """Route for the site config page."""
    return config.view_config()


@super_bp.route('/edit-config', methods=['GET', 'POST'])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["config_update"])
def edit_config():
    """Route for the site config edit page."""
    return config.edit_config(request)


# USERS
@super_bp.route("/users", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_index"])
def users():
    """Route for the users page."""
    return users_config_controller.users()


@super_bp.route("/users/active", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_index"])
def active():
    """Route for the active users page."""
    return users_config_controller.active()


@super_bp.route("/users/inactive", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_index"])
def inactive():
    """Route for the inactive users page."""
    return users_config_controller.inactive()


@super_bp.route("/users/search", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_index"])
def search():
    """Route for the users search page."""
    return users_config_controller.search()


@super_bp.route("/users/delete-user", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_destroy"])
def delete_user():
    """Route for the user delete page."""
    return users_config_controller.delete_user()


@super_bp.route("/users/add-user", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_create"])
def add_user():
    """Route for the user add page."""
    return users_config_controller.add_user()


@super_bp.route('/confirmation/<string:hashed_email>', methods=['GET'])
def user_added_confirmation(hashed_email):
    """Route for the confirmation page."""
    return users_config_controller.user_added_confirmation(hashed_email)


@super_bp.route("/users/edit-user/<int:user_id>", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_update"])
def edit_user(user_id):
    """Route for the user edit page."""
    return users_config_controller.edit_user(user_id)


@super_bp.route("/users/user-roles/<int:user_id>", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_update"])
def roles(user_id):
    """Route for the user roles page."""
    return users_config_controller.roles(user_id)


@super_bp.route("/users/user-roles/<int:user_id>/add-role", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_update"])
def add_role(user_id):
    """Route for the user roles add page."""
    return users_config_controller.add_role(user_id)


@super_bp.route("/users/user-roles/<int:user_id>/delete-role",
                methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["user_update"])
def delete_role(user_id):
    """Route for the user roles delete page."""
    return users_config_controller.delete_role(user_id)


# INSTITUTIONS
@super_bp.route("/institutions", methods=["GET"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_index",
                                       "institution_show"])
def institutions():
    """Route for the institutions page."""
    return institutions_config_controller.institutions()


@super_bp.route("/institutions/add-institution", methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_create",
                                       "institution_activate",
                                       "institution_deactivate"])
def add_institution():
    """Route for the institution add page."""
    return institutions_config_controller.add_institution()


@super_bp.route("/institutions/edit-institution/<int:institution_id>",
                methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_update",
                                       "institution_activate",
                                       "institution_deactivate"])
def edit_institution(institution_id):
    """Route for the institution edit page."""
    return institutions_config_controller.edit_institution(institution_id)


@super_bp.route("/institutions/delete-institution",
                methods=["POST"])
@LoginWrap.wrap
@PermissionWrap.wrap_args(permissions=["institution_destroy"])
def delete_institution():
    """Route for the institution delete page."""
    return institutions_config_controller.delete_institution()
