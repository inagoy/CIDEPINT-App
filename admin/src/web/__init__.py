from flask import Flask

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__)

    @app.get("/")
    def home():
        return "Hola Mundo!"

    return app