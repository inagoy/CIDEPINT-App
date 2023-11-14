"""User configuration module controllers."""
from flask import render_template, request, redirect, url_for, flash
from src.core.models.user import User, AuthEnum
from src.core.models.user import UserRoleInstitution
from src.core.models.institution import Institution
from src.core.models.privileges import Role
from src.core.models.hashed_email import HashedEmail
from src.web.helpers.users import unique_data_check, get_name
from src.web.helpers.register import initial_registration
from src.core.common import serializers as s
from src.core.bcrypt import bcrypt


def users():
    """
    Retrieve a paginated list of users and render the 'users.html' template.

    Returns:
        rendered template: 'pages/users.html'
    """
    title = "Administración de usuarios"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_paginated(page)

    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        get_name=get_name,
        users_page=True)


def active():
    """
    Render the users.html page with a paginated list of active users.

    Returns:
        The rendered template of the users.html page,
        with the following variables:
            - title: A string representing the title of the page
            - elements: A list of active user objects
            - add_function: A string for the function to add a user
            - edit_function: A string for the function to edit a user
            - view_function: A string for the function to  view a user
            - delete_function: A string for the function to delete a user
            - get_name: A function that returns the name of a user
            - users_page: A boolean indicating that this is the users page
    """
    title = "Administración de usuarios"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_paginated(page, inactive=False)

    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        get_name=get_name,
        users_page=True)


def inactive():
    """
    Render the users.html page with a paginated list of inactive users.

    Returns:
        The rendered template of the users.html page,
        with the following variables:
            - title: A string representing the title of the page
            - elements: A list of active user objects
            - add_function: A string for the function to add a user
            - edit_function: A string for the function to edit a user
            - view_function: A string for the function to  view a user
            - delete_function: A string for the function to delete a user
            - get_name: A function that returns the name of a user
            - users_page: A boolean indicating that this is the users page
    """
    title = "Administración de usuarios"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_paginated(page, active=False)

    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        get_name=get_name,
        users_page=True)


def search():
    """Return the users page for a given search term."""
    title = "Administración de usuarios"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_by_email_paginated(
        email=request.form.get('search'), page=page)

    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        get_name=get_name,
        users_page=True)


def delete_user():
    """
    Delete a user from the system.

    This function receives a user ID from the request form
    and uses it to delete the corresponding user from the database.
    If the deletion is successful, a success message is flashed,
    otherwise an error message is flashed.

    Returns:
        redirect: A redirect to the 'super.users' route.
    """
    user_id = request.form.get('user_id')
    response = User.delete(user_id)
    if response:
        flash("Usuario eliminado correctamente", "success")
    else:
        flash("Error al eliminar el usuario", "danger")
    return redirect(url_for('super.users'))


def add_user():
    """Add a new user to the database."""
    key_mapping = {'inputName': 'first_name',
                   'inputSurname': 'last_name',
                   'inputEmail': 'email',
                   'inputUsername': 'username',
                   'inputPassword': 'password',
                   'inputDocumentType': 'document_type',
                   'inputDocument': 'document',
                   'inputAddress': 'address',
                   'inputPhoneNumber': 'phone_number',
                   'inputGender': 'gender'}

    form = s.ValidateSerializer.map_keys(request.form, key_mapping)
    serializer = s.FirstRegistrationSerializer().validate(form)
    serializer2 = s.SecondRegistrationSerializer().validate(form)

    errors = []
    if not serializer["is_valid"]:
        errors.extend(serializer["errors"].values())

    if not serializer2["is_valid"]:
        errors.extend(serializer2["errors"].values())

    if errors:
        for error in errors:
            flash(error, 'danger')
        return redirect(url_for('super.users'))

    form['password'] = bcrypt.generate_password_hash(form['password'])
    form['auth_method'] = AuthEnum.APP

    data = {
        "user_data": form,
        "route": "super.user_added_confirmation",
        "auth_method": AuthEnum.APP.value,
    }
    user = initial_registration(**data)

    if not user:
        flash('Error al registrar el usuario', 'danger')
    else:
        flash('Se ha completado el registro exitosamente', 'success')

    return redirect(url_for('super.users'))


def edit_user(user_id):
    """
    Edit a user with the given user_id.

    Parameters:
        user_id (int): The ID of the user to be edited.

    Returns:
        None
    """
    user = User.get_by_id(user_id)
    if user:
        key_mapping = {'inputName': 'first_name',
                       'inputSurname': 'last_name',
                       'inputEmail': 'email',
                       'inputUsername': 'username',
                       'inputDocumentType': 'document_type',
                       'inputDocument': 'document',
                       'inputAddress': 'address',
                       'inputPhoneNumber': 'phone_number',
                       'inputGender': 'gender',
                       }
        form = s.ValidateSerializer.map_keys(request.form, key_mapping)

        form['active'] = request.form.get('inputActive') is not None

        serializer = s.EditUserSerializer().validate(form)

        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, "danger")
            return redirect(url_for('super.users'))

        data_unique_serializer = s.EditUniqueData().validate(form)
        if not data_unique_serializer["is_valid"]:
            error = unique_data_check(user, form,
                                      data_unique_serializer["errors"])
            if (error):
                flash(error, "danger")
                return redirect(url_for('super.users'))

        userUpdated = User.update(entity_id=user.id, **form)
        if userUpdated:
            flash("Se ha completado la edición exitosamente", "success")
        else:
            flash("Error al completar la edición", "danger")
    else:
        flash("El usuario no existe", "danger")
    return redirect(url_for('super.users'))


def roles(user_id):
    """
    Retrieve the roles and institutions associated with a given user ID.

    Parameters:
        user_id (int): The ID of the user.

    Returns:
        str: The rendered template for displaying the roles and institutions.
    """
    institutions = Institution.get_all()
    roles = Role.get_all_roles()
    list_raw = UserRoleInstitution.get_roles_institutions_of_user(user_id)
    list = []
    for item in list_raw:
        list.append({
            "id_role": item.role_id,
            "id_institution": item.institution_id,
            "role": Role.get_role_by_id(item.role_id).name,
            "institution": Institution.get_by_id(
                item.institution_id
            ).name
        })
    return render_template("pages/roles.html",
                           user_id=user_id,
                           elements=list,
                           institutions=institutions,
                           roles=roles)


def add_role(user_id):
    """
    Add a role to a user.

    Parameters:
        user_id (int): The ID of the user to add the role to.
    """
    form_raw = request.form.to_dict()

    same_institution = UserRoleInstitution.get_user_institution_roles(
        user_id=user_id,
        institution_id=form_raw['inputInstitution']
    )
    if same_institution:
        flash("Este usuario ya tiene un rol en esta institución", "danger")
        return redirect(url_for('super.roles', user_id=user_id))

    UserRoleInstitution.insert(user_id=user_id,
                               role_id=form_raw['inputRole'],
                               institution_id=form_raw['inputInstitution'])
    flash("Rol agregado", "success")
    return redirect(url_for('super.roles', user_id=user_id))


def delete_role(user_id):
    """
    Delete a role for a user.

    Parameters:
        user_id (int): The ID of the user.
    """
    form_raw = request.form.to_dict()
    UserRoleInstitution.delete_user_institution_role(
        user_id=user_id,
        institution_id=form_raw['institution_id'],
        role_id=form_raw['role_id']
    )
    flash("Rol eliminado", "success")
    return redirect(url_for('super.roles', user_id=user_id))


def user_added_confirmation(hashed_email):
    """
    Handle user added confirmation.

    Parameters:
        hashed_email (str): The hashed email of the user.

    Returns:
        If the user is active,
            it flashes a message and redirects to the home page.
        If the user is found,
            it renders the password change page with the user's information.
        Otherwise, it renders the error page.
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
        return render_template("pages/pswrd_change.html", **context)
    return render_template("error.html")
