import gestor_funciones as gf

gestor=gf.GestorFunciones()
while True:
        base_mostrar = input(
        """
        Ingrese opcion
        1. Añadir articulo
        2. Añadir detalles a un articulo determinado
        3. Eliminar articulo
        4. Eliminar detalle de un articulo 
        5. Mostrar articulos 
        6. Salir
        opcion: """)
        if base_mostrar =="1":
            gestor.añadir_articulos()
        elif base_mostrar =="2":
            gestor.añadir_detalles_articulos()
        elif base_mostrar=="3":
            gestor.eliminar_articulos()
        elif base_mostrar=="4":
            gestor.borrar_detalles_articulos()
        elif base_mostrar=="5":
            gestor.mostrar_articulos()
        elif base_mostrar=="6":
            break
        else:
            print("Opcion incorrecta")