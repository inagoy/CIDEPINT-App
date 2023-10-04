from flask import render_template, flash, url_for
from src.core.models.hashed_email import HashedEmail
from src.core.models.user import User
from core.common import register_validation as validation
from src.core import mail
import uuid


def first_registration():
    return render_template("register/first_registration.html")


def first_form(request):
    name = request.form.get('inputName')
    surname = request.form.get('inputSurname')
    email = request.form.get('inputEmail')

    errors = validation.first_registration_validation(name, surname, email)
    if errors:
        for error in errors:
            flash(error, 'error')
        return render_template("register/first_registration.html")

    user = User.save(name, surname, email)
    email_hash = uuid.uuid5(uuid.NAMESPACE_DNS, email)
    HashedEmail.save(email_hash, user.id)

    mail.message(
        "Confirmación de registro",
        recipients=[email],
        template="register/email.html",
        first_name=name,
        last_name=surname,
        confirmation_link=url_for(
            "register.confirmation",
            hashed_email=email_hash,
            _external=True
        )
    )

    return render_template("register/first_registration_success.html")


def confirmation(hashed_email):

    user = HashedEmail.find_user_by_hash(hashed_email)
    context = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }
    return render_template("register/confirmation.html", **context)
