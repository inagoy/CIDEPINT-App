from datetime import datetime
from src.core.models.user import User
from flask import redirect, render_template, session, request, url_for, flash
from src.core.models.service import Note, ServiceRequest
from src.core.common import serializers as s
from src.web.helpers.services import filter_conditions


def get_service_request_name(service_request):
    return service_request.title


def service_requests():
    title = "Administración de solicitudes de servicio"
    page = request.args.get("page", 1, type=int)
    institution_id = session['current_institution']

    key_mapping = {
        'service-type': 'service_type',
        'request-status': 'status',
        'start-date': 'start_date',
        'end-date': 'end_date',
        'request-email': 'email'
    }

    filters = s.ValidateSerializer.map_keys(request.args, key_mapping,
                                            delete_keys=['page'])
    if filters:
        serializer = s.ServiceRequestFilterSerializer().validate(filters)
        if not serializer['is_valid']:
            for error in serializer['errors'].values():
                flash(error, "danger")
            return redirect(url_for('service_requests.service_requests'))

        filters = filter_conditions(filters)

        service_requests = ServiceRequest.of_institution_filtered_paginated(
            page=page,
            institution_id=institution_id,
            conditions=filters
        )
    else:
        service_requests = (ServiceRequest.
                            get_service_requests_of_institution_paginated(
                                page=page,
                                institution_id=institution_id
                            ))
    return render_template("pages/service_requests.html",
                           title=title,
                           elements=service_requests,
                           get_name=get_service_request_name)


def edit_service_request(service_request_id):
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


def delete_service_request():
    service_request_id = request.form.get('request_id')
    ServiceRequest.delete(service_request_id)
    return redirect(url_for('service_requests.service_requests'))


def notes(service_request_id):
    service_request = ServiceRequest.get_by_id(service_request_id)
    notes = Note.get_notes_of_service_request(service_request_id)
    return render_template(
        "pages/notes.html", elements=notes,
        service_request=service_request,
        user_email=session['user']
    )


def new_note(service_request_id):
    text = request.form.get('message')
    user_id = User.find_user_by_email(session['user']).id
    Note.save(text, user_id, service_request_id)
    return redirect(
        url_for(
            'service_requests.notes',
            service_request_id=service_request_id
        )
    )
