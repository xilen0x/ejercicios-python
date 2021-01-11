""" Podemos importar el archivo y sus funciones de varias maneras: 
import funciones_matematicas  <---------(para usar esta forma, debemos anteponer "funciones_matematicas" cada vez q utilicemos una funcion de ese archivo, por eje: funciones_matematicas.sumar(7,5))
o
from funciones_matematicas import sumar    <---(si solo queremos la funcion sumar, y al usarla: sumar(7,5))
o
from funciones_matematicas import *    <--------(si queremos importar todo del archivo funciones_matematicas.py , y al usarla: sumar(7,5))
"""

from funciones_matematicas import *

sumar(7,5)
restar(7,5)
multiplicar(7,5)