from datetime import datetime, date, timedelta
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
    has_service_requests = db.relationship(
        'ServiceRequest', cascade='all, delete-orphan',
        passive_deletes=True, back_populates='service'
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
    __tablename__ = 'service_requests'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    observations = db.Column(db.Text)
    service_id = db.Column(db.Integer,
                           db.ForeignKey('services.id', ondelete='CASCADE'),
                           nullable=False
                           )
    service = db.relationship('Service', back_populates='has_service_requests')
    requester_id = db.Column(db.Integer,
                             db.ForeignKey('users.id', ondelete='CASCADE'),
                             nullable=False
                             )
    requester = db.relationship('User', back_populates='has_service_requests')
    status = db.Column(db.Enum(StatusEnum,
                               values_callable=lambda x:
                               [str(e.value)for e in StatusEnum]),
                       nullable=False,
                       default=StatusEnum.EN_PROCESO.value
                       )
    has_notes = db.relationship(
        'Note', cascade='all, delete-orphan',
        passive_deletes=True, back_populates='service_request'
    )

    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    closed_at = db.Column(
        db.DateTime, default=(date.today() + timedelta(days=62)),
    )
    status_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    @classmethod
    def save(cls, title: str, description: str,
             service_id: str, requester_id: str,
             **kwargs) -> object:

        service_request = ServiceRequest(
            title=title, description=description,
            service_id=service_id, requester_id=requester_id,
            **kwargs
        )
        db.session.add(service_request)
        db.session.commit()
        return service_request


class Note(BaseModel):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    service_request_id = db.Column(db.Integer,
                                   db.ForeignKey('service_requests.id',
                                                 ondelete='CASCADE'),
                                   nullable=False
                                   )
    service_request = db.relationship('ServiceRequest',
                                      back_populates='has_notes'
                                      )
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id', ondelete='CASCADE'),
                        nullable=False
                        )
    user = db.relationship('User', back_populates='has_notes')
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    @classmethod
    def save(cls, text: str, user_id: str,
             service_request_id: str, **kwargs
             ) -> object:

        note = Note(
            text=text, user_id=user_id,
            service_request_id=service_request_id, **kwargs
        )
        db.session.add(note)
        db.session.commit()
        return note
