from .features import *

class schema(object):
    def __init__(self, *args, **kwargs):
        self.db = kwargs.get('db')
        self.database_name = kwargs.get('database_name')
    
    @property
    def get_columns(self):
        columns = ""
        
        for info in self.table:
            if info == self.table[-1]:
                columns += " ".join(info)
            else:
                columns += " ".join(info) + ","
                
        return columns
    
    @property
    def get_columns_name(self):
        columns = []
        
        for info in self.table:
            columns.append(info[0])
            
        return columns
    
    def get_column_info(self, column):
        for info in self.table:
            if info[0] == column:
                return info
    
    def get_table_description(self):
        cursor = self.db.cursor()
        cursor.execute(sql_table_description % self.database_name)
        data = cursor.fetchall()
        return data