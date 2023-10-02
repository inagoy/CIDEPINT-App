from ...core.models.privileges import Role, Permission
from src.core.database import db


roles_data = [
    {"name": "Super Administrador"},
    {"name": "Dueño"},
    {"name": "Administrador"},
    {"name": "Operador"},
]


permissions_data = [
    {"name": "user_index"},
    {"name": "user_new"},
    {"name": "user_destroy"},
    {"name": "user_update"},
    {"name": "user_show"},

    {"name": "institution_index"},
    {"name": "institution_new"},
    {"name": "institution_destroy"},
    {"name": "institution_update"},
    {"name": "institution_show"},
    {"name": "institution_activate"},
    {"name": "institution_deactivate"},

    {"name": "service_index"},
    {"name": "service_new"},
    {"name": "service_destroy"},
    {"name": "service_update"},
    {"name": "service_show"},

    {"name": "request_index"},
    {"name": "request_new"},
    {"name": "request_destroy"},
    {"name": "request_update"},

    {"name": "config_index"},
    {"name": "config_update"},
]


def seed_privileges() -> None:
    def add_roles():
        for role_info in roles_data:
            role = Role(**role_info)
            db.session.add(role)

    def add_permissions():
        for permission_info in permissions_data:
            permission = Permission(**permission_info)
            db.session.add(permission)

    def add_role_permission_relationships():
        role_permission_relationships = [
            {
                "role_name": "Super Administrador",
                "permissions": ["user_index", "user_new",
                                "user_destroy", "user_update", "user_show"],
            },
            {
                "role_name": "Dueño",
                "permissions": ["service_index", "service_new",
                                "service_destroy", "service_update",
                                "service_show"],
            },
            {
                "role_name": "Administrador",
                "permissions": ["service_index", "service_new",
                                "service_destroy", "service_update",
                                "service_show"],
            },
            {
                "role_name": "Operador",
                "permissions": ["service_index", "service_new",
                                "service_update", "service_show"],
            },
        ]

        for relationship in role_permission_relationships:
            role = Role.query.filter_by(name=relationship["role_name"]).first()
            permissions = relationship["permissions"]
            role.has_permissions.extend(
                Permission.query.filter(Permission.name.in_(permissions)).all()
            )

    add_roles()
    add_permissions()
    add_role_permission_relationships()

    db.session.commit()
