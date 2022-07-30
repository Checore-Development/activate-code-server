def bytes_conversion(value):
    if isinstance(value, bytes):
        return value.decode("utf-32")
    elif isinstance(value, str):
        return value.encode("utf-32")
    else:
        return