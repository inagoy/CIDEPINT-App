"""Bcrypt extension for Flask."""
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def init_app(app):
    """Initialize the bcrypt extension for the given Flask app."""
    bcrypt.init_app(app)
