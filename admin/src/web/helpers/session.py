from src.core.models.user import User
from src.core.models.privileges import Role
from src.core.models.user_role_institution import UserRoleInstitution
from flask import session


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


def is_owner() -> bool:
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
    return Role.get_role_by_id(id=role).name == "Owner"


def has_role() -> bool:
    """
    Check if the user has a role in the institution.

    Parameters:
        None

    Returns:
        bool: True if the user has a role, False otherwise.
    """
    user = User.find_user_by_email(session.get("user"))
    return UserRoleInstitution.get_roles_institutions_of_user(user_id=user.id)


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
