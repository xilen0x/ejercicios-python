#leer información de un archivo json

import json

with open('archivo.json') as file:
    dato = json.load(file)
print(dato)

print(dato['nombres'][0])

print(dato['nombres'][1])

print(dato ['nombres'][0]['apellido'])