from src.core.models.service import Service
from src.core.api import response_error
from flask import Blueprint, request
from marshmallow import ValidationError
from src.core.schemas import id_schema
from src.core.schemas.service import search_services_schema, services_schema, \
                                     service_schema, services_types_schema

api_service_bp = Blueprint('api_services', __name__, url_prefix='/api')


@api_service_bp.route("/services/search", methods=["GET"])
def get_services():
    try:
        validated_data = search_services_schema.load(request.args)
    except ValidationError:
        return response_error()
    services = Service.search_by_keyword(**validated_data)
    services["data"] = services_schema.dump(services["data"].items)
    return services, 200


@api_service_bp.route("/services/<int:service_id>", methods=["GET"])
def get_service(service_id):
    try:
        validated_data = id_schema.load({"id": service_id})
    except ValidationError:
        return response_error()
    service = Service.get(**validated_data)
    if not service:
        return response_error()
    return service_schema.dump(service), 200


@api_service_bp.route("/services-types", methods=["GET"])
def get_services_types():
    services_types = Service.get_all_service_types()
    return services_types_schema.dump({"data": services_types}), 200
