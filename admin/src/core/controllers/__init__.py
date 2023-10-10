from .error_controller import not_found_error


def set_controllers(app) -> None:
    app.register_error_handler(404, not_found_error)
