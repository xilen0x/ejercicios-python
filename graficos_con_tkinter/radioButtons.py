from tkinter import *

root = Tk()
miFrame = Frame(root, width=200, height=100)
miFrame.pack()
root.title("Radio Buttons")


varOpcion=IntVar()

def imprimirValor():
    #print(varOpcion.get())
    if varOpcion.get()==1:
        etiqueta.config(text="Elegiste Masculino!")
    else:
        etiqueta.config(text="Elegiste Femenino!")

Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimirValor).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimirValor).pack()

etiqueta=Label(root)
etiqueta.pack()












root.mainloop()