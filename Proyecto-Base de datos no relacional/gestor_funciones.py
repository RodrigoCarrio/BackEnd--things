from platform import java_ver
from re import I
from turtle import back
import firebase_admin
import json
from firebase_admin import db

import GestorBaseDatos as gb

#conexion con base de datos
cred_obj = firebase_admin.credentials.Certificate('E:\\Analista en sistemas\\KEYS\\feria-virtual-1963d-firebase-adminsdk-uezr8-7bc94cd717.json')
databasesURL="https://feria-virtual-1963d-default-rtdb.firebaseio.com/"
default_app = firebase_admin.initialize_app(cred_obj, {	'databaseURL':databasesURL})

#creacion objeto gestor base de datos
gestorbd=gb.GestorBD()

ref=db.reference("/")
#ref1 = db.reference("/Articulos/") #Directorio RAIZ de areas LA 1° KEY SON LOS CODIGOS
#diccionario_items={}

class GestorFunciones():   
    def añadir_articulos(self):
        base_de_dato=gestorbd.obtener_base_de_dato()
        if base_de_dato == None:
            base_de_dato = {"AdminObject": "000"}
            while True:
                    nombre_articulo=input("Ingrese un articulo o salir para volver al manu: ").capitalize()
                    if nombre_articulo in base_de_dato:
                        print("Articulo ya registrado, ingrese otro articulo !")
                    elif nombre_articulo=="Salir":
                        return 
                    else:
                        base_de_dato.update({nombre_articulo: "null"})
                        gestorbd.insertar(ref,base_de_dato)
                        print(f"Se añadio el articulo {nombre_articulo} a la base de datos.")
                        return
        else:
            while True:
                nombre_articulo=input("Ingrese un articulo o salir para volver al manu: ").capitalize()
                if nombre_articulo in base_de_dato:
                    print("Articulo ya registrado")
                    return
                elif nombre_articulo=="Salir":
                    return 
                else:
                    base_de_dato.update({nombre_articulo: "null"})
                    gestorbd.insertar(ref,base_de_dato)
                    print(f"Se añadio el articulo {nombre_articulo} a la base de datos.")
                    return
          
    def eliminar_articulos(self):
        base_de_dato=gestorbd.obtener_base_de_dato()
        print(base_de_dato)       
        if base_de_dato == None:
            print("No hay datos para eliminar en la base.") 
        else:
            while True:
                articulo_a_eliminar=input("Ingrese el articulo que desea eliminar: ").capitalize()
                if articulo_a_eliminar=="Salir":
                    return
                elif articulo_a_eliminar in base_de_dato:
                    gestorbd.eliminar(ref,articulo_a_eliminar)
                    print(f"Se elimino el articulo {articulo_a_eliminar} de la base de datos. ")
                    break
                else:
                    print("El articulo que usted eligió no se encuentra cargada en la base de datos")
                    return  

    def añadir_detalles_articulos(self):
        base_de_dato = gestorbd.obtener_base_de_dato()
        while True:
            articulo_a_agregar_detalle = input("Ingrese un articulo registrado para agregar su detalle: ").capitalize()
            if articulo_a_agregar_detalle in base_de_dato:       
                clave = input(f"Ingrese el detalle de {articulo_a_agregar_detalle}: ").capitalize()       
                valor = input(f"Ingrese el valor de {clave}: ").capitalize()
                if not clave.isalpha(): #Permite no borrar el usuario admin
                    print("ERROR!!! Para el detalle ingrese unicamente LETRAS.")
                    return
                elif base_de_dato[articulo_a_agregar_detalle] == "null":
                    base_de_dato.update({articulo_a_agregar_detalle:{clave:valor}})
                    gestorbd.actualizar(ref, base_de_dato)
                    return
                else:               
                    if base_de_dato[articulo_a_agregar_detalle] == None:
                        base_de_dato.update({articulo_a_agregar_detalle:{clave:valor}})
                        gestorbd.actualizar(ref, base_de_dato)
                    else:
                        base_de_dato[articulo_a_agregar_detalle].update({clave:valor})
                        gestorbd.actualizar(ref, base_de_dato)
                    return
            elif articulo_a_agregar_detalle == "Salir":
                return
            else:
                print(f"El articulo {articulo_a_agregar_detalle} ingresado no se encuentra!")
                return

            

    def borrar_detalles_articulos(self):
        base_de_dato=gestorbd.obtener_base_de_dato()
        while True:
            print(base_de_dato)
            articulo=input("Ingrese un articulo registrado para eliminar su detalle: ").capitalize()
            if articulo in base_de_dato:
                detalle_a_eliminar=input(f"Ingrese el DETALLE de {articulo} que desea eliminar: ").capitalize()
                for i in base_de_dato:
                    if i==articulo:                      
                        for j in base_de_dato[i].keys():
                            if j == detalle_a_eliminar:
                                ref_a=db.reference(articulo)
                                gestorbd.eliminar(ref_a,detalle_a_eliminar)                        
                                print(f"Se elimino el detalle {detalle_a_eliminar} del articulo {articulo}")                               
                                return
                            """else:
                                print(f"El detalle {detalle_a_eliminar} no se encuentra dentro de {articulo}")
                                return """                             
            elif articulo=="Salir":
                break
            else:
                print(f"El articulo {articulo} ingresado no se encuentra, ingrese otro!")

    def mostrar_articulos(self):
        base_de_dato=gestorbd.obtener_base_de_dato()
        for i, j in base_de_dato.items():
            print(f"Articulo: {i} - Detalles: {j}")