import sqlite3

miConexion = sqlite3.connect('db_prodctos')
miCursor = miConexion.cursor()

#-----------------------------------------ELIMINACIÓN DE REGISTRO-----------------------------
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=2")


miConexion.commit()
miConexion.close()