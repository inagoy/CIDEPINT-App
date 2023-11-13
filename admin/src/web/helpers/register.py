from src.core import mail
from src.core.models.hashed_email import HashedEmail
from src.core.models.user import User
from flask import url_for
import uuid


def initial_registration(user_data: dict,
                         route: str,
                         auth_method: str,
                         admin_app: bool = True):

    user = User.save(**user_data)
    email_hash = uuid.uuid5(uuid.NAMESPACE_DNS, user_data["email"])
    HashedEmail.save(email_hash, user.id)

    mail_data = {
        "subject": "Confirmación de registro",
        "recipients": [user_data["email"]],
        "template": "modules/register/email.html",
        "first_name": user_data["first_name"],
        "last_name": user_data["last_name"],
        "confirmation_link": url_for(
            route,
            hashed_email=email_hash,
            admin_app=admin_app,
            auth_method=auth_method,
            _external=True
        )
    }

    mail.message(**mail_data)
    return user
