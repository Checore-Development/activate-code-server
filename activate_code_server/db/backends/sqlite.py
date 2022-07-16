import sqlite3

class sqlite():
    def __init__(self, *args, **kwargs):
        self.database_filename = kwargs.get('database_filename')
        self.db = sqlite3.connect(f'{self.database_filename}.db')
        
    def setup(self):
        cursor = self.db.cursor()
        