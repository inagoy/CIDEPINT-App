"""User model."""
from datetime import datetime
from src.core.database import db
from enum import Enum as EnumBase
from src.core.models.user_role_institution import UserRoleInstitution
from src.core.models.institution import Institution
from src.core.models.base_model import BaseModel
from flask import session
from sqlalchemy import and_


class GenderEnum(EnumBase):
    """Gender enum."""

    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    NO_BINARIO = 'No binario'


class DocumentEnum(EnumBase):
    """Document enum."""

    DNI = 'DNI'
    LIBRETA_CIVICA = 'Libreta Cívica'
    LIBRETA_ENROLAMIENTO = 'Libreta de Enrolamiento'
    PASAPORTE = 'Pasaporte'


class AuthEnum(EnumBase):
    """Auth enum."""

    GOOGLE = 'Google'
    APP = 'App'


class User(BaseModel):
    """User."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.LargeBinary())
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(31), unique=True)
    gender = db.Column(db.Enum(GenderEnum,
                               values_callable=lambda x:
                               [str(e.value)for e in GenderEnum]))
    document_type = db.Column(db.Enum(DocumentEnum,
                              values_callable=lambda x:
                              [str(e.value)for e in DocumentEnum]))
    document = db.Column(db.String(31), unique=True)

    auth_method = db.Column(db.Enum(AuthEnum,
                                    values_callable=lambda x:
                                    [str(e.value)for e in AuthEnum]))

    active = db.Column(db.Boolean, default=False)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_role_institutions = db.relationship(
        'UserRoleInstitution',
        cascade='all, delete-orphan',
        passive_deletes=True
    )
    has_service_requests = db.relationship(
        'ServiceRequest', cascade='all, delete-orphan',
        passive_deletes=True, back_populates='requester'
    )
    has_notes = db.relationship(
        'Note', cascade='all, delete-orphan',
        passive_deletes=True, back_populates='user'
    )

    @classmethod
    def save(cls, **kwargs) -> object:
        """
        Create and save a new user in the database.

        Args:
            **kwargs: Keyword arguments for user attributes.

        Return:
            User: The created user object.
        """
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def find_user_by(cls, field, value):
        """Return the user with the given attribute and value."""
        return cls.query.filter_by(**{field: value}).first()

    @classmethod
    def get_user_institutions(cls, user_id: int):
        """
        Retrieve the institutions associated with a given user.

        Parameters:
            user_id (int): The ID of the user.

        Return:
            List[Institution]: A list of Institution objects
            representing the institutions associated with the user.
        """
        query = (UserRoleInstitution.get_roles_institutions_of_user(user_id))

        institutions = [Institution.get_by_id
                        (role_institution.institution_id)
                        for role_institution in query]

        return institutions

    def get_institution(self):
        """Return the institution associated with the user."""
        return self.get_user_institutions(self.id)

    @classmethod
    def get_role_in_institution(cls, user_id: int,
                                institution_id: int = None) -> object:
        """
        Return the role associated with the user.

        Args:
            user_id (int): The ID of the user.
            institution_id (int, optional): The ID of the institution.
                Defaults to None.

        Returns:
            object: The role associated with the user.
        """
        roles = (UserRoleInstitution.get_roles_institutions_of_user
                 (user_id=user_id))
        """Return the role associated with the user."""
        if not roles:
            return None

        role_id = next((role.role_id for role in roles
                        if role.institution_id == institution_id), None)
        if role_id:
            return role_id

        return None

    @classmethod
    def get_gender_name(cls, user_id: int):
        """Return the gender associated with the user."""
        gender = cls.query.filter_by(id=user_id).first().gender
        return GenderEnum(gender).value

    @classmethod
    def get_document_type_name(cls, user_id: int):
        """Return the document type associated with the user."""
        document_type = cls.query.filter_by(id=user_id).first().document_type
        return DocumentEnum(document_type).value

    @classmethod
    def get_all(cls):
        """Return all users."""
        return cls.query.filter(and_(
            cls.id != 1, cls.email != session.get("user")))

    @classmethod
    def get_active_users(cls):
        """Return active users."""
        return cls.get_all().filter(cls.active)

    @classmethod
    def get_inactive_users(cls):
        """Return inactive users."""
        return cls.get_all().filter(and_(cls.active.is_(False)))

    @classmethod
    def get_users_paginated(cls, page, per_page=None,
                            active=True, inactive=True):
        """
        Retrieve a paginated list of users based on the specified parameters.

        Args:
            page (int): The page number of the results to retrieve.
            per_page (int, optional): The number of results per page.
                Defaults to None.
            active (bool): Flag indicating whether to include active users.
                Defaults to True.
            inactive (bool): Flag indicating whether to include inactive users.
                Defaults to True.

        Returns:
            Pagination: The paginated list of users.
        """
        if active and inactive:
            users = cls.get_all()
        elif active:
            users = cls.get_active_users()
        elif inactive:
            users = cls.get_inactive_users()

        return cls.get_query_paginated(users, page, per_page)

    @classmethod
    def get_users_by_email_paginated(cls, email, page, per_page=None):
        """
        Get users by email with pagination.

        Args:
            email (str): The email address to search for.
            page (int): The page number of the results.
            per_page (int, optional): The number of results per page.
                Defaults to None.

        Returns:
            Query: A query object containing the paginated results.
        """
        users = cls.get_all().filter(cls.email.like(f"%{email}%"))
        return cls.get_query_paginated(users, page, per_page)

    @classmethod
    def get_users_by_institution_paginated(cls, institution_id: int,
                                           page, per_page=None):
        """
        Retrieve a paginated list of users associated with the institution.

        Parameters:
            - institution_id (int): The ID of the institution.
            - page (int): The page number of the results to retrieve.
            - per_page (int, optional): The number of results to retrieve
                per page. Defaults to None.

        Returns:
            - Pagination: The paginated list of users associated with
                the institution.
        """
        users = cls.get_all().join(UserRoleInstitution).filter(
            UserRoleInstitution.institution_id == institution_id)
        return cls.get_query_paginated(users, page, per_page)
