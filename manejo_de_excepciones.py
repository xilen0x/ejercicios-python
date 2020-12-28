lista = [22,55,100]

try:
    print(lista[2]) #para este ej. podemos cambiar el indice por un valor que no exista para ver el manejo del error.
except IndexError:
    print("Error de índice!")
else: #opcional
    print("Todo ok!")
finally: #opcional - finally siempre se va a ejecutar 
    print("Finalmente")

#-------------------------------------------------------------#
print("----------------------------------------------------")
#-------------------------------------------------------------#

class MiError(Exception):
    def __init__(self,x):
        print("Este fue el valor: ",x)

try:
    raise MiError(999)
except MiError:
    print("Error tipo MiError")