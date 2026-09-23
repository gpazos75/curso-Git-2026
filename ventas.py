# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:05:45 2024

@author: Gustavo Pazos
"""

# Dependencias necesarias
from datetime import date

# FUNCIONES
import fc_menu as m
import fc_ventas as v
import fc_consultas as c

# MENÚ PRINCIPAL
m.bienvenida()
opcion = m.opcion_menu() 

# PROGRAMA
while opcion > 0:
    if opcion==1:
        v.form_venta()
        opcion = m.opcion_menu()
    
    elif opcion==2:
        lista_ventas = c.csv_a_lista()
                            
        # Consulta de ganancias por rango de fechas
        try:
            fecha1 = input("Ingresar fecha inicial en formato aaaa-mm-dd: ")
            f1 = date.fromisoformat(fecha1)
        except ValueError:
            print("Ingresar la fecha en formato aaaa-mm-dd\n")
            fecha1 = input("Ingresar fecha inicial en formato aaaa-mm-dd: ")
            f1 = date.fromisoformat(fecha1)
            
        try:
            fecha2 = input("Ingresar fecha final en formato aaaa-mm-dd: ")
            f2 = date.fromisoformat(fecha2)
                 
        except ValueError:
            print("Ingresar la fecha en formato aaaa-mm-dd\n")
            fecha2 = input("Ingrese fecha final en formato aaaa-mm-dd: ")
            f2 = date.fromisoformat(fecha2)
            
        if f2 < f1:
            print("## Error ## La fecha inicial no puede ser mayor que la fecha final")
            print("Reingresar las fechas")
            
        else: 
            ganancia = c.sumar_ganancias(f1,f2,lista_ventas)
            print(f"\nLas ventas del período totalizaron ${ganancia}\n") 
            print(f"{c.ventas_del_periodo(f1,f2,lista_ventas)}")
            
        opcion = m.opcion_menu()
    
    elif opcion==3: 
        break
    
    else:    
        print("Ingresar una opción válida\n")
        opcion = m.opcion_menu()

    
 # Agrego comentario de prueba   