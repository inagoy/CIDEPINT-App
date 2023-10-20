from src.core.models.user import User
from src.core.models.privileges import Role
from flask import session, abort
from src.core.models.institution import Institution


def superuser_session() -> bool:
    """
    Check if a session is a superuser.

    Args:
        session: The session object.

    Returns:
        bool: True if the session is a superuser, False otherwise.
    """
    user = User.find_user_by_email(session.get("user"))
    role = User.get_role_in_institution(user_id=user.id)
    if not role:
        return False
    return Role.get_role_by_id(id=role).name == "Super Admin"


def is_owner(institution_id) -> bool:
    """
    Check if a session is an owner.

    Args:
        session: The session object.

    Returns:
        bool: True if the session is an owner, False otherwise.
    """
    user = User.find_user_by_email(session.get("user"))
    role = User.get_role_in_institution(user_id=user.id,
                                        institution_id=institution_id)
    if not role:
        return False
    return Role.get_role_by_id(id=role).name == "Owner"


def is_operator() -> bool:
    """
    Check if a session is an owner.

    Args:
        session: The session object.

    Returns:
        bool: True if the session is an owner, False otherwise.
    """
    user = User.find_user_by_email(session.get("user"))
    institution = session.get("current_institution")
    role = User.get_role_in_institution(user_id=user.id,
                                        institution_id=institution)
    if not role:
        return False
    return Role.get_role_by_id(id=role).name == "Operator"


def not_enabled_and_not_owner(institution_id):
    if ((not is_owner(institution_id) and
         not Institution.is_enabled(institution_id))):
        return abort(401)
