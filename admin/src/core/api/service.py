from src.core.models.service import Service
from src.core.api import response_error
from flask import Blueprint, request
from marshmallow import ValidationError
from src.core.schemas.service import search_service_schema, services_schema

api_service_bp = Blueprint('api_services', __name__, url_prefix='/api')


@api_service_bp.route("/servicios", methods=["GET"])
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
