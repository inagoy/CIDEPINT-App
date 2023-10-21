"""Routes for the users page."""
from flask import Blueprint, request
from src.core.common.decorators import LoginWrap
from src.core.controllers import user_controller


user_bp = Blueprint('user', __name__, url_prefix='/profile')


@user_bp.route('/', methods=['GET'])
@LoginWrap.wrap
def view_profile():
    """Route for the user profile page."""
    return user_controller.view_profile(request)


@user_bp.route('/edit', methods=['GET', 'POST'])
@LoginWrap.wrap
def edit_profile():
    """Route for the user edit page."""
    return user_controller.edit_profile(request)


@user_bp.route('/password/edit', methods=['GET', 'POST'])
@LoginWrap.wrap
def change_password():
    """Route for the user change password page."""
    return user_controller.change_password(request)
