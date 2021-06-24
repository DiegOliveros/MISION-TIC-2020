# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:31:46 2021

@author: diego
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:17:00 2021

@author: diego
"""

from tkinter import *
contador=0
base=Tk()
marco=Frame(base)
marco.pack()
def suma():
    global contador
    contador+=1
    texto.configure(text="Resultado: "+str(contador))
def resta():
    global contador
    contador-=1
    texto.configure(text="Resultado: "+str(contador))
def reseteo():
    global contador
    contador=0
    texto.configure(text="Resultado: "+str(contador))
    
def listaAutos(tamanio, posi,xy,hv): 
    lista=[]
    for i in range (posi,posi+tamanio):
        lista.append(Button(marco, text="Auto"+str(i), command=suma))
        lista[i-posi].grid(row=i*10, column=hv)
        
    return lista
    
listadeautosIzquierda=listaAutos(12,1,0,3) 
listadeautosAbajoV=listaAutos(4,13,0,2) 
listadeautosArribaV=listaAutos(4,17,0,0) 
listadeautosArribaH=listaAutos(5,21,0,2)
listadeautoscentro=listaAutos(4,26,1,1) 

    
texto=Label(marco, text="Resultado: "+str(contador))




base.mainloop()