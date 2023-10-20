def mapping_form(key_dict: dict, form: dict) -> dict:
    form_dict = {key_dict.get(old_key, old_key):
                 value for old_key, value in form.items()}

    non_empty = {key: value for key, value in form_dict.items() if value}
    return non_empty
