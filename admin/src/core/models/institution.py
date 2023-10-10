from datetime import datetime
from src.core.database import db


class Institution(db.Model):
    __tablename__ = "institutions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    info = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(255), unique=True, nullable=False)
    location = db.Column(db.String(255), unique=True, nullable=False)
    website = db.Column(db.String(255), unique=True, nullable=False)
    search_keywords = db.Column(db.String(255), unique=True, nullable=False)
    days_and_hours = db.Column(db.Text, unique=True, nullable=False)
    contact_info = db.Column(db.String(255), unique=True, nullable=False)
    enabled = db.Column(db.Boolean, default=False)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    has_services = db.relationship("Service", back_populates="institution")

    @classmethod
    def save(cls, name: str, info: str, address: str, location: str,
             website: str, search_keywords: str,
             days_and_hours: str, contact_info: str,
             **kwargs) -> object:
        """save
        Create and save a new institution in the database.

        Args:
            name (str): The name of the institution.
            info (str): Information about the institution.
            address (str): The institution's address.
            location (str): The location of the institution.
            website (str): The institution's website.
            search_keywords (str): Keywords for searching the institution.
            days_and_hours (str): The days and hours of operation.
            contact_info (str): Contact information for the institution.
            **kwargs: Additional keyword arguments for user attributes.

        Returns:
            Institution: The created institution object.
        """
        institution = Institution(name=name, info=info, address=address,
                                  location=location, website=website,
                                  search_keywords=search_keywords,
                                  days_and_hours=days_and_hours,
                                  contact_info=contact_info, **kwargs)
        db.session.add(institution)
        db.session.commit()
        return institution

    @classmethod
    def get_institution_by_id(cls, id: int):
        return cls.query.filter_by(id=id).first()
