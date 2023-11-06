"""Validators."""
import re
import datetime
from src.core.models.service import ServiceRequest, StatusEnum
from marshmallow import ValidationError
from src.core.models.institution import Institution
from src.core.models.service import ServiceTypeEnum
from src.core.models.user import DocumentEnum, GenderEnum, User


def validate_not_empty(text):
    """Validate if the given text is not empty."""
    if not text:
        raise ValidationError(f"El campo '{text}' no puede estar vacío")

    pattern = r'\S'
    matches = re.findall(pattern, text)

    if len(matches) < 3:
        raise ValidationError(
            f"El campo '{text}' no puede tener menos de 3 caracteres")

    return text


def validate_email(value):
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email address is not valid.

    Returns:
        str: The validated email address.
    """
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if not re.match(email_pattern, value) is not None:
        raise ValidationError(f"El email '{value}' no es válido")
    return value


def validate_just_text(value):
    """
    Validate if the given text contains only alphabetic characters from multiple languages.

    Args:
        value (str): The text to be validated.
    Returns:
        str: The validated text.
    Raises:
        ValidationError: If the text contains non-alphabetic characters.
    """
    text_pattern = r'^[a-zA-ZáéíóúñÑÁÉÍÓÚüÜ\s,]+$'
    if not re.match(text_pattern, value, re.UNICODE) is not None:
        raise ValidationError(f"El campo '{value}' no puede contener números")
    return value


def validate_just_number(value):
    """
    Validate if the given number is a valid number.

    Parameters:
        number (str): The number to be validated.

    Returns:
        str: The validated number.

    Raises:
        ValidationError: If the number is not a valid number.
    """
    number_pattern = r'^\d+$'
    if not re.match(number_pattern, value):
        raise ValidationError(f"El campo '{value}' no es un número")
    return value


def validate_username(value):
    """
    Validate a username.

    Args:
        text (str): The text to be validated.

    Raises:
        ValidationError: If the text does not match the required pattern.

    Returns:
        str: The validated username.

    """
    text_pattern = r'^[A-Za-z0-9_]+$'
    if not re.match(text_pattern, value):
        raise ValidationError(
            f"El campo'{value}' no es un nombre de usuario válido. " +
            "Puede contener letras sin acentos, números y guiones")
    return value


def validate_password(value):
    """
    Validate a password string.

    Args:
        password (str): The password to be validated.

    Raises:
        ValidationError: If the password does not meet the
        specified requirements.

    Returns:
        str: The validated password.

    """
    pattern = r'^(?=.*[A-Z])(?=.*\d).{6,}$'

    if not re.match(pattern, value):
        raise ValidationError(
            "La contraseña ingresada no es una contraseña válida: " +
            "minimo 6 caracteres, 1 mayúscula, 1 número"
            )
    return value


def validate_address(value):
    """
    Validate an address using a regex pattern.
    The regex pattern checks if there's at least one number and one letter

    Args:
        address (str): The address to be validated.

    Raises:
        ValidationError: If the address is not valid.

    Returns:
        str: The validated address.
    """

    pattern = r'^[a-zA-Z\s.,-áéíóúÁÉÍÓÚ]*\d+[a-zA-Z0-9\s.,-áéíóúÁÉÍÓÚ]*$'

    if not re.match(pattern, value):
        raise ValidationError(
            f"La dirección '{value}' no es válida. " +
            "Debe tener al menos un número.")
    return value


def validate_phone_number(value):
    """
    Validate a phone number.

    Args:
        phone_number (str): The phone number to validate.

    Raises:
        ValidationError: If the phone number is not valid.

    Returns:
        str: The validated phone number.
    """
    value = value.strip()
    phone_number_pattern = r'^\d{9,15}$'

    if not re.match(phone_number_pattern, value):
        raise ValidationError(
            f"El campo'{value}' no es un teléfono válido. " +
            "Debe tener entre 9 y 15 digitos")
    return value


def validate_form_data(form_data, fields):
    """
    Validate the form data against the expected parameters.

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
            "Hay campos faltantes, compruebe que todos los campos " +
            "requeridos estan completos"
        )
    else:
        return form_data


def validate_no_username(value):
    """
    Validate that the given text does not match an existing username.


    Parameters:
        text (str): The text to be validated.
    Returns:
        str: The validated text.
    Raises:
        ValidationError: If the given text matches an existing username.
    """
    if User.find_user_by(field='username', value=value):
        raise ValidationError(
            f"El nombre de usuario '{value}' ya está registrado")
    return value


def validate_no_email(value):
    """
    Validate if the email is not in the User database.

    Parameters:
        email (str): The email to be validated.

    Returns:
        str: The validated email.

    Raises:
        ValidationError: If the email is already registered.

    """
    if User.find_user_by(field='email', value=value):
        raise ValidationError(
            f"El email '{value}' ya está registrado")
    return value


def validate_no_document(value):
    """
    Validates if a document is already registered in the system.

    Parameters:
        document (str): The document to validate.

    Raises:
        ValidationError: If the document is already registered.

    Returns:
        str: The validated document.
    """
    if User.find_user_by(field='document', value=value):
        raise ValidationError(
            f"El numero de documento '{value}' ya está registrado")
    return value


def validate_no_phone_number(value):
    """
    Validate that the given phone number is not already registered.

    Parameters:
        phone_number (str): The phone number to be validated.

    Returns:
        str: The validated phone number.

    Raises:
        ValidationError: If the phone number is already registered.
    """
    if User.find_user_by(field='phone_number', value=value):
        raise ValidationError(
            f"El número de teléfono '{value}' ya está registrado")
    return value


def validate_document_type(value):
    if value not in DocumentEnum:
        raise ValidationError(
            f"El tipo de documento seleccionado '{value}' no es válido")
    return value


def validate_gender(value):
    if value not in GenderEnum:
        raise ValidationError(
            f"El genero seleccionado '{value}' no es valido")
    return value


def validate_service_type(value):
    try:
        service_type = ServiceTypeEnum(value)
        return service_type
    except ValueError:
        raise ValidationError(
            f"El tipo de servicio seleccionado '{value}' no es valido")


def validate_string_as_boolean(value):
    """
    Validate that the given value is a True or False string.

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
            f"El valor '{value}' no es el valor verdadero ni falso")


def validate_string(value):
    """
    Validate that the given value is a string.

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
    """
    Validate a value against a keyword pattern.

    Parameters:
        value (str): The value to be validated.

    Returns:
        bool: True if the value matches the keyword pattern.

    Raises:
        ValidationError: If the value does not match the keyword pattern.
    """
    keyword_pattern = r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\s,]+$'
    if re.match(keyword_pattern, value):
        return True
    else:
        raise ValidationError(
            f"El valor '{value}' no cumple con el formato esperado." +
            " Debe tener palabras separadas por comas")


def validate_service_request_status(value):
    """
    Validate the service request status.

    Parameters:
        value (str): The value to be validated.

    Returns:
        StatusEnum: The validated status.

    Raises:
        ValidationError: If the value is not a valid service request status.
    """
    try:
        status = StatusEnum(value)
        return status
    except ValueError:
        raise ValidationError(
            f"El estado de la solicitud '{value}' no es valido")


def validate_date(date: str, date_format: str = '%Y-%m-%d'):
    """
    Validate that the given date is a valid date.

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
            f"La fecha '{date}' no es una fecha válida")


def validate_str_len(value):
    """
    Validate that the value is a string with a max length of 255 characters.

    Parameters:
        value (str): The value to be validated.
        max_length (int): The maximum length of the string.

    Raises:
        ValidationError: If the value is not a string with a
        maximum length of 255 characters.
    """
    if len(value) >= 255:
        raise ValidationError(
            f"La longitud de '{value}' no puede ser mayor a 255 caracteres")
    return True


def validate_website(website: str):
    """
    Validate that the given website is a valid URL.

    Parameters:
        website (str): The website to be validated.

    Raises:
        ValidationError: If the website is not a valid URL.

    Returns:
        True if the website is a valid URL, False otherwise.
    """
    pattern = r'^(www.)?[-a-zA-Z0-9@:%.+~#=]{1,256}.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%+.~#?&//=]*)$'

    if re.match(pattern, website):
        return True
    else:
        raise ValidationError(
            f"El sitio web '{website}' no es un URL válido")


def validate_no_institution_name(institution_name: str):
    """
    Validate that the institution is not registered in the system.

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


def validate_request_atribute(value):
    if value not in ServiceRequest.__table__.columns.keys():
        raise ValidationError(
            f"El valor '{value}' no es válido")
    return value


def validate_order(value):
    if value not in ['asc', 'desc']:
        raise ValidationError(
            f"El orden '{value}' no es valido")
    return value


def validate_service_request_id_exists(value):
    if not ServiceRequest.get_by_id(value):
        raise ValidationError(
            f"El tipo de servicio '{value}' no existe")
    return value
