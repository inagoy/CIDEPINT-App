def parse_institution(institution):
    """
    Generates a dictionary with the institution's information.

    Args:
        institution (Institution): The user object containing the
        institution's information.

    Returns:
        dict: A dictionary with the institution's information
    """
    data = {
        'id': institution.id,
        'name': institution.name,
        'info': institution.info,
        'address': institution.address,
        'location': institution.location,
        'website': institution.website,
        'search_keywords': institution.search_keywords,
        'days_and_hours': institution.days_and_hours,
        'contact_info': institution.contact_info,
        'enabled': str(institution.enabled)
    }

    return {key: value for key, value in data.items() if value is not None}


def get_name(institution):
    return institution.name
