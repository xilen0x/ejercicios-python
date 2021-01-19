from tkinter import *
from tkinter import messagebox
from conexion_db import *
import sqlite3

root = Tk()
miMenu = Menu(root)
root.config(menu = miMenu)
miFrame = Frame(root)
miFrame.pack()

root.geometry('500x400')
root.resizable(0,0)
root.title("My CRUD in Python")
#-----------------------------Funciones Menú:-------------------------------------
def ventanaEmergenteInfo():
    messagebox.showinfo("titulo ventana","Mensaje de Información")
def ErrorConexion():
    messagebox.showwarning("Error de conexión", "Tabla USUARIOS ya existe")
def salir():
    valor = messagebox.askquestion("Salir", "Estas seguro de salir?")
    if valor == "yes":
        root.destroy()

#----------------------------Función conexión-------------------------------------
def conexion_dataBase():
    try:        
        miConexion = sqlite3.connect("MiBase")
        miCursor = miConexion.cursor()

        miCursor.execute('''
        CREATE TABLE USUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) UNIQUE,
        PASSWORD VARCHAR(50),
        DIRECCION VARCHAR(100)
        )
        ''')

        miConexion.commit()
        miConexion.close()

    except:
        ErrorConexion()


#-----------------------------CREACIÓN DE MENUS(SUBMENUS):-------------------------------------
conectarDB = Menu(miMenu, tearoff=0) #tearoff=0 para eliminar submenu vacío o rayitas--
conectarDB.add_command(label="Conectar", command=conexion_dataBase)

limpiarMenu = Menu(miMenu, tearoff=0)
limpiarMenu.add_command(label="Limpiar campos")

ayudaMenu = Menu(miMenu, tearoff=0)
ayudaMenu.add_command(label="Ventana Emergente Info", command=ventanaEmergenteInfo)
ayudaMenu.add_command(label="Salir", command=salir)

#-----------------------------ANEXAR LOS MENÚS CREADOS A LA BARRA DE MENU: miMenu:-------------------------------------
miMenu.add_cascade(label="BBDD", menu=conectarDB)
miMenu.add_cascade(label="Limpiar Formulario", menu=limpiarMenu)
miMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#---------------------Entries------------------------------------------:
entryID = Entry(miFrame)
entryID.grid(row=0, column=1, padx=20, pady=10)
entryID.config(fg="red") 

miNombre=StringVar()
entryNombre = Entry(miFrame, textvariable=miNombre)
entryNombre.grid(row=1, column=1, padx=10, pady=10)

miPass=StringVar()
entryPass = Entry(miFrame, textvariable=miPass)
entryPass.grid(row=2, column=1, padx=10, pady=10)
entryPass.config(show="*") # para reemplazar el password por asteriscos

miDirec=StringVar()
entryDireccion = Entry(miFrame, textvariable=miDirec)
entryDireccion.grid(row=3, column=1, padx=10, pady=10)

entryComentario=Text(miFrame, width=23, height=5)
entryComentario.grid(row=4, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=entryComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")
entryComentario.config(yscrollcommand=scrollVert.set)

#----------------------Labels-------------------------------------------:
labelID= Label(miFrame, text="ID: ")
labelID.grid(row=0, column=0, sticky="e")

labelNombre = Label(miFrame, text="Nombre: ")
labelNombre.grid(row=1, column=0, sticky="e") # sticky se utliza para alinear, en este caso el label, a la derecha o este(e)...otras opciones: n, s, e, w, ne, nw, se, sw

labelPass = Label(miFrame, text="Password: ")
labelPass.grid(row=2, column=0, sticky="e") 

labelDireccion = Label(miFrame, text="Dirección: ")
labelDireccion.grid(row=3, column=0, sticky="e") 

labelComentario = Label(miFrame, text="Comentario: ")
labelComentario.grid(row=4, column=0, sticky="e") 

#------------new frame for buttons-----#
buttonFrame = Frame(root)
buttonFrame.pack()

# ---***********************--Button function-CREAR---***********************---
def createData():
    #miCursor.executemany('INSERT INTO USUARIOS VALUES(NULL,?,?,?)', miNombre, miPass, miDirec ) #AQUI VOY!!!!!!!!!!******************
    pass

botonCrear = Button(buttonFrame, text="Guardar", command=createData)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

# ---***********************--Button function-LEER---***********************---
def readData():
    ventanaEmergenteInfo()

botonLeer = Button(buttonFrame, text="Listar", command=readData)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

# ---***********************--Button function-ACTUALIZAR---***********************---
def updateData():
    ventanaEmergenteInfo()

botonActualizar = Button(buttonFrame, text="Actualizar", command=updateData)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

# ---***********************--Button function-BORRAR---***********************---
def deleteData():
    ventanaEmergenteInfo()

botonBorrar = Button(buttonFrame, text="Borrar", command=deleteData) 
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()