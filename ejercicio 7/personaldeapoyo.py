from personal import Personal
class PersonaldeApoyo(Personal):
    __Categoria=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__Categoria=categoria

    def __str__(self):
        return super().__str__()+self.__Categoria
    def getCategoria(self):
        return self.__Categoria
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                categoria=self.__Categoria
            )
        )
        return d
