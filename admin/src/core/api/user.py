from src.core.schemas.user import UserSchema
from src.web.helpers.api import response_error, get_user_if_valid
from flask import Blueprint, request

api_user_bp = Blueprint('api_user', __name__, url_prefix='/api')


@api_user_bp.route("/me/profile", methods=["GET"])
def get_profile():
    user = get_user_if_valid(request.args.get('user_id'))
    if not user:
        return response_error()
    return {
        "data": UserSchema.get_instance().dump(user)
    }, 200
