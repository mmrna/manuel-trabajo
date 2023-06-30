#manuel hernandez 
import os
import numpy 
import time 

lista_opciones:[1,2,3,4]
lista__mascotas:[]
lista_rut_dueno:[]
lista_nombre:[]
lista_totales:[]

def mostrar_menú():
  print("""bienvenido a mascotas seguras
 menú
 1.grabar
 2.buscar
 3.retirarse
 4.salir""")
def validar_opcion():
    while True:
        try: 
            opc = int(input("ingrese una opcion"))
            if opc in (1,2,3,4):
                return opc
            else:
                print("!ERROR OPCION INCORRECTA¡")
        except :
            print ("!ERROR DEBE INGRESAR UN NUMERO¡")
            
    
def validar_rut():
    while True:
     try:
         rut = int(input("ingrese su rut"))
         if rut >= 10000000 and rut <=99999999:
             return rut 
         else:
             print ("!ERROR¡ RUT ENTRE 10000000 Y 99999999")
     except:
         print("ingrese un numero entero ")
         
def validar_nombre():
    while True:
        nom= input("ingrese su nombre: ")
        if len(nom.strip) >= 3 and nom.isalpha():
            return nom 
        else:
            print("ERROR DEBE TENER AL MENOS 3 LETRAS")
        
def validar_nombre_mascota():
    while True:
        nom= input("ingrese nombre de la mascota: ")
        if len(nom.strip) >= 3 and nom.isalpha():
            return nom 
        else:
            print("ERROR DEBE TENER AL MENOS 3 LETRAS")

def validar_habitacion():
    while True:
     try:
         habitacion = int(input("ingrese su rut"))
         if habitacion >= 1000000 and habitacion <=99999999:
             return habitacion
         else:
             print ("!ERROR¡ los dias ENTRE 10000000 Y 99999999")
     except:
         print("ingrese un numero entero ")   