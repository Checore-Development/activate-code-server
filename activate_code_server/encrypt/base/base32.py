import base64 as _base64

from ..utils import *

class base32:
    def __init__(self, *args, **kwargs):
        self.token = args[0]
        
    @property
    def encode(self):
        code = bytes_conversion(self.token)
        base32_encode = _base64.b32encode(code)
        return base32_encode.decode()
    
    @property
    def decode(self):
        base32_decode = _base64.b32decode(self.token)
        code = bytes_conversion(base32_decode)
        return code