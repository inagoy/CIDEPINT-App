"""ServiceRequestController."""

from datetime import datetime
from src.core.models.user import User
from src.core.models.privileges import Role
from flask import redirect, render_template, session, request, url_for, flash
from src.core.models.service import Note, ServiceRequest, StatusEnum
from src.core.common import serializers as s
from src.web.helpers.services import filter_conditions
from src.web.helpers.users import get_institutions_user
from src.web.helpers.session import not_enabled_and_not_owner


def get_service_request_name(service_request):
    """Return the name of a service request."""
    return service_request.title


def service_requests():
    """
    Retrieve and filter service requests based on various parameters.

    Returns:
        render_template: The rendered HTML of the service requests page.
    """
    institution_id = session.get("current_institution")
    not_enabled_and_not_owner(institution_id)
    user = User.find_user_by(field='email', value=session.get('user'))
    title = "Administración de solicitudes de servicio"
    page = request.args.get("page", 1, type=int)
    institution_id = session.get("current_institution")

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
    role_id = User.get_role_in_institution(user_id=user.id,
                                           institution_id=institution_id)
    permissions = Role.evaluate_permissions_model('request', role_id)

    return render_template("pages/service_requests.html",
                           title=title,
                           user_institutions=get_institutions_user(),
                           elements=service_requests,
                           get_name=get_service_request_name,
                           permissions=permissions)


def edit_service_request(service_request_id):
    """
    Edit a service request based on the given service_request_id.

    Args:
        service_request_id (int): The ID of the service request to be edited.

    Returns:
        redirect: Redirects to the service_requests page.
    """
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
            if (data['status'] == StatusEnum.FINALIZADA.value or
                    data['status'] == StatusEnum.CANCELADA.value or
                    data['status'] == StatusEnum.RECHAZADA.value):
                data['closed_at'] = datetime.utcnow()

        updated = ServiceRequest.update(entity_id=service_request.id, **data)
        if updated:
            flash("Se ha completado la edición exitosamente", "success")
        else:
            flash("Error al completar la edición", "danger")
    else:
        flash("El servicio no existe", "danger")
    return redirect(request.referrer)


def delete_service_request():
    """Delete a service request based on the given service_request_id."""
    service_request_id = request.form.get('request_id')
    ServiceRequest.delete(service_request_id)
    return redirect(request.referrer)


def notes(service_request_id):
    """
    Retrieve the notes associated with a service request.

    Parameters:
        service_request_id (int): The ID of the service request
        to retrieve notes for.

    Returns:
        flask.Response: The rendered HTML page containing
        the notes and other related information.
    """
    service_request = ServiceRequest.get_by_id(service_request_id)
    notes = Note.get_notes_of_service_request(service_request_id)
    return render_template(
        "pages/notes.html",
        user_institutions=get_institutions_user(),
        elements=notes,
        service_request=service_request,
        user_email=session.get("user")
    )


def new_note(service_request_id):
    """
    Save a new note for a given service request.

    Parameters:
        service_request_id (int): The ID of the service request.

    Returns:
        redirect: A redirect to the notes page.
    """
    text = request.form.get('message')
    user_id = User.find_user_by(field='email', value=session.get("user")).id
    Note.save(text, user_id, service_request_id)
    return redirect(
        url_for(
            'service_requests.notes',
            service_request_id=service_request_id
        )
    )
