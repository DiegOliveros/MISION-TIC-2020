# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:50:09 2021

@author: USUARIO
"""

import datetime

class Vehiculo:
    def __init__(self,placa):
        self.placa = placa
        self.ingreso = datetime.datetime.now()
    def info(self):
        t = "{:%d, %b %Y %H:%M}".format(self.ingreso)
        return f"El vehiculo con placa {self.placa}, fecha de ingreso: {t}"
    

class Moto(Vehiculo):
    precio = 0
    def __init__(self,placa):
        super().__init__(placa)
    def info(self):
        return f"Moto - {super().info()}"
    def pago(self):
        ahora = datetime.datetime.now()
        t = ahora - self.ingreso
        m = round(t.total_seconds()/60,2)
        p =  round(m * Moto.precio,2)
        return f"La Moto de placa {self.placa} lleva {m} minutos en el parqueadero \n TOTAL PAGAR: {p}$COP"
    
class Carro(Vehiculo):
    precio = 0
    def __init__(self,placa):
        super().__init__(placa)
    def info(self):
        return f"Carro - {super().info()}"
    def pago(self):
        ahora = datetime.datetime.now()
        t = ahora - self.ingreso
        m = round(t.total_seconds()/60,2)
        p =  round(m * Carro.precio,2)
        return f"El carro de placa {self.placa} lleva {m} minutos en el parqueadero \n TOTAL PAGAR: {p}$COP"
    
