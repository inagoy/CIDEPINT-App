from flask import render_template, request, redirect, url_for, flash
from src.core.models.user import User
from src.core.models.user import UserRoleInstitution
from src.core.models.institution import Institution
from src.core.models.privileges import Role
from src.web.helpers.users import unique_data_check, get_name
from src.core.common import serializers as s
from src.core.models.hashed_email import HashedEmail
from src.core import mail
from src.core.bcrypt import bcrypt
import uuid


def users():
    """
    Generates a function comment for the given function body in a markdown
    code block with the correct language syntax.

    Returns:
        str: The function comment for the given function body.
    """
    title = "Administración de usuarios"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_paginated(page)
    add_function = "addUser()"
    edit_function = "editUser(this)"
    view_function = "viewUser(this)"
    delete_function = "deleteUser(this)"

    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        add_function=add_function,
        edit_function=edit_function,
        view_function=view_function,
        delete_function=delete_function,
        get_name=get_name,
        users_page=True)


def active():
    """
    Generates a function comment for the given function body in a markdown
    code block with the correct language syntax.

    Returns:
        str: The function comment for the given function body.
    """
    title = "Administración de usuarios"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_paginated(page, inactive=False)
    add_function = "addUser()"
    edit_function = "editUser(this)"
    view_function = "viewUser(this)"
    delete_function = "deleteUser(this)"

    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        add_function=add_function,
        edit_function=edit_function,
        view_function=view_function,
        delete_function=delete_function,
        get_name=get_name,
        users_page=True)


def inactive():
    """
    Generates a function comment for the given function body in a markdown
    code block with the correct language syntax.

    Returns:
        str: The function comment for the given function body.
    """
    title = "Administración de usuarios"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_paginated(page, active=False)
    add_function = "addUser()"
    edit_function = "editUser(this)"
    view_function = "viewUser(this)"
    delete_function = "deleteUser(this)"

    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        add_function=add_function,
        edit_function=edit_function,
        view_function=view_function,
        delete_function=delete_function,
        get_name=get_name,
        users_page=True)


def search():
    title = "Administración de usuarios"
    users = User.find_users_by_string(request.form.get('search'))
    add_function = "addUser()"
    edit_function = "editUser(this)"
    view_function = "viewUser(this)"
    delete_function = "deleteUser(this)"

    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        add_function=add_function,
        edit_function=edit_function,
        view_function=view_function,
        delete_function=delete_function,
        get_name=get_name,
        users_page=True)


def delete_user():
    # eliminar usuario
    # mensaje de exito
    user_id = request.form.get('user_id')
    print("holaaaa", user_id)
    User.delete_user(user_id)
    return redirect(url_for('super.users'))


def add_user():
    form_raw = request.form.to_dict()
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

    form = {key_mapping.get(old_key, old_key):
            value for old_key, value in form_raw.items()}
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
    user = User.save(**form)
    email_hash = uuid.uuid5(uuid.NAMESPACE_DNS, form["email"])
    HashedEmail.save(email_hash, user.id)

    flash('Se ha completado el registro exitosamente', 'success')

    mail.message(
        "Confirmación de registro",
        recipients=[form["email"]],
        template="modules/register/email.html",
        first_name=form["first_name"],
        last_name=form["last_name"],
        confirmation_link=url_for(
            "super.confirmation",
            hashed_email=email_hash,
            _external=True
        )
    )
    return redirect(url_for('super.users'))


def edit_user():
    user = User.find_user_by_id(request.form.get('user_id'))
    if user:
        form_raw = request.form.to_dict()
        key_mapping = {'inputName': 'first_name',
                       'inputSurname': 'last_name',
                       'inputEmail': 'email',
                       'inputUsername': 'username',
                       'inputDocumentType': 'document_type',
                       'inputDocument': 'document',
                       'inputAddress': 'address',
                       'inputPhoneNumber': 'phone_number',
                       'inputGender': 'gender'}
        form = {key_mapping.get(old_key, old_key):
                value for old_key, value in form_raw.items()}

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

        userUpdated = User.update(**form)
        if userUpdated:
            flash("Se ha completado la edición exitosamente", "success")
        else:
            flash("Error al completar la edición", "danger")
    else:
        flash("El usuario no existe", "danger")
    return redirect(url_for('super.users'))


def roles(user_id):
    institutions = Institution.get_all_institutions()
    roles = Role.get_all_roles()
    list_raw = UserRoleInstitution.get_roles_institutions_of_user(user_id)
    list = []
    for item in list_raw:
        list.append({
            "id_role": item.role_id,
            "id_institution": item.institution_id,
            "role": Role.get_role_by_id(item.role_id).name,
            "institution": Institution.get_institution_by_id(
                item.institution_id
            ).name
        })
    return render_template("pages/roles.html",
                           user_id=user_id,
                           elements=list,
                           institutions=institutions,
                           roles=roles)


def add_role(user_id):
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
    form_raw = request.form.to_dict()
    UserRoleInstitution.delete_user_institution_role(
        user_id=user_id,
        institution_id=form_raw['institution_id'],
        role_id=form_raw['role_id']
    )
    flash("Rol eliminado", "success")
    return redirect(url_for('super.roles', user_id=user_id))


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
        return render_template("pages/pswrd_change.html", **context)
    return render_template("error.html")
