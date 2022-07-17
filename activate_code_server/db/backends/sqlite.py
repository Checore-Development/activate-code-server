import sqlite3

sql_create_table = '''\
    CREATE TABLE IF NOT EXISTS "%s" (
        TOKEN TEXT NO NULL PRIMARY KEY,
        USAGE_COUNT INTEGER NOT NULL,
        LIMIT_COUNT INTEGER NOT NULL,
        CREATE_DATE INTEGER NOT NULL,
        EXPIRATION_DATE INTEGER NOT NULL
    )
'''

sql_insert = '''\
    INSERT INTO "%s" 
        (TOKEN, USAGE_COUNT, LIMIT_COUNT, CREATE_DATE, EXPIRATION_DATE)
        VALUES (?, ?, ?, ?, ?)
'''

sql_select = '''\
    SLECT * FROM "%s" WHERE TOKEN = ?
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
    
    def insert(self, *args, **kwargs):
        token = kwargs.get('token')
        limit = kwargs.get('limit', 1)
        create_date = kwargs.get('create_date')
        expiration_date = kwargs.get('expiration_date')
        
        cursor = self.db.cursor()
        cursor.execute(sql_insert % self.database_name, (token, 0, limit, create_date, expiration_date,))
        self.db.commit()
        cursor.close()
        
    def select(self, *args, **kwargs):
        token = kwargs.get('token')
        
        cursor = self.db.cursor()
        cursor.execute(sql_select % self.database_name, (token,))
        data = cursor.fetchall()
        cursor.close()
        return data