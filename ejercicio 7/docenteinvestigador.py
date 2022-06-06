from docente import Docente
from investigador import Investigador
class DocenteInvestigador(Docente,Investigador):
    __CategoriaProgramaInvestigacion=None
    __ImporteExtra=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo,categoriaprogramainvestigacion,importeextra):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo)
        self.__CategoriaProgramaInvestigacion=categoriaprogramainvestigacion
        self.__ImporteExtra=importeextra

    def __str__(self):
        return super().__str__()+self.__CategoriaProgramaInvestigacion+self.__ImporteExtra
    def getCategoria(self):
        return self.__CategoriaProgramaInvestigacion
    def getImporte(self):
        return self.__ImporteExtra
    def getSueldo(self):
        return self._
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                categoriaprogramainvestigacion=self.__CategoriaProgramaInvestigacion,
                importeextra=self.__ImporteExtra
            )
        )
        return d