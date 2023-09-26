from flask import Blueprint

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def view_user(user_id):
    return "Mirando perfil..."