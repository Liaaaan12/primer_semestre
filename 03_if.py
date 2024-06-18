numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese un segundo numero entero: "))
numero3 = int(input("Ingrese un tercer numero entero: "))\

if numero1>numero2 and numero1 >numero3:
    print(f"El primer numero ingresado es el mayor: {numero1}")
elif numero2>numero3:
    print(f"El segundo numero ingresado es el mayor: {numero2}")
else:
    print(f"El tercer numero ingresado es el mayor: {numero3}")