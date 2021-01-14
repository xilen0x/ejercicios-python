from tkinter import *

root=Tk()

miMenu = Menu(root)
root.config(menu=miMenu, width=300, height=300)
root.title("Ejemplo de Menú")

archivoMenu = Menu(miMenu, tearoff=0) #tearoff=0 para eliminar submenu vacío o rayitas--
archivoMenu.add_command(label="Sub-menú 1")
archivoMenu.add_command(label="Sub-menú 2")
archivoMenu.add_separator()
archivoMenu.add_command(label="Sub-menú 3")
archivoMenu.add_command(label="Sub-menú 4")


edicionMenu = Menu(miMenu)
herramientasMenu = Menu(miMenu)
ayudaMenu = Menu(miMenu)

miMenu.add_cascade(label="Archivo", menu=archivoMenu)
miMenu.add_cascade(label="Edición", menu=edicionMenu)
miMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
miMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

root.mainloop()