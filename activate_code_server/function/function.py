from .utils import *

class function(object):
    def __init__(self, *args, **kwargs):
        self.server = kwargs.get('server')
        self.database = self.server.database
        self.status = self.server.status
        self.generate = self.server.generate
        self.encrypted = self.server.encrypted
        
    def generate_code(self, *args, **kwargs):
        seed = kwargs.get('seed')
        limit = kwargs.get('limit')
        expired_date = kwargs.get('expired_date')
        
        if judgment_integer(seed) or seed is None:
            token = self.generate.token(seed=seed)
            return token
        else:
            return self.status.HTTP_400_BAD_REQUEST