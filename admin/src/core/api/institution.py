from marshmallow import ValidationError
from src.core.schemas.institution import institutions_schema
from src.core.schemas import paginated_schema
from src.core.models.institution import Institution
from src.core.api import response_error
from flask import Blueprint, request


api_institution_bp = Blueprint('api_institution', __name__, url_prefix='/api')


@api_institution_bp.route("/instituciones", methods=["GET"])
def get_institutions():
    try:
        validated_data = paginated_schema.load(request.args)
    except ValidationError:
        return response_error()
    institutions = Institution.get_institutions_paginated(**validated_data)
    institutions["data"] = institutions_schema.dump(institutions["data"].items)
    return institutions, 200
