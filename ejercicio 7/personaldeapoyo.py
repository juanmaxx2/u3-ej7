from personal import Personal
class PersonaldeApoyo(Personal):
    __Categoria=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__Categoria=categoria

    def getCategoria(self):
        return self.__Categoria
