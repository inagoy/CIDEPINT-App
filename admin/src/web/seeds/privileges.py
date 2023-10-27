"""Privileges seeds."""
from ...core.models.privileges import Role, Permission
from src.core.database import db


roles_data = [
    {"name": "Super Admin"},
    {"name": "Owner"},
    {"name": "Administrator"},
    {"name": "Operator"},
]


permissions_data = [
    {"name": "user_index"},
    {"name": "user_create"},
    {"name": "user_destroy"},
    {"name": "user_update"},
    {"name": "user_show"},

    {"name": "user_institution_index"},
    {"name": "user_institution_create"},
    {"name": "user_institution_destroy"},
    {"name": "user_institution_update"},

    {"name": "institution_index"},
    {"name": "institution_create"},
    {"name": "institution_destroy"},
    {"name": "institution_update"},
    {"name": "institution_show"},
    {"name": "institution_activate"},
    {"name": "institution_deactivate"},

    {"name": "service_index"},
    {"name": "service_create"},
    {"name": "service_destroy"},
    {"name": "service_update"},
    {"name": "service_show"},

    {"name": "request_index"},
    {"name": "request_show"},
    {"name": "request_create"},
    {"name": "request_destroy"},
    {"name": "request_update"},

    {"name": "config_show"},
    {"name": "config_update"},
]


def seed_privileges() -> None:
    """
    Seeds the privileges in the database.

    This function adds roles, permissions, and role-permission relationships
    to the database.
    It uses the data provided in the `roles_data` and
    `permissions_data` variables.
    """
    def add_roles():
        for role_info in roles_data:
            role = Role(**role_info)
            db.session.add(role)

    def add_permissions():
        for permission_info in permissions_data:
            permission = Permission(**permission_info)
            db.session.add(permission)

    def add_role_permission_relationships():
        role_permissions = [
            {"role": "Super Admin",
             "permissions": [
                "user_index", "user_create", "user_destroy", "user_update",
                "user_show", "institution_index", "institution_create",
                "institution_destroy", "institution_update",
                "institution_show", "institution_activate",
                "institution_deactivate", "user_institution_index",
                "user_institution_create", "user_institution_destroy",
                "user_institution_update", "service_index", "service_create",
                "service_destroy", "service_update", "service_show",
                "request_index", "request_show", "request_create",
                "request_destroy", "request_update", "config_show",
                "config_update"
                ]
             },

            {"role": "Owner",
             "permissions": [
                "institution_update", "institution_activate",
                "institution_deactivate", "user_institution_index",
                "user_institution_create", "user_institution_destroy",
                "user_institution_update", "service_index", "service_create",
                "service_destroy", "service_update", "service_show",
                "request_index", "request_show", "request_create",
                "request_destroy", "request_update"
                ]
             },

            {"role": "Administrator",
             "permissions": [
                "service_index", "service_create", "service_destroy",
                "service_update", "service_show", "request_index",
                "request_show", "request_create", "request_destroy",
                "request_update"
                ]
             },

            {"role": "Operator",
             "permissions": [
                "service_index", "service_show", "service_update",
                "service_create", "request_index", "request_show",
                "request_update"
                ]
             },
        ]

        for relationship in role_permissions:
            role = Role.query.filter_by(name=relationship["role"]).first()
            permissions = relationship["permissions"]
            role.has_permissions.extend(
                Permission.query.filter(Permission.name.in_(permissions)).all()
            )

    add_roles()
    add_permissions()
    add_role_permission_relationships()

    db.session.commit()
