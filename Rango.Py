cantidadInt = int(input('¿Cantidad de números?'))
contadorInt = 1
contadornumerosInt = 0
while contadorInt  <= cantidadInt:
    numeroInt = int(input('Ingrese un número -> '))
    if numeroInt >= 10 and numeroInt <=20:
        contadornumerosInt += 1
    contadorInt += 1 
print('La cantidad de números en el rango de 10 a 20 son: ', contadornumerosInt)
