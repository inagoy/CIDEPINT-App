from core.models.privileges import Role, Permission
from src.core.database import db


roles_data = [
    {"name": "Super Administrador"},
    {"name": "Dueño"},
    {"name": "Administrador"},
    {"name": "Operador"},
]


permissions_data = [
    {"name": "index"},
    {"name": "new"},
    {"name": "destroy"},
    {"name": "update"},
    {"name": "show"},
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
