from src.core.bcrypt import bcrypt
from core.common import serializers as s
from flask import redirect, render_template, flash, url_for
from src.core.models.hashed_email import HashedEmail
from src.core.models.user import User
from src.core import mail
import uuid


def first_registration():
    return render_template("register/first_registration.html")


def first_form(request):
    form_raw = request.form.to_dict()
    key_mapping = {'inputName': 'first_name',
                   'inputSurname': 'last_name',
                   'inputEmail': 'email'}

    form = {key_mapping.get(old_key, old_key):
            value for old_key, value in form_raw.items()}

    serializer = s.FirstRegistrationSerializer().validate(form)
    if not serializer["is_valid"]:
        for error in serializer["errors"].values():
            flash(error, 'danger')
            return render_template("register/first_registration.html")

    user = User.save(**form)
    email_hash = uuid.uuid5(uuid.NAMESPACE_DNS, form["email"])
    HashedEmail.save(email_hash, user.id)

    mail.message(
        "Confirmación de registro",
        recipients=[form["email"]],
        template="register/email.html",
        first_name=form["first_name"],
        last_name=form["last_name"],
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
        serializer = s.SecondRegistrationSerializer().validate(form)
        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, 'danger')
                return redirect(url_for("register.confirmation",
                                hashed_email=hashed_email))

        form['password'] = bcrypt.generate_password_hash(form['password'])
        userUpdated = User.update(user.id, active=True, **form)
        if userUpdated:
            flash("Se ha completado el registro exitosamente", "success")
        else:
            flash("Error al completar el registro", "danger")
        return redirect(url_for("home.home"))
    return render_template("error.html")
