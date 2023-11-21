from src.core.schemas import PaginateValidateSchema, BaseSchema
from src.core.common import validators as v
from marshmallow import fields, validates


class ServiceModelSchema(BaseSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    keywords = fields.Str()
    service_type = fields.Method(
        "service_type_display", description="Tipo del servicio."
    )
    laboratory = fields.String(attribute="institution.name")
    enabled = fields.Bool()

    def service_type_display(self, obj):
        return obj.service_type.value

    @classmethod
    def get_instance(cls, many=False):
        return cls(many=many)


class SearchServicesValidateSchema(PaginateValidateSchema):

    q = fields.Str(required=True)
    type = fields.Str(allow_none=True)

    @validates("type")
    def validate_type(self, value):
        v.validate_service_type(value)


class ServicesTypesModelSchema(BaseSchema):
    data = fields.List(fields.String(), required=True)
