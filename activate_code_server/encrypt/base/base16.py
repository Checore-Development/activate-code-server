import base64 as _base64

from ..utils import * 
    
class base16:
    def __init__(self, *args, **kwargs):
        self.token = args[0]
        
    @property
    def encode(self):
        code = bytes_conversion(self.token)
        base16_encode = _base64.b16encode(code)
        return base16_encode.decode()
    
    @property
    def decode(self):
        base16_decode = _base64.b16decode(self.token)
        code = bytes_conversion(base16_decode)
        return code