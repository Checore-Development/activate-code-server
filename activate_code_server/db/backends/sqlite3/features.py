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
