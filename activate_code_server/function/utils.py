def judgment_integer(value):
    if value is None or isinstance(value, int):
        return True
    else:
        try:
            int(value)
            return True
        except:
            return False
        
def match_form(code_format, token):
    if len(code_format) != len(token):
        return False
    else:
        for code_word, token_word in zip(code_format, token):
            if code_word == "x":
                pass
            else:
                if code_word != token_word:
                    return False
        return True