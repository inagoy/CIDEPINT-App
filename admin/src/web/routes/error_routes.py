"""Routes for error pages."""
from flask import Blueprint
from src.core.controllers.error_controller import unauthorized_error
from src.core.controllers.error_controller import not_found_error

error_bp = Blueprint('error', __name__)


error_bp.app_errorhandler(401)(unauthorized_error)
error_bp.app_errorhandler(404)(not_found_error)
