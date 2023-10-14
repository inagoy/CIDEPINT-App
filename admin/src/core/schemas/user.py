from marshmallow import Schema, fields, validates
from src.core.common import validators as v


class AuthUserSchema(Schema):
    email = fields.Email(description="User email address", required=True)
    password = fields.Str(description="User password", required=True)

    @validates("password")
    def validate_password(self, value):
        v.validate_password(value)

    @validates("email")
    def validate_email(self, value):
        v.validate_email(value)


auth_user_schema = AuthUserSchema()


class UserSchema(Schema):
    user = fields.Str(description="Nombre de usuario.")
    email = fields.Email(description="Correo electrónico.")
    first_name = fields.Str(description="Nombre.")
    last_name = fields.Str(description="Apellido.")
    document_type = fields.Method(
        "document_type_display", description="Tipo de documento."
    )
    document_number = fields.Str(
        description="Número de documento.", attribute="document"
    )
    gender = fields.Method("gender_display", description="Genero.")
    address = fields.Str(description="Dirección.")
    phone_number = fields.Str(description="Teléfono.")

    def gender_display(self, obj):
        return obj.gender.value

    def document_type_display(self, obj):
        return obj.document_type.value


user_schema = UserSchema()
