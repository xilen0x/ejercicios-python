#lectura de un archivo xml

from xml.etree.ElementTree import parse

doc = parse('archivo.xml')

for e in doc.findall('nombre'):
    print(e.text)
