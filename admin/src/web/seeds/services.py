"""Services seeds."""
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
            'name': 'Envejecimiento Acelerado e Intemperismo',
            'description': 'Realización de ensayos de envejecimiento acelerado e intemperismo según normativas ASTM.',
            'keywords': 'ensayos, envejecimiento acelerado, intemperismo, pinturas, recubrimientos',
            'service_type': ServiceTypeEnum.ANALISIS.value,
            'enabled': True,
            'institution_id': 2,
        },
        {
            'name': 'Asesoramiento en Biodeterioro',
            'description': 'Asesoramiento especializado en biodeterioro de materiales estructurales.',
            'keywords': 'asesoramiento, biodeterioro, materiales estructurales',
            'service_type': ServiceTypeEnum.CONSULTORIA.value,
            'enabled': True,
            'institution_id': 1,
        },
        {
            'name': 'Curso de Posgrado: Protección de Superficies Metálicas',
            'description': 'Curso de posgrado enfocado en la protección de superficies metálicas y su control por pinturas.',
            'keywords': 'curso, posgrado, protección, superficies metálicas, pinturas',
            'service_type': ServiceTypeEnum.DESARROLLO.value,
            'enabled': True,
            'institution_id': 2,
        },
        {
            'name': 'Pruebas de Resistencia a la Corrosión',
            'description': 'Realización de ensayos para evaluar la resistencia a la corrosión de materiales y recubrimientos.',
            'keywords': 'pruebas, resistencia a la corrosión, materiales, recubrimientos',
            'service_type': ServiceTypeEnum.ANALISIS.value,
            'enabled': True,
            'institution_id': 1,
        },
        {
            'name': 'Desarrollo de Nuevos Recubrimientos Anticorrosivos',
            'description': 'Asesoramiento y desarrollo de nuevos recubrimientos para prevenir la corrosión en ambientes específicos.',
            'keywords': 'desarrollo, recubrimientos anticorrosivos, asesoramiento',
            'service_type': ServiceTypeEnum.DESARROLLO.value,
            'enabled': True,
            'institution_id': 1,
        },
        {
            'name': 'Inspección de Pinturas Industriales en Obra',
            'description': 'Inspección de aplicación y calidad de pinturas industriales en proyectos de construcción.',
            'keywords': 'inspección, pinturas industriales, construcción',
            'service_type': ServiceTypeEnum.CONSULTORIA.value,
            'enabled': True,
            'institution_id': 2,
        },
        {
            'name': 'Asesoramiento en Procesos de Galvanoplastía',
            'description': 'Asesoramiento técnico en procesos de galvanoplastía para mejorar la calidad y durabilidad de los productos.',
            'keywords': 'asesoramiento, galvanoplastía, procesos',
            'service_type': ServiceTypeEnum.CONSULTORIA.value,
            'enabled': True,
            'institution_id': 2,
        },
        {
            'name': 'Curso Avanzado: Técnicas de Ensayos en Pinturas',
            'description': 'Curso avanzado dirigido a profesionales sobre las últimas técnicas de ensayos en pinturas y recubrimientos.',
            'keywords': 'curso avanzado, ensayos en pinturas, recubrimientos',
            'service_type': ServiceTypeEnum.DESARROLLO.value,
            'enabled': True,
            'institution_id': 1,
        },
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
