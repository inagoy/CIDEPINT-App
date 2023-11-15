from src.core.schemas import BaseSchema
from marshmallow import fields


class InstitutionModelSchema(BaseSchema):
    name = fields.Str()
    information = fields.Str(attribute='info')
    address = fields.Str()
    location = fields.Str()
    web = fields.Str(attribute='website')
    coordinates = fields.Str(attribute='coordinates')
    days_and_opening_hours = fields.Str(attribute='days_and_hours')
    email = fields.Email(attribute='contact_info')
    enabled = fields.Boolean()
