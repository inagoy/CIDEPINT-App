from src.core.common.validators import ValidationError
from src.core.common import validators as v


class ValidateSerializer():
    fields = {}

    @classmethod
    def validate(cls, data: dict):
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
            v.validate_form_data(data, cls.fields)
        except ValidationError as e:
            errors["missing_fields"] = str(e)
        for field in data:
            try:
                validations = cls.fields.get(field)
                if validations:
                    validation_functions = [
                        param for param in validations if param != "*"
                    ]
                    for validation_function in validation_functions:
                        validation_function(data.get(field))
            except ValidationError as e:
                errors[field] = str(e)
        return {"is_valid": False if errors else True,
                "errors": errors}

    @classmethod
    def map_keys(cls, form, keys: dict, delete_keys: list = []) -> dict:
        data = form.to_dict()
        return {
            keys.get(old_key, old_key): value
            for old_key, value in data.items()
            if value != "" and old_key not in delete_keys
        }


class FirstRegistrationSerializer(ValidateSerializer):
    fields = {
        "email": [
            v.validate_no_email, v.validate_email, v.validate_not_empty, "*"],
        "first_name": [v.validate_just_text, v.validate_not_empty, "*"],
        "last_name": [v.validate_just_text, v.validate_not_empty, "*"],
    }


class SecondRegistrationSerializer(ValidateSerializer):
    fields = {
        "username": [v.validate_no_username,
                     v.validate_username, v.validate_not_empty, "*"],
        "password": [v.validate_password, "*"],
        "address": [v.validate_address, v.validate_not_empty, "*"],
        "phone_number": [v.validate_no_phone_number,
                         v.validate_phone_number, "*"],
        "gender": [v.validate_just_text, "*"],
        "document_type": [v.validate_just_text, "*"],
        "document": [v.validate_no_document, v.validate_just_number, "*"],
    }


class UniqueDataProfile(ValidateSerializer):
    fields = {
        "username": [v.validate_no_username, "*"],
        "phone_number": [v.validate_no_phone_number, "*"],
        "document": [v.validate_no_document, "*"],
    }


class EditUniqueData(UniqueDataProfile):
    @classmethod
    def validate(cls, data: dict):
        cls.fields["email"] = [v.validate_no_email, "*"]
        return super().validate(data)


class EditProfileSerializer(ValidateSerializer):
    fields = {
        "first_name": [v.validate_just_text, v.validate_not_empty, "*"],
        "last_name": [v.validate_just_text, v.validate_not_empty, "*"],
        "username": [v.validate_username, v.validate_not_empty, "*"],
        "address": [v.validate_address, v.validate_not_empty, "*"],
        "phone_number": [v.validate_phone_number, "*"],
        "gender": [v.validate_just_text, "*"],
        "document_type": [v.validate_just_text, "*"],
        "document": [v.validate_just_number, "*"],
    }


class EditUserSerializer(EditProfileSerializer):
    @classmethod
    def validate(cls, data: dict):
        cls.fields["email"] = [v.validate_email, v.validate_not_empty, "*"]
        return super().validate(data)


class SiteConfigValidator(ValidateSerializer):
    fields = {
        "items_per_page": [v.validate_just_number, "*"],
        "maintenance_mode": [
            v.validate_string_as_boolean, v.validate_not_empty, "*"],
        "maintenance_message": [v.validate_string, v.validate_not_empty],
        "contact_info": [
            v.validate_string, v.validate_str_len, v.validate_not_empty],
    }


class InstitutionValidator(ValidateSerializer):
    fields = {
        "name": [v.validate_just_text, v.validate_str_len,
                 v.validate_no_institution_name, v.validate_not_empty, "*"],
        "info": [v.validate_string, v.validate_not_empty, "*"],
        "address": [
            v.validate_address, v.validate_str_len, v.validate_not_empty],
        "location": [
            v.validate_just_text, v.validate_str_len, v.validate_not_empty],
        "website": [
            v.validate_website, v.validate_str_len, v.validate_not_empty],
        "search_keywords": [
            v.validate_keywords, v.validate_str_len, v.validate_not_empty],
        "days_and_hours": [v.validate_string, v.validate_not_empty],
        "contact_info": [
            v.validate_string, v.validate_str_len, v.validate_not_empty],
        "enabled": [v.validate_string_as_boolean],
    }


class ServiceDataSerializer(ValidateSerializer):
    fields = {
        "name": [v.validate_string, v.validate_not_empty, "*"],
        "description": [v.validate_string, v.validate_not_empty, "*"],
        "keywords": [v.validate_keywords, v.validate_not_empty, "*"],
        "service_type": [v.validate_just_text, "*"],
    }


class ServiceRequestEditDataSerializer(ValidateSerializer):
    fields = {
        "observations": [v.validate_string],
        "status": [v.validate_service_request_status],
    }


class ServiceRequestFilterSerializer(ValidateSerializer):
    fields = {
        "status": [v.validate_service_request_status],
        "service_type": [v.validate_just_text],
        "start_date": [v.validate_date],
        "end_date": [v.validate_date],
        "email": [v.validate_email],
    }


class ChangePasswordSerializer(ValidateSerializer):
    fields = {
        "new_password": [v.validate_password, "*"],
        "confirm_password": [v.validate_password, "*"],
    }
