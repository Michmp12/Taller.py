codigoInt =int(input('Codigo'))
nombreStr = input('nombre')
existenciasInt = 0
controlBln = True
import os
while controlBln == True:
    os.system('cls')
    print('Codigo: ', codigoInt, '\nNombre: ', nombreStr,'\nExistencias: ', existenciasInt)
    opcionStr = input('1. Compras\n2. Ventas\n3. Reportes\n-> ')
    cantidadInt = int(input('Cantidad: '))
    if opcionStr == '1':
        existenciasInt += cantidadInt
    if opcionStr == '2':
        if cantidadInt <= existenciasInt:
            existenciasInt -= cantidadInt
        else: 
            print('Lo siento no hay suficientes existencias')
            enter = input('<ENTER>')
    if opcionStr == '3':
        print('Cantidad actual de inventario:', existenciasInt)
    if opcionStr == '4':
        controlBln = False