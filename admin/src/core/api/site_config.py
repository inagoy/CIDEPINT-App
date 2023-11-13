from flask import Blueprint
from src.web.helpers.api import response_error
from src.core.models.site_config import SiteConfig
from src.core.schemas.site_config import SiteConfigModelSchema
from flask_cors import cross_origin

api_site_config = Blueprint('api_site_config', __name__, url_prefix='/api')


@api_site_config.route("/contact-info", methods=["GET"])
@cross_origin()
def get_contact_info():
    """Get the contact information from the database."""
    model_schema = SiteConfigModelSchema.get_instance()
    contact_info = SiteConfig.get_config()
    if not contact_info:
        return response_error()
    data = model_schema.dump(contact_info)
    return data, 200
