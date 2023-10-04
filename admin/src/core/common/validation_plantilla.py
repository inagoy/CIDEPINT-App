from os import error
from tokenize import cookie_re
from urllib import response

class ValidationError(Exception):

    def __init__(self, msg="",*args: object) -> None:
        super().__init__(msg,*args)

def validation_string(value:str) -> bool:
    
    if isinstance(value,str):
        return value
    raise ValidationError(f"El campo no es string, es {str(type(value))}")

def validation_contains_number(value:str) -> bool:
    if any([i.isnumeric() for i in value]):
        return value
    raise ValidationError(f"El campo no contiene nÃºmeros, el valor es {str(type(value))}")

class ValidateSerializer():
    fields = {}
    @classmethod
    def validate(self,data:dict):
        errors = {}
        for i,campo in enumerate(data):
            try:
                for validation_function in self.fields.get(campo):
                    validation_function(data.get(campo))
            except TypeError:
                pass
            except ValidationError as e:
                errors[campo]= str(e)
        return {"is_valid": False if errors else True,
                "errors":errors}

class InstitutionSerialzer(ValidateSerializer):
    fields = {
                "nombre":[validation_string, validation_contains_number],
                "informacion":validation_string,
                "direccion":validation_string,
                "localizacion":validation_string,
                "web":validation_string,
                "palabras_clave":validation_string,
                "dias_horarios":validation_string,
                "info_contacto":validation_string,
                "habilitada":validation_string,
    }

class UserSerializer(ValidateSerializer):
    fields = {
        "nombre_usuario":validation_string,
    }

d = {
    "nombre":"asd",
    "informacion":"asd",
    "direccion":"asd",
    "localizacion":True,
    "web":"asd",
    "palabras_clave":"asd",
    "dias_horarios":1,
    "info_contacto":"asd",
    "habilitada":"asd",
    "cualquier_cosa":123
}
