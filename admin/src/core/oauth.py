from authlib.integrations.flask_client import OAuth

oauth = OAuth()


def init_app(app):
    """Initialize the ouath extension for the given Flask app."""
    oauth.init_app(app)
    GOOGLE_METADATA_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name="google",
        server_metadata_url=GOOGLE_METADATA_URL,
        client_kwargs={
            "scope": "openid email profile"
        }
    )
