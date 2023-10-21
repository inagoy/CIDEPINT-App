from flask import Blueprint, request
from marshmallow import ValidationError
from src.core.schemas.user import UserValidateSchema
from src.web.helpers.auth import check_user
from src.web.helpers.api import response_error

api_auth_bp = Blueprint('api_auth', __name__, url_prefix='/api')


@api_auth_bp.route("/auth", methods=["POST"])
def api_auth():
    data = request.get_json()
    try:
        parsed = UserValidateSchema.get_instance().load(data)
    except ValidationError:
        return response_error()
    user = check_user(parsed.get("user"), parsed.get("password"))
    if not user:
        return response_error()
    return {"result": "success"}, 200
