from marshmallow import Schema, validate, fields


class BaseSchema(Schema):
    @classmethod
    def get_instance(cls, many=False):
        return cls(many=many)


class PaginateValidateSchema(BaseSchema):
    page = fields.Int(missing=1, validate=validate.Range(min=1))
    per_page = fields.Int(missing=None, validate=validate.Range(min=1))
