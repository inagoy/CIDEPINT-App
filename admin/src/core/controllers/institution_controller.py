from flask import render_template, session
from src.core.models.user import User
from src.core.models.privileges import Role
from src.web.helpers.users import parse_users_roles, get_name


def institution(request, institution_id):
    session["current_institution"] = institution_id

    user = User.find_user_by_email(session.get("user"))

    context = {
        "user_institutions": user.get_institution(),
        **session
    }

    return render_template("pages/home.html", **context)


def institution_roles():
    current_institution = session["current_institution"]
    
    title = "Administración de roles"
    users = parse_users_roles(User.get_all_users(), current_institution)
    roles = Role.get_all_roles()

    return render_template(
        "pages/institution_roles.html",
        title=title,
        elements=users,
        get_name=get_name,
        roles=roles,
        current_institution=current_institution,
        users_page=False)
