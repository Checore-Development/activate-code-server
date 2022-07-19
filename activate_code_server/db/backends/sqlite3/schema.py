from .features import *

class schema(object):
    def __init__(self, *args, **kwargs):
        self.db = kwargs.get('db')
        self.database_name = kwargs.get('database_name')
        
    def get_table_description(self):
        cursor = self.db.cursor()
        cursor.execute(sql_table_description % self.database_name)
        data = cursor.fetchall()