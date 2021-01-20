import re

"""#--------------- ---------------En este ej. buscamos la letra "i"--------------------------
print(re.search(r"i","Lorem Ipsum is simply dummy text of the printing and typesetting industry."))

#Busqueda de un patron
patron = re.compile(r"\d\d") #busqueda de dos dígitos
print(patron.search("Lorem Ip55sum is simply8 dummy text of554 the printing and 11 typesetting industry.")) """

#--------------------------------------En este ej. buscamos una palabra x --------------------
""" texto_a_buscar=input("Ingresa la palabra a buscar: ")

cadena = "Este es un ejemplo de párrafo para trabajar con expresiones regulares"

if re.search(texto_a_buscar, cadena) != None:
    print("El texto '"+ texto_a_buscar + "' fue encontrado!")
else:
    print("El texto '"+ texto_a_buscar + "' no fue encontrado!")
     """
#-----------------------------------Ejemplos con start end y span---------------------------------
""" texto_a_buscar=input("Ingresa la palabra a buscar: ")

cadena = "Este es un ejemplo de párrafo para trabajar con expresiones regulares"

texto = re.search(texto_a_buscar, cadena)
#si queremos saber donde comienza el texto encontrado:
print(texto.start())
#si queremos saber donde termina el texto encontrado:
print(texto.end())
#si queremos saber donde inicia y termina el texto encontrado:
print(texto.span())
 """
#--------------------------------Búsqueda de veces q se repite una palabra en una cadena------------------------------
"""cadena = "Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:"
texto_a_buscar=input("Ingresa la palabra a buscar: ")
print(len(re.findall(texto_a_buscar, cadena)))
"""
#--------------------------------Buscar todas las coincidencias en una lista ------------------------------------
"""lista_nombres=['Rosa','Karina Villegas','Carolina','Gabriela','Paula O','Pierina','PiPian','Elielma','Mónica','Paula G','Jerusa Villegas','Evelin','Paulina']
#que comiencen por:
for e in lista_nombres:
    if re.findall('^Pa*', e): #por lo visto se requieren al menos dos caracteres para buscar las coincidecias. En este caso se imprimen todos los nombres q comiencen con "p" y que contengan además la letra "a".
        print(e)

#que terminen con:
for e in lista_nombres:
    if re.findall('Villegas$', e):
        print(e)

#que contengan la ñ:
personas = ['niños','niñas','hombres','mujeres']
for e in personas:
    if re.findall('[ñ]', e): # en el caso de buscar camion y camión podemos hacer: [ćami[oó]n]
        print(e)
"""
#--------------------------------Buscar un rango de datos ------------------------------------
"""codigo_ciudades = ['MAD1','BCN1','MAD2','MAD3','BCN7','MAD4','BCN6','MAD5','MUR5','BCN4','BCN5','MUR4','MAD6','MUR2','BCN3','MAD7','MUR1','MUR3','BCN2']

for e in codigo_ciudades:
    #if re.findall('BCN',e):#imprime todos las coincidencias con 'BCN'
       # print(e)
    if re.findall('MAD[3-6]',e):#imprime todos las coincidencias con 'MAD' en el rango del 3 al 6
        print(e)
"""
#--------------------------------Buscar con la funcion match ------------------------------------

codigo1= "BCN5"
codigo2= "BCN6"
codigo3= "bcn5"

""" if re.match("BCN5", codigo1):
    print("Valor encontrado")
else:
    print("Valor no encontrado") """

if re.match("BCN5", codigo3, re.IGNORECASE): #lo mismo pero sin importar si esta con minuscula o mayusculas.
    print("Valor encontrado")
else:
    print("Valor no encontrado") 
