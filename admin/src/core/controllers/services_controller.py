"""Services controllers."""
from flask import render_template, session, request, redirect, url_for, flash
from src.core.models.service import Service, ServiceRequest
from src.core.models.user import User
from src.core.models.privileges import Role
from src.web.helpers.users import get_institutions_user
from src.core.common import serializers as s
from src.web.helpers.session import not_enabled_and_not_owner


def get_service_name(service):
    """Return the name of the service."""
    return service.name


def services():
    """
    Render the services page for a given institution.

    Returns
        The rendered template for the services page.
    """
    institution_id = session.get("current_institution")
    not_enabled_and_not_owner(institution_id)
    title = "Administración de servicios"
    page = request.args.get("page", 1, type=int)
    services = Service.get_services_of_institution_paginated(
        page=page, institution_id=institution_id)
    user = User.find_user_by(field='email', value=session.get('user'))

    role_id = User.get_role_in_institution(user_id=user.id,
                                           institution_id=institution_id)

    permissions = Role.evaluate_permissions_model("service", role_id)
    return render_template("pages/services.html",
                           user_institutions=get_institutions_user(),
                           title=title,
                           elements=services,
                           get_name=get_service_name,
                           permissions=permissions)


def delete_service():
    """Delete a service pased in the URL."""
    service_id = request.form.get('service_id')
    Service.delete(service_id)
    return redirect(url_for('services.services'))


def add_service():
    """Add a service to the database passed in a form."""
    key_mapping = {'inputName': 'name',
                   'inputDescription': 'description',
                   'inputKeywords': 'keywords',
                   'inputServiceType': 'service_type',
                   'inputEnabled': 'enabled'
                   }

    data = s.ValidateSerializer.map_keys(request.form, key_mapping)

    data["enabled"] = request.form.get('inputEnabled') is not None
    data['institution_id'] = session.get("current_institution")

    serializer = s.ServiceDataSerializer().validate(data)
    if not serializer["is_valid"]:
        for error in serializer["errors"].values():
            flash(error, "danger")
        return redirect(url_for('services.services'))

    Service.save(**data)
    flash('Se agregó el servicio exitosamente', 'success')
    return redirect(url_for('services.services'))


def edit_service(service_id):
    """Edit service passed in the URL."""
    service = Service.get_by_id(service_id)
    if service:
        key_mapping = {'inputName': 'name',
                       'inputDescription': 'description',
                       'inputKeywords': 'keywords',
                       'inputServiceType2': 'service_type',
                       }
        data = s.ValidateSerializer.map_keys(request.form, key_mapping)
        data['enabled'] = request.form.get('inputEnabled2') is not None
        serializer = s.ServiceDataSerializer().validate(data)
        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, "danger")
            return redirect(url_for('services.services'))

        serviceUpdated = Service.update(entity_id=service.id, **data)
        if serviceUpdated:
            flash("Se ha completado la edición exitosamente", "success")
        else:
            flash("Error al completar la edición", "danger")
    else:
        flash("El servicio no existe", "danger")
    return redirect(url_for('services.services'))


def get_service_request_name(service_request):
    """Return the name of a service request."""
    return service_request.title


def service_requests(service_id):
    """
    Retrieve a paginated list of service requests for a given service.

    Args:
        service_id (int): The ID of the service.

    Returns:
        str: The rendered template for the service requests page.
    """
    title = "Administración de solicitudes"
    page = request.args.get("page", 1, type=int)
    service_requests = (ServiceRequest.
                        get_service_requests_of_service_paginated(
                            page=page,
                            service_id=service_id
                        ))
    user = User.find_user_by(field='email', value=session.get('user'))

    role_id = User.get_role_in_institution(
                        user_id=user.id,
                        institution_id=session.get('current_institution')
                    )

    permissions = Role.evaluate_permissions_model("request", role_id)
    return render_template("pages/service_requests.html",
                           title=title,
                           elements=service_requests,
                           user_institutions=get_institutions_user(),
                           service_id=service_id,
                           get_name=get_service_request_name,
                           permissions=permissions)
