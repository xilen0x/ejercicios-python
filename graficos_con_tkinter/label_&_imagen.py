from tkinter import *

root = Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

#Para ingresar un texto en el frame creado:
miLabel = Label(miFrame, text="Primera etiqueta", fg="red", font=(18))
miLabel.place(x=50, y=200)  #esto para ubicarlo en posición.

#Para insertar una imagen:
miImagen = PhotoImage(file="web.png")
Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()