from flask import render_template, session, request
from src.core.models.service import Service
from src.web.helpers.users import get_name


def get_service_name(service):
    return service.name


def services():
    
    title = "Administración de servicios"
    page = request.args.get("page", 1, type=int)
    services = Service.get_services_of_institution_paginated(
        page, session['current_institution'])
    add_function = "addUser()"
    edit_function = "editUser(this)"
    view_function = "viewUser(this)"
    delete_function = "deleteUser(this)"
    
    return render_template("pages/services.html",
                           title=title,
                           elements=services,
                           add_function=add_function,
                           edit_function=edit_function,
                           view_function=view_function,
                           delete_function=delete_function,
                           get_name=get_service_name)
