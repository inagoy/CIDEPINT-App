"""Hashed email model."""
from datetime import datetime
from src.core.models.user import User
from src.core.database import db


class HashedEmail(db.Model):
    """Hashed email."""

    __tablename__ = "hashed_email"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    hashed_email = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id",
                                                  ondelete="CASCADE"),
                        nullable=False)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def save(cls, hashed_email, user_id, **kwargs) -> object:
        """
        Save a hashed email to the database.

        Args:
            hash (str): The hash of the email.
            user_id (int): The ID of the user associated with the email.
            **kwargs: Additional keyword arguments.

        Returns:
            object: The saved hashed email object.
        """
        hashed_email = HashedEmail(hashed_email=hashed_email, user_id=user_id,
                                   **kwargs)
        db.session.add(hashed_email)
        db.session.commit()
        return hashed_email

    @classmethod
    def find_user_by_hash(cls, hashed_email) -> object:
        """
        Find a user by their hashed email.

        Parameters:
            hashed_email (str): The hashed email of the user.

        Returns:
            object: The user object if found, None otherwise.
        """
        instance = cls.query.filter_by(hashed_email=hashed_email).first()
        if instance:
            return User.query.get(instance.user_id)
        return None

    @classmethod
    def find_hashed_email_by_user_id(cls, user_id) -> object:
        """
        Find a hashed email by its ID.

        Parameters:
            id (int): The ID of the hashed email.

        Returns:
            object: The hashed email object if found, None otherwise.
        """
        instance = cls.query.filter_by(user_id=user_id).first()
        if instance:
            return instance.hashed_email
        return None
