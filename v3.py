import sql
import re
import time
import serial

database_name = "datos_serial.db"
_port='/dev/ttyUSB0'
_baud_rate = 9600
_timeout = 1

if __name__ == "__main__":
    my_sql_db = sql.my_db_class(database_name)
    my_sql_db.set_tablename("datos")
    my_sql_db.create_table_name()

    # Inicializar puerto COM
    serial_port = serial.Serial(_port,_baud_rate, timeout = _timeout)
    try:
        while True:           
            data = serial_port.readline()
            if not data:
                time.sleep(0.1)
                continue
            data = data.decode()
            mensaje = data.split("\r")
            print(mensaje)

    except Exception as e:
        print(f"Error en main = {e}")

    except KeyboardInterrupt:
        print("Lectura de datos seriales detenida.")

    finally:
        serial_port.close()
        # Cerrar la conexión a la base de datos
        my_sql_db.close()






