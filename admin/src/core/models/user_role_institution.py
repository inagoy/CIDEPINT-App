from src.core.database import db


class UserRoleInstitution(db.Model):
    __tablename__ = "user_role_institution"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id",
                                                  ondelete="CASCADE"))
    institution_id = db.Column(db.Integer, db.ForeignKey("institutions.id"),
                               nullable=True)

    @classmethod
    def insert(cls, role_id, user_id, institution_id=None):
        """insert

        Insert a new user_role_institution record into the database.

        Args:
            role_id (int): The ID of the role.
            user_id (int): The ID of the user.
            institution_id (int): The ID of the institution (nullable).

        Example:
            UserRoleInstitution.insert(role_id=1, user_id=2, institution_id=3)
        """
        user_role_institution = cls(role_id=role_id, user_id=user_id,
                                    institution_id=institution_id)
        db.session.add(user_role_institution)
        db.session.commit()

    @classmethod
    def get_roles_institutions_of_user(cls, user_id: int):
        return UserRoleInstitution.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_user_institution_roles(cls,
                                   user_id: int,
                                   institution_id: int):
        return UserRoleInstitution.query.filter_by(
            user_id=user_id,
            institution_id=institution_id
        ).first()

    @classmethod
    def delete_user_institution_role(cls, user_id: int, institution_id: int,
                                     role_id: int):
        UserRoleInstitution.query.filter_by(
            user_id=user_id,
            institution_id=institution_id,
            role_id=role_id
        ).delete()
        db.session.commit()
        return
