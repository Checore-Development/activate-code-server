import sqlite3 as _sqlite3

from .features import *
from .schema import schema
from .operations import operations

table = [
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
        self.table = table
        self.setup_db()
        self.setup_table()
        super().__init__(db=self.db, table=table, *args, **kwargs)
        
    def setup_db(self):
        self.db = _sqlite3.connect(f'{self.database_filename}.db')
        
    def setup_table(self):
        cursor = self.db.cursor()
        cursor.execute(sql_create_table % self.database_name)
        cursor.close()
        
    def setup_columns(self):
        cursor = self.db.cursor()
        cursor.execute(sql_create_columns % self.database_name)