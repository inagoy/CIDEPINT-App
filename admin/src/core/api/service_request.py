from src.core.models.service import Note, ServiceRequest
from marshmallow import ValidationError
from src.core.schemas.service_request import NoteModelSchema, NotesModelSchema
from src.core.schemas.service_request import PostNoteValidateSchema
from src.core.schemas.service_request import PostRequestValidateSchema
from src.core.schemas.service_request import SortedRequestsValidateSchema
from src.core.schemas.service_request import RequestModelSchema
from src.web.helpers.api import paginated_response
from src.web.helpers.api import response_error
from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from flask_cors import cross_origin
api_request_bp = Blueprint('api_requests', __name__, url_prefix='/api')


@api_request_bp.route("/me/requests", methods=["GET"])
@cross_origin()
@jwt_required()
def get_requests():
    """
    Get all service requests.
    """
    user_id = get_jwt_identity()
    validator = SortedRequestsValidateSchema.get_instance()
    model_schema = RequestModelSchema.get_instance(many=True)

    try:
        validated_data = validator.load(request.args)
    except ValidationError:
        return response_error()
    service_requests = ServiceRequest.get_user_sorted_paginated(
        user_id=user_id, **validated_data
    )
    return paginated_response(
        service_requests, model_schema
    )


@api_request_bp.route("/me/requests/<int:request_id>", methods=["GET"])
@cross_origin()
@jwt_required()
def get_request(request_id):
    user_id = get_jwt_identity()
    model_schema = RequestModelSchema.get_instance()

    service_request = ServiceRequest.get_by_id_and_user(
        user_id=user_id, id=request_id
    )
    if not service_request:
        return response_error()
    return model_schema.dump(service_request), 200


@api_request_bp.route("/me/requests/", methods=["POST"])
@cross_origin()
@jwt_required()
def post_request():
    user_id = get_jwt_identity()
    validator = PostRequestValidateSchema.get_instance()
    model_schema = RequestModelSchema.get_instance()

    try:
        validated_data = validator.load(request.get_json())
    except ValidationError:
        return response_error()
    service_request = ServiceRequest.save(
        requester_id=user_id, **validated_data
    )
    return model_schema.dump(service_request), 200


@api_request_bp.route("/me/requests/<int:request_id>/notes", methods=["POST"])
@cross_origin()
@jwt_required()
def post_note(request_id):
    user_id = get_jwt_identity()
    validator = PostNoteValidateSchema.get_instance()
    model_schema = NoteModelSchema.get_instance()

    try:
        validated_data = validator.load(request.get_json())
    except ValidationError:
        return response_error()
    if not ServiceRequest.get_by_id(request_id):
        return response_error()
    note = Note.save(
       **validated_data, service_request_id=request_id,
       user_id=user_id
    )
    return model_schema.dump(note), 200


@api_request_bp.route("/me/requests/<int:request_id>/notes", methods=["GET"])
@cross_origin()
@jwt_required()
def get_notes(request_id):
    model_schema = NotesModelSchema.get_instance(many=True)

    notes = Note.get_notes_of_service_request(request_id)
    return {"data": model_schema.dump(notes)}, 200
