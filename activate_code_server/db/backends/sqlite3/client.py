import sqlite3 as _sqlite3

from .features import *
from .operations import operations

class sqlite3(operations):
    def __init__(self, *args, **kwargs):
        self.database_filename = kwargs.get('database_filename')
        self.database_name = kwargs.get('database_name')
        self.db = None
        self.setup_db()
        self.setup_table()
        super().__init__(db=self.db, *args, **kwargs)
        
    def setup_db(self):
        self.db = _sqlite3.connect(f'{self.database_filename}.db')
        
    def setup_table(self):
        cursor = self.db.cursor()
        cursor.execute(sql_create_table % self.database_name)
        cursor.close()