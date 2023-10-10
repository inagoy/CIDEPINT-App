from src.web.helpers import roles


def set_helpers(app) -> None:
    app.jinja_env.globals.update(is_owner=roles.is_owner)
    app.jinja_env.globals.update(is_superuser=roles.is_superuser)
    app.jinja_env.globals.update(has_role=roles.has_role)
