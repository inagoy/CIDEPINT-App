from flask import session
from src.core.models.user import User
from src.core.models.user_role_institution import UserRoleInstitution


def parse_users_roles(users, institution_id):
    """
    Generates a list of dictionaries containing user information.

    :param users: A list of user objects.
    :type users: list
    :return: A list of dictionaries with user information.
    :rtype: list
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
    Generates a dictionary with the user's information.

    Args:
        user (User): The user object containing the user's information.

    Returns:
        dict: A dictionary with the user's information
    """
    return {'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'document': user.document,
            'document_type': User.get_document_type_name(user.id),
            'phone': user.phone_number,
            'address': user.address,
            'active': str(user.active),
            'gender': User.get_gender_name(user.id)
            }


def get_name(user):
    return user.first_name + " " + user.last_name


def unique_data_check(user, form, errors):
    """   
    Args:
        user (User): The user object containing the existing user data.
        form (dict): The form object containing the form data to be checked.
        errors (dict): The dictionary containing the error types.
        
    Returns:
        str or None: The error type if the data is not unique,
        None if all data is unique.
    """
    if 'email' in errors:
        # chequear que el mail del usuario y del form sean iguales
        if user.email != form['email']:
            return errors['email']
    if 'username' in errors:
        if user.username != form['username']:
            return errors['username']
    if 'document' in errors:
        if user.document != form['document']:
            return errors['document']
    if 'phone_number' in errors:
        if user.phone_number != form['phone_number']:
            return errors['phone_number']
    return None


def get_role_of_user(user_id):
    """
    Get the role of a user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        int: The ID of the user's role in the institution.
    """
    user = UserRoleInstitution.get_user_institution_roles(
        user_id=user_id, institution_id=session["current_institution"])
    if user:
        return user.role_id
    else:
        return None