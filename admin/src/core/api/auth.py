from flask import Blueprint, request
from marshmallow import ValidationError
from src.core.schemas.user import UserValidateSchema
from src.web.helpers.auth import check_user, check_google_user
from flask_jwt_extended import create_access_token
from flask_cors import cross_origin
from google.oauth2 import id_token
from google.auth.transport import requests


api_auth_bp = Blueprint('api_auth', __name__, url_prefix='/api')


@api_auth_bp.route("/auth", methods=["POST"])
@cross_origin()
def api_auth():
    """
    Login, return an access token if credentials are valid.
    """
    validator = UserValidateSchema.get_instance()
    try:
        validated_data = validator.load(request.get_json())
    except ValidationError:
        return {"error": "El usuario o la contraseña son incorrectos"}, 401
    user = check_user(
        validated_data.get("user"), validated_data.get("password")
    )
    if not user:
        return {"error": "El usuario o la contraseña son incorrectos"}, 401
    access_token = create_access_token(identity=user.id)
    return {"token": access_token}, 201


@api_auth_bp.route("/auth-google", methods=["POST"])
@cross_origin()
def api_auth_google():
    authinfo = request.get_json()
    idinfo = id_token.verify_oauth2_token(authinfo['credential'],
                                          requests.Request(),
                                          authinfo['client_id'])
    if not idinfo:
        return {"error": "Unauthorized"}, 401
    user = check_google_user(idinfo['email'])
    if not user:
        return {"error": "El usuario no está registrado"}, 401
    access_token = create_access_token(identity=user.id)
    return {"token": access_token}, 201
