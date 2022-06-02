class Personal:
    __Cuil=None
    __Apellido=None
    __Nombre=None
    __SueldoBasico=None
    __Antiguedad=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad):
        self.__Cuil=cuil
        self.__Apellido=apellido
        self.__Nombre=nombre
        self.__SueldoBasico=sueldobasico
        self.__Antiguedad=antiguedad
    
    def getCuil(self):
        return self.__Cuil
    def getApellido(self):
        return self.__Apellido
    def getNombre(self):
        return self.__Nombre
    def getSueldoBasico(self):
        return self.__SueldoBasico
    def getAntiguedad(self):
        return self.__Antiguedad