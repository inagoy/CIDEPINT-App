"""Helper functions for users."""
from flask import session
from src.core.models.user import User
from src.core.models.user_role_institution import UserRoleInstitution
from src.core.models.institution import Institution
import json


def parse_users_roles(users, institution_id):
    """
    Parse the roles of a list of users for a given institution.

    Parameters:
        users (list): A list of user objects.
        institution_id (int): The ID of the institution.

    Returns:
        list: A list of dictionaries containing:
            - id (int): The ID of the user.
            - first_name (str): The user's first name.
            - last_name (str): The user's last name.
            - email (str): The user's email.
            - role (str): The user's role in the institution.
            - active (str): The user's active status.
    """
    return [{'id': user.id,
             'first_name': user.first_name,
             'last_name': user.last_name,
             'email': user.email,
             'role': UserRoleInstitution.get_user_institution_roles(
                 user_id=user.id, institution_id=institution_id
             ),
             'active': str(user.active),
             } for user in users]


def parse_user(user):
    """
    Generate a dictionary with the user's information.

    Parameters:
        user (User): The user object containing the user's information.

    Returns:
        dict: A dictionary with the user's information
    """
    data = {'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'document': user.document,
            'phone': user.phone_number,
            'address': user.address,
            'active': str(user.active),
            'gender': User.get_gender_name(user.id) if user.gender else None,
            }
    return json.dumps(data)


def get_name(user):
    """Return the full name of the user."""
    return user.first_name + " " + user.last_name


def unique_data_check(user, form, errors):
    """
    Check that the user data is unique in the table.

    Parameters:
        user (User): The user object.
        form (dict): The form data.
        errors (dict): The dictionary of errors.

    Returns:
        str or None: The error message if there is a uniqueness violation,
        None otherwise.
    """
    for field in errors:
        if getattr(user, field) != form[field]:
            return errors[field]
    return None


def get_role_of_user(user_id):
    """
    Get the role of a user.

    Parameters:
        user_id (int): The ID of the user.

    Returns:
        int: The ID of the user's role in the institution.
            None otherwise.
    """
    user = UserRoleInstitution.get_user_institution_roles(
        user_id=user_id, institution_id=session.get("current_institution"))
    if user:
        return user.role_id
    else:
        return None


def get_institutions_user() -> list:
    """
    Get the list of institutions for a user.

    Returns:
        list: The list of institutions.
    """
    user_id = User.find_user_by(field='email', value=session.get('user')).id
    active_institutions = (Institution.
                           get_enabled_institutions_for_user(user_id=user_id))

    owned_institutions = (Institution.
                          get_institutions_owned_by_user(user_id=user_id))
    return list(set(active_institutions + owned_institutions))
