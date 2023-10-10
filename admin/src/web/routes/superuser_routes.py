from src.core.controllers import users_config_controller
from src.core.controllers import institutions_config_controller
from src.core.controllers import configuration_controller
from flask import Blueprint


super_bp = Blueprint('super', __name__)


@super_bp.route("/users", methods=["GET"])
def users():
    return users_config_controller.users()


@super_bp.route("/institutions", methods=["GET"])
def institutions():
    return institutions_config_controller.institutions()


@super_bp.route("/configuration", methods=["GET"])
def configuration():
    return configuration_controller.configuration()
