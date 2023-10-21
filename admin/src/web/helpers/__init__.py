from src.web.helpers import session
from src.web.helpers import users, institutions, services


def set_helpers(app) -> None:
    """
    Set the necessary helpers in the Jinja environment of the app.

    Parameters:
        app (object): The Flask app object.

    Returns:
        None: This function does not return anything.
    """
    app.jinja_env.globals.update(is_owner=session.is_owner)
    app.jinja_env.globals.update(is_operator=session.is_operator)
    app.jinja_env.globals.update(superuser_session=session.superuser_session)
    app.jinja_env.globals.update(parse_user=users.parse_user)
    app.jinja_env.globals.update(get_role=users.get_role_of_user)
    app.jinja_env.globals.update(parse_service=services.parse_service)
    app.jinja_env.globals.update(
        parse_service_request=services.parse_service_request
    )
    app.jinja_env.globals.update(parse_note=services.parse_note)
    app.jinja_env.globals.update(
        parse_institution=institutions.parse_institution
    )
    app.jinja_env.globals.update(parse_note=services.parse_note)
