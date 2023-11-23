"""Services seeds."""
from src.web.helpers.services import add_days_to_today
from src.core.models.service import Note, Service, ServiceTypeEnum
from src.core.models.service import ServiceRequest, StatusEnum


def seed_services() -> None:
    """Seed the database with initial services."""
    services_data = [
        {
            "name": "Ensayo de corrosión",
            "description": "Servicio de ensayo de corrosión de materiales",
            "keywords": "ensayo, corrosión, materiales",
            "service_type": ServiceTypeEnum.ANALISIS.value,
            "enabled": True,
            "institution_id": 1,
        },

        {
            "name": "Desarrollo de Pinturas Avanzadas",
            "description": "Servicio de desarrollo de pinturas avanzadas",
            "keywords": "desarrollo, formulación, pinturas avanzadas",
            "service_type": ServiceTypeEnum.DESARROLLO.value,
            "enabled": True,
            "institution_id": 1,
        },
        {
            "name": "Envejecimiento acelerado",
            "description": "Servicio de Cámara de envejecimiento UV",
            "keywords": "envejecimiento, acelerado, luz,condensación",
            "service_type": ServiceTypeEnum.DESARROLLO.value,
            "enabled": True,
            "institution_id": 1,
        },
        {
            "name": "Consultoria de Pinturas",
            "description": "Servicio de Consultoria de pinturas",
            "keywords": "pinturas, consultor",
            "service_type": ServiceTypeEnum.CONSULTORIA.value,
            "enabled": True,
            "institution_id": 2,
        },
        {
            "name": "Análisis de Resistencia a la Abrasión",
            "description": "Servicio de evaluación de la resistencia a la abrasión de recubrimientos",
            "keywords": "análisis, resistencia, abrasión, recubrimientos",
            "service_type": ServiceTypeEnum.ANALISIS.value,
            "enabled": True,
            "institution_id": 3
        },
        {
            "name": "Análisis de Suelos",
            "description": "Evaluación de la resistencia a los recubrimientos de suelos",
            "keywords": "análisis, resistencia, suelos, recubrimientos",
            "service_type": ServiceTypeEnum.ANALISIS.value,
            "enabled": True,
            "institution_id": 3
        }
    ]

    for service_data in services_data:
        service = Service.save(**service_data)
        print(f"Created service: {service.name} - "
              f"Type: {service.service_type.value}")


def seed_service_requests() -> None:
    """
    Populate the database with initial service request data.

    Args:
        None

    Returns:
        None
    """
    service_requests_data = [
        {
            "title": "Solicitud de Servicio de Ejemplo 1",
            "description": "Esta es una solicitud de servicio de ejemplo",
            "observations": "Sin observaciones adicionales",
            "service_id": 1,
            "requester_id": 1,
            "status": StatusEnum.ACEPTADA.value,
        },

        {
            "title": "Solicitud de Servicio de Ejemplo 2",
            "description": "Esta es una segunda solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 1,
            "requester_id": 2,
            "status": StatusEnum.EN_PROCESO.value,
        },
        {
            "title": "Solicitud de Servicio de Ejemplo 3",
            "description": "Esta es una tercera solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 2,
            "requester_id": 2,
            "status": StatusEnum.EN_PROCESO.value,
        },
        {
            "title": "Solicitud de Servicio de Ejemplo 4",
            "description": "Esta es una cuarta solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 3,
            "requester_id": 1,
            "status": StatusEnum.FINALIZADA.value,
            "closed_at": add_days_to_today(5)

        },
        {
            "title": "Solicitud de Servicio de Ejemplo 5",
            "description": "Esta es una quinta solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 3,
            "requester_id": 2,
            "status": StatusEnum.EN_PROCESO.value,
        },
        {
            "title": "Solicitud de Servicio de Ejemplo 6",
            "description": "Esta es una quinta solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 4,
            "requester_id": 2,
            "status": StatusEnum.EN_PROCESO.value,
        },
        {
            "title": "Solicitud de Servicio de Ejemplo 7",
            "description": "Esta es una quinta solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 5,
            "requester_id": 2,
            "status": StatusEnum.EN_PROCESO.value,
        },
        {
            "title": "Solicitud de Servicio de Ejemplo 8",
            "description": "Esta es una sexta solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 3,
            "requester_id": 2,
            "status": StatusEnum.EN_PROCESO.value,
        },
        {
            "title": "Solicitud de Servicio de Ejemplo 9",
            "description": "Esta es una sexta solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 3,
            "requester_id": 3,
            "status": StatusEnum.EN_PROCESO.value,
        },
        {
            "title": "Solicitud de Servicio de Ejemplo 10",
            "description": "Esta es una septima solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 4,
            "requester_id": 3,
            "status": StatusEnum.FINALIZADA.value,
            "closed_at": add_days_to_today(10)
        },
        {
            "title": "Solicitud de Servicio de Ejemplo 11",
            "description": "Esta es una octava solicitud de servicio",
            "observations": "Sin observaciones adicionales",
            "service_id": 5,
            "requester_id": 3,
            "status": StatusEnum.FINALIZADA.value,
            "closed_at": add_days_to_today(3)
        },
    ]

    for service_request_data in service_requests_data:
        service_request = ServiceRequest.save(**service_request_data)
        print(
            f"Created service request:{service_request.title}"
        )


def seed_notes() -> None:
    """
    Populate the database with initial note data.

    Args:
        None

    Returns:
        None
    """
    notes_data = [
        {
            "text": "Ejemplo de nota de usuario 1 para servicio 1",
            "user_id": 1,
            "service_request_id": 1,
        },

        {
            "text": "Otro ejemplo de nota de usuario 2 para servicio 2",
            "user_id": 2,
            "service_request_id": 2,
        },
    ]

    for note_data in notes_data:
        note = Note.save(**note_data)
        print(
            f"Created note: {note.text}"
        )
