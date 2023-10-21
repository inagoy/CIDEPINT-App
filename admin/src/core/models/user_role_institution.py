"""User role institution model."""
from src.core.database import db


class UserRoleInstitution(db.Model):
    """UserRoleInstitution."""

    __tablename__ = "user_role_institution"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id",
                                      ondelete="CASCADE"))

    institution_id = db.Column(db.Integer,
                               db.ForeignKey("institutions.id",
                                             ondelete="CASCADE"),
                               nullable=True)

    @classmethod
    def insert(cls, role_id, user_id, institution_id=None):
        """
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
        """
        Retrieve the roles and institutions associated with a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[UserRoleInstitution]: A list of UserRoleInstitution objects
            representing the roles and institutions associated with the user.
        """
        return UserRoleInstitution.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_user_institution_roles(cls,
                                   user_id: int,
                                   institution_id: int):
        """
        Get the user role in a specific institution.

        Args:
            user_id (int): The ID of the user.
            institution_id (int): The ID of the institution.

        Returns:
            UserRoleInstitution: The user role in the specified institution.
        """
        return UserRoleInstitution.query.filter_by(
            user_id=user_id,
            institution_id=institution_id
        ).first()

    @classmethod
    def delete_user_institution_role(cls, user_id: int, institution_id: int,
                                     role_id: int):
        """
        Delete a user's institution role.

        Args:
            user_id (int): The ID of the user.
            institution_id (int): The ID of the institution.
            role_id (int): The ID of the role.

        Returns:
            int: The number of rows deleted.
        """
        response = UserRoleInstitution.query.filter_by(
                    user_id=user_id,
                    institution_id=institution_id,
                    role_id=role_id
                ).delete()
        db.session.commit()
        return response

    @classmethod
    def update_role(cls, user_id: int, role_id: int, institution_id: int):
        """
        Update the role of a user in a specific institution.

        Args:
            user_id (int): The ID of the user whose role is being updated.
            role_id (int): The ID of the new role.
            institution_id (int): The ID of the institution.

        Returns:
            Union[int, bool]: If the role is successfully updated,
                returns the new role ID. If the role is not found,
                inserts a new role and returns True.
        """
        actual_role = cls.get_user_institution_roles(
            user_id=user_id, institution_id=institution_id)
        if actual_role:
            setattr(actual_role, 'role_id', role_id)
            db.session.commit()
            actual_id = role_id
            return actual_id
        else:
            cls.insert(role_id=role_id, user_id=user_id,
                       institution_id=institution_id)
            return True
