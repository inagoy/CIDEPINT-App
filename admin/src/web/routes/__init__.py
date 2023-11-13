"""Routes for the application."""
from src.web.routes.auth_routes import auth_bp
from src.web.routes.register_routes import register_bp
from src.web.routes.user_routes import user_bp
from src.web.routes.home_routes import home_bp
from src.web.routes.error_routes import error_bp
from src.web.routes.superuser_routes import super_bp
from src.web.routes.institution_routes import institution_bp
from src.web.routes.services_routes import services_bp
from src.web.routes.service_requests_routes import service_requests_bp
from src.core.api.auth import api_auth_bp
from src.core.api.user import api_user_bp
from src.core.api.service import api_service_bp
from src.core.api.institution import api_institution_bp
from src.core.api.service_request import api_request_bp
from src.core.api.site_config import api_site_config


def set_routes(app) -> None:
    """
    Register the blueprints for the different routes of the application.

    Parameters:
        app: The Flask application instance.

    Returns:
        None
    """

    # Controllers
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(super_bp)
    app.register_blueprint(institution_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(service_requests_bp)

    # API JSON
    app.register_blueprint(api_auth_bp)
    app.register_blueprint(api_user_bp)
    app.register_blueprint(api_institution_bp)
    app.register_blueprint(api_service_bp)
    app.register_blueprint(api_request_bp)
    app.register_blueprint(api_site_config)
