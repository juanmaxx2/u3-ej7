from personal import Personal
class Docente(Personal):
    __Carrera=None
    __Cargo=None
    __Catedra=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__Carrera=carrera
        self.__Cargo=cargo
        self.__Catedra=catedra
    
    def getCarrera(self):
        return self.__Carrera
    def getCargo(self):
        return self.__Cargo
    def getCatedra(self):
        return self.__Catedra