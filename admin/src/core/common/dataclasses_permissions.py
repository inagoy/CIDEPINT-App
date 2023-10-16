from dataclasses import dataclass


@dataclass
class Permissions:
    index: bool = False
    create: bool = False
    update: bool = False
    delete: bool = False
    show: bool = False


@dataclass
class InstitutionPermissions(Permissions):
    activate: bool = False
    deactivate: bool = False


dataclass_model = {
    "user": Permissions,
    "institution": InstitutionPermissions,
    "service": Permissions,
    "request": Permissions,
    "user_in_institution": Permissions,
}