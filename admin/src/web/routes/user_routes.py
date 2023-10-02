from flask import Blueprint
from src.web.helpers.auth import login_required

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/<int:user_id>', methods=['GET'])
@login_required
def view_user(user_id):
    return "Mirando perfil..."
