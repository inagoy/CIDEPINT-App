"""Privileges model."""
from src.core.database import db
from src.core.common.dataclasses_permissions import dataclass_model

role_has_pemission = db.Table(
    "role_has_pemission",
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"),
              primary_key=True),
    db.Column("permission_id", db.Integer, db.ForeignKey("permissions.id"),
              primary_key=True),
)


class Role(db.Model):
    """Role."""

    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)

    has_permissions = db.relationship("Permission",
                                      secondary=role_has_pemission,
                                      back_populates="has_roles")

    @classmethod
    def get_permissions(cls, role_id) -> list:
        """
        Retrieve the permissions associated with a given role.

        Args:
            role_id (int): The ID of the role to retrieve permissions for.

        Returns:
            list: A list of permission names associated with the role.
        """
        role = cls.query.filter_by(id=role_id).first()
        permissions = role.has_permissions
        if not permissions:
            return False
        response = [permission.name for permission in permissions]
        return response

    @classmethod
    def check_permissions(cls, role_id, required_permissions: list) -> bool:
        """
        Check if a role has all the required permissions.

        Args:
            role_id (int): The ID of the role to check permissions for.
            required_permissions (list): A list of permissions that the
                role should have.

        Returns:
            bool: True if the role has all the required permissions,
                False otherwise.
        """
        role_permissions = cls.get_permissions(role_id)
        return all(permission in role_permissions
                   for permission in required_permissions)

    @classmethod
    def evaluate_permissions_model(cls, model, role_id) -> list:
        """
        Evaluate the permissions model.

        Args:
            model (str): The model to evaluate the permissions for.

        Returns:
            list: A list of permissions for the given model.
        """
        permissions = cls.get_permissions(role_id)
        if not permissions:
            return False
        response = dict(map(lambda x: (x.split('_')[1], True),
                            filter(lambda x: model in x, permissions)))
        return dataclass_model[model](**response)

    @classmethod
    def get_role_by_id(cls, id: int) -> object:
        """Return the role with the given ID."""
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_roles(cls) -> object:
        """Return all roles."""
        return cls.query.filter(Role.name != "Super Admin").all()


class Permission(db.Model):
    """Permission."""

    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)

    has_roles = db.relationship("Role",
                                secondary=role_has_pemission,
                                back_populates="has_permissions")
