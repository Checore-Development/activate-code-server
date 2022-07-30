import base64 as _base64

from ..utils import *

class base64:
    def __init__(self, *args, **kwargs):
        self.token = args[0]
        
    @property
    def encode(self):
        code = bytes_conversion(self.token)
        base64_encode = _base64.b64encode(code)
        return base64_encode.decode()
    
    @property
    def decode(self):
        base64_decode = _base64.b64decode(self.token)
        code = bytes_conversion(base64_decode)
        return code