def judgment_integer(value):
    if value is None or isinstance(value, int):
        return True
    else:
        try:
            int(value)
            return True
        except:
            return False