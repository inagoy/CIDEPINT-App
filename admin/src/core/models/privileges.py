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
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)

    has_permissions = db.relationship("Permission",
                                      secondary=role_has_pemission,
                                      back_populates="has_roles")

    @classmethod
    def get_permissions(cls, role_id) -> list:
        role = cls.query.filter_by(id=role_id).first()
        permissions = role.has_permissions
        if not permissions:
            return False
        response = [permission.name for permission in permissions]
        return response

    @classmethod
    def check_permissions(cls, role_id, required_permissions: list) -> bool:
        role_permissions = cls.get_permissions(role_id)
        return all(permission in role_permissions
                   for permission in required_permissions)

    @classmethod
    def evaluate_permissions_model(cls, model) -> list:
        permissions = cls.get_permissions()
        if not permissions:
            return False
        response = dict(map(lambda x: (x.split('_')[1], True),
                            filter(lambda x: model in x, permissions)))
        return dataclass_model[model](**response)

    @classmethod
    def get_role_by_id(cls, id: int) -> object:
        return cls.query.filter_by(id=id).first()


class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)

    has_roles = db.relationship("Role",
                                secondary=role_has_pemission,
                                back_populates="has_permissions")
