from flask import request

def verify_request(func):
    def wrapper(*args, **kwargs):
        server = args[0].server
        
        if server.authorization:
            authorization = request.headers.get('Authorization')
            
            if authorization is None:
                return server.status.HTTP_401_UNAUTHORIZED
            elif authorization != server.authorization:
                return server.status.HTTP_403_FORBIDDEN
            else:
                pass
                    
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper