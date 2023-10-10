from flask import render_template


def institutions():
    title = "Administración de instituciones"
    institutions = [
        {
            "name": "la unlp",
        },
        {
            "name": "institución 2",
        },
        {
            "name": "institución 3",
        }
    ]
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
        delete_function=delete_function)
