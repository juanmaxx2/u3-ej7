from docente import Docente
from investigador import Investigador
class DocenteInvestigador(Docente,Investigador):
    __CategoriaProgramaInvestigacion=None
    __ImporteExtra=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,area,tipo,carrera,cargo,catedra,categoriaprogramainvestigacion,importeExtra):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,area,tipo,carrera,cargo,catedra)
        self.__CategoriaProgramaInvestigacion=categoriaprogramainvestigacion
        self.__ImporteExtra=importeExtra

    def getCategoria(self):
        return self.__CategoriaProgramaInvestigacion
    def getImporte(self):
        return self.__ImporteExtra