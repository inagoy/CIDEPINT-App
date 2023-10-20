from flask import render_template, session, request, redirect, url_for, flash
from src.core.models.service import Service
from src.web.helpers.users import get_institutions_user
from src.core.common import serializers as s
from src.web.helpers.session import not_enabled_and_not_owner


def get_service_name(service):
    return service.name


def services():
    institution_id = session['current_institution']
    not_enabled_and_not_owner(institution_id)
    title = "Administración de servicios"
    page = request.args.get("page", 1, type=int)
    services = Service.get_services_of_institution_paginated(
        page=page, institution_id=institution_id)
    add_function = "addService()"
    edit_function = "editService(this)"
    view_function = "viewService(this)"
    delete_function = "deleteService(this)"

    return render_template("pages/services.html",
                           user_institutions=get_institutions_user(),
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
    form_raw = request.form.to_dict()
    key_mapping = {'inputName': 'name',
                   'inputDescription': 'description',
                   'inputKeywords': 'keywords',
                   'inputServiceType': 'service_type',
                   'inputEnabled': 'enabled'}

    form = {key_mapping.get(old_key, old_key):
            value for old_key, value in form_raw.items()}

    form['enabled'] = form['enabled'] is not None
    form['institution_id'] = session['current_institution']

    serializer = s.ServiceDataSerializer().validate(form)
    if not serializer["is_valid"]:
        for error in serializer["errors"].values():
            flash(error, "danger")
        return redirect(url_for('services.services'))

    Service.save(**form)
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
