def judgment_integer(value):
    if value is None or isinstance(value, int):
        return True
    else:
        try:
            int(value)
            return True
        except:
            return False
        
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
    