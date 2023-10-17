from flask import render_template, session, request, redirect, url_for, flash
from src.core.models.service import Service
from src.core.common import serializers as s


def get_service_name(service):
    return service.name


def services():

    title = "Administración de servicios"
    page = request.args.get("page", 1, type=int)
    services = Service.get_services_of_institution_paginated(
        page, session['current_institution'])
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
    Service.delete_service(service_id)
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

    Service.save(**form)
    flash('Se ha completado el registro exitosamente', 'success')
    return redirect(url_for('services.services'))


def edit_service():
    service = Service.find_service_by_id(request.form.get('service_id'))
    if service:
        form_raw = request.form.to_dict()
        key_mapping = {'inputName': 'name',
                       'inputDescription': 'description',
                       'inputKeywords': 'keywords',
                       'inputServiceType2': 'service_type',
                       'inputEnabled2': 'enabled'
                       }
       
        form = {key_mapping.get(old_key, old_key):
                value for old_key, value in form_raw.items()}
        form['enabled'] = request.form.get('inputEnabled2') is not None

        serializer = s.serviceDataSerializer().validate(form)
        
        

        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, "danger")
            return redirect(url_for('services.services'))

        serviceUpdated = Service.update(**form)
        if serviceUpdated:
            flash("Se ha completado la edición exitosamente", "success")
        else:
            flash("Error al completar la edición", "danger")
    else:
        flash("El servicio no existe", "danger")
    return redirect(url_for('services.services'))
