from src.core.bcrypt import bcrypt
from src.core.models.user import User


def check_user(email, password):
    """
    Check if a user exists with the given email and password.
     :param email: The email of the user.
     :type email: str
     :param password: The password of the user.
     :type password: str
     :return: The user object if the email and password match, None otherwise.
     :rtype: User or None
     """

    user = User.find_user_by(field='email', value=email)

    if user and bcrypt.check_password_hash(user.password,
                                           password.encode("utf-8")):
        return user
    else:
        return None
