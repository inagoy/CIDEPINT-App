""" 
from marshmallow import ValidationError
from src.core.schemas.service_request import ServiceRequestValidateSchema
from src.core.schemas.service_request import ServiceRequestModelSchema
from src.web.helpers.api import response_error
"""

from flask import Blueprint, request
api_request_bp = Blueprint('api_service_requests', __name__, url_prefix='/api')

"""
@api_request_bp.route("/me/requests", methods=["GET"])
def get_services():
    validator = ServiceRequestValidateSchema.get_instance()
    model_schema = ServiceRequestModelSchema.get_instance(many=True)
    try:
        validated_data = validator.load(request.args)
    except ValidationError:
        return response_error()
    services = ServiceRequest.search_by_keyword(**validated_data)
    services["data"] = model_schema.dump(services["data"].items)
    return services, 200
 """
