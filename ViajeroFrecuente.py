class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=0
    def __init__(self,numViajero=0,dni='',nombre='',apellido='',millas=0):
        self.__num_viajero=numViajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas
    def getMillas(self):
        return self.__millas_acum
    def __gt__(self,otroViajero):
        return self.__millas_acum> otroViajero.getMillas()
    def __eq__(self,otroViajero):
        return self.__millas_acum==otroViajero.getMillas()
    def __add__(self,numero):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum+numero)
    def __sub__(self,numero):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum-numero)
    def __str__(self):
        return 'Numero:{}, DNI:{}, Nombre:{}, Apellido:{}, Millas:{}'.format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    def test(self):
        print('Comienza test ViajeroFrecuente')
        viajero1=ViajeroFrecuente(1,'33222222','Pedro','Fernandez',900)
        viajero2=ViajeroFrecuente(2,'40555555','Camila','Gutierrez',1200)
        print('Metodo getMillas()')
        print(viajero1.getMillas())
        print(viajero2.getMillas())
        print(viajero1>viajero2)
        print(viajero1==viajero2)
        viajero3=viajero1+300
        viajero4=viajero2-1000
        print(viajero3)
        print(viajero4)
        print(viajero1)
        print(viajero2)
        print('Fin test ViajeroFrecuente. \n')