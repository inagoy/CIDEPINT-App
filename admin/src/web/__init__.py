"""Initialize the web app."""
from flask import Flask
from flask_cors import CORS
from flask_session import Session
from src.core import database
from src.core import mail
from src.web.config import config
from src.web import seeds
from src.web.routes import set_routes
from src.core.bcrypt import bcrypt
from src.core.jwt import jwt
from src.core import oauth
from src.core.common.decorators import LoginWrap
from src.web.helpers import set_helpers

session = Session()


def create_app(env="development", static_folder="../../static"):
    """
    Create a Flask application.

    Parameters:
    - env (str): The environment to run the application in. Default is
    "development".
    - static_folder (str): The path to the static folder. Default is
    "../../static".

    Returns:
    - app (Flask): The Flask application object.
    """
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    oauth.init_app(app)

    set_routes(app)

    session.init_app(app)

    bcrypt.init_app(app)

    database.init_app(app)

    mail.init_app(app)

    jwt.init_app(app)

    # Jinja
    app.jinja_env.globals.update(is_authenticated=LoginWrap.evaluate_condition)
    set_helpers(app)

    # Commands
    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seedsdb")
    def seedsdb():
        seeds.run_seeds()

    return app
