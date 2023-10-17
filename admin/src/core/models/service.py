from datetime import datetime, timedelta
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

    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'),
                               nullable=False)
    institution = db.relationship('Institution', back_populates='has_services')
    has_requests = db.relationship(
        'ServiceRequest', cascade='all, delete-orphan',
        pasive_deletes=True, back_populates='service'
    )

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


class StatusEnum(EnumBase):
    ACEPTADA = "Aceptada"
    RECHAZADA = "Rechazada"
    EN_PROCESO = "En proceso"
    FINALIZADA = "Finalizada"
    CANCELADA = "Cancelada"


class ServiceRequest(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    observations = db.Column(db.Text)
    service_id = db.Column(db.Integer,
                           db.ForeignKey('service.id', ondelete='CASCADE'),
                           nullable=False
                           )
    service = db.relationship('Service', back_populates='has_requests')
    requester = db.Column(db.Integer,
                          db.ForeignKey('user.id', ondelete='CASCADE'),
                          nullable=False
                          )
    user = db.relationship('User', back_populates='has_requests')
    status = db.Column(db.Enum(StatusEnum,
                               values_callable=lambda x:
                               [str(e.value)for e in StatusEnum]),
                       nullable=False
                       )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    closed_at = db.Column(
        db.DateTime, default=datetime.utcnow + timedelta(months=2)
    )
    status_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Note(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=False
                        )
    user = db.relationship('User', back_populates='has_notes')
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
