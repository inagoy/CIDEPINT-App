from marshmallow import ValidationError
from src.core.schemas import PaginateValidateSchema
from src.core.schemas.institution import InstitutionModelSchema
from src.core.models.institution import Institution
from src.web.helpers.api import response_error
from flask import Blueprint, request
from src.web.helpers.api import paginated_response
from flask_cors import cross_origin

api_institution_bp = Blueprint('api_institution', __name__, url_prefix='/api')


@api_institution_bp.route("/institutions", methods=["GET"])
@cross_origin()
def get_institutions():
    validator = PaginateValidateSchema.get_instance()
    model_schema = InstitutionModelSchema.get_instance(many=True)
    try:
        validated_data = validator.load(
            request.args
        )
    except ValidationError:
        return response_error()
    institutions = Institution.get_paginated(**validated_data)
    return paginated_response(
        institutions, model_schema
    )
