from src.core.schemas.service import search_service_schema, services_schema
from src.core.models.service import Service
from src.core.models.user import User
from src.core.schemas.institution import institutions_schema
from src.core.models.institution import Institution
from src.web.helpers.auth import check_user
from src.core.schemas.user import user_schema, auth_user_schema
from marshmallow import ValidationError
from flask import Blueprint, request, session

api_bp = Blueprint('api', __name__, url_prefix='/api')


def response_error():
    return {
        "error": "Parámetros inválidos"
    }, 400


@api_bp.route("/auth", methods=["POST"])
def auth():
    data = request.get_json()
    try:
        parsed = auth_user_schema.load(data)
    except ValidationError:
        return response_error()
    user = check_user(parsed.get("email"), parsed.get("password"))
    if not user:
        return {"error": "No se encontró el usuario"}, 400
    return {"result": "success"}, 200


@api_bp.route("/instituciones", methods=["GET"])
def get_institutions():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except ValueError:
        return response_error()
    institutions = Institution.get_institutions_paginated(page, per_page)
    if institutions is None:
        return response_error()

    return {
        "data": institutions_schema.dump(institutions.items),
        "page": page,
        "per_page": per_page,
        "total": Institution.count()
    }, 200


@api_bp.route("/me/profile", methods=["GET"])
def get_profile():
    user = User.find_user_by_email(session.get("user"))
    if not user:
        return response_error()
    return {
        "data": user_schema.dump(user)
    }, 200


@api_bp.route("/servicios", methods=["GET"])
def get_services():
    try:
        validated_data = search_service_schema.load(request.args)
    except ValidationError:
        return response_error()
    services = Service.search_by_keyword(**validated_data)
    if services is None:
        return response_error()
    return {
        "data": services_schema.dump(services.items),
        "page": validated_data["page"],
        "per_page": validated_data["per_page"],
        "total": Service.count()
    }, 200
