from flask import Blueprint
from src.core.models.user import User
from src.web.schemas.user import users_schema

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route("/", methods=["GET"])
def api():
    return {"status": "OK"}, 200


@api_bp.route("/users", methods=["GET"])
def users():
    users = User.query.all()
    data = users_schema.dump(users)
    return data, 201
