from flask import Flask
from src.core import database
from src.web.config import config
from src.web.routes import set_routes
from src.core.controllers import set_controllers
def create_app(env="development", static_folder="../../static"):
    
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    
    set_routes(app)
    set_controllers(app)

    database.init_app(app)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    return app