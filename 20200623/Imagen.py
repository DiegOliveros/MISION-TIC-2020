# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:03:20 2021

@author: diego
"""

from tkinter import *

ventana =Tk()
ventana.geometry("500x500+500+100")
ventana.config(bg="blue")
ventana.title("Ejemplo imagenes")
miimagen=PhotoImage(file='lienzo.PNG')
fondo=PhotoImage(file='lienzo.PNG')

boton=Button(ventana, image=miimagen).place(x=0,y=0)

lblFondo=Label(ventana,image=fondo).place(x=1,y=1)
lblImagen=Label(ventana,image=miimagen).place(x=50,y=50)

ventana.mainloop()