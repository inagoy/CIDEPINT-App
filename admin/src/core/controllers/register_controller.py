from flask import redirect, render_template, flash, url_for
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

    if User.find_user_by_email(email):
        flash("Este email ya esta registrado", "error")
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
    if user.active:
        flash(""" Ya haz completado el registro,
              por favor inicia sesión""", "danger")
        return redirect(url_for("home.home"))
    if user:
        context = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "hashed_email": hashed_email
        }
        return render_template("register/confirmation.html", **context)
    return render_template("error.html")


def second_form(request, hashed_email):

    user = HashedEmail.find_user_by_hash(hashed_email)
    if user:
        form_raw = request.form.to_dict()
        key_mapping = {'inputUsername': 'username',
                       'inputPassword': 'password',
                       'inputDocumentType': 'document_type',
                       'inputDocument': 'document',
                       'inputAddress': 'address',
                       'inputPhoneNumber': 'phone_number',
                       'inputGender': 'gender'}
        form = {key_mapping.get(old_key, old_key):
                value for old_key, value in form_raw.items()}
        form['password'] = form['password'].encode("utf-8")

        errors = validation.second_registration_validation()
        if errors:
            for error in errors:
                flash(error, 'error')
            return redirect(url_for("register.confirmation",
                                    hashed_email=hashed_email))

        userUpdated = User.update(user.id, active=True, **form)
        if userUpdated:
            flash("Se ha completado el registro exitosamente", "success")
        else:
            flash("Error al completar el registro", "danger")
        return redirect(url_for("home.home"))
    return render_template("error.html")
