from src.core.models.service import Service, ServiceTypeEnum


def seed_services() -> None:
    """seed_services

    This function populates the database with initial service data
    for testing and development purposes.

    Args:
        None

    Returns:
        None
    """

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
            "institution_id": 2,
        },

    ]

    for service_data in services_data:
        service = Service.save(**service_data)
        print(f"Created service: {service.name} - "
              f"Type: {service.service_type.value}")
