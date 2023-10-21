from datetime import datetime
from src.core.database import db
from enum import Enum as EnumBase
from src.core.models.user_role_institution import UserRoleInstitution
from src.core.models.institution import Institution
from src.core.models.base_model import BaseModel
from flask import session
from sqlalchemy import and_


class GenderEnum(EnumBase):
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    NO_BINARIO = 'No binario'


class DocumentEnum(EnumBase):
    DNI = 'DNI'
    PASAPORTE = 'Pasaporte'


class User(BaseModel):
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

        Returns:
            User: The created user object.
        """

        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def find_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_user_by_document(cls, document):
        return cls.query.filter_by(document=document).first()

    @classmethod
    def find_user_by_phone_number(cls, phone_number):
        return cls.query.filter_by(phone_number=phone_number).first()

    @classmethod
    def get_user_institutions(cls, user_id: int):
        query = (UserRoleInstitution.get_roles_institutions_of_user(user_id))

        institutions = [Institution.get_by_id
                        (role_institution.institution_id)
                        for role_institution in query]

        return institutions

    def get_institution(self):
        return self.get_user_institutions(self.id)

    @classmethod
    def get_role_in_institution(cls, user_id: int,
                                institution_id: int = None) -> object:

        roles = (UserRoleInstitution.get_roles_institutions_of_user
                 (user_id=user_id))
        if not roles:
            return None

        role_id = next((role.role_id for role in roles
                        if role.institution_id == institution_id), None)
        if role_id:
            return role_id

        return None

    @classmethod
    def get_gender_name(cls, user_id: int):
        gender = cls.query.filter_by(id=user_id).first().gender
        return GenderEnum(gender).name.capitalize()

    @classmethod
    def get_document_type_name(cls, user_id: int):
        document_type = cls.query.filter_by(id=user_id).first().document_type
        return DocumentEnum(document_type).name

    @classmethod
    def get_all(cls):
        return cls.query.filter(and_(
            cls.id != 1, cls.email != session["user"]))

    @classmethod
    def get_active_users(cls):
        return cls.get_all().filter(cls.active)

    @classmethod
    def get_inactive_users(cls):
        return cls.get_all().filter(cls.active.is_(False))

    @classmethod
    def get_users_paginated(cls, page, per_page=None,
                            active=True, inactive=True):
        if active and inactive:
            users = cls.get_all()
        elif active:
            users = cls.get_active_users()
        elif inactive:
            users = cls.get_inactive_users()

        return cls.get_query_paginated(users, page, per_page)

    @classmethod
    def get_users_by_email_paginated(cls, email, page, per_page=None):
        users = cls.get_all().filter(cls.email.like(f"%{email}%"))
        return cls.get_query_paginated(users, page, per_page)

    @classmethod
    def get_users_by_institution_paginated(cls, institution_id: int,
                                           page, per_page=None):

        users = cls.get_all().join(UserRoleInstitution).filter(
            UserRoleInstitution.institution_id == institution_id)
        return cls.get_query_paginated(users, page, per_page)
