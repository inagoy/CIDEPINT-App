
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


def convert_to_percentage(int_list):
    total = sum(int_list)
    percentages = [round(((value / total) * 100), 2) for value in int_list]
    return {'percentages': percentages, 'total': total}
