from personal import Personal
class Investigador(Personal):
    __AreadeInvestigacion=None
    __TipodeInvestigacion=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,area,tipo):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__AreadeInvestigacion=area
        self.__TipodeInvestigacion=tipo
    
    def getArea(self):
        return self.__AreadeInvestigacion
    def getTipo(self):
        return self.__TipodeInvestigacion