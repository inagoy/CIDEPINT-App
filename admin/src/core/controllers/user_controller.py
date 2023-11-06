"""User controllers."""
from flask import render_template, flash, redirect, url_for, session
from src.core.models.user import User, GenderEnum, DocumentEnum
from src.core.common import serializers as s
from src.core.bcrypt import bcrypt
from src.web.helpers import users


def view_profile(request):
    """Return the profile page."""
    user = User.find_user_by(field='email', value=session.get('user'))
    context = {
        "user": user,
        "user_institutions": users.get_institutions_user(),
    }
    return render_template("modules/profile/profile.html", **context)


def edit_profile(request):
    """Return the edit profile page."""
    user = User.find_user_by(field='email', value=session.get('user'))
    context = {
            "user": user,
            "genders": GenderEnum,
            "document_types": DocumentEnum,
            "user_institutions": users.get_institutions_user(),
        }

    if request.method == 'POST':
        key_mapping = {'inputFirstName': 'first_name',
                       'inputLastName': 'last_name',
                       'inputUsername': 'username',
                       'inputPhone': 'phone_number',
                       'inputGender': 'gender',
                       'inputDocumentType': 'document_type',
                       'inputDocument': 'document',
                       'inputAddress': 'address'
                       }

        form = s.ValidateSerializer.map_keys(request.form, key_mapping)
        serializer = s.EditProfileSerializer().validate(form)
        unique_data = s.UniqueDataProfile().validate(form)
        error_unique_data = users.unique_data_check(user, form,
                                                    unique_data["errors"])

        errors = []
        if error_unique_data:
            errors.append(error_unique_data)

        for error in serializer["errors"].values():
            errors.append(error)

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template("modules/profile/edit_profile.html",
                                   **context)

        userUpdated = User.update(user.id, **form)
        if userUpdated:
            flash("Perfil actualizado", "success")
            return redirect(url_for("user.view_profile"))

    return render_template("modules/profile/edit_profile.html", **context)


def change_password(request):
    """Change the user's password."""
    user = User.find_user_by(field='email', value=session.get('user'))
    context = {
        "user_institutions": users.get_institutions_user(),
    }
    if request.method == 'POST':
        key_mapping = {'inputCurrentPassword': 'current_password',
                       'inputNewPassword': 'new_password',
                       'inputConfirmPassword': 'confirm_password'
                       }
        form = s.ValidateSerializer.map_keys(request.form, key_mapping)

        if not (bcrypt.check_password_hash(user.password,
                                           form["current_password"])):
            flash("Contraseña actual incorrecta", "danger")
            return render_template("modules/profile/change_password.html",
                                   **context)

        serializer = s.ChangePasswordSerializer().validate(form)

        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, 'danger')
            return redirect(url_for("user.change_password"))

        if form["new_password"] != form["confirm_password"]:
            flash("Las contraseñas no coinciden", 'danger')
            return redirect(url_for("user.change_password"))

        new_password = bcrypt.generate_password_hash(form["new_password"])
        userUpdated = User.update(user.id, password=new_password)
        if not userUpdated:
            flash("Error al actualizar la contraseña", "danger")
            return redirect(url_for("user.change_password"))

        flash("Contraseña actualizada", "success")
        return redirect(url_for("user.view_profile"))

    return render_template("modules/profile/change_password.html", **context)
