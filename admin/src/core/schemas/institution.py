from marshmallow import Schema, fields


class InstitutionSchema(Schema):
    name = fields.Str()
    information = fields.Str(attribute='info')
    address = fields.Str()
    location = fields.Str()
    web = fields.Str(attribute='website')
    days_and_opening_hours = fields.Str(attribute='days_and_hours')
    email = fields.Email(attribute='contact_info')
    enabled = fields.Boolean()


institution_schema = InstitutionSchema()
institutions_schema = InstitutionSchema(many=True)
