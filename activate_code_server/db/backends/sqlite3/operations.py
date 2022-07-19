from .features import *

class operations(object):
    def __init__(self, *args, **kwargs):
        self.db = kwargs.get('db')
        self.database_name = kwargs.get('database_name')

    def insert(self, *args, **kwargs):
        _id = kwargs.get('id')
        token = kwargs.get('token')
        usage = kwargs.get('usage_count', 0)
        limit = kwargs.get('limit', 1)
        create_date = kwargs.get('create_date')
        expiration_date = kwargs.get('expiration_date')
        
        cursor = self.db.cursor()
        cursor.execute(sql_insert % (self.database_name, _id, token, usage, limit, create_date, expiration_date,))
        self.db.commit()
        cursor.close()
        
    def select(self, *args, **kwargs):
        token = kwargs.get('token')
        
        cursor = self.db.cursor()
        cursor.execute(sql_select % self.database_name, (token,))
        data = cursor.fetchall()
        cursor.close()
        return data[0]
    
    def update(self, *args, **kwargs):
        token = kwargs.get('token')
        detail = self.select(token=token)
        usage = kwargs.get('usage_count', detail['usage_count'] + 1)
        limit = kwargs.get('limit', detail['limit_count'])
        create_date = kwargs.get('create_date', detail['create_date'])
        expiration_date = kwargs.get('expiration_date', detail['expiration_date'])
        
        cursor = self.db.cursor()
        cursor.execute(sql_update % self.database_name, (usage, limit, create_date, expiration_date, token))
        self.db.commit()
        cursor.close()
    
    def delete(self, *args, **kwargs):
        token = kwargs.get('token')
        
        cursor = self.db.cursor()
        cursor.execute(sql_delete % self.database_name, (token,))
        self.db.commit()
        cursor.close()