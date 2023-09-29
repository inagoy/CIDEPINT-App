from datetime import datetime
from src.core.database import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
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
