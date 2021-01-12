#RECUPERAR ARCHIVO BINARIO Y LEERLO
import pickle


fichero = open('lista_nombres', 'rb') #abrimos el archivo lista_nombres. rb = lectura/binaria

lista = pickle.load(fichero)

fichero.close() #cerramos el fichero

print(lista)