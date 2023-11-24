"""Service model."""
from datetime import datetime
from enum import Enum as EnumBase

from sqlalchemy import or_, func, and_
from src.core.database import db
from src.core.models.base_model import BaseModel


class ServiceTypeEnum(EnumBase):
    """ServiceTypeEnum."""

    ANALISIS = 'Análisis'
    CONSULTORIA = 'Consultoría'
    DESARROLLO = 'Desarrollo'


class Service(BaseModel):
    """Service."""

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

    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id',
                                                         ondelete="CASCADE"),
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
        Save a new service to the database.

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

    @classmethod
    def get_service_type_name(cls, service_id: int):
        """Return the service type associated with the service."""
        service = cls.query.filter_by(id=service_id).first().service_type
        return ServiceTypeEnum(service).name.capitalize()

    @classmethod
    def get_services_of_institution_paginated(
            cls, page: int, institution_id: int
    ):
        """
        Get the paginated list of services for a given institution.

        Args:
            page (int): The page number to retrieve.
            institution_id (int): The ID of the institution.

        Returns:
            PaginatedQuery: The paginated query object containing the services.
        """
        query = cls.query.filter_by(institution_id=institution_id)
        return cls.get_query_paginated(query, page)

    @classmethod
    def search_by_keyword(
        cls, q, page=1, per_page=None, type=None
    ):
        base_query = cls.query.filter(
            or_(
                cls.name.ilike(f"%{q}%"),
                cls.keywords.ilike(f"%{q}%"),
                cls.description.ilike(f"%{q}%")
            )
        )
        if type:
            base_query = base_query.filter(
                cls.service_type == type
            )
        return cls.get_query_paginated(
            base_query, page=page, per_page=per_page
        )

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_all_service_types(cls):
        service_types = db.session.query(cls.service_type).distinct().all()
        return [type_[0].value for type_ in service_types]

    @classmethod
    def get_top_requested_services(cls):
        result = (
            db.session.query(cls.name, func.count(ServiceRequest.id))
            .join(cls.has_service_requests)
            .group_by(cls.name)
            .order_by(func.count(ServiceRequest.id).desc())
            .limit(6)
            .all()
        )

        services = [name for name, _ in result]
        requests = [requests for _, requests in result]

        most_requested_services = {
            'services': services, 'requests': requests
        }
        return most_requested_services

    @classmethod
    def get_request_count_by_service_type(cls):
        result = (
            db.session.query(cls.service_type, func.count(ServiceRequest.id))
            .outerjoin(cls.has_service_requests)
            .group_by(cls.service_type)
            .all()
        )
        service_types = [service_type.value for service_type, _ in result]
        requests = [requests for _, requests in result]
        return {'types': service_types, 'requests': requests}


class StatusEnum(EnumBase):
    """StatusEnum."""

    ACEPTADA = "Aceptada"
    RECHAZADA = "Rechazada"
    EN_PROCESO = "En proceso"
    FINALIZADA = "Finalizada"
    CANCELADA = "Cancelada"


class ServiceRequest(BaseModel):
    """ServiceRequest."""

    __tablename__ = 'service_requests'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    observations = db.Column(db.Text, default="Sin observaciones adicionales")
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
        db.DateTime, nullable=True, default=None
    )
    status_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    @classmethod
    def save(cls, title: str, description: str,
             service_id: str, requester_id: str,
             **kwargs) -> object:
        """
        Save a service request to the database.

        Args:
            title (str): The title of the service request.
            description (str): The description of the service request.
            ervice_id (str): The ID of the service associated with the request.
            requester_id (str): The ID of the user making the request.
            **kwargs: Additional keyword arguments.

        Returns:
            object: The saved service request object.
        """
        service_request = ServiceRequest(
            title=title, description=description,
            service_id=service_id, requester_id=requester_id,
            **kwargs
        )
        db.session.add(service_request)
        db.session.commit()
        return service_request

    @classmethod
    def get_service_requests_of_service_paginated(
            cls, page: int, service_id: int
    ):
        """
        Get the service requests of a specific service in a paginated manner.

        Args:
            page (int): The page number of the paginated results.
            service_id (int): The ID of the service.

        Returns:
            Pagination: The paginated service requests
            of the specified service.
        """
        query = cls.query.filter_by(service_id=service_id)
        return cls.get_query_paginated(query, page)

    @classmethod
    def get_service_requests_of_institution(
            cls, institution_id: int
    ):
        """Return the service requests of an institution."""
        query = cls.query.join(Service).filter(
            Service.institution_id == institution_id
        )
        return query

    @classmethod
    def get_service_requests_of_institution_paginated(
            cls, page: int, institution_id: int
    ):
        """Return the paginated service requests of an institution."""
        query = cls.get_service_requests_of_institution(institution_id)
        return cls.get_query_paginated(query, page)

    @classmethod
    def of_institution_filtered_paginated(cls, page: int, institution_id: int,
                                          conditions: list):
        """Return the filtered paginated service requests of an institution."""
        query = cls.get_service_requests_of_institution(institution_id)

        institutions = query.filter(and_(*conditions))

        return cls.get_query_paginated(institutions, page)

    @classmethod
    def get_user_sorted_paginated(cls, user_id: int, page: int,
                                  per_page: int, sort: str, order: str):
        query = cls.query.filter_by(requester_id=user_id).order_by(
            getattr(cls, sort).desc() if order == 'desc' else
            getattr(cls, sort).asc()
        )
        return cls.get_query_paginated(query, page, per_page)

    @classmethod
    def get_by_id_and_user(cls, user_id: int, id: int):
        return cls.query.filter_by(id=id, requester_id=user_id).first()

    def get_response_time(self):
        """Calculate the response time in days for a service request."""
        return round(
            (
                (self.closed_at - self.inserted_at)
                .total_seconds() / (24*3600)
            ), 2)


class Note(BaseModel):
    """Note."""

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
        """
        Save the given text as a note for a specific user and service request.

        Args:
            text (str): The text of the note.
            user_id (str): The ID of the user.
            service_request_id (str): The ID of the service request.
            **kwargs: Additional keyword arguments.

        Returns:
            object: The saved note object.
        """
        note = Note(
            text=text, user_id=user_id,
            service_request_id=service_request_id, **kwargs
        )
        db.session.add(note)
        db.session.commit()
        return note

    @classmethod
    def get_notes_of_service_request(cls, service_request_id: str):
        """Return the notes of a specific service request."""
        return cls.query.filter_by(service_request_id=service_request_id).all()
