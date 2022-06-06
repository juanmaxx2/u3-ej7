from importlib.util import set_loader
from personaldeapoyo import PersonaldeApoyo
from docente import Docente
from investigador import Investigador
from docenteinvestigador import DocenteInvestigador
from personal import Personal
from lista import Lista
class Manejador:
    __Lista=None

    def __init__(self):
        self.__Lista=Lista()

    def Iniciar():
        tipo=input('\nIngrese el tipo de agente: \n1.Personal de Apoyo\n2.Docente\n3.Investigador\n4.Docente Investigador\nIngrese el tipo de Agente:')
        if int(tipo)>=1 and int(tipo)<=4:
            print('\nPara el agente Ingrese:')
            if tipo=='1':
                Cuil=input('Ingrese el cuil:')
                Apellido=input('Ingrese el apellido:')
                Nombre=input('Ingrese el nombre')
                SueldoBasico=input('Ingrese el sueldo:')
                Antiguedad=input('Ingrese la antiguedad:')
                Categoria=input('Ingrese la categoria:')
                unPersonaldeApoyo=PersonaldeApoyo(Cuil,Apellido,Nombre,SueldoBasico,Antiguedad,Categoria)
                unAgente=unPersonaldeApoyo
            elif tipo=='2':
                Cuil=input('Ingrese el cuil:')
                Apellido=input('Ingrese el apellido:')
                Nombre=input('Ingrese el nombre')
                SueldoBasico=input('Ingrese el sueldo:')
                Antiguedad=input('Ingrese la antiguedad:')
                Carrera=input('Ingrese la carrera donde dicta clases:')
                Cargo=input('Ingrese el cargo:')
                Catedra=input('Ingrese la catedra:')
                unDocente=Docente(Cuil,Apellido,Nombre,SueldoBasico,Antiguedad,Carrera,Cargo,Catedra)
                unAgente=unDocente
            elif tipo=='3':
                Cuil=input('Ingrese el cuil:')
                Apellido=input('Ingrese el apellido:')
                Nombre=input('Ingrese el nombre')
                SueldoBasico=input('Ingrese el sueldo:')
                Antiguedad=input('Ingrese la antiguedad:')
                AreadeInvestigacion=input('Ingrese el area de Investigacion:')
                TipodeInvestigacion=input('Ingrese el tipo de Investigacion:')
                unInvestigador=Investigador(Cuil,Apellido,Nombre,SueldoBasico,Antiguedad,AreadeInvestigacion,TipodeInvestigacion)
                unAgente=unInvestigador
            elif tipo=='4':
                Cuil=input('Ingrese el cuil:')
                Apellido=input('Ingrese el apellido:')
                Nombre=input('Ingrese el nombre')
                SueldoBasico=input('Ingrese el sueldo:')
                Antiguedad=input('Ingrese la antiguedad:')
                Carrera=input('Ingrese la carrera donde dicta clases:')
                Cargo=input('Ingrese el cargo:')
                Catedra=input('Ingrese la catedra:')  
                AreadeInvestigacion=input('Ingrese el area de Investigacion:')
                TipodeInvestigacion=input('Ingrese el tipo de Investigacion:')
                CategoriaProgramaInvestigacion=input('Ingrese la categoria en el programa de incentivos de investigacion:')
                ImporteExtra=input('Ingrese el importe extra por docencia e investigacion:')
                unDocenteInvestigador=DocenteInvestigador(Cuil,Apellido,Nombre,SueldoBasico,Antiguedad,AreadeInvestigacion,TipodeInvestigacion,Carrera,Cargo,Catedra,CategoriaProgramaInvestigacion,ImporteExtra)
                unAgente=unDocenteInvestigador
        else:print('Numero equivocado')
        return unAgente

    def AgregarAgente(self,agente):
        self.__Lista.AgregarPersonal(agente)
    
    def InsertarAgente(self, agente,pos):
        self.__Lista.Insertar(agente,pos)

    def MostrarTipo(self,pos):
        self.__Lista.MostrarTipo(pos)

    def DICarrera(self,carrera):
        for dato in self.__Lista:
            if isinstance(dato,DocenteInvestigador):
                if carrera==dato.getCatedra():
                    print(dato)

    def ContarxArea(self,area):
        CantDI=0
        CantI=0
        for dato in self.__Lista:
            if isinstance(dato,DocenteInvestigador):
                if dato.getArea()==area:
                    CantDI+=1
            if isinstance(dato,Investigador):
                if dato.getArea()==area:
                    CantI+=1
        print('La cantidad de docente investigador es:{}'.format(CantDI))
        print('La cantdiad de investgadores en el area es:{}'.format(CantI))
    
    def Mostrar(self):
        for dato in self.__Lista:
            if isinstance(dato,PersonaldeApoyo):
                j='Personal de apoyo'
            if isinstance(dato,Investigador):
                j='Investigador'
            if isinstance(dato,Docente):
                j='Docente'
            if isinstance(dato,DocenteInvestigador):
                j='Docente investigador'
            print('para el agente: Nombre:{}, Apellido:{}, Tipo de Agente:{}, sueldo:{}'.format(dato.getNombre(), dato.getApellido(),j,dato.getSueldoBasico()))
        
    def MostrarCategoria(self,categoria):
        importe=0
        for dato in self.__Lista:
            if isinstance(dato, DocenteInvestigador):
                if dato.getCategoria().lower()==categoria.lower():
                    print(dato.getApellido())
                    print(dato.getNombre())
                    print(dato.getImporte())
                    importe+=dato.getImporte()
        print('El total de dinero que la Secretaría de Investigación debe solicitar al Ministerio es:{}'.format(importe))

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[Personal.toJSON() for Personal in self.__Lista]
        )
        return d
     
