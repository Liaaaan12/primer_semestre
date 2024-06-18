numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese un segundo numero: "))

print("""
(1)-Suma
(2)-Resta
(3)-Multiplicacion
(4)-Divicion
""")
eleccion= int(input("Elija el tipo de operacion aritmetica(Con los numeros al costado de ellos): "))
match eleccion:

    case 1:
        print(f"La suma de los numeros ingresados es de: {numero1+numero2}")
    case 2:
        print(f"La resta de los numeros ingresados es de: {numero1-numero2}")
    case 3:
        print(f"La multiplicacion de los numeros ingresados es de: {numero1*numero2}")
    case 4:
        print(f"La divicion de los numero ingresados son de: {numero1/numero2}")
    case other:
        print("El valor de ingresado no es valido")



"""
eleccion= int(input("Elija el tipo de operacion aritmetica(Con los numeros al costado de ellos): ")) 
if eleccion == 1:
    print(f"La suma de los numeros ingresados es de: {numero1+numero2}")
elif eleccion == 2:
    print(f"La resta de los numeros ingresados es de: {numero1-numero2}")
elif eleccion == 3:
    print(f"La multiplicacion de los numeros ingresados es de: {numero1*numero2}")
else:
    print(f"La divicion de los numero ingresados son de: {numero1/numero2}")
"""