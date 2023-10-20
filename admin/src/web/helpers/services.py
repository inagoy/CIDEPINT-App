from src.core.models.service import Service
from src.core.models.user import User


def parse_service(service):
    return {'id': service.id,
            'name': service.name,
            'description': service.description,
            'keywords': service.keywords,
            'service_type': Service.get_service_type_name(service.id),
            'enabled': str(service.enabled),
            }


def parse_service_request(service_request):
    return {'id': service_request.id,
            'title': service_request.title,
            'description': service_request.description,
            'observations': service_request.observations,
            'service': Service.get_by_id(service_request.service_id).name,
            'requester': User.get_by_id(service_request.requester_id).email,
            'status': service_request.status.value
            }


def parse_note(note):
    return {
            'text': note.text,
            'user': note.user,
            'updated_at': note.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            }
