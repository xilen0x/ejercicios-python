from tkinter import *

root = Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

# Utilizamos la grilla para ubicar los elementos de forma correcta
# -------------------------------------------Cuadros de texto o entry-------------------------------------------:
#entryNombre = Entry(miFrame)
miNombre=StringVar()#con estas dos lineas(10, 11) asociamos el campo de texto con la variable miNombre
entryNombre = Entry(miFrame, textvariable=miNombre)
entryNombre.grid(row=0, column=1, padx=10, pady=10)# pad* es el padding 
entryNombre.config(fg="red") #color de fuente rojo

entryDireccion = Entry(miFrame)
entryDireccion.grid(row=2, column=1, padx=10, pady=10)


#-------------------------------------------Agregamos el campo Text para los comentarios:
entryComentarios = Text(miFrame, width=60, height=10)
entryComentarios.grid(row=1, column=1, padx=10, pady=10)
#-------------------------------------------Agregamos el campo Scrollbar para la barra de scroll:
scrollVert = Scrollbar(miFrame, command=entryComentarios.yview)#Para agregar el scroll(solo botones extremos)
scrollVert.grid(row=1, column=2, sticky="nsew") #Para agregar el boton medio del scroll
entryComentarios.config(yscrollcommand=scrollVert.set)#para q el boton medio del scroll se mueva coherentemente con la posición del cursor o texto.

#-------------------------------------------Agregamos los Labels-------------------------------------------:
labelNombre = Label(miFrame, text="Nombre: ")
labelNombre.grid(row=0, column=0, sticky="e") # sticky se utliza para alinear, en este caso el label, a la derecha o este(e)...otras opciones: n, s, e, w, ne, nw, se, sw

labelDireccion = Label(miFrame, text="Dirección: ")
labelDireccion.grid(row=2, column=0, sticky="e") 

labelComentarios = Label(miFrame, text="Comentarios: ")
labelComentarios.grid(row=1, column=0, sticky="e") 

#-------------------------------------------Agregamos una función y un botón con Button(root, text="textoCualquiera")--:
def codigoBoton():#función que inserta "Carlos" cuando se presiona el botón.
    miNombre.set("Carlos")


botonEnviar = Button(root, text="Enviar", command=codigoBoton) #codigoBoton es una funcion q crearemos.
botonEnviar.pack()






root.mainloop()