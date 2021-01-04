autores = {'libro1':'Mario Vargas Llosa',
           'libro2':'Isabel Allende',
           'libro3':'Enrique Lafourcade'}

#para recorrer e imprimir todas las claves:
for e in autores:
    print(e)
#para imprimir todas las claves:
print(autores.keys())

# para imprimir el valor de libro1, tenemos dos maneras:
print(autores['libro1'])
print(autores.get('libro1'))

#para imprimir todos los valores:
print(autores.values())

#para limpiar un diccionario:
#autores.clear()

#para copiar un diccionario:
nuevo_diccionario = autores.copy()
print(nuevo_diccionario)

#actualizar el segundo elemento del diccionario "autores" con el contenido de otro_diccionario:
otro_diccionario = {'libro2':'Desconocido'}
autores.update(otro_diccionario)
print(autores)
#---------------------------------Otro ejempplo--------------------------------------
mi_diccionario = {
    "nombre":"Carlos",
    "apellido":"Astorga",
    "ciudad":"Copiapó",
}
print(mi_diccionario)

mi_diccionario["sexo"]="Hombre"
print(mi_diccionario)

del mi_diccionario["sexo"]
print(mi_diccionario)

#---IMPRIMIR LA LONGITUD DEL DICCIONARIO CON LEN:

print(len(mi_diccionario))