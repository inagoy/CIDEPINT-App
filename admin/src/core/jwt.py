from flask_jwt_extended import JWTManager

jwt = JWTManager()


def init_app(app):
    """Initialize the database of the app."""
    jwt.init_app(app)