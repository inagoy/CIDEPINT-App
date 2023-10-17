from datetime import datetime
from enum import Enum as EnumBase
from src.core.database import db
from src.core.models.base_model import BaseModel


class ServiceTypeEnum(EnumBase):
    ANALISIS = 'Análisis'
    CONSULTORIA = 'Consultoría'
    DESARROLLO = 'Desarrollo'


class Service(BaseModel):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.String(255), nullable=False)

    # Convert enum values to strings for 'service_type' column:
    # values_callable configures how Enum values are stored in the database,
    # ensuring they are saved as human-readable strings
    service_type = db.Column(db.Enum(ServiceTypeEnum,
                                     values_callable=lambda x:
                                     [str(e.value)for e in ServiceTypeEnum]),
                             nullable=False)

    enabled = db.Column(db.Boolean, default=True)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'),
                               nullable=False)
    institution = db.relationship('Institution', back_populates='has_services')

    @classmethod
    def save(cls, name: str, description: str,
             keywords: str, service_type: str,
             institution_id: int, **kwargs) -> object:
        """
        Saves a new service to the database.

        Args:
            name (str): The name of the service.
            description (str): The description of the service.
            keywords (str): The keywords associated with the service.
            service_type (str): The type of the service.
            institution_id (int): The ID of the associated institution.
            **kwargs: Additional keyword arguments to be passed to the Service
            constructor.

        Returns:
            Service: The newly created service object.
        """

        service = Service(name=name, description=description,
                          keywords=keywords, service_type=service_type,
                          institution_id=institution_id, **kwargs)
        db.session.add(service)
        db.session.commit()
        return service
