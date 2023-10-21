from src.core.schemas.user import UserSchema
from src.web.helpers.api import response_error
from src.core.models.user import User
from flask import Blueprint, request

api_user_bp = Blueprint('api_user', __name__, url_prefix='/api')


@api_user_bp.route("/me/profile", methods=["GET"])
def get_profile():
    user_id = request.args.get('user_id')
    if not user_id:
        return response_error()
    user = User.get_by_id(user_id)
    if not user:
        return response_error()
    return {
        "data": UserSchema.get_instance().dump(user)
    }, 200
