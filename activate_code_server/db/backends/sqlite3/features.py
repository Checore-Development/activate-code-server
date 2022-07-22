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
    INSERT INTO %(table)s VALUES (%(placeholder)s)
'''

sql_select = '''\
    SELECT * FROM %(table)s WHERE %(variable)s = ?
'''

sql_update = '''\
    UPDATE %(table)s SET %(variables)s WHERE %(keyword)s = ?
'''

sql_delete = '''\
    DELETE FROM "%s"
    WHERE TOKEN = ?
'''
