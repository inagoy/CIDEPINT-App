from src.core.schemas.user import user_schema
from src.core.api import response_error
from src.core.models.user import User
from flask import Blueprint, session

api_user_bp = Blueprint('api_user', __name__, url_prefix='/api')


@api_user_bp.route("/me/profile", methods=["GET"])
def get_profile():
    user = User.find_user_by_email(session.get("user"))
    if not user:
        return response_error()
    return {
        "data": user_schema.dump(user)
    }, 200
