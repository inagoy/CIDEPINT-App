from flask import Blueprint, request
from marshmallow import ValidationError
from src.core.schemas.user import UserValidateSchema
from src.web.helpers.auth import check_user
from src.web.helpers.api import response_error
from flask_jwt_extended import create_access_token
from flask_cors import cross_origin

api_auth_bp = Blueprint('api_auth', __name__, url_prefix='/api')


@api_auth_bp.route("/auth", methods=["POST"])
@cross_origin()
def api_auth():
    validator = UserValidateSchema.get_instance()
    try:
        validated_data = validator.load(request.get_json())
    except ValidationError:
        return response_error()
    user = check_user(
        validated_data.get("user"), validated_data.get("password")
    )
    if not user:
        return response_error()
    access_token = create_access_token(identity=user.id)
    return {"access_token": access_token}, 200
