# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:08:41 2024

@author: Gustavo
"""
#Es necesario importar las depencendias necesarias
from datetime import date
#from datetime import datetime

#Fecha actual
#now = datetime.now()

print(today)
#print(now)


# Registro de una venta
def venta(planta, cantidad, precio, obs):
    today = date.today()    # fecha actual
    venta = list(planta, cantidad, precio, obs)
    venta.insert(0, today)
    return venta

    
planta=input("Especie: ")    
cantidad=int(input("Cantidad: "))      
precio=int(input("Monto: "))
obs=input("Observaciones: ")    

nueva_venta = venta(planta, cantidad, precio, obs)

#- Guardar nueva_venta en un archivo (append) 

# CONSULTAR ventas del día

#- Abrir el archivo de ventas y hacer una consulta por fecha usando
# if sobre el campo timestamp
date.today()==today


# Registro de una gasto
def gasto(item, cantidad, precio, obs):
    gasto = list(item, cantidad, precio, obs)
    gasto.insert(0, "agregar timestamp")
    
item=input("Producto")    
cantidad=int(input("Cantidad"))      
precio=int(input("Precio"))
obs=input("Observaciones")    

gasto(item, cantidad, precio, obs)

# STOCK: debe importarse de un archivo (modo append?) para que no se 
# reinicie cada vez que abrimos el programa
# El formato debe ser: planta, cantidad
stock = dict() #Construido de importar el csv

planta=input("Especie")
cantidad=int(input("Cantidad"))

# Para agregar una planta que no está en el diccionario
def agregar_planta(planta, stock) :
    #diccio = contar_palabras(texto)
    if planta in stock : stock[planta] += cantidad
    else: stock[planta] = cantidad
    return(stock)

# Para restar una planta por muerte o venta
def restar_planta(planta, stock) :
    #diccio = contar_palabras(texto)
    if planta in stock : stock[planta] -= cantidad
    else: print("Error: la especie no está registrada en el stock")
    return(stock)

#- Actualizar el archivo stock




