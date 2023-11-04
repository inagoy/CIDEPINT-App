"""Home controllers."""
from flask import render_template
from flask import session
from src.web.helpers.users import get_institutions_user


def home():
    """
    Render the home.html template.

    Returns:
        The rendered home.html template.
    """
    return render_template("pages/home.html")


def home_user():
    """
    Render the home page for the logged-in user.

    Returns:
        The rendered home page HTML.
    """

    context = {
        "user_institutions": get_institutions_user(),
        **session
    }

    return render_template("pages/home.html", **context)
