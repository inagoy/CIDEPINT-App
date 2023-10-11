from marshmallow import Schema, fields


class UserSchema(Schema):

    id = fields.Int(dump_only=True)
    email = fields.Email()
    password = fields.Str()
    first_name = fields.Str()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
