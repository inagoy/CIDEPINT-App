from src.core.models.user import User
from src.core.schemas import IdValidateSchema
from src.core.models.service import ServiceRequest
from marshmallow import ValidationError
from src.core.schemas.service_request import PostRequestValidateSchema
from src.core.schemas.service_request import SortedRequestsValidateSchema
from src.core.schemas.service_request import RequestModelSchema
from src.web.helpers.api import paginated_response
from src.web.helpers.api import response_error
from flask import Blueprint, request
api_request_bp = Blueprint('api_requests', __name__, url_prefix='/api')


@api_request_bp.route("/me/requests", methods=["GET"])
def get_requests():
    user_id = request.headers['Authorization']

    id_validator = IdValidateSchema.get_instance()
    validator = SortedRequestsValidateSchema.get_instance()
    model_schema = RequestModelSchema.get_instance(many=True)
    try:
        id_validator.load(
            {'id': user_id}
        )
        validated_data = validator.load(request.args)
    except ValidationError:
        return response_error()
    if User.get_by_id(user_id) is None:
        return response_error()
    service_requests = ServiceRequest.get_user_sorted_paginated(
        user_id=user_id, **validated_data
    )
    return paginated_response(
        service_requests, model_schema
    )


@api_request_bp.route("/me/requests/<int:request_id>", methods=["GET"])
def get_request(request_id):
    user_id = request.headers['Authorization']

    id_validator = IdValidateSchema.get_instance()
    model_schema = RequestModelSchema.get_instance()
    try:
        id_validator.load({'id': user_id})
        id_validator.load({"id": request_id})
    except ValidationError:
        return response_error()
    service_request = ServiceRequest.get_by_id_and_user(
        user_id=user_id, id=request_id
    )
    if not service_request:
        return response_error()
    return model_schema.dump(service_request), 200


@api_request_bp.route("/me/requests/", methods=["POST"])
def post_request():
    user_id = request.headers['Authorization']
    id_validator = IdValidateSchema.get_instance()
    validator = PostRequestValidateSchema.get_instance()
    model_schema = RequestModelSchema.get_instance()
    try:
        id_validator.load({'id': user_id})
        validated_data = validator.load(request.get_json())
    except ValidationError:
        return response_error()
    service_request = ServiceRequest.save(
        requester_id=user_id, **validated_data
    )
    return model_schema.dump(service_request), 200
