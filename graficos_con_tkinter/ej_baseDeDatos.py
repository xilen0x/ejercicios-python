import sqlite3

# ------Crear Conexión a la DB y la DB--------------------#
miConexion = sqlite3.connect("MiBase")

# Para crear la 1a tabla debemos crear el cursor o puntero:
miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")



miConexion.close()