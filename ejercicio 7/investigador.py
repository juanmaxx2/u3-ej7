from personal import Personal
class Investigador(Personal):
    __AreadeInvestigacion=None
    __TipodeInvestigacion=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,area,tipo,carrera="",cargo="",catedra=""):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__AreadeInvestigacion=area
        self.__TipodeInvestigacion=tipo
    
    def __str__(self):
        return super().__str__()+self.__AreadeInvestigacion+self.__TipodeInvestigacion
    def getArea(self):
        return self.__AreadeInvestigacion
    def getTipo(self):
        return self.__TipodeInvestigacion
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                area=self.__AreadeInvestigacion,
                tipo=self.__TipodeInvestigacion
            )
        )
        return d