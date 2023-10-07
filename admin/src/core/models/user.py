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
    password = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(31))
    gender = db.Column(db.Enum(GenderEnum,
                               values_callable=lambda x:
                               [str(e.value)for e in GenderEnum]))
    document_type = db.Column(db.Enum(DocumentEnum,
                              values_callable=lambda x:
                              [str(e.value)for e in DocumentEnum]))
    document = db.Column(db.String(31))

    active = db.Column(db.Boolean, default=False)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def save(cls, first_name, last_name, email, **kwargs) -> object:
        """
        Create and save a new user in the database.

        Args:
            first_name (str): The user's first_name.
            last_name (str): The user's last_name.
            email (str): The user's email address.
            **kwargs: Additional keyword arguments for user attributes.

        Returns:
            User: The created user object.
        """

        user = User(first_name=first_name, last_name=last_name, email=email,
                    **kwargs)
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
        """
        Find a user by email address.

        Args:
            email (str): The email address of the user to find.

        Returns:
            User: The user object found, or None if no user was found.
        """
        return cls.query.filter_by(email=email).first()