"""App configuration."""
from os import environ


class Config(object):
    """Base configuration."""

    SECRET_KEY = "secret"
    DEBUG = False
    TESTING = False
    SESSION_TYPE = "filesystem"

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'emiliamancini.m@gmail.com'
    MAIL_PASSWORD = 'ihej sxxz scwj bemi '
    MAIL_DEFAULT_SENDER = ('Administración CIDEPINT', 'MAIL_USERNAME')
    GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET")

    JWT_SECRET_KEY = "PSgrupo05"
    JWT_TOKEN_LOCATION = ["headers"]


class ProductionConfig(Config):
    """Production configuration."""

    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )
    PUBLIC_LOGIN_URL = "https://grupo05.proyecto2023.linti.unlp.edu.ar/login"
    PUBLIC_HOME_URL = "https://grupo05.proyecto2023.linti.unlp.edu.ar/"


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    PUBLIC_APP_PORT = environ.get("PUBLIC_APP_PORT")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )
    PUBLIC_LOGIN_URL = f"http://localhost:{PUBLIC_APP_PORT}/login"
    PUBLIC_HOME_URL = f"http://localhost:{PUBLIC_APP_PORT}/"


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    pass


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
