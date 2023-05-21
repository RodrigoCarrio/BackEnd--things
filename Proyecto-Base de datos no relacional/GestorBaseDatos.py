from firebase_admin import db

class GestorBD:
    #GESTOR DE LA BASE DE DATOS

    def insertar(self,ref,data): #inserta datos en la base de datos
        try:
            ref.set(data)
        except Exception as e:
            print(e)

    def obtener_base_de_dato(self):
        #Me conecto a la base de datos
        ref = db.reference("/")
        #Obtengo la base de datos, get
        base_de_dato = ref.get()
        return base_de_dato
    
    def actualizar(self,ref, data): #quiero actulizar datos de la base de datos
        ref.update(data)
    
    def eliminar(self,ref,datos): #ELIMINA LOS DATOS DE LA BD de FIREBASE
        try:
            base_de_dato=ref.get()
            for key, value in base_de_dato.items():
                if key==datos:
                    ref.child(key).set({})
        except Exception as e: 
            print(e)
 