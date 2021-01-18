import sqlite3

# ------Abrir Conexión y crear la DB--------------------#
miConexion = sqlite3.connect("MiBase")

# Para trabajar con la DB debemos crear el cursor o puntero:
miCursor = miConexion.cursor()

#Crar la tabla productos
#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

#-----------------------------Insertar UN REGISTRO DE datos
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

#Insertar VARIOS REGISTROS DE datos
""" compras = [
    ("camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Hogar"),
    ("Camión", 30, "Juguetería")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", compras) """

#--------------------------------Listar registros:
miCursor.execute("SELECT * FROM PRODUCTOS")
misProductos = miCursor.fetchall()
#print(misProductos) o podemos hacer un for:
for e in misProductos:
    #print(e)   ó:
    #print(e[0]) #para ver en más detalle ...'o:
    print("- Artículo:", e[0], "- Precio:",e[1],"- Sección:", e[2])
#----------------------Confirmar cambios
miConexion.commit()


#Cerrar la conexión
miConexion.close()