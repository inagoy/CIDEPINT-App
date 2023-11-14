"""Registration controllers."""
from src.core.bcrypt import bcrypt
from src.core.common import serializers as s
from flask import redirect, render_template, flash, url_for, request
from src.core.models.hashed_email import HashedEmail
from src.core.models.user import User, AuthEnum
from src.core.oauth import oauth
from src.web.helpers.redirection import url_to_login, url_to_home
from src.web.helpers.redirection import get_admin_app_param
from src.web.helpers.register import initial_registration


def first_registration():
    """
    Render the "first_registration.html" template.

    Returns:
        The rendered template.
    """
    admin_app = get_admin_app_param()
    redirect_url = url_to_login(private=admin_app)
    return render_template("modules/register/first_registration.html",
                           admin_app=admin_app, redirect_url=redirect_url)


def first_form(request):
    """
    Process the form submission from the first registration form.

    Args:
        request: The HTTP request object containing the form data.

    Returns:
        A rendered HTML template or a redirect response.
    """
    admin_app = get_admin_app_param()
    redirect_login = url_to_login(private=admin_app)

    key_mapping = {'inputName': 'first_name',
                   'inputSurname': 'last_name',
                   'inputEmail': 'email'}
    form = s.ValidateSerializer.map_keys(request.form, key_mapping)

    serializer = s.FirstRegistrationSerializer().validate(form)
    if not serializer["is_valid"]:
        for error in serializer["errors"].values():
            flash(error, 'danger')
        return render_template("modules/register/first_registration.html",
                               admin_app=admin_app,
                               redirect_url=redirect_login)

    form["auth_method"] = AuthEnum.APP
    data = {
        "user_data": form,
        "route": "register.confirmation",
        "auth_method": AuthEnum.APP.value,
        "admin_app": admin_app
    }
    user = initial_registration(**data)
    if not user:
        flash("Error al completar el registro", "danger")
        return render_template("modules/register/first_registration.html",
                               admin_app=admin_app,
                               redirect_url=redirect_login)

    redirect_home = url_to_home(private=admin_app)
    return render_template("modules/register/first_registration_success.html",
                           redirect_url=redirect_home)


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
    admin_app = get_admin_app_param()
    if user.active:
        flash(""" Ya haz completado el registro,
              por favor inicia sesión""", "danger")
        return redirect(url_to_home(private=admin_app))
    if user:
        context = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "hashed_email": hashed_email,
            "admin_app": admin_app,
            "auth_method": request.args.get("auth_method")
        }
        return render_template("modules/register/confirmation.html", **context)
    return render_template("error.html")


def second_form(request, hashed_email):
    """
    Process the second form submission of a registration process.

    Args:
        request (Request): The request object.
        hashed_email (str): The hashed email.
    """
    user = HashedEmail.find_user_by_hash(hashed_email)
    if user:
        key_mapping = {'inputUsername': 'username',
                       'inputPassword': 'password',
                       'inputDocumentType': 'document_type',
                       'inputDocument': 'document',
                       'inputAddress': 'address',
                       'inputPhoneNumber': 'phone_number',
                       'inputGender': 'gender'}

        form = s.ValidateSerializer.map_keys(request.form, key_mapping)
        serializer = s.SecondRegistrationSerializer().validate(form)
        admin_app = get_admin_app_param()
        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, 'danger')
            return redirect(url_for("register.confirmation",
                            hashed_email=hashed_email,
                            admin_app=admin_app,
                            auth_method=request.args.get("auth_method")))

        form['password'] = bcrypt.generate_password_hash(form['password'])
        userUpdated = User.update(user.id, active=True, **form)
        if userUpdated:
            flash("Se ha completado el registro exitosamente", "success")
        else:
            flash("Error al completar el registro", "danger")

        redirect_login = url_to_login(private=admin_app)
        return redirect(redirect_login)

    return render_template("error.html")


def confirm_password(request, hashed_email):
    """
    Confirm the user's password and update it if necessary.

    Parameters:
        request (Request): The Flask request object containing the form data.
        hashed_email (str): The hashed email of the user.

    Returns:
        Response: A redirect response to the appropriate page.
    """
    user = HashedEmail.find_user_by_hash(hashed_email)
    if user:
        key_mapping = {
            'inputNewPassword': 'new_password',
            'inputConfirmPassword': 'confirm_password'
        }
        form = s.ValidateSerializer.map_keys(request.form, key_mapping)
        serializer = s.ChangePasswordSerializer().validate(form)

        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, 'danger')
            return redirect(url_for("super.user_added_confirmation",
                                    hashed_email=hashed_email))

        if form["new_password"] != form["confirm_password"]:
            flash("Las contraseñas no coinciden", 'danger')
            return redirect(url_for("super.user_added_confirmation",
                                    hashed_email=hashed_email))

        new_password = bcrypt.generate_password_hash(form["new_password"])
        updated = User.update(user.id, active=True, password=new_password)
        if updated:
            flash("Se ha completado el registro exitosamente", "success")
        else:
            flash("Error al completar el registro", "danger")
        return redirect(url_for("home.home"))
    return render_template("error.html")


def google_register():
    admin_app = get_admin_app_param()
    redirect_uri = url_for('register.google_callback', admin_app=admin_app,
                           _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


def google_callback():
    token = oauth.google.authorize_access_token()
    admin_app = get_admin_app_param()

    email = token['userinfo'].get("email")

    if User.find_user_by(field='email', value=email):
        redirect_url = url_to_login(private=admin_app)
        flash("Ya existe un usuario con este correo, por favor inicia sesión",
              "danger")
        return render_template("modules/register/first_registration.html",
                               admin_app=admin_app, redirect_url=redirect_url)

    user_data = {
        "first_name": token['userinfo'].get("given_name"),
        "last_name": token['userinfo'].get("family_name"),
        "email": email,
        "auth_method": AuthEnum.GOOGLE
    }

    params = {
        "user_data": user_data,
        "route": "register.confirmation",
        "auth_method": AuthEnum.GOOGLE.value,
        "admin_app": admin_app
    }

    user = initial_registration(**params)

    if not user:
        flash("Error al completar el registro", "danger")
        return redirect(url_for(request.referrer, _external=True))

    redirect_home = url_to_home(private=admin_app)
    return render_template("modules/register/first_registration_success.html",
                           redirect_url=redirect_home)


def google_second_form(hashed_email, admin_app: bool = False):
    user = HashedEmail.find_user_by_hash(hashed_email)
    if user:
        key_mapping = {'inputUsername': 'username',
                       'inputDocumentType': 'document_type',
                       'inputDocument': 'document',
                       'inputAddress': 'address',
                       'inputPhoneNumber': 'phone_number',
                       'inputGender': 'gender'
                       }

        form = s.ValidateSerializer.map_keys(request.form, key_mapping)
        serializer = s.GoogleRegistrationSerializer().validate(form)
        admin_app = get_admin_app_param()

        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, 'danger')
            return redirect(url_for("register.confirmation",
                                    hashed_email=hashed_email,
                                    admin_app=admin_app,
                                    auth_method=request.args.get("auth_method")
                                    ))

        user = User.update(user.id, active=True, **form)

        if user:
            flash("Se ha completado el registro exitosamente", "success")
        else:
            flash("Error al completar el registro", "danger")
        return redirect(url_to_login(private=admin_app))

    return render_template("error.html")
