from flask import render_template


def configuration():
    return render_template(
        "pages/configuration.html")
