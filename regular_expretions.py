import re

#En este ej. buscamos la letra "i"
print(re.search(r"i","Lorem Ipsum is simply dummy text of the printing and typesetting industry."))

#Busqueda de un patron
patron = re.compile(r"\d\d") #busqueda de dos dígitos
print(patron.search("Lorem Ip55sum is simply8 dummy text of554 the printing and 11 typesetting industry."))