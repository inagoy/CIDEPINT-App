from datetime import datetime
from src.core.database import db
from src.core.models.base_model import BaseModel
from src.core.models.user_role_institution import UserRoleInstitution


class Institution(BaseModel):
    __tablename__ = "institutions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    info = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(255))
    location = db.Column(db.String(255))
    website = db.Column(db.String(255))
    search_keywords = db.Column(db.String(255))
    days_and_hours = db.Column(db.Text)
    contact_info = db.Column(db.String(255))
    enabled = db.Column(db.Boolean, default=True)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    has_services = db.relationship(
        "Service",
        back_populates="institution",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    user_role_institutions = db.relationship(
        'UserRoleInstitution',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    @classmethod
    def save(cls, name: str, info: str, **kwargs) -> object:
        """save
        Create and save a new institution in the database, only name and info
        are required attributes

        Args:
            name (str): The name of the institution.
            info (str): Information about the institution.
            **kwargs: Keyword arguments for institution attributes.

        Returns:
            Institution: The created institution object.
        """
        institution = Institution(name=name, info=info, **kwargs)
        db.session.add(institution)
        db.session.commit()
        return institution

    @classmethod
    def is_enabled(cls, institution_id):
        return cls.query.filter_by(id=institution_id).first().enabled

    @classmethod
    def get_all_institutions(cls):
        return cls.query.all()

    @classmethod
    def get_institutions_paginated(cls, page, per_page=None):
        if per_page is None:
            per_page = SiteConfig.get_items_per_page()
        return cls.query.paginate(page=page, per_page=per_page)
