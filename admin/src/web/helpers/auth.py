from functools import wraps
from flask import session, abort


def is_authenticated(session) -> bool:
    """
    Check if a session is authenticated.

    Args:
        session: The session object.

    Returns:
        bool: True if the session is authenticated, False otherwise.
    """
    return session.get("user") is not None


def login_required(func):
    """ login_required
    Decorator function that adds login required functionality
    to a given function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    Raises:
        None

    Example:
        @login_required
        def my_function():
            pass
    """
    @wraps(func)
    def decorated_func(*args, **kwargs):
        """
        Decorates a function to check if the user is authenticated
        before executing it.

        Parameters:
            func (function): The function to be decorated.

        Returns:
            function: The decorated function.

        Raises:
            HTTPException: If the user is not authenticated
            (HTTP status code 401).
        """
        if is_authenticated(session):
            return abort(401)
        return func(*args, **kwargs)

    return decorated_func
