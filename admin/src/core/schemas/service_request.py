from marshmallow import validates, validate, fields
from src.core.schemas import BaseSchema
from src.core.schemas import PaginateValidateSchema
from src.core.common import validators as v


class SortedRequestsValidateSchema(PaginateValidateSchema):
    sort = fields.Str(
        missing="id"
    )
    order = fields.Str(
        missing="desc"
    )

    @validates("sort")
    def validate_sort(self, value):
        v.validate_request_atribute(value)

    @validates("order")
    def validate_order(self, value):
        v.validate_order(value)


class RequestModelSchema(BaseSchema):
    id = fields.Int(required=True)
    service = fields.Nested(
        "ServiceModelSchema",
        only=["id", "name"],
    )
    title = fields.String(required=True)
    creation_date = fields.Date(
        format='%Y-%m-%d', required=True, attribute="inserted_at"
    )
    close_date = fields.Date(
        format='%Y-%m-%d', required=False, attribute="closed_at"
        )
    status = fields.Method(
        "status_display", description="Status"
    )

    def status_display(self, obj):
        return obj.status.value

    description = fields.String()


class PostRequestValidateSchema(BaseSchema):

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


class PostNoteValidateSchema(BaseSchema):
    text = fields.Str(
        required=True,
        validate=validate.Length(max=1000)
    )


class NoteModelSchema(BaseSchema):
    text = fields.Str()
    id = fields.Int()


class NotesModelSchema(NoteModelSchema):
    user = fields.Nested(
        "UserModelSchema",
        only=["email", "first_name", "last_name"],
    )
    inserted_at = fields.Date()
