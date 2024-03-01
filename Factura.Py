import os
os.system('cls')
var_PRECIOCOMPUTADOR = 2000000
var_PRECIOTABLETA = 1500000
var_PRECIOVIDEOBEAM = 120000
var_PRECIOTELEVISOR = 4500000


cantidad_computador = 0
cantidad_tableta = 0
cantidad_videobeam = 0
cantidad_televisor = 0
total_pagar = 0


nombre = input("Ingrese su nombre por favor: ")
contacto = input("Ingrese su número de contacto por favor: ")
direccion = input("Ingrese su dirección por favor: ")
var_controlBln = True
while var_controlBln == True:
    os.system('cls')
    
    print("\n1. Computador de escritorio")
    print("2. Tableta")
    print("3. Videobeam")
    print("4. Televisor")
    print("5. Facturar")
    
    opcion = input("Seleccione una opción de compra que desea: ")

    if opcion == "1":
        cantidad_computador += 1
        total_pagar += var_PRECIOCOMPUTADOR
        print("Se agregó un Computador de escritorio a la factura.")
    if opcion == "2":
        cantidad_tableta += 1
        total_pagar += var_PRECIOTABLETA
        print("Se agregó una Tableta a la factura.")
    if opcion == "3":
        cantidad_videobeam += 1
        total_pagar += var_PRECIOVIDEOBEAM
        print("Se agregó un Videobeam a la factura.")
    if opcion == "4":
        cantidad_televisor += 1
        total_pagar += var_PRECIOTELEVISOR
        print("Se agregó un Televisor a la factura.")
    if opcion == "5":
        print("\n Factura para:", nombre)
        print("Contacto:", contacto)
        print("Dirección:", direccion)
        print("\nFactura de la compra:")
        print("Computador de escritorio:", cantidad_computador)
        print("Tableta:", cantidad_tableta)
        print("Videobeam:", cantidad_videobeam)
        print("Televisor:", cantidad_televisor)
        print("Total a pagar:", total_pagar)
        print('Gracias por su compra, vuelva pronto.')
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")