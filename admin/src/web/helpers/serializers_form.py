"""Helper for serializing forms."""


def mapping_form(key_dict: dict, form: dict) -> dict:
    """
    Map the keys of a dictionary `form` using a provided mapping dictionary.

    Parameters:
        key_dict (dict): A dictionary with the mapping of old keys to new keys.
        form (dict): The dictionary to be mapped.

    Returns:
        dict: A new dictionary with the keys mapped
        according to the `key_dict` mapping.
    """
    form_dict = {key_dict.get(old_key, old_key):
                 value for old_key, value in form.items()}

    non_empty = {key: value for key, value in form_dict.items() if value}
    return non_empty
