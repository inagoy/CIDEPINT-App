from src.core.models.service import Service, ServiceRequest
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
            'service': service_request.service.name,
            'requester': service_request.requester.email,
            'status': service_request.status.value,
            'inserted_at': service_request.inserted_at.strftime("%d-%m-%Y"),
            'closed_at': service_request.closed_at.strftime("%d-%m-%Y"),
            }


def parse_note(note):
    return {
            'text': note.text,
            'user': note.user,
            'updated_at': note.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            }


def filter_conditions(filters):
    conditions = []

    filter_conditions = {
        "service_type": lambda val:
            ServiceRequest.service.has(service_type=val),
        "status": lambda val: ServiceRequest.status == val,
        "email": lambda val: ServiceRequest.requester.has(email=val),
        "start_date": lambda val: ServiceRequest.inserted_at >= val,
        "end_date": lambda val: ServiceRequest.closed_at <= val,
    }

    for key, value in filters.items():
        conditions.append(filter_conditions[key](value))

    return conditions
