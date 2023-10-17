from flask import render_template, request
from src.core.models.institution import Institution


def institutions():
    """
    Retrieves a list of institutions and renders the institutions page.

    Returns:
        str: The rendered HTML page for the institutions.
    """
    title = "Administración de instituciones"
    page = request.args.get("page", 1, type=int)
    institutions = Institution.get_paginated(page)

    def get_name(institution):
        return institution.name

    add_function = "add_institution()"
    edit_function = "editInstitution()"
    view_function = "viewInstitution()"
    delete_function = "deleteInstitution()"
    return render_template(
        "pages/institutions.html",
        title=title,
        elements=institutions,
        add_function=add_function,
        view_function=view_function,
        edit_function=edit_function,
        delete_function=delete_function,
        get_name=get_name)
