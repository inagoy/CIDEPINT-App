from src.core.schemas import BaseSchema
from marshmallow import fields


class SiteConfigModelSchema(BaseSchema):
    contact_info = fields.Str(attribute='contact_info')
