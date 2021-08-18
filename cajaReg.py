import os
from datetime import date as dt
caja_inicial= int(input('Caja Inicial: $'))
efectivo= 0
tarjeta = 0
retiro = 0
movimientos = 0
while caja_inicial >= 0:
    try:
        movimientos += 1
        print('1- Pago en Efectivo')
        print('2- Pago en Tarjeta')
        print('3- Retiro')
        print('4- Salir')
        option = input('Seleccione una opción: ')
        if option == '1':
            ft = int(input('Ingrese monto en efectivo: $'))
            efectivo += ft
        elif option == '2':
            tarj = int(input('Ingrese monto en Tarjeta: $'))
            tarjeta += tarj
        elif option == '3':
            ret = int(input('Ingrese monto a retirar: $'))
            retiro += ret
        elif option == '4':
            with open('Ventas.txt', 'a', encoding='utf8') as archivo:
                archivo.write(f'Día: {dt.today()}\nCaja inicial del día de hoy: ${caja_inicial}\nCantidad de Movimientos: {movimientos}\nVentas en Efectivo: ${efectivo}\nVentas con Tarjeta: ${tarjeta}\nRetiros: ${retiro}\nEfectivo del día en caja: ${efectivo-retiro}')
                break
        else:
            print('Elegí una opción correcta')

    except Exception:
        caja_inicial = True