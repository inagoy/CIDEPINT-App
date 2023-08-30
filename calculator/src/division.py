def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "No es posible dividir por cero"