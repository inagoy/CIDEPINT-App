from flask import render_template


def not_found_error(e):
    """not_found_error

    A function that handles the not found error.

    Parameters:
    - e: The exception object representing the error.

    Returns:
    - A tuple containing the rendered error template and the HTTP
    response code 404.
    """

    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que se quiere acceder no existe"
    }

    return render_template("error.html", **kwargs), 404


def unauthorized_error(e):
    """unauthorized_error

    A function that handles unauthorized errors.

    Args:
        e: The unauthorized error object.

    Returns:
        A rendered HTML template for the error page and the
        HTTP status code 401.
    """

    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "Debe iniciar sesión para acceder " +
                             "al recurso solicitado"
    }

    return render_template("error.html", **kwargs), 401
