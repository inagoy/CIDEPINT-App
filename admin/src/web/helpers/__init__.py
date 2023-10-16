from src.web.helpers import session
from src.web.helpers import users


def set_helpers(app) -> None:
    """
    Set the necessary helpers in the Jinja environment of the app.

    Parameters:
        app (object): The Flask app object.

    Returns:
        None: This function does not return anything.
    """
    app.jinja_env.globals.update(is_owner=session.is_owner)
    app.jinja_env.globals.update(superuser_session=session.superuser_session)
    app.jinja_env.globals.update(has_role=session.has_role)
    app.jinja_env.globals.update(parse_user=users.parse_user)