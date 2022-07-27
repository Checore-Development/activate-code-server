import time

from .utils import *

class function(object):
    def __init__(self, *args, **kwargs):
        self.server = args[0]
        self.database = self.server.database
        self.status = self.server.status
        self.generate = self.server.generate
        self.encrypt = self.server.encrypt
        self.encrypted = self.server.encrypt_method
        
    def generate_code(self, *args, **kwargs):
        data = args[0]
        seed = data.get('seed')
        limit = data.get('limit', 1)
        expired_date = data.get('expired_date', 2592000)
        encrypted = data.get('encrypted', 'False')
        
        if not judgment_integer(seed) or not judgment_integer(limit) or not judgment_integer(expired_date):
            return self.status.HTTP_400_BAD_REQUEST
        elif limit is not None:
            if int(limit) < 0:
                return self.status.HTTP_400_BAD_REQUEST
        elif expired_date is not None:
            if int(expired_date) < 0:
                return self.status.HTTP_400_BAD_REQUEST
        else:
            pass
        
        _id = self.generate.id
        token = self.generate.token(seed=seed)
        create_date = int(time.time())
        
        if seed is not None and self.database.select(token=token):
            return self.status.HTTP_400_BAD_REQUEST
        else:
            self.database.insert(
                id=_id, 
                token=token,
                limit=limit,
                expired_date=expired_date, 
                encrypted=self.encrypted
                )
            
        return self.status.HTTP_CUSTOM_201_CREATED(
            {"id": _id,
             "token": token,
             "limit": limit,
             "create_date": create_date,
             "expired_date": expired_date,
             "encrypted": self.encrypted
            }
        )