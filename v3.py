import sql
import re
import time

LINUX_STATUS = False

if LINUX_STATUS:
    import serial

database_name = "datos_serial.db"

# Configurar la comunicación serial
if LINUX_STATUS:
    puerto_serie = serial.Serial(
        port='/dev/ttyUSB0',  # Reemplaza '/dev/ttyUSB0' con el nombre correcto del puerto USB
        baudrate=9600,
        bytesize=8,
        parity='N',  # N = Ninguno, E = Par, O = Impar
        stopbits=1,
        timeout=1,
    )

my_sql_db = sql.my_db_class(database_name)
my_sql_db.set_tablename("datos")
my_sql_db.create_table_name()

try:
    while True:
        # Leer la línea de datos desde el puerto serie
        if LINUX_STATUS:
            linea_datos = puerto_serie.readline().decode('utf-8')
        else:
            linea_datos = "ID777\rTM16:18:35\rDT20 JUL 23\rSP1 Mineral\r" \
                          "U1 Limpieza\rU2 Tajo1\U3 V3\rAD4 2.32\rE\r"
        if not "U1" in linea_datos and not "U2" in linea_datos:
            continue

        # Imprimir la línea de datos recibida
        print("Datos recibidos:", linea_datos)

        # Buscar el patrón "TM" seguido de la fecha y hora correspondiente
        #patron = r'TM(\d{2}:\d{2}:\d{2})\rDT(\d{2} [A-Z]{3} \d{2})'
        #coincidencias = re.findall(patron, linea_datos)
        #print(f"Valor after re = {coincidencias}")

        # Si se encontró una coincidencia, guardar la fecha en la base de datos
        #if coincidencias:
        #    fecha_tm, fecha_dt = coincidencias[0]
        #    fecha_completa = fecha_dt + " " + fecha_tm
            #my_sql_db.insert_data_in_table(linea_datos, fecha_completa)
        
        #time.sleep(2)

except KeyboardInterrupt:
    # Capturar la interrupción con Ctrl + C
    print("Lectura de datos seriales detenida.")

finally:
    # Cerrar la conexión del puerto serie
    if LINUX_STATUS:
        puerto_serie.close()
    # Cerrar la conexión a la base de datos
    my_sql_db.close()

