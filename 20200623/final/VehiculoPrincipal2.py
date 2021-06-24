# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 17:48:27 2021

@author: USUARIO
"""

import datetime
import csv
from Vehiculo import *

class Parqueadero:
    def __init__(self,p,e,c,m):
       self.p = p
       self.e = e
       self.c = c
       Carro.precio = c
       self.m = m
       Moto.precio = m
       self.matriz = [[0] * e for i in range(p)] 

    def imprimirParqueadero(self):
         x = ""
         for i in range(len(self.matriz)):
                for j in range(len(self.matriz[0])):
                    if(self.matriz[i][j]==0):
                        x = x + f"Piso {i}, Espacio {j} -> Está vacío,\n"
                    else:                  
                        x = x + f"Piso {i}, Espacio {j} -> {self.matriz[i][j].info()},\n" 
         return x

    def imprimirVacios(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if(matriz[i][j]==0):
                    print(f"Piso {i}, Espacio {j} -> Está vacío")
                    
    def parquear(self,p,e,pl,t):
        try:
            if(self.matriz[p][e] == 0):      
                if(t == 1):
                    self.matriz[p][e] = Carro(pl)
                else:
                    self.matriz[p][e] = Moto(pl)
                return "Vehiculo creado con éxito"
            else:
                return "LUGAR NO DISPONIBLE"
        except IndexError:
            return "PISO Y ESPACIO INGRESADO NO EXISTE!!!!"
        
    def decargarArchivo(self):
        t = "{:%b%d%Y-%H-%M}".format(datetime.datetime.now())
        name = "Vehiculos-"+t
        filename = "%s.csv" % name
        with open(filename,'w',newline= '') as file:
            writer = csv.writer(file)
            for i in range(len(self.matriz)):
                for j in range(len(self.matriz[0])):
                    if(self.matriz[i][j]==0):
                        writer.writerow([f"Piso {i}, Espacio {j} -> Está vacío,\n"])
                    else:                  
                        writer.writerow([f"Piso {i}, Espacio {j} -> {self.matriz[i][j].info()},\n"])                    
        