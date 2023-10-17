from src.core.common.validators import ValidationError
from src.core.common import validators as v


class ValidateSerializer():
    fields = {}

    @classmethod
    def validate(self, data: dict):
        """
        Validates the given data dictionary.

        Args:
            data (dict): The data dictionary to be validated.

        Returns:
            dict: A dictionary containing the validation result.
                  - is_valid (bool): True if the data is valid,
                  False otherwise.
                  - errors (dict): A dictionary of validation errors, if any.
        """
        errors = {}
        try:
            v.validate_form_data(data, list(self.fields.keys()))
        except ValidationError as e:
            errors["missing_fields"] = str(e)
        for campo in data:
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
        "email": [v.validate_no_email, v.validate_email],
        "first_name": [v.validate_just_text],
        "last_name": [v.validate_just_text],
    }


class SecondRegistrationSerializer(ValidateSerializer):
    fields = {
        "username": [v.validate_no_username, v.validate_username],
        "password": [v.validate_password],
        "address": [v.validate_address],
        "phone_number": [v.validate_no_phone_number,
                         v.validate_phone_number],
        "gender": [v.validate_just_text],
        "document_type": [v.validate_just_text],
        "document": [v.validate_no_document, v.validate_just_number],
    }


class EditUniqueData(ValidateSerializer):
    fields = {
        "email": [v.validate_no_email],
        "username": [v.validate_no_username],
        "phone_number": [v.validate_no_phone_number],
        "document": [v.validate_no_document],
    }


class EditUserSerializer(ValidateSerializer):
    fields = {
        "email": [v.validate_email],
        "first_name": [v.validate_just_text],
        "last_name": [v.validate_just_text],
        "username": [v.validate_username],
        "address": [v.validate_address],
        "phone_number": [v.validate_phone_number],
        "gender": [v.validate_just_text],
        "document_type": [v.validate_just_text],
        "document": [v.validate_just_number],
    }


class SiteConfigValidator(ValidateSerializer):
    fields = {
        "items_per_page": [v.validate_just_number],
        "maintenance_mode": [v.validate_string_as_boolean],
        "maintenance_message": [v.validate_string],
        "contact_info": [v.validate_string],
    }
