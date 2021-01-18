import sqlite3

miConexion = sqlite3.connect('db_prodctos')
miCursor = miConexion.cursor()

#-----------------------------------------SELECIÓN DE REGISTRO-----------------------------
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Deportes'")
resultado = miCursor.fetchall() # Esta y el sig.print es solo para ver en la terminal.
print(resultado)

miConexion.commit()
miConexion.close()