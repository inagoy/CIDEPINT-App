from flask import render_template
from flask import session
from src.core.models.user import User


def home():
    """
    Render the home.html template.

    Returns:
        The rendered home.html template.
    """

    return render_template("pages/home.html")


def home_user():
    user = User.find_user_by_email(session.get("user"))

    context = {
        "user_institutions": user.get_institution(),
        **session
    }

    return render_template("pages/home.html", **context)
