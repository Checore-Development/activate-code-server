import time

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
        create_date = kwargs.get('create_date', int(time.time()))
        expired_date = kwargs.get('expired_date', 2592000)
        encrypted = kwargs.get('encrypted', 'False')
        
        parameter = (_id, token, usage, limit, create_date, expired_date, encrypted)
        placeholder = ", ".join(["?"] * len(parameter))
        
        cursor = self.db.cursor()
        cursor.execute(sql_insert % {
            'table': self.database_name,
            'placeholder': placeholder
            }, parameter
        )
        self.db.commit()
        cursor.close()
        
        return parameter
        
    def select(self, *args, **kwargs):
        _id = kwargs.get('id', None)
        token = kwargs.get('token', None)
        
        if _id is not None:
            variable = 'ID'
            parameter = (_id,)
        else:
            variable = 'TOKEN'
            parameter = (token,)
            
        cursor = self.db.cursor()
        cursor.execute(sql_select % {
            'table': self.database_name,
            'variable': variable
            }, parameter
        )
        data = cursor.fetchone()
        cursor.close()
        
        return data
    
    def update(self, *args, **kwargs):
        _id = kwargs.get('id', None)
        token = kwargs.get('token', None)
        
        if _id is not None:
            detail = self.select(id=_id)
            keyword = 'ID'
            parameter_keyword = (_id,)
        else:
            detail = self.select(token=token)
            keyword = 'TOKEN'
            parameter_keyword = (token,)
            
        usage = kwargs.get('usage_count', detail[2] + 1)
        limit = kwargs.get('limit', detail[3])
        create_date = kwargs.get('create_date', detail[4])
        expired_date = kwargs.get('expired_date', detail[5])
        encrypted = kwargs.get('encrypted', detail[6])
        
        parameter = (usage, limit, create_date, expired_date, encrypted) + (parameter_keyword)
        variables = ", ".join(['%s=?' % k for k in self.get_columns_name[2:]])
    
        cursor = self.db.cursor()
        cursor.execute(sql_update % {
            'table' :self.database_name,
            'variables' : variables,
            'keyword' : keyword
            }, parameter
        )
        self.db.commit()
        cursor.close()
    
    def delete(self, *args, **kwargs):
        _id = kwargs.get('id', None)
        token = kwargs.get('token', None)
        
        if _id is not None:
            keyword = 'ID'
            parameter_keyword = (_id,)
        else:
            keyword = 'TOKEN'
            parameter_keyword = (token,)
        
        cursor = self.db.cursor()
        cursor.execute(sql_delete % {
            'table': self.database_name,
            'keyword': keyword
            }, parameter_keyword
        )
        self.db.commit()
        cursor.close()