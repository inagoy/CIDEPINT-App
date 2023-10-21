from src.web.routes.auth_routes import auth_bp
from src.web.routes.register_routes import register_bp
from src.web.routes.user_routes import user_bp
from src.web.routes.home_routes import home_bp
from src.web.routes.error_routes import error_bp
from src.web.routes.superuser_routes import super_bp
from src.web.routes.institution_routes import institution_bp
from src.web.routes.services_routes import services_bp
from src.web.routes.service_requests_routes import service_requests_bp


def set_routes(app) -> None:
    """
    Register the blueprints for the different routes of the application.

    Args:
        app: The Flask application instance.

    Returns:
        None
    """
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(super_bp)
    app.register_blueprint(institution_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(service_requests_bp)
