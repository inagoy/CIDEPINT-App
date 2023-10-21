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
