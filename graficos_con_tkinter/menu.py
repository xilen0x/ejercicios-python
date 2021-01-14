from tkinter import *
from tkinter import messagebox

root=Tk()

miMenu = Menu(root)
root.config(menu=miMenu, width=300, height=300)
root.title("Ejemplo de Menú")
#-----------------------------Funciones:-------------------------------------
def ventanaEmergenteInfo():
    messagebox.showinfo("titulo ventana","Mensaje de Información")
def ventanaEmergenteWarn():
    messagebox.showwarning("titulo ventana","Mensaje de advertencia")
def salir():
    valor = messagebox.askquestion("Salir", "Estas segurod e salir?")
    if valor == "yes":
        root.destroy()
#-----------------------------opciones del menú:-------------------------------------
archivoMenu = Menu(miMenu, tearoff=0) #tearoff=0 para eliminar submenu vacío o rayitas--
archivoMenu.add_command(label="Sub-menú 1")
archivoMenu.add_command(label="Sub-menú 2")
archivoMenu.add_separator()
archivoMenu.add_command(label="Sub-menú 3")
archivoMenu.add_command(label="Salir", command=salir)


edicionMenu = Menu(miMenu)
#otras opciones o submenus

herramientasMenu = Menu(miMenu)
#otras opciones o submenus

ayudaMenu = Menu(miMenu, tearoff=0)
ayudaMenu.add_command(label="Ventana Emergente Info", command=ventanaEmergenteInfo)
ayudaMenu.add_command(label="Ventana Emergente Warning", command=ventanaEmergenteWarn)

miMenu.add_cascade(label="Archivo", menu=archivoMenu)
miMenu.add_cascade(label="Edición", menu=edicionMenu)
miMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
miMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

root.mainloop()