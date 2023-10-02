from flask import render_template


def home():
    """
    Render the home.html template.

    Returns:
        The rendered home.html template.
    """
    return render_template("home.html")
