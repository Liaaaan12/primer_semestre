#Primera_clase
#print es una funcion que muestra por mantalla.

print("Hola mundo")#Estructura de salida.
print("""Esto me permite
escribir directamente en
mas de una linea """)#Con la triple comilla dentro de un print, esto me permite escribir hacia abajo sin darme error.

print("imprimir sin", end=" ")#El end me permite hacer algo similar a la triple comilla, pero puedo separarlo con un espacio o un guion(-).
print("saltar espacios")#con esto al imprimir, si me salta de linea, saltando espacios. 

#Separa un print con \n (\)
print("Separar con\n print")
print("Separar con\n\\n print")#Aqui me muestra el salto de linea mostrando por pantalla.


"""
Segunda parte de la clase
"""

print("Hola, dime tu nombre")
nombre=input() #El imput permite ingresar una variable por teclado.
print("Hola", nombre,"¿Cual es tu apellido")
apellido=input()
print("Tu nombre completo es:", nombre, apellido)
print("¿Que edad tienes?")
edad=input()
print("La edad de ",nombre, apellido, " es de", edad)

print(f""""" ******** Tus datos personales *********
NOMBRE:{nombre} {apellido}
EDAD:{edad}
********************************************""")

"""
Tercera parte de la clase
"""
#Suma pidiendo los datos por pantalla al usuario.
print("**************SUMA DE NUMEROS ENTEROS****************")
print("Ingrese un numero entero")
numero1=int(input())
print("Ingrese un segundo numero")
numero2=int(input())
suma=numero1+numero2
print(f"La suma de los numeros es: {suma}")

print("***********SUMA DE DECIMALES************")
dec1=float(input("ingrese un numero decimal: "))#Otra forma de preguntar una variavle de forma mas optimizada en codigo.
dec2=float(input("ingrese un segundo numero decimal: "))
print(f"La suma de los decimales es:{dec1+dec2}")

"""
Boolean datos
"""
a=True
b=False

print(a)
print(b)

print("Evaluando A AND B: ", a and b)
print("EVALUANDO A OR B: ", a or b)
print("Uso de negacion de A: ", not a)
