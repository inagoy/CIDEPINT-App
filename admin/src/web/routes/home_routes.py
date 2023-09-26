from flask import render_template

def set_home_route(app):
    @app.route("/")
    def home():
        return render_template("home.html")