from src.core.models.user import User
from marshmallow import ValidationError
from src.core.schemas.user import UserModelSchema, UserValidationSchema
from src.web.helpers.api import response_error
from flask import Blueprint, request

api_user_bp = Blueprint('api_user', __name__, url_prefix='/api')


@api_user_bp.route("/me/profile", methods=["GET"])
def get_profile():
    user_validator = UserValidationSchema.get_instance()
    try:
        user_validated_data = user_validator.load(
            {"id": request.headers['Authorization']}
        )
    except ValidationError:
        return response_error()
    user = User.get_by_id(**user_validated_data)
    if not user:
        return response_error()
    return {
        "data": UserModelSchema.get_instance().dump(user)
    }, 200
