sql_create_table = '''\
    CREATE TABLE IF NOT EXISTS %(table)s (%(columns)s);
'''

sql_table_description = '''\
    PRAGMA TABLE_INFO(%(table)s);
'''

sql_alter_table = '''\
    ALTER TABLE %(table)s ADD COLUMN %(column)s %(type)s %(null)s;
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
