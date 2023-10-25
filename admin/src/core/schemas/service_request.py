from marshmallow import validates, validate, fields
from src.core.schemas import BaseSchema, IdSchema, PaginateValidationSchema
from src.core.common import validators as v


class ServiceRequestValidateSchema(PaginateValidationSchema):
    sort = fields.Str(
        missing="id"
    )
    order = fields.Str(
        missing="desc"
    )
    user_id = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    @validates("sort")
    def validate_sort(self, value):
        v.validate_request_atribute(value)

    @validates("order")
    def validate_order(self, value):
        v.validate_order(value)


class ServiceRequestModelSchema(BaseSchema):
    title = fields.String(required=True)
    creation_date = fields.Date(
        format='%Y-%m-%d', required=True, attribute="inserted_at"
        )
    close_date = fields.Date(
        format='%Y-%m-%d', required=True, attribute="closed_at"
        )
    status = fields.Method(
        "status_display", description="Status"
    )

    def status_display(self, obj):
        return obj.status.value

    description = fields.String()


class GetServiceRequestValidateSchema(IdSchema):
    request_id = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )


class PostServiceRequestValidateSchema(BaseSchema):

    service_id = fields.Int(
        required=True,
        validate=validate.Range(min=1),
    )
    title = fields.Str(
        required=True,
        validate=validate.Length(max=255)
    )
    description = fields.Str(
        required=True,
        validate=validate.Length(max=1000)
    )

    @validates("service_id")
    def validate_service_id(self, value):
        v.validate_service_request_id_exists(value)
