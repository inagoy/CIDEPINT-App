from src.core.models.service import Service


def parse_service(service):
    return {'id': service.id,
            'name': service.name,
            'description': service.description,
            'keywords': service.keywords,
            'service_type': Service.get_service_type_name(service.id),
            'enabled': str(service.enabled),
            }
