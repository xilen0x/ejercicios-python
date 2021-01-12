#CREACION DE ARCHIVO BINARIO
import pickle

lista_nombres = ['Pedro','Ana','María','Isabel'] #datos

binario = open('lista_nombres', 'wb') #abrimos el archivo y le indicamos la lista q le pasaremos luego. wb = escritura/binaria

pickle.dump(lista_nombres, binario) # volcamos los datos en la variable binario

binario.close() #cerramos el fichero

del (binario) # para borrarlo de memoria - opcional