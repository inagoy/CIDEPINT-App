from flask import render_template, request, flash, redirect, url_for
from src.core.models.institution import Institution
from src.web.helpers.institutions import get_name
from src.core.common import serializers as s


def institutions():
    """
    Retrieves a list of institutions and renders the institutions page.

    Returns:
        str: The rendered HTML page for the institutions.
    """
    title = "Administración de instituciones"
    page = request.args.get("page", 1, type=int)
    institutions = Institution.get_paginated(page)

    return render_template(
        "pages/institutions.html",
        title=title,
        elements=institutions,
        get_name=get_name,
    )


def add_institution():
    key_mapping = {
        'inputName': 'name',
        'inputInfo': 'info',
        'inputAddress': 'address',
        'inputLocation': 'location',
        'inputWebsite': 'website',
        'inputKeywords': 'search_keywords',
        'inputDaysHours': 'days_and_hours',
        'inputContact': 'contact_info',
        'inputEnabled': 'enabled'
    }
    form = s.ValidateSerializer.map_keys(request.form, key_mapping)

    serializer = s.InstitutionValidator().validate(form)
    if not serializer["is_valid"]:
        for error in serializer["errors"].values():
            flash(error, "danger")
        return redirect(url_for('super.institutions'))

    form["enabled"] = request.form.get('inputEnabled') is not None

    institution = Institution.save(**form)
    if institution:
        flash('Se ha completado el registro exitosamente', 'success')
    else:
        flash('Error al completar el registro', 'danger')

    return redirect(url_for('super.institutions'))


def edit_institution(institution_id):
    institution = Institution.get_by_id(institution_id)
    if institution:
        key_mapping = {'inputNameEdit': 'name',
                       'inputInfoEdit': 'info',
                       'inputAddressEdit': 'address',
                       'inputLocationEdit': 'location',
                       'inputWebsiteEdit': 'website',
                       'inputKeywordsEdit': 'search_keywords',
                       'inputDaysHoursEdit': 'days_and_hours',
                       'inputContactEdit': 'contact_info',
                       'inputEnabledEdit': 'enabled'
                       }
        form = s.ValidateSerializer.map_keys(request.form, key_mapping)

        serializer = s.InstitutionValidator().validate(form)

        if not serializer["is_valid"]:
            if "name" in serializer["errors"].keys():
                if institution.name == form['name']:
                    serializer["errors"].pop("name", None)
            if serializer["errors"]:
                for error in serializer["errors"].values():
                    flash(error, "danger")
                return redirect(url_for('super.institutions'))

        form["enabled"] = request.form.get('inputEnabledEdit') is not None

        updated = Institution.update(entity_id=institution.id, **form)
        if updated:
            flash("Se ha completado la edición exitosamente", "success")

        else:
            flash("Error al completar la edición", "danger")

    else:
        flash("La institución no existe", "danger")

    return redirect(url_for("super.institutions"))


def delete_institution():
    institution_id = request.form["institution_id"]
    response = Institution.delete(institution_id)
    if response:
        flash("Institución eliminada correctamente", "success")
    else:
        flash("Error al eliminar la institución", "danger")
    return redirect(url_for("super.institutions"))
