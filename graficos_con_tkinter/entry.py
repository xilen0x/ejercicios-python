from tkinter import *

root = Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

# Utilizamos la grilla para ubicar los elementos de forma correcta
# Cuadros de texto o entry
entryNombre = Entry(miFrame)
entryNombre.grid(row=0, column=1, padx=10, pady=10)# pad* es el padding 
entryNombre.config(fg="red") #color de fuente rojo
entryPass = Entry(miFrame)
entryPass.grid(row=1, column=1, padx=10, pady=10)
entryPass.config(show="*") # para reemplazar el password por asteriscos

entryDireccion = Entry(miFrame)
entryDireccion.grid(row=2, column=1, padx=10, pady=10)
#Agregamos los Labels-------------------------------------------:
labelNombre = Label(miFrame, text="Nombre: ")
labelNombre.grid(row=0, column=0, sticky="e") # sticky se utliza para alinear, en este caso el label, a la derecha o este(e)...otras opciones: n, s, e, w, ne, nw, se, sw

labelPass = Label(miFrame, text="Password: ")
labelPass.grid(row=1, column=0, sticky="e") 

labelDireccion = Label(miFrame, text="Dirección: ")
labelDireccion.grid(row=2, column=0, sticky="e") 

root.mainloop()