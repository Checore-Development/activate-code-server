from . import backends

class database():
    def __init__(self, *args, **kwargs):
        self.database_engine = kwargs.get('database_engine')
        
        if self.database_engine == 'sqlite3':
            self.database = backends.sqlite3(*args, **kwargs)
            
        elif self.database_engine == 'mysql':
            self.database = backends.mysql(*args, **kwargs)
            
        elif self.database_engine == 'postgresql':
            self.database = backends.postgresql(*args, **kwargs)
            
        elif self.database_engine == 'mongodb':
            self.database = backends.mongodb(*args, **kwargs)
            
        else:
            pass