from src.web.helpers import roles


def set_helpers(app) -> None:
    """
    Set the necessary helpers in the Jinja environment of the app.

    Parameters:
        app (object): The Flask app object.

    Returns:
        None: This function does not return anything.
    """
    app.jinja_env.globals.update(is_owner=roles.is_owner)
    app.jinja_env.globals.update(is_superuser=roles.is_superuser)
    app.jinja_env.globals.update(has_role=roles.has_role)
