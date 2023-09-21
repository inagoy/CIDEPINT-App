from flask import Flask
from flask import render_template
from .controllers import error_controller
from .routes import user_routes

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)

    @app.get("/")
    def home():
        return render_template("home.html")
    
    app.register_blueprint(user_routes.user_bp)

    app.register_error_handler(404, error_controller.not_found_error)

    return app