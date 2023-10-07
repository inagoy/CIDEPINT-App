from core.common.validation_plantilla import ValidationError
from core.common import validators as v


class ValidateSerializer():
    fields = {}

    @classmethod
    def validate(self, data: dict):
        errors = {}
        for i, campo in enumerate(data):
            try:
                for validation_function in self.fields.get(campo):
                    validation_function(data.get(campo))
            except TypeError:
                pass
            except ValidationError as e:
                errors[campo] = str(e)
        return {"is_valid": False if errors else True,
                "errors": errors}


class FirstRegistrationSerializer(ValidateSerializer):
    fields = {
                "email": [v.validate_email]
    }
