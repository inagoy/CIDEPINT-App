from datetime import datetime
from flask import redirect, render_template, session, request, url_for, flash
from src.core.models.service import ServiceRequest
from src.core.common import serializers as s


def get_service_request_name(service_request):
    return service_request.title


def service_requests():
    title = "Administración de solicitudes de servicio"
    page = request.args.get("page", 1, type=int)
    service_requests = (ServiceRequest.
                        get_service_requests_of_institution_paginated(
                            page=page,
                            institution_id=session['current_institution']
                        ))
    add_function = "addServiceRequest()"
    edit_function = "changeStatusServiceRequest(this)"
    view_function = "viewServiceRequest(this)"
    delete_function = "deleteServiceRequest(this)"

    return render_template("pages/service_requests.html",
                           title=title,
                           elements=service_requests,
                           add_function=add_function,
                           edit_function=edit_function,
                           view_function=view_function,
                           delete_function=delete_function,
                           get_name=get_service_request_name)


def edit_service_request(request, service_request_id):
    service_request = ServiceRequest.get_by_id(service_request_id)
    if service_request:
        key_mapping = {'inputObservations': 'observations',
                       'inputStatus': 'status',
                       }
        data = s.ValidateSerializer.map_keys(request.form, key_mapping)
        serializer = s.ServiceRequestEditDataSerializer().validate(data)
        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, "danger")
            return redirect(url_for('service_requests.service_requests'))

        if service_request.status != data['status']:
            data['status_at'] = datetime.utcnow()

        updated = ServiceRequest.update(entity_id=service_request.id, **data)
        if updated:
            flash("Se ha completado la edición exitosamente", "success")
        else:
            flash("Error al completar la edición", "danger")
    else:
        flash("El servicio no existe", "danger")
    return redirect(url_for('service_requests.service_requests'))


def delete_service_request(request):
    service_request_id = request.form.get('request_id')
    ServiceRequest.delete(service_request_id)
    return redirect(url_for('service_requests.service_requests'))
