from flask import render_template


def not_found_error(e):
    """
    Handle the not found error.

    Args:
        e: The exception object representing the error.

    Returns:
        A tuple containing the rendered error template and the HTTP
        response status code.

    Raises:
        None.
    """
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que se quiere acceder no existe"
    }

    return render_template("error.html", **kwargs), 400
