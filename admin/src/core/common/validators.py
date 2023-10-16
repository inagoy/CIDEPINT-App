import re
from src.core.models.user import User


class ValidationError(Exception):

    def __init__(self, msg="", *args: object) -> None:
        super().__init__(msg, *args)


def validate_email(email):
    """
    Validates an email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email address is not valid.

    Returns:
        str: The validated email address.
    """
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if not re.match(email_pattern, email) is not None:
        raise ValidationError(f"El campo '{email}' no es un email válido")
    return email


def validate_just_text(text):
    """
    Validate if the given text contains only alphabetic characters.

    Args:
        text (str): The text to be validated.

    Returns:
        str: The validated text.

    Raises:
        ValidationError: If the text contains non-alphabetic characters.
    """
    text_pattern = r'^[^\d_\W]+$'
    if not re.match(text_pattern, text, re.UNICODE) is not None:
        raise ValidationError(f"El campo '{text}' no es un texto")
    return text


def validate_just_number(number):
    """
    Validates if the given number is a valid number.

    Parameters:
        number (str): The number to be validated.

    Returns:
        str: The validated number.

    Raises:
        ValidationError: If the number is not a valid number.
    """
    number_pattern = r'^\d+$'
    if not re.match(number_pattern, number):
        raise ValidationError(f"El campo '{number}' no es un número")
    return number


def validate_username(text):
    """
    Validates a username.

    Args:
        text (str): The text to be validated.

    Raises:
        ValidationError: If the text does not match the required pattern.

    Returns:
        str: The validated username.

    """
    text_pattern = r'^[A-Za-z0-9_]+$'
    if not re.match(text_pattern, text):
        raise ValidationError(
            f"El campo'{text}' no es un nombre de usuario válido")
    return text


def validate_password(password):
    """
    Validates a password string.

    Args:
        password (str): The password to be validated.

    Raises:
        ValidationError: If the password does not meet the
        specified requirements.

    Returns:
        str: The validated password.

    """
    pattern = r'^(?=.*[A-Z])(?=.*\d).{6,}$'

    if not re.match(pattern, password):
        raise ValidationError(
            f"El campo'{password}' no es una contraseña válida")
    return password


def validate_address(address):
    """
    Validates an address using a regex pattern.

    Args:
        address (str): The address to be validated.

    Raises:
        ValidationError: If the address is not valid.

    Returns:
        str: The validated address.
    """
    # Define a regex pattern to check if there's at least one number
    pattern = r'^[a-zA-Z\s.,-]*\d+[a-zA-Z0-9\s.,-]*$'

    if not re.match(pattern, address):
        raise ValidationError(
            f"El campo'{address}' no es una dirección válida")
    return address


def validate_phone_number(phone_number):
    """
    Validates a phone number.

    Args:
        phone_number (str): The phone number to validate.

    Raises:
        ValidationError: If the phone number is not valid.

    Returns:
        str: The validated phone number.
    """
    phone_number = phone_number.strip()
    phone_number_pattern = r'^\d{9,15}$'

    if not re.match(phone_number_pattern, phone_number):
        raise ValidationError(
            f"El campo'{phone_number}' no es un teléfono válido")
    return phone_number


def validate_form_data(form_data, expected_parameters):
    """
    Validates the form data against the expected parameters.

    Args:
        form_data (dict): A dictionary containing the form data.
        expected_parameters (list): A list of expected parameter names.

    Returns:
        dict: The validated form data.

    Raises:
        ValidationError: If there are missing parameters in the form data.
    """
    missing_parameters = [
        param for param in expected_parameters if param not in form_data
    ]
    if missing_parameters:
        raise ValidationError(
            "Hay campos faltantes"
        )
    else:
        return form_data


def validate_no_username(text):
    """
    Validates that the given text does not match an existing username.

    Parameters:
        text (str): The text to be validated.

    Returns:
        str: The validated text.

    Raises:
        ValidationError: If the given text matches an existing username.
    """
    if User.find_user_by_username(text):
        raise ValidationError(
            f"El nombre de usuario '{text}' ya está registrado")
    return text


def validate_no_email(email):
    """
    Validates if the given email is not already registered in the User
    database.

    Parameters:
        email (str): The email to be validated.

    Returns:
        str: The validated email.

    Raises:
        ValidationError: If the email is already registered.

    """
    if User.find_user_by_email(email):
        raise ValidationError(
            f"El email '{email}' ya está registrado")
    return email


def validate_no_document(document):
    """
    Validates if a document is already registered in the system.

    Parameters:
        document (str): The document to validate.

    Raises:
        ValidationError: If the document is already registered.

    Returns:
        str: The validated document.
    """
    if User.find_user_by_document(document):
        raise ValidationError(
            f"El documento '{document}' ya está registrado")
    return document


def validate_no_phone_number(phone_number):
    """
    Validates that the given phone number is not already registered.

    Parameters:
        phone_number (str): The phone number to be validated.

    Returns:
        str: The validated phone number.

    Raises:
        ValidationError: If the phone number is already registered.
    """
    if User.find_user_by_phone_number(phone_number):
        raise ValidationError(
            f"El número de teléfono '{phone_number}' ya está registrado")
    return phone_number


def validate_string_as_boolean(value):
    """
    Validates that the given value is a True or False string.

    Parameters:
        field (str): The value to be validated.

    Raises:
        ValidationError: If the value is neither True nor False.

    Returns:
        True if a string with the value "True" or "False", False otherwise.
    """
    if value == "True" or value == "False":
        return True
    else:
        raise ValidationError(
            f"El valor '{value}' no es un verdadero o falso")


def validate_string(value):
    """
    Validates that the given value is a string.

    Parameters:
        field (str): The value to be validated.

    Raises:
        ValidationError: If the value is not a string.

    Returns:
        True if the value is a string, False otherwise.
    """
    if isinstance(value, str) and len(value) <= 255:
        return True
    else:
        raise ValidationError(
            f"El valor '{value}' no es un texto válido")