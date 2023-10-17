import re
import datetime
from src.core.models.service import StatusEnum
from marshmallow import ValidationError
from src.core.models.service import ServiceTypeEnum
from src.core.models.user import DocumentEnum, GenderEnum, User
from marshmallow import ValidationError


def validate_not_empty(text):
    """
    Validate if the given text is not empty.
    """
    if not text:
        raise ValidationError(f"El campo '{text}' no puede estar vacío")

    pattern = r'\S'
    matches = re.findall(pattern, text)

    if len(matches) < 3:
        raise ValidationError(
            f"El campo '{text}' no puede tener menos de 3 caracteres")

    return text


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
    text_pattern = r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\s,]+$'
    text_pattern = r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\s,]+$'
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
            f"El campo '{text}' no es un nombre de usuario válido")
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
            f"El campo '{password}' no es una contraseña válida")
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
    pattern = r'^[a-zA-Z\s.,-áéíóúÁÉÍÓÚ]*\d+[a-zA-Z0-9\s.,-áéíóúÁÉÍÓÚ]*$'

    if not re.match(pattern, address):
        raise ValidationError(
            f"El campo '{address}' no es una dirección válida")
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
            f"El campo '{phone_number}' no es un teléfono válido")
    return phone_number


def validate_form_data(form_data, fields):
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
    expected_parameters = [
        key for key in fields.keys() if "*" in fields[key]
    ]
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
    """q
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


def validate_document_type(document_type):
    if document_type not in DocumentEnum:
        raise ValidationError(
            f"El tipo de documento '{document_type}' no es válido")
    return document_type


def validate_gender(gender):
    if gender not in GenderEnum:
        raise ValidationError(
            f"El genero '{gender}' no es valido")
    return gender


def validate_service_type(input_str):
    try:
        service_type = ServiceTypeEnum(input_str)
        return service_type
    except ValueError:
        raise ValidationError(
            f"El tipo de servicio '{input_str}' no es valido")


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
    value = value.lower()
    if value == "true" or value == "false":
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
    if isinstance(value, str):
        return True
    else:
        raise ValidationError(
            f"El valor '{value}' no es un texto válido")


def validate_keywords(value):
    keyword_pattern = r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\s,]+$'
    if re.match(keyword_pattern, value):
        return True
    else:
        raise ValidationError(
            f"El valor '{value}' no cumple con el formato esperado.")


def validate_service_request_status(value):
    try:
        status = StatusEnum(value)
        return status
    except ValueError:
        raise ValidationError(
            f"El tipo de servicio '{value}' no es valido")


def validate_date(date: str, date_format: str = '%Y-%m-%d'):
    """
    Validates that the given date is a valid date.

    Parameters:
        date (str): The date to be validated.

    Raises:
        ValidationError: If the date is not a valid date.

    Returns:
        str: The validated date.
    """
    try:
        datetime.datetime.strptime(date, date_format)
        return date
    except ValueError:
        raise ValidationError(
            f"El valor '{date}' no es una fecha válida")


def validate_str_len(value):
    """
    Validates that the given value is a string with a
    maximum length of 255 characters.

    Parameters:
        value (str): The value to be validated.
        max_length (int): The maximum length of the string.

    Raises:
        ValidationError: If the value is not a string with a
        maximum length of 255 characters.
    """
    if len(value) >= 255:
        raise ValidationError(
            f"El valor '{value}' debe tener como máximo 255 caracteres")
    return True


def validate_website(website: str):
    """
    Validates that the given website is a valid URL.

    Parameters:
        website (str): The website to be validated.

    Raises:
        ValidationError: If the website is not a valid URL.

    Returns:
        True if the website is a valid URL, False otherwise.
    """

    pattern = r'^(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'

    if re.match(pattern, website):
        return True
    else:
        raise ValidationError(
            f"El sitio web '{website}' no es un URL válido")


def validate_no_institution_name(institution_name: str):
    """
    Validates that the given institution is not already
    registered in the system.

    Parameters:
        institution_name (str): The institution to validate.
        institution_id (int, optional): The ID of the current institution.
            If provided, the validation won't consider this institution
            when checking for uniqueness.

    Raises:
        ValidationError: If the institution is already
        registered.

    Returns:
        str: The validated institution.
    """
    institution = Institution.get_by(field='name', data=institution_name)
    if institution:
        raise ValidationError(
            f"La institución '{institution_name}' ya está registrada")
    return institution_name
