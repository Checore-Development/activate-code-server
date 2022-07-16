from . import backends

class database():
    def __init__(self, *args, **kwargs):
        self.database_engine = kwargs.get('database_engine')
        
        if self.database_engine == 'sqlite':
            self.database = backends.sqlite(*args, **kwargs)