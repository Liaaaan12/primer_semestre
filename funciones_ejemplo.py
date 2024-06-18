#Las funciones en python siempre van al principio del programa, ya que lee linea por linea, hacia abajo, por lo cual tenemos que crearlas antes de llamarlas al principio del codigo o antes de que sean llamadas.s


def puntuacion(clase):
    suma=sum(clase)
    suma=suma/len(clase)
    return suma
clase= [7, 8, 9]
media= puntuacion(clase)

print("La puntuacion de esta clase es: ",  media)

#Ejemplo de tabla de multiplicar

numero=2

def mostrar_linea(numero, linea):
    print(numero, "x", linea, "=>", numero * linea)

mostrar_linea(numero, 1)
mostrar_linea(numero, 2)
mostrar_linea(numero, 3)
mostrar_linea(numero, 4)
mostrar_linea(numero, 5)
mostrar_linea(numero, 6)
mostrar_linea(numero, 7)
mostrar_linea(numero, 8)
mostrar_linea(numero, 9)
mostrar_linea(numero, 10)