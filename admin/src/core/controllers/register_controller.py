from src.core.bcrypt import bcrypt
from src.core.common import serializers as s
from flask import redirect, render_template, flash, url_for
from src.core.models.hashed_email import HashedEmail
from src.core.models.user import User
from src.core import mail
import uuid


def first_registration():
    """
    Renders the "first_registration.html" template.

    :return: The rendered template.
    """
    return render_template("modules/register/first_registration.html")


def first_form(request):
    """
    Processes the form submission from the first registration form.

    Args:
        request: The HTTP request object containing the form data.

    Returns:
        A rendered HTML template or a redirect response.

    Raises:
        None.
    """
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
            return render_template("modules/register/first_registration.html")

    user = User.save(**form)
    email_hash = uuid.uuid5(uuid.NAMESPACE_DNS, form["email"])
    HashedEmail.save(email_hash, user.id)

    mail.message(
        "Confirmación de registro",
        recipients=[form["email"]],
        template="modules/register/email.html",
        first_name=form["first_name"],
        last_name=form["last_name"],
        confirmation_link=url_for(
            "register.confirmation",
            hashed_email=email_hash,
            _external=True
        )
    )
    return render_template("modules/register/first_registration_success.html")


def confirmation(hashed_email):
    """
    Find a user by their hashed email and check if they are active.

    If the user is active, display a Flash message instructing them to
    log in and redirect them to the home page.

    If the user is not active, render the confirmation template with the
    user's first name, last name, email, and hashed email as context
    variables. If no user is found, render the error template.

    Parameters:
    - hashed_email (str): The hashed email of the user to be found.

    Returns:
    - (str): If the user is active, a redirect to the home page. Otherwise,
    the rendered confirmation template or the error template.
    """
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
    """
    The `second_form` function processes the second form submission
    of a registration process.

    :param request: The Flask request object containing the form data.
    :type request: flask.Request
    :param hashed_email: The hashed email of the user.
    :type hashed_email: str
    :return: None
    :rtype: None
    """

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


def confirm_password(request, hashed_email):
    user = HashedEmail.find_user_by_hash(hashed_email)
    if user:
        form = request.form.to_dict()
        form['inputPassword'] = bcrypt.generate_password_hash(
            form['inputPassword'])
        userUpdated = User.update(user.id, active=True, **form)
        if userUpdated:
            flash("Se ha completado el registro exitosamente", "success")
        else:
            flash("Error al completar el registro", "danger")
        return redirect(url_for("home.home"))
    return render_template("error.html")
