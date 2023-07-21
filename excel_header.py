# Excel structure
excel_columns = ["Fecha", "Origen", "Operador", "Cargadora", "Producto", 
                "Funcion", "Secuencia", "Peso", "Camion", "Actividad", "IdEmpresa"]

# SQLite
sql_columns = {
    "Cargadora"     : "INTEGER",
    "Fecha"         : "VARCHAR(30)",
    "Producto"      : "VARCHAR(20)",
    "Actividad"     : "VARCHAR(10)",
    "Camion"        : "VARCHAR(15)",
    "Funcion"       : "VARCHAR(30)",
    "Secuencia"     : "INTEGER",
    "Peso"          : "FLOAT",
}


# Diccionario para desencriptar
excel_dictionary = {
    "ID"    : "Cargadora",
    "TM"    : "Fecha",
    "SP1"   : "Producto",
    "U1"    : "Actividad",
    "U2"    : "Origen",
    "U3"    : "Volquete",
    "AD"    : "Funcion", 
}


