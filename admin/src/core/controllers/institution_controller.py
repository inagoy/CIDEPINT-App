from flask import render_template, session, request, redirect, url_for, flash
from src.core.models.user import User
from src.core.models.privileges import Role
from src.core.models.user_role_institution import UserRoleInstitution
from src.core.models.institution import Institution
from src.core.common import serializers as s
from src.web.helpers.users import get_name, get_institutions_user
from src.web.helpers.session import not_enabled_and_not_owner


def institution(institution_id):
    not_enabled_and_not_owner(institution_id)

    session["current_institution"] = institution_id

    context = {
        "user_institutions": get_institutions_user(),
        **session
    }

    return render_template("pages/home.html", **context)


def institution_roles():
    title = "Administración de roles"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_by_institution_paginated(
        page=page, institution_id=session["current_institution"])

    roles = Role.get_all_roles()

    return render_template(
        "pages/institution_roles.html",
        title=title,
        user_institutions=get_institutions_user(),
        elements=users,
        get_name=get_name,
        roles=roles,
        current_institution=session["current_institution"],
        users_page=False)


def update_role():
    form = request.form.to_dict()

    if form["inputRole"]:
        response = UserRoleInstitution.update_role(
            user_id=form["user_id"],
            role_id=form["inputRole"],
            institution_id=session["current_institution"]
        )
        if response:
            flash("Rol actualizado", "success")
        else:
            flash("Error al actualizar el rol", "danger")

    else:
        relationship = UserRoleInstitution.get_user_institution_roles(
            user_id=form["user_id"],
            institution_id=session["current_institution"]
        )
        if not relationship:
            flash("No tiene rol en esta institución", "danger")
        else:
            response = UserRoleInstitution.delete_user_institution_role(
                user_id=form["user_id"],
                institution_id=session["current_institution"],
                role_id=relationship.role_id
            )
            if response:
                flash("Rol eliminado", "success")
            else:
                flash("Error al eliminar el rol", "danger")

    return redirect(url_for("institution.institution_roles"))


def user_search():
    title = "Administración de roles"
    page = request.args.get("page", 1, type=int)
    users = User.get_users_by_email_paginated(
        email=request.form.get('search'), page=page)

    roles = Role.get_all_roles()

    return render_template(
        "pages/institution_roles.html",
        title=title,
        user_institutions=get_institutions_user(),
        elements=users,
        get_name=get_name,
        roles=roles,
        current_institution=session["current_institution"],
        users_page=False)


def edit_institution():
    institution = Institution.get_by_id(session.get("current_institution"))
    if institution:
        context = {
            "institution": institution,
            "user_institutions": get_institutions_user()
        }

        if request.method == "POST":
            key_mapping = {
                'inputName': 'name',
                'inputInfo': 'info',
                'inputAddress': 'address',
                'inputLocation': 'location',
                'inputWebsite': 'website',
                'inputKeywords': 'search_keywords',
                'inputDaysHours': 'days_and_hours',
                'inputContact': 'contact_info',
                'inputEnabled': 'enabled'
            }
            form = s.ValidateSerializer.map_keys(request.form, key_mapping)

            serializer = s.InstitutionValidator().validate(form)

            if not serializer["is_valid"]:
                if "name" in serializer["errors"].keys():
                    if institution.name == form['name']:
                        serializer["errors"].pop("name", None)
                if serializer["errors"]:
                    for error in serializer["errors"].values():
                        flash(error, "danger")
                    return redirect(url_for("institution.institution",
                                    institution_id=institution.id))

            form["enabled"] = request.form.get('inputEnabled') is not None

            updated = Institution.update(entity_id=institution.id, **form)
            if updated:
                flash("Se ha completado la edición exitosamente", "success")

            else:
                flash("Error al completar la edición", "danger")

            return redirect(url_for("institution.institution",
                            institution_id=institution.id))

        return render_template("modules/institutions/edition_by_owner.html",
                               **context)
    else:
        flash("La institución no existe", "danger")
        return redirect(url_for("home.home_user"))
