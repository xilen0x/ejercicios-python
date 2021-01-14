from tkinter import *
from tkinter import filedialog

root=Tk()
miFrame = Frame(root, width=300, height=300)
miFrame.pack()


root.title("Ejemplo de Buscar Archivo")
#-----------------------------Funciones:-------------------------------------
def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="~/Documents", filetypes=(("Planillas de Cálculo", "*ods"),("Documentos de Texto", "*.txt"),("Ver todo","*.*")))
    print(fichero) # esto imprimirá en consola la ruta del archivo

Button(miFrame, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()