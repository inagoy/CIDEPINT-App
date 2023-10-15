from src.core.schemas.institution import institutions_schema
from src.core.models.institution import Institution
from src.core.api import response_error
from flask import Blueprint, request


api_institution_bp = Blueprint('api_institution', __name__, url_prefix='/api')


@api_institution_bp.route("/instituciones", methods=["GET"])
def get_institutions():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except ValueError:
        return response_error()
    institutions = Institution.get_institutions_paginated(page, per_page)
    if institutions is None:
        return response_error()

    return {
        "data": institutions_schema.dump(institutions.items),
        "page": page,
        "per_page": per_page,
        "total": Institution.count()
    }, 200
