from flask import Flask
from flask_session import Session
from src.core import database
from src.core import mail
from src.web.config import config
from src.web import seeds
from src.web.routes import set_routes
from src.core.controllers import set_controllers
from src.core.bcrypt import bcrypt
from src.core.common.decorators import LoginWrap
from src.web.helpers import set_helpers

session = Session()


def create_app(env="development", static_folder="../../static"):

    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    set_routes(app)
    set_controllers(app)

    session.init_app(app)

    bcrypt.init_app(app)

    database.init_app(app)

    mail.init_app(app)

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
