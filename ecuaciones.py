from math import sqrt

print('Programa para calcular las soluciones de una ecuación de segundo grado')

respuesta = 'S'
while respuesta == 'S':

    a = float(input('Valor de a: '))
    b = float(input('Valor de b: '))
    c = float(input('Valor de c: '))

    if a == 0:
        print('No es una ecuación de segundo grado')
    else:
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            print('No hay soluciones reales')
        else:
            x1 = (-b + sqrt(discriminante)) / (2 * a)
            x2 = (-b - sqrt(discriminante)) / (2 * a)
            if x1 == x2:
                print('Solución: x1 =', round(x1, 2))
            else:
                print('Soluciones: x1 =', round(x1, 2), 'y x2 =', round(x2, 2))
    respuesta = input('¿Quieres resolver otra ecuación? [S/N] ')
    while respuesta not in 'SN':
        respuesta = input('¿Quieres resolver otra ecuación? [S/N] ')
        
        