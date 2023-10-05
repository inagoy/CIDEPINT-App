from flask import Blueprint
# from src.core.common.decorators import login_required
from src.core.common.decorators import LoginWrap


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/<int:user_id>', methods=['GET'])
@LoginWrap.wrap
def view_user(user_id):
    return "Mirando perfil..."
