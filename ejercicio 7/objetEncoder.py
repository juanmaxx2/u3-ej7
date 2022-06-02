import json
from pathlib import Path
class ObjectEncoder(object):

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                Personal=d['Personal']
                dPerosnal = Personal[0]
                manejador=class_()
                for i in range(len(Personal)):
                    dPerosnal=Personal[i]
                    class_name=dPerosnal.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPerosnal['__atributos__']
                    personal=class_(**atributos)
                    manejador.AgregarPersonal(personal)
            return manejador


    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)