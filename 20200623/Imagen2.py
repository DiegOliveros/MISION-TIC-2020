# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:26:11 2021

@author: diego
"""

from tkinter import * 
from PIL import ImageTk, Image

ventana =Tk()
ventana.geometry("500x500+500+100")
ventana.config(bg="blue")
ventana.title("Ejemplo imagenes")

#miimagen=PhotoImage(file='lienzo.PNG')
#fondo=PhotoImage(file='lienzo.PNG')
miimagen=ImageTk.PhotoImage(Image.open("carro.jpg").resize((30,90)))
miimagen2=ImageTk.PhotoImage(Image.open("ico.ico").resize((30,90)))
boton1=Button(ventana, image=miimagen).place(x=0,y=0)
boton2=Button(ventana, image=miimagen2).place(x=50,y=0)
boton3=Button(ventana, image=miimagen).place(x=100,y=0)
boton4=Button(ventana, image=miimagen).place(x=150,y=0)
ventana.mainloop()