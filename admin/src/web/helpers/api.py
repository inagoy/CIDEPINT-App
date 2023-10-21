from src.core.models.user import User


def response_error():
    return {
        "error": "Parámetros inválidos"
    }, 400


def paginated_response(paginated_data, schema):
    return {
        "data": schema.dump(paginated_data.items),
        "page": paginated_data.page,
        "per_page": paginated_data.per_page,
        "total": paginated_data.total
    }, 200


def get_user_if_valid(user_id=None):
    if not user_id:
        return None
    user = User.get_by_id(user_id)
    if not user:
        return None
    return user
