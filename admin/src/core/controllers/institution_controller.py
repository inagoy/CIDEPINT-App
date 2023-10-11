from flask import render_template, session
from src.core.models.user import User


def institution(request, institution_id):
    session["current_institution"] = institution_id

    user = User.find_user_by_email(session.get("user"))

    context = {
        "user_institutions": user.get_institution(),
        **session
    }

    return render_template("pages/home.html", **context)
