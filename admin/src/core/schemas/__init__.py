from marshmallow import Schema, validate, fields


class BaseSchema(Schema):
    @classmethod
    def get_instance(cls, many=False):
        return cls(many=many)


class PaginateValidationSchema(BaseSchema):
    page = fields.Int(missing=1, validate=validate.Range(min=1))
    per_page = fields.Int(missing=None, validate=validate.Range(min=1))


class IdSchema(BaseSchema):
    id = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )