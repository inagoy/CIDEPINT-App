from datetime import datetime
from src.core.database import db
from enum import Enum as EnumBase


class GenderEnum(EnumBase):
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    NO_BINARIO = 'No binario'


class DocumentEnum(EnumBase):
    DNI = 'DNI'
    PASAPORTE = 'Pasaporte'


class User(db.Model):
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
    def update(cls, user_id, **kwargs):
        """
        Update an existing user's attributes in the database.

        Args:
            user_id (int): The ID of the user to be updated.
            **kwargs: Keyword arguments representing the attributes to update.

        Returns:
            User: The updated user object.
        """

        user = cls.query.get(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.updated_at = datetime.utcnow()
            db.session.commit()
            return user
        else:
            return None

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
