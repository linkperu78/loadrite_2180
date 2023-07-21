import sqlite3
import re

LINUX_STATUS = False

if LINUX_STATUS:
    import serial

# Crear o conectar a la base de datos
db_connection = sqlite3.connect('/datos_serial.db')
db_cursor = db_connection.cursor()

# Agregar la columna 'fecha' a la tabla 'datos' si no existe
try:
    db_cursor.execute('ALTER TABLE datos ADD COLUMN fecha TEXT')
except sqlite3.OperationalError as e:
    # Si la columna ya existe, no hacer nada
    pass

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

def guardar_en_base_de_datos(linea, fecha):
    # Guardar la línea y fecha en la base de datos
    db_cursor.execute('INSERT INTO datos (linea, fecha) VALUES (?, ?)', (linea, fecha))
    db_connection.commit()

try:
    while True:
        # Leer la línea de datos desde el puerto serie
        if LINUX_STATUS:
            linea_datos = puerto_serie.readline().decode('utf-8')
        else:
            linea_datos = "ID777\rTM16:18:35\rDT20 JUL 23\rSP1 Mineral\r" \
                          "U1 Limpieza\rU3 V3\rAD4 2.32\rE\r"

        # Imprimir la línea de datos recibida
        print("Datos recibidos:", linea_datos)

        # Buscar el patrón "TM" seguido de la fecha y hora correspondiente
        patron = r'TM(\d{2}:\d{2}:\d{2})\rDT(\d{2} [A-Z]{3} \d{2})'
        coincidencias = re.findall(patron, linea_datos)

        # Si se encontró una coincidencia, guardar la fecha en la base de datos
        if coincidencias:
            fecha_tm, fecha_dt = coincidencias[0]
            fecha_completa = fecha_dt + " " + fecha_tm
            guardar_en_base_de_datos(linea_datos, fecha_completa)

except KeyboardInterrupt:
    # Capturar la interrupción con Ctrl + C
    print("Lectura de datos seriales detenida.")

finally:
    # Cerrar la conexión del puerto serie
    if LINUX_STATUS:
        puerto_serie.close()

    # Cerrar la conexión a la base de datos
    db_connection.close()

