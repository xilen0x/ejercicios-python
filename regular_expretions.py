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
cadena = "Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:"
texto_a_buscar=input("Ingresa la palabra a buscar: ")
print(len(re.findall(texto_a_buscar, cadena)))