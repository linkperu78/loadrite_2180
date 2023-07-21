import sql
database_name = "datos_serial.db"
my_db = sql.my_db_class(database_name)
my_db.set_tablename("datos")
my_db.create_table_name()
#my_db.delete_table()
