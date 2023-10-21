"""
from marshmallow import validates, fields
from src.core.schemas import BaseSchema, PaginateValidationSchema
from src.core.models.service import ServiceRequest


class ServiceRequestValidateSchema(PaginateValidationSchema):
    sort = fields.Str(
        required=True,
        validate=validates.OneOf(
            ServiceRequest.__table__.columns.keys()
            ),
        missing="id"
    )
    order = fields.Str(
        required=True,
        validate=validates.OneOf(["asc", "desc"]),
        missing="desc"
    )


class ServiceRequestModelSchema(BaseSchema):
    title = fields.String(required=True)
    creation_date = fields.Date(format='%Y-%m-%d', required=True)
    close_date = fields.Date(format='%Y-%m-%d', required=True)
    status = fields.String(required=True)
    description = fields.String()
 """
