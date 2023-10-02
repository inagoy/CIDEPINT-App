from src.core.controllers import home_controller
from flask import Blueprint


home_bp = Blueprint('home', __name__)


@home_bp.route("/")
def home():
    return home_controller.home()
