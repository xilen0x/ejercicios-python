from tkinter import *
from tkinter import messagebox

root = Tk()
miMenu = Menu(root)
root.config(menu = miMenu)
miFrame = Frame(root)
miFrame.pack()
root.geometry('500x400')
root.resizable(0,0)
root.title("My CRUD in Python")
#-----------------------------Funciones:-------------------------------------
def ventanaEmergenteInfo():
    messagebox.showinfo("titulo ventana","Mensaje de Información")
def ventanaEmergenteWarn():
    messagebox.showwarning("titulo ventana","Mensaje de advertencia")
def salir():
    valor = messagebox.askquestion("Salir", "Estas segurod e salir?")
    if valor == "yes":
        root.destroy()


#-----------------------------SUBMENUS:-------------------------------------
conectarDB = Menu(miMenu, tearoff=0) #tearoff=0 para eliminar submenu vacío o rayitas--
conectarDB.add_command(label="Salir", command=salir)


limpiarMenu = Menu(miMenu, tearoff=0)


ayudaMenu = Menu(miMenu, tearoff=0)
ayudaMenu.add_command(label="Ventana Emergente Info", command=ventanaEmergenteInfo)
ayudaMenu.add_command(label="Ventana Emergente Warning", command=ventanaEmergenteWarn)

#-----------------------------MENÚ PRINCIPAL:-------------------------------------
miMenu.add_cascade(label="Conectar DB", menu=conectarDB)
miMenu.add_cascade(label="Limpiar Formulario", menu=limpiarMenu)
miMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#---------------------Entries------------------------------------------:
entryID = Entry(miFrame)
entryID.grid(row=0, column=1, padx=20, pady=10)
entryID.config(fg="red") 

entryNombre = Entry(miFrame)
entryNombre.grid(row=1, column=1, padx=10, pady=10)

entryPass = Entry(miFrame)
entryPass.grid(row=2, column=1, padx=10, pady=10)
entryPass.config(show="*") # para reemplazar el password por asteriscos

entryDireccion = Entry(miFrame)
entryDireccion.grid(row=3, column=1, padx=10, pady=10)
#----------------------Labels-------------------------------------------:
labelID= Label(miFrame, text="ID: ")
labelID.grid(row=0, column=0, sticky="e")

labelNombre = Label(miFrame, text="Nombre: ")
labelNombre.grid(row=1, column=0, sticky="e") # sticky se utliza para alinear, en este caso el label, a la derecha o este(e)...otras opciones: n, s, e, w, ne, nw, se, sw

labelPass = Label(miFrame, text="Password: ")
labelPass.grid(row=2, column=0, sticky="e") 

labelDireccion = Label(miFrame, text="Dirección: ")
labelDireccion.grid(row=3, column=0, sticky="e") 

#----------------------Buttons CRUD-------------------------------------------:
#------CREAR--------
def createData():
    ventanaEmergenteInfo()

botonCrear = Button(root, text="Guardar", command=createData) #codigoBoton es una funcion
botonCrear.pack()

#------LEER--------
def readData():
    ventanaEmergenteInfo()

botonLeer = Button(root, text="Listar", command=readData)
botonLeer.pack()

#------ACTUALIZAR--------
def updateData():
    ventanaEmergenteInfo()

botonActualizar = Button(root, text="Actualizar", command=updateData)
botonActualizar.pack()

#------BORRAR--------
def deleteData():
    ventanaEmergenteInfo()

botonBorrar = Button(root, text="Borrar", command=deleteData) #codigoBoton es una funcion
botonBorrar.pack()

root.mainloop()