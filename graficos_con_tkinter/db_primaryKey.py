import sqlite3

miConexion = sqlite3.connect('db_prodctos')
miCursor = miConexion.cursor()

#-----------------------------------------USO DE PRIMARY KEY AND UNIQUE-----------------------------
#CON UNIQUE EVITAMOS QUE SE REPITA EL NOMBRE DEL PRODUCTO (NO ES LLAVE PRIMARIA)
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')

productosNuevos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Hogar"),
    ("Camión", 30, "Juguetería")
]

miCursor.executemany('INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)', productosNuevos)

miConexion.commit()
miConexion.close()