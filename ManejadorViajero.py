import csv
from ViajeroFrecuente import ViajeroFrecuente

class ManejadorViajero:
    __listaViajeros=[]
    def __init__(self):
        self.__listaViajeros=[]
    def agregarViajero(self,viajero):
        if type(viajero)==ViajeroFrecuente:
            self.__listaViajeros.append(viajero)
        else:
            print('Error, no se pudo agregar un viajero a la lista, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='viajeros.csv'
        archivo=open(nombreArchivo)
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                self.agregarViajero(ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4])))
        archivo.close()
        print('Fin de la carga desde: ',nombreArchivo)
    def viajeroConMasMillas(self):
        iViajeroMayor=0
        for i in range(1,len(self.__listaViajeros)):
            if self.__listaViajeros[i]>self.__listaViajeros[iViajeroMayor]:
                iViajeroMayor=i
        return iViajeroMayor
    def viajerosConMasMillas(self):
        iViajero=self.viajeroConMasMillas()
        print('Viajeros con mas millas:')
        for viajero in self.__listaViajeros:
            if viajero==self.__listaViajeros[iViajero]:
                print(viajero)
    def test(self):
        print('Comienza test ManejadorViajero')
        manejador=ManejadorViajero()
        print('Metodo cargarDesdeArchivo()')
        manejador.cargarDesdeArchivo()
        print('Metodo agregarViajero()')
        manejador.agregarViajero('viajero')
        manejador.agregarViajero(ViajeroFrecuente(19,'38123123','Pedro','Fernandez',7300))
        manejador.agregarViajero(ViajeroFrecuente(88,'40123123','Juan','Frias',7300))
        print('Metodo viajeroConMasMillas()')
        print(manejador.viajeroConMasMillas())
        print('Metodo viajerosConMasMillas()')
        manejador.viajerosConMasMillas()
        print('Fin test ManejadorViajero. \n')