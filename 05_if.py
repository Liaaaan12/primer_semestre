numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese un segundo numero entero: "))

multiplo = numero1 % numero2
if multiplo == 0:
    print(f"El numero {numero1} si es multiplo de {numero2}")
else:
    print(f"El numero {numero1} no es multiplo de {numero2}")