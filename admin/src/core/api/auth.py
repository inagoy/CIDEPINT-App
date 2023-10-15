from flask import Blueprint, request
from marshmallow import ValidationError
from src.core.schemas.user import auth_user_schema
from src.web.helpers.auth import check_user
from src.core.api import response_error

api_auth_bp = Blueprint('api_auth', __name__, url_prefix='/api')


@api_auth_bp.route("/auth", methods=["POST"])
def api_auth():
    data = request.get_json()
    try:
        parsed = auth_user_schema.load(data)
    except ValidationError:
        return response_error()
    user = check_user(parsed.get("email"), parsed.get("password"))
    if not user:
        return response_error()
    return {"result": "success"}, 200
