from marshmallow import Schema, validate, fields


class PaginatedSchema(Schema):
    page = fields.Int(missing=1, validate=validate.Range(min=1))
    per_page = fields.Int(missing=None, validate=validate.Range(min=1))


paginated_schema = PaginatedSchema()


class IdSchema(Schema):
    id = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )


id_schema = IdSchema()
