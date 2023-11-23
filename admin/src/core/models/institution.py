"""Institution model."""
from datetime import datetime

from src.core.models.service import Service
from src.core.database import db
from src.core.models.base_model import BaseModel
from src.core.models.user_role_institution import UserRoleInstitution


class Institution(BaseModel):
    """Institution."""

    __tablename__ = "institutions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    info = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(255))
    location = db.Column(db.String(255))
    coordinates = db.Column(db.String(255))
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
        """
        Create and save a new institution in the database.

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
        """Return if the institution is enabled."""
        return cls.query.filter_by(id=institution_id).first().enabled

    @classmethod
    def get_all_institutions(cls):
        return cls.query.all()

    @classmethod
    def get_enabled_institutions_for_user(cls, user_id):
        """
        Get the list of enabled institutions for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Institution]: A list of enabled Institution objects.
        """
        institutions = Institution.query.join(UserRoleInstitution).filter(
            UserRoleInstitution.user_id == user_id,
            Institution.enabled
        ).all()
        return institutions

    @classmethod
    def get_institutions_owned_by_user(cls, user_id):
        """
        Retrieve the institutions owned by a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            List[Institution]: A list of Institution objects
                representing the institutions owned by the user.
        """
        institutions = Institution.query.join(UserRoleInstitution).filter(
            UserRoleInstitution.user_id == user_id,
            UserRoleInstitution.role_id == 2
        ).all()
        return institutions

    def average_response_time(self):
        """Calculate the average response time for service requests."""
        total_response_time = 0
        total_requests = 0
        for service in self.has_services:
            for service_request in service.has_service_requests:
                if service_request.closed_at:
                    total_response_time += service_request.get_response_time()
                    total_requests += 1
        return total_response_time / total_requests

    @classmethod
    def get_ordered_by_average_response_time(cls):
        """Get instances of the class ordered by average response time."""
        query = (
            db.session.query(cls)
            .filter(cls.has_services.any(Service.has_service_requests.any()))
        )

        instances = query.all()
        result = {
            instance.name:
            instance.average_response_time() for instance in instances
        }
        sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))
        institutions = list(sorted_result.keys())[:10]
        averages = list(sorted_result.values())[:10]

        return {"institutions": institutions, "averages": averages}
