import sqlite3

__all__ = ['sqlite']

sql_create_table = '''\
    CREATE TABLE IF NOT EXISTS "%s" (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TOKEN TEXT NOT NULL,
        USAGE_COUNT INTEGER NOT NULL,
        LIMIT_COUNT INTEGER NOT NULL,
        CREATE_DATE INTEGER NOT NULL,
        EXPIRATION_DATE INTEGER NOT NULL,
        ENCRYPTED TEXT NOT NULL
    )
'''

sql_insert = '''\
    INSERT INTO "%s" (TOKEN, USAGE_COUNT, LIMIT_COUNT, CREATE_DATE, EXPIRATION_DATE)
    VALUES (?, ?, ?, ?, ?)
'''

sql_select = '''\
    SELECT * 
    FROM "%s" 
    WHERE TOKEN = ?
'''

sql_update = '''\
    UPDATE "%s" 
    SET USAGE_COUNT = ?, LIMIT_COUNT = ?, CREATE_DATE = ?, EXPIRATION_DATE = ?
    WHERE TOKEN = ?
'''

sql_delete = '''\
    DELETE FROM "%s"
    WHERE TOKEN = ?
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
        usage = kwargs.get('usage_count', 0)
        limit = kwargs.get('limit', 1)
        create_date = kwargs.get('create_date')
        expiration_date = kwargs.get('expiration_date')
        
        cursor = self.db.cursor()
        cursor.execute(sql_insert % self.database_name, (token, usage, limit, create_date, expiration_date,))
        self.db.commit()
        cursor.close()
        
    def select(self, *args, **kwargs):
        token = kwargs.get('token')
        
        cursor = self.db.cursor()
        cursor.execute(sql_select % self.database_name, (token,))
        data = cursor.fetchall()
        cursor.close()
        return data[0]
    
    def update(self, *args, **kwargs):
        token = kwargs.get('token')
        detail = self.select(token=token)
        usage = kwargs.get('usage_count', detail['usage_count'] + 1)
        limit = kwargs.get('limit', detail['limit_count'])
        create_date = kwargs.get('create_date', detail['create_date'])
        expiration_date = kwargs.get('expiration_date', detail['expiration_date'])
        
        cursor = self.db.cursor()
        cursor.execute(sql_update % self.database_name, (usage, limit, create_date, expiration_date, token))
        self.db.commit()
        cursor.close()
    
    def delete(self, *args, **kwargs):
        token = kwargs.get('token')
        
        cursor = self.db.cursor()
        cursor.execute(sql_delete % self.database_name, (token,))
        self.db.commit()
        cursor.close()
        