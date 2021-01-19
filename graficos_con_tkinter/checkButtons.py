from tkinter import *

root = Tk()
root.title("Check Buttons")

miFrame = Frame(root, width=200, height=100)
miFrame.pack()

varOpcion=IntVar()

#variables que almacenan lo seleccionado
playa = IntVar()
montana = IntVar()
bosque = IntVar()

#funcion opciones
def opciones():
    opcionEscogida = ""
    if (playa.get()==1):
        opcionEscogida+=" playa"
    
    if (montana.get()==1):
        opcionEscogida+=" montaña"
    
    if (bosque.get()==1):
        opcionEscogida+=" bosque"

    textoFinal.config(text=opcionEscogida)

#Imagen
""" foto = PhotoImage(file="playa.png")
Label(root, image=foto).pack() """

#Label
Label(miFrame, text="Escoja un destino o ḿas de uno:").pack()

#opciones
Checkbutton(miFrame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(miFrame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(miFrame, text="Bosque", variable=bosque, onvalue=1, offvalue=0, command=opciones).pack()

textoFinal = Label(miFrame)
textoFinal.pack()


root.mainloop()