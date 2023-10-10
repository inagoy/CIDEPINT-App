from flask import render_template


def users():
    """
    Generates a function comment for the given function body in a markdown
    code block with the correct language syntax.

    Returns:
        str: The function comment for the given function body.
    """
    title = "Administración de usuarios"
    users = [
        {
            "name": "Julia",
        },
        {
            "name": "Juani",
        },
        {
            "name": "Emi",
        },
        {
            "name": "Iña",
        },
    ]
    add_function = "add_user()"
    edit_function = "editUser()"
    view_function = "viewUser()"
    delete_function = "deleteUser()"
    return render_template(
        "pages/users.html",
        title=title,
        elements=users,
        add_function=add_function,
        edit_function=edit_function,
        view_function=view_function,
        delete_function=delete_function,)
