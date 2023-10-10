from flask import render_template


def configuration():
    """
    Returns the rendered template for the configuration page.
    """
    return render_template(
        "pages/configuration.html")
