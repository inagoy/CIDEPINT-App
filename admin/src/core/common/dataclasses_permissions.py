from dataclasses import dataclass


@dataclass
class Permissions:
    index: bool = False
    create: bool = False
    update: bool = False
    destroy: bool = False
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
    "user_institution": Permissions,
}
