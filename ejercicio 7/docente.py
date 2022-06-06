from personal import Personal
class Docente(Personal):
    __Carrera=None
    __Cargo=None
    __Catedra=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area="",tipo=""):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,area,tipo)
        self.__Carrera=carrera
        self.__Cargo=cargo
        self.__Catedra=catedra
    
    def __str__(self):
        return super().__str__()+self.__Carrera+self.__Cargo+self.__Catedra
    def getCarrera(self):
        return self.__Carrera
    def getCargo(self):
        return self.__Cargo
    def getCatedra(self):
        return self.__Catedra
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                carrera=self.__Carrera,
                cargo=self.__Catedra,
                catedra=self.__Catedra
            )
        )
        return d