"""Site configuration module controllers."""
from flask import render_template, flash, redirect, url_for
from src.core.common import serializers as s
from src.core.models.site_config import SiteConfig


def in_maintenance_mode():
    """Return True if the site is currently in maintenance mode."""
    site_config = SiteConfig.get_config()

    context = {
        "maintenance_message": site_config.maintenance_message,
        "contact_info": site_config.contact_info
    }

    return render_template("modules/site_config/maintenance.html", **context)


def view_config():
    """Get the site configuration."""
    site_config = SiteConfig.get_config()

    context = {
        "items_per_page": site_config.get_items_per_page(),
        "maintenance_mode": site_config.in_maintenance_mode(),
        "maintenance_message": site_config.get_maintenance_message(),
        "contact_info": site_config.get_contact_info()
    }

    return render_template("pages/configuration.html", **context)


def edit_config(request):
    """
    Edit the configuration based on the given request.

    Args:
        request (Request): The request object containing the data
        for the configuration update.

    Returns:
        Response: The response object indicating the success or failure
        of the configuration update.
    """
    site_config = SiteConfig.get_config()
    context = {
        "items_per_page": site_config.get_items_per_page(),
        "maintenance_mode": site_config.in_maintenance_mode(),
        "maintenance_message": site_config.get_maintenance_message(),
        "contact_info": site_config.get_contact_info()
        }

    if request.method == 'POST':
        key_mapping = {'inputItemsPage': 'items_per_page',
                       'selectMode': 'maintenance_mode',
                       'inputMessage': 'maintenance_message',
                       'inputContact': 'contact_info'
                       }

        form = s.ValidateSerializer.map_keys(request.form, key_mapping)
        serializer = s.SiteConfigValidator().validate(form)

        if not serializer["is_valid"]:
            for error in serializer["errors"].values():
                flash(error, 'danger')

        else:
            if form['maintenance_mode'] == "True":
                form['maintenance_mode'] = True
            else:
                form['maintenance_mode'] = False

            site_config.update(**form)

            flash('Configuración actualizada', 'success')
            return redirect(url_for("super.view_config"))

    return render_template("modules/site_config/edit_config.html", **context)
