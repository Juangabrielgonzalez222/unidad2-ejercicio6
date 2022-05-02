from ManejadorViajero import ManejadorViajero
from ViajeroFrecuente import ViajeroFrecuente

if __name__== '__main__':
    manejador=ManejadorViajero()
    manejador.cargarDesdeArchivo()
    manejador.viajerosConMasMillas()
    viajero1=ViajeroFrecuente(14,33555555,'Luis','Gonzalez',1000)
    viajero2=ViajeroFrecuente(122,39883123,'Miguel','Sanders',1000)
    print('Viajeros:')
    print(viajero1)
    print(viajero2)
    print('---Acumular Millas---')
    viajeroNuevo=viajero1+500
    viajeroNuevo2=viajero2+600
    print(viajeroNuevo)
    print(viajeroNuevo2)
    print('---Canjear Millas---')
    viajeroNuevo3=viajeroNuevo-300
    viajeroNuevo4=viajeroNuevo2-400
    print(viajeroNuevo3)
    print(viajeroNuevo4)
    manejador.test()
    viajero1.test()