from flask import Flask
from flask import render_template
from web.controllers import error_controller
from web.routes import user_routes
from src.core import database
from src.web.config import config
def create_app(env="development", static_folder="../../static"):
    
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    
    app.register_blueprint(user_routes.user_bp)

    app.register_error_handler(404, error_controller.not_found_error)

    database.init_app(app)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.get("/")
    def home():
        return render_template("home.html")

    return app