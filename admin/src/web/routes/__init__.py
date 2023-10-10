from src.web.routes.auth_routes import auth_bp
from src.web.routes.register_routes import register_bp
from src.web.routes.user_routes import user_bp
from src.web.routes.home_routes import home_bp
from src.web.routes.error_routes import error_bp
from src.web.routes.superuser_routes import super_bp


def set_routes(app) -> None:
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(super_bp)
