from tkinter import *

raiz = Tk()

#Titulo de la ventana
raiz.title("Soy el título de la ventana")

#Para fijar el tamaño, lo hacemos con el método resizable y las propiedades width y height
#raiz.resizable(0,0) #--> No es posible redimencionar
#raiz.resizable(1,0) #--> Es posible redimencionar solo el ancho
#raiz.resizable(0,1) #--> Es posible redimencionar solo el alto
raiz.resizable(0,True) #--> También es posible utilizar True or False para el mismo efecto

#raiz.iconbitmap("favicon.ico") #esto para el ícono pero tiene algún error...

#Para el tamaño de la ventana:
raiz.geometry('800x500')


raiz.mainloop()