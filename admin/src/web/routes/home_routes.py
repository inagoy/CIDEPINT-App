from src.core.controllers import home_controller
from flask import Blueprint
from src.core.common.decorators import LoginWrap

home_bp = Blueprint('home', __name__)


@home_bp.route("/")
def home():
    return home_controller.home()


@home_bp.route("/-")
@LoginWrap.wrap
def home_user():
    return home_controller.home_user()
