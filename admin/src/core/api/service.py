from src.core.models.service import Service
from src.web.helpers.api import response_error, paginated_response
from src.web.helpers.api import convert_to_percentage
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
    """
    Get a service by its ID.
    """
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


@api_service_bp.route("/services/top-requested", methods=["GET"])
@cross_origin()
def get_most_popular_services():
    populars = Service.get_top_requested_services()
    res = convert_to_percentage(populars['requests'])
    populars['percentages'] = res['percentages']
    populars['total'] = res['total']
    return {
        "data": populars
    }, 200


@api_service_bp.route("/services/requests-by-type", methods=["GET"])
@cross_origin()
def get_requests_per_service():
    by_type = Service.get_request_count_by_service_type()
    return {
        "data": by_type
    }, 200
