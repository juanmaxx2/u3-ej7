class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=None

    def Iniciar(self,unManejador,encoder):
        while self.__opcion!='9':
            print('\n0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0')
            print('|                                                                                      |')
            print('0                                                                                      0')
            print('|     1.Insertar Agente.                                                               |')
            print('|     2.Agregar Agente.                                                                |')
            print('|     3.Mostrar tipo de agente en una posicion.                                        |')
            print('|     4.Mostrar Nombre de Docentes Investigadores que trabajan en una carrera.         |')
            print('|     5.Buscar docentes investigadores y investigadores pertenecientes a un area.      |')
            print('|     6.Mostrar datos de los agentes.                                                  |')
            print('|     7.                                                                               |')
            print('|     8.Guardar los datos de los agentes.                                              |')
            print('|     9.Salir                                                                          |')
            print('0                                                                                      0')
            print('|                                                                                      |')
            print('0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0 \n')
            self.__opcion=input('\nIngrese la opcion a realizar:')
            
            if int(self.__opcion)>=1 and int(self.__opcion)<=9:

                if self.__opcion=='1':
                    pos=input('\nIngrese la posicion en la que quiere ingresar el agente')
                    agente=unManejador.Iniciar()
                    unManejador.InsertarAgente(agente,pos)
                elif self.__opcion=='2':
                    agente=unManejador.Iniciar()
                    unManejador.AgregarAgente(agente)
                elif self.__opcion=='3':
                    pos=input('\nIngrese el posicion a mostrar el tipo de agente:')
                    unManejador.MostrarTipo(pos)
                elif self.__opcion=='4':
                    carrera=('\nIngrese el nombre de una carrera:')
                    unManejador.DICarrera(carrera)
                elif self.__opcion=='5':
                    area=input('\nIngrese el area a buscar:')
                    unManejador.ContarxArea(area)
                elif self.__opcion=='6':
                    unManejador.mostrar()
                elif self.__opcion=='7':
                    print('')
                elif self.__opcion=='8':
                    listaJSON=unManejador.guardarJSON()
                    encoder.guardarJSONArchivo(listaJSON,'personal.json')
                    print('Archivo guardado')
            else:print('Opcion incorrecta')
