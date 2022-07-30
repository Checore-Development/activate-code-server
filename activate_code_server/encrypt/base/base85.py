import base64 as _base64

from ..utils import * 

class base85:
    def __init__(self, *args, **kwargs):
        self.token = args[0]
        
    @property
    def encode(self):
        code = bytes_conversion(self.token)
        base85_encode = _base64.b85encode(code)
        return base85_encode.decode()
    
    @property
    def decode(self):
        base85_decode = _base64.b85decode(self.token)
        code = bytes_conversion(base85_decode)
        return code