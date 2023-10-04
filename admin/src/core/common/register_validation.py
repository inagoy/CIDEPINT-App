import re


def first_registration_validation(name: str, surname: str, email: str) -> list:
    errors = []
    if not name or not surname or not email:
        errors.append("All fields are required.")
    if not is_valid_email(email):
        errors.append("Invalid format for email.")
    if not is_just_text(name):
        errors.append("Invalid format for name.")
    if not is_just_text(surname):
        errors.append("Invalid format for surname.")
    return errors


def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return re.match(email_pattern, email) is not None


def is_just_text(text):
    text_pattern = r'^[^\d_\W]+$'
    return re.match(text_pattern, text, re.UNICODE) is not None
