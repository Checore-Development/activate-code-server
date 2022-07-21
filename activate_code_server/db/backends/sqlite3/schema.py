from .features import *

class schema(object):
    def __init__(self, *args, **kwargs):
        self.db = kwargs.get('db')
        self.database_name = kwargs.get('database_name')
    
    @property
    def get_columns(self):
        columns = ""
        
        for table in self.tables:
            if table == self.tables[-1]:
                columns += " ".join(table)
            else:
                columns += " ".join(table) + ","
                
        return columns
    
    @property
    def get_columns_name(self):
        columns = []
        
        for table in self.tables:
            columns.append(table[0])
            
        return columns
    
    def get_column_info(self, column):
        for table in self.tables:
            if table[0] == column:
                return table
    
    def get_table_description(self):
        cursor = self.db.cursor()
        cursor.execute(sql_table_description % self.database_name)
        data = cursor.fetchall()
        
        return data