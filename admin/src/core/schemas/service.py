from src.core.schemas import PaginatedSchema
from src.core.common import validators as v
from marshmallow import Schema, fields, validates


class ServiceSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    keywords = fields.Str()
    service_type = fields.Method(
        "service_type_display", description="Tipo del servicio."
    )
    enabled = fields.Bool()

    def service_type_display(self, obj):
        return obj.service_type.value


services_schema = ServiceSchema(many=True)
service_schema = ServiceSchema()


class SearchServicesSchema(PaginatedSchema):
    q = fields.Str(required=True)
    type = fields.Str(allow_none=True)

    @validates("type")
    def validate_type(self, value):
        v.validate_service_type(value)


search_services_schema = SearchServicesSchema()


class ServicesTypesSchema(Schema):
    data = fields.List(fields.String(), required=True)


services_types_schema = ServicesTypesSchema()
