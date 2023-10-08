import re
from src.core.models.user import User


class ValidationError(Exception):

    def __init__(self, msg="", *args: object) -> None:
        super().__init__(msg, *args)


def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if not re.match(email_pattern, email) is not None:
        raise ValidationError(f"El campo '{email}' no es un email válido")
    return email


def validate_just_text(text):
    text_pattern = r'^[^\d_\W]+$'
    if not re.match(text_pattern, text, re.UNICODE) is not None:
        raise ValidationError(f"El campo '{text}' no es un texto")
    return text


def validate_just_number(number):
    number_pattern = r'^\d+$'
    if not re.match(number_pattern, number):
        raise ValidationError(f"El campo '{number}' no es un número")
    return number


def validate_username(text):
    text_pattern = r'^[A-Za-z0-9_]+$'
    if not re.match(text_pattern, text):
        raise ValidationError(
            f"El campo'{text}' no es un nombre de usuario válido")
    return text


def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d).{6,}$'

    if not re.match(pattern, password):
        raise ValidationError(
            f"El campo'{password}' no es una contraseña válida")
    return password


def validate_address(address):
    # Define a regex pattern to check if there's at least one number
    pattern = r'^[a-zA-Z\s.,-]*\d+[a-zA-Z0-9\s.,-]*$'

    if not re.match(pattern, address):
        raise ValidationError(
            f"El campo'{address}' no es una dirección válida")
    return address


def validate_phone_number(phone_number):
    phone_number = phone_number.strip()
    phone_number_pattern = r'^\d{9,15}$'

    if not re.match(phone_number_pattern, phone_number):
        raise ValidationError(
            f"El campo'{phone_number}' no es un teléfono válido")
    return phone_number


def validate_form_data(form_data, expected_parameters):
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
    if User.find_user_by_username(text):
        raise ValidationError(
            f"El nombre de usuario '{text}' ya está registrado")
    return text


def validate_no_email(email):
    if User.find_user_by_email(email):
        raise ValidationError(
            f"El email '{email}' ya está registrado")
    return email


def validate_no_document(document):
    if User.find_user_by_document(document):
        raise ValidationError(
            f"El documento '{document}' ya está registrado")
    return document


def validate_no_phone_number(phone_number):
    if User.find_user_by_phone_number(phone_number):
        raise ValidationError(
            f"El número de teléfono '{phone_number}' ya está registrado")
    return phone_number
