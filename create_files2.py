# creacion de un archivo de texto y guardado de datos en él.
from io import open

"""  
archivo_texto = open("archivo2.txt","w")#modo escritura

archivo_texto.write("teste")

archivo_texto.close() """
 

# lectura de un archivo de texto
""" 
archivo_texto = open("archivo2.txt","r")#modo lectura
print(archivo_texto.read())
archivo_texto.seek(0) #esto devuelve el puntero a la posición 0(inicio)
print(archivo_texto.read())
 """

#Ejercicio3 - modo lectura/escritura r+
archivo_texto = open("archivo2.txt","r+")#modo lectura/escritura
lista = archivo_texto.readlines()
lista[1]=" nuevo nuevo nuevo \n" #reemplazamos la linea con indice 1 con el contenido indicado.
archivo_texto.seek(0)
archivo_texto.writelines(lista)
archivo_texto.close()