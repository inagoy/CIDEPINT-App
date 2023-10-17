from flask import render_template, session, request, redirect, url_for, flash
from src.core.models.user import User
from src.core.models.privileges import Role
from src.core.models.user_role_institution import UserRoleInstitution
from src.web.helpers.users import get_name


def institution(institution_id):
    session["current_institution"] = institution_id

    user = User.find_user_by_email(session.get("user"))

    context = {
        "user_institutions": user.get_institution(),
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
        elements=users,
        get_name=get_name,
        roles=roles,
        current_institution=session["current_institution"],
        users_page=False)
