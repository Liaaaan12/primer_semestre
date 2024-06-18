numero1 = int(input("Ingrese un numero:"))
numero2 = int(input("ingrese un segundo numero:"))
numero3 = int(input("Ingrese un tercer numero:"))
if numero1<numero2 and numero1<numero3 and numero2<numero3:
    print(f"Los numeros fueron ingresados en orden creciente: {numero1}, {numero2}, {numero3}")
else:
    print(f"Los numero no fueron ingresados en orden creciente: {numero1}, {numero2}, {numero3}")