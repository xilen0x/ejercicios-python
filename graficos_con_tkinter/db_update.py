import sqlite3

miConexion = sqlite3.connect('db_prodctos')
miCursor = miConexion.cursor()

#-----------------------------------------ACTUALIZACIÓN DE REGISTRO-----------------------------
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=100 WHERE NOMBRE='Camiseta'")


miConexion.commit()
miConexion.close()