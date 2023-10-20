from flask import render_template, session, request, redirect, url_for, flash
from src.core.models.service import Service, ServiceRequest
from src.core.common import serializers as s


def get_service_name(service):
    return service.name


def services():

    title = "Administración de servicios"
    page = request.args.get("page", 1, type=int)
    services = Service.get_services_of_institution_paginated(
        page=page, institution_id=session['current_institution'])
    add_function = "addService()"
    edit_function = "editService(this)"
    view_function = "viewService(this)"
    delete_function = "deleteService(this)"
    return render_template("pages/services.html",
                           title=title,
                           elements=services,
                           add_function=add_function,
                           edit_function=edit_function,
                           view_function=view_function,
                           delete_function=delete_function,
                           get_name=get_service_name)


def delete_service():
    service_id = request.form.get('service_id')
    Service.delete(service_id)
    return redirect(url_for('services.services'))


def add_service():
    key_mapping = {'inputName': 'name',
                   'inputDescription': 'description',
                   'inputKeywords': 'keywords',
                   'inputServiceType': 'service_type',
                   'inputEnabled': 'enabled'}

    data = s.ValidateSerializer.map_keys(request.form, key_mapping)

    data['enabled'] = data['enabled'] is not None
    data['institution_id'] = session['current_institution']

    serializer = s.ServiceDataSerializer().validate(data)
    if not serializer["is_valid"]:
        for error in serializer["errors"].values():
            flash(error, "danger")
        return redirect(url_for('services.services'))

    Service.save(**data)
    flash('Se agregó el servicio exitosamente', 'success')
    return redirect(url_for('services.services'))


def edit_service(service_id):
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
    return service_request.title


def a_service_requests(service_id):
    service = Service.get_by_id(service_id)
    title = f"Administración de solicitudes de {service.name}"
    page = request.args.get("page", 1, type=int)
    service_requests = (ServiceRequest.
                        get_service_requests_of_service_paginated(
                            page=page,
                            service_id=service_id
                        ))
    return render_template("pages/a_service_requests.html",
                           title=title,
                           elements=service_requests,
                           get_name=get_service_request_name)
