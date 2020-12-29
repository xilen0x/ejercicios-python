#Auditoría SEO

import urllib.request as request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

print("Auditoría al site 'python.org'")

#---------- Verificación del https y www----------#
req = request.Request('http://python.org')
resultado = request.urlopen(req)
print("Resultado: ", resultado.geturl())

#---------- Peso de la página ----------#
url = "https://python.org"
print("URL: ", url)
site = request.urlopen(url)
meta = site.info()
print("Content-Length: ", site.headers['content-length'])

#---------- Verificar description ----------#
site = request.urlopen('https://python.org')
soup = BeautifulSoup(site, "html.parser")
description = soup.find('meta', attrs={'name': 'description'})
print('El tamaño de la description de python.org es: ',
      len(description.get('content')))
if (len(description.get('content'))) < 154:
    print("La descripción es menor a 154")

#---------- Verificar etiqueta titulo ----------#
html = urlopen('https://python.org')
soup = BeautifulSoup(html.read(), "html.parser")
print("El tamaño del title es: ", len(soup.html.head.title.string))
print("y dice: ", soup.html.head.title.string)

#---------- Obtener las Palabras clave del sitio ----------#
site = request.urlopen('https://python.org')
soup = BeautifulSoup(site, "html.parser")
keywords = soup.find('meta', attrs={'name': 'keywords'})
print('Keywords: ', keywords.get('content'))
words = keywords.get('content').split()
print(words)
for word in words:
    print(word, len(soup.findAll(text=re.compile(word))))

#---------- Obtener el texto alternativo de las imágenes del sitio ----------#
site = request.urlopen('https://python.org')
soup = BeautifulSoup(site, "html.parser")
count = 1
for image in soup.findAll('img'):
    print('imagen #1: ', count, ':', image["src"])
    print("Alt. de la imagen: ", count, ':', image.get('alt', 'None'))
    count += 1
