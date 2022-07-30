def match_form(code_format, data):
    if len(code_format) != len(data):
        return False
    else:
        for code_word, data_word in zip(code_format, data):
            if code_word == "x":
                pass
            else:
                if code_word != data_word:
                    return False
        return True
    
def bytes_conversion(value):
    if isinstance(value, bytes):
        return value.decode("utf-32")
    elif isinstance(value, str):
        return value.encode("utf-32")
    else:
        return