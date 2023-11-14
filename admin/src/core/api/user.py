from flask import Blueprint
from src.core.models.user import User
from src.core.schemas.user import UserModelSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

api_user_bp = Blueprint('api_user', __name__, url_prefix='/api')


@api_user_bp.route("/me/profile", methods=["GET"])
@cross_origin()
@jwt_required()
def get_profile():
    """
    Get user profile, only for authenticated users.
    """
    user_id = get_jwt_identity()
    user = User.get_by_id(user_id)
    return {
        "data": UserModelSchema.get_instance().dump(user)
    }, 200
