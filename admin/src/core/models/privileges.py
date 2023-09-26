from src.core.database import db


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


class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)

    has_roles = db.relationship("Role",
                                secondary=role_has_pemission,
                                back_populates="has_permissions")
