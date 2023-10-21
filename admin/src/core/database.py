"""Database."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    """Initialize the database of the app."""
    db.init_app(app)
    config_db(app)


def config_db(app):
    """Configure the database for the app."""
    @app.teardown_request
    def close_session(exception=None):
        db.session.close()


def reset_db():
    """Reset the database."""
    print("Eliminando base de datos...")
    db.drop_all()
    print("Creando base de datos...")
    db.create_all()
    print("Done!")
