from .auth_routes import auth_bp
from .user_routes import user_bp
from .home_routes import set_home_route


def set_routes(app) -> None:
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    set_home_route(app)
