import sqlite3 as _sqlite3

from .features import *
from .schema import schema
from .operations import operations

tables = [
    ["ID", "INTEGER", "PRIMARY KEY"],
    ["TOKEN", "TEXT", "NOT NULL"],
    ["USAGE_COUNT", "INTEGER", "NOT NULL"],
    ["LIMIT_COUNT", "INTEGER", "NOT NULL"],
    ["CREATE_DATE", "INTEGER", "NOT NULL"],
    ["EXPIRATION_DATE", "INTEGER", "NOT NULL"],
    ["ENCRYPTED", "TEXT", "NOT NULL"]
]

class sqlite3(operations, schema):
    def __init__(self, *args, **kwargs):
        self.database_filename = kwargs.get('database_filename')
        self.database_name = kwargs.get('database_name')
        self.db = None
        self.tables = tables
        self.setup_db()
        self.setup_table()
        self.setup_columns()
        super().__init__(db=self.db, table=self.tables, *args, **kwargs)
        
    def setup_db(self):
        self.db = _sqlite3.connect(f'{self.database_filename}.db')
        
    def setup_table(self):
        cursor = self.db.cursor()
        cursor.execute(sql_create_table % {
            'table': self.database_name,
            'columns': self.get_columns
            }
        )
        cursor.close()
        
    def setup_columns(self):
        cursor = self.db.cursor()
        cursor.execute(sql_table_description % {
            'table': self.database_name
            }
        )
        table_description = cursor.fetchall()
        table_description_name = [x[1] for x in table_description]
        
        for column in self.get_columns_name:
            if column not in table_description_name:
                column_info = self.get_column_info(column)
                
                cursor.execute(sql_alter_table % {
                    'table': self.database_name,
                    'column': column_info[0],
                    'type': column_info[1],
                    'null': column_info[2]
                    }
                )
                self.db.commit()
            else:
                pass
            
        cursor.close()