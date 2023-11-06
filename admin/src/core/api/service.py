from src.core.models.service import Service
from src.web.helpers.api import response_error, paginated_response
from flask import Blueprint, request
from marshmallow import ValidationError
from src.core.schemas.service import ServiceModelSchema
from src.core.schemas.service import ServicesTypesModelSchema
from src.core.schemas.service import SearchServicesValidateSchema
from flask_cors import cross_origin

api_service_bp = Blueprint('api_services', __name__, url_prefix='/api')


@api_service_bp.route("/services/search", methods=["GET"])
@cross_origin()
def get_services():
    validator = SearchServicesValidateSchema.get_instance()
    model_schema = ServiceModelSchema.get_instance(many=True)
    try:
        validated_data = validator.load(request.args)
    except ValidationError:
        return response_error()
    services = Service.search_by_keyword(**validated_data)
    return paginated_response(
        services, model_schema
    )


@api_service_bp.route("/services/<int:service_id>", methods=["GET"])
@cross_origin()
def get_service(service_id):
    model_schema = ServiceModelSchema.get_instance()
    service = Service.get(service_id)
    if not service:
        return response_error()
    return model_schema.dump(service), 200


@api_service_bp.route("/services-types", methods=["GET"])
@cross_origin()
def get_services_types():
    model_schema = ServicesTypesModelSchema.get_instance()
    services_types = Service.get_all_service_types()
    return model_schema.dump({"data": services_types}), 200
