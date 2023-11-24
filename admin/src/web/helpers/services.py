"""Helpers for services."""
from datetime import datetime, timedelta
from src.core.models.service import Service, ServiceRequest


def parse_service(service):
    """
    Parse a Service object and return a dictionary.

    Parameters:
    - service (object): The service object to parse.

    Returns:
    - dict: A dictionary with the following keys:
        - id (int): The id of the service.
        - name (str): The name of the service.
        - description (str): The description of the service.
        - keywords (list): The keywords associated with the service.
        - service_type (str): The type of the service.
        - enabled (str): The status of the service (enabled or disabled).
    """
    return {'id': service.id,
            'name': service.name,
            'description': service.description,
            'keywords': service.keywords,
            'service_type': Service.get_service_type_name(service.id),
            'enabled': str(service.enabled),
            }


def parse_service_request(service_request):
    """
    Parse a service request object and returns a dictionary.

    Args:
        service_request (ServiceRequest): The service request object.

    Returns:
        dict: A dictionary containing the parsed data with the following keys:
            - 'id': The ID of the service request.
            - 'title': The title of the service request.
            - 'description': The description of the service request.
            - 'observations': The observations of the service request.
            - 'service': The name of the service associated with the request.
            - 'requester': The email of the requester.
            - 'status': The status of the service request.
            - 'inserted_at': The date and time the service request
                was inserted.
            - 'closed_at': The date and time when the service request
                was closed.
    """
    return {'id': service_request.id,
            'title': service_request.title,
            'description': service_request.description,
            'observations': service_request.observations,
            'service': service_request.service.name,
            'requester': service_request.requester.email,
            'status': service_request.status.value,
            'inserted_at': service_request.inserted_at.strftime("%d-%m-%Y"),
            'closed_at': (service_request.closed_at.strftime("%d-%m-%Y") if
                          service_request.closed_at else 'No cerrado'),
            }


def parse_note(note):
    """Perse note object and return a dictionary."""
    return {
            'text': note.text,
            'user': note.user,
            'updated_at': note.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            }


def filter_conditions(filters):
    """
    Generate a list of SQLAlchemy filter conditions based on the given filters.

    Parameters:
        filters (dict): A dictionary containing the filters
        to apply to the query.
            The keys are the filter names, and the values are the
            corresponding values to filter by.

    Returns:
        list: A list of SQLAlchemy filter conditions that can be used to
        filter a query.
            Each condition is a SQLAlchemy expression that can be passed to
            the `filter` method of a query object.
    """
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


def add_days_to_today(days):
    """Add days to a date."""
    result = datetime.now() + timedelta(days=days)
    return result.strftime("%Y-%m-%d %H:%M:%S")
