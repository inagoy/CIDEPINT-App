from src.core.schemas import IdSchema
from src.core.models.service import ServiceRequest
from marshmallow import ValidationError
from src.core.schemas.service_request import ServiceRequestValidateSchema
from src.core.schemas.service_request import ServiceRequestModelSchema
from src.web.helpers.api import get_user_if_valid, paginated_response, response_error
from flask import Blueprint, request
api_request_bp = Blueprint('api_requests', __name__, url_prefix='/api')


@api_request_bp.route("/me/requests", methods=["GET"])
def get_requests():
    user = get_user_if_valid(request.args.get('user_id'))
    if not user:
        return response_error()
    validator = ServiceRequestValidateSchema.get_instance()
    model_schema = ServiceRequestModelSchema.get_instance(many=True)
    try:
        validated_data = validator.load(request.args)
    except ValidationError:
        return response_error()
    service_requests = ServiceRequest.get_user_sorted_paginated(
        **validated_data
    )
    return paginated_response(
        service_requests, model_schema
    )


@api_request_bp.route("/me/requests/<int:request_id>", methods=["GET"])
def get_request(request_id):

    user = get_user_if_valid(request.args.get('user_id'))
    if not user:
        return response_error()

    validator = IdSchema.get_instance()
    model_schema = ServiceRequestModelSchema.get_instance()
    try:
        validated_data = validator.load({"id": request_id})
    except ValidationError:
        return response_error()
    service_request = ServiceRequest.get_by_id_and_user(
        user.id, **validated_data
    )
    if not service_request:
        return response_error()
    return model_schema.dump(service_request), 200
