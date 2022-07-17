import sqlite3

sql_create_table = '''\
CREATE TABLE IF NOT EXISTS "%s"(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TOKEN TEXT NOT NULL,
    USAGE_COUNT INTEGER,
    LIMIT_COUNT INTEGER NOT NULL,
    CREATE_DATE INTEGER NOT NULL,
    EXPIRATION_DATE INTEGER NOT NULL
    )
'''

class sqlite():
    def __init__(self, *args, **kwargs):
        self.database_filename = kwargs.get('database_filename')
        self.database_name = kwargs.get('database_name')
        self.db = None
        self.setup_db()
        self.setup_table()
        
    def setup_db(self):
        self.db = sqlite3.connect(f'{self.database_filename}.db')
        
    def setup_table(self):
        cursor = self.db.cursor()
        cursor.execute(sql_create_table % self.database_name)
        cursor.close()
        