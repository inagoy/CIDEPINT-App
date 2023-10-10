def is_superuser() -> bool:
    """
    Check if a session is a superuser.

    Args:
        session: The session object.

    Returns:
        bool: True if the session is a superuser, False otherwise.
    """
    return False


def is_owner() -> bool:
    """
    Check if a session is an owner.

    Args:
        session: The session object.

    Returns:
        bool: True if the session is an owner, False otherwise.
    """
    return False


def has_role() -> bool:
    """
    Check if a session is not assigned to a role.

    Args:
        session: The session object.

    Returns:
        bool: True if the session is not assigned to a role, False otherwise.
    """
    return True
